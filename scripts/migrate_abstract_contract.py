#!/usr/bin/env python3
"""Migrate historical literature records away from the old misleading summary field."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MEMORY = ROOT / "research-memory" / "literature"
DETAILS = ROOT / "web" / "data" / "paper-details"
BAD_MARKERS = ("提供机器人", "涉及 ADC", "摘要可核实数值", "当前未从摘要提取")


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def migrate_paper(paper: dict[str, Any]) -> None:
    original = str(paper.get("source_abstract") or paper.get("abstract_original") or "")
    paper["abstract_original"] = original
    paper.setdefault("source_abstract", original)
    translation = str(paper.get("abstract_translation_zh") or "")
    summary = str(paper.get("abstract_summary_zh") or "")
    if not summary or any(marker in summary for marker in BAD_MARKERS):
        summary = "待基于原文摘要生成中文总结；当前仅完成题录/摘要级筛选。"
    paper["abstract_translation_zh"] = translation
    paper["abstract_summary_zh"] = summary
    paper["summary_zh"] = summary
    paper["abstract_translation_status"] = (
        "agent_reviewed" if translation else ("pending_agent_translation" if original else "missing_source_abstract")
    )
    paper.setdefault("abstract_source", paper.get("url", ""))
    paper.setdefault(
        "source_access",
        {
            "doi_landing": f"https://doi.org/{paper['doi']}" if paper.get("doi") else "",
            "publisher_url": paper.get("url", ""),
            "candidate_urls": list(paper.get("pdf_candidates") or []),
            "successful_url": paper.get("pdf_source_url", ""),
            "failure_reasons": [],
        },
    )


def migrate_detail(detail: dict[str, Any], paper: dict[str, Any] | None = None) -> None:
    abstract = detail.setdefault("abstract", {})
    original = str(abstract.get("original") or (paper or {}).get("source_abstract") or "")
    translation = str(abstract.get("translation_zh") or "")
    legacy = str(abstract.get("zh") or "")
    if not translation and legacy and not legacy.startswith("等待") and not any(marker in legacy for marker in BAD_MARKERS):
        translation = legacy
    if any(marker in translation for marker in BAD_MARKERS):
        translation = ""
    summary = str(abstract.get("summary_zh") or (paper or {}).get("abstract_summary_zh") or "")
    if not summary or any(marker in summary for marker in BAD_MARKERS):
        summary = "待基于原文摘要生成中文总结；当前仅完成题录/摘要级筛选。"
    abstract.update({"original": original, "translation_zh": translation, "summary_zh": summary, "zh": translation})
    detail["source_access"] = detail.get("source_access") or (paper or {}).get("source_access", {})
    detail.setdefault("source_access_notes", (paper or {}).get("source_access_notes", ""))
    points = detail.get("innovation_points") or []
    if points and "relevance_reasons" not in detail:
        detail["innovation_points"] = points[:1]
        detail["relevance_reasons"] = points[1:]


def main() -> None:
    paper_by_id: dict[str, dict[str, Any]] = {}
    for path in MEMORY.glob("*/*/summaries/papers.json"):
        payload = read_json(path)
        for paper in payload.get("papers", []):
            migrate_paper(paper)
            paper_by_id[paper.get("id", "")] = paper
        write_json(path, payload)
    for path in DETAILS.glob("*.json"):
        detail = read_json(path)
        migrate_detail(detail, paper_by_id.get(detail.get("id", "")))
        write_json(path, detail)
    print(f"Migrated {len(paper_by_id)} paper records and historical detail bundles.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Build the web-facing research bundle from the GitHub memory store."""

from __future__ import annotations

import json
import os
from datetime import date
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MEMORY = ROOT / "research-memory"
WEB_DATA = ROOT / "web" / "data"


def read_text(path: Path, fallback: str = "") -> str:
    return path.read_text(encoding="utf-8") if path.exists() else fallback


def read_json(path: Path, fallback: Any) -> Any:
    if not path.exists():
        return fallback
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    os.replace(temporary, path)


def literature_days() -> list[Path]:
    literature = MEMORY / "literature"
    if not literature.exists():
        return []
    days = []
    for path in literature.glob("*/*"):
        if not path.is_dir():
            continue
        try:
            date.fromisoformat(path.name)
        except ValueError:
            continue
        days.append(path)
    return sorted(days, key=lambda item: item.name, reverse=True)


def report_history(days: list[Path]) -> list[dict[str, Any]]:
    history = []
    for day in days[:90]:
        papers_payload = read_json(day / "summaries" / "papers.json", {"papers": []})
        papers = papers_payload.get("papers", [])
        history.append(
            {
                "date": day.name,
                "paper_count": len(papers),
                "idea_count": len(papers_payload.get("generated_ideas", [])),
                "top_score": max((paper.get("relevance_score", 0) for paper in papers), default=0),
                "report_markdown": read_text(day / "daily-report.md"),
                "query_log": papers_payload.get("query_log", []),
                "source_errors": papers_payload.get("source_errors", []),
            }
        )
    return history


def build_bundle(preferred_date: date | None = None) -> dict[str, Any]:
    days = literature_days()
    selected = None
    if preferred_date:
        selected = next((path for path in days if path.name == preferred_date.isoformat()), None)
    if selected is None and days:
        selected = days[0]

    papers_payload = {"papers": [], "query_log": [], "source_errors": []}
    daily_report = "# 暂无文献日报\n\n运行今日检索后，这里会显示与研究画像匹配的论文。\n"
    selected_date = ""
    if selected:
        selected_date = selected.name
        papers_payload = read_json(selected / "summaries" / "papers.json", papers_payload)
        daily_report = read_text(selected / "daily-report.md", daily_report)

    ideas = read_json(MEMORY / "ideas" / "idea-log.json", {"ideas": []})
    decisions = read_json(MEMORY / "decisions" / "decision-log.json", {"decisions": []})
    tasks = read_json(MEMORY / "tasks" / "task-board.json", {"tasks": []})
    proposals = read_json(
        MEMORY / "profile-update-proposals" / "proposals.json", {"proposals": []}
    )
    profile = read_text(MEMORY / "profile" / "user-research-profile.md")
    history = report_history(days)
    paper_items = papers_payload.get("papers", [])
    idea_items = ideas.get("ideas", [])
    proposal_items = proposals.get("proposals", [])

    return {
        "schema_version": 2,
        "updated_at": date.today().isoformat(),
        "latest_report_date": selected_date,
        "profile_markdown": profile,
        "daily_report_markdown": daily_report,
        "papers": paper_items,
        "query_log": papers_payload.get("query_log", []),
        "source_errors": papers_payload.get("source_errors", []),
        "ideas": idea_items,
        "decisions": decisions.get("decisions", []),
        "tasks": tasks.get("tasks", []),
        "profile_proposals": proposal_items,
        "reports": history,
        "assets": {
            "hero_image2": (ROOT / "web" / "assets" / "tactile-front-end-image2.webp").exists(),
            "icon_image2": (ROOT / "web" / "assets" / "research-intelligence-icon-image2.png").exists(),
        },
        "stats": {
            "papers_today": len(paper_items),
            "must_read": sum(1 for item in paper_items if item.get("relevance_score", 0) >= 80),
            "pending_ideas": sum(1 for item in idea_items if item.get("status") in {"candidate", "watch", "proposed"}),
            "pending_proposals": sum(1 for item in proposal_items if item.get("status") == "pending"),
            "open_tasks": sum(1 for item in tasks.get("tasks", []) if item.get("status") not in {"done", "cancelled"}),
        },
    }


def refresh_bundle(preferred_date: date | None = None) -> dict[str, Any]:
    bundle = build_bundle(preferred_date)
    write_json(WEB_DATA / "research-bundle.json", bundle)
    return bundle


def main() -> None:
    refresh_bundle()
    print(f"Wrote {WEB_DATA / 'research-bundle.json'}")


if __name__ == "__main__":
    main()

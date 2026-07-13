#!/usr/bin/env python3
"""Build local research-intelligence data files for the web dashboard."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MEMORY = ROOT / "research-memory"
WEB_DATA = ROOT / "web" / "data"


def read_text(path: Path, fallback: str = "") -> str:
    if not path.exists():
        return fallback
    return path.read_text(encoding="utf-8")


def read_json(path: Path, fallback: dict) -> dict:
    if not path.exists():
        return fallback
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def ensure_daily_seed(today: date) -> tuple[Path, Path]:
    day_dir = MEMORY / "literature" / str(today.year) / today.isoformat()
    summaries = day_dir / "summaries"
    papers_path = summaries / "papers.json"
    report_path = day_dir / "daily-report.md"
    summaries.mkdir(parents=True, exist_ok=True)

    if not papers_path.exists():
        write_json(
            papers_path,
            {
                "date": today.isoformat(),
                "query_log": [
                    {
                        "source": "workflow-seed",
                        "query": "analog tactile preprocessing OR in-sensor computing tactile sensor",
                        "result_count": 0,
                    }
                ],
                "papers": [],
            },
        )

    if not report_path.exists():
        report_path.write_text(
            "\n".join(
                [
                    f"# {today.isoformat()} 每日文献报告",
                    "",
                    "今日自动任务尚未写入真实检索结果。",
                    "",
                    "## 建议关键词",
                    "",
                    "- analog tactile preprocessing",
                    "- programmable physical tactile projection",
                    "- vector tactile sensing",
                    "- fault-tolerant electronic skin",
                ]
            )
            + "\n",
            encoding="utf-8",
        )

    return papers_path, report_path


def build_bundle(today: date) -> dict:
    papers_path, report_path = ensure_daily_seed(today)
    ideas = read_json(MEMORY / "ideas" / "idea-log.json", {"ideas": []})
    decisions = read_json(MEMORY / "decisions" / "decision-log.json", {"decisions": []})
    tasks = read_json(MEMORY / "tasks" / "task-board.json", {"tasks": []})
    papers = read_json(papers_path, {"papers": [], "query_log": []})
    profile = read_text(MEMORY / "profile" / "user-research-profile.md")
    report = read_text(report_path)

    return {
        "updated_at": today.isoformat(),
        "profile_markdown": profile,
        "daily_report_markdown": report,
        "papers": papers.get("papers", []),
        "query_log": papers.get("query_log", []),
        "ideas": ideas.get("ideas", []),
        "decisions": decisions.get("decisions", []),
        "tasks": tasks.get("tasks", []),
    }


def main() -> None:
    today = date.today()
    bundle = build_bundle(today)
    write_json(WEB_DATA / "research-bundle.json", bundle)
    print(f"Wrote {WEB_DATA / 'research-bundle.json'}")


if __name__ == "__main__":
    main()

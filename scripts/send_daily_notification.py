#!/usr/bin/env python3
"""Send the latest literature briefing through optional user-configured channels."""

from __future__ import annotations

import argparse
import html
import json
import os
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MEMORY = ROOT / "research-memory"


def read_json(path: Path, fallback: Any) -> Any:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else fallback


def latest_day(requested: str = "") -> Path | None:
    if requested:
        path = MEMORY / "literature" / requested[:4] / requested
        return path if path.exists() else None
    days = sorted(
        (path for path in (MEMORY / "literature").glob("*/*") if path.is_dir()),
        key=lambda item: item.name,
        reverse=True,
    )
    return days[0] if days else None


def build_message(day: Path) -> tuple[str, str, str]:
    payload = read_json(day / "summaries" / "papers.json", {"papers": [], "generated_ideas": []})
    papers = payload.get("papers", [])
    title = f"{day.name} 柔性电子皮肤文献日报"
    targeted = [
        paper
        for paper in papers
        if any(str(query_id).startswith("venue-") for query_id in paper.get("query_ids", []))
    ]
    selected = targeted[:5]
    selected_ids = {paper.get("id") for paper in selected}
    selected.extend(paper for paper in papers if paper.get("id") not in selected_ids)
    selected = selected[:5]
    lines = []
    for index, paper in enumerate(selected, 1):
        detail_path = ROOT / "web" / str(paper.get("detail_json") or "")
        detail = read_json(detail_path, {}) if detail_path.is_file() else {}
        link = (
            "https://chenlongnb1-sudo.github.io/flexible-sensor-literature/"
            f"paper.html?id={urllib.parse.quote(str(paper.get('id') or ''))}"
        )
        lines.append(f"{index}. [{paper.get('venue') or '期刊待核验'}] {paper.get('title', '')}")
        abstract = (detail.get("abstract") or {}).get("zh")
        lines.append(f"摘要：{abstract or paper.get('summary_zh') or paper.get('core_claim') or '待精读'}")
        innovations = detail.get("innovation_points") or [
            paper.get("core_claim", ""), *paper.get("relevance_reasons", [])
        ]
        innovations = [item for item in innovations if item][:2]
        if innovations:
            lines.append(f"创新点：{'；'.join(innovations)}")
        inspirations = detail.get("inspirations") or paper.get("transferable_points", [])
        inspirations = [item for item in inspirations if item][:2]
        if inspirations:
            lines.append(f"对你的启发：{'；'.join(inspirations)}")
        lines.append(f"详情：{link}")
        lines.append("")
    if not papers:
        lines.append("今日没有达到门槛的新论文，系统未用偏题结果凑数。")
    plain = "\n".join(lines)
    html_content = "<br>".join(html.escape(line) for line in lines)
    return title, plain, html_content


def post_json(url: str, payload: dict[str, Any]) -> dict[str, Any]:
    request = urllib.request.Request(
        url,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json", "User-Agent": "ResearchIntelligence/1.0"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=25) as response:
        return json.loads(response.read().decode("utf-8", errors="replace") or "{}")


def notify_pushplus(token: str, title: str, html_content: str) -> None:
    post_json(
        "https://www.pushplus.plus/send",
        {"token": token, "title": title, "content": html_content, "template": "html"},
    )


def notify_serverchan(key: str, title: str, plain: str) -> None:
    url = f"https://sctapi.ftqq.com/{urllib.parse.quote(key)}.send"
    data = urllib.parse.urlencode({"title": title, "desp": plain}).encode("utf-8")
    request = urllib.request.Request(url, data=data, method="POST")
    with urllib.request.urlopen(request, timeout=25) as response:
        response.read()


def notify_bark(url: str, title: str, plain: str) -> None:
    post_json(url, {"title": title, "body": plain, "group": "科研情报"})


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", default="")
    args = parser.parse_args()
    day = latest_day(args.date)
    if day is None:
        print("No daily report found; notification skipped.")
        return 0
    title, plain, html_content = build_message(day)
    channels = []
    failures = []
    configured = [
        ("PushPlus", os.environ.get("PUSHPLUS_TOKEN", ""), lambda value: notify_pushplus(value, title, html_content)),
        ("ServerChan", os.environ.get("SERVERCHAN_SENDKEY", ""), lambda value: notify_serverchan(value, title, plain)),
        ("Bark", os.environ.get("BARK_URL", ""), lambda value: notify_bark(value, title, plain)),
    ]
    for name, value, sender in configured:
        if not value:
            continue
        try:
            sender(value)
            channels.append(name)
        except Exception as error:  # noqa: BLE001 - one notification channel must not block archiving
            failures.append(f"{name}: {type(error).__name__}: {error}")
    if channels:
        print(f"Notification sent via {', '.join(channels)}")
    else:
        print("No notification secret configured; report remains available in Codex/GitHub/web.")
    for failure in failures:
        print(f"Notification warning: {failure}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

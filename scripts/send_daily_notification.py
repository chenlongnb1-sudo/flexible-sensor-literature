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
    ideas = payload.get("generated_ideas", [])
    title = f"{day.name} 柔性电子皮肤文献日报"
    lines = [
        f"今日筛选 {len(papers)} 篇，创新点候选 {len(ideas)} 个。",
        "",
        "优先论文：",
    ]
    for index, paper in enumerate(papers[:3], 1):
        link = paper.get("url") or (f"https://doi.org/{paper.get('doi')}" if paper.get("doi") else "")
        lines.append(f"{index}. {paper.get('title', '')}（{paper.get('relevance_score', 0)} 分）")
        if link:
            lines.append(link)
    if not papers:
        lines.append("今日没有达到门槛的新论文，系统未用偏题结果凑数。")
    lines.extend(["", "打开网页处理 idea 和画像提案。"])
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

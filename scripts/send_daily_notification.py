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
    title = f"{day.name} 柔性电子高水平文献日报"
    selected = sorted(
        papers,
        key=lambda paper: (
            bool(paper.get("strongly_related")),
            int(paper.get("relevance_score") or 0),
            str(paper.get("date") or ""),
        ),
        reverse=True,
    )
    strong_count = sum(bool(paper.get("strongly_related")) for paper in selected)
    lines = [f"共 {len(selected)} 篇，强相关 {strong_count} 篇。", ""] if selected else []
    current_category = ""
    for index, paper in enumerate(selected, 1):
        detail_path = ROOT / "web" / str(paper.get("detail_json") or "")
        detail = read_json(detail_path, {}) if detail_path.is_file() else {}
        link = (
            "https://chenlongnb1-sudo.github.io/flexible-sensor-literature/"
            f"paper.html?id={urllib.parse.quote(str(paper.get('id') or ''))}"
        )
        category = paper.get("primary_category") or detail.get("primary_category") or "柔性材料与器件"
        if category != current_category:
            lines.append(f"【{category}】")
            current_category = category
        relation = "强相关" if paper.get("strongly_related") else "相关"
        lines.append(f"{index}. [{relation}｜{paper.get('venue') or '期刊待核验'}] {paper.get('title', '')}")
        abstract = (detail.get("abstract") or {}).get("zh")
        lines.append(f"摘要：{abstract or paper.get('summary_zh') or paper.get('core_claim') or '待精读'}")
        innovations = [
            item
            for item in (detail.get("innovation_points") or paper.get("relevance_reasons", []))
            if item and any("\u4e00" <= char <= "\u9fff" for char in str(item))
        ][:2]
        if innovations:
            lines.append(f"论文创新：{'；'.join(innovations)}")
        suggestions = detail.get("innovation_suggestions") or paper.get("innovation_suggestions", [])
        if paper.get("strongly_related") and suggestions:
            lines.append(f"给你的创新建议：{'；'.join(suggestions[:2])}")
        inspirations = [
            item
            for item in (detail.get("inspirations") or paper.get("transferable_points", []))
            if item and item not in suggestions
        ][:2]
        if inspirations:
            lines.append(f"对你的启发：{'；'.join(inspirations)}")
        lines.append(f"详情：{link}")
        lines.append("")
    if not papers:
        lines.append("今日没有达到期刊与柔性电子主题双重门槛的新论文。")
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

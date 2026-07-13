#!/usr/bin/env python3
"""Transactional mutations for the GitHub-backed research memory store."""

from __future__ import annotations

import json
import os
import re
import subprocess
import threading
import uuid
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

try:
    from .build_research_intelligence import MEMORY, ROOT, refresh_bundle
except ImportError:
    from build_research_intelligence import MEMORY, ROOT, refresh_bundle


LOCK = threading.RLock()
ALLOWED_ID = re.compile(r"^[A-Za-z0-9_.:-]+$")
IDEA_ACTIONS = {"watch", "reject", "convert_to_task", "propose_profile"}
PAPER_ACTIONS = {"read", "skim", "ignore", "add_to_ideas"}
PROPOSAL_ACTIONS = {"accept", "watch", "reject"}


class StoreError(ValueError):
    """Raised for invalid or impossible user decisions."""


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


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


def valid_id(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value or not ALLOWED_ID.fullmatch(value):
        raise StoreError(f"invalid {label}")
    return value


def find_item(items: list[dict[str, Any]], item_id: str, label: str) -> dict[str, Any]:
    item = next((candidate for candidate in items if candidate.get("id") == item_id), None)
    if item is None:
        raise StoreError(f"{label} not found: {item_id}")
    return item


def append_decision(
    *, item_type: str, item_id: str, decision: str, note: str = "", metadata: dict[str, Any] | None = None
) -> dict[str, Any]:
    path = MEMORY / "decisions" / "decision-log.json"
    payload = read_json(path, {"updated_at": "", "decisions": []})
    entry = {
        "id": f"decision-{datetime.now().strftime('%Y%m%d%H%M%S')}-{uuid.uuid4().hex[:6]}",
        "type": item_type,
        "item_id": item_id,
        "decision": decision,
        "note": note.strip()[:1000],
        "created_at": utc_now(),
    }
    if metadata:
        entry["metadata"] = metadata
    payload.setdefault("decisions", []).append(entry)
    payload["updated_at"] = date.today().isoformat()
    write_json(path, payload)
    return entry


def latest_papers() -> list[dict[str, Any]]:
    bundle = refresh_bundle()
    return bundle.get("papers", [])


def proposal_from_idea(idea: dict[str, Any]) -> dict[str, Any]:
    source_papers = idea.get("source_papers", [])
    return {
        "id": f"proposal-{uuid.uuid4().hex[:12]}",
        "source_idea": idea["id"],
        "track": idea.get("track", ""),
        "title": idea.get("title", ""),
        "proposal": f"将“{idea.get('title', '')}”纳入 {idea.get('track', '')} 研究画像，作为待验证创新方向。",
        "hypothesis": idea.get("hypothesis", ""),
        "minimum_experiment": idea.get("minimum_experiment", ""),
        "evidence": source_papers,
        "risk": idea.get("risk", ""),
        "status": "pending",
        "created_at": utc_now(),
        "decided_at": "",
    }


def idea_to_task(idea: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": f"task-{uuid.uuid4().hex[:12]}",
        "status": "next",
        "track": idea.get("track", ""),
        "title": idea.get("title", ""),
        "why": idea.get("hypothesis", ""),
        "output": idea.get("minimum_experiment", ""),
        "source_idea": idea.get("id", ""),
        "success_metrics": idea.get("success_metrics", []),
        "created_at": utc_now(),
        "due": "",
    }


def paper_to_idea(paper: dict[str, Any]) -> dict[str, Any]:
    track = (paper.get("tracks") or ["P6"])[0]
    return {
        "id": f"idea-paper-{uuid.uuid4().hex[:12]}",
        "status": "candidate",
        "grade": "A" if paper.get("relevance_score", 0) >= 82 else "B",
        "track": track,
        "title": f"从《{paper.get('title', '')}》提炼可验证迁移点",
        "source": paper.get("title", ""),
        "source_papers": [
            {
                "paper_id": paper.get("id"),
                "title": paper.get("title"),
                "doi": paper.get("doi", ""),
                "url": paper.get("url", ""),
            }
        ],
        "hypothesis": "该论文的核心机制可能补强当前研究画像中的证据缺口，但需先精读并定义可证伪假设。",
        "minimum_experiment": "精读全文后填写最小实验、基线与成功指标；未填写前不得进入研究画像。",
        "controls": [],
        "success_metrics": [],
        "risk": "当前由论文卡片直接转入候选池，尚未完成全文核查。",
        "profile_update_recommendation": "保持 candidate，精读后再决定。",
        "created_at": utc_now(),
    }


def apply_decision(payload: dict[str, Any]) -> dict[str, Any]:
    item_type = payload.get("item_type")
    item_id = valid_id(payload.get("item_id"), "item_id")
    action = payload.get("action")
    note = str(payload.get("note") or "")
    with LOCK:
        if item_type == "idea":
            if action not in IDEA_ACTIONS:
                raise StoreError("unsupported idea action")
            ideas_path = MEMORY / "ideas" / "idea-log.json"
            ideas_payload = read_json(ideas_path, {"updated_at": "", "ideas": []})
            idea = find_item(ideas_payload.get("ideas", []), item_id, "idea")
            if action == "watch":
                idea["status"] = "watch"
            elif action == "reject":
                idea["status"] = "rejected"
                idea["rejection_reason"] = note
            elif action == "convert_to_task":
                idea["status"] = "converted_to_task"
                tasks_path = MEMORY / "tasks" / "task-board.json"
                tasks_payload = read_json(tasks_path, {"updated_at": "", "tasks": []})
                if not any(task.get("source_idea") == item_id for task in tasks_payload.get("tasks", [])):
                    tasks_payload.setdefault("tasks", []).append(idea_to_task(idea))
                tasks_payload["updated_at"] = date.today().isoformat()
                write_json(tasks_path, tasks_payload)
            elif action == "propose_profile":
                idea["status"] = "proposed"
                proposals_path = MEMORY / "profile-update-proposals" / "proposals.json"
                proposals_payload = read_json(proposals_path, {"updated_at": "", "proposals": []})
                existing = next(
                    (
                        proposal
                        for proposal in proposals_payload.get("proposals", [])
                        if proposal.get("source_idea") == item_id and proposal.get("status") == "pending"
                    ),
                    None,
                )
                if existing is None:
                    proposals_payload.setdefault("proposals", []).append(proposal_from_idea(idea))
                proposals_payload["updated_at"] = date.today().isoformat()
                write_json(proposals_path, proposals_payload)
            ideas_payload["updated_at"] = date.today().isoformat()
            write_json(ideas_path, ideas_payload)

        elif item_type == "paper":
            if action not in PAPER_ACTIONS:
                raise StoreError("unsupported paper action")
            paper = find_item(latest_papers(), item_id, "paper")
            if action == "add_to_ideas":
                ideas_path = MEMORY / "ideas" / "idea-log.json"
                ideas_payload = read_json(ideas_path, {"updated_at": "", "ideas": []})
                source_exists = any(
                    any(source.get("paper_id") == item_id for source in idea.get("source_papers", []))
                    for idea in ideas_payload.get("ideas", [])
                )
                if not source_exists:
                    ideas_payload.setdefault("ideas", []).append(paper_to_idea(paper))
                ideas_payload["updated_at"] = date.today().isoformat()
                write_json(ideas_path, ideas_payload)
        else:
            raise StoreError("unsupported item_type")

        decision = append_decision(
            item_type=item_type, item_id=item_id, decision=action, note=note
        )
        bundle = refresh_bundle()
        return {"decision": decision, "bundle": bundle}


def profile_entry(proposal: dict[str, Any]) -> str:
    evidence = proposal.get("evidence", [])
    evidence_lines = []
    for item in evidence:
        link = item.get("url") or (f"https://doi.org/{item.get('doi')}" if item.get("doi") else "")
        title = item.get("title", "来源论文")
        evidence_lines.append(f"- 来源：[{title}]({link})" if link else f"- 来源：{title}")
    lines = [
        f"<!-- proposal:{proposal['id']} -->",
        f"### {proposal.get('track', '')}：{proposal.get('title', '')}",
        "",
        f"- 用户确认日期：{date.today().isoformat()}",
        f"- 核心假设：{proposal.get('hypothesis', '')}",
        f"- 最小验证：{proposal.get('minimum_experiment', '')}",
        f"- 风险边界：{proposal.get('risk', '')}",
        *evidence_lines,
        "",
    ]
    return "\n".join(lines)


def apply_proposal(proposal_id: str, action: str, note: str = "") -> dict[str, Any]:
    proposal_id = valid_id(proposal_id, "proposal_id")
    if action not in PROPOSAL_ACTIONS:
        raise StoreError("unsupported proposal action")
    with LOCK:
        proposals_path = MEMORY / "profile-update-proposals" / "proposals.json"
        proposals_payload = read_json(proposals_path, {"updated_at": "", "proposals": []})
        proposal = find_item(proposals_payload.get("proposals", []), proposal_id, "proposal")
        if proposal.get("status") != "pending":
            raise StoreError("proposal already decided")
        proposal["status"] = {"accept": "accepted", "watch": "watch", "reject": "rejected"}[action]
        proposal["decision_note"] = note.strip()[:1000]
        proposal["decided_at"] = utc_now()
        proposals_payload["updated_at"] = date.today().isoformat()
        write_json(proposals_path, proposals_payload)

        ideas_path = MEMORY / "ideas" / "idea-log.json"
        ideas_payload = read_json(ideas_path, {"updated_at": "", "ideas": []})
        source_idea = proposal.get("source_idea", "")
        idea = next((item for item in ideas_payload.get("ideas", []) if item.get("id") == source_idea), None)
        if idea:
            idea["status"] = {"accept": "accepted", "watch": "watch", "reject": "rejected"}[action]
            if action == "reject":
                idea["rejection_reason"] = note
            ideas_payload["updated_at"] = date.today().isoformat()
            write_json(ideas_path, ideas_payload)

        if action == "accept":
            profile_path = MEMORY / "profile" / "user-research-profile.md"
            profile = profile_path.read_text(encoding="utf-8") if profile_path.exists() else "# 用户研究画像\n"
            marker = f"<!-- proposal:{proposal_id} -->"
            if marker not in profile:
                heading = "## 用户确认采纳的创新点"
                if heading not in profile:
                    profile = profile.rstrip() + f"\n\n{heading}\n\n"
                profile = profile.rstrip() + "\n\n" + profile_entry(proposal)
                profile = re.sub(r"更新日期：\d{4}-\d{2}-\d{2}", f"更新日期：{date.today().isoformat()}", profile, count=1)
                profile_path.write_text(profile.rstrip() + "\n", encoding="utf-8")

        decision = append_decision(
            item_type="profile_proposal",
            item_id=proposal_id,
            decision=action,
            note=note,
            metadata={"source_idea": source_idea},
        )
        bundle = refresh_bundle()
        return {"decision": decision, "bundle": bundle}


def git_sync(message: str = "chore: sync research decisions") -> dict[str, Any]:
    with LOCK:
        refresh_bundle()
        paths = ["research-memory", "web/data/research-bundle.json"]
        subprocess.run(["git", "add", "--", *paths], cwd=ROOT, check=True)
        status = subprocess.run(
            ["git", "diff", "--cached", "--quiet"], cwd=ROOT, check=False
        )
        committed = status.returncode != 0
        if committed:
            subprocess.run(["git", "commit", "-m", message], cwd=ROOT, check=True)
        subprocess.run(["git", "push", "origin", "HEAD"], cwd=ROOT, check=True)
        revision = subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, text=True
        ).strip()
        return {"committed": committed, "revision": revision}

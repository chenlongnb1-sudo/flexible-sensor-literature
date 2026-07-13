from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts import build_research_intelligence as bundle_builder
from scripts import research_store


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")


class ResearchStoreTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.memory = self.root / "research-memory"
        self.web_data = self.root / "web" / "data"
        self.originals = {
            "store_memory": research_store.MEMORY,
            "store_root": research_store.ROOT,
            "builder_memory": bundle_builder.MEMORY,
            "builder_root": bundle_builder.ROOT,
            "builder_web": bundle_builder.WEB_DATA,
        }
        research_store.MEMORY = self.memory
        research_store.ROOT = self.root
        bundle_builder.MEMORY = self.memory
        bundle_builder.ROOT = self.root
        bundle_builder.WEB_DATA = self.web_data
        write_json(
            self.memory / "ideas" / "idea-log.json",
            {
                "updated_at": "2026-07-14",
                "ideas": [
                    {
                        "id": "idea-test",
                        "status": "candidate",
                        "grade": "A",
                        "track": "P4",
                        "title": "Programmable tactile projection",
                        "hypothesis": "Hardware projection preserves task features.",
                        "minimum_experiment": "Compare hardware and software projection.",
                        "controls": ["raw"],
                        "success_metrics": ["R2"],
                        "risk": "Needs resistor-array evidence.",
                        "profile_update_recommendation": "Require user approval.",
                        "source_papers": [{"title": "Source", "url": "https://example.org/paper"}],
                    }
                ],
            },
        )
        write_json(self.memory / "decisions" / "decision-log.json", {"updated_at": "", "decisions": []})
        write_json(self.memory / "tasks" / "task-board.json", {"updated_at": "", "tasks": []})
        write_json(self.memory / "profile-update-proposals" / "proposals.json", {"updated_at": "", "proposals": []})
        profile = self.memory / "profile" / "user-research-profile.md"
        profile.parent.mkdir(parents=True, exist_ok=True)
        profile.write_text("# 用户研究画像\n\n更新日期：2026-07-14\n", encoding="utf-8")

    def tearDown(self) -> None:
        research_store.MEMORY = self.originals["store_memory"]
        research_store.ROOT = self.originals["store_root"]
        bundle_builder.MEMORY = self.originals["builder_memory"]
        bundle_builder.ROOT = self.originals["builder_root"]
        bundle_builder.WEB_DATA = self.originals["builder_web"]
        self.temp.cleanup()

    def test_profile_requires_proposal_then_explicit_acceptance(self) -> None:
        research_store.apply_decision(
            {"item_type": "idea", "item_id": "idea-test", "action": "propose_profile"}
        )
        profile_path = self.memory / "profile" / "user-research-profile.md"
        self.assertNotIn("Programmable tactile projection", profile_path.read_text(encoding="utf-8"))
        proposals = json.loads(
            (self.memory / "profile-update-proposals" / "proposals.json").read_text(encoding="utf-8")
        )["proposals"]
        self.assertEqual(len(proposals), 1)
        self.assertEqual(proposals[0]["status"], "pending")

        research_store.apply_proposal(proposals[0]["id"], "accept", "纳入 P4，但保留实验边界。")
        profile_text = profile_path.read_text(encoding="utf-8")
        self.assertIn("Programmable tactile projection", profile_text)
        self.assertIn(f"proposal:{proposals[0]['id']}", profile_text)
        ideas = json.loads((self.memory / "ideas" / "idea-log.json").read_text(encoding="utf-8"))["ideas"]
        self.assertEqual(ideas[0]["status"], "accepted")

    def test_convert_to_task_is_idempotent(self) -> None:
        payload = {"item_type": "idea", "item_id": "idea-test", "action": "convert_to_task"}
        research_store.apply_decision(payload)
        research_store.apply_decision(payload)
        tasks = json.loads((self.memory / "tasks" / "task-board.json").read_text(encoding="utf-8"))["tasks"]
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["source_idea"], "idea-test")


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

import json
import unittest
from pathlib import Path

from scripts.daily_literature_pipeline import is_on_topic


ROOT = Path(__file__).resolve().parents[1]
PAPERS_PATH = ROOT / "research-memory" / "literature" / "2026" / "2026-07-14" / "summaries" / "papers.json"
IDEAS_PATH = ROOT / "research-memory" / "ideas" / "idea-log.json"
BUNDLE_PATH = ROOT / "web" / "data" / "research-bundle.json"


class DataContractTests(unittest.TestCase):
    def test_daily_papers_match_runtime_contract(self) -> None:
        payload = json.loads(PAPERS_PATH.read_text(encoding="utf-8"))
        self.assertTrue({"date", "searched_at", "search_window_days", "query_log", "papers", "generated_ideas"} <= payload.keys())
        required = {
            "id", "title", "tracks", "relevance_score", "score_breakdown",
            "relevance_reasons", "core_claim", "method_summary", "key_metrics",
            "transferable_points", "risks", "decision_hint", "verification_status",
        }
        allowed_actions = {"ignore", "skim", "read", "add_to_ideas", "profile_candidate", "task_candidate"}
        allowed_tracks = {"P1", "P2", "P3", "P4", "P5", "P6"}
        for paper in payload["papers"]:
            self.assertTrue(required <= paper.keys(), paper.get("title"))
            self.assertTrue(0 <= paper["relevance_score"] <= 100)
            self.assertTrue(set(paper["tracks"]) <= allowed_tracks)
            self.assertIn(paper["decision_hint"], allowed_actions)
            self.assertTrue(is_on_topic({"title": paper["title"], "abstract": paper.get("source_abstract", "")}))
            if paper.get("local_pdf"):
                pdf = ROOT / paper["local_pdf"]
                self.assertTrue(pdf.is_file(), pdf)
                self.assertTrue(pdf.read_bytes().startswith(b"%PDF"), pdf)

    def test_idea_log_statuses_and_sources_are_traceable(self) -> None:
        payload = json.loads(IDEAS_PATH.read_text(encoding="utf-8"))
        allowed = {"candidate", "watch", "proposed", "accepted", "rejected", "converted_to_task"}
        ids = set()
        for idea in payload["ideas"]:
            self.assertNotIn(idea["id"], ids)
            ids.add(idea["id"])
            self.assertIn(idea["status"], allowed)
            self.assertTrue(idea.get("minimum_experiment"))
            self.assertTrue(idea.get("success_metrics"))
            if idea["id"].startswith("idea-2026-07-14-"):
                self.assertTrue(idea.get("source_papers"))

    def test_web_bundle_counts_match_memory_store(self) -> None:
        bundle = json.loads(BUNDLE_PATH.read_text(encoding="utf-8"))
        self.assertEqual(bundle["schema_version"], 2)
        self.assertEqual(bundle["stats"]["papers_today"], len(bundle["papers"]))
        self.assertEqual(bundle["stats"]["must_read"], sum(1 for paper in bundle["papers"] if paper["relevance_score"] >= 80))
        self.assertEqual(bundle["stats"]["pending_proposals"], sum(1 for item in bundle["profile_proposals"] if item["status"] == "pending"))


if __name__ == "__main__":
    unittest.main()

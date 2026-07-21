from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.daily_literature_pipeline import is_on_topic
from scripts.send_daily_notification import build_message


ROOT = Path(__file__).resolve().parents[1]
PAPERS_PATH = ROOT / "research-memory" / "literature" / "2026" / "2026-07-14" / "summaries" / "papers.json"
IDEAS_PATH = ROOT / "research-memory" / "ideas" / "idea-log.json"
BUNDLE_PATH = ROOT / "web" / "data" / "research-bundle.json"
DETAILS_DIR = ROOT / "web" / "data" / "paper-details"
HERO_PATH = ROOT / "web" / "assets" / "tactile-front-end-image2.webp"
ICON_PATH = ROOT / "web" / "assets" / "research-intelligence-icon-image2.png"
WORKFLOW_PATH = ROOT / ".github" / "workflows" / "daily-literature.yml"
TODAY_PATH = ROOT / "research-memory" / "literature" / "2026" / "2026-07-15"
JOURNAL_DB_PATH = ROOT / "config" / "elite-journals.json"


class DataContractTests(unittest.TestCase):
    def test_elite_journal_database_is_unique_and_complete(self) -> None:
        database = json.loads(JOURNAL_DB_PATH.read_text(encoding="utf-8"))
        journals = database["journals"]
        ids = [journal["id"] for journal in journals]
        issns = [journal["issn"].upper() for journal in journals]
        titles = {journal["title"] for journal in journals}
        self.assertGreaterEqual(len(journals), 40)
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(len(issns), len(set(issns)))
        self.assertTrue(
            {
                "Advanced Materials",
                "Advanced Functional Materials",
                "Advanced Science",
                "Advanced Electronic Materials",
                "Nature",
                "Nature Sensors",
                "Science",
                "ACS Nano",
                "Nano Letters",
            }
            <= titles
        )
        for journal in journals:
            self.assertRegex(journal["issn"], r"^\d{4}-[\dX]{4}$")
            self.assertTrue(journal["tracks"])

    def test_daily_report_push_triggers_notification_without_search(self) -> None:
        workflow = WORKFLOW_PATH.read_text(encoding="utf-8")
        self.assertIn('research-memory/literature/**/daily-report.md', workflow)
        self.assertIn("Daily report push detected", workflow)
        self.assertIn("github.event_name == 'push'", workflow)
        self.assertIn("research-intelligence-bot@users.noreply.github.com", workflow)

    def test_zero_result_day_still_builds_status_notification(self) -> None:
        _, plain, _ = build_message(TODAY_PATH)
        self.assertIn("今日没有达到期刊与柔性电子主题双重门槛的新论文", plain)

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
        self.assertEqual(
            bundle["stats"]["must_read"],
            sum(
                1
                for paper in bundle["papers"]
                if paper["relevance_score"] >= 80 or paper["decision_hint"] == "read"
            ),
        )
        self.assertEqual(bundle["stats"]["pending_proposals"], sum(1 for item in bundle["profile_proposals"] if item["status"] == "pending"))

    def test_image2_assets_are_present_and_web_ready(self) -> None:
        hero = HERO_PATH.read_bytes()
        icon = ICON_PATH.read_bytes()
        self.assertGreater(len(hero), 100_000)
        self.assertEqual(hero[:4], b"RIFF")
        self.assertEqual(hero[8:12], b"WEBP")
        self.assertGreater(len(icon), 100_000)
        self.assertEqual(icon[:8], b"\x89PNG\r\n\x1a\n")

        bundle = json.loads(BUNDLE_PATH.read_text(encoding="utf-8"))
        self.assertTrue(bundle["assets"]["hero_image2"])
        self.assertTrue(bundle["assets"]["icon_image2"])

    def test_deep_read_assets_and_pdf_match_detail_contract(self) -> None:
        bundle = json.loads(BUNDLE_PATH.read_text(encoding="utf-8"))
        detail_paths = [
            ROOT / "web" / paper["detail_json"]
            for paper in bundle["papers"]
            if paper.get("detail_json")
        ]
        if not bundle["papers"]:
            self.assertFalse(detail_paths)
            self.assertTrue(list(DETAILS_DIR.glob("*.json")), "expected historical detail bundles to be retained")
            return
        self.assertTrue(detail_paths, "expected at least one current or historical detail bundle")
        required = {
            "schema_version", "id", "title", "status", "page_count", "abstract",
            "innovation_points", "inspirations", "preparation_steps", "method_blocks",
            "figures", "original_pdf", "pdf_version", "pdf_version_label",
        }
        for detail_path in detail_paths:
            detail = json.loads(detail_path.read_text(encoding="utf-8"))
            self.assertTrue(required <= detail.keys(), detail_path)
            if detail["original_pdf"]:
                self.assertGreater(detail["page_count"], 0)
                pdf = ROOT / "web" / detail["original_pdf"]
                self.assertTrue(pdf.is_file(), pdf)
                self.assertTrue(pdf.read_bytes().startswith(b"%PDF"), pdf)
            else:
                self.assertEqual(detail["status"], "metadata_only_no_legal_pdf")
                self.assertEqual(detail["page_count"], 0)
                self.assertFalse(detail["preparation_steps"])
                self.assertFalse(detail["figures"])
            for figure in detail["figures"]:
                self.assertGreater(figure.get("image_width", 0), 0)
                self.assertGreater(figure.get("image_height", 0), 0)
                image = ROOT / "web" / figure["image_path"]
                self.assertTrue(image.is_file(), image)
                self.assertGreater(image.stat().st_size, 1_000, image)
                self.assertEqual(image.read_bytes()[:8], b"\x89PNG\r\n\x1a\n", image)

    def test_notification_uses_curated_brief_without_methods_or_figures(self) -> None:
        day = PAPERS_PATH.parents[1]
        _, plain, _ = build_message(day)
        self.assertIn("摘要：", plain)
        self.assertIn("论文创新：", plain)
        self.assertIn("对你的启发：", plain)
        self.assertIn("无标记的视觉触觉传感器", plain)
        self.assertNotIn("制备步骤", plain)
        self.assertNotIn("逐图", plain)

    def test_notification_groups_categories_and_prioritizes_strong_matches(self) -> None:
        papers = [
            {
                "id": "robot-related",
                "title": "Robot related",
                "primary_category": "软体机器人与人机交互",
                "strongly_related": False,
                "relevance_score": 90,
            },
            {
                "id": "tactile-related",
                "title": "Tactile related",
                "primary_category": "电子皮肤与触觉",
                "strongly_related": False,
                "relevance_score": 95,
            },
            {
                "id": "robot-strong",
                "title": "Robot strong",
                "primary_category": "软体机器人与人机交互",
                "strongly_related": True,
                "relevance_score": 60,
            },
        ]
        with tempfile.TemporaryDirectory() as directory:
            day = Path(directory) / "2026-07-22"
            summaries = day / "summaries"
            summaries.mkdir(parents=True)
            (summaries / "papers.json").write_text(
                json.dumps({"papers": papers}, ensure_ascii=False),
                encoding="utf-8",
            )
            _, plain, _ = build_message(day)

        self.assertEqual(plain.count("【软体机器人与人机交互】"), 1)
        self.assertLess(plain.index("【电子皮肤与触觉】"), plain.index("【软体机器人与人机交互】"))
        self.assertLess(plain.index("Robot strong"), plain.index("Robot related"))


if __name__ == "__main__":
    unittest.main()

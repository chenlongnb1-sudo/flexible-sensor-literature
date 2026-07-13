from __future__ import annotations

import unittest
from datetime import date

from scripts.daily_literature_pipeline import (
    enrich_record,
    is_on_topic,
    make_ideas,
    merge_records,
)


class DailyPipelineTests(unittest.TestCase):
    def test_broad_fault_keyword_does_not_admit_motor_paper(self) -> None:
        record = {
            "title": "Inter-turn fault detection in induction motors",
            "abstract": "A neural network classifies faults from motor current signals.",
        }
        self.assertFalse(is_on_topic(record))

    def test_integrated_tactile_computing_is_high_priority(self) -> None:
        record = {
            "title": "Integrated tactile sensor with on-chip feature extraction",
            "abstract": (
                "An electronic skin tactile array uses an end-to-end sensor readout and "
                "on-chip feature extraction for low-power texture recognition. The integrated "
                "system validates robust classification and adaptive calibration."
            ),
            "authors": ["A. Researcher"],
            "venue": "Test Journal",
            "date": date.today().isoformat(),
            "doi": "10.1234/example.1",
            "url": "https://doi.org/10.1234/example.1",
            "pdf_url": "",
            "is_open_access": False,
            "paper_type": "journal-article",
            "sources": ["Crossref"],
            "query_ids": ["tactile-front-end-computing", "physical-projection"],
            "query_tracks": ["P2", "P4"],
            "cited_by_count": 0,
        }
        paper = enrich_record(record, date.today())
        self.assertIn("P4", paper["tracks"])
        self.assertGreaterEqual(paper["relevance_score"], 80)
        self.assertEqual(paper["decision_hint"], "read")

    def test_merge_prefers_complete_duplicate(self) -> None:
        records = [
            {
                "title": "A tactile paper",
                "doi": "https://doi.org/10.1234/ABC",
                "authors": [],
                "abstract": "short",
                "source": "Crossref",
                "query_ids": ["one"],
                "query_tracks": ["P2"],
            },
            {
                "title": "A tactile paper",
                "doi": "10.1234/abc",
                "authors": ["First Author"],
                "abstract": "a much more complete abstract",
                "source": "OpenAlex",
                "query_ids": ["two"],
                "query_tracks": ["P4"],
            },
        ]
        merged = merge_records(records)
        self.assertEqual(len(merged), 1)
        self.assertEqual(merged[0]["abstract"], "a much more complete abstract")
        self.assertEqual(merged[0]["query_ids"], ["one", "two"])

    def test_ideas_only_use_actionable_papers(self) -> None:
        papers = [
            {
                "id": "paper-good",
                "title": "Integrated tactile computing",
                "doi": "10.1/good",
                "url": "https://doi.org/10.1/good",
                "tracks": ["P4", "P5", "P6"],
                "relevance_score": 84,
            },
            {
                "id": "paper-low",
                "title": "Marginally related application",
                "doi": "10.1/low",
                "url": "https://doi.org/10.1/low",
                "tracks": ["P2"],
                "relevance_score": 49,
            },
        ]
        ideas = make_ideas(papers, date.today(), minimum=3)
        self.assertGreaterEqual(len(ideas), 3)
        self.assertTrue(all(idea["source"] == "Integrated tactile computing" for idea in ideas))


if __name__ == "__main__":
    unittest.main()

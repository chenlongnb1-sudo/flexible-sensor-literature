from __future__ import annotations

import io
import json
import tarfile
import unittest
from datetime import date
from unittest.mock import patch
from urllib.parse import parse_qs, urlparse

from scripts.daily_literature_pipeline import (
    classify_pdf_version,
    enrich_record,
    is_actionable_candidate,
    is_on_topic,
    make_ideas,
    meets_venue_quality,
    merge_records,
    pdf_from_oa_package,
    retain_existing_results_on_empty_refresh,
    SearchJob,
    search_crossref,
    venue_quality_tier,
)


class DailyPipelineTests(unittest.TestCase):
    def test_broad_fault_keyword_does_not_admit_motor_paper(self) -> None:
        record = {
            "title": "Inter-turn fault detection in induction motors",
            "abstract": "A neural network classifies faults from motor current signals.",
        }
        self.assertFalse(is_on_topic(record))

    def test_wiley_issue_listing_is_not_treated_as_a_research_paper(self) -> None:
        record = {
            "title": "Flexible transistor for tactile sensing (Adv. Mater. 37/2026)",
            "abstract": "",
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

    def test_nature_subjournal_meets_venue_floor(self) -> None:
        record = {
            "venue": "Microsystems & Nanoengineering",
            "paper_type": "journal-article",
        }
        self.assertTrue(meets_venue_quality(record))
        self.assertEqual(venue_quality_tier(record), "elite_subjournal_or_am_level")

    def test_preprint_is_excluded_even_when_relevant(self) -> None:
        record = {"venue": "arXiv", "paper_type": "preprint"}
        self.assertFalse(meets_venue_quality(record))
        self.assertEqual(venue_quality_tier(record), "excluded_preprint")

    def test_ordinary_journal_is_below_venue_floor(self) -> None:
        record = {"venue": "Test Journal", "paper_type": "journal-article"}
        self.assertFalse(meets_venue_quality(record))
        self.assertEqual(venue_quality_tier(record), "below_venue_threshold")

    def test_device_substring_does_not_bypass_venue_floor(self) -> None:
        record = {
            "venue": "IEEE Transactions on Electron Devices",
            "paper_type": "journal-article",
        }
        self.assertFalse(meets_venue_quality(record))

    def test_cell_press_device_journal_meets_venue_floor(self) -> None:
        record = {"venue": "Device", "paper_type": "journal-article"}
        self.assertTrue(meets_venue_quality(record))

    def test_crossref_targeted_query_uses_container_title(self) -> None:
        job = SearchJob(
            query_id="venue-nature-electronics",
            query="flexible tactile electronic skin sensor",
            source="crossref",
            tracks=("P4",),
            from_date=date(2026, 6, 14),
            to_date=date(2026, 7, 14),
            container_title="Nature Electronics",
            issn="2520-1131",
        )
        response = json.dumps(
            {
                "message": {
                    "items": [
                        {
                            "title": ["Matching tactile paper"],
                            "container-title": ["Nature Electronics"],
                            "type": "journal-article",
                        },
                        {
                            "title": ["Off-target tactile paper"],
                            "container-title": ["Advanced Science"],
                            "type": "journal-article",
                        },
                    ]
                }
            }
        ).encode("utf-8")
        with patch("scripts.daily_literature_pipeline.request_bytes", return_value=(response, "application/json")) as request:
            records = search_crossref(job)
        params = parse_qs(urlparse(request.call_args.args[0]).query)
        self.assertEqual(params["query.container-title"], ["Nature Electronics"])
        self.assertIn("/journals/2520-1131/works", request.call_args.args[0])
        self.assertEqual([record["title"] for record in records], ["Matching tactile paper"])

    def test_specific_tactile_computing_title_can_clear_relevance_threshold(self) -> None:
        record = {
            "title": "Biomimetic tactile sensor system with neuromorphic encoding",
            "abstract": "",
            "venue": "Advanced Intelligent Systems",
            "paper_type": "journal-article",
            "date": date.today().isoformat(),
            "query_ids": ["neuromorphic-tactile-encoding"],
        }
        self.assertTrue(is_actionable_candidate(record, date.today()))

    def test_targeted_elite_venue_does_not_bypass_relevance_threshold(self) -> None:
        record = {
            "title": "Reduction of appearance artifacts in wearable on-skin electronics",
            "abstract": (
                "Invisible electrodes monitor facial electrooculogram, electromyogram, "
                "and electroencephalogram signals for health monitoring."
            ),
            "venue": "Science Advances",
            "paper_type": "journal-article",
            "date": date.today().isoformat(),
            "query_ids": ["venue-science-advances"],
        }
        self.assertFalse(is_actionable_candidate(record, date.today()))

    def test_targeted_subjournal_record_still_requires_relevance_threshold(self) -> None:
        record = {
            "title": "Impedance characteristics in iontronic tactile sensors",
            "abstract": "A flexible electronic skin decouples temperature and pressure.",
            "venue": "npj Flexible Electronics",
            "paper_type": "journal-article",
            "date": date.today().isoformat(),
            "query_ids": ["venue-npj-flexible-electronics"],
            "query_tracks": ["P1", "P2"],
        }
        self.assertTrue(is_on_topic(record))
        self.assertFalse(is_actionable_candidate(record, date.today()))

    def test_missing_abstract_material_only_title_stays_excluded(self) -> None:
        record = {
            "title": "MXene tactile sensor with ultrahigh sensitivity",
            "abstract": "",
            "venue": "Small",
            "paper_type": "journal-article",
            "date": date.today().isoformat(),
            "query_ids": ["tolerance-interface"],
        }
        self.assertFalse(is_actionable_candidate(record, date.today()))

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

    def test_merge_uses_journal_metadata_and_keeps_preprint_pdf(self) -> None:
        records = [
            {
                "title": "A tactile computing paper",
                "doi": "10.1234/published",
                "venue": "arXiv",
                "paper_type": "preprint",
                "url": "https://arxiv.org/abs/1234.5678",
                "pdf_url": "https://arxiv.org/pdf/1234.5678",
                "source": "arXiv",
                "query_ids": ["one"],
                "query_tracks": ["P4"],
            },
            {
                "title": "A tactile computing paper",
                "doi": "10.1234/published",
                "venue": "Advanced Science",
                "paper_type": "journal-article",
                "url": "https://doi.org/10.1234/published",
                "pdf_url": "",
                "source": "Crossref",
                "query_ids": ["two"],
                "query_tracks": ["P4"],
            },
        ]
        merged = merge_records(records)[0]
        self.assertEqual(merged["venue"], "Advanced Science")
        self.assertEqual(merged["paper_type"], "journal-article")
        self.assertEqual(merged["pdf_url"], "https://arxiv.org/pdf/1234.5678")

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

    def test_empty_same_day_refresh_retains_existing_results(self) -> None:
        existing = {
            "papers": [{"id": "paper-kept"}],
            "generated_ideas": [{"id": "idea-kept"}],
        }
        papers, ideas, retained = retain_existing_results_on_empty_refresh([], [], existing)
        self.assertTrue(retained)
        self.assertEqual(papers, existing["papers"])
        self.assertEqual(ideas, existing["generated_ideas"])

    def test_pdf_version_labels_do_not_overclaim_repository_copies(self) -> None:
        self.assertEqual(classify_pdf_version("https://arxiv.org/pdf/1234.5678")[0], "author_preprint")
        self.assertEqual(
            classify_pdf_version("https://www.nature.com/articles/example.pdf")[0],
            "publisher_pdf",
        )
        self.assertEqual(
            classify_pdf_version("https://example.edu/repository/manuscript.pdf")[0],
            "repository_or_author_copy",
        )

    def test_pdf_can_be_read_from_pmc_oa_package(self) -> None:
        buffer = io.BytesIO()
        payload = b"%PDF-1.7\nlegal open access test"
        with tarfile.open(fileobj=buffer, mode="w:gz") as archive:
            member = tarfile.TarInfo("article/main.pdf")
            member.size = len(payload)
            archive.addfile(member, io.BytesIO(payload))
        self.assertEqual(pdf_from_oa_package(buffer.getvalue()), payload)


if __name__ == "__main__":
    unittest.main()

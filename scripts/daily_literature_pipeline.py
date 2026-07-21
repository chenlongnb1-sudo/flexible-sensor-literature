#!/usr/bin/env python3
"""Fetch, rank, archive, and report daily tactile-computing literature.

The implementation intentionally uses public scholarly APIs and Python's standard
library so it can run both locally and in GitHub Actions without API keys.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import http.cookiejar
import hashlib
import html
import io
import json
import os
import re
import subprocess
import sys
import tarfile
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Iterable

try:
    from .build_paper_deep_reads import build_deep_reads
except ImportError:
    from build_paper_deep_reads import build_deep_reads


ROOT = Path(__file__).resolve().parents[1]
MEMORY = ROOT / "research-memory"
CONFIG_PATH = ROOT / "config" / "literature-queries.json"
JOURNAL_DB_PATH = ROOT / "config" / "elite-journals.json"
USER_AGENT = "FlexibleSensorResearchIntelligence/1.0 (mailto:{})"
DEFAULT_MAILTO = os.environ.get("OPENALEX_MAILTO", "").strip()
OPENALEX_API_KEY = os.environ.get("OPENALEX_API_KEY", "").strip()
UNPAYWALL_EMAIL = os.environ.get(
    "UNPAYWALL_EMAIL",
    DEFAULT_MAILTO or "chenlongnb1-sudo@users.noreply.github.com",
).strip()

TRACK_TERMS: dict[str, tuple[str, ...]] = {
    "P1": (
        "tolerance", "dispersion", "repeatability", "reproducibility", "assembly",
        "misalignment", "electrode", "microstructure", "contact radius", "variation",
    ),
    "P2": (
        "analog front-end", "analog frontend", "pre-adc", "before digitization",
        "vector tactile", "shear", "friction", "slip", "direction", "differential",
        "summation", "decoupling", "three-axis", "triaxial",
    ),
    "P3": (
        "tactile array", "sensor array", "compressed readout", "readout channel",
        "low channel", "multiplex", "macro-pixel", "edge detection", "spatial feature",
    ),
    "P4": (
        "in-sensor computing", "in sensor computing", "near-sensor computing",
        "physical computing", "analog computing", "programmable", "projection",
        "current summation", "computational sensor", "sensor computing", "on-chip",
        "feature extraction", "end-to-end", "integrated tactile", "adaptive tactile",
        "neuromorphic", "synaptic", "encoding",
    ),
    "P5": (
        "fault tolerant", "fault-tolerant", "robust", "drift", "transferable",
        "domain adaptation", "few-shot", "few shot", "calibration", "device variation",
        "cross-device", "self-calibration",
    ),
    "P6": (
        "electronic skin", "e-skin", "soft robotics", "robotic tactile", "wearable",
        "insole", "human monitoring", "texture recognition", "grasp", "haptic",
    ),
}

CORE_TERMS = (
    "tactile", "electronic skin", "electronic skins", "electronic-skin", "e-skin",
    "pressure sensor", "force sensor", "soft sensor", "flexible sensor",
    "wearable sensor", "touch sensor", "artificial skin",
)
SYSTEM_TERMS = (
    "front-end", "frontend", "readout", "array", "computing", "circuit", "adc",
    "vector", "shear", "friction", "slip", "calibration", "fault", "system",
    "feature extraction", "on-chip", "end-to-end", "integrated", "reconfiguration",
    "neuromorphic", "synaptic", "encoding",
)
MATERIAL_TERMS = (
    "mxene", "graphene", "hydrogel", "ionogel", "nanocomposite", "nanofiber",
    "sensitivity", "gauge factor", "detection limit",
)
EVIDENCE_TERMS = (
    "comparison", "benchmark", "statistical", "array", "circuit", "latency",
    "power", "calibration", "classification", "robot", "experiment", "validation",
)

ELITE_VENUE_EXACT = {
    "nature", "nature communications", "nature electronics", "nature materials",
    "nature machine intelligence", "communications engineering", "communications materials",
    "communications physics", "communications chemistry", "microsystems & nanoengineering",
    "microsystems and nanoengineering", "science", "science advances", "science robotics",
    "science translational medicine", "cell", "cell reports physical science", "matter",
    "joule", "device", "advanced materials", "advanced functional materials",
    "advanced science", "advanced intelligent systems", "advanced electronic materials",
    "advanced materials technologies", "advanced fiber materials", "small", "small methods",
    "nano-micro letters", "acs nano", "nano letters", "materials horizons",
    "national science review", "proceedings of the national academy of sciences",
    "international journal of extreme manufacturing",
}
try:
    _journal_database = json.loads(JOURNAL_DB_PATH.read_text(encoding="utf-8"))
except (OSError, json.JSONDecodeError):
    _journal_database = {"journals": []}
ELITE_VENUE_EXACT.update(
    str(name).lower().strip()
    for journal in _journal_database.get("journals", [])
    for name in [journal.get("title"), *(journal.get("aliases") or [])]
    if name
)
TARGETED_VENUE_EXACT = {
    str(name).lower().strip()
    for journal in _journal_database.get("journals", [])
    for name in [journal.get("title"), *(journal.get("aliases") or [])]
    if name
}
PREPRINT_VENUES = ("arxiv", "biorxiv", "medrxiv", "research square", "ssrn")


@dataclass(frozen=True)
class SearchJob:
    query_id: str
    query: str
    source: str
    tracks: tuple[str, ...]
    from_date: date
    to_date: date
    container_title: str = ""
    issn: str = ""


def load_json(path: Path, fallback: Any) -> Any:
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


def configured_search_queries(config: dict[str, Any]) -> list[dict[str, Any]]:
    queries = [*config.get("queries", []), *config.get("targeted_venue_queries", [])]
    database_path = ROOT / str(config.get("journal_database") or "config/elite-journals.json")
    database = load_json(database_path, {"journals": []})
    default_query = str(
        config.get("targeted_venue_query")
        or database.get("default_query")
        or "flexible tactile electronic skin wearable pressure haptic neuromorphic sensor"
    )
    for journal in database.get("journals", []):
        if journal.get("search_enabled", True) is False:
            continue
        queries.append(
            {
                "id": f"venue-{journal['id']}",
                "query": journal.get("query") or default_query,
                "container_title": journal["title"],
                "issn": journal["issn"],
                "tracks": journal.get("tracks") or ["P1", "P2", "P3", "P4", "P5", "P6"],
                "sources": ["crossref"],
            }
        )
    deduplicated = {query["id"]: query for query in queries}
    return list(deduplicated.values())


def request_bytes(
    url: str,
    *,
    accept: str = "application/json",
    timeout: int = 25,
    extra_headers: dict[str, str] | None = None,
) -> tuple[bytes, str]:
    headers = {
        "Accept": accept,
        "User-Agent": USER_AGENT.format(DEFAULT_MAILTO or "not-configured"),
    }
    if extra_headers:
        headers.update(extra_headers)
    opener = urllib.request.build_opener(
        urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar())
    )
    last_error: Exception | None = None
    for attempt in range(3):
        try:
            with opener.open(urllib.request.Request(url, headers=headers), timeout=timeout) as response:
                return response.read(), response.headers.get("Content-Type", "")
        except urllib.error.HTTPError as error:
            last_error = error
            error.close()
            if error.code not in {429, 500, 502, 503, 504}:
                break
            if attempt < 2:
                time.sleep(1.2 * (attempt + 1))
        except (urllib.error.URLError, TimeoutError) as error:
            last_error = error
            if attempt < 2:
                time.sleep(1.2 * (attempt + 1))
    raise RuntimeError(f"{type(last_error).__name__}: {last_error}")


def reconstruct_abstract(index: dict[str, list[int]] | None) -> str:
    if not index:
        return ""
    positioned = ((position, word) for word, positions in index.items() for position in positions)
    return " ".join(word for _, word in sorted(positioned))


def normalize_doi(value: str | None) -> str:
    if not value:
        return ""
    value = value.strip().lower()
    value = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", value)
    match = re.search(r"10\.\d{4,9}/\S+", value)
    return match.group(0).rstrip(".,);]") if match else ""


def normalize_venue_name(value: str | None) -> str:
    return re.sub(r"[^a-z0-9]+", " ", html.unescape(value or "").lower()).strip()


def normalize_title(value: str) -> str:
    words = re.findall(r"[a-z0-9]+", value.lower())
    stopwords = {"a", "an", "the", "in", "of", "for", "on", "to", "and", "with", "by", "et", "al"}
    return " ".join(word for word in words if word not in stopwords)


def stable_id(title: str, doi: str = "") -> str:
    source = doi or normalize_title(title)
    return hashlib.sha1(source.encode("utf-8")).hexdigest()[:16]


def iso_date(parts: Any) -> str:
    if isinstance(parts, str):
        match = re.search(r"\d{4}-\d{2}-\d{2}", parts)
        return match.group(0) if match else parts[:10]
    if isinstance(parts, dict):
        values = parts.get("date-parts", [[]])
        if values and values[0]:
            year, *tail = values[0]
            month = tail[0] if tail else 1
            day = tail[1] if len(tail) > 1 else 1
            return f"{year:04d}-{month:02d}-{day:02d}"
    return ""


def clean_markup(value: str | None) -> str:
    if not value:
        return ""
    value = re.sub(r"<[^>]+>", " ", html.unescape(value))
    return re.sub(r"\s+", " ", value).strip()


class CitationMetaParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.pdf_urls: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "meta":
            return
        values = {key.lower(): value or "" for key, value in attrs}
        name = (values.get("name") or values.get("property") or "").lower()
        if name in {"citation_pdf_url", "wkhealth_pdf_url"} and values.get("content"):
            self.pdf_urls.append(values["content"])


def unique_urls(urls: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    result = []
    for value in urls:
        url = str(value or "").strip()
        if not url or url in seen:
            continue
        seen.add(url)
        result.append(url)
    return result


def classify_pdf_version(url: str) -> tuple[str, str]:
    """Label a PDF conservatively without treating every repository copy as the version of record."""
    value = str(url or "").lower()
    if "arxiv.org/" in value:
        return "author_preprint", "作者公开预印本（非期刊排版版）"
    if any(
        marker in value
        for marker in (
            "nature.com/articles/", "link.springer.com/content/pdf/",
            "onlinelibrary.wiley.com/doi/pdf", "science.org/doi/pdf",
            "cell.com/", "sciencedirect.com/science/article/pii/",
        )
    ):
        return "publisher_pdf", "出版社开放获取 PDF"
    if any(
        marker in value
        for marker in ("pmc.ncbi.nlm.nih.gov/", "ncbi.nlm.nih.gov/pmc/", "ftp.ncbi.nlm.nih.gov/")
    ):
        return "repository_copy", "公共全文库合法存档版本"
    return "repository_or_author_copy", "作者或机构仓储合法公开版本"


def citation_pdf_urls(landing_url: str) -> list[str]:
    raw, content_type = request_bytes(
        landing_url,
        accept="text/html,application/xhtml+xml",
        timeout=20,
    )
    if "html" not in content_type.lower() and not raw.lstrip().startswith(b"<"):
        return []
    parser = CitationMetaParser()
    parser.feed(raw.decode("utf-8", errors="replace"))
    return unique_urls(urllib.parse.urljoin(landing_url, url) for url in parser.pdf_urls)


def pmc_oa_pdf_urls(landing_url: str) -> list[str]:
    match = re.search(r"PMC\d+", landing_url, flags=re.IGNORECASE)
    if not match:
        return []
    pmcid = match.group(0).upper()
    raw, _ = request_bytes(
        "https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?" + urllib.parse.urlencode({"id": pmcid}),
        accept="application/xml,text/xml",
        timeout=20,
    )
    root = ET.fromstring(raw)
    urls = []
    for link in root.findall(".//link"):
        if link.attrib.get("format") not in {"pdf", "tgz"} or not link.attrib.get("href"):
            continue
        href = link.attrib["href"]
        urls.extend([href.replace("ftp://ftp.ncbi.nlm.nih.gov", "https://ftp.ncbi.nlm.nih.gov"), href])
    return unique_urls(urls)


def pdf_from_oa_package(raw: bytes) -> bytes | None:
    """Read a PDF from a lawful PMC OA tarball without extracting arbitrary paths."""
    try:
        with tarfile.open(fileobj=io.BytesIO(raw), mode="r:gz") as archive:
            members = [
                member
                for member in archive.getmembers()
                if member.isfile() and member.name.lower().endswith(".pdf")
            ]
            members.sort(key=lambda member: ("supp" in member.name.lower(), member.size))
            for member in members:
                if member.size > 40 * 1024 * 1024:
                    continue
                source = archive.extractfile(member)
                candidate = source.read() if source else b""
                if candidate.startswith(b"%PDF"):
                    return candidate
    except (tarfile.TarError, OSError):
        return None
    return None


def request_pdf_bytes(url: str, timeout: int = 45) -> tuple[bytes, str]:
    first_error: Exception | None = None
    try:
        raw, content_type = request_bytes(url, accept="application/pdf", timeout=timeout)
    except Exception as error:  # noqa: BLE001 - curl may handle publisher redirects better
        first_error = error
        raw, content_type = b"", ""
    if raw.startswith(b"%PDF"):
        return raw, content_type
    if urllib.parse.urlparse(url).scheme not in {"http", "https"}:
        return raw, content_type
    try:
        completed = subprocess.run(
            [
                "curl", "--fail", "--location", "--silent", "--show-error",
                "--max-time", str(timeout), "--user-agent", "Mozilla/5.0",
                "--header", "Accept: application/pdf", url,
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            timeout=timeout + 5,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return raw, content_type
    if completed.returncode == 0 and completed.stdout.startswith(b"%PDF"):
        return completed.stdout, "application/pdf"
    if first_error is not None:
        raise first_error
    return raw, content_type


def legal_pdf_candidates(paper: dict[str, Any]) -> list[str]:
    doi = normalize_doi(paper.get("doi"))
    candidates: list[str] = []
    if doi.startswith("10.1038/"):
        candidates.append(f"https://www.nature.com/articles/{doi.split('/', 1)[1]}.pdf")
    if doi.startswith("10.1007/"):
        candidates.append(f"https://link.springer.com/content/pdf/{doi}.pdf")
    candidates.append(str(paper.get("pdf_url") or ""))
    candidates.extend(paper.get("pdf_candidates") or [])

    if doi and UNPAYWALL_EMAIL:
        try:
            url = "https://api.unpaywall.org/v2/" + urllib.parse.quote(doi, safe="")
            url += "?" + urllib.parse.urlencode({"email": UNPAYWALL_EMAIL})
            payload = json.loads(request_bytes(url, timeout=20)[0])
            locations = [payload.get("best_oa_location") or {}, *(payload.get("oa_locations") or [])]
            candidates.extend(location.get("url_for_pdf") or "" for location in locations)
            for location in locations:
                landing = str(location.get("url") or "")
                if landing and not location.get("url_for_pdf"):
                    try:
                        candidates.extend(citation_pdf_urls(landing))
                    except Exception:
                        pass
                    try:
                        candidates.extend(pmc_oa_pdf_urls(landing))
                    except Exception:
                        pass
        except Exception:
            pass

    if doi:
        landing_url = f"https://doi.org/{doi}"
        try:
            candidates.extend(citation_pdf_urls(landing_url))
        except Exception:
            pass
    return unique_urls(candidates)


def search_openalex(job: SearchJob) -> list[dict[str, Any]]:
    params = {
        "search": job.query,
        "filter": f"from_publication_date:{job.from_date.isoformat()},to_publication_date:{job.to_date.isoformat()}",
        "sort": "publication_date:desc",
        "per-page": "25",
    }
    if DEFAULT_MAILTO:
        params["mailto"] = DEFAULT_MAILTO
    if OPENALEX_API_KEY:
        params["api_key"] = OPENALEX_API_KEY
    url = "https://api.openalex.org/works?" + urllib.parse.urlencode(params)
    payload = json.loads(request_bytes(url)[0])
    records = []
    for item in payload.get("results", []):
        primary = item.get("primary_location") or {}
        source = primary.get("source") or {}
        best_oa = item.get("best_oa_location") or {}
        authors = [
            authorship.get("author", {}).get("display_name", "")
            for authorship in item.get("authorships", [])[:12]
        ]
        records.append(
            {
                "title": item.get("display_name") or item.get("title") or "",
                "authors": [author for author in authors if author],
                "venue": source.get("display_name") or "",
                "date": item.get("publication_date") or "",
                "doi": normalize_doi(item.get("doi")),
                "url": primary.get("landing_page_url") or item.get("id") or "",
                "pdf_url": best_oa.get("pdf_url") or "",
                "pdf_candidates": unique_urls(
                    (location or {}).get("pdf_url") or ""
                    for location in [best_oa, primary, *(item.get("locations") or [])]
                ),
                "is_open_access": bool((item.get("open_access") or {}).get("is_oa")),
                "paper_type": item.get("type") or "",
                "abstract": reconstruct_abstract(item.get("abstract_inverted_index")),
                "cited_by_count": int(item.get("cited_by_count") or 0),
                "source": "OpenAlex",
                "query_ids": [job.query_id],
                "query_tracks": list(job.tracks),
            }
        )
    return records


def search_crossref(job: SearchJob) -> list[dict[str, Any]]:
    params = {
        "query.bibliographic": job.query,
        "filter": f"from-pub-date:{job.from_date.isoformat()},until-pub-date:{job.to_date.isoformat()}",
        "sort": "relevance",
        "order": "desc",
        "rows": "100" if job.issn else "25",
        "mailto": DEFAULT_MAILTO,
    }
    if job.container_title:
        params["query.container-title"] = job.container_title
    endpoint = "https://api.crossref.org/works"
    if job.issn:
        endpoint = f"https://api.crossref.org/journals/{urllib.parse.quote(job.issn)}/works"
    url = endpoint + "?" + urllib.parse.urlencode(params)
    payload = json.loads(request_bytes(url)[0])
    records = []
    for item in payload.get("message", {}).get("items", []):
        title_values = item.get("title") or []
        venue = clean_markup((item.get("container-title") or [""])[0])
        if job.container_title and normalize_venue_name(venue) != normalize_venue_name(job.container_title):
            continue
        authors = []
        for author in item.get("author", [])[:12]:
            name = " ".join(part for part in (author.get("given", ""), author.get("family", "")) if part)
            if name:
                authors.append(name)
        published = item.get("published-online") or item.get("published-print") or item.get("published")
        records.append(
            {
                "title": clean_markup(title_values[0] if title_values else ""),
                "authors": authors,
                "venue": venue,
                "date": iso_date(published),
                "doi": normalize_doi(item.get("DOI")),
                "url": item.get("URL") or "",
                "pdf_url": "",
                "pdf_candidates": unique_urls(
                    link.get("URL") or ""
                    for link in item.get("link", [])
                    if "pdf" in str(link.get("content-type") or "").lower()
                ),
                "is_open_access": False,
                "paper_type": item.get("type") or "",
                "abstract": clean_markup(item.get("abstract")),
                "cited_by_count": int(item.get("is-referenced-by-count") or 0),
                "source": "Crossref",
                "query_ids": [job.query_id],
                "query_tracks": list(job.tracks),
            }
        )
    return records


def arxiv_query(value: str) -> str:
    concepts = [word for word in re.findall(r"[A-Za-z][A-Za-z-]+", value) if len(word) > 3]
    return " AND ".join(f"all:{word}" for word in concepts[:2])


def search_arxiv(job: SearchJob) -> list[dict[str, Any]]:
    query = arxiv_query(job.query)
    params = {
        "search_query": query,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
        "max_results": "25",
    }
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(params)
    raw, _ = request_bytes(url, accept="application/atom+xml")
    namespace = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
    root = ET.fromstring(raw)
    records = []
    for entry in root.findall("atom:entry", namespace):
        published = (entry.findtext("atom:published", default="", namespaces=namespace) or "")[:10]
        if published and not (job.from_date.isoformat() <= published <= job.to_date.isoformat()):
            continue
        entry_url = entry.findtext("atom:id", default="", namespaces=namespace)
        pdf_url = ""
        for link in entry.findall("atom:link", namespace):
            if link.attrib.get("title") == "pdf":
                pdf_url = link.attrib.get("href", "")
        arxiv_id = entry_url.rsplit("/", 1)[-1]
        records.append(
            {
                "title": clean_markup(entry.findtext("atom:title", default="", namespaces=namespace)),
                "authors": [
                    clean_markup(author.findtext("atom:name", default="", namespaces=namespace))
                    for author in entry.findall("atom:author", namespace)
                ],
                "venue": "arXiv",
                "date": published,
                "doi": normalize_doi(entry.findtext("arxiv:doi", default="", namespaces=namespace)),
                "url": entry_url,
                "pdf_url": pdf_url,
                "pdf_candidates": [pdf_url] if pdf_url else [],
                "is_open_access": True,
                "paper_type": "preprint",
                "abstract": clean_markup(entry.findtext("atom:summary", default="", namespaces=namespace)),
                "cited_by_count": 0,
                "source": "arXiv",
                "arxiv_id": arxiv_id,
                "query_ids": [job.query_id],
                "query_tracks": list(job.tracks),
            }
        )
    return records


def search_semantic_scholar(job: SearchJob) -> list[dict[str, Any]]:
    fields = (
        "title,authors,venue,publicationDate,externalIds,url,openAccessPdf,abstract,"
        "citationCount,publicationTypes"
    )
    params = {
        "query": job.query,
        "limit": "25",
        "fields": fields,
        "publicationDateOrYear": f"{job.from_date.isoformat()}:{job.to_date.isoformat()}",
    }
    url = "https://api.semanticscholar.org/graph/v1/paper/search?" + urllib.parse.urlencode(params)
    api_key = os.environ.get("SEMANTIC_SCHOLAR_API_KEY", "").strip()
    raw, _ = request_bytes(url, extra_headers={"x-api-key": api_key} if api_key else None)
    payload = json.loads(raw)
    records = []
    for item in payload.get("data", []):
        external = item.get("externalIds") or {}
        oa_pdf = item.get("openAccessPdf") or {}
        records.append(
            {
                "title": clean_markup(item.get("title")),
                "authors": [author.get("name", "") for author in item.get("authors", [])[:12] if author.get("name")],
                "venue": item.get("venue") or "",
                "date": item.get("publicationDate") or "",
                "doi": normalize_doi(external.get("DOI")),
                "url": item.get("url") or "",
                "pdf_url": oa_pdf.get("url") or "",
                "pdf_candidates": [oa_pdf.get("url")] if oa_pdf.get("url") else [],
                "is_open_access": bool(oa_pdf.get("url")),
                "paper_type": ", ".join(item.get("publicationTypes") or []),
                "abstract": clean_markup(item.get("abstract")),
                "cited_by_count": int(item.get("citationCount") or 0),
                "source": "Semantic Scholar",
                "query_ids": [job.query_id],
                "query_tracks": list(job.tracks),
            }
        )
    return records


SEARCHERS = {
    "openalex": search_openalex,
    "crossref": search_crossref,
    "semantic_scholar": search_semantic_scholar,
    "arxiv": search_arxiv,
}


def merge_records(records: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    merged: list[dict[str, Any]] = []
    doi_index: dict[str, int] = {}
    title_index: dict[str, int] = {}
    for record in records:
        title = record.get("title", "").strip()
        if not title:
            continue
        doi = normalize_doi(record.get("doi"))
        title_key = normalize_title(title)
        index = doi_index.get(doi) if doi else title_index.get(title_key)
        if index is None:
            record["doi"] = doi
            merged.append(record)
            index = len(merged) - 1
            if doi:
                doi_index[doi] = index
            title_index[title_key] = index
            continue

        current = merged[index]
        current["query_ids"] = sorted(set(current.get("query_ids", []) + record.get("query_ids", [])))
        current["query_tracks"] = sorted(set(current.get("query_tracks", []) + record.get("query_tracks", [])))
        current["sources"] = sorted(
            set(current.get("sources", [current.get("source", "")]) + [record.get("source", "")])
        )
        current["pdf_candidates"] = unique_urls(
            [*current.get("pdf_candidates", []), *record.get("pdf_candidates", [])]
        )
        current_is_preprint = (
            "preprint" in str(current.get("paper_type", "")).lower()
            or any(term in str(current.get("venue", "")).lower() for term in PREPRINT_VENUES)
        )
        candidate_is_preprint = (
            "preprint" in str(record.get("paper_type", "")).lower()
            or any(term in str(record.get("venue", "")).lower() for term in PREPRINT_VENUES)
        )
        prefer_candidate_metadata = current_is_preprint and not candidate_is_preprint
        for field in ("abstract", "authors", "venue", "date", "url", "pdf_url", "doi", "paper_type"):
            existing = current.get(field)
            candidate = record.get(field)
            replace_with_journal = prefer_candidate_metadata and field in {
                "authors", "venue", "date", "url", "doi", "paper_type"
            }
            if (
                not existing
                or replace_with_journal
                or (field == "abstract" and len(candidate or "") > len(existing or ""))
            ):
                current[field] = candidate
        current["is_open_access"] = bool(current.get("is_open_access") or record.get("is_open_access"))
        current["cited_by_count"] = max(int(current.get("cited_by_count") or 0), int(record.get("cited_by_count") or 0))
    for record in merged:
        record.setdefault("sources", [record.pop("source", "")])
        record.pop("source", None)
    return merged


def count_terms(text: str, terms: Iterable[str]) -> int:
    lowered = text.lower()
    return sum(1 for term in terms if term in lowered)


def is_on_topic(record: dict[str, Any]) -> bool:
    """Hard gate before scoring so broad Crossref matches cannot pollute the report."""
    text = " ".join((record.get("title", ""), record.get("abstract", ""))).lower()
    title = str(record.get("title", ""))
    if "issue information" in title.lower() or re.search(
        r"\((?:adv\.|advanced)\s+[^)]*\d+/\d{4}\)\s*$", title, re.IGNORECASE
    ):
        return False
    direct_tactile = any(
        term in text
        for term in ("tactile", "electronic skin", "electronic-skin", "e-skin", "artificial skin")
    )
    sensor_context = count_terms(text, CORE_TERMS) > 0
    front_end_context = count_terms(text, SYSTEM_TERMS) > 0
    track_context = sum(count_terms(text, terms) for terms in TRACK_TERMS.values())
    targeted_venue = any(
        str(query_id).startswith("venue-") for query_id in record.get("query_ids", [])
    )
    targeted_sensor_system = (
        targeted_venue
        and any(term in title.lower() for term in ("pressure sensor", "force sensor", "strain sensor"))
        and any(
            term in text
            for term in (
                "wearable", "robotic", "signal acquisition", "human monitoring",
                "human-machine", "array", "readout", "decoupl", "biological signal",
            )
        )
    )
    return direct_tactile or targeted_sensor_system or (
        sensor_context and front_end_context and track_context >= 1
    )


def venue_quality_tier(record: dict[str, Any]) -> str:
    venue = re.sub(r"\s+", " ", html.unescape(str(record.get("venue", "")))).lower().strip()
    paper_type = str(record.get("paper_type", "")).lower()
    if "preprint" in paper_type or any(term in venue for term in PREPRINT_VENUES):
        return "excluded_preprint"
    if venue in ELITE_VENUE_EXACT or venue.startswith("nature ") or venue.startswith("npj "):
        return "elite_subjournal_or_am_level"
    return "below_venue_threshold"


def meets_venue_quality(record: dict[str, Any]) -> bool:
    return venue_quality_tier(record) == "elite_subjournal_or_am_level"


def is_targeted_venue_record(record: dict[str, Any]) -> bool:
    venue = re.sub(
        r"\s+", " ", html.unescape(str(record.get("venue", "")))
    ).lower().strip()
    return venue in TARGETED_VENUE_EXACT or any(
        str(query_id).startswith("venue-") for query_id in record.get("query_ids", [])
    )


def is_actionable_candidate(record: dict[str, Any], today: date) -> bool:
    score = score_record(record, today)["relevance_score"]
    if score >= 48:
        return True
    if not is_targeted_venue_record(record) or score < 30:
        return False
    title = str(record.get("title", "")).lower()
    return any(
        term in title
        for term in (
            "tactile", "electronic skin", "e-skin", "artificial skin", "iontronic skin",
            "haptic", "pressure sensor", "pressure sensing", "force sensor",
            "human-machine interaction", "robotic perception",
        )
    )


def score_record(record: dict[str, Any], today: date) -> dict[str, Any]:
    text = " ".join((record.get("title", ""), record.get("abstract", ""))).lower()
    core_hits = count_terms(text, CORE_TERMS)
    track_hits = {track: count_terms(text, terms) for track, terms in TRACK_TERMS.items()}
    ranked_tracks = sorted(
        TRACK_TERMS,
        key=lambda track: track_hits[track],
        reverse=True,
    )
    tracks = [track for track in ranked_tracks if track_hits[track] > 0][:3]

    system_hits = count_terms(text, SYSTEM_TERMS)
    material_hits = count_terms(text, MATERIAL_TERMS)
    evidence_hits = count_terms(text, EVIDENCE_TERMS)
    relevance = 12 + min(core_hits, 3) * 7 + min(sum(track_hits.values()), 8) * 4 + min(system_hits, 5) * 4
    relevance += min(len(set(record.get("query_ids", []))), 3) * 3
    if any(term in text for term in ("tactile", "electronic skin", "e-skin")) and system_hits >= 3:
        relevance += 12
    material_penalty = 0
    if material_hits >= 2 and system_hits < 2:
        material_penalty = 16
        relevance -= material_penalty

    publication = record.get("date", "")
    recency = 0
    try:
        age = max(0, (today - date.fromisoformat(publication[:10])).days)
        recency = 8 if age <= 7 else 5 if age <= 30 else 2 if age <= 365 else 0
    except (ValueError, TypeError):
        pass
    relevance += recency
    relevance = max(0, min(100, relevance))

    evidence = min(100, 30 + evidence_hits * 9 + (15 if record.get("abstract") else 0) + (10 if record.get("doi") else 0))
    transferability = min(100, 20 + system_hits * 10 + sum(5 for track in tracks if track in {"P1", "P2", "P3", "P4", "P5"}))
    innovation = min(
        100,
        25
        + count_terms(
            text,
            (
                "novel", "new", "first", "programmable", "computing", "decoupl",
                "robust", "end-to-end", "feature extraction", "reconfigur", "integrated",
            ),
        )
        * 10,
    )
    total = round(relevance * 0.5 + evidence * 0.15 + transferability * 0.25 + innovation * 0.1)
    if "P4" in tracks and "tactile" in text and any(term in text for term in ("integrated", "on-chip", "feature extraction")):
        total = min(100, total + 10)

    if total >= 80:
        hint = "read"
    elif total >= 68:
        hint = "add_to_ideas"
    elif total >= 58:
        hint = "skim"
    elif is_targeted_venue_record(record) and total >= 28:
        hint = "skim"
    else:
        hint = "ignore"

    reasons = []
    for track in tracks:
        reasons.append(track_reason(track))
    if material_penalty:
        reasons.append("材料性能词较多、前端/阵列/系统证据偏少，已降权")
    if not reasons:
        reasons.append("与柔性触觉相关，但尚未显示对前端触觉计算的直接贡献")

    return {
        "tracks": tracks or ["P6"],
        "relevance_score": total,
        "score_breakdown": {
            "topic_relevance": relevance,
            "evidence_strength": evidence,
            "transferability": transferability,
            "innovation_density": innovation,
            "material_only_penalty": material_penalty,
        },
        "relevance_reasons": reasons,
        "decision_hint": hint,
    }


def track_reason(track: str) -> str:
    return {
        "P1": "可用于低离散/装配容差触觉界面的结构与对照设计",
        "P2": "涉及 ADC 前模拟矢量、剪切/摩擦/方向相关触觉读出",
        "P3": "涉及低冗余阵列、空间特征或读出通道压缩",
        "P4": "涉及 in-sensor/物理计算或可编程触觉前端",
        "P5": "涉及坏点、漂移、跨器件迁移或少样本校准",
        "P6": "提供机器人、可穿戴或电子皮肤系统任务证据",
    }.get(track, "与当前研究画像相关")


def sentence_summary(record: dict[str, Any]) -> str:
    abstract = record.get("abstract", "").strip()
    if not abstract:
        return "当前仅获得题录信息，需要打开 DOI/原文核实机制、实验和性能指标。"
    sentences = re.split(r"(?<=[.!?])\s+", abstract)
    return sentences[0][:520]


def method_summary(record: dict[str, Any]) -> str:
    abstract = record.get("abstract", "").strip()
    if not abstract:
        return "当前题录没有摘要，需打开原文核实方法。"
    sentences = re.split(r"(?<=[.!?])\s+", abstract)
    method_terms = ("present", "propose", "develop", "design", "implement", "using", "based on")
    selected = next(
        (sentence for sentence in sentences if any(term in sentence.lower() for term in method_terms)),
        sentences[0],
    )
    return selected[:620]


def extract_metrics(record: dict[str, Any]) -> list[str]:
    abstract = record.get("abstract", "")
    pattern = re.compile(
        r"(?<![A-Za-z0-9])(?:\d+(?:\.\d+)?(?:\s*(?:±|\+/-)\s*\d+(?:\.\d+)?)?)\s*"
        r"(?:%|mW|µW|uW|W|ms|µs|us|s|Hz|kHz|MHz|dB|Pa|kPa|MPa|N|mN|V|mV|A|mA|"
        r"mm|µm|um|cm|nm|fps|classes|class)(?![A-Za-z])",
        flags=re.IGNORECASE,
    )
    metrics = []
    for match in pattern.finditer(abstract):
        value = re.sub(r"\s+", " ", match.group(0)).strip()
        if value not in metrics:
            metrics.append(value)
        if len(metrics) >= 10:
            break
    return metrics


def enrich_record(record: dict[str, Any], today: date) -> dict[str, Any]:
    scoring = score_record(record, today)
    tracks = scoring["tracks"]
    title = record.get("title", "")
    doi = normalize_doi(record.get("doi"))
    transfer = [track_reason(track) for track in tracks[:2]]
    if "P2" in tracks:
        transfer.append("优先核查是否有 hardware output 与 software projection 的同步一致性证据")
    if "P4" in tracks or "P5" in tracks:
        transfer.append("可对照 raw pixel、software feature 与 physical projection 的性能/通道/功耗")
    risks = ["当前为题录/摘要级初筛，论文结论、对照和数值必须在精读全文后核实。"]
    metrics = extract_metrics(record)
    if scoring["score_breakdown"]["material_only_penalty"]:
        risks.append("可能主要贡献是材料灵敏度，未必能支撑前端触觉计算主线。")
    if any(term in (title + " " + record.get("abstract", "")).lower() for term in ("three-axis", "triaxial", "3d force")):
        risks.append("如无完整标定矩阵，不应直接迁移为 full 3D force reconstruction 主张。")
    return {
        "id": f"paper-{stable_id(title, doi)}",
        "title": title,
        "authors": record.get("authors", []),
        "venue": record.get("venue", ""),
        "date": record.get("date", ""),
        "doi": doi,
        "url": record.get("url", "") or (f"https://doi.org/{doi}" if doi else ""),
        "pdf_url": record.get("pdf_url", ""),
        "pdf_candidates": record.get("pdf_candidates", []),
        "local_pdf": "",
        "is_open_access": bool(record.get("is_open_access")),
        "paper_type": record.get("paper_type", ""),
        "venue_quality": venue_quality_tier(record),
        "sources": record.get("sources", []),
        "query_ids": record.get("query_ids", []),
        "tracks": tracks,
        "relevance_score": scoring["relevance_score"],
        "score_breakdown": scoring["score_breakdown"],
        "relevance_reasons": scoring["relevance_reasons"],
        "core_claim": sentence_summary(record),
        "summary_zh": (
            "；".join(scoring["relevance_reasons"][:2])
            + (f"。摘要可核实数值包括：{'、'.join(metrics[:5])}" if metrics else "。当前未从摘要提取到可比较数值")
            + "。"
        ),
        "method_summary": method_summary(record),
        "key_metrics": metrics,
        "transferable_points": transfer,
        "risks": risks,
        "source_abstract": record.get("abstract", ""),
        "cited_by_count": int(record.get("cited_by_count") or 0),
        "decision_hint": scoring["decision_hint"],
        "verification_status": "metadata_abstract_screened",
    }


IDEA_TEMPLATES = {
    "P1": {
        "title": "把论文中的结构机制转成偏移/旋转/接触半径容差地图",
        "hypothesis": "若界面机制真正降低输入离散性，其优势应在装配扰动和接触条件变化下保持，而不只体现在灵敏度。",
        "minimum_experiment": "在统一载荷下扫描 shift、rotation 与 contact radius，输出 CV、signal-void ratio 和 sensitivity map。",
        "controls": ["周期电极+常规微结构", "周期电极+HCP", "梯度/非周期电极+常规微结构", "目标结构"],
        "success_metrics": ["CV", "shift sensitivity", "rotation sensitivity", "contact-radius sensitivity", "signal void ratio"],
    },
    "P2": {
        "title": "把新型矢量/剪切读出转成 ADC 前硬件-软件一致性证据",
        "hypothesis": "ADC 前 Kz/Kx/Ky 类模拟组合应保留任务相关方向信息，并减少后端通道和计算。",
        "minimum_experiment": "同步记录 raw A/B/C/D、software vector 与 hardware vector，在相同纹理/滑动/剪切输入下做波形、PSD/SNR、R2 和任务消融。",
        "controls": ["raw four-channel", "z-only", "software vector", "hardware vector", "reference force"],
        "success_metrics": ["hardware-software R2", "PSD/SNR", "task accuracy", "latency", "ADC channel count"],
    },
    "P3": {
        "title": "把论文的阵列读出策略改写为低冗余 hardware macro-pixel 对照",
        "hypothesis": "可解释的局部矢量/空间投影能以更少读出通道保持边缘、形状和滑移方向信息。",
        "minimum_experiment": "在同一阵列输入上比较 raw scanning、scalar pooling、software gradient 与 hardware macro-pixel。",
        "controls": ["raw pixel scanning", "scalar pooling", "software gradient", "hardware macro-pixel"],
        "success_metrics": ["channel count", "latency", "power", "edge/shape accuracy", "direction accuracy"],
    },
    "P4": {
        "title": "把论文机制映射为 3x3 可编程物理触觉投影核",
        "hypothesis": "Ksum/Kx/Ky/Klap/Kring/Kcorner 等可解释投影可在 ADC 前形成，并与软件投影保持一致。",
        "minimum_experiment": "先用 3x3 精密电阻阵列施加标准图案，再迁移到触觉阵列，比较六类投影核的硬件与软件输出。",
        "controls": ["raw scanning", "software projection", "fixed hardware kernel", "programmable hardware kernel"],
        "success_metrics": ["hardware-software R2", "linearity", "kernel switching error", "ADC count", "latency"],
    },
    "P5": {
        "title": "把论文的鲁棒/迁移策略加入物理投影坏点渐进退化实验",
        "hypothesis": "归一化物理投影特征在坏点、漂移和跨器件变化下应比 raw readout 更平滑退化，并减少重标定样本。",
        "minimum_experiment": "设置 0/1/5/10/20% 等效坏点与增益漂移，比较 raw、software projection、hardware projection 及少样本校准。",
        "controls": ["raw readout", "software projection", "hardware projection", "hardware projection + few-shot calibration"],
        "success_metrics": ["accuracy degradation", "feature drift", "calibration samples", "fault ratio", "cross-device variance"],
    },
    "P6": {
        "title": "把论文系统任务压缩成不拖累主线的最小闭环演示",
        "hypothesis": "一个受控的纹理/滑移/抓取演示足以证明前端特征的任务价值，无需把主张扩展成完整机器人系统。",
        "minimum_experiment": "选择单一任务，固定机械输入和后端分类器，只消融 raw、z-only 与前端矢量/投影特征。",
        "controls": ["raw signal", "z-only", "front-end vector/projection"],
        "success_metrics": ["task accuracy", "response time", "channel count", "failure cases"],
    },
}


def make_ideas(papers: list[dict[str, Any]], run_date: date, minimum: int = 3) -> list[dict[str, Any]]:
    ideas: list[dict[str, Any]] = []
    used_tracks: set[str] = set()
    choices: list[tuple[dict[str, Any], str]] = []
    eligible_papers = [paper for paper in papers if paper.get("relevance_score", 0) >= 60]
    for paper in eligible_papers:
        tracks = paper.get("tracks", []) or ["P6"]
        for track in tracks:
            if track in IDEA_TEMPLATES and track not in used_tracks:
                choices.append((paper, track))
                used_tracks.add(track)
            if len(choices) >= 5:
                break
        if len(choices) >= 5:
            break
    for paper in eligible_papers:
        if len(choices) >= minimum:
            break
        track = next((item for item in paper.get("tracks", []) if item in IDEA_TEMPLATES), "P6")
        if (paper, track) not in choices:
            choices.append((paper, track))
    for index, (paper, track) in enumerate(choices[: max(minimum, 5)]):
        template = IDEA_TEMPLATES[track]
        source_key = paper.get("doi") or paper.get("id")
        idea_id = hashlib.sha1(f"{run_date}:{source_key}:{track}".encode("utf-8")).hexdigest()[:12]
        ideas.append(
            {
                "id": f"idea-{run_date.isoformat()}-{idea_id}",
                "status": "candidate",
                "grade": "A" if paper.get("relevance_score", 0) >= 82 else "B",
                "track": track,
                "title": template["title"],
                "source": paper.get("title", ""),
                "source_papers": [
                    {
                        "paper_id": paper.get("id"),
                        "title": paper.get("title"),
                        "doi": paper.get("doi", ""),
                        "url": paper.get("url", ""),
                    }
                ],
                "hypothesis": template["hypothesis"],
                "minimum_experiment": template["minimum_experiment"],
                "controls": template["controls"],
                "success_metrics": template["success_metrics"],
                "risk": "该 idea 是基于题录/摘要和用户画像生成的可验证假设，需先精读来源论文并做最小实验。",
                "profile_update_recommendation": "先进入候选池；只有用户在网页中确认并接受画像提案后才写入研究画像。",
                "created_at": datetime.now(timezone.utc).isoformat(),
            }
        )
    return ideas


def historical_keys(exclude_date: date) -> set[str]:
    keys: set[str] = set()
    literature = MEMORY / "literature"
    if not literature.exists():
        return keys
    for path in literature.glob("*/*/summaries/papers.json"):
        if exclude_date.isoformat() in path.parts:
            continue
        payload = load_json(path, {"papers": []})
        for paper in payload.get("papers", []):
            doi = normalize_doi(paper.get("doi"))
            keys.add(f"doi:{doi}" if doi else f"title:{normalize_title(paper.get('title', ''))}")
    return keys


def paper_key(paper: dict[str, Any]) -> str:
    doi = normalize_doi(paper.get("doi"))
    return f"doi:{doi}" if doi else f"title:{normalize_title(paper.get('title', ''))}"


def download_open_access_pdfs(papers: list[dict[str, Any]], output_dir: Path, limit: int) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    downloaded = 0
    for paper in papers:
        if downloaded >= limit:
            break
        errors = []
        for pdf_url in legal_pdf_candidates(paper):
            try:
                raw, content_type = request_pdf_bytes(pdf_url, timeout=40)
                if len(raw) > 40 * 1024 * 1024:
                    errors.append("PDF 超过 40 MB")
                    continue
                if not raw.startswith(b"%PDF") and (
                    pdf_url.lower().endswith((".tar.gz", ".tgz"))
                    or "gzip" in content_type.lower()
                ):
                    raw = pdf_from_oa_package(raw) or raw
                if not (raw.startswith(b"%PDF") or "application/pdf" in content_type.lower()):
                    errors.append("链接未返回 PDF")
                    continue
                path = output_dir / f"{paper['id']}.pdf"
                path.write_bytes(raw)
                paper["pdf_url"] = pdf_url
                paper["pdf_source_url"] = pdf_url
                paper["pdf_version"], paper["pdf_version_label"] = classify_pdf_version(pdf_url)
                paper["is_open_access"] = True
                paper["local_pdf"] = str(path.relative_to(ROOT)).replace("\\", "/")
                downloaded += 1
                break
            except Exception as error:  # noqa: BLE001 - try the next lawful OA candidate
                errors.append(type(error).__name__)
        if not paper.get("local_pdf"):
            summary = "、".join(dict.fromkeys(errors)) if errors else "未找到合法开放获取 PDF"
            paper.setdefault("risks", []).append(f"开放获取 PDF 下载失败：{summary}。")


def append_ideas(ideas: list[dict[str, Any]], run_date: date) -> None:
    path = MEMORY / "ideas" / "idea-log.json"
    payload = load_json(path, {"updated_at": "", "ideas": []})
    prefix = f"idea-{run_date.isoformat()}-"
    retained = [
        idea
        for idea in payload.get("ideas", [])
        if not (str(idea.get("id", "")).startswith(prefix) and idea.get("status") == "candidate")
    ]
    existing = {idea.get("id") for idea in retained}
    retained.extend(idea for idea in ideas if idea.get("id") not in existing)
    payload["ideas"] = retained
    payload["updated_at"] = run_date.isoformat()
    write_json(path, payload)


def retain_existing_results_on_empty_refresh(
    papers: list[dict[str, Any]],
    ideas: list[dict[str, Any]],
    existing_payload: dict[str, Any],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], bool]:
    """Keep a same-day result set when a repeat refresh yields no eligible papers."""
    existing_papers = existing_payload.get("papers") or []
    if papers or not existing_papers:
        return papers, ideas, False
    return existing_papers, existing_payload.get("generated_ideas") or [], True


def report_markdown(
    run_date: date,
    window_days: int,
    query_log: list[dict[str, Any]],
    papers: list[dict[str, Any]],
    ideas: list[dict[str, Any]],
    source_errors: list[dict[str, str]],
    excluded_seen: int,
    excluded_venue: int,
) -> str:
    must_read = [
        paper
        for paper in papers
        if paper["relevance_score"] >= 80 or paper.get("decision_hint") == "read"
    ][:3]
    must_read_ids = {paper["id"] for paper in must_read}
    tracking = [
        paper
        for paper in papers
        if 60 <= paper["relevance_score"] < 80 and paper["id"] not in must_read_ids
    ][:8]
    lines = [
        f"# {run_date.isoformat()} 柔性电子皮肤前端触觉计算文献日报",
        "",
        "## 今日结论",
        "",
        f"本次从 OpenAlex、Crossref、Semantic Scholar 和 arXiv 检索最近 {window_days} 天结果，去重并排除历史已收录论文后保留 {len(papers)} 篇。",
        "期刊等级采用硬门槛：仅保留 Nature/Science/Cell 子刊、Advanced Materials 系列及明确同等级期刊；预印本、会议论文和普通期刊不进入正式推荐。",
        "通过期刊门槛后，再优先考虑 ADC 前模拟触觉、矢量/剪切/摩擦读出、低冗余阵列、物理投影和容错迁移。",
        "",
        f"- 今日必看：{len(must_read)} 篇",
        f"- 值得追踪：{len(tracking)} 篇",
        f"- 新增可评估 idea：{len(ideas)} 个",
        f"- 历史重复排除：{excluded_seen} 篇",
        f"- 期刊等级排除：{excluded_venue} 篇",
        "",
        "## 今日必看",
        "",
    ]
    if not must_read:
        lines.extend(["今日没有达到精读阈值的论文；不要为了凑数把普通高灵敏材料论文推到顶部。", ""])
    for index, paper in enumerate(must_read, 1):
        link = paper.get("url") or (f"https://doi.org/{paper['doi']}" if paper.get("doi") else "")
        lines.extend(
            [
                f"### {index}. [{paper['title']}]({link})" if link else f"### {index}. {paper['title']}",
                "",
                f"- 来源：{paper.get('venue') or '未标注'}；{paper.get('date') or '日期未知'}；评分 {paper['relevance_score']}/100",
                f"- 为什么重要：{'；'.join(paper['relevance_reasons'][:2])}",
                f"- 摘要级结论：{paper.get('summary_zh') or paper['core_claim']}",
                f"- 方法：{paper.get('method_summary', '需精读原文核实')}",
                f"- 摘要数值：{'、'.join(paper.get('key_metrics', [])) or '未提取到可比较数值'}",
                f"- 可迁移：{'；'.join(paper['transferable_points'][:3])}",
                f"- 风险：{'；'.join(paper['risks'][:2])}",
                f"- 建议操作：{paper['decision_hint']}",
                "",
            ]
        )
    lines.extend(["## 值得追踪", "", "| 评分 | 轨道 | 论文 | 建议 |", "|---:|---|---|---|"])
    for paper in tracking:
        link = paper.get("url") or (f"https://doi.org/{paper['doi']}" if paper.get("doi") else "")
        title = f"[{paper['title']}]({link})" if link else paper["title"]
        lines.append(f"| {paper['relevance_score']} | {', '.join(paper['tracks'])} | {title} | {paper['decision_hint']} |")
    if not tracking:
        lines.append("| - | - | 今日无新增候选 | - |")
    lines.extend(
        [
            "",
            "## 方法与指标速览",
            "",
            "| 论文 | 方法（摘要证据） | 可核实数值 | 画像价值 |",
            "|---|---|---|---|",
        ]
    )
    for paper in papers:
        short_title = paper["title"].replace("|", "/")
        method = paper.get("method_summary", "需精读核实").replace("|", "/")[:220]
        metrics = "、".join(paper.get("key_metrics", [])) or "摘要未给出"
        value = "；".join(paper.get("relevance_reasons", [])[:2]).replace("|", "/")
        lines.append(f"| {short_title} | {method} | {metrics} | {value} |")
    lines.extend(["", "## 今日创新点候选", ""])
    for index, idea in enumerate(ideas, 1):
        source = idea.get("source_papers", [{}])[0]
        lines.extend(
            [
                f"### Idea {index}：{idea['title']}",
                "",
                f"- 对应轨道：{idea['track']}；分级：{idea['grade']}",
                f"- 来源论文：{source.get('title', '')}",
                f"- 核心假设：{idea['hypothesis']}",
                f"- 最小实验：{idea['minimum_experiment']}",
                f"- 对照：{'；'.join(idea['controls'])}",
                f"- 成功指标：{'；'.join(idea['success_metrics'])}",
                "- 用户操作：加入画像提案 / 观察 / 转任务 / 拒绝",
                "",
            ]
        )
    lines.extend(
        [
            "## 检索记录",
            "",
            "| 来源 | 目标期刊 | 查询 | 命中 | 状态 |",
            "|---|---|---|---:|---|",
        ]
    )
    for item in query_log:
        target_venue = item.get("container_title") or "-"
        lines.append(
            f"| {item['source']} | {target_venue} | `{item['query']}` | "
            f"{item['result_count']} | {item['status']} |"
        )
    if source_errors:
        lines.extend(["", "## 数据源异常", ""])
        grouped_errors: dict[str, list[dict[str, str]]] = {}
        for item in source_errors:
            grouped_errors.setdefault(item["source"], []).append(item)
        for source, items in grouped_errors.items():
            first_error = items[0]["error"]
            lines.append(f"- {source}：{len(items)} 个查询失败；首个错误为 {first_error}。其余来源已继续运行。")
    lines.extend(
        [
            "",
            "## 纳入与排除标准",
            "",
            "- 纳入：论文能服务 P1-P6 至少一条主线，并能形成机制、前端、阵列、系统任务或可验证对照。",
            "- 降权：只强调 sensitivity、gauge factor 或材料配方，而缺少读出、阵列、校准、鲁棒性或任务证据。",
            "- 排除：历史已收录、题录明显偏题、来源元数据不足且无法核实。",
            "- 可信度边界：本日报首先完成题录/摘要级筛选；数值、机理和优先级需在点击“精读”后核查全文。",
            "",
        ]
    )
    return "\n".join(lines)


def run_git_sync(run_date: date) -> None:
    paths = [
        "research-memory/literature",
        "research-memory/ideas/idea-log.json",
        "web/data/research-bundle.json",
    ]
    subprocess.run(["git", "add", "--", *paths], cwd=ROOT, check=True)
    diff = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=ROOT)
    if diff.returncode == 0:
        return
    subprocess.run(
        ["git", "commit", "-m", f"docs: add literature report for {run_date.isoformat()}"],
        cwd=ROOT,
        check=True,
    )
    subprocess.run(["git", "push", "origin", "HEAD"], cwd=ROOT, check=True)


def search_window(
    config: dict[str, Any],
    run_date: date,
    window_days: int,
    disabled_sources: set[str] | None = None,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, str]], set[str]]:
    disabled_sources = disabled_sources or set()
    jobs = []
    from_date = run_date - timedelta(days=window_days)
    for query in configured_search_queries(config):
        for source in query.get("sources", []):
            if source in SEARCHERS and source not in disabled_sources:
                jobs.append(
                    SearchJob(
                        query_id=query["id"],
                        query=query["query"],
                        source=source,
                        tracks=tuple(query.get("tracks", [])),
                        from_date=from_date,
                        to_date=run_date,
                        container_title=str(query.get("container_title") or ""),
                        issn=str(query.get("issn") or ""),
                    )
                )
    records: list[dict[str, Any]] = []
    query_log: list[dict[str, Any]] = []
    errors: list[dict[str, str]] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        future_jobs = {pool.submit(SEARCHERS[job.source], job): job for job in jobs}
        for future in concurrent.futures.as_completed(future_jobs):
            job = future_jobs[future]
            try:
                found = future.result()
                records.extend(found)
                query_log.append(
                    {
                        "source": job.source,
                        "query_id": job.query_id,
                        "query": job.query,
                        "container_title": job.container_title,
                        "result_count": len(found),
                        "status": "ok",
                    }
                )
            except Exception as error:  # noqa: BLE001 - continue remaining scholarly sources
                message = re.sub(r"\s+", " ", str(error))[:260]
                errors.append({"source": job.source, "query_id": job.query_id, "error": message})
                query_log.append(
                    {
                        "source": job.source,
                        "query_id": job.query_id,
                        "query": job.query,
                        "container_title": job.container_title,
                        "result_count": 0,
                        "status": "failed",
                    }
                )
    query_log.sort(key=lambda item: (item["query_id"], item["source"]))
    attempted = {source: 0 for source in SEARCHERS}
    failed = {source: 0 for source in SEARCHERS}
    for item in query_log:
        attempted[item["source"]] = attempted.get(item["source"], 0) + 1
        if item["status"] == "failed":
            failed[item["source"]] = failed.get(item["source"], 0) + 1
    fully_failed = {
        source for source, count in attempted.items() if count and failed.get(source, 0) == count
    }
    return records, query_log, errors, fully_failed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", dest="run_date", help="Run date in YYYY-MM-DD format")
    parser.add_argument("--max-papers", type=int, default=0, help="Override maximum paper count")
    parser.add_argument(
        "--lookback-days",
        type=int,
        default=0,
        help="Force one search window, for example 30 for a monthly backfill",
    )
    parser.add_argument("--no-pdf", action="store_true", help="Do not download legal open-access PDFs")
    parser.add_argument("--git-sync", action="store_true", help="Commit and push generated artifacts")
    parser.add_argument("--dry-run", action="store_true", help="Search and score without writing files")
    args = parser.parse_args()

    run_date = date.fromisoformat(args.run_date) if args.run_date else date.today()
    config = load_json(CONFIG_PATH, {})
    minimum = int(config.get("minimum_candidates", 6))
    maximum = args.max_papers or int(config.get("maximum_candidates", 12))
    seen = historical_keys(run_date)

    chosen_records: list[dict[str, Any]] = []
    final_log: list[dict[str, Any]] = []
    final_errors: list[dict[str, str]] = []
    seen_error_keys: set[tuple[str, str]] = set()
    disabled_sources: set[str] = set()
    excluded_seen = 0
    excluded_venue = 0
    used_window = int(config.get("lookback_windows_days", [30])[-1])
    search_windows = (
        [args.lookback_days]
        if args.lookback_days > 0
        else config.get("lookback_windows_days", [3, 7, 30])
    )
    for window in search_windows:
        records, query_log, errors, fully_failed = search_window(
            config, run_date, int(window), disabled_sources
        )
        disabled_sources.update(fully_failed)
        merged = merge_records(records)
        on_topic = [record for record in merged if is_on_topic(record)]
        fresh = [record for record in on_topic if paper_key(record) not in seen]
        qualified = [record for record in fresh if meets_venue_quality(record)]
        actionable = [record for record in qualified if is_actionable_candidate(record, run_date)]
        chosen_records = actionable
        final_log = query_log
        excluded_seen = len(on_topic) - len(fresh)
        excluded_venue = len(fresh) - len(qualified)
        for error in errors:
            key = (error["source"], error["query_id"])
            if key not in seen_error_keys:
                final_errors.append(error)
                seen_error_keys.add(key)
        used_window = int(window)
        if len(actionable) >= minimum:
            break

    enriched = [enrich_record(record, run_date) for record in chosen_records]
    enriched.sort(key=lambda item: (item["relevance_score"], item.get("date", "")), reverse=True)
    papers = enriched[:maximum]

    ideas = make_ideas(papers, run_date, minimum=3) if papers else []
    day_dir = MEMORY / "literature" / str(run_date.year) / run_date.isoformat()
    papers_path = day_dir / "summaries" / "papers.json"
    report_path = day_dir / "daily-report.md"

    if args.dry_run:
        print(json.dumps({"window_days": used_window, "papers": papers, "ideas": ideas, "errors": final_errors}, ensure_ascii=False, indent=2))
        return 0

    existing_payload = load_json(papers_path, {})
    papers, ideas, retained_existing = retain_existing_results_on_empty_refresh(
        papers, ideas, existing_payload
    )

    if not args.no_pdf:
        download_open_access_pdfs(
            papers,
            day_dir / "papers",
            int(config.get("open_access_pdf_limit", 3)),
        )
    build_deep_reads(papers, day_dir)
    payload = {
        "date": run_date.isoformat(),
        "searched_at": datetime.now(timezone.utc).isoformat(),
        "search_window_days": used_window,
        "query_log": final_log,
        "source_errors": final_errors,
        "screening_policy": {
            "profile": "flexible electronic skin front-end tactile computing",
            "minimum_score": 48,
            "minimum_venue_level": "Nature/Science/Cell subjournal or Advanced Materials equivalent",
            "preprints_and_conference_papers_excluded": True,
            "material_only_papers_are_downranked": True,
            "verification_level": "metadata and abstract screening",
            "refresh_status": (
                "retained_existing_results_after_empty_refresh"
                if retained_existing
                else "fresh_results"
            ),
        },
        "papers": papers,
        "generated_ideas": ideas,
    }
    write_json(papers_path, payload)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(
        report_markdown(
            run_date,
            used_window,
            final_log,
            papers,
            ideas,
            final_errors,
            excluded_seen,
            excluded_venue,
        ),
        encoding="utf-8",
    )
    append_ideas(ideas, run_date)
    subprocess.run([sys.executable, str(ROOT / "scripts" / "build_research_intelligence.py")], cwd=ROOT, check=True)
    if args.git_sync:
        run_git_sync(run_date)
    print(f"Archived {len(papers)} papers and {len(ideas)} ideas for {run_date.isoformat()}")
    if final_errors:
        print(f"Completed with {len(final_errors)} source errors; see papers.json", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

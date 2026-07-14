#!/usr/bin/env python3
"""Build source-grounded paper detail bundles from lawful open-access PDFs."""

from __future__ import annotations

import argparse
import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

try:
    import fitz  # type: ignore
except ImportError:  # pragma: no cover - handled as a visible draft state
    fitz = None


ROOT = Path(__file__).resolve().parents[1]
MEMORY = ROOT / "research-memory"
WEB = ROOT / "web"

METHOD_HEADING = re.compile(
    r"^(?:\d+(?:\.\d+)*\s*)?(materials? and methods?|methods?|experimental section|"
    r"experimental methods?|fabrication|device fabrication|sample preparation|methods summary)$",
    re.IGNORECASE,
)
METHOD_HEADING_ANYWHERE = re.compile(
    r"(?:^|\s)(materials? and methods?|experimental section|experimental methods?|"
    r"device fabrication|sample preparation|methods summary)(?:\s|[.:—-]|$)",
    re.IGNORECASE,
)
METHOD_HEADING_PREFIX = re.compile(r"^(?:\d+(?:\.\d+)*\s*)?methods?\b", re.IGNORECASE)
SECTION_STOP = re.compile(
    r"^(?:\d+(?:\.\d+)*\s*)?(results?|discussion|conclusions?|references|"
    r"data availability|acknowledg(?:e)?ments?|supplementary information)$",
    re.IGNORECASE,
)
SECTION_STOP_PREFIX = re.compile(
    r"^(?:\d+(?:\.\d+)*\s*)?(?:results?|discussion|conclusions?|references|"
    r"data availability|code availability|acknowledg(?:e)?ments?|author contributions|"
    r"conflict of interest|supplementary information)(?:\s|$)",
    re.IGNORECASE,
)
FIGURE_START = re.compile(r"^\s*(fig(?:ure)?\.?\s*(?:s?\d+)[a-z]?)\s*[.:]?\s*(.*)", re.IGNORECASE)
PANEL_MARKER = re.compile(r"(?:\(([a-z])\)|(?<![A-Za-z])([A-Z])\.)\s+", re.IGNORECASE)
NATURE_PANEL_MARKER = re.compile(
    r"(?:(?<=\.\s)|(?<=;\s))([a-z])(?:\s*([-–,])\s*([a-z]))?[,.)]?\s+",
    re.IGNORECASE,
)
PREPARATION_VERBS = (
    "prepare", "fabricat", "mix", "dispers", "stir", "sonicat", "dissolv",
    "coat", "spin-coat", "deposit", "print", "laser", "etch", "pattern",
    "cure", "dry", "anneal", "bake", "assemble", "bond", "encapsulat",
    "laminat", "cast", "mold", "polymeriz", "transfer", "sputter", "evaporat",
)
PREPARATION_ACTION = re.compile(
    r"\b(?:prepar(?:e|ed|es|ing|ation)|fabricat(?:e|ed|es|ing|ion)|construct(?:ed|ion)|"
    r"mix(?:ed|es|ing)?|dispers(?:e|ed|es|ing|ion)|stir(?:red|ring|s)?|"
    r"sonicat(?:e|ed|es|ing|ion)|dissolv(?:e|ed|es|ing)|coat(?:ed|ing|s)?|"
    r"spin[- ]coat(?:ed|ing)?|deposit(?:ed|ing|ion)|print(?:ed|ing|s)?|"
    r"laser(?:ed|ing|[- ]cutting|[- ]pattern(?:ed|ing)?)|etch(?:ed|ing|es)?|"
    r"pattern(?:ed|ing|s)?|cure(?:d|s|ing)?|"
    r"dry(?:ied|ing|ies)?|anneal(?:ed|ing|s)?|bak(?:e|ed|ing)|assembl(?:e|ed|ing|y)|"
    r"bond(?:ed|ing|s)?|encapsulat(?:e|ed|ing|ion)|laminat(?:e|ed|ing|ion)|"
    r"cast(?:ed|ing|s)?|mold(?:ed|ing|s)?|polymeriz(?:e|ed|ing|ation)|"
    r"transfer(?:red|ring|s)?|sputter(?:ed|ing|s)?|evaporat(?:e|ed|ing|ion))\b",
    re.IGNORECASE,
)


def read_json(path: Path, fallback: Any) -> Any:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else fallback


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def clean_text(value: str) -> str:
    value = value.replace("\u00ad", "").replace("\ufb01", "fi").replace("\ufb02", "fl")
    value = re.sub(r"(?<=\w)-\n(?=\w)", "", value)
    return re.sub(r"\s+", " ", value).strip()


def first_line(value: str) -> str:
    return clean_text(value.splitlines()[0] if value.splitlines() else value)


def is_heading(value: str) -> bool:
    line = first_line(value)
    if not line or len(line) > 100:
        return False
    return bool(METHOD_HEADING.match(line) or SECTION_STOP.match(line))


def split_panel_caption(caption: str) -> list[dict[str, str]]:
    nature_matches = []
    expected = "a"
    for match in NATURE_PANEL_MARKER.finditer(caption):
        start = match.group(1).lower()
        end = (match.group(3) or start).lower()
        if start != expected or end < start:
            continue
        nature_matches.append(match)
        expected = chr(ord(end) + 1)
    matches = nature_matches if len(nature_matches) >= 2 else list(PANEL_MARKER.finditer(caption))
    panels = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(caption)
        text = clean_text(caption[match.end():end].strip(" .;:"))
        if text:
            if match.re is NATURE_PANEL_MARKER:
                start_label = match.group(1).lower()
                end_label = (match.group(3) or start_label).lower()
                separator = "," if match.group(2) == "," else "-"
                label = (
                    start_label
                    if start_label == end_label
                    else f"{start_label}{separator}{end_label}"
                )
            else:
                label = (match.group(1) or match.group(2)).lower()
            panels.append({"label": label, "original": text})
    return panels


def reading_note_zh(text: str) -> str:
    value = text.lower()
    if any(term in value for term in ("fabrication", "schematic", "structure", "device design", "architecture")):
        return "重点查看器件结构、材料层次、信号路径和制备流程。"
    if any(term in value for term in ("calibration", "sensitivity", "linearity", "error", "response", "force")):
        return "重点查看标定方法、量程、误差、线性和动态响应，避免只比较单一灵敏度。"
    if any(term in value for term in ("array", "mapping", "spatial", "pixel", "image")):
        return "重点查看阵列规模、空间分辨率、串扰、读出通道和空间特征表达。"
    if any(term in value for term in ("robot", "grasp", "application", "recognition", "classification")):
        return "重点查看任务设置、基线、消融和失败案例，判断系统演示是否真正支撑前端价值。"
    if any(term in value for term in ("mechanism", "simulation", "model", "finite element")):
        return "重点查看机制模型与实验结果是否一致，以及关键结构参数的对照关系。"
    return "结合正文首次引用位置和原始图注核对该图的证据角色。"


def preparation_category(sentence: str) -> str:
    value = sentence.lower()
    if any(term in value for term in ("mix", "dispers", "stir", "sonicat", "dissolv")):
        return "材料混合与分散"
    if any(term in value for term in ("coat", "deposit", "print", "sputter", "evaporat")):
        return "成膜与沉积"
    if any(term in value for term in ("laser", "etch", "pattern", "mold", "cast")):
        return "图形化与结构成形"
    if any(term in value for term in ("cure", "dry", "anneal", "bake", "polymeriz", "oven")):
        return "固化与热处理"
    if any(term in value for term in ("assemble", "construct", "bond", "encapsulat", "laminat", "transfer")):
        return "组装与封装"
    return "制备与实验操作"


def page_blocks(document: Any) -> list[dict[str, Any]]:
    blocks = []
    for page_index in range(document.page_count):
        page = document.load_page(page_index)
        for block in page.get_text("blocks", sort=True):
            text = clean_text(str(block[4] or ""))
            if not text:
                continue
            blocks.append(
                {
                    "page": page_index + 1,
                    "bbox": [round(float(value), 2) for value in block[:4]],
                    "text": text,
                }
            )
    return blocks


def extract_method_blocks(blocks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    ordered: list[dict[str, Any]] = []
    pages = sorted({int(block["page"]) for block in blocks})
    for page in pages:
        page_items = [block for block in blocks if int(block["page"]) == page]
        if not page_items:
            continue
        min_x = min(float(block["bbox"][0]) for block in page_items)
        max_x = max(float(block["bbox"][2]) for block in page_items)
        midpoint = (min_x + max_x) / 2
        left = [block for block in page_items if float(block["bbox"][2]) <= midpoint + 12]
        right = [block for block in page_items if float(block["bbox"][0]) >= midpoint - 12]
        full = [block for block in page_items if block not in left and block not in right]
        if max_x - min_x > 300 and left and right:
            ordered.extend(sorted(full, key=lambda block: float(block["bbox"][1])))
            ordered.extend(sorted(left, key=lambda block: float(block["bbox"][1])))
            ordered.extend(sorted(right, key=lambda block: float(block["bbox"][1])))
        else:
            ordered.extend(page_items)

    selected: list[dict[str, Any]] = []
    active = False
    for block in ordered:
        line = first_line(block["text"])
        heading = (
            METHOD_HEADING.match(line)
            or METHOD_HEADING_PREFIX.match(line)
            or METHOD_HEADING_ANYWHERE.search(block["text"])
        )
        if heading:
            active = True
            trailing = clean_text(block["text"][heading.end():].strip(" .:-"))
            if len(trailing) >= 20:
                selected.append({**block, "text": trailing})
            continue
        if active and (SECTION_STOP.match(line) or SECTION_STOP_PREFIX.match(line)):
            break
        if active:
            selected.append(block)
    if selected:
        return selected[:100]
    return [
        block
        for block in blocks
        if PREPARATION_ACTION.search(block["text"])
    ][:40]


def extract_preparation_steps(method_blocks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    stitched: list[dict[str, Any]] = []
    for block in method_blocks:
        if (
            stitched
            and not re.search(r"[.!?]$", stitched[-1]["text"])
            and re.match(r"^(?:\d+(?:\.\d+)?\s*(?:h|min|s)\b|[a-z])", block["text"], re.IGNORECASE)
        ):
            stitched[-1]["text"] = clean_text(f"{stitched[-1]['text']} {block['text']}")
        else:
            stitched.append({**block})

    steps = []
    seen = set()
    for block in stitched:
        for sentence in re.split(r"(?<!Fig\.)(?<=[.!?])\s+", block["text"]):
            cleaned = clean_text(sentence)
            lowered = cleaned.lower()
            action_text = re.sub(
                r"\b(?:3[- ]?d|three-dimensional)[- ]printed\b",
                "",
                cleaned,
                flags=re.IGNORECASE,
            )
            if len(cleaned) < 24 or not PREPARATION_ACTION.search(action_text):
                continue
            key = re.sub(r"\W+", "", lowered)[:180]
            if key in seen:
                continue
            seen.add(key)
            category = preparation_category(cleaned)
            steps.append(
                {
                    "step": len(steps) + 1,
                    "page": block["page"],
                    "category_zh": category,
                    "original": cleaned[:1200],
                    "explanation_zh": f"{category}步骤，关键配比、时间、温度和设备参数以 p.{block['page']} 原文为准。",
                }
            )
            if len(steps) >= 16:
                return steps
    return steps


def figure_candidates(blocks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    figures = []
    seen = set()
    for block in blocks:
        match = FIGURE_START.match(block["text"])
        if not match or len(block["text"]) < 18:
            continue
        label = re.sub(r"\s+", " ", match.group(1)).strip().title()
        key = label.lower().replace(" ", "")
        if key in seen:
            continue
        seen.add(key)
        caption = clean_text(block["text"])
        figures.append({"label": label, "page": block["page"], "bbox": block["bbox"], "caption": caption})
    return figures[:24]


def union_rect(rects: Iterable[Any]) -> Any | None:
    values = list(rects)
    if not values:
        return None
    return fitz.Rect(
        min(rect.x0 for rect in values),
        min(rect.y0 for rect in values),
        max(rect.x1 for rect in values),
        max(rect.y1 for rect in values),
    )


def figure_crop(page: Any, caption_bbox: list[float]) -> tuple[Any, str]:
    caption_top = float(caption_bbox[1])
    page_area = max(1.0, page.rect.width * page.rect.height)
    image_rects = []
    for image in page.get_images(full=True):
        for rect in page.get_image_rects(image[0]):
            if rect.get_area() >= page_area * 0.012 and rect.y1 <= caption_top + 8:
                image_rects.append(rect)
    if image_rects:
        nearest_bottom = max(rect.y1 for rect in image_rects)
        grouped = [rect for rect in image_rects if rect.y1 >= nearest_bottom - page.rect.height * 0.38]
        result = union_rect(grouped)
        if result is not None:
            result.x0 = max(page.rect.x0, result.x0 - 5)
            result.y0 = max(page.rect.y0, result.y0 - 5)
            result.x1 = min(page.rect.x1, result.x1 + 5)
            result.y1 = min(caption_top - 2, result.y1 + 5)
            return result, "high"
    return fitz.Rect(18, 24, page.rect.width - 18, max(40, caption_top - 3)), "approximate"


def render_figures(document: Any, candidates: list[dict[str, Any]], output_dir: Path) -> list[dict[str, Any]]:
    output_dir.mkdir(parents=True, exist_ok=True)
    figures = []
    for index, item in enumerate(candidates, 1):
        page = document.load_page(item["page"] - 1)
        rect, confidence = figure_crop(page, item["bbox"])
        if rect.width < 40 or rect.height < 40:
            continue
        filename = f"figure-{index:02d}.png"
        pixmap = page.get_pixmap(matrix=fitz.Matrix(2, 2), clip=rect, alpha=False)
        pixmap.save(output_dir / filename)
        image_width = pixmap.width
        image_height = pixmap.height
        panels = []
        for panel in split_panel_caption(item["caption"]):
            panels.append(
                {
                    **panel,
                    "explanation_zh": reading_note_zh(panel["original"]),
                }
            )
        figures.append(
            {
                "id": f"F{index:03d}",
                "label": item["label"],
                "page": item["page"],
                "caption_original": item["caption"],
                "caption_zh": f"{item['label']} 原始图注已提取；逐项含义见下方分图说明。",
                "reading_note_zh": reading_note_zh(item["caption"]),
                "panels": panels,
                "image_filename": filename,
                "image_width": image_width,
                "image_height": image_height,
                "crop_confidence": confidence,
                "bbox": [round(value, 2) for value in rect],
            }
        )
    return figures


def source_map(blocks: list[dict[str, Any]], figures: list[dict[str, Any]], paper: dict[str, Any], pdf_path: Path) -> dict[str, Any]:
    source_blocks = []
    pages: dict[int, list[str]] = {}
    for index, block in enumerate(blocks, 1):
        block_id = f"S{index:04d}"
        source_blocks.append(
            {
                "id": block_id,
                "page": block["page"],
                "type": "heading" if is_heading(block["text"]) else "paragraph",
                "order": index,
                "original_text": block["text"],
                "translation": "",
                "bbox": block["bbox"],
                "confidence": "high",
                "refs": [],
            }
        )
        pages.setdefault(block["page"], []).append(block_id)
    return {
        "paper": {
            "title": paper.get("title", ""),
            "venue": paper.get("venue", ""),
            "source_type": "pdf",
            "language": "en",
            "source_path": str(pdf_path.relative_to(ROOT)).replace("\\", "/"),
        },
        "blocks": source_blocks,
        "pages": [{"page": page, "block_ids": ids} for page, ids in sorted(pages.items())],
        "figures": figures,
        "glossary": [],
    }


def paper_markdown(detail: dict[str, Any], method_blocks: list[dict[str, Any]]) -> str:
    lines = [
        f"# {detail['title']}",
        "",
        f"- 期刊：{detail.get('venue') or '未标注'}",
        f"- 日期：{detail.get('date') or '未标注'}",
        f"- DOI：{detail.get('doi') or '未标注'}",
        f"- 解析状态：{detail['status']}",
        "",
        "## 摘要与研究价值",
        "",
        f"**Original:** {detail['abstract']['original'] or 'PDF/题录未提供摘要。'}",
        "",
        f"**中文:** {detail['abstract']['zh'] or '等待智能体精读补充。'}",
        "",
        "## 创新点",
        "",
    ]
    lines.extend(f"- {item}" for item in detail.get("innovation_points", []))
    lines.extend(["", "## 对当前课题的启发", ""])
    lines.extend(f"- {item}" for item in detail.get("inspirations", []))
    lines.extend(["", "## 制备与实验步骤", ""])
    for step in detail.get("preparation_steps", []):
        lines.extend(
            [
                f"### {step['step']}. {step['category_zh']}",
                "",
                f"**Source:** p.{step['page']}",
                "",
                f"**Original:** {step['original']}",
                "",
                f"**中文:** {step['explanation_zh']}",
                "",
            ]
        )
    lines.extend(["## 方法原文锚点", ""])
    for index, block in enumerate(method_blocks, 1):
        lines.extend(
            [
                f"<a id=\"M{index:03d}\"></a>",
                f"**Source:** p.{block['page']} M{index:03d}",
                "",
                f"**Original:** {block['text']}",
                "",
                "**中文:** 该段已进入结构化方法步骤；完整逐段翻译待智能体精读补齐。",
                "",
            ]
        )
    lines.extend(["## 图表解读", ""])
    for figure in detail.get("figures", []):
        lines.extend(
            [
                f"<a id=\"{figure['id']}\"></a>",
                f"### {figure['label']}",
                "",
                f"**Source:** p.{figure['page']}",
                "",
                f"![{figure['label']}](assets/{figure['image_filename']})",
                "",
                f"**Original caption:** {figure['caption_original']}",
                "",
                f"**中文图注:** {figure['caption_zh']}",
                "",
                f"**Reading note:** {figure['reading_note_zh']}",
                "",
            ]
        )
        for panel in figure.get("panels", []):
            lines.append(f"- ({panel['label']}) {panel['explanation_zh']} 原文：{panel['original']}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def apply_curation(detail: dict[str, Any], detail_root: Path) -> dict[str, Any]:
    curation = read_json(detail_root / "curation.json", {})
    if not curation:
        detail["curation_status"] = "automatic_draft"
        return detail
    for field in ("innovation_points", "inspirations"):
        if curation.get(field):
            detail[field] = curation[field]
    if curation.get("abstract_zh"):
        detail["abstract"]["zh"] = curation["abstract_zh"]
    step_overrides = {
        int(item["step"]): item for item in curation.get("preparation_steps", []) if item.get("step")
    }
    for step in detail.get("preparation_steps", []):
        override = step_overrides.get(int(step["step"]))
        if override:
            step.update({key: value for key, value in override.items() if key != "step"})
    figure_overrides = {
        item["label"]: item for item in curation.get("figures", []) if item.get("label")
    }
    for figure in detail.get("figures", []):
        override = figure_overrides.get(figure["label"])
        if not override:
            continue
        for field in ("caption_zh", "explanation_zh", "reading_note_zh"):
            if override.get(field):
                figure[field] = override[field]
        panel_overrides = override.get("panels") or {}
        for panel in figure.get("panels", []):
            if panel.get("label") in panel_overrides:
                panel["explanation_zh"] = panel_overrides[panel["label"]]
    detail["curation_status"] = curation.get("status", "agent_reviewed")
    return detail


def build_metadata_only(paper: dict[str, Any], day_dir: Path) -> dict[str, Any]:
    detail_root = day_dir / "deep-reads" / paper["id"]
    detail = {
        "schema_version": 1,
        "id": paper["id"],
        "title": paper.get("title", ""),
        "authors": paper.get("authors", []),
        "venue": paper.get("venue", ""),
        "date": paper.get("date", ""),
        "doi": paper.get("doi", ""),
        "source_url": paper.get("url", ""),
        "pdf_source_url": "",
        "pdf_version": "unavailable",
        "pdf_version_label": "暂无可合法自动获取的开放全文",
        "status": "metadata_only_no_legal_pdf",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "page_count": 0,
        "abstract": {
            "original": paper.get("source_abstract", ""),
            "zh": paper.get("summary_zh", ""),
        },
        "innovation_points": [paper.get("core_claim", ""), *paper.get("relevance_reasons", [])],
        "inspirations": paper.get("transferable_points", []),
        "preparation_steps": [],
        "method_blocks": [],
        "figures": [],
        "original_pdf": "",
        "reader_markdown": str((detail_root / "paper.md").relative_to(ROOT)).replace("\\", "/"),
        "source_map": "",
        "notes": [
            "当前仅完成题录/摘要级筛选。",
            "未获得合法开放全文，因此不生成制备步骤、逐图解释或 PDF 副本。",
        ],
    }
    apply_curation(detail, detail_root)
    if detail.get("curation_status", "").startswith("agent_reviewed"):
        paper["summary_zh"] = detail["abstract"]["zh"]
        paper["verification_status"] = "abstract_agent_curated"
    detail_root.mkdir(parents=True, exist_ok=True)
    (detail_root / "paper.md").write_text(paper_markdown(detail, []), encoding="utf-8")
    write_json(detail_root / "detail.json", detail)
    write_json(WEB / "data" / "paper-details" / f"{paper['id']}.json", detail)
    paper["deep_read_status"] = detail["status"]
    paper["detail_path"] = f"paper.html?id={paper['id']}"
    paper["detail_json"] = f"data/paper-details/{paper['id']}.json"
    return detail


def build_one(paper: dict[str, Any], day_dir: Path) -> dict[str, Any] | None:
    local_pdf = str(paper.get("local_pdf") or "")
    if not local_pdf:
        return build_metadata_only(paper, day_dir)
    pdf_path = (ROOT / local_pdf).resolve()
    if not pdf_path.exists() or fitz is None:
        paper["deep_read_status"] = "draft_pdf_parser_unavailable"
        return None

    document = fitz.open(pdf_path)
    blocks = page_blocks(document)
    method_blocks = extract_method_blocks(blocks)
    steps = extract_preparation_steps(method_blocks)
    detail_root = day_dir / "deep-reads" / paper["id"]
    assets_dir = detail_root / "assets"
    figures = render_figures(document, figure_candidates(blocks), assets_dir)

    web_root = WEB / "papers" / paper["id"]
    web_figures = web_root / "figures"
    web_figures.mkdir(parents=True, exist_ok=True)
    for figure in figures:
        shutil.copy2(assets_dir / figure["image_filename"], web_figures / figure["image_filename"])
        figure["image_path"] = f"papers/{paper['id']}/figures/{figure['image_filename']}"
    shutil.copy2(pdf_path, web_root / "original.pdf")

    detail = {
        "schema_version": 1,
        "id": paper["id"],
        "title": paper.get("title", ""),
        "authors": paper.get("authors", []),
        "venue": paper.get("venue", ""),
        "date": paper.get("date", ""),
        "doi": paper.get("doi", ""),
        "source_url": paper.get("url", ""),
        "pdf_source_url": paper.get("pdf_source_url", paper.get("pdf_url", "")),
        "pdf_version": paper.get("pdf_version", "repository_or_author_copy"),
        "pdf_version_label": paper.get(
            "pdf_version_label", "作者或机构仓储合法公开版本"
        ),
        "status": "fulltext_draft" if blocks else "metadata_only",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "page_count": document.page_count,
        "abstract": {
            "original": paper.get("source_abstract", ""),
            "zh": paper.get("summary_zh", ""),
        },
        "innovation_points": [paper.get("core_claim", ""), *paper.get("relevance_reasons", [])],
        "inspirations": paper.get("transferable_points", []),
        "preparation_steps": steps,
        "method_blocks": [
            {"page": block["page"], "text": block["text"], "bbox": block["bbox"]}
            for block in method_blocks
        ],
        "figures": figures,
        "original_pdf": f"papers/{paper['id']}/original.pdf",
        "reader_markdown": str((detail_root / "paper.md").relative_to(ROOT)).replace("\\", "/"),
        "source_map": str((detail_root / "source_map.json").relative_to(ROOT)).replace("\\", "/"),
        "notes": [
            "方法步骤和图注来自 PDF 文本层与页码锚点。",
            "中文逐段翻译和复杂分图语义仍需智能体精读复核。",
            "裁图标为 approximate 时，应在人工精读阶段调整边界。",
        ],
    }
    apply_curation(detail, detail_root)
    if detail.get("curation_status", "").startswith("agent_reviewed"):
        paper["summary_zh"] = detail["abstract"]["zh"]
        paper["verification_status"] = "fulltext_agent_curated"
        paper["risks"] = [
            risk
            for risk in paper.get("risks", [])
            if not str(risk).startswith("当前为题录/摘要级初筛")
        ]
        paper["risks"].append("全文与页码锚点已核对；复杂分图语义和裁图边界仍应在引用前复核。")
    if detail.get("curation_status", "").startswith("agent_reviewed") and int(
        paper.get("relevance_score") or 0
    ) >= 60:
        paper["decision_hint"] = "read"
    write_json(detail_root / "source_map.json", source_map(blocks, figures, paper, pdf_path))
    (detail_root / "paper.md").write_text(paper_markdown(detail, method_blocks), encoding="utf-8")
    (detail_root / "translation_notes.md").write_text(
        "# Translation and extraction notes\n\n"
        "- 当前为自动结构化草稿。\n"
        "- 原文页码、方法段和图注已保留。\n"
        "- 中文逐段翻译、复杂分图解释和近似裁图需要智能体复核。\n",
        encoding="utf-8",
    )
    write_json(detail_root / "detail.json", detail)
    write_json(WEB / "data" / "paper-details" / f"{paper['id']}.json", detail)
    paper["deep_read_status"] = detail["status"]
    paper["detail_path"] = f"paper.html?id={paper['id']}"
    paper["detail_json"] = f"data/paper-details/{paper['id']}.json"
    document.close()
    return detail


def build_deep_reads(papers: list[dict[str, Any]], day_dir: Path) -> list[dict[str, Any]]:
    details = []
    for paper in papers:
        try:
            detail = build_one(paper, day_dir)
            if detail:
                details.append(detail)
        except Exception as error:  # noqa: BLE001 - one malformed PDF must not stop the daily report
            paper["deep_read_status"] = f"draft_error_{type(error).__name__}"
            paper.setdefault("risks", []).append(f"全文解析失败：{type(error).__name__}。")
    return details


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", default="", help="Literature date in YYYY-MM-DD format")
    args = parser.parse_args()
    selected = args.date
    if not selected:
        days = sorted(path for path in (MEMORY / "literature").glob("*/*") if path.is_dir())
        if not days:
            print("No literature day found.")
            return 0
        selected = days[-1].name
    day_dir = MEMORY / "literature" / selected[:4] / selected
    papers_path = day_dir / "summaries" / "papers.json"
    payload = read_json(papers_path, {"papers": []})
    details = build_deep_reads(payload.get("papers", []), day_dir)
    write_json(papers_path, payload)
    print(f"Built {len(details)} paper detail bundles for {selected}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

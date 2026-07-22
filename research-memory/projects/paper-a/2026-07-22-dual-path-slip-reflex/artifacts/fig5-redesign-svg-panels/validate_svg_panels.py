"""Structural and scientific-boundary validation for the standalone SVG set."""

from __future__ import annotations

import re
from pathlib import Path
from xml.etree import ElementTree as ET


ROOT = Path(__file__).resolve().parent
SVG_DIR = ROOT / "svg"
EXPECTED = {
    "fig5a_lossy_pre_adc_task_vectors.svg": (54, 44),
    "fig5b_continuous_vector_calibration.svg": (117, 44),
    "fig5c_comparator_event_generation.svg": (57, 76),
    "fig5d_hierarchical_hardware_events.svg": (54, 76),
    "fig5e_frozen_threshold_event_timing.svg": (56, 36),
    "fig5f_independent_event_validation.svg": (56, 36),
}


def all_text(root: ET.Element) -> str:
    return " ".join("".join(node.itertext()) for node in root.iter() if node.tag.endswith("text"))


def main() -> None:
    failures: list[str] = []
    for filename, (width_mm, height_mm) in EXPECTED.items():
        path = SVG_DIR / filename
        if not path.exists():
            failures.append(f"{filename}: missing")
            continue

        raw = path.read_text(encoding="utf-8")
        root = ET.fromstring(raw)
        text = all_text(root)
        tags = [node.tag.rsplit("}", 1)[-1] for node in root.iter()]
        width = root.attrib.get("width")
        height = root.attrib.get("height")
        view_box = root.attrib.get("viewBox")
        expected_view = f"0 0 {width_mm * 10} {height_mm * 10}"

        checks = {
            "width": width == f"{width_mm}mm",
            "height": height == f"{height_mm}mm",
            "viewBox": view_box == expected_view,
            "pure-vector": "image" not in tags and "foreignObject" not in tags,
            "no-gradient-filter": not any(tag in tags for tag in ("linearGradient", "radialGradient", "filter")),
            "Arial": "font-family: Arial" in raw,
            "letter-spacing-zero": "letter-spacing: 0" in raw and not re.search(r"letter-spacing\s*:\s*-", raw),
            "no-rounded-containers": " rx=" not in raw and " ry=" not in raw,
            "no-energy-scope": not re.search(r"\b(power|energy|grasp|slip|boost|reflex)\b", text, re.I),
            "no-fake-sample-size": not re.search(r"\bn\s*=\s*\d", text, re.I),
        }

        if filename.startswith("fig5a"):
            checks.update(
                {
                    "equations": all(s in text for s in ("Vz = V1 + V2 +", "V3 + V4", "Vx = V1 - V3", "Vy = V2 - V4")),
                    "degeneracy": all(s in text for s in ("0101", "1010", "[2, 0, 0]")),
                    "lossy-boundary": "Irreversibility boundary" in text,
                }
            )
        if filename.startswith(("fig5b", "fig5c", "fig5e", "fig5f")):
            checks["measurement-placeholder"] = "[TO BE MEASURED]" in text
        if filename.startswith("fig5b"):
            checks["raw-threshold-boundary"] = "offline analysis only" in text
        if filename.startswith("fig5d"):
            checks.update(
                {
                    "event-hierarchy": all(s in text for s in ("CONTACT gate", "OVERLOAD priority", "Direction events")),
                    "firmware-is-planned": all(s in text for s in ("planned", "firmware", "phase", "gate")),
                    "event-not-action": "STOP" not in text and "OVERLOAD_N asserted" in text,
                }
            )
        if filename.startswith("fig5e"):
            checks["common-clock"] = "common clock" in text.lower() and "Force ref." in text
        if filename.startswith("fig5f"):
            checks["event-only-metrics"] = all(s in text for s in ("FP", "FN", "delay", "jitter", "Per-pin"))
            checks["signed-pin-axis"] = "signed event pin" in text
            checks["illegal-concurrent-audit"] = all(s in text for s in ("X+ & X-", "Y+ & Y-", "X± + Y±"))

        bad = [name for name, ok in checks.items() if not ok]
        if bad:
            failures.append(f"{filename}: {', '.join(bad)}")
        print(f"{filename}: {'PASS' if not bad else 'FAIL'}; checks={len(checks)}; bytes={path.stat().st_size}")

    if failures:
        raise SystemExit("\n".join(failures))
    print("All standalone SVG panels pass structural and scientific-boundary checks.")


if __name__ == "__main__":
    main()

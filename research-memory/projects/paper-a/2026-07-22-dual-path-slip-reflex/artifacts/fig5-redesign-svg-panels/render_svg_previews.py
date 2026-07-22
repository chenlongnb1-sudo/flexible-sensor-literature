"""Render the standalone SVGs with the system browser and build a QA contact sheet."""

from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parent
SVG_DIR = ROOT / "svg"
PREVIEW_DIR = ROOT / "preview"
PIXELS_PER_MM = 24
EDGE_CANDIDATES = (
    Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
    Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
    Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
)


def browser_path() -> Path:
    for candidate in EDGE_CANDIDATES:
        if candidate.exists():
            return candidate
    raise FileNotFoundError("No supported Chromium browser was found")


def dimensions_mm(svg_text: str) -> tuple[int, int]:
    import re

    width = re.search(r'<svg[^>]+width="(\d+)mm"', svg_text)
    height = re.search(r'<svg[^>]+height="(\d+)mm"', svg_text)
    if not width or not height:
        raise ValueError("SVG is missing integer millimetre width/height")
    return int(width.group(1)), int(height.group(1))


def render_svg(browser: Path, svg_path: Path, png_path: Path) -> None:
    svg = svg_path.read_text(encoding="utf-8")
    width_mm, height_mm = dimensions_mm(svg)
    width_px = width_mm * PIXELS_PER_MM
    height_px = height_mm * PIXELS_PER_MM

    # The SVG is embedded inline so Chromium does not need cross-file permissions.
    html = f"""<!doctype html><html><head><meta charset=\"utf-8\">
<style>html,body{{margin:0;width:100%;height:100%;overflow:hidden;background:#fff}}
svg{{display:block;width:100vw!important;height:100vh!important}}</style></head>
<body>{svg}</body></html>"""

    with tempfile.TemporaryDirectory(prefix="fig5_svg_render_") as temp_dir:
        temp = Path(temp_dir)
        html_path = temp / "panel.html"
        profile = temp / "edge-profile"
        html_path.write_text(html, encoding="utf-8")
        command = [
            str(browser),
            "--headless=new",
            "--disable-gpu",
            "--hide-scrollbars",
            "--no-first-run",
            "--no-default-browser-check",
            f"--user-data-dir={profile}",
            f"--screenshot={png_path}",
            f"--window-size={width_px},{height_px}",
            html_path.as_uri(),
        ]
        result = subprocess.run(command, capture_output=True, text=True, timeout=60)
        if result.returncode != 0 or not png_path.exists():
            raise RuntimeError(
                f"Browser rendering failed for {svg_path.name}:\n{result.stdout}\n{result.stderr}"
            )

    with Image.open(png_path) as image:
        if image.size != (width_px, height_px):
            raise RuntimeError(
                f"Unexpected render size for {svg_path.name}: {image.size} != {(width_px, height_px)}"
            )
        print(f"{png_path.name}: {image.width}x{image.height}")


def contact_sheet(png_paths: list[Path], output: Path) -> None:
    # Exact existing assembly slots on the 183 x 132 mm canvas.
    slots_mm = {
        "fig5a": (4, 4, 54, 44),
        "fig5b": (62, 4, 117, 44),
        "fig5c": (4, 52, 57, 76),
        "fig5d": (65, 52, 54, 76),
        "fig5e": (123, 52, 56, 36),
        "fig5f": (123, 92, 56, 36),
    }
    scale = 20
    sheet = Image.new("RGB", (183 * scale, 132 * scale), "#F1F3F4")
    for path in png_paths:
        prefix = path.stem[:5]
        x_mm, y_mm, w_mm, h_mm = slots_mm[prefix]
        with Image.open(path).convert("RGB") as image:
            expected = (w_mm * scale, h_mm * scale)
            image = image.resize(expected, Image.Resampling.LANCZOS)
            sheet.paste(image, (x_mm * scale, y_mm * scale))
    sheet.save(output, format="PNG", optimize=True)
    print(f"{output.name}: {sheet.width}x{sheet.height}")


def main() -> None:
    PREVIEW_DIR.mkdir(parents=True, exist_ok=True)
    browser = browser_path()
    png_paths: list[Path] = []
    for svg_path in sorted(SVG_DIR.glob("*.svg")):
        png_path = PREVIEW_DIR / f"{svg_path.stem}.png"
        render_svg(browser, svg_path, png_path)
        png_paths.append(png_path)
    contact_sheet(png_paths, PREVIEW_DIR / "fig5_svg_contact_sheet.png")


if __name__ == "__main__":
    main()

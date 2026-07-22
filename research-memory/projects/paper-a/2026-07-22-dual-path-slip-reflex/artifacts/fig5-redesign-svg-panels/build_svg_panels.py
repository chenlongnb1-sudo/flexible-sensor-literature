"""Build six standalone, editable SVG panels for the redesigned Figure 5.

The generated panels contain only confirmed equations, analytic schematics, empty
measurement templates, and explicit [TO BE MEASURED] labels. No experimental data,
curves, values, or sample sizes are synthesized.
"""

from __future__ import annotations

from html import escape
from pathlib import Path


OUT = Path(__file__).resolve().parent / "svg"

BLACK = "#222222"
BLUE = "#0072B2"
GREEN = "#009E73"
VERMILION = "#D55E00"
ORANGE = "#E69F00"
GRAY = "#7A7A7A"
LIGHT = "#F5F5F5"
GRID = "#D7DCE2"
PALE_BLUE = "#EAF3F8"
PALE_GREEN = "#E8F4EF"
PALE_ORANGE = "#FCF0E8"
WHITE = "#FFFFFF"


class Panel:
    def __init__(
        self,
        letter: str,
        title: str,
        description: str,
        width_mm: int,
        height_mm: int,
        compact_title: bool = False,
    ):
        self.letter = letter
        self.title = title
        self.description = description
        self.width_mm = width_mm
        self.height_mm = height_mm
        self.w = width_mm * 10
        self.h = height_mm * 10
        self.parts: list[str] = []
        self.parts.append(
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{width_mm}mm" height="{height_mm}mm" '
            f'viewBox="0 0 {self.w} {self.h}" role="img" aria-labelledby="title desc">'
        )
        self.parts.append(f"<title id=\"title\">Fig. 5{letter}: {escape(title)}</title>")
        self.parts.append(f"<desc id=\"desc\">{escape(description)}</desc>")
        self.parts.append(
            """<defs>
<style>
text { font-family: Arial, Helvetica, sans-serif; letter-spacing: 0; }
.panel-letter { font-size: 35.3px; font-weight: 700; fill: #222222; }
.panel-title { font-size: 30px; font-weight: 700; fill: #222222; }
.panel-title-compact { font-size: 27px; font-weight: 700; fill: #222222; }
.label { font-size: 28px; fill: #222222; }
.small { font-size: 27px; fill: #222222; }
.tiny { font-size: 26.5px; fill: #7A7A7A; }
.micro { font-size: 22px; fill: #7A7A7A; }
.micro-placeholder { font-size: 19px; fill: #7A7A7A; }
.clock-label { font-size: 20px; fill: #7A7A7A; }
.formula { font-size: 29px; font-weight: 700; }
.placeholder-tag { font-size: 27px; font-weight: 700; fill: #7A7A7A; }
.placeholder-name { font-size: 28px; font-weight: 700; fill: #222222; }
.placeholder-output { font-size: 26.5px; fill: #7A7A7A; }
</style>
<marker id="arrow-black" markerWidth="10" markerHeight="10" refX="8.5" refY="3.5" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L9,3.5 L0,7 Z" fill="#222222"/></marker>
<marker id="arrow-blue" markerWidth="10" markerHeight="10" refX="8.5" refY="3.5" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L9,3.5 L0,7 Z" fill="#0072B2"/></marker>
<marker id="arrow-green" markerWidth="10" markerHeight="10" refX="8.5" refY="3.5" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L9,3.5 L0,7 Z" fill="#009E73"/></marker>
<marker id="arrow-orange" markerWidth="10" markerHeight="10" refX="8.5" refY="3.5" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L9,3.5 L0,7 Z" fill="#D55E00"/></marker>
<marker id="arrow-warning" markerWidth="10" markerHeight="10" refX="8.5" refY="3.5" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L9,3.5 L0,7 Z" fill="#E69F00"/></marker>
</defs>"""
        )
        self.rect(0, 0, self.w, self.h, fill=WHITE, stroke="none", sw=0)
        self.text(12, 38, letter, cls="panel-letter")
        self.text(56, 36, title, cls="panel-title-compact" if compact_title else "panel-title")

    def add(self, item: str) -> None:
        self.parts.append(item)

    def rect(
        self,
        x: float,
        y: float,
        w: float,
        h: float,
        *,
        fill: str = "none",
        stroke: str = BLACK,
        sw: float = 3,
        dash: str | None = None,
    ) -> None:
        dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{sw}"{dash_attr}/>'
        )

    def line(
        self,
        x1: float,
        y1: float,
        x2: float,
        y2: float,
        *,
        stroke: str = BLACK,
        sw: float = 3,
        dash: str | None = None,
        arrow: str | None = None,
    ) -> None:
        dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
        marker = f' marker-end="url(#{arrow})"' if arrow else ""
        self.add(
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
            f'stroke="{stroke}" stroke-width="{sw}"{dash_attr}{marker}/>'
        )

    def path(
        self,
        d: str,
        *,
        fill: str = "none",
        stroke: str = BLACK,
        sw: float = 3,
        dash: str | None = None,
        arrow: str | None = None,
    ) -> None:
        dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
        marker = f' marker-end="url(#{arrow})"' if arrow else ""
        self.add(
            f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" '
            f'stroke-linejoin="miter" stroke-linecap="butt"{dash_attr}{marker}/>'
        )

    def circle(
        self,
        cx: float,
        cy: float,
        r: float,
        *,
        fill: str = WHITE,
        stroke: str = BLACK,
        sw: float = 3,
    ) -> None:
        self.add(
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{sw}"/>'
        )

    def polygon(
        self,
        points: list[tuple[float, float]],
        *,
        fill: str = WHITE,
        stroke: str = BLACK,
        sw: float = 3,
    ) -> None:
        p = " ".join(f"{x},{y}" for x, y in points)
        self.add(
            f'<polygon points="{p}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
        )

    def text(
        self,
        x: float,
        y: float,
        content: str | list[str],
        *,
        cls: str = "label",
        fill: str | None = None,
        weight: int | None = None,
        anchor: str = "start",
        italic: bool = False,
        line_height: float = 1.18,
        rotate: float | None = None,
    ) -> None:
        style = []
        if fill:
            style.append(f"fill:{fill}")
        if weight:
            style.append(f"font-weight:{weight}")
        if italic:
            style.append("font-style:italic")
        style_attr = f' style="{";".join(style)}"' if style else ""
        rotate_attr = f' transform="rotate({rotate} {x} {y})"' if rotate is not None else ""
        lines = [content] if isinstance(content, str) else content
        self.add(
            f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}"{style_attr}{rotate_attr}>'
        )
        for i, line in enumerate(lines):
            dy = "0" if i == 0 else f"{line_height}em"
            self.add(f'<tspan x="{x}" dy="{dy}">{escape(line)}</tspan>')
        self.add("</text>")

    def save(self, path: Path) -> None:
        self.parts.append("</svg>")
        path.write_text("\n".join(self.parts), encoding="utf-8")


def diamond(panel: Panel, cx: float, cy: float, size: float, fill: str, stroke: str = BLACK) -> None:
    half = size / 2.0
    panel.polygon(
        [(cx, cy - half), (cx + half, cy), (cx, cy + half), (cx - half, cy)],
        fill=fill,
        stroke=stroke,
        sw=3,
    )


def sensor_topology(
    panel: Panel,
    cx: float,
    cy: float,
    radius: float,
    *,
    active_bits: str | None = None,
    labels: bool = True,
    scale: float = 1.0,
) -> None:
    positions = {
        "V1": (cx + radius, cy, BLUE, "R4"),
        "V2": (cx, cy - radius, GREEN, "R1"),
        "V3": (cx - radius, cy, BLUE, "R2"),
        "V4": (cx, cy + radius, GREEN, "R3"),
    }
    panel.line(cx - radius, cy, cx + radius, cy, stroke=GRID, sw=3)
    panel.line(cx, cy - radius, cx, cy + radius, stroke=GRID, sw=3)
    bit_map = dict(zip(("V1", "V2", "V3", "V4"), active_bits or "1111"))
    for logical, (x, y, colour, physical) in positions.items():
        active = bit_map[logical] == "1"
        diamond(panel, x, y, 33 * scale, colour if active else WHITE, colour)
        if labels:
            panel.text(
                x,
                y + 6,
                f"{physical}/{logical}",
                cls="tiny",
                fill=BLACK,
                weight=700,
                anchor="middle",
            )


def placeholder_box(
    panel: Panel,
    x: float,
    y: float,
    w: float,
    h: float,
    name: list[str],
    output: list[str],
) -> None:
    panel.rect(x, y, w, h, fill=LIGHT, stroke=GRAY, sw=3.5, dash="12 9")
    panel.text(x + 16, y + 32, "[TO BE MEASURED]", cls="placeholder-tag")
    panel.text(x + 16, y + 72, name, cls="placeholder-name", line_height=1.12)
    output_y = y + h - 62 - (len(output) - 1) * 26
    panel.text(x + 16, output_y, output, cls="placeholder-output", line_height=1.12)


def blank_axes(
    panel: Panel,
    x: float,
    y: float,
    w: float,
    h: float,
    xlabel: str,
    ylabel: str,
    *,
    colour: str,
    placeholder_cls: str = "tiny",
    placeholder_x_offset: float = 0,
) -> None:
    panel.line(x, y + h, x + w, y + h, stroke=BLACK, sw=3)
    panel.line(x, y + h, x, y, stroke=BLACK, sw=3)
    panel.text(x + w / 2, y + h + 28, xlabel, cls="small", anchor="middle")
    panel.text(x - 23, y + h / 2, ylabel, cls="small", fill=colour, weight=700, anchor="middle", rotate=-90)
    panel.text(
        x + w / 2 + placeholder_x_offset,
        y + h / 2,
        "[TO BE MEASURED]",
        cls=placeholder_cls,
        fill=GRAY,
        weight=700,
        anchor="middle",
    )


def make_panel_a() -> Panel:
    p = Panel(
        "a",
        "Lossy pre-ADC task vectors",
        "Four diamond-arranged sensing units map to Vz, Vx, and Vy; the compact inset shows an irreversible degeneracy.",
        54,
        44,
    )
    sensor_topology(p, 92, 158, 48, labels=True, scale=0.78)
    p.line(154, 158, 182, 158, stroke=VERMILION, sw=4, arrow="arrow-orange")
    p.rect(190, 72, 320, 195, fill=WHITE, stroke=VERMILION, sw=4)
    p.text(205, 101, "Pre-ADC projection", cls="small", fill=VERMILION, weight=700)
    p.text(213, 137, ["Vz = V1 + V2 +", "V3 + V4"], cls="formula", fill=BLACK, line_height=1.0)
    p.text(213, 213, "Vx = V1 - V3", cls="formula", fill=BLUE)
    p.text(213, 251, "Vy = V2 - V4", cls="formula", fill=GREEN)

    p.rect(24, 282, 496, 140, fill="#FAFAFA", stroke=GRID, sw=3)
    p.text(38, 311, "Irreversibility boundary", cls="small", weight=700)
    sensor_topology(p, 88, 344, 27, active_bits="0101", labels=False, scale=0.60)
    sensor_topology(p, 220, 344, 27, active_bits="1010", labels=False, scale=0.60)
    p.text(88, 392, "0101", cls="small", weight=700, anchor="middle")
    p.text(220, 392, "1010", cls="small", weight=700, anchor="middle")
    p.line(263, 344, 326, 344, stroke=VERMILION, sw=4, arrow="arrow-orange")
    p.rect(340, 311, 158, 70, fill=PALE_ORANGE, stroke=VERMILION, sw=3)
    p.text(419, 338, "same vector", cls="tiny", fill=VERMILION, weight=700, anchor="middle")
    p.text(419, 368, "[2, 0, 0]", cls="formula", fill=BLACK, anchor="middle")
    return p


def mini_force_pair(panel: Panel, cx: float, cy: float, axis: str) -> None:
    sensor_topology(panel, cx, cy, 38, labels=False, scale=0.72)
    if axis == "x":
        panel.line(cx - 92, cy, cx - 54, cy, stroke=BLUE, sw=4, arrow="arrow-blue")
        panel.line(cx + 92, cy, cx + 54, cy, stroke=BLUE, sw=4, arrow="arrow-blue")
        panel.text(cx - 94, cy - 15, "F3", cls="small", fill=BLUE, weight=700, anchor="middle")
        panel.text(cx + 94, cy - 15, "F1", cls="small", fill=BLUE, weight=700, anchor="middle")
    else:
        panel.line(cx, cy - 90, cx, cy - 54, stroke=GREEN, sw=4, arrow="arrow-green")
        panel.line(cx, cy + 90, cx, cy + 54, stroke=GREEN, sw=4, arrow="arrow-green")
        panel.text(cx + 30, cy - 63, "F2", cls="small", fill=GREEN, weight=700)
        panel.text(cx + 30, cy + 68, "F4", cls="small", fill=GREEN, weight=700)


def make_panel_b() -> Panel:
    p = Panel(
        "b",
        "Continuous vector calibration",
        "Constant-total-load sweeps test whether raw Vx and Vy track signed pair imbalance; normalized eta variables remain offline analysis only.",
        117,
        44,
    )
    mini_force_pair(p, 132, 150, "x")
    mini_force_pair(p, 354, 150, "y")
    p.text(132, 250, "F1 + F3 constant", cls="tiny", anchor="middle")
    p.text(354, 250, "F2 + F4 constant", cls="tiny", anchor="middle")
    p.text(34, 291, "ρx = (F1 - F3)/(F1 + F3)", cls="tiny", fill=BLUE, weight=700)
    p.text(34, 325, "ρy = (F2 - F4)/(F2 + F4)", cls="tiny", fill=GREEN, weight=700)

    blank_axes(p, 510, 72, 270, 210, "ρx", "raw Vx", colour=BLUE)
    blank_axes(p, 855, 72, 270, 210, "ρy", "raw Vy", colour=GREEN)
    p.rect(492, 338, 653, 90, fill=LIGHT, stroke=GRAY, sw=3.5, dash="12 9")
    p.text(508, 372, "[TO BE MEASURED]", cls="placeholder-tag")
    p.text(800, 357, ["Constant-total-load", "force-ratio scan"], cls="small", weight=700, line_height=1.0)
    p.text(1125, 419, "Vz constancy • orthogonal leakage • sweep direction", cls="tiny", fill=GRAY, anchor="end")
    p.text(238, 381, ["ηx = Vx/Vz and ηy = Vy/Vz", "offline analysis only"], cls="tiny", fill=GRAY, anchor="middle", italic=True, line_height=1.0)
    return p


def make_panel_c() -> Panel:
    p = Panel(
        "c",
        "Comparator event generation",
        "Calibrated raw Vz, Vx, and Vy feed hysteretic comparators that expose contact, overload, and signed direction event pins.",
        57,
        76,
    )
    rows = [
        ("Vz", BLACK, "Vz > θc", "CONTACT"),
        ("Vz", BLACK, "Vz > θo", "OVERLOAD"),
        ("Vx", BLUE, "Vx > +θx / < -θx", "X+ / X-"),
        ("Vy", GREEN, "Vy > +θy / < -θy", "Y+ / Y-"),
    ]
    for i, (signal, colour, rule, output) in enumerate(rows):
        y = 100 + i * 91
        p.text(48, y + 35, signal, cls="formula", fill=colour, anchor="middle")
        p.line(72, y + 27, 103, y + 27, stroke=colour, sw=4, arrow={BLACK:"arrow-black", BLUE:"arrow-blue", GREEN:"arrow-green"}[colour])
        p.rect(112, y, 270, 62, fill=WHITE, stroke=colour, sw=3)
        p.text(247, y + 40, rule, cls="small", fill=colour, weight=700, anchor="middle")
        p.line(382, y + 31, 390, y + 31, stroke=colour, sw=4, arrow={BLACK:"arrow-black", BLUE:"arrow-blue", GREEN:"arrow-green"}[colour])
        p.text(558, y + 40, output, cls="tiny", fill=colour, weight=700, anchor="end")

    blank_axes(p, 90, 480, 390, 130, "input voltage (up / down)", "event state", colour=VERMILION)
    p.rect(55, 662, 470, 76, fill=LIGHT, stroke=GRAY, sw=3.5, dash="12 9")
    p.text(70, 694, "[TO BE MEASURED]", cls="placeholder-tag")
    p.text(70, 727, "trip/release • hysteresis • jitter • polarity", cls="micro", fill=GRAY, weight=700)
    p.text(520, 84, "event pins", cls="tiny", anchor="end")
    return p


def make_panel_d() -> Panel:
    p = Panel(
        "d",
        "Hierarchical hardware events",
        "Frozen thresholds first gate contact, then prioritize overload, then expose signed x and y direction events; task-phase interpretation remains planned firmware.",
        54,
        76,
    )
    p.rect(35, 90, 338, 88, fill=WHITE, stroke=BLACK, sw=4)
    p.text(58, 118, "1  CONTACT gate", cls="small", weight=700)
    p.text(58, 150, "Vz > θc", cls="formula", fill=BLACK)
    p.line(204, 178, 204, 220, stroke=BLACK, sw=4, arrow="arrow-black")

    p.rect(35, 225, 338, 96, fill="#FFF8E8", stroke=ORANGE, sw=4)
    p.text(53, 260, "2  OVERLOAD priority", cls="small", fill=ORANGE, weight=700)
    p.text(53, 292, "Vz > θo", cls="formula", fill=BLACK)
    p.text(53, 316, "OVERLOAD_N asserted", cls="tiny", fill=ORANGE, weight=700)
    p.line(204, 321, 204, 363, stroke=BLACK, sw=4, arrow="arrow-black")

    p.rect(35, 368, 338, 151, fill=WHITE, stroke=BLUE, sw=4)
    p.text(53, 405, "3  Direction events", cls="small", fill=BLUE, weight=700)
    p.text(53, 450, "Vx → X+ / X-", cls="formula", fill=BLUE)
    p.text(53, 495, "Vy → Y+ / Y-", cls="formula", fill=GREEN)

    p.rect(397, 106, 126, 310, fill="#FAFAFA", stroke=GRAY, sw=3, dash="10 8")
    p.text(460, 140, "planned", cls="tiny", fill=GRAY, weight=700, anchor="middle")
    p.text(460, 174, ["firmware", "phase", "gate"], cls="tiny", weight=700, anchor="middle", line_height=0.92)
    p.line(460, 205, 460, 248, stroke=GRAY, sw=3, dash="8 7", arrow="arrow-black")
    p.text(460, 280, ["phase", "+ history"], cls="tiny", anchor="middle", line_height=1.0)
    p.line(460, 340, 460, 374, stroke=GRAY, sw=3, dash="8 7", arrow="arrow-black")
    p.text(460, 401, "Fig. 6", cls="small", fill=GRAY, weight=700, anchor="middle")

    event_boxes = [
        (45, 558, "CONTACT", BLACK),
        (285, 558, "OVERLOAD", ORANGE),
        (45, 625, "X±", BLUE),
        (285, 625, "Y±", GREEN),
    ]
    for x, y, label, colour in event_boxes:
        p.rect(x, y, 210, 52, fill=WHITE, stroke=colour, sw=3)
        p.text(x + 105, y + 35, label, cls="small", fill=colour, weight=700, anchor="middle")
    p.text(270, 714, "Thresholds frozen before test.", cls="tiny", fill=GRAY, anchor="middle", italic=True)
    p.text(270, 746, "Task-phase logic → Fig. 6.", cls="tiny", fill=GRAY, anchor="middle")
    return p


def make_panel_e() -> Panel:
    p = Panel(
        "e",
        "Frozen-threshold event timing",
        "A common clock must align the external force reference, continuous vectors, and all six event pins on independent test sequences.",
        56,
        36,
        True,
    )
    blocks = [
        (20, 58, 140, "Force", "reference", BLACK),
        (210, 58, 140, "Vectors", "Vz / Vx / Vy", VERMILION),
        (400, 58, 140, "Six event", "pins", BLUE),
    ]
    for i, (x, y, w, line1, line2, colour) in enumerate(blocks):
        p.rect(x, y, w, 64, fill=WHITE, stroke=colour, sw=3)
        p.text(x + w / 2, y + 27, line1, cls="tiny", fill=colour, weight=700, anchor="middle")
        p.text(x + w / 2, y + 51, line2, cls="tiny", anchor="middle")
        if i < len(blocks) - 1:
            p.line(x + w, y + 32, blocks[i + 1][0] - 9, y + 32, stroke=GRAY, sw=3, arrow="arrow-black")

    p.line(38, 160, 522, 160, stroke=GRAY, sw=4)
    for cx in (90, 280, 470):
        p.line(cx, 122, cx, 160, stroke=GRAY, sw=3)
    # Keep the shared-bus label fully between the first two vertical taps.
    p.rect(100, 130, 170, 27, fill=WHITE, stroke="none", sw=0)
    p.text(185, 152, "COMMON CLOCK", cls="clock-label", fill=GRAY, weight=700, anchor="middle")

    p.rect(18, 170, 524, 146, fill=LIGHT, stroke=GRAY, sw=3.5, dash="12 9")
    p.line(180, 205, 525, 205, stroke=BLACK, sw=3, arrow="arrow-black")
    p.text(480, 195, "time", cls="micro", anchor="end")
    p.text(365, 228, "[TO BE MEASURED]", cls="micro-placeholder", fill=GRAY, weight=700, anchor="middle")

    timing_rows = [
        ("Force ref.", BLACK, 170),
        ("Vz / Vx / Vy", BLACK, 170),
        ("CONTACT / OVERLOAD", BLUE, 300),
        ("X± / Y±", BLUE, 170),
    ]
    for i, (label, colour, trace_x) in enumerate(timing_rows):
        y = 235 + i * 24
        p.text(30, y + 5, label, cls="micro", fill=colour)
        p.line(trace_x, y, 525, y, stroke=GRID, sw=3)
    p.text(280, 345, "Thresholds frozen before independent test.", cls="micro", fill=GRAY, anchor="middle")
    return p


def make_panel_f() -> Panel:
    p = Panel(
        "f",
        "Independent event validation",
        "The final evidence reports per-pin event errors and timing, plus illegal same-axis combinations and valid concurrent signed-direction patterns.",
        56,
        36,
        True,
    )
    p.text(160, 79, "Per-pin metrics", cls="tiny", weight=700, anchor="middle")
    blank_axes(
        p,
        60,
        90,
        200,
        135,
        "signed event pin",
        "event metric",
        colour=BLUE,
        placeholder_cls="micro-placeholder",
        placeholder_x_offset=8,
    )

    p.text(430, 79, "Illegal / concurrent", cls="tiny", weight=700, anchor="middle")
    p.rect(310, 90, 230, 135, fill=WHITE, stroke=GRID, sw=3)
    p.line(310, 135, 540, 135, stroke=GRID, sw=2.5)
    p.line(310, 180, 540, 180, stroke=GRID, sw=2.5)
    p.line(455, 90, 455, 225, stroke=GRID, sw=2.5)
    audit_rows = ["X+ & X-", "Y+ & Y-", "X± + Y±"]
    for i, label in enumerate(audit_rows):
        p.text(326, 120 + i * 45, label, cls="tiny", weight=700)

    p.text(280, 292, "Per-pin: FP/FN • delay • jitter", cls="tiny", fill=GRAY, anchor="middle")
    p.text(280, 329, "Co-occurrence audit • frozen test set", cls="tiny", fill=GRAY, anchor="middle")
    return p


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    panels = {
        "fig5a_lossy_pre_adc_task_vectors.svg": make_panel_a(),
        "fig5b_continuous_vector_calibration.svg": make_panel_b(),
        "fig5c_comparator_event_generation.svg": make_panel_c(),
        "fig5d_hierarchical_hardware_events.svg": make_panel_d(),
        "fig5e_frozen_threshold_event_timing.svg": make_panel_e(),
        "fig5f_independent_event_validation.svg": make_panel_f(),
    }
    for filename, panel in panels.items():
        panel.save(OUT / filename)
        print(OUT / filename)


if __name__ == "__main__":
    main()

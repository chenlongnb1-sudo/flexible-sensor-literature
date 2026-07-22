# Fig. 5 standalone SVG panels

This directory contains a redesign that follows the current paper narrative. It does
not overwrite the existing `fig5_editable.pptx` or the older `BRIEF.txt`.

Run:

```powershell
python build_svg_panels.py
python validate_svg_panels.py
python render_svg_previews.py
```

The editable vectors are in `svg/`; rendered QA previews are in `preview/`.

Data-bearing panels deliberately contain empty axes or empty matrices. Replace only
the `[TO BE MEASURED]` region with plots generated from the qualifying experiment.
Do not convert the conceptual paths in panels c-d into claimed measured performance.

See `panel-map.md` for panel roles and missing measurements, and `qa.md` for the
final structural, scientific-boundary, and physical-slot visual audit.

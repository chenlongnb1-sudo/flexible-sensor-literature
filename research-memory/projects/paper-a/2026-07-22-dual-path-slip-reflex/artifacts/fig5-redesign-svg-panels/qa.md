# Fig. 5 standalone SVG QA

QA date: 2026-07-22

## Automated validation

- `python -X utf8 validate_svg_panels.py`: PASS for all six panels.
- Total checks: 75 across dimensions, viewBox, vector purity, typography,
  scientific scope, required placeholders, lossy-boundary example, event
  hierarchy, shared-clock semantics, and signed-pin validation.
- All outputs are pure SVG: no `<image>`, `foreignObject`, gradients, filters,
  rounded containers, fabricated sample sizes, or Fig. 6 power/control claims.
- `python -X utf8 render_svg_previews.py`: PASS; all six PNG previews and the
  3660 x 2640 physical-slot contact sheet were regenerated from the final script.
- Raster boundary check: PASS; every standalone PNG retains an all-white 8 px
  safety border, so no rendered content touches or crosses a canvas edge.

## Visual validation

- a: PASS. Equations retain a safe right margin; 0101/1010 degeneracy remains
  readable at the 54 x 44 mm slot.
- b: PASS. Force schematics, two empty plots, offline eta note, and measurement
  contract occupy separate regions without collision.
- c: PASS. Output arrowheads do not touch CONTACT/OVERLOAD labels; the axis title
  and comparator measurement contract remain inside the panel.
- d: PASS. Hardware-event hierarchy, planned firmware inset, event labels, and
  Fig. 6 boundary are legible without clipping.
- e: PASS. COMMON CLOCK is a shared bus rather than a causal output; its label is
  isolated from all taps, `time` is inside the timing frame and clear of the
  arrowhead, trace labels do not intersect guide lines, and the footer is visible.
- f: PASS. The small measurement tag stays inside the left axes; the right table
  contains only three illegal/concurrent audits; both metric-definition lines
  remain inside the panel.

## Data integrity

- No experimental curve, waveform, confusion count, performance value, or
  sample size was synthesized.
- Data-bearing regions in b, c, e, and f remain marked `[TO BE MEASURED]`.
- Calibration data and independent-test validation remain explicitly separated.

## Final SVG SHA256

| File | SHA256 |
| --- | --- |
| `fig5a_lossy_pre_adc_task_vectors.svg` | `267C395A57D53D4520C4A3599781F5EB44134E3091B138F9903381A8CD26A212` |
| `fig5b_continuous_vector_calibration.svg` | `E1D58BE6B9B4C51CA0456118A28B588EAC02D8D8E51BE59BA20EABF36A6AEC0C` |
| `fig5c_comparator_event_generation.svg` | `0F78521AD6B35090772259C5C73039674B120020C374D0D15475061ACB6055DC` |
| `fig5d_hierarchical_hardware_events.svg` | `7C8ADA19E3CCDC6F6D3581D7FBE77C1932462C7FF5B2726EED0760B0C8763F07` |
| `fig5e_frozen_threshold_event_timing.svg` | `6BF4BDC7C9A2DA3ACBE79ECA94B215EAB8E80093721A49EC42B7D5F0DCCF7DB3` |
| `fig5f_independent_event_validation.svg` | `4014A5A5C12D533465C54F004EE084F380EC85382913EB294D82EA15980220B0` |

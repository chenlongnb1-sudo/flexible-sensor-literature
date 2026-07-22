# Shared visual specification

- Canvas per panel matches the existing 183 x 132 mm assembly slots:
  - a: 54 x 44 mm
  - b: 117 x 44 mm
  - c: 57 x 76 mm
  - d: 54 x 76 mm
  - e: 56 x 36 mm
  - f: 56 x 36 mm
- Background: white.
- Typeface: Arial with Helvetica/sans-serif fallback; letter spacing 0.
- Panel letters: lowercase a-f, bold, 10 pt equivalent.
- Panel title: bold, approximately 8.8 pt at native size.
- Body labels: approximately 7.9 pt at native size.
- Shapes: square corners only; no cards, gradients, shadows, or decorative frames.
- Signal colors:
  - `Vz` / total contact: `#222222`
  - `Vx` / x direction: `#0072B2`
  - `Vy` / y direction: `#009E73`
  - analog/event emphasis: `#D55E00`
  - overload/warning: `#E69F00`
  - neutral/planned/unverified: `#7A7A7A`
- Solid lines: confirmed analytic signal paths.
- Gray dashed lines: planned firmware or missing evidence.
- Missing measurements: light-gray field, dashed gray border, explicit
  `[TO BE MEASURED]`, empty axes or empty matrix only.

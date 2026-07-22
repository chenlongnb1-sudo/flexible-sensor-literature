# Figure 5 standalone SVG redesign

## Takeaway

Continuous `Vz`, `Vx`, and `Vy` outputs form a lossy task representation that frozen
comparator thresholds convert into contact, signed-direction, and overload hardware
events.

## Scope boundary

- Figure 5 ends at hardware event generation and independent event validation.
- Grasp-phase control, local reflex actuation, object slip, and system/task energy
  belong to Figure 6.
- The full sixteen-anchor catalog is not repeated here. Panel a preserves the required
  `0101` and `1010 -> [2, 0, 0]` degeneracy as the irreversibility boundary.
- `eta_x = Vx/Vz` and `eta_y = Vy/Vz` are offline analysis variables. Hardware events
  use calibrated raw `Vx` and `Vy` thresholds.

## Panel questions

| Panel | Question | Evidence status |
| --- | --- | --- |
| a | What information does the pre-ADC projection retain and discard? | Analytic equations and ideal-anchor boundary |
| b | Do continuous raw vectors follow opposed-pair load imbalance at fixed total load? | To be measured |
| c | How do calibrated comparators expose contact, overload, and signed direction pins? | Analytic interface; thresholds/hysteresis to be measured |
| d | In what priority are the hardware events produced? | Analytic hierarchy; firmware phase gate is planned only |
| e | Can frozen thresholds produce synchronized events on independent force sequences? | To be measured |
| f | What are the per-pin errors/timing and the illegal or concurrent event patterns? | To be measured |

## Confirmed invariants

- Physical layout: R1 top, R2 left, R3 bottom, R4 right.
- Logical mapping: `V1=R4`, `V2=R1`, `V3=R2`, `V4=R3`.
- `Vx = V1 - V3`, `Vy = V2 - V4`, `Vz = V1 + V2 + V3 + V4`.
- The representation is lossy and does not reconstruct a tactile image or full 3D force.
- Overload requires a calibrated `Vz` threshold; it is not one of the sixteen anchors.

## Generation mode

Deterministic SVG only. No image-generation model, experimental image, synthetic
trace, point, number, sample size, or performance trend is embedded.

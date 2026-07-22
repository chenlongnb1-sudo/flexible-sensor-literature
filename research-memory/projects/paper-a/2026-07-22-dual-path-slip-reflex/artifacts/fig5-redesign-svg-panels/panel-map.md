# Fig. 5 panel map

Central conclusion: continuous Vz/Vx/Vy form a lossy task representation that is
converted by frozen thresholds into contact, overload, and signed-direction
hardware events. Closed-loop grasp control and energy measurements belong to
Fig. 6.

| Panel | Physical slot | Editable SVG | Role | Evidence status |
| --- | --- | --- | --- | --- |
| a | 54 x 44 mm | `fig5a_lossy_pre_adc_task_vectors.svg` | Four 45-degree sensing units map to Vz, Vx, and Vy before ADC; 0101 and 1010 show the irreversible `[2, 0, 0]` degeneracy. | Analytic schematic; no measured curve. |
| b | 117 x 44 mm | `fig5b_continuous_vector_calibration.svg` | Constant-total-load x/y pair sweeps test raw Vx and Vy; normalized eta terms are explicitly offline only. | Data missing; empty axes and measurement contract retained. |
| c | 57 x 76 mm | `fig5c_comparator_event_generation.svg` | Hysteretic comparators expose CONTACT, OVERLOAD, X+/X-, and Y+/Y- pins from calibrated raw voltages. | Circuit/interface schematic plus empty hysteresis template. |
| d | 54 x 76 mm | `fig5d_hierarchical_hardware_events.svg` | CONTACT gates the event hierarchy, OVERLOAD has priority, and signed direction pins remain hardware events. | Analytic event logic; firmware phase gate is marked planned and routed to Fig. 6. |
| e | 56 x 36 mm | `fig5e_frozen_threshold_event_timing.svg` | A shared clock aligns external force reference, continuous vectors, and all six event pins on an independent test sequence. | Data missing; no waveform is invented. |
| f | 56 x 36 mm | `fig5f_independent_event_validation.svg` | Per-pin errors/timing and illegal or concurrent signed-event combinations are audited. | Data missing; no metric values or matrix counts are invented. |

## Required measurements

1. Panel b: constant-total-load x- and y-pair ratio sweeps; report raw Vx/Vy,
   Vz constancy, orthogonal leakage, and sweep direction.
2. Panel c: comparator up/down sweeps for trip and release thresholds,
   hysteresis, jitter, and output polarity.
3. Panel e: common-clock recordings of external force reference, Vz/Vx/Vy,
   and CONTACT, OVERLOAD, X+, X-, Y+, and Y- pins with thresholds frozen
   before the independent test.
4. Panel f: per-pin FP, FN, trigger/release delay, and jitter; audit X+ with X-,
   Y+ with Y-, and valid concurrent signed x/y patterns on the independent set.

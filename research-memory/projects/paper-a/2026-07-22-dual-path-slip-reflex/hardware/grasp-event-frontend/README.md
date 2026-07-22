# ADC-preceding three-vector and event-triggered grasp front end

## Status

This is a parameterized Rev-A design package. It is an implementable circuit
definition and verification plan, but it is **not released for PCB fabrication**
because the sensor, ADC, supply, GPIO, threshold, and motor-driver electrical
limits listed in `PARAMETER_GAPS.md` are not present in the workspace.

No measured voltage, current, threshold, latency, noise, energy, or success-rate
result is claimed in this directory.

## Bounded function

The circuit forms only the following mathematical vectors before digitization:

```text
z = V1 + V2 + V3 + V4
x = V1 - V3
y = V2 - V4
```

On a single supply, the external ADC pins are affine encodings of these vectors:

```text
VZ_ADC = BZ + GZ (z - z0)
VX_ADC = BX + GX (x - x0)
VY_ADC = BY + GY (y - y0)
```

The gains, zero terms, and biases are selected only after the missing electrical
ranges are supplied. This distinction prevents a single-supply level shift from
being misreported as a different physical vector.

## Recommended architecture

- Four protected, filtered sensor inputs with optional unity-gain buffers.
- Matched-ratio difference amplifiers for x and y.
- Equal-resistor average followed by a referenced gain stage for z.
- Three ADC outputs with separate ADC charge-kickback filters.
- Six always-on open-drain event outputs: `CONTACT_N`, `OVERLOAD_N`,
  `X_POS_N`, `X_NEG_N`, `Y_POS_N`, and `Y_NEG_N`.
- In A4, comparator events form before quantization and wake the MCU. The embedded
  ADC/reference is sampled only after an event if bench traces prove that it really
  stopped or entered standby during idle.
- `OVERLOAD_N` is planned to enter an independent motor-enable gate, but this path is
  `[TO BE VALIDATED]`. P13/P14 polarity and safety behavior, power-up/down safe state,
  fault injection, and overload-to-disable latency are still missing; do not claim
  that hardware already stops the actuator first.

The physical event pins are active low to support open-drain level translation
and falling-edge wake-up. The logical event names in firmware are the inverted
forms without the `_N` suffix.

## Core claim boundary

Architecture 2 (three continuous analog vectors plus continuous ADC) is
functionally close to architecture 1 (four continuous ADC channels plus digital
vector calculation). Reducing four continuous conversions to three is not, by
itself, evidence of a large power reduction.

Architecture 3 is the required ADC-first event baseline. Its ADC continuously
converts, or uses the strongest DMA/analog-watchdog/low-power-monitor mode supported
by the selected hardware; the event forms after quantization and the MCU main core
may sleep. Architecture 4 is the proposed pre-ADC event path. Its additional claim
is not "event-driven control" itself, but avoiding idle quantization when the
embedded ADC/reference demonstrably stops or enters standby. A1-vs-A2 isolates
4-to-3 resource changes; A3-vs-A4 isolates post-ADC versus pre-ADC event formation.

A3 and A4 must share the same vector AFE, `VZ_ADC/VX_ADC/VY_ADC` inputs,
ADC/reference, active sampling rate, physical thresholds, burst configuration, and
downstream controller. A3 is never the raw-4 path.

If A4 still samples continuously, describe it only as `hardware-thresholded
event-driven control`. Do not claim `ADC-gated acquisition`, `event-triggered
acquisition`, or reduced ADC conversions. Report the measured event-rate break-even
where frequent events remove any energy advantage.

`ADC_EN/CS/DRDY` alone does not prove internal converter or reference shutdown. P10
must define the standby/power-down state from its datasheet, and separate
ADC/reference rail current must validate it. Until then use `standby to be verified`.

## Files

- `DESIGN_REVIEW.md`: evidence audit, design decisions, and major risks.
- `PARAMETER_GAPS.md`: electrical information required before PCB release.
- `SYSTEM_ARCHITECTURE.md`: block diagrams, baseline comparison, and event map.
- `SCHEMATIC.md`: complete parameterized component-level schematic definition.
- `netlist.csv`: machine-readable reference/pin-role/net connection list.
- `FORMULAS_AND_SELECTION.md`: gain, range, filter, hysteresis, and error formulas.
- `BOM_CANDIDATES.csv`: verified candidate families and conditional alternatives.
- `MCU_INTERFACE_AND_CONTROL.md`: GPIO, wake, priority, and state logic.
- `CALIBRATION_TEST_LAYOUT.md`: calibration, test points, startup, safety, and PCB layout.
- `SIMULATION_PLAN.md`: SPICE/equivalent simulation matrix and release checks.
- `spice/grasp_event_frontend_parametric.cir.in`: parameterized behavioral bench template.
- `POWER_VALIDATION_PROTOCOL.md`: matched four-architecture energy and break-even experiment.
- `SOURCES.md`: local evidence and official component sources.
- `DESIGN_QA.md`: automated/visual QA results and remaining release blockers.
- `validate_package.ps1`: repeatable netlist, token, sign, overload-path, and
  hysteresis-polarity checks.
- `drawings/`: editable SVG and full-size PNG system, baseline, and two-sheet
  schematic review drawings, plus figure brief and provenance.

Run the package QA from this directory with:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\validate_package.ps1
```

## Existing-project audit

The existing `APTE_RevA_Projection_Frontend` is a nine-branch programmable
DAC/TMUX/TIA design. It is not electrically equivalent to this four-voltage,
fixed-vector front end. This package reuses its evidence labels, saturation
budgeting, test-point discipline, separated power measurement, and validation
structure only. It does not reuse its 5 V rail, 1.65 V common mode, DAC codes,
sensor resistance range, or TIA values as facts for the present sensor.

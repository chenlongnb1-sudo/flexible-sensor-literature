# Matched four-architecture power validation

## 1. Claim under test

The test separates two questions. A1-vs-A2 asks what changes when four raw continuous
conversions become three continuous vector conversions. A3-vs-A4 asks whether forming
the event before rather than after quantization avoids idle digitization and reduces
measured electronics energy under a matched grasping task. ADC-first systems can also
implement event-driven control and can let the MCU main core sleep.

## 2. Architectures

| Mode | Analog front end | ADC behavior | MCU behavior |
|---|---|---|---|
| A1 raw-4 continuous | Four matched raw channels | Four conversions per sample continuously | Computes z/x/y and classifies continuously |
| A2 vector-3 continuous | Three-vector circuit | Three conversions per sample continuously | Classifies continuously |
| A3 ADC-first event | Same three-vector circuit as A4; event thresholding after quantization | Continuous conversion, or the strongest supported DMA/analog-watchdog/low-power monitor mode | Main core may sleep; digital-side event wakes processing and communication |
| A4 pre-ADC vector event | Same three-vector circuit plus always-on event comparators | ADC/reference truly stopped or in validated standby during idle; bounded z/x/y burst after GPIO event | Atomically snapshot events, start ADC/reference, wait measured settling, process burst, act/log, return to sleep |

A2, A3, and A4 must use the same vector board and matched analog bandwidth. A1 must
use a gain/bandwidth-matched raw path so the comparison is not confounded by different
sensor loading. The actual ADC/MCU is TBC; A3 must use the strongest low-power digital
event mechanism the selected hardware really supports.

A3 and A4 additionally share the same three `VZ_ADC/VX_ADC/VY_ADC` inputs, the same
ADC/reference, active sampling rate, physical threshold definitions, burst length,
and downstream controller. Their only intended causal difference is whether the
event forms after or before quantization. A3 must not be implemented as raw-4.

## 3. Controlled conditions

- Same sensor specimen, orientation, object, gripper, controller target, initial pose,
  closing speed, ambient conditions, and mechanical task sequence.
- Same ADC resolution, per-channel sampling rate when active, reference, and valid
  sample definition.
- Same MCU, compiler, clock policy while active, motor command policy, and logging.
- Same physical event definitions and frozen thresholds. A3 applies them after
  quantization; A4 applies them before quantization.
- Same task acceptance and failure definitions.
- Randomized/interleaved architecture order to reduce drift and battery/temperature bias.
- Independent trials and device count recorded separately; no `n` assigned in advance here.

## 4. Electrical measurement boundary

Measure synchronized voltage/current for:

1. always-on analog/vector/comparator rail;
2. ADC/reference rail;
3. MCU/digital/communication rail;
4. motor-driver electronics rail;
5. actuator power as a separate non-electronics result.

The continuously recording diagnostic DAQ/scope/logic analyzer stays outside the
deployment-energy boundary. Its continuous acquisition does not imply that the
embedded ADC is continuously converting in A4.

Report board electronics both with and without the motor-driver electronics, but never
mix actuator energy into the claimed tactile readout saving.

## 5. Required metrics

| Metric | Definition |
|---|---|
| Front-end idle/active power | Time-resolved rail power in the declared operating states |
| ADC conversions | Hardware counter or trace-derived accepted conversions per task |
| MCU active duty | Time outside declared sleep state divided by task duration |
| Communication bytes | Payload plus protocol overhead per task |
| Average electronics power | Rail energy divided by task duration |
| Electronics energy per task | Integral of all included electronics rail powers |
| Single-event incremental energy | Integral of `P(t)-P_idle` over a declared event window |
| Event-to-first-valid-vector latency | GPIO edge to first settled z/x/y sample |
| Overload-to-disable latency | Physical threshold crossing to motor disable edge |
| False positive rate | Events asserted without ground-truth condition |
| False negative rate | Ground-truth condition without required event in latency window |
| Task performance | Success, peak force, slip distance, response delay, and retained failures |
| Event-rate break-even | Measured A3/A4 task energy versus event rate or idle duty, including the crossing where A4 no longer saves energy |

## 6. Calculations

```text
E_rail = integral(v_rail(t) * i_rail(t) dt)
E_electronics_task = sum(E_included_rails)
P_average = E_electronics_task / T_task
MCU_active_duty = T_active / T_task
E_event_incremental = integral_window(P(t) - P_idle dt)
```

Report instrument bandwidth, sample rate, shunt value/tolerance, synchronization error,
integration window, rail inclusion, and uncertainty.

## 7. Synchronization

Record on the same time base:

```text
V1-V4 or z/x/y
six event pins
ADC enable/CS and conversion marker
MCU sleep/active marker
motor command and hardware enable
object motion/force ground truth
all measured rail powers
```

## 8. Decision rule

Do not claim that only the proposed system supports event-driven control. A3 is the
required strong digital-event baseline and may already reduce MCU-main duty and
communication.

Do not make a pre-ADC acquisition-gating claim unless A4 reduces measured electronics
energy per task relative to A3 with comparable task performance and declared
uncertainty, and hardware traces prove that the embedded ADC/reference stopped or
entered the declared standby state during idle. If the A4 embedded ADC still converts
continuously, downgrade the claim to `hardware-thresholded event-driven control`; do
not claim `ADC-gated acquisition`, `event-triggered acquisition`, or reduced ADC
conversions.

`ADC_EN`, `CS`, and `DRDY` are external activity evidence; they do not by themselves
prove that the converter core stopped or that the reference powered down. After P10
selection, define standby/power-down from the component datasheet and confirm it with
separate ADC/reference rail current. Until then label the state `standby to be
verified`.

A2-vs-A1 results must be reported separately as vectorization/channel-conversion
resource changes. A4-vs-A3 isolates the location of event formation. Report the
low/medium/high-event-rate break-even boundary rather than hiding workloads where A4
loses its energy advantage.

## 9. Data template

Use `power_measurement_template.csv` for run-level and task-level summaries. Preserve
the raw synchronized waveform files and hashes; the summary CSV is not a replacement.

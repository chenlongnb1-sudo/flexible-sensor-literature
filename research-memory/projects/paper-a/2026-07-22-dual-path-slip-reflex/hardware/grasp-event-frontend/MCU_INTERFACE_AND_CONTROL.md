# MCU, ADC, GPIO, and grasp-control interface

## 1. Physical event interface

| Pin | Electrical form | MCU configuration | Logical meaning when low |
|---|---|---|---|
| `CONTACT_N` | Open drain; external pull-up to `EVENT_VIO` | Falling-edge EXTI/wake | Contact threshold crossed |
| `OVERLOAD_N` | Open drain; external pull-up; hardware safety branch | Highest-priority falling-edge EXTI | Overload threshold crossed |
| `X_POS_N` | Open drain | Falling-edge EXTI/wake | Positive x imbalance |
| `X_NEG_N` | Open drain | Falling-edge EXTI/wake | Negative x imbalance |
| `Y_POS_N` | Open drain | Falling-edge EXTI/wake | Positive y imbalance |
| `Y_NEG_N` | Open drain | Falling-edge EXTI/wake | Negative y imbalance |

Verify GPIO absolute maximum, VIH/VIL, unpowered injection, and wake-capable pins.
External pull-ups are mandatory for deterministic behavior and must be included in
the event latency/static-power budget. Disable internal pulls unless required by the
selected MCU.

## 2. ADC interface

The embedded design may use either:

- an external three-or-more-channel ADC with `CS/SHDN` or a verified low-power mode;
- three channels of the motor-control MCU ADC.

Required signals are `VZ_ADC`, `VX_ADC`, `VY_ADC`, analog reference/ground, and
an optional `ADC_EN` or `ADC_CS_N`. The DABL logger may be used for synchronized
laboratory validation, but its software-reported range is not an embedded-ADC spec.

Before selecting output RC values, obtain the ADC input capacitance, acquisition
time, maximum source impedance, reference settling, and wake time.

## 3. A4 pre-ADC event state machine

```text
RESET:
    force MCU_MOTOR_EN = 0
    confirm AFE_PGOOD and event-pin legal levels
    load/verify threshold configuration if DAC is fitted
    reject theta_o <= theta_c
    clear optional kill latch only under a safe mechanical condition

IDLE:
    embedded ADC/reference in datasheet-defined standby/power-down if verified
    tactile MCU enters wake-capable sleep only if motor-control responsibility permits

ON GPIO EDGE:
    snapshot all six GPIOs atomically
    if OVERLOAD:
        planned hardware-disable path is TO BE VALIDATED
        follow approved bench safety policy
        timestamp event and capture validation evidence
    else if not CONTACT:
        log isolated direction event as noise/fault candidate
        return to IDLE unless persistence policy requests a diagnostic burst
    else if CONTACT edge and no load-direction event:
        issue immediate stop/hold command to motor controller
        optionally start ADC/reference, wait characterized settling, and capture a short burst
        log contact-stop timing; do not put the complete burst before the stop command
    else if X/Y load event:
        apply the one frozen policy selected after pilot work:
            policy A = bounded action first, then ADC/reference wake + burst + log
            policy B = short confirmation burst first, then bounded action + log
        do not switch policy by trial or load condition
    finally when permitted:
        record unified-clock timestamps
        return ADC/reference to standby to be verified
        return tactile MCU to the measured state required by motor-control division
```

In the proposed A4 path, continuous embedded-ADC polling is not used to create
contact, direction, or overload events. This statement does not apply to A3: the
matched ADC-first baseline forms events after quantization using continuous ADC or
the strongest supported DMA/analog-watchdog/low-power-monitor mode.

## 4. Priority and invalid combinations

1. `OVERLOAD` dominates every other state.
2. Direction events are gated by `CONTACT` for normal control, but retained for
   diagnostics because they can reveal drift or wiring faults.
3. `X_POS && X_NEG` or `Y_POS && Y_NEG` is invalid when threshold/hysteresis ranges
   are non-overlapping; enter a safe diagnostic mode.
4. `CONTACT && !X_POS && !X_NEG && !Y_POS && !Y_NEG` is a balanced-contact candidate.
5. One axis event gives signed correction; simultaneous x and y events give mixed
   or oblique correction.

## 5. Sixteen-state boundary

Do not create a sixteen-state lookup that claims invertibility. Ideal `0101` and
`1010` both produce `[2,0,0]`; the controller treats both as balanced-contact
anchors. `1111` does not assert `OVERLOAD` unless measured z exceeds `theta_o`.

## 6. Planned hardware stop and recovery `[TO BE VALIDATED]`

`OVERLOAD_N` is planned to reach the motor-enable gate without MCU intervention, but
P13 enable/brake polarity, P14 safety action, power-up/down state, fault injection,
and overload-to-disable latency are not yet validated. Do not state that hardware has
already disabled the motor. After interface validation, the MCU may select among:

- coast and wait;
- brake;
- controlled release after the MCU is awake;
- latched disabled until operator reset.

Never command release directly from the comparator without confirming that release
cannot worsen slip, impact, or pinch risk.

## 7. Timing records required in firmware

Timestamp on one clock:

```text
t_event_gpio
t_hardware_motor_disable
t_mcu_wake
t_adc_enable
t_first_valid_vector
t_motor_command
t_mechanical_response
```

These timestamps separate comparator performance, firmware wake, ADC wake, command
latency, and mechanical response.

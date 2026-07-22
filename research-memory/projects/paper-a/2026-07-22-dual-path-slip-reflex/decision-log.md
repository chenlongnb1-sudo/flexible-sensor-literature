# Decision log

## D1. Paper identity

主线为同一组三矢量支持的双时间尺度触觉系统：慢通路负责表面状态感知和参数配置，快通路负责 ADC 前滑移风险判断和有界反射。A1-A4 只作为验证架构因果关系的实验框架。

固定三矢量定义：

```text
Vx = V1 - V3
Vy = V2 - V4
Vz = V1 + V2 + V3 + V4
```

三矢量是任务相关、有损表示，不是完整触觉图像重建，也不是未经标定的三维力计量。

## D2. Slow path

- ADC 采集 `Vz/Vx/Vy` 时序，用于表面/纹理类别识别。
- 分类输出只选择低、中、高三个离散档位，不输出连续“精确摩擦系数”。
- 两个 GPIO 可控制模拟开关，从三组校准后的电阻比例中选择一组。
- 一次抓取开始后冻结所选档位，快速通路不再连续自适应。

## D3. Fast path

快速通路在量化前并行判断：

```text
+Vx - lambda*Vz > theta_x
-Vx - lambda*Vz > theta_x
+Vy - lambda*Vz > theta_y
-Vy - lambda*Vz > theta_y
```

任一条件满足时输出 `SLIP_RISK`。在没有独立力传感器标定 `Ft/Fz` 前，`lambda` 必须称为 `texture-conditioned slip-margin coefficient`，不能直接称为真实摩擦系数。

## D4. Reflex action and MCU boundary

- `SLIP_RISK` 只触发一次定宽、定幅、带死区/迟滞的 `GRIP_INC` 请求。
- 比较器不能直接驱动电机无限闭合。
- 快速事件判定绕过 ADC 转换和高级 MCU 处理，但整套抓取系统仍可包含 MCU 和电机控制器。
- MCU 可配置档位与阈值、快照 GPIO、记录时间戳、按需采集短 burst、监督安全和处理恢复。
- `OVERLOAD_N` 直接硬件禁能仍为 `[TO BE VALIDATED]`，不能按已实现结果表述。

## D5. A1-A4 evaluation contract

```text
A1 Raw-4 continuous: 4 ADC channels, continuous digital vector computation
A2 Vector-3 continuous: analog Vz/Vx/Vy, 3 ADC channels, continuous processing
A3 ADC-first event: matched vector AFE, ADC/digital monitor active, main MCU wakes on event
A4 Pre-ADC event: matched vector AFE, comparators form events before ADC, burst acquisition after event
```

A1-vs-A2 隔离 4 路到 3 路矢量化收益；A3-vs-A4 隔离事件形成位置。A3/A4 必须共享传感器、矢量 AFE、ADC/reference、活动采样率、物理阈值、burst 设置、下游控制和任务条件。

## D6. Event-driven claim boundary

- ADC-first 和 pre-ADC 都能实现事件驱动控制。
- 只有当 `ADC_EN/CS/DRDY` 和 ADC/reference 电流证明空闲期停止转换或进入数据手册定义的待机状态时，才可写 `event-triggered acquisition` 或 `ADC-gated acquisition`。
- 如果 ADC 仍连续采样，只能写 `hardware-thresholded event-driven control`。
- 外部示波器/DAQ 可持续记录，但必须位于部署电子系统和功耗边界之外。

## D7. Fig. 5 role

Fig. 5 证明：连续 `Vz/Vx/Vy` 是有损的任务坐标，冻结比较器阈值可把它们转换为接触、正负方向和过载事件。

- a：投影公式与 `0101/1010 -> [2,0,0]` 简并。
- b：恒总载荷下的连续 x/y 比例标定。
- c：比较器事件生成。
- d：分层硬件事件逻辑。
- e：冻结阈值后的独立同步时序。
- f：逐引脚错误、延迟和非法/并发事件审计。

数据面板在实验完成前必须保留 `[TO BE MEASURED]`。

## D8. Fig. 6 role

主对象使用标准刚性圆柱体。稳定抓取后，用标定砝码/线轮或位移台施加随机化 `+/-x`、`+/-y` 扰动；不得用手推作为正式刺激。记录同一时钟下的载荷真值、`Vz/Vx/Vy`、事件脚、ADC 活动、ADC/reference 电流、`MCU_ACTIVE`、控制命令、电机状态和物体位移。

核心比较包括：无方向控制、最强公平 `Vz-only` 触发、完整三矢量控制，以及 A1-A4 数据量、占空比、每任务电子能量和事件率收支平衡点。执行器能量与触觉电子能量分开报告。

## D9. Three-day priority

1. Day 1：同步矢量验证、串扰矩阵、恒总载荷比例扫描。
2. Day 2：强预载下 raw/数字后差分/模拟前差分三路径及 8/10/12/16-bit 离线量化。
3. Day 3：冻结阈值事件验证、A1-A4 功耗与占空比、圆柱体抓取扰动任务。

同步采集和公平基线不能因时间不足而删除；机器人泛化对象和额外力级可以后移。

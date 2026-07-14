# 2026-07-14 柔性电子皮肤前端触觉计算文献日报

## 今日结论

本次从 OpenAlex、Crossref、Semantic Scholar 和 arXiv 检索最近 30 天结果，去重并排除历史已收录论文后保留 5 篇。
排序优先考虑 ADC 前模拟触觉、矢量/剪切/摩擦读出、低冗余阵列、物理投影和容错迁移；只强调材料灵敏度而缺少系统价值的论文已降权。

- 今日必看：1 篇
- 值得追踪：3 篇
- 新增可评估 idea：5 个
- 历史重复排除：0 篇

## 今日必看

### 1. [GelNeuro: A Sensing-Computing Integrated Neuromorphic Tactile System for Texture Recognition](https://arxiv.org/abs/2607.05241)

- 来源：arXiv (Cornell University)；2026-07-06；评分 83/100
- 为什么重要：涉及 in-sensor/物理计算或可编程触觉前端；涉及坏点、漂移、跨器件迁移或少样本校准
- 摘要级结论：Neuromorphic visuo-tactile sensing offers a promising paradigm for low-latency and low-power robotic perception.
- 方法：This paper presents GelNeuro, a fully integrated sensing-computing visuo-tactile system that directly pairs a GelSight Mini-based optical tactile front end with the Speck2f neuromorphic system-on-chip (SoC).
- 摘要数值：96.3%、80 ms、19.6 mW
- 可迁移：涉及 in-sensor/物理计算或可编程触觉前端；涉及坏点、漂移、跨器件迁移或少样本校准；可对照 raw pixel、software feature 与 physical projection 的性能/通道/功耗
- 风险：当前为题录/摘要级初筛，论文结论、对照和数值必须在精读全文后核实。
- 建议操作：read

## 值得追踪

| 评分 | 轨道 | 论文 | 建议 |
|---:|---|---|---|
| 64 | P6, P1, P5 | [Design, Validation, and Metrological Limits of Biofidelic Instrumentation in PFL Collaborative Robotics: A Systematic Review of Longitudinal Trends and Future Paradigms](https://doi.org/10.3390/s26133984) | skim |
| 63 | P6, P1, P4 | [Femtosecond laser-engraved ultra-broad-range pressure sensors with enhanced sensitivity](https://doi.org/10.1088/2631-7990/ae83ec) | skim |
| 63 | P1, P3, P5 | [Vision-based tactile sensing enhanced by microstructures and lightweight convolutional neural network](https://doi.org/10.1038/s41378-026-01355-5) | skim |

## 方法与指标速览

| 论文 | 方法（摘要证据） | 可核实数值 | 画像价值 |
|---|---|---|---|
| GelNeuro: A Sensing-Computing Integrated Neuromorphic Tactile System for Texture Recognition | This paper presents GelNeuro, a fully integrated sensing-computing visuo-tactile system that directly pairs a GelSight Mini-based optical tactile front end with the Speck2f neuromorphic system-on-chip (SoC). | 96.3%、80 ms、19.6 mW | 涉及 in-sensor/物理计算或可编程触觉前端；涉及坏点、漂移、跨器件迁移或少样本校准 |
| Design, Validation, and Metrological Limits of Biofidelic Instrumentation in PFL Collaborative Robotics: A Systematic Review of Longitudinal Trends and Future Paradigms | This review article systematically maps the technological and normative development of certified Pressure and Force Measurement Devices (PFMDs) and experimental biofidelic instruments for Physical Human–Robot Interaction | 摘要未给出 | 提供机器人、可穿戴或电子皮肤系统任务证据；可用于低离散/装配容差触觉界面的结构与对照设计 |
| Femtosecond laser-engraved ultra-broad-range pressure sensors with enhanced sensitivity | Abstract Achieving flexible pressure sensors that simultaneously combine ultra-high sensitivity, ultra-broad detection range, and low detection limit remains a major challenge due to the intrinsic trade-off between signa | 6414 kPa、800 kPa、3.4 Pa、30 ms | 提供机器人、可穿戴或电子皮肤系统任务证据；可用于低离散/装配容差触觉界面的结构与对照设计 |
| Vision-based tactile sensing enhanced by microstructures and lightweight convolutional neural network | This paper presents a comprehensive approach combining a novel microstructure-based sensor design and efficient image processing, demonstrating that carefully engineered microstructures can significantly enhance performa | 5 mN、0.05 mm | 可用于低离散/装配容差触觉界面的结构与对照设计；涉及低冗余阵列、空间特征或读出通道压缩 |
| Triboelectric Wearable Sensors for Human-Centric Smart Electronics: From Self-Powered Sensing to Artificial Intelligence-Assisted Human–Machine Interface Systems | Triboelectric wearable sensors are particularly attractive in this regard because they directly transduce human-generated mechanical stimuli, provide broad material and structural design freedom, and are readily adaptabl | 摘要未给出 | 涉及 ADC 前模拟矢量、剪切/摩擦/方向相关触觉读出；提供机器人、可穿戴或电子皮肤系统任务证据 |

## 今日创新点候选

### Idea 1：把论文机制映射为 3x3 可编程物理触觉投影核

- 对应轨道：P4；分级：A
- 来源论文：GelNeuro: A Sensing-Computing Integrated Neuromorphic Tactile System for Texture Recognition
- 核心假设：Ksum/Kx/Ky/Klap/Kring/Kcorner 等可解释投影可在 ADC 前形成，并与软件投影保持一致。
- 最小实验：先用 3x3 精密电阻阵列施加标准图案，再迁移到触觉阵列，比较六类投影核的硬件与软件输出。
- 对照：raw scanning；software projection；fixed hardware kernel；programmable hardware kernel
- 成功指标：hardware-software R2；linearity；kernel switching error；ADC count；latency
- 用户操作：加入画像提案 / 观察 / 转任务 / 拒绝

### Idea 2：把论文的鲁棒/迁移策略加入物理投影坏点渐进退化实验

- 对应轨道：P5；分级：A
- 来源论文：GelNeuro: A Sensing-Computing Integrated Neuromorphic Tactile System for Texture Recognition
- 核心假设：归一化物理投影特征在坏点、漂移和跨器件变化下应比 raw readout 更平滑退化，并减少重标定样本。
- 最小实验：设置 0/1/5/10/20% 等效坏点与增益漂移，比较 raw、software projection、hardware projection 及少样本校准。
- 对照：raw readout；software projection；hardware projection；hardware projection + few-shot calibration
- 成功指标：accuracy degradation；feature drift；calibration samples；fault ratio；cross-device variance
- 用户操作：加入画像提案 / 观察 / 转任务 / 拒绝

### Idea 3：把论文系统任务压缩成不拖累主线的最小闭环演示

- 对应轨道：P6；分级：A
- 来源论文：GelNeuro: A Sensing-Computing Integrated Neuromorphic Tactile System for Texture Recognition
- 核心假设：一个受控的纹理/滑移/抓取演示足以证明前端特征的任务价值，无需把主张扩展成完整机器人系统。
- 最小实验：选择单一任务，固定机械输入和后端分类器，只消融 raw、z-only 与前端矢量/投影特征。
- 对照：raw signal；z-only；front-end vector/projection
- 成功指标：task accuracy；response time；channel count；failure cases
- 用户操作：加入画像提案 / 观察 / 转任务 / 拒绝

### Idea 4：把论文中的结构机制转成偏移/旋转/接触半径容差地图

- 对应轨道：P1；分级：B
- 来源论文：Design, Validation, and Metrological Limits of Biofidelic Instrumentation in PFL Collaborative Robotics: A Systematic Review of Longitudinal Trends and Future Paradigms
- 核心假设：若界面机制真正降低输入离散性，其优势应在装配扰动和接触条件变化下保持，而不只体现在灵敏度。
- 最小实验：在统一载荷下扫描 shift、rotation 与 contact radius，输出 CV、signal-void ratio 和 sensitivity map。
- 对照：周期电极+常规微结构；周期电极+HCP；梯度/非周期电极+常规微结构；目标结构
- 成功指标：CV；shift sensitivity；rotation sensitivity；contact-radius sensitivity；signal void ratio
- 用户操作：加入画像提案 / 观察 / 转任务 / 拒绝

### Idea 5：把论文的阵列读出策略改写为低冗余 hardware macro-pixel 对照

- 对应轨道：P3；分级：B
- 来源论文：Vision-based tactile sensing enhanced by microstructures and lightweight convolutional neural network
- 核心假设：可解释的局部矢量/空间投影能以更少读出通道保持边缘、形状和滑移方向信息。
- 最小实验：在同一阵列输入上比较 raw scanning、scalar pooling、software gradient 与 hardware macro-pixel。
- 对照：raw pixel scanning；scalar pooling；software gradient；hardware macro-pixel
- 成功指标：channel count；latency；power；edge/shape accuracy；direction accuracy
- 用户操作：加入画像提案 / 观察 / 转任务 / 拒绝

## 检索记录

| 来源 | 查询 | 命中 | 状态 |
|---|---|---:|---|
| crossref | `electronic skin fault tolerant transferable calibration domain adaptation` | 25 | ok |
| openalex | `electronic skin fault tolerant transferable calibration domain adaptation` | 1 | ok |
| crossref | `electronic skin tactile array compressed readout low channel` | 25 | ok |
| openalex | `electronic skin tactile array compressed readout low channel` | 7 | ok |
| crossref | `tactile sensor physical computing analog computing programmable projection` | 25 | ok |
| openalex | `tactile sensor physical computing analog computing programmable projection` | 5 | ok |
| crossref | `tactile sensor analog front-end in-sensor computing` | 25 | ok |
| openalex | `tactile sensor analog front-end in-sensor computing` | 21 | ok |
| crossref | `flexible tactile sensor assembly tolerance response dispersion electrode microstructure` | 25 | ok |
| openalex | `flexible tactile sensor assembly tolerance response dispersion electrode microstructure` | 2 | ok |
| crossref | `flexible tactile sensor vector shear friction slip direction` | 25 | ok |
| openalex | `flexible tactile sensor vector shear friction slip direction` | 2 | ok |

## 数据源异常

- semantic_scholar：6 个查询失败；首个错误为 HTTPError: HTTP Error 429: 。其余来源已继续运行。
- arxiv：4 个查询失败；首个错误为 TimeoutError: The read operation timed out。其余来源已继续运行。

## 纳入与排除标准

- 纳入：论文能服务 P1-P6 至少一条主线，并能形成机制、前端、阵列、系统任务或可验证对照。
- 降权：只强调 sensitivity、gauge factor 或材料配方，而缺少读出、阵列、校准、鲁棒性或任务证据。
- 排除：历史已收录、题录明显偏题、来源元数据不足且无法核实。
- 可信度边界：本日报首先完成题录/摘要级筛选；数值、机理和优先级需在点击“精读”后核查全文。

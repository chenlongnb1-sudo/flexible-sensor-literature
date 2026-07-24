# 2026-07-24 柔性电子高水平文献日报

## 今日结论

本次从 OpenAlex、Crossref、Semantic Scholar、arXiv 和 Science 官网 RSS 检索最近 3 天结果，去重并排除历史已收录论文后保留 17 篇。
期刊等级采用硬门槛：仅保留 Nature/Science 旗舰与子刊、Cell 子刊、Advanced Materials/AFM 及明确同等级期刊；预印本、会议论文和普通期刊不进入正式推荐。
所有柔性电子相关论文均进入分类日报；与 ADC 前模拟触觉、矢量读出、低冗余阵列、物理投影和容错迁移直接相关的论文标为强相关并生成创新建议。

- 今日必看：3 篇
- 值得追踪：12 篇
- 新增可评估 idea：3 个
- 历史重复排除：27 篇
- 期刊等级排除：20 篇
- 小类分布：电子皮肤与触觉 2 篇；神经形态与传感计算 3 篇；软体机器人与人机交互 3 篇；多模态与生化传感 3 篇；可穿戴健康与生理监测 1 篇；柔性能源与自供能 1 篇；柔性材料与器件 4 篇

## 今日必看

### 1. [Self‐Driven Hybrid Piezomagnetic–Iontronic Mechanoreceptors for Bimodal SA/RA Perception and Tactile Synthesis](https://doi.org/10.1002/smll.74799)

- 来源：Small；2026-07-23；分类：电子皮肤与触觉；评分 65/100
- 为什么重要：涉及 ADC 前模拟矢量、剪切/摩擦/方向相关触觉读出；涉及 in-sensor/物理计算或可编程触觉前端
- 摘要级结论：涉及 ADC 前模拟矢量、剪切/摩擦/方向相关触觉读出；涉及 in-sensor/物理计算或可编程触觉前端。摘要可核实数值包括：15 mV、3.2 N、1 kHz、0.48 mV、0.75 mV。
- 方法：Here, we present a tactile sensing system based on hybrid materials that integrate an Fe 3 O 4 ‐based piezomagnetic elastomer and a poly(vinyl chloride) (PVC)‐based iontronic gel in a unified layered architecture, enabling the orthogonal encoding of SA and RA mechanotransduction.
- 摘要数值：15 mV、3.2 N、1 kHz、0.48 mV、0.75 mV
- 可迁移：涉及 ADC 前模拟矢量、剪切/摩擦/方向相关触觉读出；涉及 in-sensor/物理计算或可编程触觉前端；优先核查是否有 hardware output 与 software projection 的同步一致性证据
- 给你的创新建议：将法向/剪切/摩擦信息改写为 ADC 前差分或矢量组合，并同步比较 hardware output 与 software vector 的 R2、PSD/SNR。
- 风险：当前为题录/摘要级初筛，论文结论、对照和数值必须在精读全文后核实。；开放获取 PDF 下载失败：RuntimeError。
- 建议操作：skim

### 2. [Monolithic 6-Axis Force/Torque Sensing by a Single Ultrathin Piezoceramic Shell](https://doi.org/10.1038/s41467-026-75631-3)

- 来源：Nature Communications；2026-07-21；分类：软体机器人与人机交互；评分 44/100
- 为什么重要：可用于低离散/装配容差触觉界面的结构与对照设计；涉及 ADC 前模拟矢量、剪切/摩擦/方向相关触觉读出
- 摘要级结论：可用于低离散/装配容差触觉界面的结构与对照设计；涉及 ADC 前模拟矢量、剪切/摩擦/方向相关触觉读出。摘要可核实数值包括：99.37%、3 mN、4 mN、0.3 mN、2.53 cm。
- 方法：Miniature multi-axis force/torque sensors are essential for advanced robotics and wearable devices, yet their development is hindered by complex multi-beam structures and laborious calibration.
- 摘要数值：99.37%、3 mN、4 mN、0.3 mN、2.53 cm
- 可迁移：可用于低离散/装配容差触觉界面的结构与对照设计；涉及 ADC 前模拟矢量、剪切/摩擦/方向相关触觉读出；优先核查是否有 hardware output 与 software projection 的同步一致性证据
- 给你的创新建议：将法向/剪切/摩擦信息改写为 ADC 前差分或矢量组合，并同步比较 hardware output 与 software vector 的 R2、PSD/SNR。；加入坏点比例、增益漂移和跨器件迁移实验，比较重标定样本量与性能渐进退化，形成可靠性主张。
- 风险：当前为题录/摘要级初筛，论文结论、对照和数值必须在精读全文后核实。；可能主要贡献是材料灵敏度，未必能支撑前端触觉计算主线。
- 建议操作：skim

### 3. [Ultra‐Sensitive, Ultra‐Linear, Temperature‐Robust Yarn Sensor for Intelligent Monitoring Under Harsh Thermal Condition](https://doi.org/10.1002/adfm.77096)

- 来源：Advanced Functional Materials；2026-07-23；分类：可穿戴健康与生理监测；评分 40/100
- 为什么重要：可用于低离散/装配容差触觉界面的结构与对照设计；涉及坏点、漂移、跨器件迁移或少样本校准
- 摘要级结论：可用于低离散/装配容差触觉界面的结构与对照设计；涉及坏点、漂移、跨器件迁移或少样本校准。摘要可核实数值包括：99.9%、98 ms、0.05%。
- 方法：Here we propose a hierarchical assembly strategy to address these limitations and develop a temperature‐robust yarn sensor (TRYS).
- 摘要数值：99.9%、98 ms、0.05%
- 可迁移：可用于低离散/装配容差触觉界面的结构与对照设计；涉及坏点、漂移、跨器件迁移或少样本校准；可对照 raw pixel、software feature 与 physical projection 的性能/通道/功耗
- 给你的创新建议：加入坏点比例、增益漂移和跨器件迁移实验，比较重标定样本量与性能渐进退化，形成可靠性主张。
- 风险：当前为题录/摘要级初筛，论文结论、对照和数值必须在精读全文后核实。；可能主要贡献是材料灵敏度，未必能支撑前端触觉计算主线。
- 建议操作：skim

## 其他柔性电子相关论文

| 分类 | 评分 | 论文 | 建议 |
|---|---:|---|---|
| 神经形态与传感计算 | 56 | [All-solution-processable hydrogen-bonded organic framework artificial synapse for neuromorphic application](https://doi.org/10.1088/2631-7990/ae8f85) | skim |
| 软体机器人与人机交互 | 54 | [High-Strength, Self-Sensing Multiphase Hydrogels for Load-Bearing Actuation and Logical Human–Machine Interaction](https://doi.org/10.1007/s40820-026-02280-y) | skim |
| 神经形态与传感计算 | 52 | [Programmable Nanofluidic Memristors Based on Hierarchical Nanochannel/Ionchannel Composite as Artificial Synapses](https://doi.org/10.1002/adfm.77342) | skim |
| 多模态与生化传感 | 43 | [A fully integrated smart ring for daily biochemical monitoring](https://doi.org/10.1038/s41467-026-75980-z) | skim |
| 多模态与生化传感 | 43 | [Acoustic Mixed Photothermal Actuators for Multimodal Amphibious Robots](https://doi.org/10.1002/admt.71201) | skim |
| 多模态与生化传感 | 40 | [Flanking‐Group Engineering Unlocks Emerging Functionalities in Diketopyrrolopyrrole Semiconductors](https://doi.org/10.1002/advs.76548) | skim |
| 神经形态与传感计算 | 40 | [A Minimalist, Flexible, Transparent, and Water‐Degradable Ultraviolet Photodetector for Visible‐Blind Applications](https://doi.org/10.1002/admt.71194) | skim |
| 软体机器人与人机交互 | 33 | [Double Helix Structure for Stable Flexural Actuation in Soft Robotics](https://doi.org/10.1002/aisy.202501383) | skim |
| 柔性能源与自供能 | 33 | [Stretchable and Self‐Healable Acoustic Sensor for Fast Respiratory Diseases Identification Based on Biocompatible Piezoelectric Polyester Elastomer](https://doi.org/10.1002/smll.74718) | skim |
| 柔性材料与器件 | 32 | [Spatially Resolved Strain Mapping In Flexible Oxide Membranes](https://doi.org/10.1002/smll.74801) | skim |
| 柔性材料与器件 | 30 | [Data-driven design of disordered structures for direction- and geometry-independent stretchable electrodes](https://doi.org/10.1038/s41528-026-00620-x) | skim |
| 电子皮肤与触觉 | 30 | [Graphene-Skinned Glass Fiber Fabric for Seamless Structural–Functional Integration in Advanced Composites](https://doi.org/10.1021/acsnano.6c07455) | skim |

## 方法与指标速览

| 论文 | 方法（摘要证据） | 可核实数值 | 画像价值 |
|---|---|---|---|
| Self‐Driven Hybrid Piezomagnetic–Iontronic Mechanoreceptors for Bimodal SA/RA Perception and Tactile Synthesis | Here, we present a tactile sensing system based on hybrid materials that integrate an Fe 3 O 4 ‐based piezomagnetic elastomer and a poly(vinyl chloride) (PVC)‐based iontronic gel in a unified layered architecture, enabli | 15 mV、3.2 N、1 kHz、0.48 mV、0.75 mV | 涉及 ADC 前模拟矢量、剪切/摩擦/方向相关触觉读出；涉及 in-sensor/物理计算或可编程触觉前端 |
| All-solution-processable hydrogen-bonded organic framework artificial synapse for neuromorphic application | An all-solution-processed 10×10 2D MXene/TCPP-HOF/MXene/polyimine (PI) heterostructured flexible device array using MXene as electrode and PI as substrate is fabricated, presenting gradient conductance modulation under b | 摘要未给出 | 涉及 in-sensor/物理计算或可编程触觉前端；可用于低离散/装配容差触觉界面的结构与对照设计 |
| High-Strength, Self-Sensing Multiphase Hydrogels for Load-Bearing Actuation and Logical Human–Machine Interaction | Based on the corresponding relationship between the mass of the load and the actuation behavior (such as "0/1" encoding), we develop a novel material-based binary information encoding system. | 摘要未给出 | 提供机器人、可穿戴或电子皮肤系统任务证据；涉及 in-sensor/物理计算或可编程触觉前端 |
| Programmable Nanofluidic Memristors Based on Hierarchical Nanochannel/Ionchannel Composite as Artificial Synapses | Hierarchical structural design offers a potent route to tailor ion transport properties, harnessing multiscale asymmetry to integrate divergent transport regimes within a unified architecture. | 摘要未给出 | 涉及 in-sensor/物理计算或可编程触觉前端；涉及坏点、漂移、跨器件迁移或少样本校准 |
| Monolithic 6-Axis Force/Torque Sensing by a Single Ultrathin Piezoceramic Shell | Miniature multi-axis force/torque sensors are essential for advanced robotics and wearable devices, yet their development is hindered by complex multi-beam structures and laborious calibration. | 99.37%、3 mN、4 mN、0.3 mN、2.53 cm | 可用于低离散/装配容差触觉界面的结构与对照设计；涉及 ADC 前模拟矢量、剪切/摩擦/方向相关触觉读出 |
| A fully integrated smart ring for daily biochemical monitoring | Overall, our ring extends beyond commercial smart rings focusing on only biophysical signals, by enabling continuous assessment of biochemical changes and advancing the development of next generation personalized and min | 摘要未给出 | 涉及坏点、漂移、跨器件迁移或少样本校准 |
| Acoustic Mixed Photothermal Actuators for Multimodal Amphibious Robots | This work provides a practical fabrication paradigm for multifunctional soft robotic systems designed for complex, cross‐domain environments. | 350 mW | 可用于低离散/装配容差触觉界面的结构与对照设计；涉及坏点、漂移、跨器件迁移或少样本校准 |
| Ultra‐Sensitive, Ultra‐Linear, Temperature‐Robust Yarn Sensor for Intelligent Monitoring Under Harsh Thermal Condition | Here we propose a hierarchical assembly strategy to address these limitations and develop a temperature‐robust yarn sensor (TRYS). | 99.9%、98 ms、0.05% | 可用于低离散/装配容差触觉界面的结构与对照设计；涉及坏点、漂移、跨器件迁移或少样本校准 |
| Flanking‐Group Engineering Unlocks Emerging Functionalities in Diketopyrrolopyrrole Semiconductors | Conventional DPP synthesis relies on aromatic nitrile precursors, establishing a design paradigm in which flanking aromatic units govern energy levels, molecular packing, and charge transport. | 摘要未给出 | 可用于低离散/装配容差触觉界面的结构与对照设计；涉及坏点、漂移、跨器件迁移或少样本校准 |
| A Minimalist, Flexible, Transparent, and Water‐Degradable Ultraviolet Photodetector for Visible‐Blind Applications | ABSTRACT The advancement of flexible and transparent photodetectors represents a technological frontier for wearable electronics and imperceptible monitoring networks. | 89%、405 nm、0.4 cm、200 V | 可用于低离散/装配容差触觉界面的结构与对照设计；涉及 in-sensor/物理计算或可编程触觉前端 |
| Double Helix Structure for Stable Flexural Actuation in Soft Robotics | While such designs offer a high degree of mechanical compliance, they can lead to inadvertent twisting and loss of mechanical stability. | 50% | 提供机器人、可穿戴或电子皮肤系统任务证据 |
| Stretchable and Self‐Healable Acoustic Sensor for Fast Respiratory Diseases Identification Based on Biocompatible Piezoelectric Polyester Elastomer | In this study, a stretchable and self‐healable acoustic sensor is fabricated based on bio‐based piezoelectric elastomer (BBPE) to realize fast respiratory diseases identification. | 0.1%、1200%、79% | 提供机器人、可穿戴或电子皮肤系统任务证据 |
| Spatially Resolved Strain Mapping In Flexible Oxide Membranes | However, accurately determining strain transfer and distribution within these membranes remains challenging, limiting direct correlations between structural distortion and functional response and hindering the rational d | 摘要未给出 | 涉及坏点、漂移、跨器件迁移或少样本校准 |
| Data-driven design of disordered structures for direction- and geometry-independent stretchable electrodes | 当前题录没有摘要，需打开原文核实方法。 | 摘要未给出 | 可用于低离散/装配容差触觉界面的结构与对照设计 |
| Graphene-Skinned Glass Fiber Fabric for Seamless Structural–Functional Integration in Advanced Composites | 当前题录没有摘要，需打开原文核实方法。 | 摘要未给出 | 提供机器人、可穿戴或电子皮肤系统任务证据 |
| Rational Design of π‐Conjugated Polymers for Enantioselective Recognition of Amino Acids | In this work, we report the rational design of a specific class of conducting polymers with chiral features for the enantiodiscrimination of amino acids. | 摘要未给出 | 与柔性触觉相关，但尚未显示对前端触觉计算的直接贡献 |
| Bioinspired Permeable Soft Electronics for Advanced Healthcare Monitoring | 当前题录没有摘要，需打开原文核实方法。 | 摘要未给出 | 与柔性触觉相关，但尚未显示对前端触觉计算的直接贡献 |

## 今日创新点候选

### Idea 1：把新型矢量/剪切读出转成 ADC 前硬件-软件一致性证据

- 对应轨道：P2；分级：B
- 来源论文：Self‐Driven Hybrid Piezomagnetic–Iontronic Mechanoreceptors for Bimodal SA/RA Perception and Tactile Synthesis
- 核心假设：ADC 前 Kz/Kx/Ky 类模拟组合应保留任务相关方向信息，并减少后端通道和计算。
- 最小实验：同步记录 raw A/B/C/D、software vector 与 hardware vector，在相同纹理/滑动/剪切输入下做波形、PSD/SNR、R2 和任务消融。
- 对照：raw four-channel；z-only；software vector；hardware vector；reference force
- 成功指标：hardware-software R2；PSD/SNR；task accuracy；latency；ADC channel count
- 用户操作：加入画像提案 / 观察 / 转任务 / 拒绝

### Idea 2：把论文机制映射为 3x3 可编程物理触觉投影核

- 对应轨道：P4；分级：B
- 来源论文：Self‐Driven Hybrid Piezomagnetic–Iontronic Mechanoreceptors for Bimodal SA/RA Perception and Tactile Synthesis
- 核心假设：Ksum/Kx/Ky/Klap/Kring/Kcorner 等可解释投影可在 ADC 前形成，并与软件投影保持一致。
- 最小实验：先用 3x3 精密电阻阵列施加标准图案，再迁移到触觉阵列，比较六类投影核的硬件与软件输出。
- 对照：raw scanning；software projection；fixed hardware kernel；programmable hardware kernel
- 成功指标：hardware-software R2；linearity；kernel switching error；ADC count；latency
- 用户操作：加入画像提案 / 观察 / 转任务 / 拒绝

### Idea 3：把论文系统任务压缩成不拖累主线的最小闭环演示

- 对应轨道：P6；分级：B
- 来源论文：Self‐Driven Hybrid Piezomagnetic–Iontronic Mechanoreceptors for Bimodal SA/RA Perception and Tactile Synthesis
- 核心假设：一个受控的纹理/滑移/抓取演示足以证明前端特征的任务价值，无需把主张扩展成完整机器人系统。
- 最小实验：选择单一任务，固定机械输入和后端分类器，只消融 raw、z-only 与前端矢量/投影特征。
- 对照：raw signal；z-only；front-end vector/projection
- 成功指标：task accuracy；response time；channel count；failure cases
- 用户操作：加入画像提案 / 观察 / 转任务 / 拒绝

## 检索记录

| 来源 | 目标期刊 | 查询 | 命中 | 状态 |
|---|---|---|---:|---|
| arxiv | - | `electronic skin fault tolerant transferable calibration domain adaptation` | 0 | ok |
| crossref | - | `electronic skin fault tolerant transferable calibration domain adaptation` | 25 | ok |
| openalex | - | `electronic skin fault tolerant transferable calibration domain adaptation` | 0 | ok |
| semantic_scholar | - | `electronic skin fault tolerant transferable calibration domain adaptation` | 0 | failed |
| arxiv | - | `electronic skin tactile array compressed readout low channel` | 0 | ok |
| crossref | - | `electronic skin tactile array compressed readout low channel` | 25 | ok |
| openalex | - | `electronic skin tactile array compressed readout low channel` | 0 | ok |
| semantic_scholar | - | `electronic skin tactile array compressed readout low channel` | 0 | failed |
| arxiv | - | `near-sensor analog computing tactile sensing electronic skin` | 0 | ok |
| crossref | - | `near-sensor analog computing tactile sensing electronic skin` | 25 | ok |
| openalex | - | `near-sensor analog computing tactile sensing electronic skin` | 1 | ok |
| semantic_scholar | - | `near-sensor analog computing tactile sensing electronic skin` | 0 | failed |
| crossref | - | `tactile sensor neuromorphic encoding in-sensor computing robotic perception` | 25 | ok |
| openalex | - | `tactile sensor neuromorphic encoding in-sensor computing robotic perception` | 0 | ok |
| semantic_scholar | - | `tactile sensor neuromorphic encoding in-sensor computing robotic perception` | 0 | failed |
| arxiv | - | `tactile sensor physical computing analog computing programmable projection` | 2 | ok |
| crossref | - | `tactile sensor physical computing analog computing programmable projection` | 25 | ok |
| openalex | - | `tactile sensor physical computing analog computing programmable projection` | 0 | ok |
| semantic_scholar | - | `tactile sensor physical computing analog computing programmable projection` | 0 | failed |
| science_official | - | `electronic skin` | 0 | ok |
| science_official | - | `flexible sensor` | 0 | ok |
| science_official | - | `haptic sensor` | 0 | ok |
| science_official | - | `tactile sensor` | 0 | ok |
| arxiv | - | `tactile sensor analog front-end in-sensor computing` | 2 | ok |
| crossref | - | `tactile sensor analog front-end in-sensor computing` | 25 | ok |
| openalex | - | `tactile sensor analog front-end in-sensor computing` | 2 | ok |
| semantic_scholar | - | `tactile sensor analog front-end in-sensor computing` | 0 | failed |
| crossref | - | `flexible tactile sensor assembly tolerance response dispersion electrode microstructure` | 25 | ok |
| openalex | - | `flexible tactile sensor assembly tolerance response dispersion electrode microstructure` | 1 | ok |
| semantic_scholar | - | `flexible tactile sensor assembly tolerance response dispersion electrode microstructure` | 0 | ok |
| crossref | - | `flexible tactile sensor vector shear friction slip direction` | 25 | ok |
| openalex | - | `flexible tactile sensor vector shear friction slip direction` | 0 | ok |
| semantic_scholar | - | `flexible tactile sensor vector shear friction slip direction` | 0 | failed |
| crossref | ACS Nano | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 22 | ok |
| crossref | Advanced Electronic Materials | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 3 | ok |
| crossref | Advanced Energy Materials | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 18 | ok |
| crossref | Advanced Fiber Materials | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 1 | ok |
| crossref | Advanced Functional Materials | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 104 | ok |
| crossref | Advanced Healthcare Materials | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 11 | ok |
| crossref | Advanced Intelligent Systems | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 3 | ok |
| crossref | Advanced Materials | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 71 | ok |
| crossref | Advanced Materials Technologies | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 9 | ok |
| crossref | Advanced Optical Materials | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 12 | ok |
| crossref | Advanced Science | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 45 | ok |
| crossref | Cell Reports Physical Science | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 0 | ok |
| crossref | Communications Chemistry | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 6 | ok |
| crossref | Communications Engineering | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 8 | ok |
| crossref | Communications Materials | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 8 | ok |
| crossref | Communications Physics | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 4 | ok |
| crossref | Device | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 0 | ok |
| crossref | InfoMat | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 1 | ok |
| crossref | International Journal of Extreme Manufacturing | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 4 | ok |
| crossref | Joule | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 0 | ok |
| crossref | Light: Science & Applications | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 4 | ok |
| crossref | Materials Horizons | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 0 | ok |
| crossref | Matter | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 0 | ok |
| crossref | Microsystems & Nanoengineering | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 6 | ok |
| crossref | Nano Energy | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 0 | ok |
| crossref | Nano Letters | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 21 | ok |
| crossref | Nano-Micro Letters | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 5 | ok |
| crossref | National Science Review | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 8 | ok |
| crossref | Nature | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 58 | ok |
| crossref | Nature Biomedical Engineering | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 2 | ok |
| crossref | Nature Communications | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 178 | ok |
| crossref | Nature Electronics | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 5 | ok |
| crossref | Nature Machine Intelligence | `tactile electronic skin neuromorphic sensor computing robotic perception` | 1 | ok |
| crossref | Nature Materials | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 2 | ok |
| crossref | Nature Nanotechnology | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 7 | ok |
| crossref | Nature Sensors | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 3 | ok |
| crossref | npj Flexible Electronics | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 4 | ok |
| crossref | Proceedings of the National Academy of Sciences | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 51 | ok |
| crossref | Research | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 1 | ok |
| crossref | Science | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 40 | ok |
| crossref | Science Advances | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 40 | ok |
| crossref | Science Robotics | `tactile electronic skin flexible sensor haptic robotic perception` | 3 | ok |
| crossref | Science Translational Medicine | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 9 | ok |
| crossref | Small | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 74 | ok |
| crossref | Small Methods | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 15 | ok |

## 数据源异常

- semantic_scholar：7 个查询失败；首个错误为 HTTPError: HTTP Error 429: 。其余来源已继续运行。

## 纳入与排除标准

- 纳入：达到期刊等级门槛，且属于柔性/可拉伸/可穿戴/皮肤界面电子、柔性器件、软体机器人、自供能或相关传感系统。
- 分类：电子皮肤与触觉、可穿戴健康、柔性材料与器件、柔性能源、软体机器人与 HMI、神经形态/传感计算、制造封装与可靠性、多模态生化传感。
- 强相关：命中阵列读出、矢量/剪切、ADC 前处理、传感计算、校准漂移或跨器件迁移时，额外生成可验证创新建议。
- 降权但保留：只强调 sensitivity、gauge factor 或材料配方，而缺少读出、阵列、校准、鲁棒性或任务证据。
- 排除：历史已收录、题录明显偏题、来源元数据不足且无法核实。
- 可信度边界：本日报首先完成题录/摘要级筛选；数值、机理和优先级需在点击“精读”后核查全文。

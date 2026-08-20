# 2026-08-20 柔性电子高水平文献日报

## 今日结论

本次从 OpenAlex、Crossref、Semantic Scholar、arXiv 和 Science 官网 RSS 检索最近 3 天结果，去重并排除历史已收录论文后保留 16 篇。
期刊等级采用硬门槛：仅保留 Nature/Science 旗舰与子刊、Cell 子刊、Advanced Materials/AFM 及明确同等级期刊；预印本、会议论文和普通期刊不进入正式推荐。
所有柔性电子相关论文均进入分类日报；与 ADC 前模拟触觉、矢量读出、低冗余阵列、物理投影和容错迁移直接相关的论文标为强相关并生成创新建议。

- 今日必看：3 篇
- 值得追踪：12 篇
- 新增可评估 idea：3 个
- 历史重复排除：11 篇
- 期刊等级排除：14 篇
- 小类分布：电子皮肤与触觉 2 篇；软体机器人与人机交互 3 篇；可穿戴健康与生理监测 3 篇；神经形态与传感计算 3 篇；制造、封装与可靠性 2 篇；柔性能源与自供能 2 篇；多模态与生化传感 1 篇

## 今日必看

### 1. [Neuromorphic tactile sensing and haptic display enable fine distributed cutaneous feedback in telepresence](https://doi.org/10.1038/s44172-026-00757-7)

- 来源：Communications Engineering；2026-08-18；分类：电子皮肤与触觉；评分 86/100
- 为什么重要：提供机器人、可穿戴或电子皮肤系统任务证据；涉及 in-sensor/物理计算或可编程触觉前端
- 摘要级结论：提供机器人、可穿戴或电子皮肤系统任务证据；涉及 in-sensor/物理计算或可编程触觉前端。摘要可核实数值包括：16 mm、96 %。
- 方法：This study presents an Integrated Neuromorphic Tactile-Haptic Interface System (INTHIS) enabling a human operator to perceive tactile feedback over the upper limb skin in response to the real-time distributed tactile stimulation of a remote robotic e-skin integrating Fiber Bragg Gratings transducers.
- 摘要数值：16 mm、96 %
- 可迁移：提供机器人、可穿戴或电子皮肤系统任务证据；涉及 in-sensor/物理计算或可编程触觉前端；可对照 raw pixel、software feature 与 physical projection 的性能/通道/功耗
- 给你的创新建议：把文中的传感/计算耦合机制映射为可编程物理投影核，增加原始像素、软件投影和硬件投影三组严格消融。
- 风险：当前为题录/摘要级初筛，论文结论、对照和数值必须在精读全文后核实。；开放获取 PDF 下载失败：链接未返回 PDF。
- 建议操作：read

### 2. [A Bioinspired, Multimodal Soft Tactile Skin with Task‐Adaptive Perception for Intelligent Robotic Manipulation](https://doi.org/10.1002/advs.77230)

- 来源：Advanced Science；2026-08-18；分类：电子皮肤与触觉；评分 84/100
- 为什么重要：涉及 ADC 前模拟矢量、剪切/摩擦/方向相关触觉读出；涉及 in-sensor/物理计算或可编程触觉前端
- 摘要级结论：涉及 ADC 前模拟矢量、剪切/摩擦/方向相关触觉读出；涉及 in-sensor/物理计算或可编程触觉前端。摘要可核实数值包括：97.62%。
- 方法：However, most tactile sensors have deviated from the physiological encoding based on human mechanoreceptors.
- 摘要数值：97.62%
- 可迁移：涉及 ADC 前模拟矢量、剪切/摩擦/方向相关触觉读出；涉及 in-sensor/物理计算或可编程触觉前端；优先核查是否有 hardware output 与 software projection 的同步一致性证据
- 给你的创新建议：将法向/剪切/摩擦信息改写为 ADC 前差分或矢量组合，并同步比较 hardware output 与 software vector 的 R2、PSD/SNR。
- 风险：当前为题录/摘要级初筛，论文结论、对照和数值必须在精读全文后核实。；开放获取 PDF 下载失败：RuntimeError。
- 建议操作：read

### 3. [High‐Fidelity Fabrication of 3D Multiscale‐Structured Pressure Sensors for High‐Performance Wearable Sensing](https://doi.org/10.1002/smll.75240)

- 来源：Small；2026-08-18；分类：制造、封装与可靠性；评分 42/100
- 为什么重要：可用于低离散/装配容差触觉界面的结构与对照设计；提供机器人、可穿戴或电子皮肤系统任务证据
- 摘要级结论：可用于低离散/装配容差触觉界面的结构与对照设计；提供机器人、可穿戴或电子皮肤系统任务证据。摘要可核实数值包括：809 kPa、4%。
- 方法：In this work, a high‐precision and controllable fabrication strategy based on a novel secondary replica molding approach is proposed.
- 摘要数值：809 kPa、4%
- 可迁移：可用于低离散/装配容差触觉界面的结构与对照设计；提供机器人、可穿戴或电子皮肤系统任务证据；把论文结构转成 shift、rotation、contact-radius 与跨器件 CV 的容差地图，验证优势是否超越单点灵敏度。
- 给你的创新建议：把论文结构转成 shift、rotation、contact-radius 与跨器件 CV 的容差地图，验证优势是否超越单点灵敏度。
- 风险：当前为题录/摘要级初筛，论文结论、对照和数值必须在精读全文后核实。；开放获取 PDF 下载失败：RuntimeError。
- 建议操作：skim

## 其他柔性电子相关论文

| 分类 | 评分 | 论文 | 建议 |
|---|---:|---|---|
| 软体机器人与人机交互 | 72 | [BeetleBot: An integrated bioinspired soft robot for multimodal sensing and adaptive interaction](https://www.science.org/doi/abs/10.1126/sciadv.aeg8849) | add_to_ideas |
| 可穿戴健康与生理监测 | 60 | [Intelligent Foot Perception System Based on Flexible MXene Triboelectric Sensing and Deep Learning for Motion Recognition and Health Monitoring](https://doi.org/10.1002/admt.71263) | skim |
| 软体机器人与人机交互 | 58 | [Programmable Pneumatic Actuator System for a Bioinspired Artificial Colon](https://doi.org/10.1002/admt.71240) | skim |
| 神经形态与传感计算 | 56 | [Fibrous Neuromorphic Electronics: From Single Device to All-Fiber System](https://doi.org/10.1021/acs.nanolett.6c02650) | skim |
| 神经形态与传感计算 | 48 | [Analog Synaptic Plasticity in 2D Layered Material Iontronic Memtransistors for Brain‐Inspired Computing](https://doi.org/10.1002/advs.77150) | skim |
| 神经形态与传感计算 | 46 | [Elastomer‐Assisted Segregation Growth of Large‐Scale Stretchable Organic Crystalline Films for Flexible Photosynapses](https://doi.org/10.1002/smll.75292) | skim |
| 可穿戴健康与生理监测 | 43 | [A Fully Integrated Wearable Sensor for Real Time Monitoring of Multiple Sweat Liver Disease Biomarkers](https://doi.org/10.1002/adma.74688) | skim |
| 可穿戴健康与生理监测 | 42 | [Wearable Sensing Devices for Continuous Animal Health Monitoring](https://doi.org/10.1002/smtd.70982) | skim |
| 软体机器人与人机交互 | 41 | [Shearing‐Assisted Interfacial Exfoliation of Graphene Inks for Embodied Intelligence](https://doi.org/10.1002/smll.75299) | skim |
| 柔性能源与自供能 | 40 | [Tendon‐Inspired Multiscale Bamboo‐Based Ionic Gel for High‐Performance Flexible Energy Conversion](https://doi.org/10.1002/adfm.77773) | skim |
| 制造、封装与可靠性 | 39 | [Flexible and Scalable 2D/3D Tin‐Based Perovskite Photodetectors via Inkjet Printing](https://doi.org/10.1002/adom.71629) | skim |
| 多模态与生化传感 | 37 | [Energy‐Transfer‐Driven Programmable Luminescence in Bi 3+ ‐Eu 3+ Co‐Doped Na 3 Ca 2 TaO 6 Phosphors Toward Multifunctional Optical Applications](https://doi.org/10.1002/adom.71631) | skim |

## 方法与指标速览

| 论文 | 方法（摘要证据） | 可核实数值 | 画像价值 |
|---|---|---|---|
| Neuromorphic tactile sensing and haptic display enable fine distributed cutaneous feedback in telepresence | This study presents an Integrated Neuromorphic Tactile-Haptic Interface System (INTHIS) enabling a human operator to perceive tactile feedback over the upper limb skin in response to the real-time distributed tactile sti | 16 mm、96 % | 提供机器人、可穿戴或电子皮肤系统任务证据；涉及 in-sensor/物理计算或可编程触觉前端 |
| A Bioinspired, Multimodal Soft Tactile Skin with Task‐Adaptive Perception for Intelligent Robotic Manipulation | However, most tactile sensors have deviated from the physiological encoding based on human mechanoreceptors. | 97.62% | 涉及 ADC 前模拟矢量、剪切/摩擦/方向相关触觉读出；涉及 in-sensor/物理计算或可编程触觉前端 |
| BeetleBot: An integrated bioinspired soft robot for multimodal sensing and adaptive interaction | Here, we present BeetleBot, an adaptive beetle-bioinspired soft robot platform that seamlessly integrates programmable locomotion, object manipulation, sensory feedback, and intuitive human-machine interaction. | 摘要未给出 | 提供机器人、可穿戴或电子皮肤系统任务证据；涉及 in-sensor/物理计算或可编程触觉前端 |
| Intelligent Foot Perception System Based on Flexible MXene Triboelectric Sensing and Deep Learning for Motion Recognition and Health Monitoring | This study presents an intelligent foot perception system for wearable health monitoring. | 0.91 mW、1.3 V、200 kPa、15.6 Pa、97.6% | 涉及 ADC 前模拟矢量、剪切/摩擦/方向相关触觉读出；提供机器人、可穿戴或电子皮肤系统任务证据 |
| Programmable Pneumatic Actuator System for a Bioinspired Artificial Colon | A programmable pneumatic actuator system is presented in this paper, integrated within a modular soft robotic colon simulator that mimics physiological motility through distributed pneumatic actuation and custom control. | 摘要未给出 | 可用于低离散/装配容差触觉界面的结构与对照设计；涉及 in-sensor/物理计算或可编程触觉前端 |
| Fibrous Neuromorphic Electronics: From Single Device to All-Fiber System | This Mini-Review systematically discusses recent advancements in fibrous neuromorphic devices, focusing on underlying physical mechanisms, three-dimensional interface designs, and all-fiber system integration. | 摘要未给出 | 涉及 in-sensor/物理计算或可编程触觉前端；涉及坏点、漂移、跨器件迁移或少样本校准 |
| Analog Synaptic Plasticity in 2D Layered Material Iontronic Memtransistors for Brain‐Inspired Computing | Using tailored input‐output pulse schemes, the device demonstrates key synaptic and cognitive learning functionalities with lower energy consumption per event and faster response speed down to the microsecond regime. | 3 s | 涉及 in-sensor/物理计算或可编程触觉前端 |
| Elastomer‐Assisted Segregation Growth of Large‐Scale Stretchable Organic Crystalline Films for Flexible Photosynapses | Herein, inspired by soil salinization, we developed a segregation strategy to in situ grow large‐area organic single crystals on elastomer substrates via a simple air–water interface drop‐casting method. | 171%、15% | 涉及 in-sensor/物理计算或可编程触觉前端；可用于低离散/装配容差触觉界面的结构与对照设计 |
| A Fully Integrated Wearable Sensor for Real Time Monitoring of Multiple Sweat Liver Disease Biomarkers | In this study, we developed a skin‐conformal, wearable electrochemical biosensing platform capable of real time monitoring of liver health by continuously analyzing liver‐related metabolic biomarkers (creatine and lactat | 摘要未给出 | 提供机器人、可穿戴或电子皮肤系统任务证据 |
| High‐Fidelity Fabrication of 3D Multiscale‐Structured Pressure Sensors for High‐Performance Wearable Sensing | In this work, a high‐precision and controllable fabrication strategy based on a novel secondary replica molding approach is proposed. | 809 kPa、4% | 可用于低离散/装配容差触觉界面的结构与对照设计；提供机器人、可穿戴或电子皮肤系统任务证据 |
| Wearable Sensing Devices for Continuous Animal Health Monitoring | This review presents a system‐level, design‐oriented analysis of animal health monitoring sensing technologies. | 摘要未给出 | 提供机器人、可穿戴或电子皮肤系统任务证据 |
| Shearing‐Assisted Interfacial Exfoliation of Graphene Inks for Embodied Intelligence | Based on this ink, we fabricate screen‑printed multifunctional sensors that exhibit a gauge factor (GF) of 192.2 for strain sensing, together with excellent cyclic stability. | 4 S | 提供机器人、可穿戴或电子皮肤系统任务证据 |
| Tendon‐Inspired Multiscale Bamboo‐Based Ionic Gel for High‐Performance Flexible Energy Conversion | Inspired by tendon hierarchy, we propose a three‐step strategy (delignification, ionic‐liquid induction, and UV‐crosslinking) to reconstruct bamboo across molecular‐nano‐macro scales into a multiscale bamboo ionic gel wi | 100 MPa、48%、1%、1.43 mS、472%、366 V、99.98 µW、99% | 可用于低离散/装配容差触觉界面的结构与对照设计 |
| Flexible and Scalable 2D/3D Tin‐Based Perovskite Photodetectors via Inkjet Printing | ABSTRACT This study investigates the scalable development of lead‐free 2D/3D metal halide perovskites for advanced optoelectronic applications via the precise deployment of inkjet printing. | 50 A、10 V、400 kHz、0.2 A | 可用于低离散/装配容差触觉界面的结构与对照设计；涉及坏点、漂移、跨器件迁移或少样本校准 |
| Energy‐Transfer‐Driven Programmable Luminescence in Bi 3+ ‐Eu 3+ Co‐Doped Na 3 Ca 2 TaO 6 Phosphors Toward Multifunctional Optical Applications | Furthermore, the distinct thermal responses of Bi 3+ and Eu 3+ emission centers give rise to a reliable fluorescence intensity ratio behavior based on non‐thermally coupled luminescence, enabling accurate temperature sen | 摘要未给出 | 涉及 in-sensor/物理计算或可编程触觉前端 |
| Ultrathin Freestanding BiFeO 3 Membranes Grown by Pulsed Laser Deposition | Here we report the design of few‐unit‐cell‐thick ferroelectric membranes using pulsed laser deposition. | 摘要未给出 | 与柔性触觉相关，但尚未显示对前端触觉计算的直接贡献 |

## 今日创新点候选

### Idea 1：把论文系统任务压缩成不拖累主线的最小闭环演示

- 对应轨道：P6；分级：A
- 来源论文：Neuromorphic tactile sensing and haptic display enable fine distributed cutaneous feedback in telepresence
- 核心假设：一个受控的纹理/滑移/抓取演示足以证明前端特征的任务价值，无需把主张扩展成完整机器人系统。
- 最小实验：选择单一任务，固定机械输入和后端分类器，只消融 raw、z-only 与前端矢量/投影特征。
- 对照：raw signal；z-only；front-end vector/projection
- 成功指标：task accuracy；response time；channel count；failure cases
- 用户操作：加入画像提案 / 观察 / 转任务 / 拒绝

### Idea 2：把论文机制映射为 3x3 可编程物理触觉投影核

- 对应轨道：P4；分级：A
- 来源论文：Neuromorphic tactile sensing and haptic display enable fine distributed cutaneous feedback in telepresence
- 核心假设：Ksum/Kx/Ky/Klap/Kring/Kcorner 等可解释投影可在 ADC 前形成，并与软件投影保持一致。
- 最小实验：先用 3x3 精密电阻阵列施加标准图案，再迁移到触觉阵列，比较六类投影核的硬件与软件输出。
- 对照：raw scanning；software projection；fixed hardware kernel；programmable hardware kernel
- 成功指标：hardware-software R2；linearity；kernel switching error；ADC count；latency
- 用户操作：加入画像提案 / 观察 / 转任务 / 拒绝

### Idea 3：把新型矢量/剪切读出转成 ADC 前硬件-软件一致性证据

- 对应轨道：P2；分级：A
- 来源论文：A Bioinspired, Multimodal Soft Tactile Skin with Task‐Adaptive Perception for Intelligent Robotic Manipulation
- 核心假设：ADC 前 Kz/Kx/Ky 类模拟组合应保留任务相关方向信息，并减少后端通道和计算。
- 最小实验：同步记录 raw A/B/C/D、software vector 与 hardware vector，在相同纹理/滑动/剪切输入下做波形、PSD/SNR、R2 和任务消融。
- 对照：raw four-channel；z-only；software vector；hardware vector；reference force
- 成功指标：hardware-software R2；PSD/SNR；task accuracy；latency；ADC channel count
- 用户操作：加入画像提案 / 观察 / 转任务 / 拒绝

## 检索记录

| 来源 | 目标期刊 | 查询 | 命中 | 状态 |
|---|---|---|---:|---|
| arxiv | - | `electronic skin fault tolerant transferable calibration domain adaptation` | 0 | failed |
| crossref | - | `electronic skin fault tolerant transferable calibration domain adaptation` | 25 | ok |
| openalex | - | `electronic skin fault tolerant transferable calibration domain adaptation` | 0 | ok |
| semantic_scholar | - | `electronic skin fault tolerant transferable calibration domain adaptation` | 0 | failed |
| arxiv | - | `electronic skin tactile array compressed readout low channel` | 0 | failed |
| crossref | - | `electronic skin tactile array compressed readout low channel` | 25 | ok |
| openalex | - | `electronic skin tactile array compressed readout low channel` | 0 | ok |
| semantic_scholar | - | `electronic skin tactile array compressed readout low channel` | 0 | ok |
| arxiv | - | `near-sensor analog computing tactile sensing electronic skin` | 0 | failed |
| crossref | - | `near-sensor analog computing tactile sensing electronic skin` | 25 | ok |
| openalex | - | `near-sensor analog computing tactile sensing electronic skin` | 0 | ok |
| semantic_scholar | - | `near-sensor analog computing tactile sensing electronic skin` | 0 | failed |
| crossref | - | `tactile sensor neuromorphic encoding in-sensor computing robotic perception` | 25 | ok |
| openalex | - | `tactile sensor neuromorphic encoding in-sensor computing robotic perception` | 1 | ok |
| semantic_scholar | - | `tactile sensor neuromorphic encoding in-sensor computing robotic perception` | 0 | ok |
| arxiv | - | `tactile sensor physical computing analog computing programmable projection` | 0 | failed |
| crossref | - | `tactile sensor physical computing analog computing programmable projection` | 25 | ok |
| openalex | - | `tactile sensor physical computing analog computing programmable projection` | 0 | ok |
| semantic_scholar | - | `tactile sensor physical computing analog computing programmable projection` | 0 | failed |
| science_official | - | `electronic skin` | 0 | ok |
| science_official | - | `flexible sensor` | 0 | ok |
| science_official | - | `haptic sensor` | 0 | ok |
| science_official | - | `tactile sensor` | 1 | ok |
| arxiv | - | `tactile sensor analog front-end in-sensor computing` | 0 | failed |
| crossref | - | `tactile sensor analog front-end in-sensor computing` | 25 | ok |
| openalex | - | `tactile sensor analog front-end in-sensor computing` | 0 | ok |
| semantic_scholar | - | `tactile sensor analog front-end in-sensor computing` | 0 | failed |
| crossref | - | `flexible tactile sensor assembly tolerance response dispersion electrode microstructure` | 25 | ok |
| openalex | - | `flexible tactile sensor assembly tolerance response dispersion electrode microstructure` | 0 | ok |
| semantic_scholar | - | `flexible tactile sensor assembly tolerance response dispersion electrode microstructure` | 0 | failed |
| crossref | - | `flexible tactile sensor vector shear friction slip direction` | 25 | ok |
| openalex | - | `flexible tactile sensor vector shear friction slip direction` | 0 | ok |
| semantic_scholar | - | `flexible tactile sensor vector shear friction slip direction` | 0 | failed |
| crossref | ACS Nano | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 21 | ok |
| crossref | Advanced Electronic Materials | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 1 | ok |
| crossref | Advanced Energy Materials | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 21 | ok |
| crossref | Advanced Fiber Materials | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 1 | ok |
| crossref | Advanced Functional Materials | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 41 | ok |
| crossref | Advanced Healthcare Materials | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 7 | ok |
| crossref | Advanced Intelligent Systems | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 3 | ok |
| crossref | Advanced Materials | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 65 | ok |
| crossref | Advanced Materials Technologies | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 13 | ok |
| crossref | Advanced Optical Materials | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 30 | ok |
| crossref | Advanced Science | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 76 | ok |
| crossref | Cell Reports Physical Science | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 0 | ok |
| crossref | Communications Chemistry | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 0 | ok |
| crossref | Communications Engineering | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 3 | ok |
| crossref | Communications Materials | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 2 | ok |
| crossref | Communications Physics | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 5 | ok |
| crossref | Device | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 0 | ok |
| crossref | InfoMat | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 0 | ok |
| crossref | International Journal of Extreme Manufacturing | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 5 | ok |
| crossref | Joule | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 0 | ok |
| crossref | Light: Science & Applications | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 8 | ok |
| crossref | Materials Horizons | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 0 | ok |
| crossref | Matter | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 0 | ok |
| crossref | Microsystems & Nanoengineering | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 4 | ok |
| crossref | Nano Energy | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 0 | ok |
| crossref | Nano Letters | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 16 | ok |
| crossref | Nano-Micro Letters | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 1 | ok |
| crossref | National Science Review | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 18 | ok |
| crossref | Nature | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 58 | ok |
| crossref | Nature Biomedical Engineering | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 2 | ok |
| crossref | Nature Communications | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 93 | ok |
| crossref | Nature Electronics | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 5 | ok |
| crossref | Nature Machine Intelligence | `tactile electronic skin neuromorphic sensor computing robotic perception` | 4 | ok |
| crossref | Nature Materials | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 6 | ok |
| crossref | Nature Nanotechnology | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 2 | ok |
| crossref | Nature Sensors | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 2 | ok |
| crossref | npj Flexible Electronics | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 2 | ok |
| crossref | Proceedings of the National Academy of Sciences | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 87 | ok |
| crossref | Research | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 1 | ok |
| crossref | Science | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 0 | ok |
| crossref | Science Advances | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 0 | ok |
| crossref | Science Robotics | `tactile electronic skin flexible sensor haptic robotic perception` | 3 | ok |
| crossref | Science Translational Medicine | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 8 | ok |
| crossref | Small | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 68 | ok |
| crossref | Small Methods | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 10 | ok |

## 数据源异常

- semantic_scholar：6 个查询失败；首个错误为 HTTPError: HTTP Error 429: 。其余来源已继续运行。
- arxiv：5 个查询失败；首个错误为 TimeoutError: The read operation timed out。其余来源已继续运行。

## 纳入与排除标准

- 纳入：达到期刊等级门槛，且属于柔性/可拉伸/可穿戴/皮肤界面电子、柔性器件、软体机器人、自供能或相关传感系统。
- 分类：电子皮肤与触觉、可穿戴健康、柔性材料与器件、柔性能源、软体机器人与 HMI、神经形态/传感计算、制造封装与可靠性、多模态生化传感。
- 强相关：命中阵列读出、矢量/剪切、ADC 前处理、传感计算、校准漂移或跨器件迁移时，额外生成可验证创新建议。
- 降权但保留：只强调 sensitivity、gauge factor 或材料配方，而缺少读出、阵列、校准、鲁棒性或任务证据。
- 排除：历史已收录、题录明显偏题、来源元数据不足且无法核实。
- 可信度边界：本日报首先完成题录/摘要级筛选；数值、机理和优先级需在点击“精读”后核查全文。

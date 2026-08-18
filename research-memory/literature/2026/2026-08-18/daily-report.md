# 2026-08-18 柔性电子高水平文献日报

## 今日结论

本次从 OpenAlex、Crossref、Semantic Scholar、arXiv 和 Science 官网 RSS 检索最近 3 天结果，去重并排除历史已收录论文后保留 15 篇。
期刊等级采用硬门槛：仅保留 Nature/Science 旗舰与子刊、Cell 子刊、Advanced Materials/AFM 及明确同等级期刊；预印本、会议论文和普通期刊不进入正式推荐。
所有柔性电子相关论文均进入分类日报；与 ADC 前模拟触觉、矢量读出、低冗余阵列、物理投影和容错迁移直接相关的论文标为强相关并生成创新建议。

- 今日必看：1 篇
- 值得追踪：12 篇
- 新增可评估 idea：2 个
- 历史重复排除：2 篇
- 期刊等级排除：6 篇
- 小类分布：电子皮肤与触觉 2 篇；柔性能源与自供能 5 篇；制造、封装与可靠性 2 篇；可穿戴健康与生理监测 4 篇；软体机器人与人机交互 1 篇；多模态与生化传感 1 篇

## 今日必看

### 1. [Microstructural Engineering of Flexible Sensors: From Uniaxial to Triaxial Force Detection](https://doi.org/10.1002/smll.75254)

- 来源：Small；2026-08-16；分类：电子皮肤与触觉；评分 70/100
- 为什么重要：涉及 ADC 前模拟矢量、剪切/摩擦/方向相关触觉读出；提供机器人、可穿戴或电子皮肤系统任务证据
- 摘要级结论：涉及 ADC 前模拟矢量、剪切/摩擦/方向相关触觉读出；提供机器人、可穿戴或电子皮肤系统任务证据。当前未从摘要提取到可比较数值。
- 方法：In this Review, microstructural architecture is identified as a primary design variable governing force‐to‐electrical transduction beyond material composition alone.
- 摘要数值：未提取到可比较数值
- 可迁移：涉及 ADC 前模拟矢量、剪切/摩擦/方向相关触觉读出；提供机器人、可穿戴或电子皮肤系统任务证据；优先核查是否有 hardware output 与 software projection 的同步一致性证据
- 给你的创新建议：将法向/剪切/摩擦信息改写为 ADC 前差分或矢量组合，并同步比较 hardware output 与 software vector 的 R2、PSD/SNR。；把论文的跨模态解耦机制迁移为法向/切向通道设计，并分别验证结构解耦、模拟前端解耦和软件解耦的增益。
- 风险：当前为题录/摘要级初筛，论文结论、对照和数值必须在精读全文后核实。；如无完整标定矩阵，不应直接迁移为 full 3D force reconstruction 主张。
- 建议操作：add_to_ideas

## 其他柔性电子相关论文

| 分类 | 评分 | 论文 | 建议 |
|---|---:|---|---|
| 柔性能源与自供能 | 58 | [Bioinspired Fiber‐Based Moisture Electricity Generator Enabled by Bilayer Hydrogel and MOF Nanosheet Arrays for Self‐Powered Sensing](https://doi.org/10.1002/adfm.77753) | skim |
| 柔性能源与自供能 | 49 | [Neuron‐Inspired Orbital‐Interface Engineering of FeS 2 Anodes for Ultrafast and Durable Potassium Storage](https://doi.org/10.1002/adma.74460) | skim |
| 电子皮肤与触觉 | 42 | [Triboelectric Tactile Sensors for Embodied Intelligence: Design, Performances, and Applications](https://doi.org/10.1002/adma.74599) | skim |
| 制造、封装与可靠性 | 41 | [Defect‐Engineered ZnO Nanowire Arrays for Flexible Room‐Temperature Hydrogen Sensors](https://doi.org/10.1002/admt.71246) | skim |
| 可穿戴健康与生理监测 | 40 | [A Wearable Electrochemical Patch for Sustained Local Oxygen Therapy of Chronic Wounds](https://doi.org/10.1002/adma.74636) | skim |
| 可穿戴健康与生理监测 | 40 | [Bio‐Compatible Flexible Memristive Devices Enabled by BNNT/MWCNT–ZnO Quantum Dot Hybrid Percolation Networks](https://doi.org/10.1002/smll.75269) | skim |
| 柔性能源与自供能 | 38 | [Ru‐Doping‐Engineered Oxygen Vacancies in MoO 3‐ x Nanostructured Films With Ultrahigh Capacitance for Flexible Asymmetric Supercapacitors](https://doi.org/10.1002/advs.77131) | skim |
| 可穿戴健康与生理监测 | 37 | [Tough Hydrophobic Ionogel Fibers via Molecularly Engineered Phase Separation for Multi‐Scenario Sensing](https://doi.org/10.1002/adfm.77764) | skim |
| 软体机器人与人机交互 | 36 | [Skeletal‐Muscle‐Inspired Superstrong Dynamic Covalent Liquid‐Crystal Elastomers With Exceptional Actuation Performance](https://doi.org/10.1002/adma.74679) | skim |
| 制造、封装与可靠性 | 36 | [Transparent Deformable Thin Film Electric Heater for Stable and Accurate Control of High Temperatures](https://doi.org/10.1002/adfm.202600071) | skim |
| 柔性能源与自供能 | 35 | [Intrinsic Direct‐Current Generation in an All‐Paper‐Based Triboelectric Nanogenerator via Asymmetric Interfacial Electronic Structure Engineering](https://doi.org/10.1002/smtd.70971) | skim |
| 多模态与生化传感 | 34 | [Bioinspired Hydrogen‐Bond Traps Enabling Ultrasensitive Temperature Sensing](https://doi.org/10.1002/adma.74571) | skim |

## 方法与指标速览

| 论文 | 方法（摘要证据） | 可核实数值 | 画像价值 |
|---|---|---|---|
| Microstructural Engineering of Flexible Sensors: From Uniaxial to Triaxial Force Detection | In this Review, microstructural architecture is identified as a primary design variable governing force‐to‐electrical transduction beyond material composition alone. | 摘要未给出 | 涉及 ADC 前模拟矢量、剪切/摩擦/方向相关触觉读出；提供机器人、可穿戴或电子皮肤系统任务证据 |
| Bioinspired Fiber‐Based Moisture Electricity Generator Enabled by Bilayer Hydrogel and MOF Nanosheet Arrays for Self‐Powered Sensing | However, achieving efficient ion generation, directional transport, and charge separation simultaneously in fibrous architectures remains challenging due to the absence of coordinated structural design. | 0.9 V、82.3 µW | 可用于低离散/装配容差触觉界面的结构与对照设计；涉及 in-sensor/物理计算或可编程触觉前端 |
| Neuron‐Inspired Orbital‐Interface Engineering of FeS 2 Anodes for Ultrafast and Durable Potassium Storage | Herein, a neuron‐inspired orbital‐interface engineering strategy is proposed to construct a hierarchical Co‐FeS 2 /C@C composite via a novel in situ FeS 2 ‐to‐MOF reconstruction, where porous Co‐FeS 2 nanoparticles are i | 268 mA、20 A | 可用于低离散/装配容差触觉界面的结构与对照设计；涉及坏点、漂移、跨器件迁移或少样本校准 |
| Triboelectric Tactile Sensors for Embodied Intelligence: Design, Performances, and Applications | ABSTRACT Embodied intelligence is driving artificial intelligence from digital reasoning toward real physical interaction, while tactile perception capabilities lag behind algorithmic advances and have become a critical  | 摘要未给出 | 与柔性触觉相关，但尚未显示对前端触觉计算的直接贡献 |
| Defect‐Engineered ZnO Nanowire Arrays for Flexible Room‐Temperature Hydrogen Sensors | ABSTRACT We report a scalable fabrication strategy combining photolithographic patterning with chemical bath deposition (CBD) to produce ordered ZnO nanowire arrays on flexible polyimides for room‐temperature hydrogen se | 5 nm、241%、112.9% | 与柔性触觉相关，但尚未显示对前端触觉计算的直接贡献 |
| A Wearable Electrochemical Patch for Sustained Local Oxygen Therapy of Chronic Wounds | This hierarchical design enables an ultralight ( 100 mA cm −2 ), sustaining continuous operation for 735 h to deliver 16.8 L of high‐purity (>99%) O 2 . | 100 mA、99% | 可用于低离散/装配容差触觉界面的结构与对照设计；提供机器人、可穿戴或电子皮肤系统任务证据 |
| Bio‐Compatible Flexible Memristive Devices Enabled by BNNT/MWCNT–ZnO Quantum Dot Hybrid Percolation Networks | Here, we report a flexible and transparent ReRAM device based on a BNNT rod/MWCNT–ZnO quantum dot (QD) nanocomposite and evaluate its electrical operation under static bending, stability after low‐temperature exposure, a | 63%、3 cm、000 s | 涉及坏点、漂移、跨器件迁移或少样本校准；提供机器人、可穿戴或电子皮肤系统任务证据 |
| Ru‐Doping‐Engineered Oxygen Vacancies in MoO 3‐ x Nanostructured Films With Ultrahigh Capacitance for Flexible Asymmetric Supercapacitors | ABSTRACT Molybdenum trioxide (MoO 3 ) is a promising pseudocapacitive material owing to its high theoretical charge‐storage capacity, but its practical application is limited by low electrical conductivity and sluggish i | 1 A、1 V、2.4 V | 可用于低离散/装配容差触觉界面的结构与对照设计；涉及坏点、漂移、跨器件迁移或少样本校准 |
| Tough Hydrophobic Ionogel Fibers via Molecularly Engineered Phase Separation for Multi‐Scenario Sensing | Inspired by the composite architecture of natural biomaterials (e.g., spider silk and human skin), we develop tough hydrophobic ionogel fibers (IGFs) through molecularly engineered polymerization‐induced phase separation | 4.5 MPa、900%、1.325 kPa | 可用于低离散/装配容差触觉界面的结构与对照设计；涉及坏点、漂移、跨器件迁移或少样本校准 |
| Skeletal‐Muscle‐Inspired Superstrong Dynamic Covalent Liquid‐Crystal Elastomers With Exceptional Actuation Performance | Inspired by the critical role of noncovalent interactions in natural skeletal‐muscle actuation, we develop a superstrong DCv‐LCE (SS‐DCv‐LCE) by deliberately engineering a dynamic covalent liquid‐crystal network that sim | 27.6 MPa、30.7 MPa、1.6 MPa | 涉及坏点、漂移、跨器件迁移或少样本校准；提供机器人、可穿戴或电子皮肤系统任务证据 |
| Transparent Deformable Thin Film Electric Heater for Stable and Accurate Control of High Temperatures | However, current transparent heater technologies—based on conductive oxides, carbon‐based materials, and metallic nanowires—suffer from intrinsic limitations such as brittleness, susceptibility to oxidation, high operati | 69%、86% | 提供机器人、可穿戴或电子皮肤系统任务证据 |
| Intrinsic Direct‐Current Generation in an All‐Paper‐Based Triboelectric Nanogenerator via Asymmetric Interfacial Electronic Structure Engineering | Here, we report a fully paper‐based direct‐current triboelectric nanogenerator (DC‐TENG) fabricated through a water‐processable and low‐temperature strategy using biodegradable Xuan paper and environmentally benign funct | 0.32 µW、0.8 mW | 提供机器人、可穿戴或电子皮肤系统任务证据 |
| Bioinspired Hydrogen‐Bond Traps Enabling Ultrasensitive Temperature Sensing | ABSTRACT The development of flexible temperature sensors is hindered by the intrinsically low thermal sensitivity of soft ionic conductors, which arises from averaged energy landscapes and competing transport mechanisms. | 178%、1.0 mm | 与柔性触觉相关，但尚未显示对前端触觉计算的直接贡献 |
| Wearable bioelectronic system with conductive hydrogel for wound management through sensing and electrical stimulation | 当前题录没有摘要，需打开原文核实方法。 | 摘要未给出 | 提供机器人、可穿戴或电子皮肤系统任务证据 |
| Graphene‐Engineered Rear Interfaces Enable Efficient Flexible CZTSSe Solar Cells on Metal Foils | ABSTRACT Flexible kesterite (S,Se) (CZTSSe) solar cells on metal foils are attractive for lightweight and conformable photovoltaic applications, yet their efficiencies remain significantly lower than those of rigid devic | 11.6% | 与柔性触觉相关，但尚未显示对前端触觉计算的直接贡献 |

## 今日创新点候选

### Idea 1：把新型矢量/剪切读出转成 ADC 前硬件-软件一致性证据

- 对应轨道：P2；分级：B
- 来源论文：Microstructural Engineering of Flexible Sensors: From Uniaxial to Triaxial Force Detection
- 核心假设：ADC 前 Kz/Kx/Ky 类模拟组合应保留任务相关方向信息，并减少后端通道和计算。
- 最小实验：同步记录 raw A/B/C/D、software vector 与 hardware vector，在相同纹理/滑动/剪切输入下做波形、PSD/SNR、R2 和任务消融。
- 对照：raw four-channel；z-only；software vector；hardware vector；reference force
- 成功指标：hardware-software R2；PSD/SNR；task accuracy；latency；ADC channel count
- 用户操作：加入画像提案 / 观察 / 转任务 / 拒绝

### Idea 2：把论文系统任务压缩成不拖累主线的最小闭环演示

- 对应轨道：P6；分级：B
- 来源论文：Microstructural Engineering of Flexible Sensors: From Uniaxial to Triaxial Force Detection
- 核心假设：一个受控的纹理/滑移/抓取演示足以证明前端特征的任务价值，无需把主张扩展成完整机器人系统。
- 最小实验：选择单一任务，固定机械输入和后端分类器，只消融 raw、z-only 与前端矢量/投影特征。
- 对照：raw signal；z-only；front-end vector/projection
- 成功指标：task accuracy；response time；channel count；failure cases
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
| openalex | - | `tactile sensor neuromorphic encoding in-sensor computing robotic perception` | 0 | ok |
| semantic_scholar | - | `tactile sensor neuromorphic encoding in-sensor computing robotic perception` | 0 | failed |
| arxiv | - | `tactile sensor physical computing analog computing programmable projection` | 0 | failed |
| crossref | - | `tactile sensor physical computing analog computing programmable projection` | 25 | ok |
| openalex | - | `tactile sensor physical computing analog computing programmable projection` | 0 | ok |
| semantic_scholar | - | `tactile sensor physical computing analog computing programmable projection` | 0 | failed |
| science_official | - | `electronic skin` | 0 | ok |
| science_official | - | `flexible sensor` | 0 | ok |
| science_official | - | `haptic sensor` | 0 | ok |
| science_official | - | `tactile sensor` | 0 | ok |
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
| crossref | ACS Nano | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 9 | ok |
| crossref | Advanced Electronic Materials | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 0 | ok |
| crossref | Advanced Energy Materials | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 11 | ok |
| crossref | Advanced Fiber Materials | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 0 | ok |
| crossref | Advanced Functional Materials | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 37 | ok |
| crossref | Advanced Healthcare Materials | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 10 | ok |
| crossref | Advanced Intelligent Systems | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 1 | ok |
| crossref | Advanced Materials | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 33 | ok |
| crossref | Advanced Materials Technologies | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 9 | ok |
| crossref | Advanced Optical Materials | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 8 | ok |
| crossref | Advanced Science | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 42 | ok |
| crossref | Cell Reports Physical Science | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 0 | ok |
| crossref | Communications Chemistry | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 2 | ok |
| crossref | Communications Engineering | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 2 | ok |
| crossref | Communications Materials | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 2 | ok |
| crossref | Communications Physics | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 6 | ok |
| crossref | Device | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 0 | ok |
| crossref | InfoMat | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 1 | ok |
| crossref | International Journal of Extreme Manufacturing | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 2 | ok |
| crossref | Joule | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 0 | ok |
| crossref | Light: Science & Applications | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 0 | ok |
| crossref | Materials Horizons | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 0 | ok |
| crossref | Matter | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 0 | ok |
| crossref | Microsystems & Nanoengineering | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 4 | ok |
| crossref | Nano Energy | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 0 | ok |
| crossref | Nano Letters | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 8 | ok |
| crossref | Nano-Micro Letters | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 0 | ok |
| crossref | National Science Review | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 8 | ok |
| crossref | Nature | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 9 | ok |
| crossref | Nature Biomedical Engineering | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 2 | ok |
| crossref | Nature Communications | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 79 | ok |
| crossref | Nature Electronics | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 1 | ok |
| crossref | Nature Machine Intelligence | `tactile electronic skin neuromorphic sensor computing robotic perception` | 1 | ok |
| crossref | Nature Materials | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 1 | ok |
| crossref | Nature Nanotechnology | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 2 | ok |
| crossref | Nature Sensors | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 1 | ok |
| crossref | npj Flexible Electronics | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 1 | ok |
| crossref | Proceedings of the National Academy of Sciences | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 42 | ok |
| crossref | Research | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 3 | ok |
| crossref | Science | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 0 | ok |
| crossref | Science Advances | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 0 | ok |
| crossref | Science Robotics | `tactile electronic skin flexible sensor haptic robotic perception` | 0 | ok |
| crossref | Science Translational Medicine | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 0 | ok |
| crossref | Small | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 36 | ok |
| crossref | Small Methods | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 5 | ok |

## 数据源异常

- semantic_scholar：7 个查询失败；首个错误为 HTTPError: HTTP Error 429: 。其余来源已继续运行。
- arxiv：5 个查询失败；首个错误为 HTTPError: HTTP Error 429: Unknown Error。其余来源已继续运行。

## 纳入与排除标准

- 纳入：达到期刊等级门槛，且属于柔性/可拉伸/可穿戴/皮肤界面电子、柔性器件、软体机器人、自供能或相关传感系统。
- 分类：电子皮肤与触觉、可穿戴健康、柔性材料与器件、柔性能源、软体机器人与 HMI、神经形态/传感计算、制造封装与可靠性、多模态生化传感。
- 强相关：命中阵列读出、矢量/剪切、ADC 前处理、传感计算、校准漂移或跨器件迁移时，额外生成可验证创新建议。
- 降权但保留：只强调 sensitivity、gauge factor 或材料配方，而缺少读出、阵列、校准、鲁棒性或任务证据。
- 排除：历史已收录、题录明显偏题、来源元数据不足且无法核实。
- 可信度边界：本日报首先完成题录/摘要级筛选；数值、机理和优先级需在点击“精读”后核查全文。

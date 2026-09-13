# 2026-09-13 柔性电子高水平文献日报

## 今日结论

本次从 OpenAlex、Crossref、Semantic Scholar、arXiv 和 Science 官网 RSS 检索最近 3 天结果，去重并排除历史已收录论文后保留 9 篇。
期刊等级采用硬门槛：仅保留 Nature/Science 旗舰与子刊、Cell 子刊、Advanced Materials/AFM 及明确同等级期刊；预印本、会议论文和普通期刊不进入正式推荐。
所有柔性电子相关论文均进入分类日报；与 ADC 前模拟触觉、矢量读出、低冗余阵列、物理投影和容错迁移直接相关的论文标为强相关并生成创新建议。

- 今日必看：2 篇
- 值得追踪：7 篇
- 新增可评估 idea：2 个
- 历史重复排除：19 篇
- 期刊等级排除：5 篇
- 小类分布：电子皮肤与触觉 1 篇；可穿戴健康与生理监测 4 篇；柔性材料与器件 1 篇；柔性能源与自供能 2 篇；多模态与生化传感 1 篇

## 今日必看

### 1. [Decoupled Temperature‐Pressure Sensing via Hierarchical Porous Sponge for Thermo‐Tactile Perception](https://doi.org/10.1002/adfm.78367)

- 来源：Advanced Functional Materials；2026-09-12；分类：电子皮肤与触觉；评分 64/100
- 为什么重要：涉及低冗余阵列、空间特征或读出通道压缩；涉及坏点、漂移、跨器件迁移或少样本校准
- 摘要级结论：待基于原文摘要生成中文总结；当前仅完成题录/摘要级筛选。
- 方法：Herein, we present a flexible, high‐fidelity dual‐modal sensor based on an ultralight hierarchically porous conductive sponge.
- 摘要数值：4.43 kPa、25 Pa、91 ms
- 可迁移：涉及低冗余阵列、空间特征或读出通道压缩；涉及坏点、漂移、跨器件迁移或少样本校准；可对照 raw pixel、software feature 与 physical projection 的性能/通道/功耗
- 给你的创新建议：把论文的跨模态解耦机制迁移为法向/切向通道设计，并分别验证结构解耦、模拟前端解耦和软件解耦的增益。
- 风险：当前为题录/摘要级初筛，论文结论、对照和数值必须在精读全文后核实。；开放获取 PDF 下载失败：RuntimeError: https://advanced.onlinelibrary.wiley.com/doi/pdf/10.1002/adfm.78367。
- 建议操作：skim

### 2. [Programmable Crack Networks for Wide‐Range and Reversible Strain Sensing in Vertically Oriented van der Waals Molybdenum Disulfide Thin Films](https://doi.org/10.1002/admt.71310)

- 来源：Advanced Materials Technologies；2026-09-12；分类：柔性材料与器件；评分 48/100
- 为什么重要：涉及坏点、漂移、跨器件迁移或少样本校准；可用于低离散/装配容差触觉界面的结构与对照设计
- 摘要级结论：待基于原文摘要生成中文总结；当前仅完成题录/摘要级筛选。
- 方法：This study presents a mechanically programmable crack network‐based strategy for achieving wide‐range and reversible strain sensing with vertically aligned van der Waals (vdW) polycrystalline molybdenum disulfide (MoS 2 ) thin films deposited onto flexible polyimide (PI) substrates.
- 摘要数值：未提取到可比较数值
- 可迁移：涉及坏点、漂移、跨器件迁移或少样本校准；可用于低离散/装配容差触觉界面的结构与对照设计；可对照 raw pixel、software feature 与 physical projection 的性能/通道/功耗
- 给你的创新建议：加入坏点比例、增益漂移和跨器件迁移实验，比较重标定样本量与性能渐进退化，形成可靠性主张。
- 风险：当前为题录/摘要级初筛，论文结论、对照和数值必须在精读全文后核实。；开放获取 PDF 下载失败：RuntimeError: https://advanced.onlinelibrary.wiley.com/doi/pdf/10.1002/admt.71310。
- 建议操作：skim

## 其他柔性电子相关论文

| 分类 | 评分 | 论文 | 建议 |
|---|---:|---|---|
| 可穿戴健康与生理监测 | 48 | [Wearable Electrochemical Sweat Sensors Beyond Snapshots With Long‐Term Stability](https://doi.org/10.1002/adfm.78410) | skim |
| 可穿戴健康与生理监测 | 44 | [Systematic Parameter‐Space Mapping Strategy for a Deep‐Subwavelength‐Thick Low‐Frequency Electromagnetic Metasurface Absorber](https://doi.org/10.1002/adom.71799) | skim |
| 可穿戴健康与生理监测 | 42 | [Synergistic Mechano-Electric Coupling Enables Contraction-Guided Wound Healing](https://doi.org/10.1021/acsnano.6c10614) | skim |
| 柔性能源与自供能 | 30 | [Buried Ultrathin Perovskite Layer Seeding Homogeneous Crystallization Toward Efficient Flexible Perovskite Solar Cells](https://doi.org/10.1002/adfm.78413) | skim |
| 可穿戴健康与生理监测 | 26 | [Stabilisation of Liquid Metal With a Short Peptide to Prepare Adhesive Piezoresistive Stretchable Hydrogel for Advanced Applications](https://doi.org/10.1002/smll.75763) | ignore |
| 柔性能源与自供能 | 25 | [Advances in Electrospun Stimuli‐Responsive Smart Fibers: A Review](https://doi.org/10.1002/adfm.78377) | ignore |
| 多模态与生化传感 | 22 | [One‐Step Pyrolysis and ZnO Nanostructure Functionalization of Flexible Textiles for Multimodal Sensing of Pressure, Temperature and Sunlight](https://doi.org/10.1002/admt.71316) | ignore |

## 方法与指标速览

| 论文 | 方法（摘要证据） | 可核实数值 | 画像价值 |
|---|---|---|---|
| Decoupled Temperature‐Pressure Sensing via Hierarchical Porous Sponge for Thermo‐Tactile Perception | Herein, we present a flexible, high‐fidelity dual‐modal sensor based on an ultralight hierarchically porous conductive sponge. | 4.43 kPa、25 Pa、91 ms | 涉及低冗余阵列、空间特征或读出通道压缩；涉及坏点、漂移、跨器件迁移或少样本校准 |
| Wearable Electrochemical Sweat Sensors Beyond Snapshots With Long‐Term Stability | ABSTRACT Wearable sweat electrochemical sensors enable continuous and noninvasive monitoring of electrolytes, metabolites, and stress‐related biomarkers for personalized healthcare. | 摘要未给出 | 涉及坏点、漂移、跨器件迁移或少样本校准；提供机器人、可穿戴或电子皮肤系统任务证据 |
| Programmable Crack Networks for Wide‐Range and Reversible Strain Sensing in Vertically Oriented van der Waals Molybdenum Disulfide Thin Films | This study presents a mechanically programmable crack network‐based strategy for achieving wide‐range and reversible strain sensing with vertically aligned van der Waals (vdW) polycrystalline molybdenum disulfide (MoS 2  | 摘要未给出 | 涉及坏点、漂移、跨器件迁移或少样本校准；可用于低离散/装配容差触觉界面的结构与对照设计 |
| Systematic Parameter‐Space Mapping Strategy for a Deep‐Subwavelength‐Thick Low‐Frequency Electromagnetic Metasurface Absorber | ABSTRACT Overcoming the intrinsic thickness–frequency trade‐off while simultaneously ensuring ultra‐thinness, wide‐angle absorption, and mechanical conformability remains a fundamental challenge in designing electromagne | 0.908 mm、98.7%、95%、20 cm | 涉及坏点、漂移、跨器件迁移或少样本校准；提供机器人、可穿戴或电子皮肤系统任务证据 |
| Synergistic Mechano-Electric Coupling Enables Contraction-Guided Wound Healing | Abstract Physical therapies for wound management are attractive because of comfort and noninvasiveness. | 5.5 kPa、100 mV | 可用于低离散/装配容差触觉界面的结构与对照设计；涉及坏点、漂移、跨器件迁移或少样本校准 |
| Buried Ultrathin Perovskite Layer Seeding Homogeneous Crystallization Toward Efficient Flexible Perovskite Solar Cells | Herein, we propose an interfacial seeding strategy that introduces an ultrathin perovskite layer into the SAM layer prior to the deposition of perovskite films. | 25.18% | 可用于低离散/装配容差触觉界面的结构与对照设计 |
| Stabilisation of Liquid Metal With a Short Peptide to Prepare Adhesive Piezoresistive Stretchable Hydrogel for Advanced Applications | ABSTRACT Liquid metals (LMs) are promising materials for flexible electronics because of their high electrical conductivity, fluidity, and biocompatibility. | 250%、160% | 可用于低离散/装配容差触觉界面的结构与对照设计；提供机器人、可穿戴或电子皮肤系统任务证据 |
| Advances in Electrospun Stimuli‐Responsive Smart Fibers: A Review | This review systematically summarizes the fundamentals, structural design strategies, fabrication technologies, and applications of electrospun stimuli‐responsive smart fibers. | 摘要未给出 | 材料性能词较多、前端/阵列/系统证据偏少，已降权 |
| One‐Step Pyrolysis and ZnO Nanostructure Functionalization of Flexible Textiles for Multimodal Sensing of Pressure, Temperature and Sunlight | These findings establish laser irradiation of ZnSO 4 ‐treated textiles as an initial proof‐of‐concept toward developing wearable multimodal sensors with little crosstalk, while further evaluation of wearability‐related c | 10% | 提供机器人、可穿戴或电子皮肤系统任务证据；材料性能词较多、前端/阵列/系统证据偏少，已降权 |

## 今日创新点候选

### Idea 1：把论文的阵列读出策略改写为低冗余 hardware macro-pixel 对照

- 对应轨道：P3；分级：B
- 来源论文：Decoupled Temperature‐Pressure Sensing via Hierarchical Porous Sponge for Thermo‐Tactile Perception
- 核心假设：可解释的局部矢量/空间投影能以更少读出通道保持边缘、形状和滑移方向信息。
- 最小实验：在同一阵列输入上比较 raw scanning、scalar pooling、software gradient 与 hardware macro-pixel。
- 对照：raw pixel scanning；scalar pooling；software gradient；hardware macro-pixel
- 成功指标：channel count；latency；power；edge/shape accuracy；direction accuracy
- 用户操作：加入画像提案 / 观察 / 转任务 / 拒绝

### Idea 2：把论文的鲁棒/迁移策略加入物理投影坏点渐进退化实验

- 对应轨道：P5；分级：B
- 来源论文：Decoupled Temperature‐Pressure Sensing via Hierarchical Porous Sponge for Thermo‐Tactile Perception
- 核心假设：归一化物理投影特征在坏点、漂移和跨器件变化下应比 raw readout 更平滑退化，并减少重标定样本。
- 最小实验：设置 0/1/5/10/20% 等效坏点与增益漂移，比较 raw、software projection、hardware projection 及少样本校准。
- 对照：raw readout；software projection；hardware projection；hardware projection + few-shot calibration
- 成功指标：accuracy degradation；feature drift；calibration samples；fault ratio；cross-device variance
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
| semantic_scholar | - | `electronic skin tactile array compressed readout low channel` | 0 | failed |
| arxiv | - | `near-sensor analog computing tactile sensing electronic skin` | 0 | failed |
| crossref | - | `near-sensor analog computing tactile sensing electronic skin` | 25 | ok |
| openalex | - | `near-sensor analog computing tactile sensing electronic skin` | 0 | ok |
| semantic_scholar | - | `near-sensor analog computing tactile sensing electronic skin` | 0 | ok |
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
| crossref | ACS Nano | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 7 | ok |
| crossref | Advanced Electronic Materials | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 1 | ok |
| crossref | Advanced Energy Materials | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 15 | ok |
| crossref | Advanced Fiber Materials | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 1 | ok |
| crossref | Advanced Functional Materials | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 88 | ok |
| crossref | Advanced Healthcare Materials | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 5 | ok |
| crossref | Advanced Intelligent Systems | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 4 | ok |
| crossref | Advanced Materials | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 36 | ok |
| crossref | Advanced Materials Technologies | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 11 | ok |
| crossref | Advanced Optical Materials | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 31 | ok |
| crossref | Advanced Science | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 35 | ok |
| crossref | Cell Reports Physical Science | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 0 | ok |
| crossref | Communications Chemistry | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 6 | ok |
| crossref | Communications Engineering | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 1 | ok |
| crossref | Communications Materials | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 6 | ok |
| crossref | Communications Physics | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 6 | ok |
| crossref | Device | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 0 | ok |
| crossref | InfoMat | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 0 | ok |
| crossref | International Journal of Extreme Manufacturing | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 6 | ok |
| crossref | Joule | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 0 | ok |
| crossref | Light: Science & Applications | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 0 | ok |
| crossref | Materials Horizons | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 0 | ok |
| crossref | Matter | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 0 | ok |
| crossref | Microsystems & Nanoengineering | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 1 | ok |
| crossref | Nano Energy | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 0 | ok |
| crossref | Nano Letters | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 12 | ok |
| crossref | Nano-Micro Letters | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 1 | ok |
| crossref | National Science Review | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 9 | ok |
| crossref | Nature | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 12 | ok |
| crossref | Nature Biomedical Engineering | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 3 | ok |
| crossref | Nature Communications | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 98 | ok |
| crossref | Nature Electronics | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 3 | ok |
| crossref | Nature Machine Intelligence | `tactile electronic skin neuromorphic sensor computing robotic perception` | 1 | ok |
| crossref | Nature Materials | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 2 | ok |
| crossref | Nature Nanotechnology | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 1 | ok |
| crossref | Nature Sensors | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 0 | ok |
| crossref | npj Flexible Electronics | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 1 | ok |
| crossref | Proceedings of the National Academy of Sciences | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 22 | ok |
| crossref | Research | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 3 | ok |
| crossref | Science | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 40 | ok |
| crossref | Science Advances | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 85 | ok |
| crossref | Science Robotics | `tactile electronic skin flexible sensor haptic robotic perception` | 0 | ok |
| crossref | Science Translational Medicine | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 0 | ok |
| crossref | Small | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 57 | ok |
| crossref | Small Methods | `flexible tactile electronic skin wearable pressure force strain haptic neuromorphic sensor array readout robotic perception` | 5 | ok |

## 数据源异常

- semantic_scholar：7 个查询失败；首个错误为 HTTPError: HTTP Error 429: 。其余来源已继续运行。
- arxiv：5 个查询失败；首个错误为 HTTPError: HTTP Error 429: Too Many Requests。其余来源已继续运行。

## 纳入与排除标准

- 纳入：达到期刊等级门槛，且属于柔性/可拉伸/可穿戴/皮肤界面电子、柔性器件、软体机器人、自供能或相关传感系统。
- 分类：电子皮肤与触觉、可穿戴健康、柔性材料与器件、柔性能源、软体机器人与 HMI、神经形态/传感计算、制造封装与可靠性、多模态生化传感。
- 强相关：命中阵列读出、矢量/剪切、ADC 前处理、传感计算、校准漂移或跨器件迁移时，额外生成可验证创新建议。
- 降权但保留：只强调 sensitivity、gauge factor 或材料配方，而缺少读出、阵列、校准、鲁棒性或任务证据。
- 排除：历史已收录、题录明显偏题、来源元数据不足且无法核实。
- 可信度边界：本日报首先完成题录/摘要级筛选；数值、机理和优先级需在点击“精读”后核查全文。

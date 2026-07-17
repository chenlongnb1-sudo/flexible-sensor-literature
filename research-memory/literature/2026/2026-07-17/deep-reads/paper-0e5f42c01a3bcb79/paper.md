# A spike–language dual framework bridges fast perception and deep reasoning in artificial tactile somatosensory systems

- 期刊：Nature Sensors
- 日期：2026-07-15
- DOI：10.1038/s44460-026-00108-1
- 解析状态：metadata_only_no_legal_pdf

## 摘要与研究价值

**Original:** The human somatosensory system achieves both rapid tactile perception and high-level cognitive reasoning through a hierarchical architecture, yet robotic tactile systems still lack the integration between multimodal sensory hardware and semantic computing frameworks, leaving a gap between fast perception and deep cognition. Here we present a spike–language dual encoding strategy for embodied somatosensory systems, implemented on a robotic skin-like sensor array that mimics human mechanoreceptors and thermoreceptors. Tactile time-series data are simultaneously encoded into spikes for a spiking neural network, enabling fast object classification, and into natural language prompts for a large language model, supporting semantic reasoning. A confidence-based gating mechanism adaptively routes sensory data, ensuring reflexive responses for routine tasks while reserving computationally intensive reasoning for open-set recognition—an underexplored capability in tactile systems. This dual-pathway framework provides a foundation for human-like somatosensation and advancing the development of autonomous, cognitively capable robots.

**中文:** 该研究在机器人皮肤式多模态传感阵列上提出脉冲—语言双编码框架：同一触觉时序一方面转换为脉冲供 SNN 快速分类，另一方面转换为自然语言提示供大模型进行开放集语义推理，并通过置信度门控在快速反射与深度推理之间自适应路由。

## 创新点

- A spike-language dual encoding strategy combines fast SNN classification with LLM-based semantic reasoning on tactile time-series data from a robotic skin-like sensor array.
- 使用仿生机械感受器和温度感受器的皮肤式传感阵列
- 同一触觉时序同时编码为脉冲和自然语言，形成快感知与深推理双通路
- 可作为硬件投影前端与分层事件编码/语义路由的系统级对照

## 对当前课题的启发

- 将 P4 的硬件投影输出进一步组织为事件脉冲与语义特征两条可切换通路
- 用置信度门控决定简单任务走低延迟路径、未知触觉走高成本推理路径
- 可设计 hardware projection、raw array、SNN-only 与双通路方案的延迟和开放集识别对照

## 制备与实验步骤

## 方法原文锚点

## 图表解读

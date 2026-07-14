# 2026-07-14 柔性电子皮肤前端触觉计算文献日报

## 今日结论

本次检索最近 30 天文献。人工硬门控后仅保留 1 篇直接 sensor-to-chip 神经形态触觉系统。PFL 协作机器人计量综述、飞秒激光高灵敏压力传感器、视觉触觉 CNN、摩擦电穿戴综述，以及上一轮出现的工具轨迹重建、sim-to-real 强化学习和金属超声波导均因缺少用户 P1-P6 所需的前端/阵列证据被移除。没有用弱匹配或通用高灵敏材料论文填充日报。

- 今日必看：1 篇
- 值得追踪：0 篇
- 新增候选 idea：1 个
- 用户研究画像：未修改

## 今日必看

### 1. [GelNeuro: A Sensing-Computing Integrated Neuromorphic Tactile System for Texture Recognition](https://arxiv.org/abs/2607.05241)

- 对应 P4/P6：直接把 GelSight Mini 的 DVS 事件送入 Speck2f 上的 INT8 SCNN，活动推理不依赖主机预处理，可作为前端计算路径和最小任务演示的系统基线。
- 方法：1 ms 事件分箱；硬件感知权重裁剪；INT8 量化；映射到 9 个物理处理核；15 类天然纹理硬件在环验证。
- 指标：96.3%（芯片）对 99.0%（PC）；80 ms；19.6 mW 板级活动功耗。全文对照 GelSight handcrafted/PC、Evetac、NeuroTac/Loihi2、NeuroTac/Speck2f 以及 CPU/GPU 功耗。
- 局限：光学事件触觉并非压阻阵列 ADC 前模拟计算；1 ms 时间离散受 BPTT 内存约束；INT8 映射仍有精度损失；芯片串扰和热噪声未被离线噪声完全覆盖；滑移闭环尚未验证。
- 可迁移：对 Paper A/P4 建立 raw/host software/hardware vector/physical projection 的 accuracy-latency-power-channel 联合消融。未见深度泛化只能作为工况鲁棒性参考，不能写成跨器件迁移或坏点容错。

## 今日创新点候选

`candidate`，P4/P6：建立 raw acquisition、host software feature、hardware vector、programmable hardware projection 的联合消融。成功指标包括任务精度、ADC/通道数、端到端延迟、前端功耗与 hardware-software R2。该想法未写入用户画像。

## 数据源异常

- Semantic Scholar：6 个查询失败，HTTP 429。
- arXiv：4 个查询超时；其他 arXiv 查询及已有题录仍可用。
- OpenAlex、Crossref：本次最新并发运行正常返回；最终保留论文来自 arXiv，并已用合法下载全文核验。

## 纳入与排除标准

- 纳入：能服务 P1-P6，且提供前端、阵列、系统路径、资源权衡或可验证任务证据。
- 排除：仅关键词命中；通用高灵敏材料；纯后端机器人算法；与柔性电子皮肤前端无关的刚性或计量平台。
- 证据边界：保留论文已核对下载全文；新 idea 仅为 `candidate`，未修改 `user-research-profile.md`。

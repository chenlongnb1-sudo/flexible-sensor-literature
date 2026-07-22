# Paper A: dual-path pre-ADC tactile slip reflex

本目录归档 Codex 任务 `019f5f9e-ab04-7b43-b8e2-3b8a486282d5` 中形成的论文逻辑、实验决策和核心生成文件。归档日期为 2026-07-22；目录组织参考任务 `019f2060-44ed-7f63-91d9-151c452340cc` 的研究记忆工作流。

## 当前论文身份

论文主线采用“双时间尺度、ADC 前触觉计算”：慢通路数字化 `Vz/Vx/Vy` 并识别表面类别；快通路在量化前计算纹理条件化的滑移裕量，输出有界增握事件。A1-A4 不取代这条主线，而是作为公平的架构评测框架。

## 目录内容

- `conversation.md`：当前任务的时间顺序对话纪要。
- `decision-log.md`：已锁定的论文、硬件、控制与实验边界。
- `artifacts/fig5-redesign-svg-panels/`：Fig. 5 六个独立可编辑 SVG 面板、预览、生成脚本和 QA。
- `artifacts/fig6/`：Fig. 6 可编辑 PPTX、PDF、预览、实验规划图、图注、实验协议和缺口清单。
- `hardware/grasp-event-frontend/`：与双通路、MCU 分工和 A1-A4 功耗验证直接相关的四份更新文档。
- `research-memory/`：由 `research-memory-sync` 生成的会话入口和文件映射。

## 证据边界

- Fig. 5 数据区保持 `[TO BE MEASURED]`，没有合成实验曲线、样本量或性能数字。
- Fig. 6 是“证据占位主图 + 实验规划图”，不是完成后的实验结果。
- `OVERLOAD_N` 硬件旁路、ADC/reference 休眠、功耗优势和闭环防滑效果仍需实测。
- 本次归档没有上传原始实验数据、用户提供的源 PPT/OPJU、源幻灯片拆图、缓存、调试文件或旧版重复图稿。
- 目标 GitHub 仓库为公开仓库；Fig. 6 中保留的是用户明确要求归档的生成图稿，其中可能包含论文尚未发表的设备图像。

## 使用顺序

1. 先读 `decision-log.md`，确认当前论文表述和禁止越界的主张。
2. 用 Fig. 5 协议完成连续比例扫描、冻结阈值和独立事件验证。
3. 用 Fig. 6 协议完成同一时钟下的抓取、事件、动作、能量和 A1-A4 对照。
4. 只有在独立力标定完成后，才可把 `lambda` 解释为真实摩擦系数；此前统一称为 `texture-conditioned slip-margin coefficient`。

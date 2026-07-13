# 个人科研情报与论文画像系统方案

更新日期：2026-07-14

## 1. 系统定位

这个系统不是普通文献订阅器，也不是只做论文摘要的工具。它应该被设计成用户的 **个人科研情报中枢**：

1. 读取并持续理解用户本地科研资料、论文草稿、组会 PPT、实验数据目录、项目申请书和已有研究画像。
2. 每天筛选与用户真实课题高度相关的新论文。
3. 将论文创新点拆解为“可迁移机制”“可补实验”“可对照 baseline”“可写作表述”“风险与边界”。
4. 生成每日推送，用户可以在网页或微信小程序里快速判断：精读、忽略、加入画像、加入 idea 池、转成实验任务。
5. 经过用户确认后，系统才更新论文画像、idea log、实验计划和写作素材库。

一句话：

> 让 Agent 每天替用户读新文献，但最终由用户决定哪些外部创新真正进入自己的论文路线。

## 2. 用户当前科研主线

根据 `E:\BaiduSyncdisk\博` 和当前 `research-memory/profile/user-research-profile.md`，用户主线应被理解为：

- 柔性电子皮肤前端触觉计算。
- 低离散/容差触觉界面。
- ADC 前模拟矢量触觉读出。
- 低冗余矢量触觉阵列。
- 可编程物理触觉投影前端。
- 容错、可迁移、少样本校准的电子皮肤。
- 面向摩擦、纹理、滑移、剪切/方向相关线索、机械臂触觉、鞋垫和空间人体监测的柔性传感系统。

系统不能把用户方向降级成“柔性压力传感器材料性能提升”。每日筛文献必须围绕“结构-传感器-模拟前端-阵列-系统任务”的组合价值。

## 3. 核心对象

### 3.1 论文画像

论文画像是系统的主记忆，描述用户正在做什么、不能乱写什么、缺什么证据、需要什么论文启发。

画像包括：

- 研究身份：例如 front-end tactile computing for soft electronic skins。
- 论文方向：P1/P2/P3/P4/P5/P6。
- 已有证据：数据、图组、实验、材料、器件结构。
- 缺口：硬件 Kz/Kx/Ky、方向标定、PSD/SNR、容差实验、阵列指标等。
- 禁止夸大：不能写 full 3D force sensor、不能只讲 high sensitivity。
- 文献筛选优先级。
- idea 池和已采纳 idea。

### 3.2 文献卡片

每篇论文进入系统后，不只是标题和摘要，而是生成结构化卡片：

- title、authors、venue、date、DOI/link。
- 论文类型：材料、结构、器件、电路、阵列、算法、系统、应用。
- 传感对象：pressure、strain、shear、friction、slip、texture、bio-signal 等。
- 核心创新：机制创新、结构创新、读出创新、系统创新。
- 与用户画像匹配点。
- 可迁移到用户工作的点。
- 不能迁移或风险。
- 建议动作：忽略、略读、精读、加入 idea 池、加入画像、转实验任务。
- 可信度评分和相关度评分。

### 3.3 创新点候选

系统每天从论文中抽取创新点，但先进入候选池：

- `candidate`：未处理。
- `watch`：值得关注，但暂不写入画像。
- `accepted`：用户确认加入画像。
- `rejected`：不适合或已被否决。
- `converted_to_task`：转为实验/写作任务。

每个创新点都要有来源论文和原因，避免以后找不到出处。

### 3.4 实验/写作任务

用户确认后的 idea 可以进一步转成：

- 补实验任务：例如四方向滑动标定、hardware vs software projection R2、坏点模拟实验。
- 图表任务：例如 baseline 对照图、机制示意图、性能对比表。
- 写作素材：例如 Introduction 缺口、Related Work 分类、Discussion 边界表述。
- 审稿风险：例如 claim 过强、缺少对照、缺少统计显著性。

## 4. 每日 Agent 工作流

### 4.1 输入

每天 9:00 自动任务读取：

- `research-memory/profile/user-research-profile.md`
- `research-memory/ideas/idea-log.md`
- 最近 7-30 天文献报告
- 用户标记为 accepted/rejected/watch 的历史记录
- 可选：本地 `E:\BaiduSyncdisk\博` 的文件索引摘要

### 4.2 搜索

搜索不应只用单一关键词，而应分层：

一级主线：

- flexible electronic skin
- soft electronic skin
- tactile sensor
- flexible tactile sensor
- wearable tactile sensing

二级机制：

- analog tactile preprocessing
- in-sensor computing
- sensor-near computing
- pre-ADC tactile
- tactile front-end
- vector tactile sensing
- shear/friction/slip tactile sensing

三级用户特定方向：

- low-redundancy tactile array
- programmable tactile projection
- fault-tolerant tactile sensing
- transferable tactile sensing
- cross-sensor calibration
- macro-pixel tactile array
- interdigitated electrode microstructure
- assembly tolerance tactile interface

### 4.3 初筛

每篇论文打分：

- 相关度：是否服务用户 P1-P6 主线。
- 创新密度：是不是新机制/新结构/新前端/新阵列。
- 可迁移性：能否转化为用户已有平台上的实验。
- 证据强度：是否有对照、统计、阵列、系统任务。
- 风险：是否只是材料堆性能，或与用户主线不搭。

建议阈值：

- `score >= 85`：精读并推送顶部。
- `70 <= score < 85`：进入候选。
- `50 <= score < 70`：只记录标题和理由。
- `< 50`：忽略，除非是顶刊综述或方向突变。

### 4.4 深读与总结

对高分论文生成：

- 一句话结论。
- 论文真正创新点。
- 对用户 P1/P2/P3/P4/P5/P6 哪条线有用。
- 能直接借鉴的实验。
- 能构成对照的 baseline。
- 可写进 Introduction 的 gap。
- 可写进 Discussion 的边界。
- 与用户现有方案相比强在哪里、弱在哪里。
- 是否建议加入画像。

### 4.5 推送

每日推送不应太长，分成三层：

1. 今日必看：1-3 篇。
2. 值得追踪：3-8 篇。
3. 今日 idea：3-5 个，可一键处理。

推送示例：

```text
今日最相关：3 篇

1. 论文 A
   为什么重要：它把 tactile feature formation 前移到模拟前端。
   对你有用：可作为 P4 programmable projection 的 related work/baseline。
   建议：精读；加入 P4 画像候选。

今日 idea：
Idea 1：把 hardware projection 加入坏点模拟实验，比较 raw vs normalized projection 的性能退化曲线。
操作：加入 idea 池 / 加入画像 / 转实验任务 / 忽略
```

## 5. 网页或微信小程序形态

### 5.1 网页版

优点：

- 开发最快。
- 适合展示论文卡片、文献库、画像编辑器、图表和 Markdown 报告。
- 可以直接部署在 GitHub Pages、Vercel、本地服务器或实验室电脑。
- 后台 Agent 和 GitHub 仓库集成更简单。

推荐作为第一阶段 MVP。

核心页面：

- Dashboard：今日摘要、待处理 idea、最近文献趋势。
- Papers：文献卡片列表、筛选、搜索、评分。
- Ideas：候选创新点池，支持 accepted/watch/rejected。
- Profile：论文画像编辑与版本历史。
- Reports：每日文献报告归档。
- Tasks：从 idea 转成的实验/写作任务。

### 5.2 微信小程序

优点：

- 适合每天早上推送和碎片时间处理。
- 操作轻：点一下“加入画像”“稍后精读”“忽略”。
- 适合手机端查看今日摘要。

限制：

- 需要小程序账号、后端服务和订阅消息配置。
- 微信订阅消息通常需要用户授权，不能无限制主动骚扰式推送。
- 复杂 Markdown、PDF 阅读和长文编辑体验不如网页。

建议定位：

- 微信小程序做“每日收件箱”和轻量决策。
- 网页做“深度阅读、画像编辑、报告归档、系统配置”。

## 6. 推荐技术架构

### 6.1 最小可用版本

```text
Codex 自动任务
  -> 搜索/总结论文
  -> 写入 GitHub 仓库 Markdown/JSON
  -> 网页读取 JSON/Markdown 展示
  -> 用户在网页里标记 idea 状态
  -> 生成 profile update proposal
  -> 用户确认后合并到画像
```

第一版可以不做数据库，直接用 GitHub 仓库作为数据库：

```text
research-memory/
  profile/user-research-profile.md
  literature/YYYY/YYYY-MM-DD/daily-report.md
  literature/YYYY/YYYY-MM-DD/summaries/papers.json
  ideas/idea-log.json
  decisions/decision-log.json
  tasks/task-board.json
```

### 6.2 完整版本

```text
文献源
  -> 搜索 Agent
  -> 解析 Agent
  -> 相关度评分 Agent
  -> 创新点抽取 Agent
  -> 用户决策层
  -> 画像更新 Agent
  -> GitHub 记忆库
  -> Web / 小程序 / 推送
```

可选后端：

- Node.js/Next.js：适合网页和 API。
- Python/FastAPI：适合文献处理、PDF 解析、embedding、学术搜索脚本。
- SQLite/Postgres：当 JSON 文件不够用时再加。
- GitHub Actions 或 Codex cron：负责每天定时。

建议先做：

- GitHub 仓库 + Codex 自动任务 + 静态/轻后端网页。

后续再做：

- 小程序 + 云函数/后端推送。

## 7. 人机确认机制

这是系统最重要的设计。

Agent 不能直接改画像，只能生成 `profile_update_proposal`：

```json
{
  "date": "2026-07-14",
  "source": "daily literature report",
  "proposal": "将 fault-tolerant programmable projection 加入 P4/P5 交叉方向",
  "evidence": ["paper doi/link", "daily report path"],
  "risk": "目前缺少真实 3x3 阵列坏点实验",
  "status": "pending"
}
```

用户可选：

- 接受：写入画像。
- 暂存：进入 watch。
- 拒绝：记录拒绝理由，避免反复推荐。
- 转任务：生成实验/写作任务。

## 8. 创新点生成逻辑

系统每天不只是“想点子”，而是用矩阵生成可验证 idea。

### 8.1 交叉矩阵

把新论文创新放入矩阵：

```text
新论文机制 x 用户已有平台 x 用户缺口 x 可验证指标
```

例子：

```text
论文：坏点鲁棒触觉阵列
用户平台：3x3 programmable physical projection
用户缺口：P4/P5 需要容错与迁移证据
指标：fault ratio, graceful degradation, few-shot calibration
idea：用 projection kernel 在 0/1/5/10/20% 坏点条件下比较 raw vs normalized projection 的退化曲线。
```

### 8.2 idea 分级

- A 级：可直接进入论文主线，有明确实验和指标。
- B 级：适合做补充实验或 discussion。
- C 级：有启发但短期不做。
- D 级：好看但偏题，拒绝。

### 8.3 idea 输出格式

每个 idea 必须包含：

- 名称。
- 对应用户方向：P1/P2/P3/P4/P5/P6。
- 来源论文。
- 核心假设。
- 最小实验。
- 对照组。
- 成功指标。
- 失败降级路线。
- 是否建议加入画像。

## 9. 隐私和安全

本地 `E:\BaiduSyncdisk\博` 包含论文草稿、项目申请、审稿、报销、数据、代码和可能敏感文件。

原则：

- 不把整个本地文件夹上传 GitHub。
- 只上传摘要化画像、文件索引和用户确认可公开的报告。
- 审稿文件、项目申请、未公开数据、报销资料默认不上传。
- 文献 PDF 只保存合法来源；不能保存的只记录 DOI/link。
- GitHub 仓库如果公开，应避免放未发表细节和原始实验数据。

建议：

- GitHub 仓库设为 private。
- 每次上传前区分 `public-safe` 和 `private-research`。
- 小程序/网页登录后才能访问。

## 10. 分阶段路线

### 第 0 阶段：已完成基础

- 建立 GitHub 仓库。
- 建立每日 9:00 自动文献任务。
- 建立研究画像。
- 根据本地项目文件夹更新画像。

### 第 1 阶段：GitHub 记忆库完善

目标：先让每日任务稳定产出高质量报告。

任务：

- 固化 `papers.json` schema。
- 建立 `idea-log.json`。
- 建立 `decision-log.json`。
- 建立 `task-board.json`。
- 每日报告中加入“建议用户操作”。

完成标准：

- 每天能产出 3-10 篇筛选结果。
- 每篇都有相关度理由。
- 每天至少给出 3 个可评估 idea。

### 第 2 阶段：网页 MVP

目标：把 GitHub 里的 Markdown/JSON 做成可视化仪表盘。

页面：

- 今日文献。
- 论文卡片。
- 创新点候选。
- 画像编辑。
- 决策历史。

完成标准：

- 用户可以在网页点选 accepted/watch/rejected。
- 系统生成待确认画像更新。
- 用户确认后写回 GitHub。

### 第 3 阶段：微信小程序

目标：手机端每日查看与轻量决策。

功能：

- 今日推送摘要。
- 三个按钮：加入画像、加入 idea 池、忽略。
- 精读稍后看。
- 每周总结。

完成标准：

- 每天 9:00 后能看到当天摘要。
- 用户手机端完成 80% 的初筛决策。

### 第 4 阶段：深度科研助理

目标：从文献情报升级为论文推进系统。

功能：

- 自动生成 Related Work 分类。
- 自动生成实验缺口清单。
- 自动生成审稿风险矩阵。
- 根据 accepted ideas 更新 P1-P6 路线评分。
- 生成每周组会汇报 PPT 草稿。
- 生成论文 Introduction/Discussion 素材库。

## 11. 最推荐的下一步

不要一开始就做完整微信小程序。最稳路径是：

1. 先完善 GitHub 数据结构和每日任务输出。
2. 做一个网页版 Dashboard。
3. 等文献卡片、idea 状态、画像更新机制稳定后，再做微信小程序。

这样系统的科研判断先站稳，再做漂亮入口。

## 12. MVP 功能清单

第一版只做 6 个功能：

1. 每日论文抓取与总结。
2. 论文相关度评分。
3. 创新点候选池。
4. 用户决策：接受、观察、拒绝、转任务。
5. 画像更新提案。
6. GitHub 自动归档和版本追踪。

这 6 个功能跑顺后，网页和小程序都会自然长出来。

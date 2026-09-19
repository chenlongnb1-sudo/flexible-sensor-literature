# Codex 迁移交接说明

仓库：chenlongnb1-sudo/flexible-sensor-literature
用途：柔性电子传感器与电子皮肤科研文献情报、论文精读、研究画像和创新点管理。

## 给新电脑 Codex 的第一条指令

请先阅读本文件、README.md、research-memory/profile/user-research-profile.md、research-memory/system-blueprint.md 和最近一个 research-memory/literature/YYYY/YYYY-MM-DD/summaries/papers.json。然后检查仓库状态和目录，不要假设能读取旧电脑的本地路径或其他 Codex 对话。所有持续记忆以本仓库为准。

## 用户研究主线

用户的核心方向是柔性电子皮肤前端触觉计算，包含：低离散/装配容差触觉界面、ADC 前模拟矢量触觉读出、低冗余触觉阵列、可编程物理触觉投影、坏点/漂移/跨器件迁移/少样本校准，以及摩擦、纹理、滑移、机器人和人体监测应用。

每日论文最低进入正式日报的期刊门槛为 Nature/Science/Cell 子刊或 Advanced Materials 同等级来源。强相关论文才生成针对用户论文主线的创新建议；普通相关论文只做分类和摘要总结。

## 第一次恢复步骤

在 Windows PowerShell 中：

    git clone https://github.com/chenlongnb1-sudo/flexible-sensor-literature.git
    cd flexible-sensor-literature
    py -m venv .venv
    .\.venv\Scripts\Activate.ps1
    python -m pip install -r requirements.txt
    python -m unittest discover -s tests -v
    python scripts\build_research_intelligence.py
    python scripts\research_server.py

然后打开 http://127.0.0.1:8765。只查看网页也可以运行：

    cd web
    python -m http.server 8765

## 自动化配置

每日主任务由 Codex 自动任务在北京时间 09:00 执行；GitHub Actions 在北京时间 09:15 做容灾运行。仓库中的 .github/workflows/daily-literature.yml 已包含后备检索、测试、归档和通知逻辑。

在 GitHub 仓库 Settings > Secrets and variables > Actions 中配置：

- OPENAI_API_KEY：用于摘要的忠实中文翻译和中文总结。
- PUSHPLUS_TOKEN：推送到微信，可选。
- SERVERCHAN_SENDKEY：推送到微信，可选。
- BARK_URL：手机推送，可选。
- OPENALEX_MAILTO、OPENALEX_API_KEY、SEMANTIC_SCHOLAR_API_KEY：学术检索增强，可选。

可在 Actions Variables 中设置 LITERATURE_TRANSLATE_MODEL，默认使用 gpt-4o-mini。密钥只放 GitHub Secrets 或新电脑本地 .env，不能写进仓库文件。

## 数据目录

- research-memory/profile/user-research-profile.md：用户研究画像和当前论文主线。
- research-memory/system-blueprint.md：系统设计、筛选规则和后续路线。
- research-memory/conversations/：已归档的可见对话上下文。
- research-memory/file-maps/：本地科研文件的摘要索引。
- research-memory/literature/：按日期归档的论文、摘要、详情和日报。
- research-memory/ideas/idea-log.json：创新点候选及其状态。
- research-memory/decisions/decision-log.json：用户决策记录。
- research-memory/tasks/task-board.json：实验和写作任务。
- web/data/research-bundle.json：网页读取的数据包。
- web/data/paper-details/：逐篇详情、原文摘要、翻译、总结、方法和图解。

## 论文输出规则

每篇论文必须按以下顺序处理：保存原文摘要 -> 忠实中文翻译 -> 基于原文的中文总结 -> 创新点和对用户的启发。原文摘要不能被相关性理由替代。

只有拿到合法全文 PDF，才生成制备步骤、方法原文锚点和逐图/分图解释。拿不到 PDF 时保留 DOI、出版社页、Unpaywall/PMC/作者仓储等合法入口和失败原因，不猜测方法、图和实验数值。

## 新电脑上的 Codex 工作方式

1. 先读画像和最近日报，再处理用户的新问题。
2. 用户提供新的研究背景或本地文件目录时，更新 research-memory/profile/ 和 research-memory/file-maps/，不要上传整个本地科研文件夹。
3. 运行每日论文时，检查期刊等级、柔性电子主题和与 P1-P6 的相关性。
4. 用户确认加入画像后，才更新画像；创新点先进入候选或提案状态。
5. 所有代码和数据修改完成后运行测试，并提交到 main，除非用户指定其他分支。

## 隐私边界

仓库只保存摘要化研究画像、公开论文题录、合法可归档全文和用户明确可归档的科研记忆。未发表原始数据、项目申请、审稿文件、报销材料、私人文件和本地原始实验目录不应上传。公开仓库尤其要避免写入未发表实验细节和任何密钥。

## 当前已知限制

仓库不能自动读取旧电脑上没有提交的本地文件，也不能读取其他 Codex 对话中未归档的内容。需要持续记忆的内容必须写入本仓库的 profile、conversations、file-maps 或 literature 目录。

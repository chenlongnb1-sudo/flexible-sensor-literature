# Flexible Sensor Literature Intelligence

这是一个个人科研情报与论文画像仓库，用于持续维护柔性电子皮肤/触觉前端计算方向的研究记忆、每日文献报告、创新点候选、用户决策和网页 Dashboard。

## 当前主线

- 柔性电子皮肤前端触觉计算
- 低离散/容差触觉界面
- ADC 前模拟矢量触觉读出
- 低冗余矢量触觉阵列
- 可编程物理触觉投影前端
- 容错、可迁移、少样本校准的电子皮肤

## 本地打开网页

```powershell
cd C:\Users\Administrator\Documents\论文汇总\web
python -m http.server 8765
```

然后打开：

```text
http://localhost:8765
```

## 每日数据刷新

自动任务每天 09:00 运行。手动刷新网页数据包：

```powershell
cd C:\Users\Administrator\Documents\论文汇总
python scripts\build_research_intelligence.py
```

## 目录

```text
research-memory/
  profile/user-research-profile.md
  system-blueprint.md
  literature/YYYY/YYYY-MM-DD/
  ideas/idea-log.json
  decisions/decision-log.json
  tasks/task-board.json
  schemas/papers.schema.json
web/
  index.html
  styles.css
  app.js
  data/research-bundle.json
scripts/
  build_research_intelligence.py
```

## 决策原则

Agent 可以生成论文卡片、创新点候选和画像更新提案，但不能自动把新 idea 合并进用户论文画像。只有用户明确接受后，idea 才能进入画像或转成实验/写作任务。

const state = {
  view: "dashboard",
  filter: "all",
  paperQuery: "",
  trackFilter: "all",
  decisions: [],
  papers: [
    {
      id: "seed-pre-adc-tactile-front-end",
      title: "Seed topic: pre-ADC tactile front-end computing for flexible electronic skins",
      authors: [],
      venue: "System seed",
      date: "2026-07-14",
      paper_type: "topic-seed",
      tracks: ["P2", "P4"],
      relevance_score: 95,
      core_claim: "每日 Agent 应优先寻找把触觉特征形成从后端算法前移到传感器/模拟前端的论文。",
      transferable_points: [
        "Hardware Kz/Kx/Ky evidence for Paper A",
        "Programmable physical projection kernels for P4",
        "Fault tolerance and few-shot transfer for P5"
      ],
      risks: ["不要把高灵敏材料论文误判为核心相关。", "没有标定矩阵时不要写完整三维力重建。"],
      decision_hint: "profile_candidate"
    }
  ],
  ideas: [
    {
      id: "idea-p4-fault-projection-001",
      status: "watch",
      grade: "A",
      track: "P4/P5",
      title: "用可编程物理投影验证坏点条件下的渐进退化",
      hypothesis: "Normalized hardware projection features should degrade more gracefully than raw pixel readout when tactile pixels fail or drift.",
      minimum_experiment: "Construct 3x3 resistor/tactile array states with 0, 1, 5, 10, and 20 percent equivalent faults; compare raw, software projection, and hardware projection."
    },
    {
      id: "idea-p2-vector-ablation-001",
      status: "candidate",
      grade: "A",
      track: "P2",
      title: "把纹理识别消融转成 ADC 前矢量触觉证据链",
      hypothesis: "Kx/Ky tangential dynamics provide task-relevant friction cues that z-only or external force-reference channels miss.",
      minimum_experiment: "Record raw A/B/C/D, hardware Kz/Kx/Ky, z-only, and reference force under matched texture/sliding conditions."
    },
    {
      id: "idea-p1-tolerance-map-001",
      status: "candidate",
      grade: "B",
      track: "P1",
      title: "用偏移/旋转/接触半径热图证明低离散界面不是只提高灵敏度",
      hypothesis: "Gradient or non-periodic electrodes plus HCP microstructures reduce response dispersion under assembly and contact perturbations.",
      minimum_experiment: "Test G1-G5 under controlled shift, rotation, and contact-radius conditions; produce CV, void ratio, and sensitivity maps."
    }
  ],
  tasks: [
    {
      id: "task-p2-sync-vector-data",
      status: "next",
      track: "P2",
      title: "同步采集 raw A/B/C/D 与 hardware Kz/Kx/Ky",
      why: "这是 Paper A 高配身份能否成立的关键证据。",
      output: "A matched dataset and plot package for hardware vector vs software projection."
    },
    {
      id: "task-p4-resistor-projection",
      status: "planned",
      track: "P4",
      title: "搭建 3x3 精密电阻阵列验证 programmable projection",
      why: "先用低风险平台证明可编程物理投影前端的 R2 和坏点鲁棒性。",
      output: "Ksum/Kx/Ky/Klap/Kring/Kcorner hardware vs software projection report."
    }
  ],
  profileMarkdown: `# 用户研究画像

## 当前研究方向

用户当前博士主线不是普通“高灵敏柔性压力传感器”，而是围绕 **柔性电子皮肤前端触觉计算** 展开：

- 结构-传感器-模拟前端-阵列-闭环协同设计。
- 低离散/容差触觉界面。
- ADC 前模拟矢量触觉读出。
- 低冗余矢量触觉阵列。
- 可编程物理触觉投影前端。
- 容错、可迁移、少样本校准的电子皮肤。

## 当前瓶颈

- 高配 Paper A 需要硬件 Kz/Kx/Ky 的 ADC 前证据。
- P1 需要 shift、rotation、contact-radius、signal void ratio 等容差证据。
- P3/P4 需要从单器件推进到阵列层面的边缘/形状/容错/迁移指标。

## 每日文献筛选优先级

1. ADC 前、模拟前端、in-sensor computing、sensor-near computing。
2. 矢量触觉、剪切力/摩擦/滑移方向。
3. 柔性触觉阵列低通道读出和 macro-pixel。
4. 可编程物理计算、投影核、模拟矩阵/电流求和、单 ADC。
5. 电子皮肤容错、坏点鲁棒、跨器件迁移、少样本校准。`,
  report: `# 2026-07-14 文献工作流种子报告

本文件用于网页 MVP 和每日 Agent 输出格式对齐。正式每日任务应替换为当天真实检索结果。

## 今日聚焦

- ADC 前触觉计算。
- 模拟矢量触觉读出。
- 可编程物理触觉投影。
- 低冗余/容错/可迁移电子皮肤。

## 今日候选 idea

1. 用 3x3 精密电阻阵列先验证 programmable projection 的硬件-软件一致性。
2. 将坏点比例作为 P4/P5 的鲁棒性变量，比较 raw 与 normalized projection。
3. 将纹理识别消融实验重写为 tangential/vector dynamics 的任务证据，而不是普通分类精度。`
};

const titleMap = {
  dashboard: "总览",
  papers: "论文",
  ideas: "创新点",
  profile: "画像",
  tasks: "任务",
  reports: "报告"
};

function $(selector) {
  return document.querySelector(selector);
}

function $all(selector) {
  return Array.from(document.querySelectorAll(selector));
}

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function tag(label, tone = "") {
  return `<span class="tag ${tone}">${escapeHtml(label)}</span>`;
}

function showToast(message) {
  const toast = $("#toast");
  toast.textContent = message;
  toast.classList.add("show");
  window.setTimeout(() => toast.classList.remove("show"), 1800);
}

function recordDecision(type, itemId, decision) {
  state.decisions.push({
    id: `decision-${Date.now()}`,
    type,
    item_id: itemId,
    decision,
    created_at: new Date().toISOString()
  });
  showToast(`已记录：${decision}`);
}

function paperCard(paper) {
  return `
    <article class="paper-card">
      <div>
        <h3>${escapeHtml(paper.title)}</h3>
        <div class="paper-meta">
          <span>${escapeHtml(paper.venue || "Unknown venue")}</span>
          <span>${escapeHtml(paper.date || "")}</span>
          <span>${escapeHtml(paper.paper_type || "")}</span>
        </div>
        <p>${escapeHtml(paper.core_claim)}</p>
        <div class="tags">
          ${(paper.tracks || []).map((item) => tag(item, "blue")).join("")}
          ${tag(paper.decision_hint, "amber")}
        </div>
        <div class="card-actions">
          <button class="small-btn" data-paper-action="read" data-id="${paper.id}">精读</button>
          <button class="small-btn" data-paper-action="add_to_ideas" data-id="${paper.id}">加入 idea</button>
          <button class="small-btn" data-paper-action="profile_candidate" data-id="${paper.id}">画像候选</button>
          <button class="small-btn" data-paper-action="ignore" data-id="${paper.id}">忽略</button>
        </div>
      </div>
      <div class="score">${paper.relevance_score}</div>
    </article>
  `;
}

function ideaCard(idea) {
  return `
    <article class="idea-card">
      <div class="tags">${tag(idea.track, "blue")}${tag(`${idea.grade} 级`, "amber")}${tag(idea.status)}</div>
      <h3>${escapeHtml(idea.title)}</h3>
      <p>${escapeHtml(idea.hypothesis)}</p>
      <p><strong>最小实验：</strong>${escapeHtml(idea.minimum_experiment)}</p>
      <div class="card-actions">
        <button class="small-btn" data-idea-action="accepted" data-id="${idea.id}">加入画像</button>
        <button class="small-btn" data-idea-action="watch" data-id="${idea.id}">观察</button>
        <button class="small-btn" data-idea-action="converted_to_task" data-id="${idea.id}">转任务</button>
        <button class="small-btn" data-idea-action="rejected" data-id="${idea.id}">拒绝</button>
      </div>
    </article>
  `;
}

function taskCard(task) {
  return `
    <article class="task-card">
      <div class="tags">${tag(task.track, "blue")}${tag(task.status, "amber")}</div>
      <h3>${escapeHtml(task.title)}</h3>
      <p>${escapeHtml(task.why)}</p>
      <p><strong>输出：</strong>${escapeHtml(task.output)}</p>
    </article>
  `;
}

function markdownToHtml(markdown) {
  const lines = markdown.split(/\r?\n/);
  let html = "";
  let inList = false;
  for (const raw of lines) {
    const line = raw.trim();
    if (!line) {
      if (inList) {
        html += "</ul>";
        inList = false;
      }
      continue;
    }
    if (line.startsWith("# ")) {
      if (inList) {
        html += "</ul>";
        inList = false;
      }
      html += `<h1>${escapeHtml(line.slice(2))}</h1>`;
    } else if (line.startsWith("## ")) {
      if (inList) {
        html += "</ul>";
        inList = false;
      }
      html += `<h2>${escapeHtml(line.slice(3))}</h2>`;
    } else if (line.startsWith("- ")) {
      if (!inList) {
        html += "<ul>";
        inList = true;
      }
      html += `<li>${escapeHtml(line.slice(2))}</li>`;
    } else {
      if (inList) {
        html += "</ul>";
        inList = false;
      }
      html += `<p>${escapeHtml(line)}</p>`;
    }
  }
  if (inList) html += "</ul>";
  return html;
}

function getFilteredPapers() {
  const query = state.paperQuery.toLowerCase();
  return state.papers.filter((paper) => {
    const trackOk = state.trackFilter === "all" || (paper.tracks || []).includes(state.trackFilter);
    const text = [paper.title, paper.core_claim, paper.decision_hint, ...(paper.tracks || [])].join(" ").toLowerCase();
    return trackOk && (!query || text.includes(query));
  });
}

function renderDashboard() {
  $("#paperCount").textContent = state.papers.length;
  $("#ideaCount").textContent = state.ideas.length;
  $("#taskCount").textContent = state.tasks.length;
  const papers = state.filter === "all" ? state.papers : state.papers.filter((paper) => paper.decision_hint === state.filter);
  $("#topPapers").innerHTML = papers.map(paperCard).join("");
  $("#ideaQueue").innerHTML = state.ideas.filter((idea) => idea.status !== "accepted").map(ideaCard).join("");
  $("#gapList").innerHTML = [
    ["P2", "缺少 raw A/B/C/D 与 hardware Kz/Kx/Ky 同步证据。"],
    ["P1", "缺少 shift、rotation、contact-radius 容差热图。"],
    ["P4", "需要先用电阻阵列验证 projection kernel 的硬件-软件一致性。"]
  ].map(([track, text]) => `<div class="gap-item">${tag(track, "blue")}<p>${escapeHtml(text)}</p></div>`).join("");
}

function renderPapers() {
  $("#paperGrid").innerHTML = getFilteredPapers().map(paperCard).join("");
}

function renderIdeas() {
  const columns = [
    ["candidate", "候选"],
    ["watch", "观察"],
    ["accepted", "已加入"],
    ["rejected", "已拒绝"]
  ];
  $("#ideaBoard").innerHTML = columns.map(([status, label]) => {
    const ideas = state.ideas.filter((idea) => idea.status === status);
    return `<section class="kanban-col"><h2>${label}</h2>${ideas.map(ideaCard).join("") || "<p>暂无</p>"}</section>`;
  }).join("");
}

function renderProfile() {
  $("#profileContent").innerHTML = markdownToHtml(state.profileMarkdown);
}

function renderTasks() {
  $("#taskList").innerHTML = state.tasks.map(taskCard).join("");
}

function renderReports() {
  $("#dailyReport").textContent = state.report;
}

function render() {
  $("#viewTitle").textContent = titleMap[state.view];
  $all(".view").forEach((view) => view.classList.toggle("active", view.id === state.view));
  $all(".nav-item").forEach((button) => button.classList.toggle("active", button.dataset.view === state.view));
  renderDashboard();
  renderPapers();
  renderIdeas();
  renderProfile();
  renderTasks();
  renderReports();
}

function downloadJson(filename, data) {
  const blob = new Blob([JSON.stringify(data, null, 2)], { type: "application/json;charset=utf-8" });
  const link = document.createElement("a");
  link.href = URL.createObjectURL(blob);
  link.download = filename;
  link.click();
  URL.revokeObjectURL(link.href);
}

function bindEvents() {
  $all(".nav-item").forEach((button) => {
    button.addEventListener("click", () => {
      state.view = button.dataset.view;
      render();
    });
  });
  $all(".segment").forEach((button) => {
    button.addEventListener("click", () => {
      state.filter = button.dataset.filter;
      $all(".segment").forEach((item) => item.classList.toggle("active", item === button));
      renderDashboard();
    });
  });
  $("#paperSearch").addEventListener("input", (event) => {
    state.paperQuery = event.target.value;
    renderPapers();
  });
  $("#trackFilter").addEventListener("change", (event) => {
    state.trackFilter = event.target.value;
    renderPapers();
  });
  document.body.addEventListener("click", (event) => {
    const paperButton = event.target.closest("[data-paper-action]");
    if (paperButton) recordDecision("paper", paperButton.dataset.id, paperButton.dataset.paperAction);
    const ideaButton = event.target.closest("[data-idea-action]");
    if (ideaButton) {
      const idea = state.ideas.find((item) => item.id === ideaButton.dataset.id);
      if (idea) idea.status = ideaButton.dataset.ideaAction;
      recordDecision("idea", ideaButton.dataset.id, ideaButton.dataset.ideaAction);
      render();
    }
  });
  $("#exportDecisions").addEventListener("click", () => {
    downloadJson("decision-log-export.json", { updated_at: new Date().toISOString(), decisions: state.decisions });
  });
  $("#downloadProposal").addEventListener("click", () => {
    const acceptedIdeas = state.ideas.filter((idea) => idea.status === "accepted");
    downloadJson("profile-update-proposal.json", {
      created_at: new Date().toISOString(),
      proposals: acceptedIdeas.map((idea) => ({
        source_idea: idea.id,
        proposal: `将“${idea.title}”加入 ${idea.track} 画像候选。`,
        evidence_needed: idea.minimum_experiment,
        status: "pending_manual_merge"
      }))
    });
  });
  $("#syncHint").addEventListener("click", () => {
    state.view = "profile";
    render();
    showToast("先处理 idea，再导出画像更新提案");
  });
}

bindEvents();
loadBundle().finally(render);

async function loadBundle() {
  try {
    const response = await fetch("./data/research-bundle.json", { cache: "no-store" });
    if (!response.ok) return;
    const bundle = await response.json();
    if (Array.isArray(bundle.papers) && bundle.papers.length) state.papers = bundle.papers;
    if (Array.isArray(bundle.ideas) && bundle.ideas.length) state.ideas = bundle.ideas;
    if (Array.isArray(bundle.tasks) && bundle.tasks.length) state.tasks = bundle.tasks;
    if (typeof bundle.profile_markdown === "string" && bundle.profile_markdown.trim()) {
      state.profileMarkdown = bundle.profile_markdown;
    }
    if (typeof bundle.daily_report_markdown === "string" && bundle.daily_report_markdown.trim()) {
      state.report = bundle.daily_report_markdown;
    }
  } catch (error) {
    console.warn("Using embedded seed data because research-bundle.json could not be loaded.", error);
  }
}

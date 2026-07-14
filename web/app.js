const EMPTY_BUNDLE = {
  latest_report_date: "",
  profile_markdown: "",
  daily_report_markdown: "",
  papers: [], ideas: [], tasks: [], decisions: [], profile_proposals: [], reports: [],
  query_log: [], source_errors: [],
  assets: { hero_image2: false, icon_image2: false },
  stats: { papers_today: 0, must_read: 0, pending_ideas: 0, pending_proposals: 0, open_tasks: 0 }
};

const state = {
  view: "dashboard",
  dashboardFilter: "all",
  paperQuery: "",
  trackFilter: "all",
  paperActionFilter: "all",
  ideaStatusFilter: "all",
  selectedReportDate: "",
  apiMode: false,
  busy: false,
  bundle: structuredClone(EMPTY_BUNDLE),
  offlineQueue: JSON.parse(localStorage.getItem("research-decision-queue") || "[]"),
  dialogAction: null
};

const titleMap = {
  dashboard: "总览", papers: "论文", ideas: "创新点", profile: "研究画像",
  tasks: "任务", reports: "日报", decisions: "决策历史", settings: "运行状态"
};
const actionLabels = {
  read: "精读", skim: "略读", ignore: "忽略", add_to_ideas: "加入 idea",
  watch: "观察", reject: "拒绝", convert_to_task: "转任务", propose_profile: "生成画像提案",
  accept: "接受并写入画像"
};
const statusLabels = {
  candidate: "候选", watch: "观察", proposed: "提案中", accepted: "已采纳",
  rejected: "已拒绝", converted_to_task: "已转任务", next: "下一步", planned: "计划中", done: "已完成"
};

const $ = (selector) => document.querySelector(selector);
const $all = (selector) => Array.from(document.querySelectorAll(selector));

function escapeHtml(value = "") {
  return String(value).replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll(">", "&gt;").replaceAll('"', "&quot;").replaceAll("'", "&#039;");
}

function safeUrl(value = "") {
  try {
    const url = new URL(value, window.location.href);
    return ["http:", "https:"].includes(url.protocol) ? url.href : "";
  } catch { return ""; }
}

function inlineMarkdown(value = "") {
  let output = escapeHtml(value);
  output = output.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
  output = output.replace(/\[([^\]]+)\]\((https?:\/\/[^)]+)\)/g, (_, label, url) => `<a href="${escapeHtml(safeUrl(url))}" target="_blank" rel="noreferrer">${label}</a>`);
  return output;
}

function markdownToHtml(markdown = "") {
  const lines = markdown.split(/\r?\n/);
  let html = "";
  let inList = false;
  let inTable = false;
  for (let index = 0; index < lines.length; index += 1) {
    const raw = lines[index];
    const line = raw.trim();
    const closeList = () => { if (inList) { html += "</ul>"; inList = false; } };
    const closeTable = () => { if (inTable) { html += "</tbody></table>"; inTable = false; } };
    if (!line) { closeList(); closeTable(); continue; }
    if (/^\|[-:| ]+\|$/.test(line)) continue;
    if (line.startsWith("|")) {
      closeList();
      const cells = line.split("|").slice(1, -1).map((cell) => `<td>${inlineMarkdown(cell.trim())}</td>`).join("");
      if (!inTable) { html += "<table><tbody>"; inTable = true; }
      html += `<tr>${cells}</tr>`;
      continue;
    }
    closeTable();
    if (line.startsWith("### ")) { closeList(); html += `<h3>${inlineMarkdown(line.slice(4))}</h3>`; }
    else if (line.startsWith("## ")) { closeList(); html += `<h2>${inlineMarkdown(line.slice(3))}</h2>`; }
    else if (line.startsWith("# ")) { closeList(); html += `<h1>${inlineMarkdown(line.slice(2))}</h1>`; }
    else if (line.startsWith("- ")) { if (!inList) { html += "<ul>"; inList = true; } html += `<li>${inlineMarkdown(line.slice(2))}</li>`; }
    else if (/^\d+\.\s/.test(line)) { closeList(); html += `<p>${inlineMarkdown(line)}</p>`; }
    else if (line.startsWith("> ")) { closeList(); html += `<blockquote>${inlineMarkdown(line.slice(2))}</blockquote>`; }
    else { closeList(); html += `<p>${inlineMarkdown(line)}</p>`; }
  }
  if (inList) html += "</ul>";
  if (inTable) html += "</tbody></table>";
  return html;
}

function icon(name, size = 16) { return `<i data-lucide="${name}" width="${size}" height="${size}"></i>`; }
function tag(label, tone = "") { return `<span class="tag ${tone}">${escapeHtml(label)}</span>`; }
function formatDate(value) { if (!value) return "日期未知"; return escapeHtml(value.slice(0, 10)); }
function emptyState(title, text) { return `<div class="empty-state">${icon("inbox", 22)}<h3>${escapeHtml(title)}</h3><p>${escapeHtml(text)}</p></div>`; }

function showToast(message, tone = "") {
  const toast = $("#toast");
  toast.textContent = message;
  toast.className = `toast show ${tone}`;
  window.clearTimeout(showToast.timer);
  showToast.timer = window.setTimeout(() => { toast.className = "toast"; }, 2600);
}

function setBusy(busy, label = "") {
  state.busy = busy;
  $("#runDaily").disabled = busy || !state.apiMode;
  $("#syncGitHub").disabled = busy || !state.apiMode;
  if (label) showToast(label);
}

async function fetchJson(url, options = {}) {
  const response = await fetch(url, { cache: "no-store", ...options });
  const payload = await response.json().catch(() => ({}));
  if (!response.ok) throw new Error(payload.error || `HTTP ${response.status}`);
  return payload;
}

async function postJson(url, payload) {
  return fetchJson(url, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(payload) });
}

function paperLink(paper) { return safeUrl(paper.url) || (paper.doi ? `https://doi.org/${paper.doi}` : ""); }
function paperDetailLink(paper) { return `./paper.html?id=${encodeURIComponent(paper.id || "")}`; }
function localPdfLink(paper) {
  if (!paper.local_pdf) return "";
  if (state.apiMode) return `./files/${paper.local_pdf}`;
  return `https://github.com/chenlongnb1-sudo/flexible-sensor-literature/blob/main/${paper.local_pdf}`;
}

function paperCard(paper, compact = false) {
  const link = paperLink(paper);
  const detailLink = paperDetailLink(paper);
  const pdfLink = localPdfLink(paper);
  const authors = (paper.authors || []).slice(0, 4).join(", ");
  const scoreTone = paper.relevance_score >= 80 ? "high" : paper.relevance_score >= 60 ? "medium" : "low";
  const sources = (paper.sources || []).map((source) => tag(source)).join("");
  const risks = (paper.risks || []).map((item) => `<li>${escapeHtml(item)}</li>`).join("");
  const transfers = (paper.transferable_points || []).map((item) => `<li>${escapeHtml(item)}</li>`).join("");
  return `
    <article class="paper-card ${compact ? "compact" : ""}">
      <div class="paper-main">
        <div class="paper-topline"><div class="tags">${(paper.tracks || []).map((item) => tag(item, "blue")).join("")}${tag(actionLabels[paper.decision_hint] || paper.decision_hint || "待判断", "amber")}${sources}</div><span class="paper-date">${formatDate(paper.date)}</span></div>
        <h3><a href="${escapeHtml(detailLink)}">${escapeHtml(paper.title)}</a></h3>
        <div class="paper-meta"><span>${escapeHtml(paper.venue || "来源未标注")}</span>${authors ? `<span>${escapeHtml(authors)}${(paper.authors || []).length > 4 ? " et al." : ""}</span>` : ""}</div>
        <p class="paper-claim">${escapeHtml(paper.summary_zh || paper.core_claim || "等待摘要分析")}</p>
        ${compact ? "" : `<details><summary>迁移价值与风险</summary><div class="detail-grid"><div><strong>可迁移</strong><ul>${transfers || "<li>需精读后判断</li>"}</ul></div><div><strong>边界</strong><ul>${risks || "<li>需精读后判断</li>"}</ul></div></div></details>`}
        <div class="card-actions">
          <button class="small-btn" data-paper-action="read" data-id="${escapeHtml(paper.id)}">${icon("book-open-check")}精读</button>
          <button class="small-btn" data-paper-action="add_to_ideas" data-id="${escapeHtml(paper.id)}">${icon("lightbulb")}加入 idea</button>
          <button class="small-btn quiet-action" data-paper-action="ignore" data-id="${escapeHtml(paper.id)}">${icon("archive")}忽略</button>
          <a class="small-btn primary-action" href="${escapeHtml(detailLink)}">${icon("book-open-text")}详情</a>
          ${link ? `<a class="small-btn" href="${escapeHtml(link)}" target="_blank" rel="noreferrer">${icon("external-link")}来源</a>` : ""}
          ${pdfLink ? `<a class="small-btn" href="${escapeHtml(pdfLink)}" target="_blank" rel="noreferrer">${icon("file-down")}PDF</a>` : ""}
        </div>
      </div>
      <div class="score ${scoreTone}"><strong>${Number(paper.relevance_score || 0)}</strong><span>画像匹配</span></div>
    </article>`;
}

function ideaCard(idea, compact = false) {
  const source = (idea.source_papers || [])[0];
  const status = statusLabels[idea.status] || idea.status;
  return `
    <article class="idea-card ${compact ? "compact" : ""}">
      <div class="tags">${tag(idea.track || "未分轨", "blue")}${tag(`${idea.grade || "B"} 级`, "amber")}${tag(status)}</div>
      <h3>${escapeHtml(idea.title)}</h3>
      <p>${escapeHtml(idea.hypothesis || "")}</p>
      ${compact ? "" : `<div class="experiment-block"><span>最小实验</span><p>${escapeHtml(idea.minimum_experiment || "待定义")}</p></div>`}
      ${source ? `<a class="source-link" href="${escapeHtml(safeUrl(source.url || (source.doi ? `https://doi.org/${source.doi}` : "")))}" target="_blank" rel="noreferrer">${icon("external-link")} ${escapeHtml(source.title || "来源论文")}</a>` : ""}
      ${["candidate", "watch"].includes(idea.status) ? `<div class="card-actions">
        <button class="small-btn primary-action" data-idea-action="propose_profile" data-id="${escapeHtml(idea.id)}">${icon("scan-search")}加入画像提案</button>
        <button class="small-btn" data-idea-action="watch" data-id="${escapeHtml(idea.id)}">${icon("eye")}观察</button>
        <button class="small-btn" data-idea-action="convert_to_task" data-id="${escapeHtml(idea.id)}">${icon("list-plus")}转任务</button>
        <button class="small-btn quiet-action" data-idea-action="reject" data-id="${escapeHtml(idea.id)}">${icon("x")}拒绝</button>
      </div>` : ""}
    </article>`;
}

function proposalCard(proposal) {
  return `<article class="proposal-card">
    <div class="tags">${tag(proposal.track || "未分轨", "blue")}${tag(statusLabels[proposal.status] || proposal.status, "amber")}</div>
    <h3>${escapeHtml(proposal.title)}</h3><p>${escapeHtml(proposal.proposal)}</p>
    <div class="proposal-evidence"><strong>写入前条件</strong><p>${escapeHtml(proposal.minimum_experiment || "需补充最小验证")}</p><strong>风险</strong><p>${escapeHtml(proposal.risk || "需人工判断")}</p></div>
    ${proposal.status === "pending" ? `<div class="card-actions"><button class="small-btn primary-action" data-proposal-action="accept" data-id="${escapeHtml(proposal.id)}">${icon("check")}接受并写入</button><button class="small-btn" data-proposal-action="watch" data-id="${escapeHtml(proposal.id)}">${icon("eye")}暂存观察</button><button class="small-btn quiet-action" data-proposal-action="reject" data-id="${escapeHtml(proposal.id)}">${icon("x")}拒绝</button></div>` : ""}
  </article>`;
}

function taskCard(task) {
  return `<article class="task-card"><div class="task-track">${tag(task.track || "未分轨", "blue")}${tag(statusLabels[task.status] || task.status, "amber")}</div><div><h3>${escapeHtml(task.title)}</h3><p>${escapeHtml(task.why || "")}</p><div class="task-output"><strong>交付物</strong><span>${escapeHtml(task.output || "待定义")}</span></div></div></article>`;
}

function filteredPapers() {
  const query = state.paperQuery.trim().toLowerCase();
  return state.bundle.papers.filter((paper) => {
    const trackOk = state.trackFilter === "all" || (paper.tracks || []).includes(state.trackFilter);
    const actionOk = state.paperActionFilter === "all" || paper.decision_hint === state.paperActionFilter;
    const haystack = [paper.title, paper.venue, paper.core_claim, paper.summary_zh, ...(paper.tracks || [])].join(" ").toLowerCase();
    return trackOk && actionOk && (!query || haystack.includes(query));
  });
}

function renderDashboard() {
  const stats = state.bundle.stats || EMPTY_BUNDLE.stats;
  $("#reportDate").textContent = state.bundle.latest_report_date ? `${state.bundle.latest_report_date} 日报` : "暂无日报";
  $("#paperCount").textContent = stats.papers_today ?? state.bundle.papers.length;
  $("#mustReadCount").textContent = stats.must_read ?? 0;
  $("#ideaCount").textContent = stats.pending_ideas ?? 0;
  $("#taskCount").textContent = stats.open_tasks ?? 0;
  const papers = state.dashboardFilter === "all" ? state.bundle.papers : state.bundle.papers.filter((paper) => paper.decision_hint === state.dashboardFilter);
  $("#topPapers").innerHTML = papers.length ? papers.slice(0, 5).map((paper) => paperCard(paper, true)).join("") : emptyState("没有符合当前筛选的论文", "系统不会用偏题论文填满日报。") ;
  const pending = state.bundle.ideas.filter((idea) => ["candidate", "watch"].includes(idea.status));
  $("#ideaQueue").innerHTML = pending.length ? pending.slice(0, 4).map((idea) => ideaCard(idea, true)).join("") : emptyState("暂无待处理 idea", "新论文中的可验证迁移点会进入这里。") ;
  const gaps = [
    ["P2", "同步记录 raw A/B/C/D 与 hardware Kz/Kx/Ky，并完成 R2、PSD/SNR 与通道消融。"],
    ["P1", "补齐 shift、rotation、contact-radius 和 signal-void ratio 容差地图。"],
    ["P4", "用 3x3 精密电阻阵列验证 projection kernel 的硬件-软件一致性。"],
    ["P5", "建立坏点比例、增益漂移和少样本校准下的渐进退化曲线。"]
  ];
  $("#gapList").innerHTML = gaps.map(([track, text]) => `<div class="gap-item">${tag(track, "blue")}<p>${escapeHtml(text)}</p></div>`).join("");
}

function renderPapers() {
  const papers = filteredPapers();
  $("#paperGrid").innerHTML = papers.length ? papers.map((paper) => paperCard(paper)).join("") : emptyState("没有匹配论文", "调整搜索词、轨道或建议动作筛选。") ;
}

function renderIdeas() {
  const ideas = state.ideaStatusFilter === "all" ? state.bundle.ideas : state.bundle.ideas.filter((idea) => idea.status === state.ideaStatusFilter);
  $("#ideaSummary").textContent = `${ideas.length} 个创新点`;
  $("#ideaBoard").innerHTML = ideas.length ? ideas.map((idea) => ideaCard(idea)).join("") : emptyState("这个状态下没有 idea", "切换状态筛选查看其他候选。") ;
}

function renderProfile() {
  const pending = state.bundle.profile_proposals.filter((proposal) => proposal.status === "pending");
  $("#proposalList").innerHTML = pending.length ? pending.map(proposalCard).join("") : emptyState("暂无待确认画像提案", "先在创新点页选择“加入画像提案”。") ;
  $("#profileContent").innerHTML = markdownToHtml(state.bundle.profile_markdown || "# 暂无研究画像");
}

function renderTasks() {
  const open = state.bundle.tasks.filter((task) => !["done", "cancelled"].includes(task.status));
  $("#taskSummary").textContent = `${open.length} 个开放任务`;
  $("#taskList").innerHTML = state.bundle.tasks.length ? state.bundle.tasks.map(taskCard).join("") : emptyState("暂无任务", "把一个 idea 转为任务后会在这里生成交付物。") ;
}

function renderReports() {
  const reports = state.bundle.reports || [];
  if (!state.selectedReportDate && reports.length) state.selectedReportDate = reports[0].date;
  $("#reportIndex").innerHTML = reports.length ? reports.map((report) => `<button class="report-index-item ${report.date === state.selectedReportDate ? "active" : ""}" data-report-date="${escapeHtml(report.date)}"><span>${escapeHtml(report.date)}</span><small>${report.paper_count} 篇 · top ${report.top_score}</small></button>`).join("") : emptyState("暂无归档", "运行今日检索后会生成第一份日报。") ;
  const selected = reports.find((report) => report.date === state.selectedReportDate);
  $("#reportContent").innerHTML = markdownToHtml(selected?.report_markdown || state.bundle.daily_report_markdown || "# 暂无报告");
}

function renderDecisions() {
  const decisions = [...state.bundle.decisions].reverse();
  $("#decisionList").innerHTML = decisions.length ? decisions.map((item) => `<article class="decision-item"><div class="decision-icon">${icon(item.decision === "reject" ? "x" : item.decision === "watch" ? "eye" : "check")}</div><div><div class="decision-title"><strong>${escapeHtml(actionLabels[item.decision] || item.decision)}</strong>${tag(item.type || "item")}</div><p>${escapeHtml(item.item_id)}</p>${item.note ? `<blockquote>${escapeHtml(item.note)}</blockquote>` : ""}</div><time>${formatDate(item.created_at)}</time></article>`).join("") : emptyState("暂无决策记录", "你对论文、idea 和画像提案的每次操作都会留痕。") ;
}

function renderSettings() {
  const sourceMap = new Map();
  state.bundle.query_log.forEach((item) => {
    const source = item.source || "unknown";
    const current = sourceMap.get(source) || { ok: 0, failed: 0, results: 0 };
    current[item.status === "ok" ? "ok" : "failed"] += 1;
    current.results += Number(item.result_count || 0);
    sourceMap.set(source, current);
  });
  state.bundle.source_errors.forEach((item) => {
    if (!sourceMap.has(item.source)) sourceMap.set(item.source, { ok: 0, failed: 1, results: 0 });
  });
  $("#sourceStatus").innerHTML = sourceMap.size ? [...sourceMap.entries()].map(([source, data]) => `<div class="source-item"><span class="status-dot ${data.ok ? "online" : "warning"}"></span><div><strong>${escapeHtml(source)}</strong><small>${data.results} 条题录 · ${data.failed} 个异常</small></div></div>`).join("") : emptyState("尚未运行检索", "运行后会显示每个学术数据源的状态。") ;
  $("#runtimeInfo").innerHTML = [
    ["工作模式", state.apiMode ? "本地写入模式" : "静态只读模式"],
    ["最新日报", state.bundle.latest_report_date || "暂无"],
    ["离线决策", `${state.offlineQueue.length} 条`],
    ["画像提案", `${state.bundle.stats?.pending_proposals || 0} 条待确认`],
    ["数据版本", `schema v${state.bundle.schema_version || 1}`]
  ].map(([label, value]) => `<div class="runtime-item"><span>${escapeHtml(label)}</span><strong>${escapeHtml(value)}</strong></div>`).join("");
}

function renderServiceState() {
  $("#serviceDot").className = `status-dot ${state.apiMode ? "online" : "warning"}`;
  $("#serviceLabel").textContent = state.apiMode ? "本地写入已连接" : "静态只读 / 离线队列";
  $("#runDaily").disabled = !state.apiMode || state.busy;
  $("#syncGitHub").disabled = !state.apiMode || state.busy;
  $("#exportQueue").hidden = !state.offlineQueue.length;
  const pending = state.bundle.stats?.pending_proposals || 0;
  $("#proposalNavCount").hidden = pending === 0;
  $("#proposalNavCount").textContent = pending;
}

function renderAssets() {
  const assets = state.bundle.assets || EMPTY_BUNDLE.assets;
  const hero = assets.hero_image2 ? "./assets/tactile-front-end-image2.webp" : "./assets/tactile-front-end.svg";
  const iconSource = assets.icon_image2 ? "./assets/research-intelligence-icon-image2.png" : "./assets/tactile-front-end.svg";
  if ($("#heroImage").getAttribute("src") !== hero) $("#heroImage").setAttribute("src", hero);
  if ($("#brandImage").getAttribute("src") !== iconSource) $("#brandImage").setAttribute("src", iconSource);
}

function render() {
  $("#viewTitle").textContent = titleMap[state.view];
  $all(".view").forEach((view) => view.classList.toggle("active", view.id === state.view));
  $all(".nav-item").forEach((button) => button.classList.toggle("active", button.dataset.view === state.view));
  renderDashboard(); renderPapers(); renderIdeas(); renderProfile(); renderTasks(); renderReports(); renderDecisions(); renderSettings(); renderServiceState(); renderAssets();
  window.setTimeout(() => window.lucide?.createIcons(), 0);
}

function queueOfflineDecision(itemType, itemId, action, note = "") {
  state.offlineQueue.push({ id: `offline-${Date.now()}`, item_type: itemType, item_id: itemId, action, note, created_at: new Date().toISOString() });
  localStorage.setItem("research-decision-queue", JSON.stringify(state.offlineQueue));
  showToast("当前为静态模式，决策已放入离线队列", "warning");
  renderServiceState();
}

async function sendDecision(itemType, itemId, action, note = "") {
  if (!state.apiMode) { queueOfflineDecision(itemType, itemId, action, note); return; }
  setBusy(true);
  try {
    const result = await postJson("./api/decisions", { item_type: itemType, item_id: itemId, action, note });
    state.bundle = { ...EMPTY_BUNDLE, ...result.bundle };
    showToast(`已记录：${actionLabels[action] || action}`);
    render();
  } catch (error) { showToast(error.message, "error"); }
  finally { setBusy(false); renderServiceState(); }
}

async function sendProposalDecision(id, action, note = "") {
  if (!state.apiMode) { queueOfflineDecision("profile_proposal", id, action, note); return; }
  setBusy(true);
  try {
    const result = await postJson(`./api/proposals/${encodeURIComponent(id)}/${action}`, { note });
    state.bundle = { ...EMPTY_BUNDLE, ...result.bundle };
    showToast(action === "accept" ? "已写入研究画像" : "提案状态已更新");
    render();
  } catch (error) { showToast(error.message, "error"); }
  finally { setBusy(false); renderServiceState(); }
}

function openDialog({ title, message, confirmLabel = "确认", noteRequired = false, action }) {
  state.dialogAction = action;
  $("#dialogTitle").textContent = title;
  $("#dialogMessage").textContent = message;
  $("#dialogConfirm").textContent = confirmLabel;
  $("#dialogNoteWrap").classList.toggle("required", noteRequired);
  $("#dialogNote").required = noteRequired;
  $("#dialogNote").value = "";
  $("#decisionDialog").showModal();
  window.setTimeout(() => window.lucide?.createIcons(), 0);
}

function downloadJson(filename, data) {
  const blob = new Blob([JSON.stringify(data, null, 2)], { type: "application/json;charset=utf-8" });
  const link = document.createElement("a");
  link.href = URL.createObjectURL(blob); link.download = filename; link.click(); URL.revokeObjectURL(link.href);
}

function changeView(view) {
  state.view = view;
  render();
  window.scrollTo({ top: 0, behavior: "smooth" });
}

function bindEvents() {
  $all(".nav-item").forEach((button) => button.addEventListener("click", () => changeView(button.dataset.view)));
  $all("[data-dashboard-filter]").forEach((button) => button.addEventListener("click", () => {
    state.dashboardFilter = button.dataset.dashboardFilter;
    $all("[data-dashboard-filter]").forEach((item) => item.classList.toggle("active", item === button));
    renderDashboard(); window.lucide?.createIcons();
  }));
  $("#paperSearch").addEventListener("input", (event) => { state.paperQuery = event.target.value; renderPapers(); window.lucide?.createIcons(); });
  $("#trackFilter").addEventListener("change", (event) => { state.trackFilter = event.target.value; renderPapers(); window.lucide?.createIcons(); });
  $("#paperActionFilter").addEventListener("change", (event) => { state.paperActionFilter = event.target.value; renderPapers(); window.lucide?.createIcons(); });
  $("#ideaStatusFilter").addEventListener("change", (event) => { state.ideaStatusFilter = event.target.value; renderIdeas(); window.lucide?.createIcons(); });

  document.body.addEventListener("click", (event) => {
    const jump = event.target.closest("[data-jump]");
    if (jump) { changeView(jump.dataset.jump); return; }
    const report = event.target.closest("[data-report-date]");
    if (report) { state.selectedReportDate = report.dataset.reportDate; renderReports(); return; }
    const paperButton = event.target.closest("[data-paper-action]");
    if (paperButton) {
      const action = paperButton.dataset.paperAction;
      sendDecision("paper", paperButton.dataset.id, action);
      if (action === "read") {
        const paper = state.bundle.papers.find((item) => item.id === paperButton.dataset.id);
        const link = paper && paperDetailLink(paper); if (link) window.open(link, "_blank", "noopener");
      }
      return;
    }
    const ideaButton = event.target.closest("[data-idea-action]");
    if (ideaButton) {
      const action = ideaButton.dataset.ideaAction;
      if (action === "reject") {
        openDialog({ title: "拒绝这个创新点", message: "拒绝理由会进入决策历史，帮助系统避免重复推荐。", confirmLabel: "确认拒绝", noteRequired: true, action: (note) => sendDecision("idea", ideaButton.dataset.id, action, note) });
      } else sendDecision("idea", ideaButton.dataset.id, action);
      return;
    }
    const proposalButton = event.target.closest("[data-proposal-action]");
    if (proposalButton) {
      const action = proposalButton.dataset.proposalAction;
      const messages = {
        accept: "确认后，该创新点会永久追加到用户研究画像并保留来源与风险边界。",
        watch: "提案将退回观察状态，不会写入画像。",
        reject: "提案和来源 idea 将标记为拒绝，理由用于以后去重。"
      };
      openDialog({ title: action === "accept" ? "接受画像提案" : action === "watch" ? "暂存观察" : "拒绝画像提案", message: messages[action], confirmLabel: action === "accept" ? "接受并写入" : "确认", noteRequired: action === "reject", action: (note) => sendProposalDecision(proposalButton.dataset.id, action, note) });
    }
  });

  $("#decisionForm").addEventListener("submit", (event) => {
    const value = event.submitter?.value;
    if (value !== "confirm") { state.dialogAction = null; return; }
    event.preventDefault();
    if (!event.currentTarget.reportValidity()) return;
    const action = state.dialogAction; const note = $("#dialogNote").value.trim();
    $("#decisionDialog").close(); state.dialogAction = null; action?.(note);
  });

  $("#exportQueue").addEventListener("click", () => downloadJson("research-decision-queue.json", { exported_at: new Date().toISOString(), decisions: state.offlineQueue }));
  $("#syncGitHub").addEventListener("click", async () => {
    if (!state.apiMode) return;
    setBusy(true, "正在提交并推送 GitHub…");
    try { const result = await postJson("./api/sync", { message: "chore: sync research decisions" }); showToast(`GitHub 已同步 · ${result.revision}`); }
    catch (error) { showToast(error.message, "error"); }
    finally { setBusy(false); renderServiceState(); }
  });
  $("#runDaily").addEventListener("click", async () => {
    if (!state.apiMode) return;
    setBusy(true, "正在检索多源文献，通常需要 1–3 分钟…");
    try { const result = await postJson("./api/run-daily", { download_pdfs: true }); state.bundle = { ...EMPTY_BUNDLE, ...result.bundle }; showToast("今日文献与创新点已刷新"); render(); }
    catch (error) { showToast(error.message, "error"); }
    finally { setBusy(false); renderServiceState(); }
  });
}

async function loadBundle() {
  try {
    await fetchJson("./api/health");
    state.apiMode = true;
    state.bundle = { ...EMPTY_BUNDLE, ...(await fetchJson("./api/bundle")) };
  } catch {
    state.apiMode = false;
    try { state.bundle = { ...EMPTY_BUNDLE, ...(await fetchJson("./data/research-bundle.json")) }; }
    catch (error) { showToast(`数据加载失败：${error.message}`, "error"); }
  }
  state.selectedReportDate = state.bundle.latest_report_date;
  render();
}

bindEvents();
loadBundle();
if ("serviceWorker" in navigator && location.protocol !== "file:") navigator.serviceWorker.register("./sw.js").catch(() => {});

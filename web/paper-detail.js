const detailRoot = document.querySelector("#paperDetail");
const sourceLink = document.querySelector("#sourceLink");

function escapeHtml(value) {
  return String(value ?? "").replace(/[&<>'"]/g, (char) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", "'": "&#39;", '"': "&quot;" }[char]));
}

function safeUrl(value) {
  if (!value) return "";
  try {
    const url = new URL(value, window.location.href);
    return ["http:", "https:"].includes(url.protocol) ? url.href : "";
  } catch { return ""; }
}

function list(items, empty = "等待全文解析") {
  return items?.length ? `<ul>${items.map((item) => `<li>${escapeHtml(item)}</li>`).join("")}</ul>` : `<p class="quiet">${escapeHtml(empty)}</p>`;
}

function renderSteps(steps, hasFulltext) {
  if (!steps?.length) return `<div class="detail-empty">${hasFulltext ? "PDF 未识别出可靠的制备步骤，需在人工精读阶段复核。" : "尚未取得合法开放全文，暂不生成制备步骤。"}</div>`;
  return `<ol class="preparation-steps">${steps.map((step) => `
    <li>
      <div class="step-index">${Number(step.step || 0)}</div>
      <div><div class="step-head"><strong>${escapeHtml(step.category_zh)}</strong><a href="#pdf">p.${Number(step.page || 0)}</a></div>
      <p>${escapeHtml(step.explanation_zh)}</p><details><summary>查看方法原文</summary><p>${escapeHtml(step.original)}</p></details></div>
    </li>`).join("")}</ol>`;
}

function renderMethods(blocks, hasFulltext) {
  if (!blocks?.length) return `<div class="detail-empty">${hasFulltext ? "当前 PDF 文本层未定位到独立 Methods/Experimental Section。" : "尚未取得合法开放全文，暂无方法原文锚点。"}</div>`;
  return `<div class="method-blocks">${blocks.map((block, index) => `
    <details><summary><span>M${String(index + 1).padStart(3, "0")}</span> p.${Number(block.page || 0)}</summary><p>${escapeHtml(block.text)}</p></details>`).join("")}</div>`;
}

function renderFigures(figures, hasFulltext) {
  if (!figures?.length) return `<div class="detail-empty">${hasFulltext ? "未从 PDF 文本层可靠识别主图和图注。" : "尚未取得合法开放全文，暂无逐图解释。"}</div>`;
  return `<div class="paper-figures">${figures.map((figure) => `
    <figure class="paper-figure" id="${escapeHtml(figure.id)}">
      <div class="figure-head"><div><span>${escapeHtml(figure.id)}</span><h3>${escapeHtml(figure.label)}</h3></div><a href="#pdf">p.${Number(figure.page || 0)}</a></div>
      <img src="./${escapeHtml(figure.image_path)}" alt="${escapeHtml(figure.label)}" ${figure.image_width && figure.image_height ? `width="${Number(figure.image_width)}" height="${Number(figure.image_height)}"` : ""} loading="lazy" />
      <figcaption><strong>图注</strong><p>${escapeHtml(figure.caption_original)}</p>${figure.explanation_zh ? `<p class="figure-explanation">${escapeHtml(figure.explanation_zh)}</p>` : ""}<p class="figure-note">${escapeHtml(figure.reading_note_zh)}</p></figcaption>
      ${figure.panels?.length ? `<div class="panel-list">${figure.panels.map((panel) => `<div><b>(${escapeHtml(panel.label)})</b><p>${escapeHtml(panel.explanation_zh)}</p><small>${escapeHtml(panel.original)}</small></div>`).join("")}</div>` : ""}
      ${figure.crop_confidence === "approximate" ? `<p class="crop-warning">该图为近似裁图，精读时需复核边界。</p>` : ""}
    </figure>`).join("")}</div>`;
}

function renderPaper(paper, detail) {
  const source = safeUrl(paper.url || (paper.doi ? `https://doi.org/${paper.doi}` : ""));
  if (source) { sourceLink.href = source; sourceLink.hidden = false; }
  const pdf = detail
    ? safeUrl(detail.original_pdf ? new URL(detail.original_pdf, window.location.href).href : "")
    : safeUrl(paper.pdf_url || "");
  const hasFulltext = detail?.status === "fulltext_draft";
  const status = detail?.status === "fulltext_draft" ? "全文已解析" : "仅摘要级";
  detailRoot.innerHTML = `
    <section class="paper-title-band">
      <div class="tags"><span class="tag">${escapeHtml(paper.venue || "来源未标注")}</span><span class="tag">${escapeHtml(paper.primary_category || "柔性材料与器件")}</span>${paper.strongly_related ? '<span class="tag amber">强相关</span>' : '<span class="tag">相关</span>'}<span class="tag amber">${escapeHtml(status)}</span>${(paper.tracks || []).map((track) => `<span class="tag blue">${escapeHtml(track)}</span>`).join("")}</div>
      <h1>${escapeHtml(paper.title)}</h1>
      <p class="paper-detail-meta">${escapeHtml((paper.authors || []).join(", "))}<span>${escapeHtml(paper.date || "")}</span>${paper.doi ? `<span>DOI ${escapeHtml(paper.doi)}</span>` : ""}</p>
      <nav class="paper-section-nav"><a href="#summary">摘要</a><a href="#methods">制备步骤</a><a href="#figures">图解</a><a href="#pdf">PDF</a></nav>
    </section>

    <section id="summary" class="paper-detail-section">
      <div class="section-head"><div><p class="eyebrow">Paper brief</p><h2>摘要、创新点与课题启发</h2></div></div>
      <div class="paper-summary-grid">
        <article><h3>中文摘要</h3><p>${escapeHtml(detail?.abstract?.zh || paper.summary_zh || "等待摘要分析")}</p></article>
        <article><h3>创新点</h3>${list(detail?.innovation_points || [paper.core_claim].filter(Boolean))}</article>
        ${(detail?.innovation_suggestions || paper.innovation_suggestions || []).length ? `<article><h3>给你的创新建议</h3>${list(detail?.innovation_suggestions || paper.innovation_suggestions)}</article>` : ""}
        <article><h3>对你的启发</h3>${list(detail?.inspirations || paper.transferable_points)}</article>
      </div>
      <details class="abstract-original"><summary>查看原始摘要</summary><p>${escapeHtml(detail?.abstract?.original || paper.source_abstract || "未获取原始摘要")}</p></details>
    </section>

    <section id="methods" class="paper-detail-section">
      <div class="section-head"><div><p class="eyebrow">Methods and fabrication</p><h2>制备与实验步骤</h2></div></div>
      ${renderSteps(detail?.preparation_steps, hasFulltext)}
      <div class="section-head method-source-head"><div><p class="eyebrow">Source anchors</p><h2>方法原文锚点</h2></div></div>
      ${renderMethods(detail?.method_blocks, hasFulltext)}
    </section>

    <section id="figures" class="paper-detail-section">
      <div class="section-head"><div><p class="eyebrow">Figure-by-figure</p><h2>主图与分图解释</h2></div></div>
      ${renderFigures(detail?.figures, hasFulltext)}
    </section>

    <section id="pdf" class="paper-detail-section pdf-section">
      <div class="section-head"><div><p class="eyebrow">Lawful open-access source</p><h2>合法开放全文 PDF</h2><p class="pdf-version">${escapeHtml(detail?.pdf_version_label || "版本类型待核实")}</p></div>${pdf ? `<a class="secondary-btn" href="${escapeHtml(pdf)}" target="_blank" rel="noreferrer"><i data-lucide="download"></i><span>打开 PDF</span></a>` : ""}</div>
      ${pdf ? `<iframe class="pdf-frame" src="${escapeHtml(pdf)}#view=FitH" title="${escapeHtml(paper.title)} PDF"></iframe>` : `<div class="detail-empty">没有获取到合法开放获取 PDF，只保留 DOI/出版社来源。</div>`}
    </section>`;
  document.title = `${paper.title}｜论文精读`;
  window.lucide?.createIcons();
}

async function loadPaper() {
  const id = new URLSearchParams(window.location.search).get("id") || "";
  try {
    const bundle = await fetch("./data/research-bundle.json", { cache: "no-store" }).then((response) => response.json());
    const paper = (bundle.papers || []).find((item) => item.id === id);
    if (!paper) throw new Error("论文不存在或已不在当前日报中");
    let detail = null;
    if (paper.detail_json) {
      const response = await fetch(`./${paper.detail_json}`, { cache: "no-store" });
      if (response.ok) detail = await response.json();
    }
    renderPaper(paper, detail);
  } catch (error) {
    detailRoot.innerHTML = `<div class="detail-error"><h1>无法打开论文详情</h1><p>${escapeHtml(error.message)}</p><a class="primary-btn" href="./">返回论文列表</a></div>`;
  }
}

loadPaper();

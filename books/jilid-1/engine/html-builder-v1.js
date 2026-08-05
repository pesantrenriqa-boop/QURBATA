(() => {
  "use strict";

  function escapeHtml(value = "") {
    return String(value)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/\"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }

  function renderTargets(targets = {}) {
    return Object.entries(targets)
      .map(([key, value]) => `<div class="target-item"><span>${escapeHtml(key)}</span><strong>${escapeHtml(value)}</strong></div>`)
      .join("");
  }

  function renderPage(data, objectEngine, options = {}) {
    const title = (data.material_title || []).map(escapeHtml).join(" ");
    const objects = objectEngine.renderGroups(data.objects || {});

    return `<!doctype html>
<html lang="id">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>${escapeHtml(data.book || "QURBATA")}</title>
<link rel="stylesheet" href="${options.css || "../layout/master-layout-v1.css"}">
</head>
<body>
<main class="page" data-page-number="${escapeHtml(data.page)}">
<header class="header">
<div class="brand-block">QURBATA</div>
<div class="heading"><div class="subtitle">${escapeHtml(data.identity?.subtitle || "")}</div></div>
<div class="page-number">${escapeHtml(data.page)}</div>
</header>
<section class="targets">${renderTargets(data.targets)}</section>
<section class="material-title"><div class="material-title-text">${title}</div></section>
<section class="exercise-area">${objects}</section>
<footer class="footer"></footer>
</main>
<script src="${options.validator || "./layout-validator-v1.js"}"></script>
</body>
</html>`;
  }

  window.QurbataHtmlBuilder = Object.freeze({ renderPage });
})();

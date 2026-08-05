/**
 * QURBATA Page Renderer v1
 *
 * Purpose:
 * YAML page data -> HTML document structure
 *
 * This is the first renderer layer. It intentionally does not replace
 * the visual design system; it connects structured data with layout.
 */

import { renderObjectGroup } from './object-engine-v1.js';

function escapeHtml(value = '') {
  return String(value)
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#039;');
}

function renderTargets(targets = {}) {
  return Object.entries(targets)
    .map(([key, value]) => `
      <div class="target-item">
        <span>${escapeHtml(key)}</span>
        <strong>${escapeHtml(value)}</strong>
      </div>`)
    .join('');
}

function renderFooter(footer = {}) {
  return `
    <footer class="footer">
      <div class="field">${escapeHtml(footer.teacher_label || 'Guru')} <span class="line"></span></div>
      <div class="field">${escapeHtml(footer.score_label || 'Nilai')} <span class="line"></span></div>
      <div class="field">${escapeHtml(footer.date_label || 'Tanggal')} <span class="line"></span></div>
    </footer>`;
}

export function renderPage(page) {
  return `
<section class="page" data-page-number="${escapeHtml(page.page)}">
  <header class="header">
    <div class="brand-block">QURBATA</div>
    <div class="heading">
      <div class="subtitle">${escapeHtml(page.identity?.subtitle)}</div>
    </div>
    <div class="page-number">${escapeHtml(page.page)}</div>
  </header>

  <div class="targets">
    ${renderTargets(page.targets)}
  </div>

  <div class="material-title">
    <div class="material-title-text">
      ${(page.material_title || []).map(escapeHtml).join(' ')}
    </div>
  </div>

  <main class="exercise-area">
    <section class="exercise-section singles">
      <div class="group">
        ${renderObjectGroup('singles', page.objects?.singles || [])}
      </div>
    </section>
    <section class="exercise-section pairs">
      <div class="group">
        ${renderObjectGroup('pairs', page.objects?.pairs || [])}
      </div>
    </section>
    <section class="exercise-section triples">
      <div class="group">
        ${renderObjectGroup('triples', page.objects?.triples || [])}
      </div>
    </section>
  </main>

  ${renderFooter(page.footer)}
</section>`;
}

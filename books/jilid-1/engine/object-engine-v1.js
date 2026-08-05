/**
 * QURBATA Object Engine v1
 *
 * Purpose:
 * Convert canonical YAML page objects into renderer-ready HTML objects.
 *
 * Input concept:
 * {
 *   singles: ["بَ", "تَ"],
 *   pairs: [["بَ", "تَ"]],
 *   triples: [["بَ", "تَ", "ثَ"]]
 * }
 *
 * Output:
 * <div class="group singles">...
 */
(() => {
  "use strict";

  const TYPE_ORDER = ["singles", "pairs", "triples"];

  function escapeHTML(value) {
    return String(value)
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");
  }

  function normalizeObject(item) {
    if (Array.isArray(item)) {
      return item.map(escapeHTML).join("");
    }
    return escapeHTML(item);
  }

  function renderObject(item) {
    return `<div class="object"><span class="arabic-token"><span class="arabic-base">${normalizeObject(item)}</span></span></div>`;
  }

  function renderGroup(type, objects = []) {
    const safeObjects = Array.isArray(objects) ? objects : [];

    return `
      <section class="exercise-section ${type}">
        <div class="group">
          ${safeObjects.map(renderObject).join("\n")}
        </div>
      </section>`;
  }

  function renderExerciseArea(data = {}) {
    return `
      <div class="exercise-area">
        ${TYPE_ORDER.map((type) => renderGroup(type, data[type])).join("\n")}
      </div>`;
  }

  window.QurbataObjectEngine = Object.freeze({
    renderObject,
    renderGroup,
    renderExerciseArea
  });
})();

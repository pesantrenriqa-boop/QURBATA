(() => {
  "use strict";

  const DEFAULT_TOLERANCE_PX = 0.75;
  const SELECTORS = {
    page: ".page",
    guarded: [
      ".page",
      ".header",
      ".heading",
      ".targets",
      ".material-title",
      ".material-title-text",
      ".exercise-area",
      ".exercise-section",
      ".group",
      ".object",
      ".arabic-token",
      ".footer"
    ].join(",")
  };

  function numericDatasetValue(element, key, fallback) {
    const value = Number.parseFloat(element?.dataset?.[key] ?? "");
    return Number.isFinite(value) ? value : fallback;
  }

  function isStrictMode() {
    const root = document.documentElement;
    const params = new URLSearchParams(window.location.search);
    return root.dataset.layoutStrict === "true" || params.get("layoutStrict") === "true";
  }

  function overflowMetrics(element, tolerance) {
    const horizontal = element.scrollWidth - element.clientWidth;
    const vertical = element.scrollHeight - element.clientHeight;

    return {
      horizontal,
      vertical,
      overflowX: horizontal > tolerance,
      overflowY: vertical > tolerance
    };
  }

  function elementDescriptor(element) {
    const classes = [...element.classList].filter((name) => name !== "is-overflow");
    return {
      tag: element.tagName.toLowerCase(),
      id: element.id || null,
      classes,
      page: element.closest(SELECTORS.page)?.dataset?.pageNumber ?? null,
      text: (element.textContent || "").replace(/\s+/g, " ").trim().slice(0, 120)
    };
  }

  function validateElement(element, tolerance) {
    const metrics = overflowMetrics(element, tolerance);
    const failed = metrics.overflowX || metrics.overflowY;

    element.classList.toggle("is-overflow", failed);
    element.dataset.layoutOverflow = failed ? "true" : "false";

    if (!failed) {
      delete element.dataset.overflowX;
      delete element.dataset.overflowY;
      return null;
    }

    element.dataset.overflowX = metrics.horizontal.toFixed(2);
    element.dataset.overflowY = metrics.vertical.toFixed(2);

    return {
      ...elementDescriptor(element),
      overflowX: Number(metrics.horizontal.toFixed(2)),
      overflowY: Number(metrics.vertical.toFixed(2))
    };
  }

  function validateLayout(options = {}) {
    const root = document.documentElement;
    const tolerance = Number.isFinite(options.tolerance)
      ? options.tolerance
      : numericDatasetValue(root, "layoutTolerance", DEFAULT_TOLERANCE_PX);

    const elements = [...document.querySelectorAll(SELECTORS.guarded)];
    const failures = elements
      .map((element) => validateElement(element, tolerance))
      .filter(Boolean);

    const pages = [...document.querySelectorAll(SELECTORS.page)];
    const report = {
      ok: failures.length === 0,
      checkedAt: new Date().toISOString(),
      tolerance,
      pages: pages.length,
      elements: elements.length,
      failures
    };

    root.dataset.layoutStatus = report.ok ? "pass" : "fail";
    root.dataset.layoutFailureCount = String(failures.length);
    window.__QURBATA_LAYOUT_REPORT__ = report;
    window.dispatchEvent(new CustomEvent("qurbata:layout-validated", { detail: report }));

    if (!report.ok) {
      console.error("[QURBATA] Layout validation failed", report);
      if (options.throwOnFailure ?? isStrictMode()) {
        throw new Error(`QURBATA layout validation failed: ${failures.length} overflow(s)`);
      }
    } else {
      console.info("[QURBATA] Layout validation passed", report);
    }

    return report;
  }

  async function runWhenStable() {
    if (document.fonts?.ready) {
      await document.fonts.ready;
    }

    await new Promise((resolve) => requestAnimationFrame(() => requestAnimationFrame(resolve)));
    return validateLayout();
  }

  let resizeTimer = null;
  window.addEventListener("resize", () => {
    window.clearTimeout(resizeTimer);
    resizeTimer = window.setTimeout(() => validateLayout({ throwOnFailure: false }), 150);
  });

  window.QurbataLayoutValidator = Object.freeze({
    validate: validateLayout,
    runWhenStable
  });

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", runWhenStable, { once: true });
  } else {
    runWhenStable();
  }
})();

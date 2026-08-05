/*
 * QURBATA Production Test Runner v1
 *
 * Purpose:
 * - verify the production chain stages
 * - provide a stable report object before PDF pipeline exists
 *
 * Flow:
 * YAML -> Object Engine -> Page Renderer -> HTML Builder -> Validation
 */

(() => {
  "use strict";

  const REQUIRED_STAGES = [
    "yaml",
    "object-engine",
    "page-renderer",
    "html-builder",
    "layout-validator"
  ];

  function createReport(stages = {}) {
    const result = REQUIRED_STAGES.map((stage) => ({
      stage,
      passed: Boolean(stages[stage]),
      detail: stages[stage] || null
    }));

    return {
      engine: "QURBATA Production Engine",
      version: "v1-test",
      passed: result.every((item) => item.passed),
      stages: result,
      createdAt: new Date().toISOString()
    };
  }

  function runProductionTest(context = {}) {
    const report = createReport(context);

    window.__QURBATA_PRODUCTION_REPORT__ = report;

    if (report.passed) {
      console.info("[QURBATA] Production test passed", report);
    } else {
      console.warn("[QURBATA] Production test incomplete", report);
    }

    return report;
  }

  window.QurbataProductionTestRunner = Object.freeze({
    run: runProductionTest,
    stages: REQUIRED_STAGES
  });
})();

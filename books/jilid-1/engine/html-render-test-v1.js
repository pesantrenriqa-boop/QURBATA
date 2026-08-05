// QURBATA HTML Render Test v1
// Purpose: verify page generation flow before PDF production.

(function () {
  'use strict';

  function runRenderTest(pageData) {
    const required = [
      'identity',
      'targets',
      'material_title',
      'objects'
    ];

    const missing = required.filter((key) => !(key in pageData));

    const report = {
      engine: 'QURBATA HTML Render Test v1',
      passed: missing.length === 0,
      checked: required,
      missing,
      page: pageData.page ?? null,
      timestamp: new Date().toISOString()
    };

    window.__QURBATA_RENDER_TEST__ = report;

    if (!report.passed) {
      console.error('[QURBATA] Render test failed', report);
      throw new Error('QURBATA render test failed');
    }

    console.info('[QURBATA] Render test passed', report);
    return report;
  }

  window.QurbataRenderTest = Object.freeze({
    run: runRenderTest
  });
})();

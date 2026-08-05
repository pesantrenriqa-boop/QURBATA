/**
 * QURBATA Chromium Runner v1
 *
 * Production adapter contract for converting rendered HTML
 * into A5 PDF and proof images.
 *
 * The actual browser dependency is intentionally injected so
 * the engine remains testable in CI and local environments.
 */

(function (global) {
  'use strict';

  function createPdfTask(options = {}) {
    return {
      input: options.input || null,
      output: options.output || 'qurbata-proof.pdf',
      screenshot: options.screenshot || 'qurbata-proof.png',
      viewport: {
        width: 559,
        height: 794
      },
      pdf: {
        format: 'A5',
        landscape: false,
        printBackground: true,
        margin: {
          top: '0mm',
          right: '0mm',
          bottom: '0mm',
          left: '0mm'
        }
      }
    };
  }

  function validateTask(task) {
    const errors = [];

    if (!task.input) errors.push('missing_html_input');
    if (!task.output) errors.push('missing_pdf_output');
    if (!task.screenshot) errors.push('missing_screenshot_output');

    return {
      ok: errors.length === 0,
      errors
    };
  }

  global.QURBATA_CHROMIUM_RUNNER_V1 = {
    createPdfTask,
    validateTask
  };

})(typeof window !== 'undefined' ? window : globalThis);

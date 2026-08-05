/*
 * QURBATA PDF Production Pipeline v1
 *
 * Purpose:
 * Prepare the production contract from rendered HTML to printable PDF.
 *
 * This module defines the expected flow:
 * HTML -> Browser Renderer -> PDF A5 -> Proof Image
 *
 * Actual browser execution adapter can be connected later.
 */

(function(global){
  'use strict';

  function createJob(htmlPath, options = {}) {
    return {
      source: htmlPath,
      format: options.format || 'A5',
      orientation: options.orientation || 'portrait',
      printBackground: true,
      margin: options.margin || {
        top: '12mm',
        right: '12mm',
        bottom: '12mm',
        left: '12mm'
      },
      status: 'prepared'
    };
  }

  function validateJob(job) {
    const required = ['source', 'format', 'orientation'];
    const missing = required.filter(key => !job[key]);

    return {
      ok: missing.length === 0,
      missing,
      job
    };
  }

  global.QURBATA_PDF_PIPELINE = {
    createJob,
    validateJob
  };

})(typeof window !== 'undefined' ? window : globalThis);

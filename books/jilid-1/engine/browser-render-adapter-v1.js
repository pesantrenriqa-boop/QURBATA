/*
 * QURBATA Browser Render Adapter v1
 *
 * Contract layer between generated HTML and browser PDF engines.
 * This file intentionally keeps Chromium/Puppeteer implementation separate.
 */

const QURBATA_BROWSER_RENDER = {
  version: '1.0.0',

  createConfig(options = {}) {
    return {
      format: 'A5',
      landscape: false,
      printBackground: true,
      preferCSSPageSize: true,
      margin: {
        top: '0mm',
        right: '0mm',
        bottom: '0mm',
        left: '0mm'
      },
      ...options
    };
  },

  validate(html) {
    if (!html || typeof html !== 'string') {
      return { ok: false, error: 'HTML source is required' };
    }

    const required = ['<!doctype', 'qurbata'];
    const missing = required.filter(item => !html.toLowerCase().includes(item));

    return {
      ok: missing.length === 0,
      missing
    };
  },

  buildJob(htmlPath, outputPath, options = {}) {
    return {
      input: htmlPath,
      output: outputPath,
      pdf: this.createConfig(options),
      createdAt: new Date().toISOString()
    };
  }
};

if (typeof module !== 'undefined') {
  module.exports = QURBATA_BROWSER_RENDER;
}

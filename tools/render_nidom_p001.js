const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

(async () => {
  const root = path.resolve(__dirname, '..');
  const html = path.join(root, 'books/nidom-akhlak/jilid-1/page-001.html');
  const outDir = path.join(root, 'dist/nidom-akhlak');
  fs.mkdirSync(outDir, { recursive: true });
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 1331, height: 1890 }, deviceScaleFactor: 2 });
  await page.goto('file://' + html, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  const ok = await page.evaluate(() => document.fonts.check('32px "KFGQPC Uthman Taha Naskh"', 'أَفْشُوا السَّلَامَ بَيْنَكُمْ'));
  if (!ok) throw new Error('UTHMAN_TAHA_FONT_NOT_ACTIVE');
  const info = await page.evaluate(() => {
    const e = document.querySelector('.hadith-ar');
    const cs = getComputedStyle(e);
    const sig = document.querySelector('.signatures').getBoundingClientRect();
    const footer = document.querySelector('.footer').getBoundingClientRect();
    const nidom = document.querySelector('.nidom').getBoundingClientRect();
    return { family: cs.fontFamily, dir: cs.direction, text: e.textContent.trim(), width: e.getBoundingClientRect().width, height: e.getBoundingClientRect().height, nidomBottom: nidom.bottom, signaturesBottom: sig.bottom, footerTop: footer.top };
  });
  if (info.signaturesBottom > info.footerTop - 8) throw new Error('SIGNATURE_FOOTER_COLLISION');
  console.log('ARABIC_RENDER_CHECK=' + JSON.stringify(info));
  await page.screenshot({ path: path.join(outDir, 'QURBATA-NIDOM-J1-P001-v0.5.png'), fullPage: true });
  await page.pdf({
    path: path.join(outDir, 'QURBATA-NIDOM-J1-P001-v0.5.pdf'),
    width: '176mm',
    height: '250mm',
    printBackground: true,
    margin: { top: '0', right: '0', bottom: '0', left: '0' }
  });
  await browser.close();
})();

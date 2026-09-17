import fs from "node:fs/promises";
import path from "node:path";

const root = path.resolve(import.meta.dirname, "..");
const htmlPath = path.join(root, "dist/QURBATA-J1-P011-P020-AUDIT.html");
let html = await fs.readFile(htmlPath, "utf8");

const override = `
<style id="p011-p020-final-layout-audit">
/* HARD GATE P011-P020: exactly one A5 PDF page per meeting after v1.3 overlay. */
.book-page { break-after: page !important; page-break-after: always !important; overflow: hidden !important; }
.book-page:last-child { break-after: auto !important; page-break-after: auto !important; }
.lesson-heading h1 { font-size: 17pt !important; line-height: .96 !important; }
.lesson-heading h1 .arabic-title { font-size: 20pt !important; margin-top: .2mm !important; line-height: .95 !important; }
.lesson-heading p { margin: .25mm 3mm 0 !important; font-size: 6pt !important; line-height: 1 !important; max-width: 96%; }

.book-page.has-intro {
  grid-template-rows: 7mm 18mm 24mm 13mm minmax(0,1fr) 23mm 7mm !important;
  gap: 1mm !important;
}
.intro-strip { padding: .45mm 2mm !important; grid-template-columns: 22mm 1fr !important; gap: 1mm !important; overflow: hidden !important; min-height: 0 !important; }
.intro-strip strong { font-size: 6pt !important; line-height: 1 !important; }
.intro-items { display:grid !important; grid-template-columns:repeat(2,minmax(0,1fr)); grid-template-rows:repeat(2,1fr); align-items:center; justify-items:center; gap:.1mm 1.2mm !important; min-width:0; min-height:0; }
.intro-items:has(.intro-pair:nth-child(5)) { grid-template-columns:repeat(5,minmax(0,1fr)); grid-template-rows:repeat(2,1fr); gap:.05mm .4mm !important; }
.intro-pair { font-size: 12.5pt !important; line-height:.9 !important; }
.intro-items:has(.intro-pair:nth-child(5)) .intro-pair { font-size:10.2pt !important; }

.book-page.has-intro .integration-grid { gap:1mm !important; min-height:0 !important; overflow:hidden !important; }
.book-page.has-intro .integration-card { grid-template-rows:5mm 3.6mm minmax(0,1fr) 4.8mm !important; min-height:0 !important; overflow:hidden !important; }
.book-page.has-intro .integration-card h2 { padding:.8mm .5mm !important; font-size:6.5pt !important; line-height:1 !important; }
.book-page.has-intro .integration-title { margin:.35mm .5mm 0 !important; font-size:5.2pt !important; line-height:1 !important; }
.book-page.has-intro .integration-arabic { font-size:10pt !important; line-height:1 !important; padding:0 .35mm !important; overflow:hidden !important; }
.book-page.has-intro .integration-instruction { margin:0 .5mm .4mm !important; padding:.3mm !important; font-size:4.9pt !important; line-height:1 !important; overflow:hidden !important; }

.book-page.checkpoint .lesson-heading h1 { font-size:16pt !important; }
.book-page.checkpoint .lesson-heading h1 .arabic-title { font-size:19pt !important; }
.book-page.checkpoint .lesson-heading p { font-size:5.8pt !important; }

/* Tartil remains the dominant flexible zone. */
.book-page.has-intro .practice-panel { min-height:0 !important; overflow:hidden !important; }
.book-page.has-intro .practice-panel > header { padding:0 2.5mm !important; }
.book-page.has-intro .practice-panel h2 { font-size:9.2pt !important; }
.book-page.has-intro .practice-panel header p { font-size:6pt !important; line-height:1 !important; }
.book-page.has-intro .practice-grid { min-height:0 !important; height:calc(100% - 8mm) !important; grid-template-rows:repeat(8,minmax(0,1fr)) !important; overflow:hidden !important; }
.book-page.has-intro .practice-row { min-height:0 !important; }
.book-page.has-intro .practice-cell { font-size:20.5pt !important; line-height:.9 !important; min-height:0 !important; padding:.2mm !important; }

/* Teacher zone v1.2: blank writing space ABOVE Tanggal/Nilai/TTD labels. */
.book-page.has-intro .activity-strip { height:23mm !important; min-height:23mm !important; margin-top:0 !important; padding:.8mm 2.2mm .8mm !important; align-self:stretch !important; overflow:hidden !important; }
.book-page.has-intro .activity-content { grid-template-rows:auto 1fr !important; min-height:0 !important; }
.book-page.has-intro .activity-content h2 { margin:0 0 .25mm !important; font-size:6.8pt !important; line-height:1 !important; }
.book-page.has-intro .study-fields { height:11.5mm !important; min-height:11.5mm !important; margin-top:0 !important; gap:1.6mm !important; align-items:end !important; font-size:5.3pt !important; }
.book-page.has-intro .study-fields span,
.book-page.has-intro .study-fields span:last-child { height:11.5mm !important; min-height:11.5mm !important; display:flex !important; align-items:flex-end !important; justify-content:center !important; border-top:0 !important; border-bottom:.3mm solid #7da4b6 !important; padding:0 0 .4mm !important; }
.book-page.has-intro .qr-link img { width:11.5mm !important; height:11.5mm !important; }
.book-page.has-intro .page-footer { min-height:0 !important; overflow:hidden !important; }
.book-page.has-intro .page-footer p { margin-top:.5mm !important; font-size:5.4pt !important; line-height:1 !important; }
</style>`;

html = html.replace(/<style id="p011-p020-final-layout-audit">[\s\S]*?<\/style>\s*/g, "");
html = html.replace("</head>", `${override}\n</head>`);
await fs.writeFile(htmlPath, html);
console.log("Applied hardened P011-P020 one-page-per-meeting layout gate for v1.3.");
import fs from "node:fs/promises";
import path from "node:path";

const root = path.resolve(import.meta.dirname, "..");
const htmlPath = path.join(root, "dist/QURBATA-J1-P011-P020-AUDIT.html");
let html = await fs.readFile(htmlPath, "utf8");

const override = `
<style id="p011-p020-final-layout-audit">
/* P011-P020 FINAL PAGINATION GATE — applies to normal, intro, and checkpoint pages. */
.book-page {
  box-sizing:border-box !important;
  height:239mm !important;
  min-height:239mm !important;
  max-height:239mm !important;
  break-after:page !important;
  page-break-after:always !important;
  overflow:hidden !important;
  grid-template-rows:7mm 18mm 24mm minmax(0,1fr) 23mm 7mm !important;
  gap:1mm !important;
}
.book-page:last-child{break-after:auto !important;page-break-after:auto !important;}
.book-page.has-intro{grid-template-rows:7mm 18mm 24mm 12mm minmax(0,1fr) 23mm 7mm !important;}
.book-page.checkpoint{grid-template-rows:7mm 18mm 22mm 22mm minmax(0,1fr) 23mm 7mm !important;}

.lesson-heading{min-height:0 !important;overflow:hidden !important;}
.lesson-heading h1{font-size:16pt !important;line-height:.94 !important;margin:0 !important;}
.lesson-heading h1 .arabic-title{font-size:19pt !important;margin-top:.15mm !important;line-height:.94 !important;}
.lesson-heading p{margin:.2mm 3mm 0 !important;font-size:5.8pt !important;line-height:1 !important;max-width:96%;}

.integration-grid{gap:1mm !important;min-height:0 !important;overflow:hidden !important;}
.integration-card{grid-template-rows:4.8mm 3.3mm minmax(0,1fr) 4.5mm !important;min-height:0 !important;overflow:hidden !important;}
.integration-card h2{padding:.7mm .45mm !important;font-size:6.2pt !important;line-height:1 !important;}
.integration-title{margin:.3mm .45mm 0 !important;font-size:5pt !important;line-height:1 !important;}
.integration-arabic{font-size:9.5pt !important;line-height:.98 !important;padding:0 .3mm !important;overflow:hidden !important;}
.integration-instruction{margin:0 .45mm .3mm !important;padding:.25mm !important;font-size:4.7pt !important;line-height:1 !important;overflow:hidden !important;}

.intro-strip{padding:.35mm 1.8mm !important;grid-template-columns:21mm 1fr !important;gap:.8mm !important;overflow:hidden !important;min-height:0 !important;}
.intro-strip strong{font-size:5.7pt !important;line-height:1 !important;}
.intro-items{display:grid !important;grid-template-columns:repeat(2,minmax(0,1fr));grid-template-rows:repeat(2,1fr);align-items:center;justify-items:center;gap:.05mm 1mm !important;min-width:0;min-height:0;}
.intro-items:has(.intro-pair:nth-child(5)){grid-template-columns:repeat(5,minmax(0,1fr));grid-template-rows:repeat(2,1fr);gap:.03mm .3mm !important;}
.intro-pair{font-size:11.5pt !important;line-height:.88 !important;}
.intro-items:has(.intro-pair:nth-child(5)) .intro-pair{font-size:9.4pt !important;}

.checkpoint-strip{padding:.6mm 1.5mm !important;gap:.3mm !important;min-height:0 !important;overflow:hidden !important;}
.checkpoint-strip h2{font-size:6.5pt !important;line-height:1 !important;}
.checkpoint-letters{gap:.5mm 1.8mm !important;font-size:11.5pt !important;line-height:.9 !important;overflow:hidden !important;}
.checkpoint-harakat{font-size:5.5pt !important;line-height:1 !important;}
.checkpoint-harakat .arabic{font-size:9pt !important;margin:0 .8mm !important;}

/* Tartil remains the largest/flexible learning area. */
.practice-panel{min-height:0 !important;overflow:hidden !important;}
.practice-panel>header{padding:0 2.2mm !important;min-height:0 !important;}
.practice-panel h2{font-size:8.8pt !important;line-height:1 !important;}
.practice-panel header p{font-size:5.7pt !important;line-height:1 !important;}
.practice-grid{min-height:0 !important;height:calc(100% - 7mm) !important;grid-template-rows:repeat(8,minmax(0,1fr)) !important;overflow:hidden !important;}
.practice-row{min-height:0 !important;overflow:hidden !important;}
.practice-cell{font-size:20pt !important;line-height:.88 !important;min-height:0 !important;padding:.1mm !important;overflow:hidden !important;}

/* Teacher work zone: writing/signature space ABOVE labels, never below. */
.activity-strip{height:23mm !important;min-height:23mm !important;max-height:23mm !important;margin-top:0 !important;padding:.7mm 2mm .7mm !important;align-self:stretch !important;overflow:hidden !important;}
.activity-content{grid-template-rows:auto 1fr !important;min-height:0 !important;overflow:hidden !important;}
.activity-content h2{margin:0 0 .2mm !important;font-size:6.5pt !important;line-height:1 !important;}
.study-fields{height:11mm !important;min-height:11mm !important;margin-top:0 !important;gap:1.5mm !important;align-items:end !important;font-size:5.1pt !important;}
.study-fields span,.study-fields span:last-child{height:11mm !important;min-height:11mm !important;display:flex !important;align-items:flex-end !important;justify-content:center !important;border-top:0 !important;border-bottom:.3mm solid #7da4b6 !important;padding:0 0 .35mm !important;}
.qr-link img{width:11mm !important;height:11mm !important;}
.page-footer{min-height:0 !important;overflow:hidden !important;}
.page-footer p{margin-top:.35mm !important;font-size:5.2pt !important;line-height:1 !important;}
.page-footer small{font-size:4.7pt !important;line-height:1 !important;}
</style>`;

html=html.replace(/<style id="p011-p020-final-layout-audit">[\s\S]*?<\/style>\s*/g,"");
html=html.replace("</head>",`${override}\n</head>`);
await fs.writeFile(htmlPath,html);
console.log("Applied P011-P020 pagination gate to normal + intro + checkpoint pages.");
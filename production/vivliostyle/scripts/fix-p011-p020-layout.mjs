import fs from "node:fs/promises";
import path from "node:path";

const root = path.resolve(import.meta.dirname, "..");
const htmlPath = path.join(root, "dist/QURBATA-J1-P011-P020-AUDIT.html");
let html = await fs.readFile(htmlPath, "utf8");

const override = `
<style id="p011-p020-final-layout-audit">
/* P011-P020 pagination gate: preserve all v1.3 content inside one A5 page per meeting. */
.lesson-heading h1 { font-size: 18pt !important; line-height: 1 !important; }
.lesson-heading h1 .arabic-title { font-size: 22pt !important; margin-top: .4mm !important; line-height: 1 !important; }
.lesson-heading p { margin: .5mm 3mm 0 !important; font-size: 6.5pt !important; line-height: 1.02 !important; max-width: 96%; }

/* Kasrah planting remains a real teaching zone, but the whole fixed grid must fit 250mm. */
.book-page.has-intro {
  grid-template-rows: 8mm 20mm 27mm 16mm minmax(0, 1fr) 25mm 8mm !important;
  gap: 1.4mm !important;
}
.intro-strip {
  padding: .8mm 2.2mm !important;
  grid-template-columns: 25mm 1fr !important;
  gap: 1.5mm !important;
  overflow: hidden;
}
.intro-strip strong { font-size: 6.7pt !important; line-height: 1.08 !important; }
.intro-items {
  display: grid !important;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  grid-template-rows: repeat(2, 1fr);
  align-items: center;
  justify-items: center;
  gap: .25mm 2mm !important;
  min-width: 0;
}
.intro-items:has(.intro-pair:nth-child(5)) {
  grid-template-columns: repeat(5, minmax(0, 1fr));
  grid-template-rows: repeat(2, 1fr);
  gap: .15mm .7mm !important;
}
.intro-pair { font-size: 14pt !important; line-height: .95 !important; }
.intro-items:has(.intro-pair:nth-child(5)) .intro-pair { font-size: 11.8pt !important; }

/* Integration v1.3 retains Arabic + Indonesian meaning; compact typography prevents overflow. */
.book-page.has-intro .integration-grid { gap: 1.4mm !important; min-height: 0 !important; }
.book-page.has-intro .integration-card {
  grid-template-rows: 6mm 4.5mm minmax(0,1fr) 5.5mm !important;
  min-height: 0 !important;
}
.book-page.has-intro .integration-card h2 { padding: 1.2mm .7mm !important; font-size: 7.2pt !important; }
.book-page.has-intro .integration-title { margin: .7mm .7mm 0 !important; font-size: 5.8pt !important; line-height: 1 !important; }
.book-page.has-intro .integration-arabic { font-size: 11.2pt !important; line-height: 1.05 !important; padding: 0 .5mm !important; }
.book-page.has-intro .integration-instruction { margin: 0 .7mm .7mm !important; padding: .5mm !important; font-size: 5.5pt !important; line-height: 1.05 !important; }

/* Checkpoint heading also stays contained. */
.book-page.checkpoint .lesson-heading h1 { font-size: 17pt !important; }
.book-page.checkpoint .lesson-heading h1 .arabic-title { font-size: 21pt !important; }
.book-page.checkpoint .lesson-heading p { font-size: 6.3pt !important; }

/* Tartil remains dominant; example text is large but does not collide with cell lines. */
.book-page.has-intro .practice-panel { min-height: 0 !important; }
.book-page.has-intro .practice-panel > header { padding: 0 3mm !important; }
.book-page.has-intro .practice-panel h2 { font-size: 10pt !important; }
.book-page.has-intro .practice-panel header p { font-size: 6.8pt !important; }
.book-page.has-intro .practice-cell { font-size: 22pt !important; line-height: .95 !important; }

/* Teacher zone: blank writing space is ABOVE Tanggal/Nilai/TTD labels. */
.book-page.has-intro .activity-strip {
  min-height: 25mm !important;
  margin-top: 0 !important;
  padding: 1.2mm 2.5mm 1.2mm !important;
  align-self: stretch !important;
}
.book-page.has-intro .activity-content { grid-template-rows: auto 1fr !important; }
.book-page.has-intro .activity-content h2 { margin: 0 0 .5mm !important; font-size: 7.5pt !important; }
.book-page.has-intro .study-fields {
  height: 13mm !important;
  min-height: 13mm !important;
  margin-top: .2mm !important;
  gap: 2mm !important;
  align-items: end !important;
  font-size: 5.8pt !important;
}
.book-page.has-intro .study-fields span,
.book-page.has-intro .study-fields span:last-child {
  height: 13mm !important;
  min-height: 13mm !important;
  display: flex !important;
  align-items: flex-end !important;
  justify-content: center !important;
  border-top: 0 !important;
  border-bottom: .3mm solid #7da4b6 !important;
  padding: 0 0 .6mm !important;
}
.book-page.has-intro .qr-link img { width: 13mm !important; height: 13mm !important; }
.book-page.has-intro .page-footer p { margin-top: 1.2mm !important; }
</style>`;

html = html.replace("</head>", `${override}\n</head>`);
await fs.writeFile(htmlPath, html);
console.log("Applied P011-P020 one-page-per-meeting layout gate for v1.3.");
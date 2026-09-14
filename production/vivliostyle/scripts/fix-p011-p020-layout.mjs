import fs from "node:fs/promises";
import path from "node:path";

const root = path.resolve(import.meta.dirname, "..");
const htmlPath = path.join(root, "dist/QURBATA-J1-P011-P020-AUDIT.html");
let html = await fs.readFile(htmlPath, "utf8");

const override = `
<style id="p011-p020-final-layout-audit">
/* Gate correction: heading text must stay inside its box after Uthman Taha embedding. */
.lesson-heading h1 { font-size: 18pt !important; line-height: 1 !important; }
.lesson-heading h1 .arabic-title { font-size: 22pt !important; margin-top: .4mm !important; line-height: 1 !important; }
.lesson-heading p { margin: .6mm 3mm 0 !important; font-size: 6.7pt !important; line-height: 1.05 !important; max-width: 96%; }

/* Kasrah planting is a real two-row teaching zone, not a tiny decorative strip. */
.book-page.has-intro { grid-template-rows: 8mm 22mm 29mm 18mm 1fr 22mm 11mm !important; }
.intro-strip {
  padding: 1mm 2.5mm !important;
  grid-template-columns: 27mm 1fr !important;
  gap: 2mm !important;
  overflow: hidden;
}
.intro-strip strong { font-size: 7pt !important; line-height: 1.15; }
.intro-items {
  display: grid !important;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  grid-template-rows: repeat(2, 1fr);
  align-items: center;
  justify-items: center;
  gap: .4mm 3mm !important;
  min-width: 0;
}
.intro-items:has(.intro-pair:nth-child(5)) {
  grid-template-columns: repeat(5, minmax(0, 1fr));
  grid-template-rows: repeat(2, 1fr);
  gap: .2mm 1mm !important;
}
.intro-pair { font-size: 15pt !important; line-height: 1 !important; }
.intro-items:has(.intro-pair:nth-child(5)) .intro-pair { font-size: 12.5pt !important; }

/* Checkpoint heading also stays contained. */
.book-page.checkpoint .lesson-heading h1 { font-size: 17pt !important; }
.book-page.checkpoint .lesson-heading h1 .arabic-title { font-size: 21pt !important; }
.book-page.checkpoint .lesson-heading p { font-size: 6.5pt !important; }

/* Preserve dominant reading area and compact learning record. */
.book-page.has-intro .practice-cell { font-size: 21.5pt !important; }
.book-page.has-intro .activity-strip { padding-top: 1.8mm !important; padding-bottom: 1.8mm !important; }
.book-page.has-intro .page-footer p { margin-top: 1.5mm !important; }
</style>`;

html = html.replace("</head>", `${override}\n</head>`);
await fs.writeFile(htmlPath, html);
console.log("Applied P011-P020 final layout audit corrections.");

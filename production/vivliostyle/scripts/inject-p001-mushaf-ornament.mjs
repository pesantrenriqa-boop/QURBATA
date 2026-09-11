import fs from "node:fs/promises";
import path from "node:path";

const root = path.resolve(import.meta.dirname, "..");
const file = path.join(root, "dist-p001", "index.html");
let html = await fs.readFile(file, "utf8");

const ornamentCss = `
/* QURBATA Mushaf Ornament Layer v2 — organic arabesque, spacious and deterministic */
.page{
  position:relative;
  border:.42mm solid #b89543 !important;
  outline:.22mm solid #1b5a49 !important;
  outline-offset:-1.9mm !important;
  box-shadow:
    inset 0 0 0 .36mm #f1e3b8,
    inset 0 0 0 .68mm #fffaf0;
  background:linear-gradient(180deg,#fffef9 0%,#fffdf7 52%,#fffaf0 100%) !important;
}
.mushaf-ornaments{
  position:absolute;
  inset:1.2mm;
  width:calc(100% - 2.4mm);
  height:calc(100% - 2.4mm);
  pointer-events:none;
  z-index:19;
  overflow:visible;
}
.mushaf-ornaments .gold{stroke:#c5a14d;fill:none;stroke-linecap:round;stroke-linejoin:round}
.mushaf-ornaments .green{stroke:#1b5a49;fill:none;stroke-linecap:round;stroke-linejoin:round}
.mushaf-ornaments .fill-gold{fill:#d0ae59}
.mushaf-ornaments .fill-green{fill:#1b5a49}
.mushaf-ornaments .soft{opacity:.72}
.head,.meta,.practice,.panels,.foot{position:relative;z-index:2}
.head{
  border:0 !important;
  border-bottom:.28mm solid #c6a14d !important;
  border-radius:0 !important;
  background:linear-gradient(90deg,transparent 0%,#fff8e6 22%,#f8ebc7 50%,#fff8e6 78%,transparent 100%) !important;
  box-shadow:none !important;
}
.vol{
  position:relative;
  background:#185443;
  color:#fffaf0;
  border:.25mm solid #c9a855;
  border-radius:48% 48% 16% 16% / 28% 28% 12% 12%;
  padding:1.05mm 2.4mm;
  margin:0 4mm;
  box-shadow:0 .35mm .8mm rgba(49,62,47,.10);
}
.num{
  border:.3mm solid #bd9947 !important;
  border-radius:45% 45% 12% 12% / 22% 22% 10% 10%;
  background:#fffaf0;
  box-shadow:inset 0 0 0 .18mm #efe0b5 !important;
}
.competency,.letters,.panel{
  border:.24mm solid #c8ad69 !important;
  border-radius:1.4mm;
  box-shadow:none !important;
  background:linear-gradient(145deg,#fffefa 0%,#fffaf0 100%) !important;
}
.practice{
  border:.28mm solid #bea05d !important;
  border-radius:1.3mm;
  box-shadow:none !important;
  background:rgba(255,254,249,.96) !important;
}
.r{border-top:.18mm solid #d8c58d !important}
.c{border-left:.18mm solid #d8c58d !important}
.panel h3{
  display:inline-block;
  padding:.15mm 1.2mm .35mm;
  border-bottom:.2mm solid #c8a858;
}
.foot{
  border-top:.25mm solid #c5a55d !important;
  background:linear-gradient(90deg,transparent,#fff7df 22%,#fff7df 78%,transparent) !important;
}
.assessment{
  padding-top:.35mm;
  border-top:.16mm solid #dfcb91 !important;
}
`;

const ornamentSvg = `
<svg class="mushaf-ornaments" viewBox="0 0 664 944" preserveAspectRatio="none" aria-hidden="true">
  <defs>
    <g id="cornerArabesque">
      <path class="gold soft" stroke-width="1.25" d="M7 72 C12 42, 25 22, 55 9 C39 22, 35 40, 43 56 C51 72, 66 72, 78 59 C67 83, 48 91, 31 82 C18 75, 13 69, 7 72Z"/>
      <path class="green soft" stroke-width="1.05" d="M11 82 C30 73, 40 57, 38 39 C37 28, 30 20, 23 15 M42 57 C54 45, 67 39, 83 40"/>
      <path class="gold" stroke-width="1" d="M18 57 C26 51, 31 42, 30 31 C40 38, 46 48, 44 59 C42 68, 35 76, 26 79"/>
      <path class="green" stroke-width=".9" d="M53 19 C61 28, 64 39, 60 50 C70 45, 78 46, 87 52"/>
      <path class="gold" stroke-width=".9" d="M19 92 C34 90, 47 95, 56 106 C58 91, 66 80, 79 73"/>
      <circle class="fill-gold" cx="40" cy="60" r="2.25"/>
      <path class="fill-green" d="M56 29 C62 34,65 40,63 47 C57 45,52 41,49 35 C50 31,52 30,56 29Z"/>
      <path class="fill-gold" d="M25 76 C31 71,37 70,43 73 C39 79,34 83,27 84 C24 82,23 79,25 76Z"/>
    </g>
    <g id="topMedallion">
      <path class="gold" stroke-width="1.1" d="M-34 2 C-22 -8,-10 -8,0 0 C10 -8,22 -8,34 2 C22 7,12 11,0 18 C-12 11,-22 7,-34 2Z"/>
      <path class="green" stroke-width=".9" d="M-23 2 C-14 1,-7 5,0 12 C7 5,14 1,23 2"/>
      <path class="fill-gold" d="M0 -3 l4 5 -4 5 -4 -5Z"/>
    </g>
  </defs>

  <use href="#cornerArabesque" x="0" y="0"/>
  <use href="#cornerArabesque" transform="translate(664 0) scale(-1 1)"/>
  <use href="#cornerArabesque" transform="translate(0 944) scale(1 -1)"/>
  <use href="#cornerArabesque" transform="translate(664 944) scale(-1 -1)"/>

  <g transform="translate(332 10)"><use href="#topMedallion"/></g>
  <g transform="translate(332 934) scale(1 -1)"><use href="#topMedallion"/></g>

  <path class="gold soft" stroke-width=".75" d="M92 11 C160 7,220 7,288 11 M376 11 C444 7,504 7,572 11"/>
  <path class="green soft" stroke-width=".55" d="M105 15 C166 12,222 12,282 15 M382 15 C442 12,498 12,559 15"/>
  <path class="gold soft" stroke-width=".75" d="M92 933 C160 937,220 937,288 933 M376 933 C444 937,504 937,572 933"/>

  <path class="gold soft" stroke-width=".65" d="M11 120 C7 240,7 330,11 430 M11 514 C7 614,7 704,11 824"/>
  <path class="gold soft" stroke-width=".65" d="M653 120 C657 240,657 330,653 430 M653 514 C657 614,657 704,653 824"/>

  <g transform="translate(11 472)">
    <path class="green soft" stroke-width=".8" d="M0 -16 C8 -11,12 -5,12 0 C12 5,8 11,0 16 C-8 11,-12 5,-12 0 C-12 -5,-8 -11,0 -16Z"/>
    <path class="gold" stroke-width=".75" d="M-7 0 C-3 -4,3 -4,7 0 C3 4,-3 4,-7 0Z"/>
  </g>
  <g transform="translate(653 472)">
    <path class="green soft" stroke-width=".8" d="M0 -16 C8 -11,12 -5,12 0 C12 5,8 11,0 16 C-8 11,-12 5,-12 0 C-12 -5,-8 -11,0 -16Z"/>
    <path class="gold" stroke-width=".75" d="M-7 0 C-3 -4,3 -4,7 0 C3 4,-3 4,-7 0Z"/>
  </g>
</svg>`;

// Remove the v1 rigid ornament layer if a previously built HTML is being postprocessed again.
html = html.replace(/\/\* QURBATA Mushaf Ornament Layer - deterministic, no AI artwork \*\/[\s\S]*?(?=<\/style>)/, "");

if (!html.includes("QURBATA Mushaf Ornament Layer v2")) {
  html = html.replace("</style>", `${ornamentCss}\n</style>`);
}
if (!html.includes('class="mushaf-ornaments"')) {
  html = html.replace('<article class="page">', `<article class="page">${ornamentSvg}`);
}

await fs.writeFile(file, html, "utf8");
console.log("QJ1-P001 organic mushaf arabesque layer injected -> dist-p001/index.html");
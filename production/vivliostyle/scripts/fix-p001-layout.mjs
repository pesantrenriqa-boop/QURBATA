import fs from "node:fs/promises";
import path from "node:path";

const root = path.resolve(import.meta.dirname, "..");
const file = path.join(root, "dist-p001/index.html");
let html = await fs.readFile(file, "utf8");

const replacements = [
  ["grid-template-rows:12mm 17mm minmax(0,1fr) 22mm 7mm", "grid-template-rows:12mm 17mm minmax(0,1fr) 20.5mm 9.5mm"],
  ["gap:1.5mm;border:1.2mm double", "gap:1.2mm;border:1.2mm double"],
  ["padding:.7mm 2mm 0;font-size:5.4pt", "padding:.45mm 2mm 0;font-size:4.8pt"],
  [".foot b{font-size:6.7pt}", ".foot b{font-size:5.9pt}"],
  [".motto{font-family:Uthmani;font-size:8.5pt}", ".motto{font-family:Uthmani;font-size:7.5pt}"],
  ["column-gap:3mm;row-gap:.6mm", "column-gap:2.4mm;row-gap:.35mm"],
  ["grid-template-columns:1.15fr .8fr 1fr;gap:4mm", "grid-template-columns:1.15fr .75fr 1fr;gap:3mm"],
  ["min-width:16mm;border-bottom:.2mm solid #8f7b48;height:2.5mm", "min-width:14mm;border-bottom:.2mm solid #8f7b48;height:1.7mm"]
];

for (const [from, to] of replacements) {
  if (!html.includes(from)) throw new Error(`P001 layout patch target not found: ${from}`);
  html = html.replace(from, to);
}

await fs.writeFile(file, html);
console.log("QJ1-P001 compact footer layout applied; page remains single-sheet target.");

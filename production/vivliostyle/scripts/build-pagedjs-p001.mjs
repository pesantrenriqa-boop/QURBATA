import fs from "node:fs/promises";
import path from "node:path";

const root=path.resolve(import.meta.dirname,"..");
const out=path.join(root,"dist/QURBATA-J1-P001-PAGEDJS.html");
const exercises=["بَ تَ","ثَ ثَ","بَ بَ","تَ ثَ","ثَ تَ","ثَ بَ","بَ ثَ","تَ بَ","تَ تَ تَ","ثَ ثَ تَ","تَ ثَ بَ","تَ بَ ثَ","بَ ثَ ثَ","بَ ثَ بَ","بَ ثَ تَ","بَ بَ بَ","تَ تَ ثَ","تَ ثَ ثَ","ثَ بَ تَ","ثَ ثَ بَ","ثَ تَ تَ","بَ تَ تَ","بَ بَ ثَ","تَ تَ بَ"];
const cells=exercises.map(x=>`<div class="cell" dir="rtl">${x}</div>`).join("");
const html=`<!doctype html><html lang="id"><head><meta charset="utf-8"><title>QURBATA P001 Paged.js</title>
<style>
@font-face{font-family:Uthman;src:url("./fonts/KFGQPC-Uthman-Taha-Naskh.woff2") format("woff2");}
@page{size:A5 portrait;margin:7mm;}
*{box-sizing:border-box}html,body{margin:0;padding:0}
.page{width:134mm;height:196mm;overflow:hidden;display:grid;grid-template-rows:18mm 22mm 34mm 1fr 16mm;gap:2mm;font-family:Arial,sans-serif;color:#14384c;break-after:page}
.header{display:grid;grid-template-columns:1fr auto;align-items:center;border-bottom:.5mm solid #9bc9dc}
.header h1{font-size:16pt;margin:0}.code{font-size:7pt;font-weight:700}
.plant{display:flex;align-items:center;justify-content:center;border:.35mm solid #9bc9dc;border-radius:3mm;background:#f7fcfe}
.ar{font-family:Uthman,serif;direction:rtl}.plant .ar{font-size:38pt;line-height:1}
.integrations{display:grid;grid-template-columns:repeat(3,1fr);gap:1.5mm}
.card{border:.3mm solid #b6d5e1;border-radius:2.5mm;padding:1.2mm;overflow:hidden;text-align:center}
.card b{display:block;font-size:7pt}.card .ar{font-size:12.5pt;line-height:1.15;margin:.7mm 0}.card small{font-size:5.5pt;line-height:1.05;display:block}
.practice{display:grid;grid-template-rows:6mm 1fr;border:.35mm solid #8dbed2;border-radius:3mm;overflow:hidden}
.practice-title{display:flex;align-items:center;justify-content:space-between;padding:0 2mm;font-size:7pt;font-weight:700;background:#f4fbfd}
.grid{display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:repeat(8,1fr);min-height:0}
.cell{font-family:Uthman,serif;font-size:25pt;line-height:1;display:flex;align-items:center;justify-content:center;border-top:.2mm solid #c7dfe8;border-left:.2mm solid #c7dfe8;white-space:nowrap;overflow:hidden;padding:.2mm}
.footer{display:grid;grid-template-columns:17mm 1fr 1fr 1fr 16mm;gap:1.2mm;align-items:end;font-size:6pt}
.id{align-self:center;text-align:center;font-weight:700}.field{height:13mm;border-bottom:.3mm solid #7db4ca;display:flex;align-items:flex-end;justify-content:center;padding-bottom:1mm}.brand{text-align:center;align-self:center;font-weight:700;font-size:6pt}
</style></head><body>
<article class="page">
<header class="header"><div><h1>Mari Membaca</h1><div class="ar" style="font-size:17pt">بَ تَ ثَ</div></div><div class="code">QJ1-P001</div></header>
<section class="plant"><div class="ar">بَ تَ ثَ</div></section>
<section class="integrations">
<div class="card"><b>TAHFIDZ · An-Nas 1</b><div class="ar">قُلْ أَعُوذُ بِرَبِّ النَّاسِ</div><small>Aku berlindung kepada Tuhan manusia.</small></div>
<div class="card"><b>BI'AH ARABIYAH · Salam</b><div class="ar">السَّلَامُ عَلَيْكُمْ</div><small>Gunakan saat bertemu guru dan teman.</small></div>
<div class="card"><b>AKHLAK · Adab Salam</b><div class="ar">أَفْشُوا السَّلَامَ بَيْنَكُمْ</div><small>Biasakan menyebarkan salam.</small></div>
</section>
<section class="practice"><div class="practice-title"><span>LATIHAN TARTIL</span><span>8 baris × 3 kelompok</span></div><div class="grid">${cells}</div></section>
<footer class="footer"><div class="id">QJ1-P001</div><div class="field">Tanggal</div><div class="field">Nilai</div><div class="field">TTD</div><div class="brand"><span class="ar">تَعَلَّمْ<br>اِعْمَلْ<br>عَلِّمْ</span><br>RIQA OS</div></footer>
</article></body></html>`;
if(exercises.length!==24)throw new Error("P001 must have 24 exercises");
await fs.mkdir(path.dirname(out),{recursive:true});await fs.writeFile(out,html);
console.log("Built Paged.js P001 HTML: fixed A5, 24 exercises, frozen P001 content.");

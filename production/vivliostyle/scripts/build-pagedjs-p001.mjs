import fs from "node:fs/promises";
import path from "node:path";
import QRCode from "qrcode";

const root=path.resolve(import.meta.dirname,"..");
const out=path.join(root,"dist/QURBATA-J1-P001-PAGEDJS.html");
const exercises=["بَ تَ","ثَ ثَ","بَ بَ","تَ ثَ","ثَ تَ","ثَ بَ","بَ ثَ","تَ بَ","تَ تَ تَ","ثَ ثَ تَ","تَ ثَ بَ","تَ بَ ثَ","بَ ثَ ثَ","بَ ثَ بَ","بَ ثَ تَ","بَ بَ بَ","تَ تَ ثَ","تَ ثَ ثَ","ثَ بَ تَ","ثَ ثَ بَ","ثَ تَ تَ","بَ تَ تَ","بَ بَ ثَ","تَ تَ بَ"];
if(exercises.length!==24||exercises.some(x=>!/[\u0600-\u06FF]/.test(x)))throw new Error("P001 practice gate failed");
const qr=await QRCode.toDataURL("https://rumahilmualquran.com",{margin:0,width:128});
const cells=exercises.map(x=>`<div class="cell" dir="rtl">${x}</div>`).join("");
const html=`<!doctype html><html lang="id"><head><meta charset="utf-8"><title>QURBATA P001 Paged.js</title><style>
@font-face{font-family:Uthman;src:url("./fonts/KFGQPC-Uthman-Taha-Naskh.woff2") format("woff2")}
@page{size:A5 portrait;margin:5mm}*{box-sizing:border-box}html,body{margin:0;padding:0;background:#fffdf8}
.page{position:relative;width:138mm;height:200mm;padding:3.5mm;overflow:hidden;display:grid;grid-template-rows:15mm 21mm 28mm 1fr 17mm;gap:1.7mm;font-family:Arial,sans-serif;color:#173b52;border:.35mm solid #d9b968;break-after:page;background:linear-gradient(180deg,#fffefa,#fff)}
.page:before,.page:after{content:"";position:absolute;width:18mm;height:18mm;border-color:#d9b968;pointer-events:none}
.page:before{left:1.3mm;top:1.3mm;border-left:.7mm double #d9b968;border-top:.7mm double #d9b968;border-radius:5mm 0 0 0}
.page:after{right:1.3mm;bottom:1.3mm;border-right:.7mm double #d9b968;border-bottom:.7mm double #d9b968;border-radius:0 0 5mm 0}
.ar{font-family:Uthman,serif;direction:rtl}.header{display:grid;grid-template-columns:27mm 1fr 24mm;align-items:center;border-bottom:.3mm solid #d9b968;padding:0 2mm}
.logo{font-weight:800;font-size:11pt;letter-spacing:.4mm}.logo small{display:block;font-size:4.8pt;font-weight:500;letter-spacing:0}
.header h1{text-align:center;font-size:17pt;margin:0}.code{text-align:center;border:.25mm solid #e2ca8d;border-radius:5mm;padding:1.5mm;font-size:7pt;font-weight:700;background:#fff8e8}
.plant{display:flex;align-items:center;justify-content:center;border:.4mm solid #77b7d2;border-radius:4mm;background:linear-gradient(90deg,#f7fcff,#eef8fc,#f7fcff);box-shadow:inset 0 0 0 .5mm #fff}
.plant .ar{font-size:42pt;line-height:1}
.integrations{display:grid;grid-template-columns:repeat(3,1fr);gap:1.4mm}.card{border:.3mm solid #b8d5df;border-radius:3mm;padding:1.2mm;text-align:center;overflow:hidden;background:#fff}.card:nth-child(1){background:#f6fbf4}.card:nth-child(2){background:#fffaf0}.card:nth-child(3){background:#fff7f3}
.card b{display:block;font-size:6.3pt}.card .ar{font-size:13pt;line-height:1.15;margin:.7mm 0}.card small{font-size:5.5pt;line-height:1.1;display:block}
.practice{display:grid;grid-template-rows:6.5mm 1fr;border:.4mm solid #70b3d0;border-radius:3.5mm;overflow:hidden;background:#fff}
.practice-title{display:flex;align-items:center;justify-content:space-between;padding:0 2mm;font-size:6.5pt;font-weight:700;background:linear-gradient(90deg,#e9f6fb,#fff8e9)}
.practice-title strong{font-size:9pt}.grid{display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:repeat(8,1fr);min-height:0}
.cell{font-family:Uthman,serif;font-size:27pt;line-height:.95;display:flex;align-items:center;justify-content:center;border-top:.2mm solid #c4dfe9;border-left:.2mm solid #c4dfe9;white-space:nowrap;overflow:hidden}
.footer{position:relative;z-index:1;display:grid;grid-template-columns:19mm 1fr 1fr 1fr 18mm;gap:1.4mm;align-items:center;border:.3mm solid #e2ca8d;border-radius:3mm;padding:1.2mm 1.8mm;background:#fffdfa;font-size:5.8pt}
.id{text-align:center;font-weight:700}.field{height:9mm;border-bottom:.25mm dotted #7995a5;display:flex;align-items:flex-end;justify-content:center;padding-bottom:.7mm}.qr{text-align:center;font-size:5pt;font-weight:700}.qr img{display:block;width:9mm;height:9mm;margin:auto}.motto{position:absolute;bottom:1.2mm;left:50%;transform:translateX(-50%);font-family:Uthman,serif;font-size:6pt;color:#9c7b34;white-space:nowrap}
</style></head><body><article class="page">
<header class="header"><div class="logo">QURBATA<small>Quran · Bahasa Arab · Tahfidz · Akhlak</small></div><h1>Mari Membaca</h1><div class="code">QJ1-P001</div></header>
<section class="plant"><div class="ar">بَ تَ ثَ</div></section>
<section class="integrations">
<div class="card"><b>TAHFIDZ · An-Nas 1</b><div class="ar">قُلْ أَعُوذُ بِرَبِّ النَّاسِ</div><small>Katakanlah, “Aku berlindung kepada Tuhan manusia.”</small></div>
<div class="card"><b>BI'AH ARABIYAH · Salam</b><div class="ar">السَّلَامُ عَلَيْكُمْ</div><small>Semoga keselamatan tercurah atas kalian.</small></div>
<div class="card"><b>AKHLAK · Adab Salam</b><div class="ar">أَفْشُوا السَّلَامَ بَيْنَكُمْ</div><small>Sebarkanlah salam di antara kalian.</small></div>
</section>
<section class="practice"><div class="practice-title"><strong>LATIHAN TARTIL</strong><span>8 baris × 3 kelompok</span></div><div class="grid">${cells}</div></section>
<footer class="footer"><div class="id">QJ1-P001</div><div class="field">Tanggal</div><div class="field">Nilai</div><div class="field">TTD</div><div class="qr"><img src="${qr}">RIQA OS</div></footer>
<div class="motto">تَعَلَّمْ — اِعْمَلْ — عَلِّمْ</div></article></body></html>`;
await fs.mkdir(path.dirname(out),{recursive:true});await fs.writeFile(out,html);
console.log("Built ornamental Paged.js P001 master: A5, 24 Arabic cells, translations, QR, fixed footer.");

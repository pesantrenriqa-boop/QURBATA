import fs from "node:fs/promises";
import path from "node:path";

const root = path.resolve(import.meta.dirname, "..");
const file = path.join(root, "dist-p001", "index.html");
let html = await fs.readFile(file, "utf8");

const ornamentCss = `
/* QURBATA Mushaf Ornament Layer - deterministic, no AI artwork */
.page{
  position:relative;
  border:1.05mm solid #0f5a48 !important;
  outline:.32mm solid #c7a34d !important;
  outline-offset:-2.25mm !important;
  box-shadow:
    inset 0 0 0 .55mm #f8edc9,
    inset 0 0 0 .9mm #c7a34d,
    inset 0 0 0 1.35mm #0f5a48,
    inset 0 0 0 1.65mm #e8d394;
  background:
    radial-gradient(circle at 3mm 3mm, transparent 0 1.25mm, #c7a34d 1.3mm 1.55mm, transparent 1.6mm),
    radial-gradient(circle at calc(100% - 3mm) 3mm, transparent 0 1.25mm, #c7a34d 1.3mm 1.55mm, transparent 1.6mm),
    radial-gradient(circle at 3mm calc(100% - 3mm), transparent 0 1.25mm, #c7a34d 1.3mm 1.55mm, transparent 1.6mm),
    radial-gradient(circle at calc(100% - 3mm) calc(100% - 3mm), transparent 0 1.25mm, #c7a34d 1.3mm 1.55mm, transparent 1.6mm),
    linear-gradient(#fffef9,#fffaf0) !important;
}
.page::before{
  content:"";
  position:absolute;
  inset:1.45mm;
  pointer-events:none;
  z-index:20;
  border:.28mm solid #d4b45d;
  background:
    repeating-linear-gradient(45deg,#0f5a48 0 .45mm,#0f5a48 .45mm .8mm,#d5b85f .8mm 1.05mm,#fff7db 1.05mm 1.5mm) top / 100% 1.65mm no-repeat,
    repeating-linear-gradient(45deg,#0f5a48 0 .45mm,#0f5a48 .45mm .8mm,#d5b85f .8mm 1.05mm,#fff7db 1.05mm 1.5mm) bottom / 100% 1.65mm no-repeat,
    repeating-linear-gradient(-45deg,#0f5a48 0 .45mm,#0f5a48 .45mm .8mm,#d5b85f .8mm 1.05mm,#fff7db 1.05mm 1.5mm) left / 1.65mm 100% no-repeat,
    repeating-linear-gradient(-45deg,#0f5a48 0 .45mm,#0f5a48 .45mm .8mm,#d5b85f .8mm 1.05mm,#fff7db 1.05mm 1.5mm) right / 1.65mm 100% no-repeat;
}
.page::after{
  content:"◆";
  position:absolute;
  top:1.9mm;
  left:50%;
  transform:translateX(-50%);
  width:8mm;
  height:4mm;
  line-height:3.6mm;
  text-align:center;
  font-size:6pt;
  color:#d2b057;
  background:#0f5a48;
  border:.3mm solid #d2b057;
  border-radius:45% 45% 55% 55%;
  z-index:21;
}
.head,.meta,.practice,.panels,.foot{position:relative;z-index:2}
.head{
  border:.35mm solid #c5a24f !important;
  border-radius:2mm 2mm .9mm .9mm;
  background:linear-gradient(90deg,#fffdf3 0%,#f8edcb 50%,#fffdf3 100%);
  box-shadow:inset 0 0 0 .25mm #f2dfaa;
}
.vol{
  background:#0f5a48;
  color:#fffaf0;
  border:.3mm solid #c9aa57;
  border-radius:50% 50% 12% 12% / 24% 24% 14% 14%;
  padding:1.2mm 2mm;
  margin:0 4mm;
  text-shadow:0 .2mm 0 rgba(0,0,0,.16);
}
.num{
  border:.45mm double #b99642 !important;
  background:#fffaf0;
  box-shadow:inset 0 0 0 .3mm #f2dfaa;
}
.competency,.letters,.panel{
  border:.32mm solid #c3a253 !important;
  box-shadow:inset 0 0 0 .22mm #f0dfae;
  background:linear-gradient(135deg,#fffefa 0%,#fff9e8 100%) !important;
}
.practice{
  border:.45mm double #b99747 !important;
  box-shadow:inset 0 0 0 .2mm #eee0b5;
  background:#fffef9;
}
.r{border-top:.22mm solid #c9ae65 !important}
.c{border-left:.22mm solid #c9ae65 !important}
.panel h3{
  display:inline-block;
  padding:.3mm 1.4mm .45mm;
  border-bottom:.25mm solid #c6a44f;
}
.foot{
  border-top:.38mm double #b99747 !important;
  background:linear-gradient(90deg,transparent,#fff5d8 18%,#fff5d8 82%,transparent);
}
.assessment{
  padding-top:.45mm;
  border-top:.2mm solid #ddc887;
}
`;

if (!html.includes("QURBATA Mushaf Ornament Layer")) {
  html = html.replace("</style>", `${ornamentCss}\n</style>`);
  await fs.writeFile(file, html, "utf8");
}

console.log("QJ1-P001 mushaf ornament layer injected -> dist-p001/index.html");
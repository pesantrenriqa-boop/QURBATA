const fs=require('fs');
const p='tools/render_nidom_j3_v01.js';
let s=fs.readFileSync(p,'utf8');
if(!s.includes('J3_LOGO_BASELINE_V02')){
  s=s.replace(".head{height:15mm;border-bottom:.35mm solid #b8a66e;display:flex;justify-content:space-between;font-size:8pt;font-weight:700}",".head{height:15mm;border-bottom:.35mm solid #b8a66e;display:grid;grid-template-columns:11mm 1fr 12mm;gap:4mm;align-items:start}.logo{width:10mm;height:11mm;object-fit:contain}.headtxt{font-size:7pt;font-weight:700;color:#5f705d;padding-top:1mm}.num{height:12mm;background:#405d49;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:800;border-radius:0 0 2.5mm 2.5mm}");
  s=s.replace('function html(p,font){','function html(p,font,logo){');
  s=s.replace('<div class=head><span>QURBATA NIDOM · JILID 3 · BEGINNER 2</span><span>${String(p.n).padStart(2,\'0\')}</span></div>','<div class=head><img class=logo src="data:image/svg+xml;base64,${logo}"><div class=headtxt>QURBATA NIDOM · JILID 3 · BEGINNER 2</div><div class=num>${String(p.n).padStart(2,\'0\')}</div></div>');
  s=s.replace("const font=fs.readFileSync(fp).toString('base64');const b=await chromium.launch", "const font=fs.readFileSync(fp).toString('base64');const lp=path.resolve(__dirname,'../books/shared/assets/qurbata-logo.svg');if(!fs.existsSync(lp))throw Error('LOGO_MISSING');const logo=fs.readFileSync(lp).toString('base64');const b=await chromium.launch");
  s=s.replace('await pg.setContent(html(p,font));','await pg.setContent(html(p,font,logo));');
  s += "\n// J3_LOGO_BASELINE_V02\n";
}
// Typography v0.3: larger, still hierarchical and guarded by overflow gate.
s=s.replace('.title{font-size:17pt;', '.title{font-size:19pt;');
s=s.replace('.ar{font-size:21pt;', '.ar{font-size:24pt;');
s=s.replace('.tr{font-size:8pt}', '.tr{font-size:9pt}');
s=s.replace('.src{font-size:6.5pt;', '.src{font-size:7pt;');
s=s.replace('font-size:8.5pt;line-height:1.5', 'font-size:9.5pt;line-height:1.48');
s=s.replace('.w{font-size:14pt}', '.w{font-size:16pt}');
s=s.replace('.m{font-size:6pt}', '.m{font-size:7pt}');
s=s.replace('.headtxt{font-size:7pt;', '.headtxt{font-size:7.5pt;');
s += "\n// J3_TYPOGRAPHY_V03_LARGER_PROPORTIONAL\n";
fs.writeFileSync(p,s);
console.log('J3_LOGO_BASELINE_V02=READY');
console.log('J3_TYPOGRAPHY_V03=LARGER_PROPORTIONAL');
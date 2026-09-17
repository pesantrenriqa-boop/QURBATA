import fs from 'node:fs/promises';

const files=['P001-P010','P011-P020','P021-P030','P031-P040'].map(x=>`dist/QURBATA-J1-${x}-AUDIT.html`);

const css=`<style id="j1-layout-v14">
/* FROZEN v1.4.3 — proportional footer INSIDE every printed page. */
.activity-content>h2{display:none!important;}
.activity-strip:not(:has(.study-fields)){display:none!important;}
.audit-meta,.audit-footer,.page-register-meta,.debug-meta{display:none!important;}
.qurbata-footer-v143{display:grid!important;grid-template-columns:9fr 21fr 14fr 23fr 11fr 22fr!important;column-gap:1mm!important;align-items:center!important;width:100%!important;height:18mm!important;min-height:18mm!important;max-height:18mm!important;margin-top:.7mm!important;padding:0!important;box-sizing:border-box!important;break-inside:avoid!important;overflow:hidden!important;font-family:Arial,sans-serif!important;color:#12415c!important;}
.qf-id{display:flex!important;align-items:center!important;justify-content:center!important;height:7mm!important;border-radius:4mm!important;background:#dff2fb!important;font-weight:700!important;font-size:6pt!important;white-space:nowrap!important;min-width:0!important;}
.qf-field{display:grid!important;grid-template-rows:4.5mm 11mm!important;gap:.5mm!important;min-width:0!important;height:16mm!important;align-self:center!important;}
.qf-label{font-size:6pt!important;font-weight:600!important;line-height:4.5mm!important;padding-left:.8mm!important;white-space:nowrap!important;overflow:hidden!important;}
.qf-box{height:11mm!important;min-height:11mm!important;border:.28mm solid #73b8db!important;border-radius:2.4mm!important;background:#fff!important;box-sizing:border-box!important;position:relative!important;overflow:hidden!important;}
.qf-box:after{content:'················';position:absolute!important;left:1.5mm!important;right:1.5mm!important;bottom:1.1mm!important;text-align:center!important;letter-spacing:.2mm!important;color:#1473a8!important;font-size:5.7pt!important;white-space:nowrap!important;overflow:hidden!important;}
.qf-qr{display:flex!important;align-items:center!important;justify-content:center!important;min-width:0!important;height:17mm!important;padding:1mm!important;background:#fff!important;box-sizing:border-box!important;overflow:hidden!important;}
.qf-qr img,.qf-qr svg,.qf-qr canvas{display:block!important;position:static!important;float:none!important;width:14mm!important;height:14mm!important;max-width:14mm!important;max-height:14mm!important;margin:0!important;object-fit:contain!important;}
.qf-brand{display:flex!important;flex-direction:column!important;align-items:center!important;justify-content:center!important;gap:.45mm!important;min-width:0!important;height:17mm!important;text-align:center!important;overflow:hidden!important;}
.qf-brand-ar{font-family:'KFGQPC Uthman Taha Naskh','KFGQPCUthmanTahaNaskh',serif!important;font-size:9.5pt!important;line-height:1.05!important;color:#0870ad!important;white-space:nowrap!important;}
.qf-brand-id{font-size:4.7pt!important;line-height:1.05!important;white-space:nowrap!important;color:#12618d!important;}
.qf-brand-os{font-size:6.8pt!important;line-height:1!important;font-weight:700!important;letter-spacing:.35px!important;color:#075f92!important;white-space:nowrap!important;}
.qurbata-footer-v143~.page-footer,.qurbata-footer-v143~.footer,.qurbata-footer-v143~.book-footer{display:none!important;}
.practice-panel{min-height:0!important;overflow:visible!important;}
.practice-grid{grid-template-rows:repeat(8,minmax(0,1fr))!important;gap:.7mm!important;min-height:0!important;overflow:visible!important;}
.practice-row{min-height:0!important;overflow:visible!important;}
.practice-cell{font-size:25pt!important;line-height:1.08!important;padding:.55mm .35mm!important;overflow:visible!important;}
.planting .arabic,.intro-pair,.lesson-heading .arabic-title{font-size:24pt!important;line-height:1.08!important;}
.integration-card{padding-bottom:.4mm!important;}
.integration-arabic{line-height:1.12!important;padding:.5mm .6mm!important;}
.integration-meaning,.integration-instruction{line-height:1.12!important;padding:.35mm .55mm!important;}
</style>`;

function stripTechnicalText(html){
 html=html.replace(/<[^>]+class=["'][^"']*(?:audit-meta|audit-footer|page-register-meta|debug-meta)[^"']*["'][^>]*>[\s\S]*?<\/[^>]+>/gi,'');
 html=html.replace(/AUDIT\s*[—-][^<\n]*/gi,'');
 html=html.replace(/(?:03_BOOKS|PAGE_REGISTER)[^<\n]*/gi,'');
 return html;
}

function getQr(html){
 const m=html.match(/<img[^>]+src=["'][^"']*(?:qr|QR|qrcode|riqa)[^"']*["'][^>]*>/i);
 return m?m[0]:'';
}

function footer(pageNo,qr){
 const id=`QJ1-P${String(pageNo).padStart(3,'0')}`;
 return `<div class="qurbata-footer-v143" data-qurbata-footer="${id}">
 <div class="qf-id">${id}</div>
 <div class="qf-field"><div class="qf-label">Tanggal:</div><div class="qf-box"></div></div>
 <div class="qf-field"><div class="qf-label">Nilai:</div><div class="qf-box"></div></div>
 <div class="qf-field"><div class="qf-label">TTD:</div><div class="qf-box"></div></div>
 <div class="qf-qr">${qr}</div>
 <div class="qf-brand"><div class="qf-brand-ar" dir="rtl">تَعَلَّمْ – اِعْمَلْ – عَلِّمْ</div><div class="qf-brand-id">Belajar, Mengamalkan, Mengajarkan</div><div class="qf-brand-os">RIQA OS</div></div>
 </div>`;
}

function normalizeArticle(article,pageNo){
 const qr=getQr(article);
 let one=article;
 one=one.replace(/<section class="activity-strip">[\s\S]*?<\/section>/gi,'');
 one=one.replace(/<div class=["']study-fields["'][^>]*>[\s\S]*?<\/div>/gi,'');
 one=one.replace(/<div class=["']qurbata-footer-v14[23]["'][^>]*>[\s\S]*?<\/div>\s*<\/div>\s*<\/div>\s*<\/div>\s*<\/div>\s*<\/div>/gi,'');
 one=one.replace(/<[^>]+class=["'][^"']*(?:page-footer|book-footer|footer)[^"']*["'][^>]*>[\s\S]*?<\/[^>]+>/gi,'');
 const f=footer(pageNo,qr);
 /* Footer MUST be inside the article. */
 one=one.replace(/<\/article>\s*$/i,`${f}</article>`);
 return one;
}

for(const file of files){
 let html=await fs.readFile(file,'utf8');
 html=html.replace(/<style id="j1-layout-v14">[\s\S]*?<\/style>\s*/g,'');
 html=stripTechnicalText(html);
 let pageCounter=Number(file.match(/P(\d{3})-/)?.[1]||1);
 html=html.replace(/<article\b[^>]*>[\s\S]*?<\/article>/gi,(article)=>normalizeArticle(article,pageCounter++));
 html=html.replace('</head>',`${css}\n</head>`);
 /* Build assertions required by FROZEN v1.4.3. */
 const footers=(html.match(/class="qurbata-footer-v143"/g)||[]).length;
 const dates=(html.match(/Tanggal:/g)||[]).length;
 const scores=(html.match(/Nilai:/g)||[]).length;
 const signs=(html.match(/TTD:/g)||[]).length;
 if(footers!==10||dates<10||scores<10||signs<10) throw new Error(`${file}: FOOTER_ASSERT_FAIL footers=${footers} tanggal=${dates} nilai=${scores} ttd=${signs}`);
 if(/AUDIT\s*[—-]|PAGE_REGISTER|03_BOOKS/.test(html)) throw new Error(`${file}: PRINTED_TECHNICAL_METADATA_FAIL`);
 await fs.writeFile(file,html);
}
console.log('Applied J1 v1.4.3: proportional per-page footer with mandatory Tanggal/Nilai/TTD and build assertions.');
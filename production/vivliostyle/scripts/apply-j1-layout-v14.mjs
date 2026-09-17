import fs from 'node:fs/promises';

const files=['P001-P010','P011-P020','P021-P030','P031-P040'].map(x=>`dist/QURBATA-J1-${x}-AUDIT.html`);

const css=`<style id="j1-layout-v14">
/* FROZEN v1.5 — use the page for learning: large planting + large Tartil + compact footer. */
.activity-content>h2{display:none!important;}
.activity-strip:not(:has(.study-fields)){display:none!important;}
.audit-meta,.audit-footer,.page-register-meta,.debug-meta{display:none!important;}

/* The page itself becomes a controlled vertical learning system. */
article,.page,.lesson-page{box-sizing:border-box!important;overflow:hidden!important;}
article{display:grid!important;grid-template-rows:auto auto minmax(0,1fr) auto 16mm!important;align-content:stretch!important;row-gap:1.2mm!important;}

/* New competency / planting is intentionally large. */
.planting,.intro-pair,.lesson-heading{min-height:0!important;margin-top:0!important;margin-bottom:0!important;overflow:visible!important;}
.planting .arabic,.intro-pair,.lesson-heading .arabic-title{font-size:34pt!important;line-height:1.12!important;padding:.8mm .5mm!important;overflow:visible!important;}

/* Tartil is the flexible dominant area: no dead vertical block below it. */
.practice-panel{height:100%!important;min-height:0!important;margin:0!important;overflow:visible!important;display:flex!important;flex-direction:column!important;}
.practice-grid{flex:1 1 auto!important;height:100%!important;min-height:0!important;display:grid!important;grid-template-rows:repeat(8,minmax(0,1fr))!important;gap:.9mm!important;overflow:visible!important;}
.practice-row{height:100%!important;min-height:0!important;overflow:visible!important;}
.practice-cell{font-size:31pt!important;line-height:1.12!important;padding:.9mm .5mm!important;min-height:0!important;overflow:visible!important;display:flex!important;align-items:center!important;justify-content:center!important;}

/* Supporting domains stay readable but compact. */
.integration-panel,.integration-grid{margin:0!important;min-height:0!important;}
.integration-card{padding:.5mm .7mm!important;min-height:0!important;}
.integration-arabic{line-height:1.12!important;padding:.35mm .5mm!important;}
.integration-meaning,.integration-instruction{line-height:1.1!important;padding:.25mm .45mm!important;}

/* Compact official footer: one row, mandatory administration. */
.qurbata-footer-v15{display:grid!important;grid-template-columns:9fr 21fr 14fr 23fr 11fr 22fr!important;column-gap:.8mm!important;align-items:center!important;width:100%!important;height:16mm!important;min-height:16mm!important;max-height:16mm!important;margin:0!important;padding:0!important;box-sizing:border-box!important;break-inside:avoid!important;overflow:hidden!important;font-family:Arial,sans-serif!important;color:#12415c!important;}
.qf-id{display:flex!important;align-items:center!important;justify-content:center!important;height:6.5mm!important;border-radius:3.5mm!important;background:#dff2fb!important;font-weight:700!important;font-size:5.8pt!important;white-space:nowrap!important;min-width:0!important;}
.qf-field{display:grid!important;grid-template-rows:4mm 9.5mm!important;gap:.35mm!important;min-width:0!important;height:14mm!important;align-self:center!important;}
.qf-label{font-size:5.7pt!important;font-weight:600!important;line-height:4mm!important;padding-left:.7mm!important;white-space:nowrap!important;overflow:hidden!important;}
.qf-box{height:9.5mm!important;min-height:9.5mm!important;border:.28mm solid #73b8db!important;border-radius:2.2mm!important;background:#fff!important;box-sizing:border-box!important;position:relative!important;overflow:hidden!important;}
.qf-box:after{content:'··············';position:absolute!important;left:1.2mm!important;right:1.2mm!important;bottom:.9mm!important;text-align:center!important;color:#1473a8!important;font-size:5.4pt!important;white-space:nowrap!important;overflow:hidden!important;}
.qf-qr{display:flex!important;align-items:center!important;justify-content:center!important;min-width:0!important;height:15mm!important;padding:1mm!important;background:#fff!important;box-sizing:border-box!important;overflow:hidden!important;}
.qf-qr img,.qf-qr svg,.qf-qr canvas{display:block!important;position:static!important;float:none!important;width:13mm!important;height:13mm!important;max-width:13mm!important;max-height:13mm!important;margin:0!important;object-fit:contain!important;}
.qf-brand{display:flex!important;flex-direction:column!important;align-items:center!important;justify-content:center!important;gap:.35mm!important;min-width:0!important;height:15mm!important;text-align:center!important;overflow:hidden!important;}
.qf-brand-ar{font-family:'KFGQPC Uthman Taha Naskh','KFGQPCUthmanTahaNaskh',serif!important;font-size:9pt!important;line-height:1!important;color:#0870ad!important;white-space:nowrap!important;}
.qf-brand-id{font-size:4.5pt!important;line-height:1!important;white-space:nowrap!important;color:#12618d!important;}
.qf-brand-os{font-size:6.4pt!important;line-height:1!important;font-weight:700!important;color:#075f92!important;white-space:nowrap!important;}
</style>`;

function stripTechnicalText(html){
 html=html.replace(/<[^>]+class=["'][^"']*(?:audit-meta|audit-footer|page-register-meta|debug-meta)[^"']*["'][^>]*>[\s\S]*?<\/[^>]+>/gi,'');
 html=html.replace(/AUDIT\s*[—-][^<\n]*/gi,'');
 html=html.replace(/(?:03_BOOKS|PAGE_REGISTER)[^<\n]*/gi,'');
 return html;
}
function getQr(html){const m=html.match(/<img[^>]+src=["'][^"']*(?:qr|QR|qrcode|riqa)[^"']*["'][^>]*>/i);return m?m[0]:'';}
function footer(pageNo,qr){const id=`QJ1-P${String(pageNo).padStart(3,'0')}`;return `<div class="qurbata-footer-v15" data-qurbata-footer="${id}"><div class="qf-id">${id}</div><div class="qf-field"><div class="qf-label">Tanggal:</div><div class="qf-box"></div></div><div class="qf-field"><div class="qf-label">Nilai:</div><div class="qf-box"></div></div><div class="qf-field"><div class="qf-label">TTD:</div><div class="qf-box"></div></div><div class="qf-qr">${qr}</div><div class="qf-brand"><div class="qf-brand-ar" dir="rtl">تَعَلَّمْ – اِعْمَلْ – عَلِّمْ</div><div class="qf-brand-id">Belajar, Mengamalkan, Mengajarkan</div><div class="qf-brand-os">RIQA OS</div></div></div>`;}
function normalizeArticle(article,pageNo){
 const qr=getQr(article);let one=article;
 one=one.replace(/<section class="activity-strip">[\s\S]*?<\/section>/gi,'');
 one=one.replace(/<div class=["']study-fields["'][^>]*>[\s\S]*?<\/div>/gi,'');
 one=one.replace(/<div class=["']qurbata-footer-v(?:142|143|15)["'][^>]*>[\s\S]*?<\/div>\s*<\/div>\s*<\/div>\s*<\/div>\s*<\/div>\s*<\/div>/gi,'');
 one=one.replace(/<[^>]+class=["'][^"']*(?:page-footer|book-footer|footer)[^"']*["'][^>]*>[\s\S]*?<\/[^>]+>/gi,'');
 return one.replace(/<\/article>\s*$/i,`${footer(pageNo,qr)}</article>`);
}
for(const file of files){
 let html=await fs.readFile(file,'utf8');
 html=html.replace(/<style id="j1-layout-v14">[\s\S]*?<\/style>\s*/g,'');html=stripTechnicalText(html);
 let pageCounter=Number(file.match(/P(\d{3})-/)?.[1]||1);
 html=html.replace(/<article\b[^>]*>[\s\S]*?<\/article>/gi,a=>normalizeArticle(a,pageCounter++));
 html=html.replace('</head>',`${css}\n</head>`);
 const footers=(html.match(/class="qurbata-footer-v15"/g)||[]).length;
 const dates=(html.match(/Tanggal:/g)||[]).length,scores=(html.match(/Nilai:/g)||[]).length,signs=(html.match(/TTD:/g)||[]).length;
 if(footers!==10||dates<10||scores<10||signs<10)throw new Error(`${file}: V15_FOOTER_ASSERT_FAIL`);
 if(/AUDIT\s*[—-]|PAGE_REGISTER|03_BOOKS/.test(html))throw new Error(`${file}: PRINTED_TECHNICAL_METADATA_FAIL`);
 await fs.writeFile(file,html);
}
console.log('Applied J1 FROZEN v1.5: 34pt planting, 31pt Tartil, flexible practice area, compact 16mm footer, no dead-space allocation.');
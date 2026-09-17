import fs from 'node:fs/promises';

const files=['P001-P010','P011-P020','P021-P030','P031-P040'].map(x=>`dist/QURBATA-J1-${x}-AUDIT.html`);
const css=`<style id="j1-layout-v14">
/* FROZEN v1.4.1: clean footer reference approved 2026-09-17. */
.activity-content>h2{display:none!important;}
.activity-strip{display:contents!important;}
.activity-content{display:contents!important;}
/* Remove obsolete empty blue/mint activity panel completely. */
.activity-strip:not(:has(.study-fields)){display:none!important;}
.study-fields{display:grid!important;visibility:visible!important;grid-template-columns:1.05fr .62fr 1.25fr!important;gap:2mm!important;height:13mm!important;min-height:13mm!important;margin:0!important;align-items:end!important;font-size:6pt!important;line-height:1!important;overflow:visible!important;}
.study-fields span,.study-fields span:last-child{visibility:visible!important;height:12mm!important;min-height:12mm!important;display:flex!important;align-items:flex-start!important;justify-content:flex-start!important;box-sizing:border-box!important;padding:1.5mm 1.8mm!important;border:.28mm solid #78b6d5!important;border-radius:2.5mm!important;color:#123f59!important;background:#fff!important;overflow:visible!important;}
/* Footer is one clean horizontal system; QR/metadata may never overlap fields. */
.page-footer,.footer,.book-footer{position:relative!important;display:grid!important;grid-template-columns:auto minmax(0,1fr) auto!important;align-items:center!important;column-gap:2mm!important;min-height:15mm!important;overflow:visible!important;}
.page-footer img,.footer img,.book-footer img{position:static!important;float:none!important;max-width:14mm!important;max-height:14mm!important;margin:0!important;z-index:auto!important;}
.page-footer .qr,.footer .qr,.book-footer .qr{position:static!important;width:14mm!important;height:14mm!important;margin:0!important;padding:1mm!important;background:#fff!important;box-sizing:content-box!important;}
/* Audit/debug strings must never cross the printed footer. */
.audit-meta,.audit-footer,.page-register-meta,.debug-meta{display:none!important;}
/* Tartil remains dominant. */
.practice-panel{min-height:0!important;overflow:visible!important;}
.practice-grid{grid-template-rows:repeat(8,minmax(0,1fr))!important;gap:.7mm!important;min-height:0!important;overflow:visible!important;}
.practice-row{min-height:0!important;overflow:visible!important;}
.practice-cell{font-size:25pt!important;line-height:1.08!important;padding:.55mm .35mm!important;overflow:visible!important;}
.planting .arabic,.intro-pair,.lesson-heading .arabic-title{font-size:24pt!important;line-height:1.08!important;}
.integration-card{padding-bottom:.4mm!important;}
.integration-arabic{line-height:1.12!important;padding:.5mm .6mm!important;}
.integration-meaning,.integration-instruction{line-height:1.12!important;padding:.35mm .55mm!important;}
</style>`;
for(const file of files){
 let html=await fs.readFile(file,'utf8');
 html=html.replace(/<style id="j1-layout-v14">[\s\S]*?<\/style>\s*/g,'');
 /* Remove the obsolete empty activity box at source when it contains no admin fields. */
 html=html.replace(/<section class="activity-strip">\s*<div class="activity-content">\s*<h2>[\s\S]*?<\/h2>\s*<\/div>\s*<\/section>/g,'');
 html=html.replace('</head>',`${css}\n</head>`);
 await fs.writeFile(file,html);
}
console.log('Applied J1 layout v1.4.1: obsolete activity box removed; clean horizontal admin/QR footer; Tartil protected.');
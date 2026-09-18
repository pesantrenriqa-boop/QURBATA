import fs from 'node:fs/promises';

const files=['P001-P010','P011-P020','P021-P030','P031-P040'].map(x=>`dist/QURBATA-J1-${x}-AUDIT.html`);

const css=`<style id="j1-layout-v14">
/* FROZEN v1.5.5 — preserve readable 34pt Tartil; fix vertical density and footer as one system. */
.activity-content>h2{display:none!important;}
.activity-strip{display:none!important;height:0!important;min-height:0!important;margin:0!important;padding:0!important;}
.audit-meta,.audit-footer,.page-register-meta,.debug-meta{display:none!important;}
article,.page,.lesson-page{box-sizing:border-box!important;overflow:hidden!important;}
/* A5 page content is a definite vertical system. 100% is inherited where the master already defines page height. */
article{height:100%!important;min-height:100%!important;display:grid!important;grid-template-rows:auto minmax(18mm,auto) auto minmax(0,1fr) 15mm!important;align-content:stretch!important;row-gap:.8mm!important;}
.planting,.intro-pair{min-height:18mm!important;margin:0!important;overflow:visible!important;display:flex!important;align-items:center!important;justify-content:center!important;box-sizing:border-box!important;}
.planting .arabic,.intro-pair{font-size:38pt!important;line-height:1.12!important;padding:1.2mm .8mm!important;overflow:visible!important;min-height:16mm!important;display:flex!important;align-items:center!important;justify-content:center!important;}
.integration-panel,.integration-grid{margin:0!important;min-height:0!important;}
.integration-card{padding:.4mm .6mm!important;min-height:0!important;}
.integration-arabic{line-height:1.1!important;padding:.25mm .4mm!important;}
.integration-meaning,.integration-instruction{line-height:1.06!important;padding:.15mm .35mm!important;}
/* Example track is reserved first. Practice receives only the remaining height. */
.practice-panel{height:100%!important;min-height:0!important;margin:0!important;padding:0!important;overflow:hidden!important;display:flex!important;flex-direction:column!important;align-self:stretch!important;}
.practice-grid{flex:1 1 0!important;height:auto!important;min-height:0!important;margin:0!important;display:grid!important;grid-template-rows:repeat(8,minmax(0,1fr))!important;gap:0!important;overflow:hidden!important;align-self:stretch!important;}
.practice-row{height:auto!important;min-height:0!important;margin:0!important;overflow:hidden!important;display:grid!important;align-items:stretch!important;}
.practice-cell{font-size:34pt!important;line-height:1.12!important;padding:.7mm .55mm!important;min-height:0!important;height:100%!important;overflow:visible!important;display:flex!important;align-items:center!important;justify-content:center!important;box-sizing:border-box!important;}
/* Official footer: exactly one compact horizontal system. */
.qurbata-footer-v155{display:grid!important;grid-template-columns:9fr 21fr 14fr 23fr 11fr 22fr!important;column-gap:.7mm!important;align-items:center!important;width:100%!important;height:15mm!important;min-height:15mm!important;max-height:15mm!important;margin:0!important;padding:0!important;box-sizing:border-box!important;break-inside:avoid!important;overflow:hidden!important;font-family:Arial,sans-serif!important;color:#12415c!important;align-self:end!important;}
.qf-id{display:flex!important;align-items:center!important;justify-content:center!important;height:6mm!important;border-radius:3.2mm!important;background:#dff2fb!important;font-weight:700!important;font-size:5.7pt!important;white-space:nowrap!important;min-width:0!important;}
.qf-field{display:grid!important;grid-template-rows:3.6mm 9mm!important;gap:.3mm!important;min-width:0!important;height:13mm!important;align-self:center!important;}
.qf-label{font-size:5.6pt!important;font-weight:600!important;line-height:3.6mm!important;padding-left:.6mm!important;white-space:nowrap!important;overflow:hidden!important;}
.qf-box{height:9mm!important;min-height:9mm!important;border:.28mm solid #73b8db!important;border-radius:2.1mm!important;background:#fff!important;box-sizing:border-box!important;position:relative!important;overflow:hidden!important;}
.qf-box:after{content:'············';position:absolute!important;left:1.1mm!important;right:1.1mm!important;bottom:.8mm!important;text-align:center!important;color:#1473a8!important;font-size:5.3pt!important;white-space:nowrap!important;overflow:hidden!important;}
.qf-qr{display:flex!important;align-items:center!important;justify-content:center!important;min-width:0!important;height:14mm!important;padding:.8mm!important;background:#fff!important;box-sizing:border-box!important;overflow:hidden!important;}
.qf-qr img,.qf-qr svg,.qf-qr canvas{display:block!important;position:static!important;float:none!important;width:12.5mm!important;height:12.5mm!important;max-width:12.5mm!important;max-height:12.5mm!important;margin:0!important;object-fit:contain!important;}
.qf-brand{display:flex!important;flex-direction:column!important;align-items:center!important;justify-content:center!important;gap:.3mm!important;min-width:0!important;height:14mm!important;text-align:center!important;overflow:hidden!important;}
.qf-brand-ar{font-family:'KFGQPC Uthman Taha Naskh','KFGQPCUthmanTahaNaskh',serif!important;font-size:8.7pt!important;line-height:1!important;color:#0870ad!important;white-space:nowrap!important;}
.qf-brand-id{font-size:4.4pt!important;line-height:1!important;white-space:nowrap!important;color:#12618d!important;}
.qf-brand-os{font-size:6.2pt!important;line-height:1!important;font-weight:700!important;color:#075f92!important;white-space:nowrap!important;}
/* All legacy loose footer identities are forbidden by v1.5.5. */
article>.motto,article>.footer-motto,article>.riqa-os-brand,article>.brand-footer,article>.page-footer,article>.book-footer,article>.footer{display:none!important;}
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
 return `<div class="qurbata-footer-v155" data-qurbata-footer="${id}"><div class="qf-id">${id}</div><div class="qf-field"><div class="qf-label">Tanggal:</div><div class="qf-box"></div></div><div class="qf-field"><div class="qf-label">Nilai:</div><div class="qf-box"></div></div><div class="qf-field"><div class="qf-label">TTD:</div><div class="qf-box"></div></div><div class="qf-qr">${qr}</div><div class="qf-brand"><div class="qf-brand-ar" dir="rtl">تَعَلَّمْ – اِعْمَلْ – عَلِّمْ</div><div class="qf-brand-id">Belajar, Mengamalkan, Mengajarkan</div><div class="qf-brand-os">RIQA OS</div></div></div>`;
}
const examples={1:'بَ تَ ثَ',2:'ءَ أَ',3:'جَ حَ خَ',4:'دَ ذَ رَ زَ',5:'سَ شَ',6:'صَ ضَ',7:'طَ ظَ',8:'عَ غَ',9:'فَ قَ',11:'كَ لَ',12:'مَ نَ',13:'هَ وَ يَ',14:'بَ ← بِ · تَ ← تِ · ثَ ← ثِ · جَ ← جِ',15:'حِ خِ دِ ذِ',16:'رِ زِ سِ شِ',17:'صِ ضِ طِ ظِ',18:'عِ غِ فِ قِ',19:'كِ لِ مِ نِ هِ وِ يِ ءِ إِ',21:'بِ ← بُ · تِ ← تُ · ثِ ← ثُ · جِ ← جُ',22:'حِ ← حُ · خِ ← خُ · دِ ← دُ · ذِ ← ذُ',23:'رِ ← رُ · زِ ← زُ · سِ ← سُ · شِ ← شُ',24:'صِ ← صُ · ضِ ← ضُ · طِ ← طُ · ظِ ← ظُ',25:'عِ ← عُ · غِ ← غُ · فِ ← فُ · قِ ← قُ',26:'كِ ← كُ · لِ ← لُ · مِ ← مُ · نِ ← نُ',27:'هِ ← هُ · وِ ← وُ · يِ ← يُ · ءِ ← ءُ'};
function stripTags(s){return s.replace(/<[^>]*>/g,' ').replace(/&nbsp;/g,' ').replace(/\s+/g,' ').trim();}
function ensureExample(one,pageNo){
 const expected=examples[pageNo]; if(!expected)return one;
 const block=one.match(/<[^>]+class=["'][^"']*(?:planting|intro-pair)[^"']*["'][^>]*>[\s\S]*?<\/[^>]+>/i);
 const hasArabic=block&&/[\u0600-\u06FF]/.test(stripTags(block[0]));
 if(hasArabic)return one;
 const html='<section class="planting example-source-v155"><div class="arabic" dir="rtl">'+expected+'</div></section>';
 const anchor=one.search(/<[^>]+class=["'][^"']*(?:integration-panel|integration-grid)[^"']*["']/i);
 if(anchor<0)throw new Error('P'+String(pageNo).padStart(3,'0')+': EXAMPLE_CONTENT_MISSING_NO_INSERT_ANCHOR');
 return one.slice(0,anchor)+html+one.slice(anchor);
}
function normalizeArticle(article,pageNo){
 const qr=getQr(article);let one=ensureExample(article,pageNo);
 const exampleRequired=Boolean(examples[pageNo]);
 if(exampleRequired){const b=one.match(/<[^>]+class=["'][^"']*(?:planting|intro-pair)[^"']*["'][^>]*>[\s\S]*?<\/[^>]+>/i);if(!b||!/[\u0600-\u06FF]/.test(stripTags(b[0])))throw new Error(`P${String(pageNo).padStart(3,'0')}: EXAMPLE_CONTENT_MISSING`);if(pageNo===1&&!['بَ','تَ','ثَ'].every(x=>stripTags(b[0]).includes(x)))throw new Error('P001: EXAMPLE_SENTINEL_FAIL');}
 one=one.replace(/<section class="activity-strip">[\s\S]*?<\/section>/gi,'');
 one=one.replace(/<div class=["']study-fields["'][^>]*>[\s\S]*?<\/div>/gi,'');
 one=one.replace(/<div class=["']qurbata-footer-v(?:142|143|15|151|152)["'][^>]*>[\s\S]*?<\/div>\s*<\/div>\s*<\/div>\s*<\/div>\s*<\/div>\s*<\/div>/gi,'');
 one=one.replace(/<[^>]+class=["'][^"']*(?:page-footer|book-footer|footer-motto|riqa-os-brand|brand-footer)[^"']*["'][^>]*>[\s\S]*?<\/[^>]+>/gi,'');
 return one.replace(/<\/article>\s*$/i,`${footer(pageNo,qr)}</article>`);
}
for(const file of files){
 let html=await fs.readFile(file,'utf8');
 html=html.replace(/<style id="j1-layout-v14">[\s\S]*?<\/style>\s*/g,'');
 html=stripTechnicalText(html);
 let pageCounter=Number(file.match(/P(\d{3})-/)?.[1]||1);
 html=html.replace(/<article\b[^>]*>[\s\S]*?<\/article>/gi,a=>normalizeArticle(a,pageCounter++));
 html=html.replace('</head>',`${css}\n</head>`);
 const footers=(html.match(/class="qurbata-footer-v155"/g)||[]).length;
 const dates=(html.match(/Tanggal:/g)||[]).length,scores=(html.match(/Nilai:/g)||[]).length,signs=(html.match(/TTD:/g)||[]).length;
 if(footers!==10||dates<10||scores<10||signs<10)throw new Error(`${file}: V155_FOOTER_ASSERT_FAIL footers=${footers}`);
 if(/AUDIT\s*[—-]|PAGE_REGISTER|03_BOOKS/.test(html))throw new Error(`${file}: PRINTED_TECHNICAL_METADATA_FAIL`);
 if(!/font-size:34pt!important/.test(css))throw new Error(`${file}: READING_SIZE_ASSERT_FAIL`);
 const articles=[...html.matchAll(/<article\b[^>]*>[\s\S]*?<\/article>/gi)].map(m=>m[0]);
 if(articles.length!==10)throw new Error(`${file}: PAGE_COUNT_DOM_FAIL articles=${articles.length}`);
 articles.forEach((a,i)=>{
   const pageNo=Number(file.match(/P(\d{3})-/)?.[1]||1)+i;
   if(![10,20,40].includes(pageNo)){
     const panel=a.match(/<[^>]+class=["'][^"']*(?:practice-panel|practice-grid|exercise-grid)[^"']*["'][^>]*>[\s\S]*?<\/[^>]+>/i);
     if(!panel)throw new Error(`P${String(pageNo).padStart(3,'0')}: PRACTICE_CONTAINER_MISSING`);
     const rows=(a.match(/class=["'][^"']*(?:practice-row|exercise-row)[^"']*["']/g)||[]).length;
     const cells=(a.match(/class=["'][^"']*(?:practice-cell|exercise-cell)[^"']*["']/g)||[]).length;
     const arabic=(a.match(/[\u0600-\u06FF]/g)||[]).length;
     /* Some frozen legacy pages encode 8×3 as grid children without explicit row wrappers.
        The non-negotiable content gate is therefore 24 rendered exercise cells; when row
        wrappers exist, they must be exactly eight. */
     if(cells!==24)throw new Error(`P${String(pageNo).padStart(3,'0')}: PRACTICE_24_FAIL rows=${rows} cells=${cells}`);
     if(rows!==0&&rows!==8)throw new Error(`P${String(pageNo).padStart(3,'0')}: PRACTICE_8ROW_FAIL rows=${rows}`);
     if(arabic<24)throw new Error(`P${String(pageNo).padStart(3,'0')}: PRACTICE_CONTENT_EMPTY`);
   }
 });
 const examples=(html.match(/class=["'][^"']*(?:planting|intro-pair)[^"']*["']/g)||[]).length;
 if(examples<7)throw new Error(`${file}: V155_EXAMPLE_ASSERT_FAIL examples=${examples}`);
 await fs.writeFile(file,html);
}
console.log('Applied J1 FROZEN v1.5.5: protect heading separately; assert practice 8x3 + Arabic content; inject/verify Page Register example, distribute remaining height to 8 rows, unified 15mm footer.');
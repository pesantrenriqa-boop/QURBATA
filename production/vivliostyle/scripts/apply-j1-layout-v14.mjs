import fs from 'node:fs/promises';

const files=['P001-P010','P011-P020','P021-P030','P031-P040'].map(x=>`dist/QURBATA-J1-${x}-AUDIT.html`);

const css=`<style id="j1-layout-v14">
/* FROZEN v1.4.2 — footer is one normalized horizontal component. */
.activity-content>h2{display:none!important;}
.activity-strip:not(:has(.study-fields)){display:none!important;}
.audit-meta,.audit-footer,.page-register-meta,.debug-meta{display:none!important;}
.qurbata-footer-v142{display:grid!important;grid-template-columns:13mm minmax(30mm,1.15fr) minmax(18mm,.68fr) minmax(31mm,1.28fr) 17mm minmax(31mm,1fr)!important;gap:1.6mm!important;align-items:center!important;width:100%!important;min-height:17mm!important;max-height:18mm!important;margin-top:1mm!important;box-sizing:border-box!important;break-inside:avoid!important;overflow:visible!important;font-family:Arial,sans-serif!important;color:#12415c!important;}
.qf-id{display:flex!important;align-items:center!important;justify-content:center!important;height:7mm!important;border-radius:4mm!important;background:#dff2fb!important;font-weight:700!important;font-size:6.2pt!important;white-space:nowrap!important;}
.qf-field{display:grid!important;grid-template-rows:4mm 11mm!important;gap:.5mm!important;min-width:0!important;}
.qf-label{font-size:6pt!important;font-weight:600!important;line-height:4mm!important;padding-left:1mm!important;white-space:nowrap!important;}
.qf-box{height:11mm!important;border:.3mm solid #73b8db!important;border-radius:2.6mm!important;background:#fff!important;box-sizing:border-box!important;position:relative!important;}
.qf-box:after{content:'··················';position:absolute!important;left:2mm!important;right:2mm!important;bottom:1.4mm!important;text-align:center!important;letter-spacing:.4mm!important;color:#1473a8!important;font-size:6pt!important;white-space:nowrap!important;overflow:hidden!important;}
.qf-qr{display:flex!important;align-items:center!important;justify-content:center!important;width:17mm!important;height:17mm!important;padding:1mm!important;background:#fff!important;box-sizing:border-box!important;overflow:hidden!important;}
.qf-qr img,.qf-qr svg,.qf-qr canvas{display:block!important;position:static!important;float:none!important;width:15mm!important;height:15mm!important;max-width:15mm!important;max-height:15mm!important;margin:0!important;object-fit:contain!important;}
.qf-brand{display:flex!important;flex-direction:column!important;align-items:center!important;justify-content:center!important;gap:.5mm!important;min-width:0!important;text-align:center!important;overflow:visible!important;}
.qf-brand-ar{font-family:'KFGQPC Uthman Taha Naskh','KFGQPCUthmanTahaNaskh',serif!important;font-size:10.5pt!important;line-height:1!important;color:#0870ad!important;white-space:nowrap!important;}
.qf-brand-id{font-size:5.2pt!important;line-height:1.05!important;white-space:nowrap!important;color:#12618d!important;}
.qf-brand-os{font-size:7pt!important;line-height:1!important;font-weight:700!important;letter-spacing:.5px!important;color:#075f92!important;white-space:nowrap!important;}
/* Hide legacy footer pieces after their useful QR source has been cloned. */
.qurbata-footer-v142~.page-footer,.qurbata-footer-v142~.footer,.qurbata-footer-v142~.book-footer{display:none!important;}
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

function normalizeFooter(html,pageNo){
  const id=`QJ1-P${String(pageNo).padStart(3,'0')}`;
  const qrMatch=html.match(/<(?:img|svg|canvas)[^>]*(?:qr|QR|qrcode|riqa)[^>]*>[\s\S]*?(?:<\/svg>|<\/canvas>)?/i)
    || html.match(/<img[^>]+src=["'][^"']*(?:qr|QR)[^"']*["'][^>]*>/i);
  const qr=qrMatch?qrMatch[0]:'';
  const footer=`<div class="qurbata-footer-v142">
    <div class="qf-id">${id}</div>
    <div class="qf-field"><div class="qf-label">Tanggal:</div><div class="qf-box"></div></div>
    <div class="qf-field"><div class="qf-label">Nilai:</div><div class="qf-box"></div></div>
    <div class="qf-field"><div class="qf-label">TTD:</div><div class="qf-box"></div></div>
    <div class="qf-qr">${qr}</div>
    <div class="qf-brand"><div class="qf-brand-ar" dir="rtl">تَعَلَّمْ – اِعْمَلْ – عَلِّمْ</div><div class="qf-brand-id">Belajar, Mengamalkan, Mengajarkan</div><div class="qf-brand-os">RIQA OS</div></div>
  </div>`;
  /* Remove legacy admin strip/footer content so nothing can fall to a second row. */
  html=html.replace(/<section class="activity-strip">[\s\S]*?<\/section>/gi,'');
  html=html.replace(/<div class=["']study-fields["'][^>]*>[\s\S]*?<\/div>/gi,'');
  html=html.replace(/<[^>]+class=["'][^"']*(?:page-footer|book-footer|footer)[^"']*["'][^>]*>[\s\S]*?<\/[^>]+>/gi,'');
  const pageClose=html.lastIndexOf('</main>');
  if(pageClose>=0) return html.slice(0,pageClose)+footer+html.slice(pageClose);
  return html.replace('</body>',footer+'</body>');
}

for(const file of files){
 let html=await fs.readFile(file,'utf8');
 html=html.replace(/<style id="j1-layout-v14">[\s\S]*?<\/style>\s*/g,'');
 html=stripTechnicalText(html);
 /* Each dist block contains ten article/page elements. Inject one normalized footer per page. */
 let pageCounter=Number(file.match(/P(\d{3})-/)?.[1]||1);
 html=html.replace(/<article([^>]*)>([\s\S]*?)<\/article>/gi,(all,attrs,body)=>{
   let one=`<article${attrs}>${body}</article>`;
   one=normalizeFooter(one,pageCounter++);
   return one;
 });
 html=html.replace('</head>',`${css}\n</head>`);
 await fs.writeFile(file,html);
}
console.log('Applied J1 v1.4.2: normalized single-row footer; legacy footer and printed audit metadata removed.');
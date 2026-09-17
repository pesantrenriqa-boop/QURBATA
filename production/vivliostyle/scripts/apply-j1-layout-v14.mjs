import fs from 'node:fs/promises';

const files=['P001-P010','P011-P020','P021-P030','P031-P040'].map(x=>`dist/QURBATA-J1-${x}-AUDIT.html`);
const css=`<style id="j1-layout-v14">
/* FROZEN v1.4: Tartil first, no lower Bi'ah activity heading, teacher zone = Tanggal/Nilai/TTD only. */
.activity-content>h2{display:none!important;}
.activity-strip{display:block!important;min-height:16mm!important;height:16mm!important;max-height:16mm!important;padding:.5mm 2mm!important;margin-top:.6mm!important;overflow:visible!important;}
.activity-content{display:block!important;height:100%!important;min-height:0!important;overflow:visible!important;}
.study-fields{display:grid!important;visibility:visible!important;grid-template-columns:1fr .72fr 1.35fr!important;gap:2mm!important;height:14mm!important;min-height:14mm!important;margin:0!important;align-items:stretch!important;font-size:6.2pt!important;line-height:1!important;overflow:visible!important;}
.study-fields span,.study-fields span:last-child{visibility:visible!important;height:14mm!important;min-height:14mm!important;display:flex!important;align-items:flex-end!important;justify-content:center!important;box-sizing:border-box!important;padding:0 0 .8mm!important;border:0!important;border-bottom:.3mm solid #7da4b6!important;color:#183b4b!important;background:transparent!important;overflow:visible!important;}
/* The recovered vertical space belongs primarily to Tartil. */
.practice-panel{min-height:0!important;overflow:visible!important;}
.practice-grid{grid-template-rows:repeat(8,minmax(0,1fr))!important;gap:.7mm!important;min-height:0!important;overflow:visible!important;}
.practice-row{min-height:0!important;overflow:visible!important;}
.practice-cell{font-size:25pt!important;line-height:1.08!important;padding:.55mm .35mm!important;overflow:visible!important;}
/* New-competency examples must remain large and clear. */
.planting .arabic,.intro-pair,.lesson-heading .arabic-title{font-size:24pt!important;line-height:1.08!important;}
.integration-card{padding-bottom:.4mm!important;}
.integration-arabic{line-height:1.12!important;padding:.5mm .6mm!important;}
.integration-meaning,.integration-instruction{line-height:1.12!important;padding:.35mm .55mm!important;}
</style>`;
for(const file of files){
 let html=await fs.readFile(file,'utf8');
 html=html.replace(/<style id="j1-layout-v14">[\s\S]*?<\/style>\s*/g,'');
 html=html.replace('</head>',`${css}\n</head>`);
 await fs.writeFile(file,html);
}
console.log('Applied J1 layout v1.4: large Tartil; lower activity heading removed; Tanggal/Nilai/TTD explicitly visible.');
import fs from 'node:fs/promises';

const files=['P001-P010','P011-P020','P021-P030','P031-P040'].map(x=>`dist/QURBATA-J1-${x}-AUDIT.html`);
const css=`<style id="j1-layout-v14">
/* FROZEN v1.4: Tartil first, no lower Bi'ah activity heading, compact teacher administration. */
.activity-content>h2{display:none!important;}
.activity-strip{min-height:15mm!important;height:15mm!important;max-height:15mm!important;padding:.5mm 2mm!important;margin-top:1mm!important;overflow:hidden!important;}
.activity-content{display:block!important;min-height:0!important;}
.study-fields{display:grid!important;grid-template-columns:1fr .72fr 1.35fr!important;gap:2mm!important;height:13mm!important;min-height:13mm!important;margin:0!important;align-items:end!important;font-size:5.5pt!important;}
.study-fields span,.study-fields span:last-child{height:13mm!important;min-height:13mm!important;display:flex!important;align-items:flex-end!important;justify-content:center!important;padding:0 0 .4mm!important;border-top:0!important;border-bottom:.3mm solid #7da4b6!important;}
/* The recovered vertical space belongs to Tartil. */
.practice-panel{min-height:0!important;overflow:visible!important;}
.practice-grid{grid-template-rows:repeat(8,minmax(0,1fr))!important;gap:.7mm!important;min-height:0!important;overflow:visible!important;}
.practice-row{min-height:0!important;overflow:visible!important;}
.practice-cell{font-size:25pt!important;line-height:1.08!important;padding:.55mm .35mm!important;overflow:visible!important;}
/* New-competency examples must never be smaller than ordinary explanatory text. */
.planting .arabic,.intro-pair,.lesson-heading .arabic-title{font-size:24pt!important;line-height:1.08!important;}
/* Breathing room: support text must not touch borders/glyphs. */
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
console.log('Applied J1 layout v1.4: larger Tartil, compact Tanggal/Nilai/TTD, lower Bi\'ah activity heading removed.');
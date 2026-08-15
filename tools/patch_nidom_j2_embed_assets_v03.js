const fs=require('fs');
const p='tools/render_nidom_j2_v01.js';
let s=fs.readFileSync(p,'utf8');
if(!s.includes('J2_EMBED_ASSETS_V03')){
  s=s.replace("const OUT=path.resolve(__dirname,'../dist/nidom-akhlak/j2-v01');fs.mkdirSync(OUT,{recursive:true});", "const OUT=path.resolve(__dirname,'../dist/nidom-akhlak/j2-v01');fs.mkdirSync(OUT,{recursive:true});\n// J2_EMBED_ASSETS_V03\nconst FONT_DATA=fs.readFileSync(path.resolve(__dirname,'../.build-fonts/UthmanTaha.woff2')).toString('base64');\nconst LOGO_DATA=Buffer.from(fs.readFileSync(path.resolve(__dirname,'../books/shared/assets/qurbata-logo.svg'),'utf8')).toString('base64');");
  s=s.replace("@font-face{font-family:Uthman;src:url('../../../.build-fonts/UthmanTaha.woff2')}", "@font-face{font-family:Uthman;src:url('data:font/woff2;base64,${FONT_DATA}') format('woff2');font-display:block}");
  s=s.replace('src=\"../../shared/assets/qurbata-logo.svg\"', 'src=\"data:image/svg+xml;base64,${LOGO_DATA}\"');
  fs.writeFileSync(p,s);
}
console.log('J2_EMBED_ASSETS_V03=PASS');
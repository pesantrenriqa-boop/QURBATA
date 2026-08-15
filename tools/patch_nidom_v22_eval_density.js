const fs=require('fs');
const p='tools/render_nidom_j1_variative_v22.js';
let s=fs.readFileSync(p,'utf8');
const from="style='height:${p.mode==='quiz'?'7':'10'}mm'";
const to="style='height:${p.mode==='quiz'?'0':'10'}mm'";
if(!s.includes(from)){console.error('EVAL_DENSITY_PATCH_TARGET_NOT_FOUND');process.exit(1)}
s=s.replace(from,to);
fs.writeFileSync(p,s);
console.log('NIDOM_V22_EVAL_DENSITY_PATCH=PASS');
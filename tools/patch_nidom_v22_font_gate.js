const fs=require('fs');
const p='tools/render_nidom_j1_variative_v22.js';
let s=fs.readFileSync(p,'utf8');
const old="if(!check.font)throw new Error(`UTHMAN_FAIL_P${p.n}`);";
const neu="if((p.theme || p.arab) && !check.font)throw new Error(`UTHMAN_FAIL_P${p.n}`);";
if(!s.includes(old)) throw new Error('FONT_GATE_PATTERN_NOT_FOUND');
s=s.replace(old,neu);
fs.writeFileSync(p,s);
console.log('NIDOM_V22_FONT_GATE_PATCH=PASS');
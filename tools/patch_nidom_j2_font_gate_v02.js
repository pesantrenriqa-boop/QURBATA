const fs=require('fs');
const p='tools/render_nidom_j2_v01.js';
let s=fs.readFileSync(p,'utf8');
const from="font:[...document.fonts].some(x=>x.family==='Uthman'&&x.status==='loaded')";
const to="font:document.fonts.check('30px Uthman','السَّلَامُ')";
if(!s.includes(from)){console.error('J2_FONT_GATE_TARGET_NOT_FOUND');process.exit(1)}
s=s.replace(from,to);
fs.writeFileSync(p,s);
console.log('J2_FONT_GATE_PATCH=PASS');
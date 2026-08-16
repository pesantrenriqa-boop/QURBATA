const fs=require('fs');
const p='tools/render_nidom_j2_v01.js';
let s=fs.readFileSync(p,'utf8');
if(s.includes('J2_AUDIT_V03_APPLIED')){console.log('J2_AUDIT_V03=ALREADY');process.exit(0)}
// Audit policy: checkpoint/evaluation pages do not inherit a random hadith/dictionary.
s=s.replace("let t=p.t?T[p.t]:null;let dict=t?t.dict:((n=>n<=20?T.jujur.dict:T.tolong.dict)(p.n));", "let t=p.t?T[p.t]:null;let dict=t?t.dict:[];");
s=s.replace("let count=p.n>=36?2:Math.min(4,dict.length),off=(p.n-1)%dict.length;dict=[...dict.slice(off),...dict.slice(0,off)].slice(0,count);", "let count=dict.length?(p.n>=36?Math.min(2,dict.length):Math.min(4,dict.length)):0,off=dict.length?(p.n-1)%dict.length:0;dict=dict.length?[...dict.slice(off),...dict.slice(0,off)].slice(0,count):[];");
s=s.replace("let had=t?`<div class=\"had\"><div class=\"arab\">${t.had}</div><div class=\"tr\">${t.tr}</div><div class=\"src\">${t.src}</div></div>`:'';", "let had=t?`<div class=\"had\"><div class=\"arab\">${t.had}</div><div class=\"tr\">${t.tr}</div><div class=\"src\">${t.src}${[16,17,18,26,33,34].includes(p.n)?' · potongan hadits / redaksi tematik':''}</div></div>`:'';");
s=s.replace("<div class=\"kam\"><h3>KAMUS HADITS · ARTI PER KATA</h3><div class=\"kg\" style=\"grid-template-columns:repeat(${count},1fr)\">${dict.map(w=>`<div class=\"kc\"><div class=\"kw\">${w[0]}</div><div class=\"ki\">${w[1]}</div></div>`).join('')}</div></div>", "${count?`<div class=\"kam\"><h3>KAMUS HADITS · ARTI PER KATA</h3><div class=\"kg\" style=\"grid-template-columns:repeat(${count},1fr)\">${dict.map(w=>`<div class=\"kc\"><div class=\"kw\">${w[0]}</div><div class=\"ki\">${w[1]}</div></div>`).join('')}</div></div>`:`<div class=\"kam\"><h3>MUROJAAH DALIL</h3><div class=\"ki\">Ingat kembali satu hadits dari tema sebelumnya bersama guru. Halaman ini berfungsi untuk evaluasi/praktik, bukan menambah hadits baru.</div></div>`}");
s += "\n// J2_AUDIT_V03_APPLIED\n";
fs.writeFileSync(p,s);console.log('J2_AUDIT_V03=PATCHED');
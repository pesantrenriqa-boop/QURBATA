import fs from 'node:fs/promises';
import path from 'node:path';

const file=path.resolve(import.meta.dirname,'build-pagedjs-p001-p010.mjs');
let src=await fs.readFile(file,'utf8');

// CI invokes this enforcer more than once. Never inject the sentinel twice.
if(src.includes('const P003_SENTINEL_VERSION="v1.1";')){
  console.log('P003_COMPETENCY_SENTINEL_PATCHED');
  console.log('P003_SENTINEL_ALREADY_PRESENT');
  console.log('P003_TARGET=جَ حَ خَ');
  console.log('P003_PLANTING=6xEXACT2_TARGET_ONLY');
  console.log('P003_PRACTICE=18xEXACT3_TARGET_REQUIRED');
  console.log('P003_REVIEW_ALLOWED=ءَ أَ بَ تَ ثَ');
  process.exit(0);
}

const start=src.indexOf('function exercisesFor(n){');
const end=src.indexOf('\nconst logo=',start);
if(start<0||end<0) throw new Error('Cannot locate exercisesFor() for J1 competency-first patch');

const replacement=String.raw`const P003_SENTINEL_VERSION="v1.1";
// Parse one pedagogical unit as Arabic base letter plus its combining marks.
// Do not depend on spaces: detached rendering may normalize whitespace later.
const p003Units=x=>String(x).normalize('NFC').match(/[ء-ي][\\u064B-\\u065F\\u0670]*/gu)||[];
const p003Key=x=>p003Units(x).join('|');
const assertP003Regular=(items,target,review)=>{
 if(items.length!==24)throw new Error('P003 GROUP_COUNT_FAIL '+items.length+'/24');
 const keys=items.map(p003Key);if(new Set(keys).size!==items.length)throw new Error('P003 DUPLICATE_GROUP_FAIL');
 const allowed=new Set([...target,...review].map(x=>x.normalize('NFC')));
 const targetSet=new Set(target.map(x=>x.normalize('NFC')));
 for(let i=0;i<items.length;i++){
   const u=p003Units(items[i]);
   if(u.length===1)throw new Error('P003 SINGLE_LETTER_GROUP_FAIL cell='+(i+1));
   if(i<6&&u.length!==2)throw new Error('P003 PLANTING_LENGTH_FAIL cell='+(i+1)+' len='+u.length);
   if(i>=6&&u.length!==3)throw new Error('P003 PRACTICE_LENGTH_FAIL cell='+(i+1)+' len='+u.length);
   if(i<6&&u.some(x=>!targetSet.has(x.normalize('NFC'))))throw new Error('P003 COMPETENCY_MISMATCH_FAIL planting='+(i+1));
   if(i>=6&&!u.some(x=>targetSet.has(x.normalize('NFC'))))throw new Error('P003 COMPETENCY_MISMATCH_FAIL practice='+(i+1));
   if(u.some(x=>!allowed.has(x.normalize('NFC'))))throw new Error('P003 FUTURE_COMPETENCY_FAIL cell='+(i+1)+' units='+u.join(','));
 }
 return items;
};
const P003_REGISTER={target:['جَ','حَ','خَ'],review:['ءَ','أَ','بَ','تَ','ثَ']};
const P003_PLANTING=['جَ حَ','جَ خَ','حَ جَ','حَ خَ','خَ جَ','خَ حَ'];
const P003_PRACTICE=[
 'جَ بَ حَ','حَ تَ خَ','خَ ثَ جَ','بَ جَ خَ','تَ حَ جَ','ثَ خَ حَ',
 'جَ أَ خَ','حَ ءَ جَ','خَ بَ حَ','أَ جَ حَ','ءَ حَ خَ','بَ خَ جَ',
 'جَ ثَ حَ','حَ بَ خَ','خَ تَ جَ','ثَ جَ خَ','تَ خَ حَ','أَ حَ جَ'
];
function exercisesFor(n){
 if(n===3)return assertP003Regular([...P003_PLANTING,...P003_PRACTICE],P003_REGISTER.target,P003_REGISTER.review);
 if(n===1)return assertUniquePage(n,p1);
 if(n===2){const p=['ءَ','أَ','بَ','تَ','ثَ'],out=[];for(let i=0;i<p.length;i++)for(let j=0;j<p.length;j++)if(i!==j)out.push(p[i]+' '+p[j]);for(const x of p)if(out.length<24)out.push(x);return assertUniquePage(n,out.slice(0,24));}
 const learned=n<=13?fathah:n<=19?[...fathah,...kasrahTo(n)]:[...fathah,...kasrahTo(19),...Object.entries(intro).filter(([k])=>+k>=21&&+k<=Math.min(n,27)).flatMap(([,v])=>v)];
 const lexical=[...new Set((approvedWords[n]||approved21_39[n]||[]).map(x=>String(x).replace(/→/g,' ').trim().replace(/\\s+/g,' ')))].filter(x=>Array.from(x).filter(ch=>/[ء-ي]/.test(ch)).length===3);
 const out=[],seen=new Set();for(const x of lexical){const k=x.replace(/\\s+/g,'');if(!seen.has(k)&&out.length<24){out.push(x);seen.add(k);}}
 for(let i=0;i<learned.length&&out.length<24;i++)for(let j=0;j<learned.length&&out.length<24;j++)for(let k=0;k<learned.length&&out.length<24;k++){
   const x=learned[i]+' '+learned[j]+' '+learned[k],key=x.replace(/\\s+/g,'');if(!seen.has(key)){out.push(x);seen.add(key);}
 }
 return assertUniquePage(n,out.slice(0,24));
}`;

src=src.slice(0,start)+replacement+src.slice(end);
await fs.writeFile(file,src,'utf8');
console.log('P003_COMPETENCY_SENTINEL_PATCHED');
console.log('P003_PARSER=ARABIC_BASE_PLUS_COMBINING_MARKS');
console.log('P003_TARGET=جَ حَ خَ');
console.log('P003_PLANTING=6xEXACT2_TARGET_ONLY');
console.log('P003_PRACTICE=18xEXACT3_TARGET_REQUIRED');
console.log('P003_REVIEW_ALLOWED=ءَ أَ بَ تَ ثَ');

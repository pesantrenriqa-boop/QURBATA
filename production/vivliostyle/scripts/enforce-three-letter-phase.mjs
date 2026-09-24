import fs from 'node:fs/promises';
import path from 'node:path';

const file=path.resolve(import.meta.dirname,'build-pagedjs-p001-p010.mjs');
let src=await fs.readFile(file,'utf8');

const start=src.indexOf('function exercisesFor(n){');
const end=src.indexOf('\nconst logo=',start);
if(start<0||end<0) throw new Error('Cannot locate exercisesFor() for three-letter phase patch');

const replacement=String.raw`const baseLetters=x=>Array.from(String(x)).filter(ch=>/[ء-ي]/.test(ch));
const normalizeGroup=x=>String(x).replace(/→/g,' ').trim().replace(/\\s+/g,' ');
const groupLen=x=>baseLetters(normalizeGroup(x)).length;
const unique3=(pool,start,count,required=[])=>{
  const out=[],seen=new Set();
  const add=x=>{x=normalizeGroup(x);if(groupLen(x)!==3)return false;const k=x.replace(/\\s+/g,'');if(seen.has(k))return false;if(required.length&&!required.some(r=>x.includes(r)))return false;seen.add(k);out.push(x);return true};
  for(let z=0;z<pool.length*pool.length*pool.length&&out.length<count;z++){
    const i=(start+z)%pool.length,j=(start+Math.floor(z/pool.length)+z*3)%pool.length,k=(start+Math.floor(z/(pool.length*pool.length))+z*7)%pool.length;
    add(pool[i]+' '+pool[j]+' '+pool[k]);
  }
  if(out.length!==count)throw new Error('3-letter pool shortage: '+out.length+'/'+count);
  return out;
};
const assertJ1Shape=(n,items)=>{
  if(items.length!==24)throw new Error('P'+String(n).padStart(3,'0')+' must have 24 groups, got '+items.length);
  const keys=items.map(x=>normalizeGroup(x).replace(/\\s+/g,''));
  if(new Set(keys).size!==24)throw new Error('P'+String(n).padStart(3,'0')+' duplicate group');
  if(n>=3){const bad=items.filter(x=>groupLen(x)!==3);if(bad.length)throw new Error('P'+String(n).padStart(3,'0')+' EXACT-3 gate failed: '+bad.join(' | '));}
  return items;
};
function exercisesFor(n){
  if(n===1)return assertUniquePage(n,p1);
  if(n===2){const p=['ءَ','أَ','بَ','تَ','ثَ'],out=[];for(let i=0;i<p.length;i++)for(let j=0;j<p.length;j++)if(i!==j)out.push(p[i]+' '+p[j]);for(const x of p)if(out.length<24)out.push(x);return assertUniquePage(n,out.slice(0,24));}
  const learned=n<=13?fathah:n<=19?[...fathah,...kasrahTo(n)]:[...fathah,...kasrahTo(19),...Object.entries(intro).filter(([k])=>+k>=21&&+k<=Math.min(n,27)).flatMap(([,v])=>v)];
  const lexical=[...new Set((approvedWords[n]||approved21_39[n]||[]).map(normalizeGroup))].filter(x=>groupLen(x)===3);
  let out=[];
  if(n>=21&&n<=27){
    const target=intro[n]||[];
    const active=unique3(learned,n*37,14,target);
    const activeKeys=new Set(active.map(x=>x.replace(/\\s+/g,'')));
    const reviewPool=learned.filter(x=>!target.includes(x));
    const review=unique3(reviewPool,n*53,10).filter(x=>!activeKeys.has(x.replace(/\\s+/g,''))).slice(0,10);
    if(review.length!==10)throw new Error('P'+n+' 60/40 review shortage');
    out=[...active,...review];
  }else{
    for(const x of lexical){const detached=baseLetters(x).map((ch,i)=>{const a=Array.from(x);return ch;}); if(out.length<24)out.push(x);}
    const seen=new Set(out.map(x=>x.replace(/\\s+/g,'')));
    const fill=unique3(learned,n*71,24);
    for(const x of fill){const k=x.replace(/\\s+/g,'');if(!seen.has(k)&&out.length<24){out.push(x);seen.add(k);}}
    if(out.length<24){const extra=unique3(learned,n*97,24);for(const x of extra){const k=x.replace(/\\s+/g,'');if(!seen.has(k)&&out.length<24){out.push(x);seen.add(k);}}}
  }
  return assertJ1Shape(n,out.slice(0,24));
}`;

src=src.slice(0,start)+replacement+src.slice(end);
await fs.writeFile(file,src,'utf8');
console.log('THREE_LETTER_PHASE_PATCHED: P003-P040 exact 3 letters/group; P021-P027 14:10 active-review');

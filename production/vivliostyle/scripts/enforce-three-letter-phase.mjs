import fs from 'node:fs/promises';
import path from 'node:path';

const file=path.resolve(import.meta.dirname,'build-pagedjs-p001-p010.mjs');
let src=await fs.readFile(file,'utf8');
const start=src.indexOf('function exercisesFor(n){');
const end=src.indexOf('\nconst logo=',start);
if(start<0||end<0) throw new Error('Cannot locate exercisesFor() for J1 row-structure patch');

const replacement=String.raw`const baseLetters=x=>Array.from(String(x)).filter(ch=>/[ء-ي]/.test(ch));
const normalizeGroup=x=>String(x).replace(/→/g,' ').trim().replace(/\\s+/g,' ');
const groupLen=x=>baseLetters(normalizeGroup(x)).length;
const groupKey=x=>normalizeGroup(x).replace(/\\s+/g,'');
const uniqueGroups=(pool,len,start,count,required=[])=>{
 const out=[],seen=new Set();
 const add=x=>{x=normalizeGroup(x);if(groupLen(x)!==len)return;if(required.length&&!required.some(r=>x.includes(r)))return;const k=groupKey(x);if(seen.has(k))return;seen.add(k);out.push(x)};
 const max=Math.max(1,pool.length**len)*3;
 for(let z=0;z<max&&out.length<count;z++){
   const chars=[];for(let q=0;q<len;q++)chars.push(pool[(start+z*(q*2+1)+Math.floor(z/(pool.length||1))*(q+1))%pool.length]);
   add(chars.join(' '));
 }
 if(out.length!==count)throw new Error(len+'-letter pool shortage: '+out.length+'/'+count);
 return out;
};
const assertJ1Shape=(n,items,plantCount=0)=>{
 if(items.length!==24)throw new Error('P'+String(n).padStart(3,'0')+' must have 24 groups, got '+items.length);
 const keys=items.map(groupKey);if(new Set(keys).size!==items.length)throw new Error('P'+String(n).padStart(3,'0')+' duplicate group');
 if(n>=3&&n!==10&&n!==20&&n!==40){
   const badPlant=items.slice(0,plantCount).filter(x=>groupLen(x)!==2);
   const badPractice=items.slice(plantCount).filter(x=>groupLen(x)!==3);
   if(badPlant.length)throw new Error('P'+String(n).padStart(3,'0')+' planting must be EXACT-2: '+badPlant.join(' | '));
   if(badPractice.length)throw new Error('P'+String(n).padStart(3,'0')+' practice must be EXACT-3: '+badPractice.join(' | '));
 }
 return items;
};
function exercisesFor(n){
 if(n===1)return assertUniquePage(n,p1);
 if(n===2){const p=['ءَ','أَ','بَ','تَ','ثَ'],out=[];for(let i=0;i<p.length;i++)for(let j=0;j<p.length;j++)if(i!==j)out.push(p[i]+' '+p[j]);for(const x of p)if(out.length<24)out.push(x);return assertUniquePage(n,out.slice(0,24));}
 const target=intro[n]||[];
 const learned=n<=13?fathah:n<=19?[...fathah,...kasrahTo(n)]:[...fathah,...kasrahTo(19),...Object.entries(intro).filter(([k])=>+k>=21&&+k<=Math.min(n,27)).flatMap(([,v])=>v)];
 // Grid has 24 cells. Two planting rows = first 6 cells (3 columns x 2 rows).
 // Remaining 18 cells = 3-letter practice. Target letters dominate both zones.
 if(n>=3&&n!==10&&n!==20&&n!==40){
   if(target.length<3)throw new Error('P'+n+' target register missing for planting');
   const planting=uniqueGroups(target,2,n*11,6,target);
   const activeNeed=11; // 11/18 practice groups target-active ~=61%; 7/18 cumulative review ~=39%.
   const active=uniqueGroups(learned,3,n*37,activeNeed,target);
   const used=new Set([...planting,...active].map(groupKey));
   const reviewPool=learned.filter(x=>!target.includes(x));
   let review=uniqueGroups(reviewPool,3,n*53,7).filter(x=>!used.has(groupKey(x)));
   if(review.length<7){const extra=uniqueGroups(learned,3,n*79,18).filter(x=>!target.some(t=>x.includes(t))&&!used.has(groupKey(x)));review=[...review,...extra].slice(0,7);}
   if(review.length!==7)throw new Error('P'+n+' review shortage: '+review.length+'/7');
   return assertJ1Shape(n,[...planting,...active,...review],6);
 }
 // Checkpoint/evaluation pages retain explicit evaluation allocation, but stay unique.
 const lexical=[...new Set((approvedWords[n]||approved21_39[n]||[]).map(normalizeGroup))].filter(x=>groupLen(x)===3);
 const out=[],seen=new Set();for(const x of lexical){const k=groupKey(x);if(!seen.has(k)&&out.length<24){out.push(x);seen.add(k);}}
 const fill=uniqueGroups(learned,3,n*71,24);for(const x of fill){const k=groupKey(x);if(!seen.has(k)&&out.length<24){out.push(x);seen.add(k);}}
 return assertUniquePage(n,out.slice(0,24));
}`;

src=src.slice(0,start)+replacement+src.slice(end);
await fs.writeFile(file,src,'utf8');
console.log('J1_ROW_STRUCTURE_PATCHED: 2 planting rows x 2 letters, then 7 practice rows x 3 letters, target/review ~60:40');

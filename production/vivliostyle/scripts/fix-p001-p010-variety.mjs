import fs from "node:fs/promises";
import path from "node:path";

const root=path.resolve(import.meta.dirname,"..");
const file=path.join(root,"dist/QURBATA-J1-P001-P010-AUDIT.html");
let html=await fs.readFile(file,"utf8");

const introduced={1:["بَ","تَ","ثَ"],2:["ءَ","أَ"],3:["جَ","حَ","خَ"],4:["دَ","ذَ","رَ","زَ"],5:["سَ","شَ"],6:["صَ","ضَ"],7:["طَ","ظَ"],8:["عَ","غَ"],9:["فَ","قَ"]};
const cumulative=n=>Object.entries(introduced).filter(([p])=>Number(p)<=n).flatMap(([,x])=>x);
const p1=[
"بَ تَ","تَ بَ","بَ ثَ","ثَ بَ","تَ ثَ","ثَ تَ","بَ بَ","ثَ ثَ",
"بَ تَ ثَ","بَ ثَ تَ","تَ بَ ثَ","تَ ثَ بَ","ثَ بَ تَ","ثَ تَ بَ",
"بَ بَ تَ","بَ تَ بَ","تَ تَ ثَ","تَ ثَ تَ","ثَ ثَ بَ","ثَ بَ ثَ",
"بَ ثَ ثَ","تَ بَ بَ","ثَ تَ تَ","بَ بَ ثَ"
];

for(let n=1;n<=9;n++){
 const id=`QJ1-P${String(n).padStart(3,"0")}`;
 const start=html.indexOf(`data-page-id="${id}"`); if(start<0)throw new Error(`${id} missing`);
 const nextArticle=html.indexOf('<article class="book-page',start+1); const end=nextArticle<0?html.length:nextArticle;
 let article=html.slice(start,end);
 const re=/<div class="practice-cell arabic" lang="ar" dir="rtl">([^<]*)<\/div>/g;
 const cells=[...article.matchAll(re)].map(m=>m[1]); if(cells.length!==24)throw new Error(`${id}: expected 24 cells`);
 if(n===1){p1.forEach((v,i)=>cells[i]=v);} else {
   const A=introduced[n],R=cumulative(n-1),pairs=[];
   for(const x of A)for(const y of A)if(pairs.length<4)pairs.push(`${x} ${y}`);
   let ai=0,ri=(n*3)%R.length;
   while(pairs.length<8){const av=A[ai++%A.length],rv=R[ri++%R.length];pairs.push(pairs.length%2===0?`${av} ${rv}`:`${rv} ${av}`);}
   pairs.forEach((v,i)=>cells[i]=v);
 }
 let i=0;article=article.replace(re,()=>`<div class="practice-cell arabic" lang="ar" dir="rtl">${cells[i++]}</div>`);
 html=html.slice(0,start)+article+html.slice(end);
}
await fs.writeFile(file,html);
console.log("Applied early-page variety gate P001-P009 without introducing premature competencies.");

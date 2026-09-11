import fs from "node:fs/promises";
import path from "node:path";

const root=path.resolve(import.meta.dirname,"..");
const letters=["بَ","تَ","ثَ","ءَ","أَ","جَ","حَ","خَ","دَ","ذَ","رَ","زَ","سَ","شَ","صَ","ضَ","طَ","ظَ","عَ","غَ","فَ","قَ"];
let i=0;
const next=()=>letters[(i++)%letters.length];
const rows=[];
for(let r=0;r<2;r++) rows.push(Array.from({length:3},()=>`${next()} ${next()}`));
for(let r=0;r<6;r++) rows.push(Array.from({length:3},()=>`${next()} ${next()} ${next()}`));
const cells=rows.map(row=>`<div class="r">${row.map(x=>`<div class="c arabic">${x}</div>`).join("")}</div>`).join("");

async function patch(file,combined=false){
 let html=await fs.readFile(file,"utf8");
 if(combined){
   const marker='<span>QJ1-P010</span>';
   const end=html.lastIndexOf(marker);
   if(end<0) throw new Error('P010 marker missing in combined audit');
   const start=html.lastIndexOf('<main class="practice">',end);
   const close=html.indexOf('</main>',start)+7;
   html=html.slice(0,start)+`<main class="practice">${cells}</main>`+html.slice(close);
 }else{
   html=html.replace(/<main class="practice">[\s\S]*?<\/main>/,`<main class="practice">${cells}</main>`);
 }
 await fs.writeFile(file,html,"utf8");
}
await patch(path.join(root,'dist-p010/index.html'));
await patch(path.join(root,'dist-p004-p010/index.html'),true);
console.log('P010 evaluation coverage fixed: all learned fathah letters distributed across 8x3 grid');
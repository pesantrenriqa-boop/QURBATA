import fs from "node:fs/promises";
import path from "node:path";

const root = path.resolve(import.meta.dirname, "..");
const file = path.join(root, "dist/QURBATA-J1-P021-P030-AUDIT.html");
let html = await fs.readFile(file, "utf8");

const D={21:["بُ","تُ","ثُ","جُ"],22:["حُ","خُ","دُ","ذُ"],23:["رُ","زُ","سُ","شُ"],24:["صُ","ضُ","طُ","ظُ"],25:["عُ","غُ","فُ","قُ"],26:["كُ","لُ","مُ","نُ"],27:["هُ","وُ","يُ","ءُ","أُ"]};
const cumD=n=>Object.entries(D).filter(([s])=>Number(s)<=n).flatMap(([,x])=>x);
const preferred={
21:["بُ عِ ثَ","تُ رِ كَ","جُ عِ لَ","ثُ قِ لَ"],
22:["حُ فِ ظَ","خُ لِ قَ","دُ خِ لَ","ذُ كِ رَ"],
23:["رُ فِ عَ","سُ مِ عَ","شُ رِ بَ","زُ رِ عَ"],
24:["صُ بِ رَ","ضُ رِ بَ","طُ لِ بَ","ظُ لِ مَ"],
25:["عُ لِ مَ","غُ فِ رَ","فُ هِ مَ","قُ بِ لَ"],
26:["كُ تِ بَ","مُ لِ كَ","نُ ظِ رَ","لُ بِ سَ"],
27:["هُ دِ يَ","وُ جِ دَ","يُ سِ رَ","أُ خِ ذَ"],
28:["كُ تِ بَ","ضُ رِ بَ","ذُ كِ رَ","سُ مِ عَ"],
29:["عُ لِ مَ","حُ فِ ظَ","فُ هِ مَ","رُ حِ مَ"],
30:["جُ لِ سَ","شُ رِ بَ","رُ كِ بَ","قُ بِ لَ"]
};

for(let n=21;n<=30;n++){
  const id=`QJ1-P${String(n).padStart(3,"0")}`;
  const start=html.indexOf(`data-page-id="${id}"`);
  if(start<0) throw new Error(`${id} tidak ditemukan`);
  const next=html.indexOf('<article class="book-page',start+1);
  const end=next<0?html.length:next;
  let article=html.slice(start,end);
  const cellRe=/<div class="practice-cell arabic" lang="ar" dir="rtl">([^<]*)<\/div>/g;
  const cells=[...article.matchAll(cellRe)];
  if(cells.length!==24) throw new Error(`${id}: ${cells.length} cells, expected 24`);
  const values=cells.map(m=>m[1]);
  const active=cumD(Math.min(n,27));
  const offset=n*2;
  // Empat pasangan AR diubah menjadi AA untuk mengompensasi empat contoh bermakna
  // yang masing-masing memakai 1 Dhammah aktif + 2 murojaah. Rasio total tetap 38:26.
  [1,3,5,7].forEach((idx,j)=>{values[idx]=`${active[(offset+j*2)%active.length]} ${active[(offset+j*2+1)%active.length]}`;});
  preferred[n].forEach((v,j)=>{values[8+j]=v;});
  let i=0;
  article=article.replace(cellRe,()=>`<div class="practice-cell arabic" lang="ar" dir="rtl">${values[i++]}</div>`);
  html=html.slice(0,start)+article+html.slice(end);
}

await fs.writeFile(file,html);
console.log("Applied meaningful-practice gate P021-P030; ratio remains 38 active : 26 review tokens.");

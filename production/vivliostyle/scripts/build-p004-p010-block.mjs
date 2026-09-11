import fs from "node:fs/promises";
import path from "node:path";
import QRCode from "qrcode";

const root = path.resolve(import.meta.dirname, "..");
const pages = [
 {n:4,focus:"دَ ذَ رَ زَ",comp:"Dal, Dzal, Ra, Zai dengan Fathah",desc:"Membedakan dan membaca دَ ذَ رَ زَ bersama murojaah materi sebelumnya. Hanya huruf lepas berharakat fathah.",tahTitle:"An-Nas 4",tah:"مِنْ شَرِّ الْوَسْوَاسِ الْخَنَّاسِ",biah:"رَدِّدْ",akhTitle:"Ma'ruf",akh:"لَا تَحْقِرَنَّ مِنَ الْمَعْرُوفِ شَيْئًا",akhNote:"Biasakan menghargai setiap kebaikan.",active:["دَ","ذَ","رَ","زَ"],review:["بَ","تَ","ثَ","ءَ","أَ","جَ","حَ","خَ"]},
 {n:5,focus:"سَ شَ",comp:"Sin dan Syin dengan Fathah",desc:"Membedakan dan membaca سَ شَ bersama murojaah materi sebelumnya. Hanya huruf lepas berharakat fathah.",tahTitle:"An-Nas 5",tah:"الَّذِي يُوَسْوِسُ فِي صُدُورِ النَّاسِ",biah:"اِقْرَأْ",akhTitle:"Haya'",akh:"الْحَيَاءُ مِنَ الْإِيمَانِ",akhNote:"Tanamkan rasa malu yang menjaga adab.",active:["سَ","شَ"],review:["بَ","تَ","ثَ","جَ","حَ","خَ","دَ","ذَ","رَ","زَ"]},
 {n:6,focus:"صَ ضَ",comp:"Shad dan Dhad dengan Fathah",desc:"Membedakan dan membaca صَ ضَ bersama murojaah materi sebelumnya. Hanya huruf lepas berharakat fathah.",tahTitle:"An-Nas 6",tah:"مِنَ الْجِنَّةِ وَالنَّاسِ",biah:"أَعِدْ",akhTitle:"Rifq",akh:"إِنَّ اللَّهَ رَفِيقٌ يُحِبُّ الرِّفْقَ",akhNote:"Biasakan kelembutan dalam belajar dan berinteraksi.",active:["صَ","ضَ"],review:["سَ","شَ","دَ","ذَ","رَ","زَ","جَ","حَ","خَ"]},
 {n:7,focus:"طَ ظَ",comp:"Tha dan Zha dengan Fathah",desc:"Membedakan dan membaca طَ ظَ bersama murojaah materi sebelumnya. Hanya huruf lepas berharakat fathah.",tahTitle:"Al-Falaq 1",tah:"قُلْ أَعُوذُ بِرَبِّ الْفَلَقِ",biah:"مَرَّةً أُخْرَى",akhTitle:"Salam",akh:"أَفْشُوا السَّلَامَ بَيْنَكُمْ",akhNote:"Hidupkan salam dalam lingkungan belajar.",active:["طَ","ظَ"],review:["صَ","ضَ","سَ","شَ","دَ","ذَ","رَ","زَ"]},
 {n:8,focus:"عَ غَ",comp:"Ain dan Ghain dengan Fathah",desc:"Membedakan dan membaca عَ غَ bersama murojaah materi sebelumnya. Hanya huruf lepas berharakat fathah.",tahTitle:"Al-Falaq 2",tah:"مِنْ شَرِّ مَا خَلَقَ",biah:"نَعَمْ / لَا",akhTitle:"Ma'ruf",akh:"لَا تَحْقِرَنَّ مِنَ الْمَعْرُوفِ شَيْئًا",akhNote:"Biasakan menghargai setiap kebaikan.",active:["عَ","غَ"],review:["طَ","ظَ","صَ","ضَ","سَ","شَ","دَ","ذَ"]},
 {n:9,focus:"فَ قَ",comp:"Fa dan Qaf dengan Fathah",desc:"Membedakan dan membaca فَ قَ bersama murojaah materi sebelumnya. Hanya huruf lepas berharakat fathah.",tahTitle:"Al-Falaq 3",tah:"وَمِنْ شَرِّ غَاسِقٍ إِذَا وَقَبَ",biah:"أَحْسَنْتَ / أَحْسَنْتِ",akhTitle:"Niat",akh:"إِنَّمَا الْأَعْمَالُ بِالنِّيَّاتِ",akhNote:"Biasakan memulai amal dengan niat yang baik.",active:["فَ","قَ"],review:["عَ","غَ","طَ","ظَ","صَ","ضَ","سَ","شَ"]},
 {n:10,focus:"بَ تَ ثَ جَ حَ خَ دَ ذَ رَ زَ سَ شَ صَ ضَ طَ ظَ عَ غَ فَ قَ",comp:"Evaluasi Fathah I",desc:"Gate evaluasi: membaca dan membedakan seluruh huruf fathah yang telah dipelajari sampai P009. Tidak ada kompetensi baru.",tahTitle:"REVIEW GATE",tah:"قُلْ أَعُوذُ بِرَبِّ النَّاسِ",biah:"مُرَاجَعَةُ التَّعْلِيمَاتِ",akhTitle:"Istiqamah",akh:"أَحَبُّ الْأَعْمَالِ إِلَى اللَّهِ أَدْوَمُهَا وَإِنْ قَلَّ",akhNote:"Jaga konsistensi amal meskipun sedikit.",active:["بَ","تَ","ثَ","ءَ","أَ","جَ","حَ","خَ","دَ","ذَ","رَ","زَ","سَ","شَ","صَ","ضَ","طَ","ظَ","عَ","غَ","فَ","قَ"],review:[]}
];

function rowsFor(p){
 const a=p.active, r=p.review.length?p.review:p.active;
 const pick=(arr,i)=>arr[i%arr.length];
 const rows=[];
 rows.push([`${pick(a,0)} ${pick(a,1)}`,`${pick(a,1)} ${pick(a,2)}`,`${pick(a,2)} ${pick(a,0)}`]);
 rows.push([`${pick(a,1)} ${pick(a,0)}`,`${pick(a,0)} ${pick(a,2)}`,`${pick(a,2)} ${pick(a,1)}`]);
 for(let k=0;k<6;k++) rows.push([
   `${pick(a,k)} ${pick(a,k+1)} ${pick(r,k)}`,
   `${pick(a,k+1)} ${pick(r,k+2)} ${pick(a,k+2)}`,
   `${pick(r,k+3)} ${pick(a,k+2)} ${pick(a,k)}`
 ]);
 return rows;
}

let prevDir=path.join(root,"dist-p003");
const built=[];
for(const p of pages){
 const id=`P${String(p.n).padStart(3,"0")}`;
 const qid=`QJ1-${id}`;
 const out=path.join(root,`dist-p${String(p.n).padStart(3,"0")}`);
 await fs.rm(out,{recursive:true,force:true});
 await fs.cp(prevDir,out,{recursive:true});
 const file=path.join(out,"index.html");
 let html=await fs.readFile(file,"utf8");
 const url=`https://www.rumahilmualquran.com/q/${qid}`;
 const qr=await QRCode.toDataURL(url,{errorCorrectionLevel:"H",margin:1,width:300,color:{dark:"#123f34",light:"#fffdf6"}});
 const cells=rowsFor(p).map(row=>`<div class="r">${row.map(x=>`<div class="c arabic">${x}</div>`).join("")}</div>`).join("");
 html=html.replace(/<div class="num">\d{2}<\/div>/,`<div class="num">${String(p.n).padStart(2,"0")}</div>`);
 html=html.replace(/<div class="competency">[\s\S]*?<\/div><div class="letters">/,`<div class="competency"><b>${qid} · ${p.comp}</b><br>${p.desc}</div><div class="letters">`);
 const focusStyle=p.n===10?' style="font-size:11pt;word-spacing:.2em"':'';
 html=html.replace(/<div class="letters">[\s\S]*?<\/div><\/div><\/section><main class="practice">/,`<div class="letters"><small>${p.n===10?'EVALUASI FATHAH I':'HURUF YANG DIPELAJARI'}</small><div class="arabic"${focusStyle}>${p.focus}</div></div></section><main class="practice">`);
 html=html.replace(/<main class="practice">[\s\S]*?<\/main>/,`<main class="practice">${cells}</main>`);
 html=html.replace(/<section class="panels">[\s\S]*?<\/section><footer class="foot">/,`<section class="panels"><div class="panel"><h3>TAHFIDZ · ${p.tahTitle}</h3><div class="arabic">${p.tah}</div><small>${p.n===10?'Review hafalan; tidak ada hafalan baru.':'Talqin dan hafalkan ayat.'}</small></div><div class="panel"><h3>BI'AH ARABIYAH</h3><div class="arabic">${p.biah}</div><small>${p.n===10?'Review ungkapan kelas yang telah dipakai.':'Gunakan ungkapan ini dalam pembelajaran.'}</small></div><div class="panel"><h3>AKHLAK · ${p.akhTitle}</h3><div class="arabic">${p.akh}</div><small>${p.akhNote}</small></div><a class="panel qr" href="${url}"><h3>RIQA OS</h3><img src="${qr}"><div class="id">${qid}</div><small>Pindai untuk belajar</small></a></section><footer class="foot">`);
 html=html.replace(/<span>QJ1-P\d{3}<\/span>/,`<span>${qid}</span>`);
 await fs.writeFile(file,html,"utf8");
 built.push(html.match(/<article class="page">[\s\S]*?<\/article>/)?.[0]||"");
 prevDir=out;
}

// Combined audit book P004-P010, sharing the exact P004 CSS/font/ornament baseline.
const first=await fs.readFile(path.join(root,"dist-p004/index.html"),"utf8");
const combined=first.replace(/<article class="page">[\s\S]*?<\/article>/,built.join("\n"));
const block=path.join(root,"dist-p004-p010");
await fs.rm(block,{recursive:true,force:true});
await fs.mkdir(path.join(block,"fonts"),{recursive:true});
await fs.copyFile(path.join(root,"fonts/KFGQPC-Uthman-Taha-Naskh.woff2"),path.join(block,"fonts/KFGQPC-Uthman-Taha-Naskh.woff2"));
await fs.writeFile(path.join(block,"index.html"),combined,"utf8");
console.log("QJ1 P004-P010 frozen block generated: 7 pages + combined audit HTML");
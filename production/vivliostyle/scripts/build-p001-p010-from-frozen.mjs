import fs from "node:fs/promises";
import path from "node:path";
import QRCode from "qrcode";

const root=path.resolve(import.meta.dirname,"..");
const template=await fs.readFile(path.join(root,"templates/book.html"),"utf8");
const baseCss=await fs.readFile(path.join(root,"styles/book.css"),"utf8");
const SOURCE_REGISTER="03_BOOKS/JILID-1/PAGE_REGISTER_P001-P010_FROZEN-v1.0.md";
const esc=(v="")=>String(v).replaceAll("&","&amp;").replaceAll("<","&lt;").replaceAll(">","&gt;").replaceAll('"',"&quot;");

const introduced={
1:["بَ","تَ","ثَ"],2:["ءَ","أَ"],3:["جَ","حَ","خَ"],4:["دَ","ذَ","رَ","زَ"],5:["سَ","شَ"],6:["صَ","ضَ"],7:["طَ","ظَ"],8:["عَ","غَ"],9:["فَ","قَ"]
};
const cumulative=n=>Object.entries(introduced).filter(([p])=>Number(p)<=n).flatMap(([,x])=>x);
const specs=[
{n:1,a:"بَ تَ ثَ",c:"Mengenali dan membaca بَ تَ ثَ berharakat Fathah.",tf:["An-Nas 1","قُلْ أَعُوذُ بِرَبِّ النَّاسِ"],ba:["Salam","السَّلَامُ عَلَيْكُمْ"],ak:["Adab salam","أَفْشُوا السَّلَامَ بَيْنَكُمْ"],words:[]},
{n:2,a:"ءَ أَ",c:"Membedakan dan membaca ءَ dan أَ bersama murojaah بَ تَ ثَ.",tf:["An-Nas 2","مَلِكِ النَّاسِ"],ba:["Bacalah","اِقْرَأْ"],ak:["Adab belajar","وَقُلْ رَبِّ زِدْنِي عِلْمًا"],words:[]},
{n:3,a:"جَ حَ خَ",c:"Membaca جَ حَ خَ dengan murojaah kumulatif P001-P002.",tf:["An-Nas 3","إِلَهِ النَّاسِ"],ba:["Ulangi","أَعِدْ"],ak:["Mendengar","فَاسْتَمِعُوا لَهُ وَأَنْصِتُوا"],words:["بَ حَ ثَ","ثَ بَ تَ"]},
{n:4,a:"دَ ذَ رَ زَ",c:"Membaca دَ ذَ رَ زَ dengan murojaah kumulatif sejak P001.",tf:["An-Nas 4","مِنْ شَرِّ الْوَسْوَاسِ الْخَنَّاسِ"],ba:["Lihatlah","اُنْظُرْ"],ak:["Sabar","إِنَّ اللَّهَ مَعَ الصَّابِرِينَ"],words:["خَ رَ جَ","بَ دَ أَ","جَ رَ حَ"]},
{n:5,a:"سَ شَ",c:"Membaca سَ شَ; review tetap mencakup P001-P004 termasuk ءَ أَ.",tf:["An-Nas 5","الَّذِي يُوَسْوِسُ فِي صُدُورِ النَّاسِ"],ba:["Bukalah Al-Qur’an","اِفْتَحِ الْقُرْآنَ"],ak:["Bersungguh-sungguh","وَالَّذِينَ جَاهَدُوا فِينَا لَنَهْدِيَنَّهُمْ سُبُلَنَا"],words:["دَ رَ سَ","شَ رَ حَ","حَ رَ سَ"]},
{n:6,a:"صَ ضَ",c:"Membaca صَ ضَ dengan review kumulatif P001-P005.",tf:["An-Nas 6","مِنَ الْجِنَّةِ وَالنَّاسِ"],ba:["Tutuplah Al-Qur’an","أَغْلِقِ الْقُرْآنَ"],ak:["Bersyukur","لَئِنْ شَكَرْتُمْ لَأَزِيدَنَّكُمْ"],words:["صَ بَ رَ","ضَ رَ بَ"]},
{n:7,a:"طَ ظَ",c:"Membaca طَ ظَ dengan review kumulatif P001-P006.",tf:["Al-Falaq 1","قُلْ أَعُوذُ بِرَبِّ الْفَلَقِ"],ba:["Ini buku","هَذَا كِتَابٌ"],ak:["Berkata baik","وَقُولُوا لِلنَّاسِ حُسْنًا"],words:[]},
{n:8,a:"عَ غَ",c:"Membaca عَ غَ dengan review kumulatif P001-P007.",tf:["Al-Falaq 2","مِنْ شَرِّ مَا خَلَقَ"],ba:["Ini pena","هَذَا قَلَمٌ"],ak:["Rendah hati","وَعِبَادُ الرَّحْمَنِ الَّذِينَ يَمْشُونَ عَلَى الْأَرْضِ هَوْنًا"],words:["عَ بَ دَ","بَ عَ ثَ","رَ جَ عَ","خَ شَ عَ"]},
{n:9,a:"فَ قَ",c:"Membaca فَ قَ dengan review kumulatif seluruh P001-P008.",tf:["Al-Falaq 3","وَمِنْ شَرِّ غَاسِقٍ إِذَا وَقَبَ"],ba:["Ini halaman","هَذِهِ صَفْحَةٌ"],ak:["Menjaga kebersihan","إِنَّ اللَّهَ يُحِبُّ التَّوَّابِينَ وَيُحِبُّ الْمُتَطَهِّرِينَ"],words:["غَ فَ رَ","فَ تَ حَ","قَ رَ أَ","فَ رَ حَ","رَ فَ عَ","قَ طَ عَ"]},
{n:10,a:"تَقْيِيمُ الْفَتْحَةِ",c:"Evaluasi seluruh 22 bentuk Fathah P001-P009 tanpa materi baru.",tf:["Al-Falaq 4","وَمِنْ شَرِّ النَّفَّاثَاتِ فِي الْعُقَدِ"],ba:["Di sini","هُنَا"],ak:["Tolong-menolong","وَتَعَاوَنُوا عَلَى الْبِرِّ وَالتَّقْوَى"],eval:true,words:["غَ فَ رَ","فَ تَ حَ","قَ رَ أَ","عَ بَ دَ","بَ عَ ثَ","رَ جَ عَ","صَ بَ رَ","ضَ رَ بَ","دَ رَ سَ","شَ رَ حَ","خَ رَ جَ","بَ دَ أَ"]}
];
const next=(arr,s)=>arr[(s.i++)%arr.length];
const makeRows=s=>{
 if(s.eval){const pool=cumulative(9),st={i:0},g=[];for(let i=0;i<8;i++)g.push(`${next(pool,st)} ${next(pool,st)}`);for(let i=0;i<16;i++)g.push(s.words[i]||`${next(pool,st)} ${next(pool,st)} ${next(pool,st)}`);return Array.from({length:8},(_,r)=>g.slice(r*3,r*3+3));}
 const active=introduced[s.n], review=cumulative(s.n-1),a={i:s.n},r={i:s.n*2},g=[];
 if(!review.length){for(let i=0;i<8;i++)g.push(`${next(active,a)} ${next(active,a)}`);for(let i=0;i<16;i++)g.push(`${next(active,a)} ${next(active,a)} ${next(active,a)}`);}
 else {
   const p2=["AA","AA","AA","AA","AA","AA","RR","RR"];
   p2.forEach(p=>g.push([...p].map(x=>x==="A"?next(active,a):next(review,r)).join(" ")));
   const p3=[...Array(10).fill("AAR"),...Array(6).fill("ARR")];
   p3.forEach(p=>g.push([...p].map(x=>x==="A"?next(active,a):next(review,r)).join(" ")));
   (s.words||[]).forEach((w,i)=>{if(8+i<g.length)g[8+i]=w;});
 }
 return Array.from({length:8},(_,row)=>g.slice(row*3,row*3+3));
};
const css=`
.lesson-heading h1{font-size:17pt;line-height:1.02}.lesson-heading h1 .arabic-title{display:block;font-family:"QURBATA Uthmani",serif;font-size:28pt;color:#111;margin-top:.5mm}.lesson-heading p{font-size:7pt;line-height:1.15;margin:.7mm 2mm 0}.integration-card--akhlak h2{background:linear-gradient(90deg,#6b5b24,#9b7d2f)}.book-page.fatha{grid-template-rows:8mm 22mm 31mm 1fr 20mm 11mm;gap:1.8mm}.study-fields{display:grid;grid-template-columns:repeat(3,1fr);gap:2mm;margin-top:1.2mm;font-size:6.5pt}.study-fields span{border-top:.3mm solid #7da4b6;padding-top:.7mm;text-align:center}.practice-cell{font-size:25pt}.activity-strip{padding:1.5mm 3mm}
`;
const card=(label,v)=>`<section class="integration-card integration-card--${label.toLowerCase().replaceAll(" ","-")}"><h2>${esc(label)}</h2><p class="integration-title">${esc(v[0])}</p><p class="arabic integration-arabic" lang="ar" dir="rtl">${esc(v[1])}</p><p class="integration-instruction">Praktikkan secara nyata dalam pembelajaran.</p></section>`;
const out=[];
for(const s of specs){const rows=makeRows(s);if(rows.length!==8||rows.some(r=>r.length!==3))throw new Error(`P${s.n} grid invalid`);const url=`https://www.rumahilmualquran.com/q/QJ1-P${String(s.n).padStart(3,"0")}`;const qr=await QRCode.toDataURL(url,{errorCorrectionLevel:"H",margin:1,width:220});const rowhtml=rows.map(r=>`<div class="practice-row">${r.map(x=>`<div class="practice-cell arabic" lang="ar" dir="rtl">${esc(x)}</div>`).join("")}</div>`).join("");out.push(`<article class="book-page fatha" data-page-id="QJ1-P${String(s.n).padStart(3,"0")}"><header class="page-header"><div class="header-line"></div><div class="book-name">QURBATA JILID 1</div><div class="page-number">${String(s.n).padStart(2,"0")}</div></header><section class="lesson-heading"><h1>${s.eval?"Evaluasi Fathah I":"Mari Membaca"}<span class="arabic-title" lang="ar" dir="rtl">${esc(s.a)}</span></h1><p><strong>Kompetensi Tartil:</strong> ${esc(s.c)}</p></section><div class="integration-grid">${card("TAHFIDZ",s.tf)}${card("BAHASA ARAB",s.ba)}${card("AKHLAK",s.ak)}</div><section class="practice-panel"><header><h2>LATIHAN TARTIL</h2><p>${s.eval?"Evaluasi cakupan 22 bentuk Fathah":"Bacalah dengan tartil dan jelas."}</p></header><div class="practice-grid">${rowhtml}</div></section><section class="activity-strip"><div class="activity-content"><h2>AKTIVITAS BI’AH QURBATA</h2><div class="study-fields"><span>Tanggal: __________</span><span>Nilai: __________</span><span>TTD: __________</span></div></div><a class="qr-link" href="${url}"><img src="${qr}" alt="QR"><span>RIQA OS</span></a></section><footer class="page-footer"><div><span class="page-id">QJ1-P${String(s.n).padStart(3,"0")}</span><span>AUDIT — ${SOURCE_REGISTER}</span></div><p class="arabic" lang="ar" dir="rtl">تَعَلَّمْ — اِعْمَلْ — عَلِّمْ</p><small>Belajarlah • Amalkan • Ajarkan</small></footer></article>`);}
const html=template.replace("/*__BOOK_CSS__*/",`${baseCss}\n${css}`).replace("<!--__BOOK_PAGES__-->",out.join("\n"));
await fs.mkdir(path.join(root,"dist"),{recursive:true});
await fs.writeFile(path.join(root,"dist/QURBATA-J1-P001-P010-AUDIT.html"),html);
console.log(`Built P001-P010 from ${SOURCE_REGISTER}`);

import fs from "node:fs/promises";
import path from "node:path";
import QRCode from "qrcode";

const root = path.resolve(import.meta.dirname, "..");
const template = await fs.readFile(path.join(root, "templates/book.html"), "utf8");
const baseCss = await fs.readFile(path.join(root, "styles/book.css"), "utf8");
const SOURCE_REGISTER = "03_BOOKS/JILID-1/PAGE_REGISTER_P021-P030_FROZEN-v1.0.md";
const esc=(v="")=>String(v).replaceAll("&","&amp;").replaceAll("<","&lt;").replaceAll(">","&gt;").replaceAll('"',"&quot;");

const F=["بَ","تَ","ثَ","ءَ","أَ","جَ","حَ","خَ","دَ","ذَ","رَ","زَ","سَ","شَ","صَ","ضَ","طَ","ظَ","عَ","غَ","فَ","قَ","كَ","لَ","مَ","نَ","هَ","وَ","يَ"];
const K=["بِ","تِ","ثِ","ءِ","إِ","جِ","حِ","خِ","دِ","ذِ","رِ","زِ","سِ","شِ","صِ","ضِ","طِ","ظِ","عِ","غِ","فِ","قِ","كِ","لِ","مِ","نِ","هِ","وِ","يِ"];
const D={21:["بُ","تُ","ثُ","جُ"],22:["حُ","خُ","دُ","ذُ"],23:["رُ","زُ","سُ","شُ"],24:["صُ","ضُ","طُ","ظُ"],25:["عُ","غُ","فُ","قُ"],26:["كُ","لُ","مُ","نُ"],27:["هُ","وُ","يُ","ءُ","أُ"]};
const cumD=n=>Object.entries(D).filter(([s])=>Number(s)<=n).flatMap(([,x])=>x);

const specs=[
{n:21,t:"Dhammah 1",a:"الضَّمَّةُ ١",c:"Penanaman Dhammah pada بُ تُ ثُ جُ; Fathah dan Kasrah tetap murojaah kumulatif.",tf:["An-Nasr 1","إِذَا جَاءَ نَصْرُ اللَّهِ وَالْفَتْحُ"],ba:["Benar","صَحِيحٌ"],ak:["Amanah","أَدِّ الْأَمَانَةَ إِلَى مَنِ ائْتَمَنَكَ"],intro:[["بِ","بُ"],["تِ","تُ"],["ثِ","ثُ"],["جِ","جُ"]]},
{n:22,t:"Dhammah 2",a:"الضَّمَّةُ ٢",c:"Dhammah baru حُ خُ دُ ذُ; Dhammah P021 tetap aktif dan Fathah–Kasrah tetap cumulative review.",tf:["An-Nasr 2","وَرَأَيْتَ النَّاسَ يَدْخُلُونَ فِي دِينِ اللَّهِ أَفْوَاجًا"],ba:["Coba lagi","حَاوِلْ مَرَّةً أُخْرَى"],ak:["Mencintai saudara","لَا يُؤْمِنُ أَحَدُكُمْ حَتَّى يُحِبَّ لِأَخِيهِ مَا يُحِبُّ لِنَفْسِهِ"],intro:[["حِ","حُ"],["خِ","خُ"],["دِ","دُ"],["ذِ","ذُ"]]},
{n:23,t:"Dhammah 3",a:"الضَّمَّةُ ٣",c:"Dhammah baru رُ زُ سُ شُ dengan perpindahan Fathah–Kasrah–Dhammah yang legal.",tf:["An-Nasr 3","فَسَبِّحْ بِحَمْدِ رَبِّكَ وَاسْتَغْفِرْهُ إِنَّهُ كَانَ تَوَّابًا"],ba:["Siap","مُسْتَعِدٌّ"],ak:["Memberi salam","أَفْشُوا السَّلَامَ بَيْنَكُمْ"],intro:[["رِ","رُ"],["زِ","زُ"],["سِ","سُ"],["شِ","شُ"]]},
{n:24,t:"Dhammah 4",a:"الضَّمَّةُ ٤",c:"Dhammah baru صُ ضُ طُ ظُ; seluruh kompetensi lama tetap berputar.",tf:["Al-Kafirun 1","قُلْ يَا أَيُّهَا الْكَافِرُونَ"],ba:["Saya siap","أَنَا مُسْتَعِدٌّ"],ak:["Tersenyum","تَبَسُّمُكَ فِي وَجْهِ أَخِيكَ لَكَ صَدَقَةٌ"],intro:[["صِ","صُ"],["ضِ","ضُ"],["طِ","طُ"],["ظِ","ظُ"]]},
{n:25,t:"Dhammah 5",a:"الضَّمَّةُ ٥",c:"Dhammah baru عُ غُ فُ قُ dengan cumulative review sejak P001.",tf:["Al-Kafirun 2","لَا أَعْبُدُ مَا تَعْبُدُونَ"],ba:["Giliran saya","دَوْرِي"],ak:["Menjaga waktu","إِنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا"],intro:[["عِ","عُ"],["غِ","غُ"],["فِ","فُ"],["قِ","قُ"]]},
{n:26,t:"Dhammah 6",a:"الضَّمَّةُ ٦",c:"Dhammah baru كُ لُ مُ نُ; tidak ada Dhammah prematur pada huruf lain.",tf:["Al-Kafirun 3","وَلَا أَنْتُمْ عَابِدُونَ مَا أَعْبُدُ"],ba:["Giliranmu","دَوْرُكَ"],ak:["Tidak berlebihan","وَلَا تُسْرِفُوا"],intro:[["كِ","كُ"],["لِ","لُ"],["مِ","مُ"],["نِ","نُ"]]},
{n:27,t:"Dhammah 7",a:"الضَّمَّةُ ٧",c:"Penuntasan Dhammah pada هُ وُ يُ ءُ أُ dengan audit grafem Hamzah/Alif.",tf:["Al-Kafirun 4","وَلَا أَنَا عَابِدٌ مَا عَبَدْتُمْ"],ba:["Bersama-sama","مَعًا"],ak:["Memaafkan","وَلْيَعْفُوا وَلْيَصْفَحُوا"],intro:[["هِ","هُ"],["وِ","وُ"],["يِ","يُ"],["ءِ","ءُ"],["إِ","أُ"]]},
{n:28,t:"Penguatan Dhammah",a:"تَثْبِيتُ الضَّمَّةِ",c:"Penguatan seluruh Dhammah dengan cumulative review Kasrah dan Fathah; tanpa harakat baru.",tf:["Al-Kafirun 5","وَلَا أَنْتُمْ عَابِدُونَ مَا أَعْبُدُ"],ba:["Sendiri","وَحْدِي"],ak:["Berlomba dalam kebaikan","فَاسْتَبِقُوا الْخَيْرَاتِ"]},
{n:29,t:"Latihan Kumulatif Dhammah 1",a:"تَدْرِيبُ الضَّمَّةِ ١",c:"Latihan kumulatif Fathah–Kasrah–Dhammah pada huruf lepas; tanpa kompetensi baru.",tf:["Al-Kafirun 6","لَكُمْ دِينُكُمْ وَلِيَ دِينِ"],ba:["Apa ini?","مَا هَذَا؟"],ak:["Tawakal","وَعَلَى اللَّهِ فَتَوَكَّلُوا"]},
{n:30,t:"Latihan Kumulatif Dhammah 2",a:"تَدْرِيبُ الضَّمَّةِ ٢",c:"Penguatan perpindahan Fathah–Kasrah–Dhammah dengan murojaah kumulatif sejak P001.",tf:["Al-Kawthar 1","إِنَّا أَعْطَيْنَاكَ الْكَوْثَرَ"],ba:["Ini Al-Qur’an","هَذَا الْقُرْآنُ"],ak:["Istiqamah","فَاسْتَقِمْ كَمَا أُمِرْتَ"]}
];

const next=(arr,s)=>arr[(s.i++)%arr.length];
const rowsFor=spec=>{
  const active=cumD(Math.min(spec.n,27));
  const review=[...F,...K];
  const a={i:spec.n*3},r={i:spec.n*5},groups=[];
  // 8 dua-huruf = 16 token: 10 aktif + 6 review.
  const p2=["AA","AR","AA","AR","AA","AR","AA","AR"];
  p2.forEach(p=>groups.push([...p].map(x=>x==="A"?next(active,a):next(review,r)).join(" ")));
  // 16 tiga-huruf = 48 token: 28 aktif + 20 review. Total 38:26 = 59.4:40.6.
  const p3=[...Array(12).fill("AAR"),...Array(4).fill("ARR")];
  p3.forEach(p=>groups.push([...p].map(x=>x==="A"?next(active,a):next(review,r)).join(" ")));
  return Array.from({length:8},(_,i)=>groups.slice(i*3,i*3+3));
};

const css=`
.lesson-heading h1{font-size:17pt;line-height:1.02}.lesson-heading h1 .arabic-title{display:block;font-family:"QURBATA Uthmani",serif;font-size:23pt;color:#111;margin-top:.5mm}.lesson-heading p{font-size:7pt;line-height:1.15;margin:.7mm 2mm 0}.integration-grid{grid-template-columns:repeat(3,1fr)}
.integration-card--akhlak h2{background:linear-gradient(90deg,#6b5b24,#9b7d2f)}
.book-page.has-intro{grid-template-rows:8mm 20mm 29mm 29mm 1fr 20mm 11mm;gap:1.5mm}.book-page.no-intro{grid-template-rows:8mm 20mm 31mm 1fr 20mm 11mm;gap:1.8mm}
.planting{border:.5mm solid #0f8f91;border-radius:2.5mm;background:#f2fffe;display:grid;grid-template-rows:1fr 1fr;overflow:hidden}.plant-row{display:flex;justify-content:space-evenly;align-items:center;border-top:.25mm solid #8fdad6}.plant-row:first-child{border-top:0}.plant-pair{font-family:"QURBATA Uthmani",serif;font-size:24pt;direction:rtl;white-space:nowrap;color:#111}.plant-label{font-size:6.5pt;font-weight:800;color:#0f6d70;margin-right:2mm}
.study-fields{display:grid;grid-template-columns:repeat(3,1fr);gap:2mm;margin-top:1.2mm;font-size:6.5pt}.study-fields span{border-top:.3mm solid #7da4b6;padding-top:.7mm;text-align:center}.practice-cell{font-size:24pt}.activity-strip{padding:1.5mm 3mm}
`;
const card=(label,v)=>`<section class="integration-card integration-card--${label.toLowerCase().replaceAll(" ","-")}"><h2>${esc(label)}</h2><p class="integration-title">${esc(v[0])}</p><p class="arabic integration-arabic" lang="ar" dir="rtl">${esc(v[1])}</p><p class="integration-instruction">Praktikkan secara nyata dalam pembelajaran.</p></section>`;

const out=[];
for(const s of specs){
 const rows=rowsFor(s); if(rows.length!==8||rows.some(x=>x.length!==3))throw new Error(`P${s.n} bukan 8x3`);
 const url=`https://www.rumahilmualquran.com/q/QJ1-P${String(s.n).padStart(3,"0")}`; const qr=await QRCode.toDataURL(url,{errorCorrectionLevel:"H",margin:1,width:220});
 let plant=""; if(s.intro){const half=Math.ceil(s.intro.length/2); const render=x=>x.map(([oldv,newv])=>`<span class="plant-pair">${esc(oldv)} ← ${esc(newv)}</span>`).join(""); plant=`<section class="planting"><div class="plant-row"><span class="plant-label">PENANAMAN</span>${render(s.intro.slice(0,half))}</div><div class="plant-row"><span class="plant-label">PENANAMAN</span>${render(s.intro.slice(half))}</div></section>`;}
 const rowhtml=rows.map(r=>`<div class="practice-row">${r.map(x=>`<div class="practice-cell arabic" lang="ar" dir="rtl">${esc(x)}</div>`).join("")}</div>`).join("");
 out.push(`<article class="book-page ${s.intro?"has-intro":"no-intro"}" data-page-id="QJ1-P${String(s.n).padStart(3,"0")}"><header class="page-header"><div class="header-line"></div><div class="book-name">QURBATA JILID 1</div><div class="page-number">${String(s.n).padStart(2,"0")}</div></header><section class="lesson-heading"><h1>${esc(s.t)}<span class="arabic-title" lang="ar" dir="rtl">${esc(s.a)}</span></h1><p><strong>Kompetensi Tartil:</strong> ${esc(s.c)}</p></section><div class="integration-grid">${card("TAHFIDZ",s.tf)}${card("BAHASA ARAB",s.ba)}${card("AKHLAK",s.ak)}</div>${plant}<section class="practice-panel"><header><h2>LATIHAN TARTIL</h2><p>Bacalah dengan tartil dan jelas.</p></header><div class="practice-grid">${rowhtml}</div></section><section class="activity-strip"><div class="activity-content"><h2>AKTIVITAS BI’AH QURBATA</h2><div class="study-fields"><span>Tanggal: __________</span><span>Nilai: __________</span><span>TTD: __________</span></div></div><a class="qr-link" href="${url}"><img src="${qr}" alt="QR"><span>RIQA OS</span></a></section><footer class="page-footer"><div><span class="page-id">QJ1-P${String(s.n).padStart(3,"0")}</span><span>AUDIT — ${SOURCE_REGISTER}</span></div><p class="arabic" lang="ar" dir="rtl">تَعَلَّمْ — اِعْمَلْ — عَلِّمْ</p><small>Belajarlah • Amalkan • Ajarkan</small></footer></article>`);
}
const html=template.replace("/*__BOOK_CSS__*/",`${baseCss}\n${css}`).replace("<!--__BOOK_PAGES__-->",out.join("\n"));
await fs.mkdir(path.join(root,"dist"),{recursive:true});
await fs.writeFile(path.join(root,"dist/QURBATA-J1-P021-P030-AUDIT.html"),html);
console.log(`Built P021-P030 from ${SOURCE_REGISTER}`);

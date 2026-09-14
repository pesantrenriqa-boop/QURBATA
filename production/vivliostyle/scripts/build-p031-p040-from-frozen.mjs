import fs from "node:fs/promises";
import path from "node:path";
import QRCode from "qrcode";

const root = path.resolve(import.meta.dirname, "..");
const template = await fs.readFile(path.join(root, "templates/book.html"), "utf8");
const baseCss = await fs.readFile(path.join(root, "styles/book.css"), "utf8");
const SOURCE_REGISTER = "03_BOOKS/JILID-1/PAGE_REGISTER_P031-P040_FROZEN-v1.0.md";
const esc=(v="")=>String(v).replaceAll("&","&amp;").replaceAll("<","&lt;").replaceAll(">","&gt;").replaceAll('"',"&quot;");

const LETTERS29=["ا","ب","ت","ث","ج","ح","خ","د","ذ","ر","ز","س","ش","ص","ض","ط","ظ","ع","غ","ف","ق","ك","ل","م","ن","ه","و","ي","ء"];

// Bank bentuk Arab sah. Huruf sengaja dipisah visual untuk menjaga aturan huruf lepas Jilid 1.
const WORDS=[
"كَ تَ بَ","عَ لِ مَ","فَ هِ مَ","عَ مِ لَ","سَ مِ عَ","رَ حِ مَ","شَ رِ بَ","رَ كِ بَ",
"جَ لِ سَ","لَ بِ سَ","فَ رِ حَ","حَ مِ دَ","نَ دِ مَ","مَ لِ كَ","كَ بِ رَ","صَ غِ رَ",
"كُ تِ بَ","ضُ رِ بَ","ذُ كِ رَ","سُ مِ عَ","عُ لِ مَ","حُ فِ ظَ","فُ هِ مَ","رُ حِ مَ",
"جُ لِ سَ","شُ رِ بَ","رُ كِ بَ","قُ بِ لَ","نُ صِ رَ","مُ نِ عَ","أُ خِ ذَ","أُ مِ رَ",
"وُ جِ دَ","هُ دِ يَ","خُ لِ قَ","دُ خِ لَ","رُ فِ عَ","زُ رِ عَ","صُ بِ رَ","طُ لِ بَ",
"غُ فِ رَ","فُ تِ حَ","قُ رِ ئَ","عُ رِ فَ","نَ صَ رَ","مَ نَ عَ","نَ فَ عَ","وَ جَ دَ"
];

const specs=[
{n:31,t:"Penguatan Kumulatif 1",a:"مُرَاجَعَةٌ تَرَاكُمِيَّةٌ ١",c:"Penguatan Fathah–Kasrah–Dhammah pada huruf lepas tanpa kompetensi baru.",tf:["Al-Kawthar 2","فَصَلِّ لِرَبِّكَ وَانْحَرْ"],ba:["Mana buku?","أَيْنَ الْكِتَابُ؟"],ak:["Menjaga persaudaraan","إِنَّمَا الْمُؤْمِنُونَ إِخْوَةٌ"]},
{n:32,t:"Penguatan Kumulatif 2",a:"مُرَاجَعَةٌ تَرَاكُمِيَّةٌ ٢",c:"Penguatan perpindahan Fathah–Kasrah–Dhammah termasuk grafem Hamzah/Alif yang telah legal.",tf:["Al-Kawthar 3","إِنَّ شَانِئَكَ هُوَ الْأَبْتَرُ"],ba:["Buku di sini","الْكِتَابُ هُنَا"],ak:["Tidak sombong","إِنَّ اللَّهَ لَا يُحِبُّ كُلَّ مُخْتَالٍ فَخُورٍ"]},
{n:33,t:"Penguatan Kumulatif 3",a:"مُرَاجَعَةٌ تَرَاكُمِيَّةٌ ٣",c:"Penguatan seluruh tiga harakat pada rentang 29 identitas huruf tanpa kompetensi baru.",tf:["Al-Ma'un 1","أَرَأَيْتَ الَّذِي يُكَذِّبُ بِالدِّينِ"],ba:["Ambil bukumu","خُذْ كِتَابَكَ"],ak:["Pemaaf","وَالْعَافِينَ عَنِ النَّاسِ"]},
{n:34,t:"Latihan Kumulatif Akhir 1",a:"تَدْرِيبٌ تَرَاكُمِيٌّ ١",c:"Kelompok tiga huruf lepas berbasis bentuk Arab sah dengan tiga harakat yang telah legal.",tf:["Al-Ma'un 2","فَذَلِكَ الَّذِي يَدُعُّ الْيَتِيمَ"],ba:["Letakkan bukumu","ضَعْ كِتَابَكَ"],ak:["Dermawan","لَنْ تَنَالُوا الْبِرَّ حَتَّى تُنْفِقُوا مِمَّا تُحِبُّونَ"]},
{n:35,t:"Latihan Kumulatif Akhir 2",a:"تَدْرِيبٌ تَرَاكُمِيٌّ ٢",c:"Kelancaran perpindahan Fathah–Kasrah–Dhammah tanpa mengubah pola harakat kata secara palsu.",tf:["Al-Ma'un 3","وَلَا يَحُضُّ عَلَى طَعَامِ الْمِسْكِينِ"],ba:["Buka halaman","اِفْتَحِ الصَّفْحَةَ"],ak:["Menjaga pandangan","قُلْ لِلْمُؤْمِنِينَ يَغُضُّوا مِنْ أَبْصَارِهِمْ"]},
{n:36,t:"Penguatan Jilid 1 — 1",a:"مُرَاجَعَةُ الْجُزْءِ الْأَوَّلِ ١",c:"Latihan evaluatif kumulatif seluruh Fathah–Kasrah–Dhammah.",tf:["Al-Ma'un 4","فَوَيْلٌ لِلْمُصَلِّينَ"],ba:["Tunjukkan","أَشِرْ"],ak:["Berdoa","ادْعُونِي أَسْتَجِبْ لَكُمْ"]},
{n:37,t:"Penguatan Jilid 1 — 2",a:"مُرَاجَعَةُ الْجُزْءِ الْأَوَّلِ ٢",c:"Penguatan akurasi bunyi dan murojaah kompetensi sejak P001.",tf:["Al-Ma'un 5","الَّذِينَ هُمْ عَنْ صَلَاتِهِمْ سَاهُونَ"],ba:["Ikuti saya","اِتَّبِعْنِي"],ak:["Mengingat Allah","فَاذْكُرُونِي أَذْكُرْكُمْ"]},
{n:38,t:"Penguatan Jilid 1 — 3",a:"مُرَاجَعَةُ الْجُزْءِ الْأَوَّلِ ٣",c:"Penguatan tiga harakat dengan integritas bentuk Arab yang sah.",tf:["Al-Ma'un 6","الَّذِينَ هُمْ يُرَاءُونَ"],ba:["Dengarkan guru","اِسْتَمِعْ إِلَى الْمُعَلِّمِ"],ak:["Membaca dengan tartil","وَرَتِّلِ الْقُرْآنَ تَرْتِيلًا"]},
{n:39,t:"Pra-Checkpoint",a:"التَّهْيِئَةُ لِلتَّقْيِيمِ",c:"Simulasi penguatan akhir seluruh Fathah–Kasrah–Dhammah sebelum checkpoint P040.",tf:["Al-Ma'un 7","وَيَمْنَعُونَ الْمَاعُونَ"],ba:["Terima kasih","شُكْرًا"],ak:["Mengamalkan ilmu","تَعَلَّمْ — اِعْمَلْ — عَلِّمْ"]},
{n:40,t:"Checkpoint Akhir Jilid 1",a:"التَّقْيِيمُ الْخِتَامِيُّ",c:"Checkpoint seluruh kompetensi Fathah–Kasrah–Dhammah; tanpa kompetensi baru.",tf:["Murojaah Jilid 1","مُرَاجَعَةٌ شَامِلَةٌ"],ba:["Alhamdulillah","الْحَمْدُ لِلَّهِ"],ak:["Penutup adab","خَيْرُكُمْ أَحْسَنُكُمْ أَخْلَاقًا"],checkpoint:true}
];

const rowsFor=n=>{
  const offset=(n-31)*5;
  const vals=Array.from({length:24},(_,i)=>WORDS[(offset+i)%WORDS.length]);
  return Array.from({length:8},(_,r)=>vals.slice(r*3,r*3+3));
};

const css=`
.lesson-heading h1{font-size:17pt;line-height:1.02}.lesson-heading h1 .arabic-title{display:block;font-family:"QURBATA Uthmani",serif;font-size:22pt;color:#111;margin-top:.4mm}.lesson-heading p{font-size:7pt;line-height:1.15;margin:.7mm 2mm 0}
.integration-card--akhlak h2{background:linear-gradient(90deg,#6b5b24,#9b7d2f)}
.book-page.cumulative{grid-template-rows:8mm 20mm 31mm 1fr 20mm 11mm;gap:1.8mm}.book-page.final-checkpoint{grid-template-rows:8mm 20mm 28mm 31mm 1fr 20mm 11mm;gap:1.5mm}
.study-fields{display:grid;grid-template-columns:repeat(3,1fr);gap:2mm;margin-top:1.2mm;font-size:6.5pt}.study-fields span{border-top:.3mm solid #7da4b6;padding-top:.7mm;text-align:center}.practice-cell{font-size:23pt}.activity-strip{padding:1.5mm 3mm}
.final-check{border:.45mm solid #0879bd;border-radius:2.5mm;background:#f7fcff;padding:1.3mm 2mm;display:grid;grid-template-rows:auto 1fr auto;gap:1mm}.final-check h2{font-size:8pt;margin:0;color:#075985;text-align:center}.letters29{font-family:"QURBATA Uthmani",serif;direction:rtl;display:flex;flex-wrap:wrap;justify-content:center;gap:1.4mm 3mm;font-size:15pt;line-height:1.05}.harakat3{text-align:center;font-size:6.8pt}.harakat3 .arabic{font-size:12pt;margin:0 1mm}
`;
const card=(label,v)=>`<section class="integration-card integration-card--${label.toLowerCase().replaceAll(" ","-")}"><h2>${esc(label)}</h2><p class="integration-title">${esc(v[0])}</p><p class="arabic integration-arabic" lang="ar" dir="rtl">${esc(v[1])}</p><p class="integration-instruction">Praktikkan secara nyata dalam pembelajaran.</p></section>`;

const out=[];
for(const s of specs){
 const rows=rowsFor(s.n); const url=`https://www.rumahilmualquran.com/q/QJ1-P${String(s.n).padStart(3,"0")}`; const qr=await QRCode.toDataURL(url,{errorCorrectionLevel:"H",margin:1,width:220});
 const check=s.checkpoint?`<section class="final-check"><h2>CHECKPOINT HURUF & HARAKAT</h2><div class="letters29" lang="ar" dir="rtl">${LETTERS29.map(x=>`<span>${x}</span>`).join("")}</div><div class="harakat3"><strong>Fathah</strong> <span class="arabic">فَتْحَة</span> • <strong>Kasrah</strong> <span class="arabic">كَسْرَة</span> • <strong>Dhammah</strong> <span class="arabic">ضَمَّة</span></div></section>`:"";
 const rowhtml=rows.map(r=>`<div class="practice-row">${r.map(x=>`<div class="practice-cell arabic" lang="ar" dir="rtl">${esc(x)}</div>`).join("")}</div>`).join("");
 out.push(`<article class="book-page ${s.checkpoint?"final-checkpoint":"cumulative"}" data-page-id="QJ1-P${String(s.n).padStart(3,"0")}"><header class="page-header"><div class="header-line"></div><div class="book-name">QURBATA JILID 1</div><div class="page-number">${String(s.n).padStart(2,"0")}</div></header><section class="lesson-heading"><h1>${esc(s.t)}<span class="arabic-title" lang="ar" dir="rtl">${esc(s.a)}</span></h1><p><strong>Kompetensi Tartil:</strong> ${esc(s.c)}</p></section><div class="integration-grid">${card("TAHFIDZ",s.tf)}${card("BAHASA ARAB",s.ba)}${card("AKHLAK",s.ak)}</div>${check}<section class="practice-panel"><header><h2>LATIHAN TARTIL</h2><p>${s.checkpoint?"Evaluasi akhir Jilid 1":"Bacalah dengan tartil dan jelas."}</p></header><div class="practice-grid">${rowhtml}</div></section><section class="activity-strip"><div class="activity-content"><h2>AKTIVITAS BI’AH QURBATA</h2><div class="study-fields"><span>Tanggal: __________</span><span>Nilai: __________</span><span>TTD: __________</span></div></div><a class="qr-link" href="${url}"><img src="${qr}" alt="QR"><span>RIQA OS</span></a></section><footer class="page-footer"><div><span class="page-id">QJ1-P${String(s.n).padStart(3,"0")}</span><span>AUDIT — ${SOURCE_REGISTER}</span></div><p class="arabic" lang="ar" dir="rtl">تَعَلَّمْ — اِعْمَلْ — عَلِّمْ</p><small>Belajarlah • Amalkan • Ajarkan</small></footer></article>`);
}
const html=template.replace("/*__BOOK_CSS__*/",`${baseCss}\n${css}`).replace("<!--__BOOK_PAGES__-->",out.join("\n"));
await fs.mkdir(path.join(root,"dist"),{recursive:true});
await fs.writeFile(path.join(root,"dist/QURBATA-J1-P031-P040-AUDIT.html"),html);
console.log(`Built P031-P040 from ${SOURCE_REGISTER}`);

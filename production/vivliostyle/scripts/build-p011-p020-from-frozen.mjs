import fs from "node:fs/promises";
import path from "node:path";
import QRCode from "qrcode";

const root = path.resolve(import.meta.dirname, "..");
const template = await fs.readFile(path.join(root, "templates/book.html"), "utf8");
const baseCss = await fs.readFile(path.join(root, "styles/book.css"), "utf8");

const SOURCE_REGISTER = "03_BOOKS/JILID-1/PAGE_REGISTER_P011-P020_FROZEN-v1.0.md";

const esc = (v = "") => String(v)
  .replaceAll("&", "&amp;")
  .replaceAll("<", "&lt;")
  .replaceAll(">", "&gt;")
  .replaceAll('"', "&quot;");

const FATHA_ALL = [
  "بَ","تَ","ثَ","ءَ","أَ","جَ","حَ","خَ","دَ","ذَ","رَ","زَ","سَ","شَ",
  "صَ","ضَ","طَ","ظَ","عَ","غَ","فَ","قَ","كَ","لَ","مَ","نَ","هَ","وَ","يَ"
];

const kasraByStage = {
  14: ["بِ","تِ","ثِ","جِ"],
  15: ["حِ","خِ","دِ","ذِ"],
  16: ["رِ","زِ","سِ","شِ"],
  17: ["صِ","ضِ","طِ","ظِ"],
  18: ["عِ","غِ","فِ","قِ"],
  19: ["كِ","لِ","مِ","نِ","هِ","وِ","يِ","ءِ","إِ"]
};

const pageSpecs = [
  {
    n: 11, title: "Mari Membaca", titleArabic: "كَ لَ", active: ["كَ","لَ"],
    competency: "Membedakan dan membaca كَ لَ bersama murojaah kumulatif P001–P010.",
    tahfidz: ["Al-Falaq 5", "وَمِنْ شَرِّ حَاسِدٍ إِذَا حَسَدَ"],
    arabic: ["Di sana", "هُنَاكَ"], akhlak: ["Menepati janji", "وَأَوْفُوا بِالْعَهْدِ"],
    triples: ["كَ تَ بَ","أَ كَ لَ","شَ كَ رَ","خَ لَ قَ","جَ عَ لَ","دَ خَ لَ","سَ لَ كَ"]
  },
  {
    n: 12, title: "Mari Membaca", titleArabic: "مَ نَ", active: ["مَ","نَ"],
    competency: "Membedakan dan membaca مَ نَ bersama murojaah kumulatif sejak P001.",
    tahfidz: ["Al-Ikhlas 1", "قُلْ هُوَ اللَّهُ أَحَدٌ"],
    arabic: ["Duduklah", "اِجْلِسْ"], akhlak: ["Jujur", "وَكُونُوا مَعَ الصَّادِقِينَ"],
    triples: ["حَ مَ دَ","رَ حَ مَ","عَ مَ لَ","مَ لَ كَ","نَ صَ رَ","مَ نَ عَ","نَ فَ عَ","أَ مَ نَ","سَ مَ عَ","جَ مَ عَ"]
  },
  {
    n: 13, title: "Mari Membaca", titleArabic: "هَ وَ يَ", active: ["هَ","وَ","يَ"],
    competency: "Membedakan dan membaca هَ وَ يَ bersama murojaah; وَ tetap pendek dan bukan mad.",
    tahfidz: ["Al-Ikhlas 2", "اللَّهُ الصَّمَدُ"],
    arabic: ["Berdirilah", "قُمْ"], akhlak: ["Tidak mengejek", "لَا يَسْخَرْ قَوْمٌ مِنْ قَوْمٍ"],
    triples: ["هَ دَ يَ","وَ عَ دَ","وَ جَ دَ","وَ هَ بَ","يَ سَ رَ","هَ لَ كَ","هَ جَ رَ","وَ قَ عَ"]
  },
  {
    n: 14, title: "Kasrah 1", titleArabic: "الْكَسْرَةُ ١", active: kasraByStage[14],
    competency: "PENANAMAN KASRAH pada بِ تِ ثِ جِ; Fathah tetap menjadi murojaah kumulatif.",
    tahfidz: ["Al-Ikhlas 3", "لَمْ يَلِدْ وَلَمْ يُولَدْ"],
    arabic: ["Majulah", "تَقَدَّمْ"], akhlak: ["Berbuat baik", "إِنَّ اللَّهَ يُحِبُّ الْمُحْسِنِينَ"],
    intro: [["بَ","بِ"],["تَ","تِ"],["ثَ","ثِ"],["جَ","جِ"]],
    triples: ["كَ تِ بَ","ثَ بِ تَ","تَ بِ عَ","وَ جِ دَ","سَ جِ دَ","رَ جِ عَ"]
  },
  {
    n: 15, title: "Kasrah 2", titleArabic: "الْكَسْرَةُ ٢", active: kasraByStage[15],
    competency: "Kasrah baru pada حِ خِ دِ ذِ dengan murojaah Kasrah sebelumnya dan seluruh Fathah.",
    tahfidz: ["Al-Ikhlas 4", "وَلَمْ يَكُنْ لَهُ كُفُوًا أَحَدٌ"],
    arabic: ["Kembalilah", "اِرْجِعْ"], akhlak: ["Menghormati orang tua", "وَبِالْوَالِدَيْنِ إِحْسَانًا"],
    intro: [["حَ","حِ"],["خَ","خِ"],["دَ","دِ"],["ذَ","ذِ"]],
    triples: ["حَ فِ ظَ","خَ دِ مَ","دَ خِ لَ","ذَ كِ رَ","حَ ذِ رَ","قَ دِ مَ"]
  },
  {
    n: 16, title: "Kasrah 3", titleArabic: "الْكَسْرَةُ ٣", active: kasraByStage[16],
    competency: "Kasrah baru pada رِ زِ سِ شِ; posisi Kasrah–Fathah dibuat bervariasi dengan murojaah kumulatif.",
    tahfidz: ["Al-Masad 1", "تَبَّتْ يَدَا أَبِي لَهَبٍ وَتَبَّ"],
    arabic: ["Pelan-pelan", "بِتَأَنٍّ"], akhlak: ["Menjaga lisan", "مَنْ كَانَ يُؤْمِنُ بِاللَّهِ وَالْيَوْمِ الْآخِرِ فَلْيَقُلْ خَيْرًا أَوْ لِيَصْمُتْ"],
    intro: [["رَ","رِ"],["زَ","زِ"],["سَ","سِ"],["شَ","شِ"]],
    triples: ["شَ رِ بَ","رَ كِ بَ","فَ رِ حَ","كَ رِ هَ","وَ رِ ثَ","سَ مِ عَ"]
  },
  {
    n: 17, title: "Kasrah 4", titleArabic: "الْكَسْرَةُ ٤", active: kasraByStage[17],
    competency: "Kasrah baru pada صِ ضِ طِ ظِ; Fathah dan Kasrah sebelumnya tetap berputar merata.",
    tahfidz: ["Al-Masad 2", "مَا أَغْنَى عَنْهُ مَالُهُ وَمَا كَسَبَ"],
    arabic: ["Dengan jelas", "بِوُضُوحٍ"], akhlak: ["Malu", "الْحَيَاءُ مِنَ الْإِيمَانِ"],
    intro: [["صَ","صِ"],["ضَ","ضِ"],["طَ","طِ"],["ظَ","ظِ"]],
    triples: ["بَ صِ رَ","رَ ضِ يَ","فَ طِ نَ","عَ ظِ مَ","حَ صِ رَ","فَ ضِ لَ","عَ طِ شَ"]
  },
  {
    n: 18, title: "Kasrah 5", titleArabic: "الْكَسْرَةُ ٥", active: kasraByStage[18],
    competency: "Kasrah baru pada عِ غِ فِ قِ; contoh bermakna diutamakan tanpa melompati kompetensi.",
    tahfidz: ["Al-Masad 3", "سَيَصْلَى نَارًا ذَاتَ لَهَبٍ"],
    arabic: ["Sekali lagi", "مَرَّةً أُخْرَى"], akhlak: ["Kasih sayang", "الرَّاحِمُونَ يَرْحَمُهُمُ الرَّحْمَنُ"],
    intro: [["عَ","عِ"],["غَ","غِ"],["فَ","فِ"],["قَ","قِ"]],
    triples: ["شَ عِ رَ","لَ عِ بَ","نَ عِ مَ","صَ غِ رَ","رَ غِ بَ","حَ فِ ظَ","فَ قِ هَ","بَ قِ يَ"]
  },
  {
    n: 19, title: "Kasrah 6", titleArabic: "الْكَسْرَةُ ٦", active: kasraByStage[19],
    competency: "Penuntasan Kasrah pada كِ لِ مِ نِ هِ وِ يِ ءِ إِ sebelum checkpoint P020.",
    tahfidz: ["Al-Masad 4", "وَامْرَأَتُهُ حَمَّالَةَ الْحَطَبِ"],
    arabic: ["Bagus", "جَيِّدٌ"], akhlak: ["Membantu teman", "وَاللَّهُ فِي عَوْنِ الْعَبْدِ"],
    intro: [["كَ","كِ"],["لَ","لِ"],["مَ","مِ"],["نَ","نِ"],["هَ","هِ"],["وَ","وِ"],["يَ","يِ"],["ءَ","ءِ"],["أَ","إِ"]],
    triples: ["مَ لِ كَ","كَ بِ رَ","عَ مِ لَ","فَ هِ مَ","لَ بِ سَ","جَ لِ سَ","وَ رِ ثَ","بَ قِ يَ"]
  },
  {
    n: 20, checkpoint: true, title: "Checkpoint 20", titleArabic: "مُرَاجَعَةُ الْفَتْحَةِ وَالْكَسْرَةِ",
    active: [], competency: "Checkpoint seluruh kompetensi Fathah + Kasrah sampai P019; tanpa Dhammah baru.",
    tahfidz: ["Al-Masad 5 — Review", "فِي جِيدِهَا حَبْلٌ مِنْ مَسَدٍ"],
    arabic: ["Sangat bagus", "جَيِّدٌ جِدًّا"], akhlak: ["Tidak marah", "لَا تَغْضَبْ"],
    triples: ["كَ تَ بَ","حَ مَ دَ","رَ حِ مَ","عَ مِ لَ","وَ جَ دَ","شَ كَ رَ","خَ لَ قَ","حَ فِ ظَ","فَ هِ مَ","سَ مِ عَ","شَ رِ بَ","بَ صِ رَ","فَ قِ هَ","بَ قِ يَ","مَ لِ كَ","جَ لِ سَ"]
  }
];

const cumulativeKasra = (n) => Object.entries(kasraByStage)
  .filter(([stage]) => Number(stage) <= n)
  .flatMap(([, forms]) => forms);

const priorFatha = (n) => {
  if (n <= 11) return FATHA_ALL.filter(x => !["كَ","لَ","مَ","نَ","هَ","وَ","يَ"].includes(x));
  if (n === 12) return FATHA_ALL.filter(x => !["مَ","نَ","هَ","وَ","يَ"].includes(x));
  if (n === 13) return FATHA_ALL.filter(x => !["هَ","وَ","يَ"].includes(x));
  return FATHA_ALL;
};

const nextFrom = (arr, state) => {
  if (!arr.length) throw new Error("Pool kosong");
  const value = arr[state.i % arr.length];
  state.i += 1;
  return value;
};

// 8 kelompok dua-huruf = 16 token: 11 active + 5 review.
// 16 kelompok tiga-huruf = 48 token: 27 active + 21 review.
// Total halaman normal = 38 active + 26 review = 64 token (~59.4% : 40.6%).
const makeRows = (spec) => {
  if (spec.checkpoint) {
    const learnedKasra = cumulativeKasra(19);
    const pool = [...FATHA_ALL, ...learnedKasra];
    const state = { i: 0 };
    const groups = [];
    for (let i = 0; i < 8; i++) groups.push(`${nextFrom(pool,state)} ${nextFrom(pool,state)}`);
    for (const triple of spec.triples.slice(0,16)) groups.push(triple);
    while (groups.length < 24) groups.push(`${nextFrom(pool,state)} ${nextFrom(pool,state)} ${nextFrom(pool,state)}`);
    return Array.from({ length: 8 }, (_, r) => groups.slice(r * 3, r * 3 + 3));
  }

  const review = [...priorFatha(spec.n), ...(spec.n >= 15 ? cumulativeKasra(spec.n - 1) : [])];
  const active = spec.active;
  const a = { i: 0 }, r = { i: Math.max(0, spec.n - 11) * 3 };
  const groups = [];
  const pairPattern = ["AA","AR","AR","AA","AR","AR","AA","AR"];
  for (const p of pairPattern) {
    const tokens = Array.from(p).map(ch => ch === "A" ? nextFrom(active,a) : nextFrom(review,r));
    groups.push(tokens.join(" "));
  }

  const preferred = [...(spec.triples || [])];
  const triplePattern = [...Array(11).fill("AAR"), ...Array(5).fill("ARR")];
  triplePattern.forEach((p, idx) => {
    if (preferred[idx]) {
      groups.push(preferred[idx]);
      return;
    }
    const tokens = Array.from(p).map(ch => ch === "A" ? nextFrom(active,a) : nextFrom(review,r));
    groups.push(tokens.join(" "));
  });
  return Array.from({ length: 8 }, (_, row) => groups.slice(row * 3, row * 3 + 3));
};

const letters29 = ["ا","ب","ت","ث","ج","ح","خ","د","ذ","ر","ز","س","ش","ص","ض","ط","ظ","ع","غ","ف","ق","ك","ل","م","ن","ه","و","ي","ء"];

const extraCss = `
.lesson-heading h1 .arabic-title{display:block;font-family:"QURBATA Uthmani",serif;font-size:25pt;margin-top:1mm;color:#111}
.integration-card--akhlak h2{background:linear-gradient(90deg,#6b5b24,#9b7d2f)}
.study-fields{display:grid;grid-template-columns:1fr 1fr 1fr;gap:2mm;margin-top:1.2mm;font-size:6.5pt}.study-fields span{border-top:.3mm solid #7da4b6;padding-top:.7mm;text-align:center}
.intro-strip{border:.4mm solid #0f8f91;border-radius:2.5mm;padding:1.2mm 2mm;background:#f3fffe;display:grid;grid-template-columns:auto 1fr;align-items:center;gap:2mm}.intro-strip strong{font-size:7pt;color:#0f6d70}.intro-items{display:flex;justify-content:space-around;gap:1mm}.intro-pair{font-family:"QURBATA Uthmani",serif;font-size:17pt;direction:rtl;white-space:nowrap}
.book-page.has-intro{grid-template-rows:8mm 22mm 31mm 12mm 1fr 24mm 13mm}.book-page.checkpoint{grid-template-rows:8mm 22mm 27mm 27mm 1fr 24mm 13mm}
.checkpoint-strip{border:.45mm solid #0879bd;border-radius:2.5mm;background:#f7fcff;padding:1.3mm 2mm;display:grid;grid-template-rows:auto 1fr auto;gap:1mm}.checkpoint-strip h2{font-size:8pt;margin:0;color:#075985}.checkpoint-letters{font-family:"QURBATA Uthmani",serif;direction:rtl;display:flex;flex-wrap:wrap;justify-content:center;gap:1.5mm 3mm;font-size:15pt;line-height:1}.checkpoint-harakat{text-align:center;font-size:6.8pt}.checkpoint-harakat .arabic{font-size:12pt;margin:0 1.5mm}
`;

const card = (label, value) => `
<section class="integration-card integration-card--${label.toLowerCase().replaceAll(" ","-")}">
  <h2>${esc(label)}</h2><p class="integration-title">${esc(value[0])}</p>
  <p class="arabic integration-arabic" lang="ar" dir="rtl">${esc(value[1])}</p>
  <p class="integration-instruction">Praktikkan secara nyata dalam pembelajaran.</p>
</section>`;

const rendered = [];
for (const spec of pageSpecs) {
  const rows = makeRows(spec);
  if (rows.length !== 8 || rows.some(row => row.length !== 3)) throw new Error(`P${spec.n}: grid bukan 8×3`);
  const qrUrl = `https://www.rumahilmualquran.com/q/QJ1-P${String(spec.n).padStart(3,"0")}`;
  const qr = await QRCode.toDataURL(qrUrl, { errorCorrectionLevel:"H", margin:1, width:220 });
  const intro = spec.intro ? `<section class="intro-strip"><strong>PENANAMAN KOMPETENSI</strong><div class="intro-items">${spec.intro.map(([oldF,newF]) => `<span class="intro-pair">${esc(oldF)} ← ${esc(newF)}</span>`).join("")}</div></section>` : "";
  const checkpoint = spec.checkpoint ? `<section class="checkpoint-strip"><h2>CHECKPOINT HURUF & HARAKAT</h2><div class="checkpoint-letters" lang="ar" dir="rtl">${letters29.map(x=>`<span>${x}</span>`).join("")}</div><div class="checkpoint-harakat"><strong>Fathah</strong> <span class="arabic">فَتْحَة</span> &nbsp; • &nbsp; <strong>Kasrah</strong> <span class="arabic">كَسْرَة</span> &nbsp; — &nbsp; belum ada Dhammah baru.</div></section>` : "";
  const rowHtml = rows.map(row => `<div class="practice-row">${row.map(item => `<div class="practice-cell arabic" lang="ar" dir="rtl">${esc(item)}</div>`).join("")}</div>`).join("");
  rendered.push(`<article class="book-page ${spec.intro ? "has-intro" : ""} ${spec.checkpoint ? "checkpoint" : ""}" data-page-id="QJ1-P${String(spec.n).padStart(3,"0")}">
<header class="page-header"><div class="header-line"></div><div class="book-name">QURBATA JILID 1</div><div class="page-number">${String(spec.n).padStart(2,"0")}</div></header>
<section class="lesson-heading"><h1>${esc(spec.title)}<span class="arabic-title" lang="ar" dir="rtl">${esc(spec.titleArabic)}</span></h1><p><strong>Kompetensi Tartil:</strong> ${esc(spec.competency)}</p></section>
<div class="integration-grid">${card("TAHFIDZ",spec.tahfidz)}${card("BAHASA ARAB",spec.arabic)}${card("AKHLAK",spec.akhlak)}</div>
${intro}${checkpoint}
<section class="practice-panel"><header><h2>LATIHAN TARTIL</h2><p>${spec.checkpoint ? "Evaluasi Fathah + Kasrah" : "Bacalah dengan tartil dan jelas."}</p></header><div class="practice-grid">${rowHtml}</div></section>
<section class="activity-strip"><div class="activity-content"><h2>AKTIVITAS BI’AH QURBATA</h2><div class="study-fields"><span>Tanggal: __________</span><span>Nilai: __________</span><span>TTD: __________</span></div></div><a class="qr-link" href="${qrUrl}"><img src="${qr}" alt="QR QJ1-P${String(spec.n).padStart(3,"0")}"><span>RIQA OS</span></a></section>
<footer class="page-footer"><div><span class="page-id">QJ1-P${String(spec.n).padStart(3,"0")}</span><span>AUDIT — sumber: PAGE REGISTER FROZEN v1.0</span></div><p class="arabic" lang="ar" dir="rtl">تَعَلَّمْ — اِعْمَلْ — عَلِّمْ</p><small>Belajarlah • Amalkan • Ajarkan</small></footer>
</article>`);
}

const html = template.replace("/*__BOOK_CSS__*/", `${baseCss}\n${extraCss}`).replace("<!--__BOOK_PAGES__-->", rendered.join("\n"));
await fs.mkdir(path.join(root,"dist"), { recursive:true });
await fs.writeFile(path.join(root,"dist/QURBATA-J1-P011-P020-AUDIT.html"), html);
console.log(`Built P011-P020 from ${SOURCE_REGISTER}`);

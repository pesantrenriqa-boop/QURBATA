import fs from "node:fs/promises";
import path from "node:path";
import QRCode from "qrcode";

const root = path.resolve(import.meta.dirname, "..");
const data = JSON.parse(await fs.readFile(path.join(root, "data/jilid-1.json"), "utf8"));
const template = await fs.readFile(path.join(root, "templates/book.html"), "utf8");
const css = await fs.readFile(path.join(root, "styles/book.css"), "utf8");

const escapeHtml = (value = "") => String(value)
  .replaceAll("&", "&amp;")
  .replaceAll("<", "&lt;")
  .replaceAll(">", "&gt;")
  .replaceAll('"', "&quot;");

const arabicLetters = (value) => Array.from(value.normalize("NFD"))
  .filter((character) => /\p{Script=Arabic}/u.test(character) && !/\p{Mark}/u.test(character));

const renderPracticeArabic = (value = "") => escapeHtml(value)
  // U+06BE gives the requested two-aperture isolated ha, but its combining
  // fathah is not reliably positioned by the bundled KFGQPC font.
  // Keep the glyph and render the fathah explicitly as a positioned mark.
  .replaceAll("ھَ", '<span class="ha-two-fatha"><span class="ha-two">ھ</span><span class="ha-fatha">َ</span></span>');

const card = (label, value) => `
  <section class="integration-card integration-card--${label.toLowerCase()}">
    <h2>${escapeHtml(label)}</h2>
    <p class="integration-title">${escapeHtml(value.title)}</p>
    <p class="arabic integration-arabic" lang="ar" dir="rtl">${escapeHtml(value.arabic)}</p>
    <p class="integration-instruction">${escapeHtml(value.instruction)}</p>
  </section>`;

const frontMatterData = [
  { title: "SAMBUTAN PENDIRI QURBATA & RIQA", type: "founder", arabic: `بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ

الْحَمْدُ لِلَّهِ الَّذِي أَنْزَلَ الْقُرْآنَ هُدًى وَبُرْهَانًا، وَجَعَلَهُ لِلْقُلُوبِ نُورًا وَلِلصُّدُورِ إِيمَانًا، وَأَنْزَلَهُ بِلِسَانٍ عَرَبِيٍّ مُبِينٍ فَزَادَهُ فَصَاحَةً وَبَيَانًا، وَيَسَّرَهُ لِلذِّكْرِ تِلَاوَةً وَحِفْظًا وَإِمْعَانًا، وَجَعَلَ الْعِلْمَ بِهِ هُدًى وَعِرْفَانًا، وَالْعَمَلَ بِهِ رُشْدًا وَإِذْعَانًا، وَالتَّخَلُّقَ بِآدَابِهِ لِلنُّفُوسِ زِينَةً، وَلِلسُّلُوكِ تَهْذِيبًا، وَلِلْحَيَاةِ صَلَاحًا وَاتِّزَانًا.

نَحْمَدُهُ سُبْحَانَهُ حَمْدَ الشَّاكِرِينَ، وَنَسْأَلُهُ تِلَاوَةً يَخْشَعُ لَهَا الْجَنَانُ وَيَلِينُ، وَعَرَبِيَّةً يَفْصُحُ بِهَا اللِّسَانُ وَيَسْتَبِينُ، وَحِفْظًا يَثْبُتُ فِي الصُّدُورِ وَلَا يَهُونُ، وَخُلُقًا يَسْمُو بِهِ الْمَرْءُ وَيَزِينُ، وَعِلْمًا يُثْمِرُ عَمَلًا وَيَقِينًا، وَتَعْلِيمًا يَبْقَى نَفْعُهُ عَلَى مَرِّ السِّنِينِ؛ حَتَّى تَحْيَا بِالْقُرْآنِ قُلُوبُنَا، وَتَسْتَنِيرَ بِنُورِهِ دُرُوبُنَا، وَتَنْطِقَ بِالْعَرَبِيَّةِ أَلْسِنَتُنَا، وَتَعْمُرَ بِآيَاتِهِ صُدُورُنَا، وَتَسْتَقِيمَ بِهَدْيِهِ أَخْلَاقُنَا، فَنَكُونَ بِهِ فِي الدُّنْيَا مِنَ الْمُهْتَدِينَ، وَفِي الْآخِرَةِ مِنَ الْفَائِزِينَ.

وَالصَّلَاةُ وَالسَّلَامُ عَلَى سَيِّدِنَا مُحَمَّدٍ، الَّذِي تَلَا الْقُرْآنَ فَأَجَادَ تِلَاوَتَهُ، وَبَيَّنَ آيَاتِهِ فَأَظْهَرَ هِدَايَتَهُ، وَعَلَّمَ أُمَّتَهُ فَأَحْكَمَ تَرْبِيَتَهَا، وَعَمِلَ بِوَحْيِ رَبِّهِ فَاسْتَقَامَ عَلَى هَدْيِهِ، وَتَخَلَّقَ بِآدَابِهِ فَكَانَ قُدْوَةً فِي مَكَارِمِ الْأَخْلَاقِ؛ وَعَلَى آلِهِ وَصَحْبِهِ مَصَابِيحِ الْهُدَى، وَمَنَابِعِ الْعِلْمِ وَالتُّقَى، وَمَنْ تَبِعَهُمْ بِإِحْسَانٍ وَاقْتَفَى أَثَرَهُمْ إِلَى يَوْمِ اللِّقَاءِ.

أَمَّا بَعْدُ؛`, source: "", body: "QURBATA lahir dari ikhtiar menghadirkan pembelajaran Al-Qur’an sebagai ekosistem pendidikan: bacaan dibenahi, Bahasa Arab dihidupkan, hafalan dijaga, dan Akhlak dibiasakan. Ilmu tidak berhenti pada kemampuan pribadi, tetapi bergerak menuju amal dan pengajaran. Sebagaimana pesan KH. Basori Alwi: لِكُلِّ شَيْءٍ زَكَاةٌ، وَزَكَاةُ الْعِلْمِ التَّعْلِيمُ. Ruh itu kami ringkas dalam tiga kata: تَعَلَّمْ — اِعْمَلْ — عَلِّمْ." },
  { title: "PENDAHULUAN", arabic: "خَيْرُكُمْ مَنْ تَعَلَّمَ الْقُرْآنَ وَعَلَّمَهُ", source: "HR. al-Bukhari", body: "QURBATA dikembangkan dari kebutuhan akan pembelajaran Al-Qur’an yang tidak berhenti pada kemampuan membaca. Al-Qur’an ditempatkan sebagai pusat ekosistem belajar; Bahasa Arab, Tahfidz, dan Akhlak hadir untuk menguatkan kedekatan peserta dengan Al-Qur’an secara utuh. Integrasi tidak berarti mencampur seluruh bidang menjadi satu, tetapi menempatkan setiap unsur pada fungsi pedagogisnya masing-masing." },
  { title: "MENGENAL QURBATA", arabic: "إِنَّا أَنْزَلْنَاهُ قُرْآنًا عَرَبِيًّا لَعَلَّكُمْ تَعْقِلُونَ", source: "QS. Yusuf [12]: 2", body: "QURBATA adalah metode integratif Qur’an, Bahasa Arab, Tahfidz, dan Akhlak. Qur’an/Tartil menjadi kompetensi inti. Bahasa Arab QURBATA berfungsi sebagai bi’ah ‘Arabiyah dalam proses pembelajaran dan berbeda dari Bahasa Arab RIQA, yaitu jalur Bahasa Arab Qur’ani berbasis tangga kompetensi korpus Al-Qur’an. Tahfidz berjalan bertahap per ayat dengan murojaah. Akhlak QURBATA merupakan pembiasaan nilai melalui hadis atau nasihat yang dapat berlangsung beberapa pertemuan, dan berbeda dari jalur Hadis RIQA." },
  { title: "LANDASAN & PRINSIP PEMBELAJARAN", arabic: "وَلَقَدْ يَسَّرْنَا الْقُرْآنَ لِلذِّكْرِ فَهَلْ مِنْ مُدَّكِرٍ", source: "QS. Al-Qamar [54]: 17", body: "Pembelajaran mengikuti tangga kompetensi yang bertahap, terukur, dan tidak dilompati. Guru membimbing melalui talqin, talaqqi, koreksi langsung, latihan, murojaah, pembiasaan, dan verifikasi. Ketepatan bacaan didahulukan daripada kecepatan. Bahasa Arab digunakan secara fungsional dalam kelas; Tahfidz dibangun sedikit demi sedikit; dan Akhlak diarahkan menjadi perilaku yang dapat diamati." },
  { title: "GAMBARAN QURBATA JILID 1", arabic: "تَعَلَّمْ — اِعْمَلْ — عَلِّمْ", source: "Ruh QURBATA", body: "Jilid 1 merupakan gerbang fondasi. Materi Tartil disusun menurut tangga kompetensi awal dan menjadi porsi utama halaman. Tahfidz dimulai dari Surah An-Nas, bergerak ayat demi ayat sesuai peta yang ditetapkan. Bahasa Arab QURBATA memperkenalkan ungkapan kelas yang langsung dipakai dalam interaksi. Akhlak menggunakan satu pesan atau matan selama beberapa pertemuan agar peserta bergerak dari mendengar, memahami, hingga membiasakan." },
  { title: "CARA MENGGUNAKAN BUKU", arabic: "تَعَلَّمْ — اِعْمَلْ — عَلِّمْ", source: "Belajarlah · Amalkan · Ajarkan", body: "Peserta mengikuti contoh guru, membaca sesuai target halaman, mengulang bagian yang dikoreksi, menjaga hafalan sebelumnya, menggunakan ungkapan Bahasa Arab yang sedang dibiasakan, dan mempraktikkan pesan Akhlak. Guru menjadikan buku sebagai peta kompetensi dan media talaqqi, bukan pengganti pendampingan. Orang tua atau pendamping mengulang materi yang telah diajarkan tanpa mendahului kompetensi baru. QR dan RIQA OS menjadi penghubung buku fisik dengan materi pendamping, asesmen, pencatatan, dan kesinambungan kompetensi." },
  { title: "PANDUAN PENGAJARAN", arabic: "وَإِنَّكَ لَعَلَى خُلُقٍ عَظِيمٍ", source: "QS. Al-Qalam [68]: 4", body: "Satu pertemuan QURBATA bergerak melalui pembukaan dan kesiapan belajar, talqin, talaqqi, latihan dan murojaah, Tahfidz, penggunaan Bahasa Arab secara fungsional, pembiasaan Akhlak, lalu verifikasi hasil. Guru menjaga agar unsur integratif menguatkan latihan Tartil, bukan mengurangi porsinya. Perpindahan halaman mengikuti penguasaan kompetensi, bukan semata-mata jumlah pertemuan." },
  { title: "PETA KOMPETENSI JILID 1", arabic: "قُرْآنًا عَرَبِيًّا", source: "Qur’an · Bahasa Arab · Tahfidz · Akhlak", body: "Peta kompetensi Jilid 1 menampilkan perkembangan empat jalur secara berdampingan: tangga Tartil sebagai jalur inti; Tahfidz per ayat; Bahasa Arab sebagai bi’ah kelas; serta Akhlak sebagai pembiasaan. Peta ini berfungsi sebagai gambaran perkembangan, bukan pengganti rincian kompetensi pada halaman pembelajaran." },
  { title: "DAFTAR ISI", arabic: "تَعَلَّمْ — اِعْمَلْ — عَلِّمْ", source: "QURBATA Jilid 1", body: "Sambutan Pendiri QURBATA & RIQA · Pendahuluan · Mengenal QURBATA · Landasan & Prinsip Pembelajaran · Gambaran QURBATA Jilid 1 · Cara Menggunakan Buku · Panduan Pengajaran · Peta Kompetensi Jilid 1 · Materi QURBATA Jilid 1." }
];

const frontMatter = frontMatterData.map((item, index) => `
  <article class="book-page front-matter-page">
    <header class="page-header"><div class="header-line"></div><div class="book-name"><span class="qurbata-brand-text"><strong>QURBATA</strong><small>Qur’an · Bahasa Arab · Tahfidz · Akhlak</small></span></div><div class="page-number">${String(index + 1).padStart(2, "0")}</div></header>
    <section class="front-matter-content official-front">
      <h1>${escapeHtml(item.title)}</h1>
      <div class="official-epigraph"><p class="arabic front-arabic" lang="ar" dir="rtl">${escapeHtml(item.arabic)}</p><p class="front-source">${escapeHtml(item.source)}</p></div>
      <p class="front-body">${escapeHtml(item.body)}</p>
      ${index === 0 ? `<div class="front-motto"><p class="arabic" lang="ar" dir="rtl">تَعَلَّمْ — اِعْمَلْ — عَلِّمْ</p><small>Belajarlah · Amalkan · Ajarkan</small></div>` : ""}
    </section>
    <footer class="page-footer"><p class="arabic" lang="ar" dir="rtl">تَعَلَّمْ — اِعْمَلْ — عَلِّمْ</p><small>Belajarlah • Amalkan • Ajarkan</small></footer>
  </article>`).join("\n");

const pages = await Promise.all(data.pages.map(async (page) => {
  if (!page.title || !page.titleArabic || arabicLetters(page.titleArabic).length === 0) {
    throw new Error(`${page.pageId}: judul Indonesia dan judul Arab wajib diisi terpisah.`);
  }
  if (page.rows.length !== 8 || page.rows.some((row) => row.length !== 3)) {
    throw new Error(`${page.pageId}: grid wajib tepat 8 baris x 3 kolom.`);
  }
  const items = page.rows.flat();
  if (items.length !== 24) {
    throw new Error(`${page.pageId}: halaman wajib mempunyai tepat 24 tangga.`);
  }
  const firstEightValid = items.slice(0, 8).every((item) => arabicLetters(item).length === 2);
  const lastSixteenValid = items.slice(8).every((item) => arabicLetters(item).length === 3);
  if (!firstEightValid || !lastSixteenValid) {
    throw new Error(`${page.pageId}: tangga 1-8 wajib dua huruf dan tangga 9-24 wajib tiga huruf.`);
  }
  if (!/^https:\/\/www\.rumahilmualquran\.com\/q\/[A-Z0-9-]+$/.test(page.riqaOsUrl)) {
    throw new Error(`${page.pageId}: URL RIQA OS tidak mengikuti kontrak /q/{pageId}.`);
  }

  const qr = await QRCode.toDataURL(page.riqaOsUrl, {
    errorCorrectionLevel: "H",
    margin: 1,
    width: 240,
    color: { dark: "#075985", light: "#ffffff" }
  });

  const rows = page.rows.map((row) => `
    <div class="practice-row">
      ${row.map((item) => `<div class="practice-cell arabic" lang="ar" dir="rtl">${renderPracticeArabic(item)}</div>`).join("")}
    </div>`).join("");

  const activities = page.activities.map((item, index) => `
    <div class="activity"><span>${index + 1}</span>${escapeHtml(item)}</div>`).join("");

  return `
  <article class="book-page" data-page-id="${escapeHtml(page.pageId)}">
    <header class="page-header">
      <div class="header-line"></div>
      <div class="book-name"><span class="qurbata-brand-logo"><svg viewBox="0 0 1956 2048" aria-label="Logo QURBATA"><path fill="#0f8f91" fill-rule="evenodd" d="M1034,1576 958,1652 1035,1729 1111,1652Z M1637,1221 1629,1213 1608,1204 1573,1202 1541,1207 1506,1223 1483,1249 1473,1276 1509,1265 1540,1264 1570,1269 1588,1277 1543,1317 1469,1361 1502,1360 1539,1353 1564,1344 1597,1324 1619,1301 1638,1266 1644,1240Z M1483,800 1340,868 1217,936 1138,991 1107,1021 1093,1044 1457,852Z M1816,838 1790,819 1754,801 1703,789 1662,799 1625,820 1589,856 1560,909 1542,976 1541,1041 1552,1080 1569,1107 1598,1132 1630,1147 1664,1154 1704,1155 1827,1145 1854,1154 1872,1172 1882,1199 1883,1245 1829,1296 1769,1337 1688,1384 1556,1453 1455,1522 1386,1586 1308,1681 1250,1741 1143,1837 1059,1905 1001,1928 948,1937 904,1933 875,1921 854,1906 827,1875 810,1844 800,1795 800,1758 806,1712 826,1644 864,1564 938,1453 876,1514 830,1576 790,1651 767,1718 756,1798 756,1846 761,1886 772,1923 784,1948 802,1974 824,1996 851,2015 893,2035 925,2044 954,2047 988,2046 1032,2036 1098,2005 1139,1977 1186,1937 1233,1889 1345,1762 1471,1646 1581,1565 1688,1505 1760,1458 1831,1400 1881,1347 1919,1297 1945,1236 1955,1179 1953,1100 1930,1020 1898,946 1860,885Z M1604,968 1614,953 1636,934 1658,925 1680,922 1720,934 1749,950 1779,980 1793,1009 1725,1020 1652,1019 1624,1009 1611,997 1604,982Z M1602,582 1527,658 1604,734 1680,657Z M1807,579 1730,655 1806,732 1883,656Z M476,251 401,328 478,403 554,327Z M639,250 564,326 641,402 717,325Z M1294,287 1271,261 1244,245 1211,236 1176,233 1100,255 1015,299 935,358 849,439 782,514 663,662 606,725 518,813 411,904 315,971 205,1030 105,1068 1,1092 51,1104 103,1111 203,1109 240,1103 308,1083 390,1043 458,995 540,917 592,855 683,732 777,615 845,538 933,453 988,412 1046,384 1105,370 1160,374 1187,386 1213,407 1239,442 1249,464 1250,501 1241,538 1220,582 1201,611 1161,660 1107,714 1057,758 962,831 919,634 898,566 882,528 847,702 847,728 875,843 879,893 765,973 690,1032 624,1090 563,1152 513,1214 482,1265 462,1314 457,1373 463,1400 473,1418 494,1436 529,1448 577,1450 655,1437 707,1419 774,1380 839,1319 891,1245 932,1160 945,1248 974,1337 1015,1407 1063,1458 1121,1497 1191,1525 1253,1523 1283,1515 1317,1498 1354,1465 1379,1429 1402,1377 1415,1303 1415,1246 1402,1168 1381,1105 1352,1043 1298,1219 1337,1283 1356,1339 1307,1375 1259,1394 1210,1397 1170,1388 1125,1365 1104,1347 1076,1308 1047,1246 1009,1113 974,904 976,898 1079,816 1161,736 1216,669 1263,594 1296,516 1313,437 1314,349 1306,313Z M904,988 910,1032 903,1115 895,1138 843,1189 762,1251 728,1270 682,1289 638,1299 592,1300 567,1297 527,1284 538,1262 575,1212 656,1132 788,1027 891,955Z M1766,124 1738,112 1706,128 1671,157 1646,193 1641,219 1648,239 1675,270 1700,289 1656,344 1614,385 1541,443 1470,491 1363,555 1416,546 1451,535 1497,514 1543,486 1591,448 1641,399 1715,307 1729,325 1734,341 1731,373 1674,466 1662,497 1658,529 1666,550 1682,562 1713,560 1729,554 1746,541 1765,507 1772,463 1760,483 1743,501 1723,510 1699,504 1692,494 1692,482 1710,443 1746,392 1762,352 1762,311 1755,292 1737,268 1766,213 1776,181 1777,143Z M1731,152 1744,171 1746,192 1740,215 1721,249 1691,227 1671,197 1698,166Z M740,0 588,73 457,147 382,203 361,225 350,244 714,52Z"/></svg></span><span class="qurbata-brand-text"><strong>${escapeHtml(data.book.title)}</strong><small>Qur’an · Bahasa Arab · Tahfidz · Akhlak</small></span></div>
      <div class="page-number">${escapeHtml(page.pageNumber)}</div>
    </header>

    <section class="lesson-heading">
      <h1><span>${escapeHtml(page.title)}</span> <span class="arabic lesson-title-arabic" lang="ar" dir="rtl">${escapeHtml(page.titleArabic)}</span></h1>
      <p><strong>Kompetensi Tartil:</strong> ${escapeHtml(page.tartilCompetency)}</p>
    </section>

    <div class="integration-grid">
      ${card("TAHFIDZ", page.integration.tahfidz)}
      ${card("BAHASA ARAB", page.integration.arabic)}
      ${card("AKHLAK", page.integration.akhlak)}
    </div>

    <section class="practice-panel">
      <header><h2>LATIHAN TARTIL</h2><p>Bacalah dengan tartil dan jelas.</p></header>
      <div class="practice-grid">${rows}</div>
    </section>

    <section class="activity-strip">
      <div class="activity-content">
        <h2>AKTIVITAS BI’AH QURBATA</h2>
        <div class="activity-grid">${activities}</div>
      </div>
      <a class="qr-link" href="${escapeHtml(page.riqaOsUrl)}" aria-label="Buka kompetensi ${escapeHtml(page.pageId)} di RIQA OS">
        <img src="${qr}" alt="QR ${escapeHtml(page.pageId)}">
        <span>Pindai di RIQA OS</span>
      </a>
      <div class="learning-record" aria-label="Catatan hasil belajar">
        <div><span>Tanggal</span><i></i></div>
        <div><span>Nilai</span><i></i></div>
        <div><span>TTD Guru</span><i></i></div>
      </div>
    </section>

    <footer class="page-footer">
      <div><span class="page-id">${escapeHtml(page.pageId)}</span><span>${escapeHtml(data.book.status)}</span></div>
      <p class="arabic" lang="ar" dir="rtl">تَعَلَّمْ — اِعْمَلْ — عَلِّمْ</p>
      <small>Belajarlah • Amalkan • Ajarkan</small>
    </footer>
  </article>`;
}));

const html = template
  .replace("/*__BOOK_CSS__*/", css)
  .replace("<!--__BOOK_PAGES__-->", process.env.QURBATA_FRONT_MATTER_ONLY === "1" ? frontMatter : `${frontMatter}\n${pages.join("\n")}`);

await fs.mkdir(path.join(root, "dist"), { recursive: true });
await fs.mkdir(path.join(root, "dist/fonts"), { recursive: true });
await fs.copyFile(
  path.join(root, "fonts/KFGQPC-Uthman-Taha-Naskh.woff2"),
  path.join(root, "dist/fonts/KFGQPC-Uthman-Taha-Naskh.woff2")
);
await fs.writeFile(path.join(root, "dist/index.html"), html);
console.log(`Dibangun: ${data.pages.length} halaman -> dist/index.html`);

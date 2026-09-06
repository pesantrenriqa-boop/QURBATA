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

const card = (label, value) => `
  <section class="integration-card integration-card--${label.toLowerCase()}">
    <h2>${escapeHtml(label)}</h2>
    <p class="integration-title">${escapeHtml(value.title)}</p>
    <p class="arabic integration-arabic" lang="ar" dir="rtl">${escapeHtml(value.arabic)}</p>
    <p class="integration-instruction">${escapeHtml(value.instruction)}</p>
  </section>`;

const pages = await Promise.all(data.pages.map(async (page) => {
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
      ${row.map((item) => `<div class="practice-cell arabic" lang="ar" dir="rtl">${escapeHtml(item)}</div>`).join("")}
    </div>`).join("");

  const activities = page.activities.map((item, index) => `
    <div class="activity"><span>${index + 1}</span>${escapeHtml(item)}</div>`).join("");

  return `
  <article class="book-page" data-page-id="${escapeHtml(page.pageId)}">
    <header class="page-header">
      <div class="header-line"></div>
      <div class="book-name">${escapeHtml(data.book.title)}</div>
      <div class="page-number">${escapeHtml(page.pageNumber)}</div>
    </header>

    <section class="lesson-heading">
      <h1>${escapeHtml(page.title)}</h1>
      <p><strong>Kompetensi Tartil:</strong> ${escapeHtml(page.tartilCompetency)}</p>
    </section>

    <div class="integration-grid">
      ${card("TAHFIDZ", page.integration.tahfidz)}
      ${card("BAHASA ARAB", page.integration.arabic)}
      ${card("NIDHOM", page.integration.nidom)}
    </div>

    <section class="practice-panel">
      <header><h2>LATIHAN TARTIL</h2><p>Bacalah dengan tartil dan jelas.</p></header>
      <div class="practice-grid">${rows}</div>
    </section>

    <section class="activity-strip">
      <div class="activity-content">
        <h2>AKTIVITAS BI’AH QURBATA</h2>
        <div class="activity-grid">${activities}</div>
        <div class="learning-record" aria-label="Catatan hasil belajar">
          <div><span>Tanggal</span><i></i></div>
          <div><span>Nilai</span><i></i></div>
          <div><span>TTD Guru</span><i></i></div>
        </div>
      </div>
      <a class="qr-link" href="${escapeHtml(page.riqaOsUrl)}" aria-label="Buka kompetensi ${escapeHtml(page.pageId)} di RIQA OS">
        <img src="${qr}" alt="QR ${escapeHtml(page.pageId)}">
        <span>Pindai di RIQA OS</span>
      </a>
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
  .replace("<!--__BOOK_PAGES__-->", pages.join("\n"));

await fs.mkdir(path.join(root, "dist"), { recursive: true });
await fs.mkdir(path.join(root, "dist/fonts"), { recursive: true });
await fs.copyFile(
  path.join(root, "node_modules/@fontsource/amiri-quran/files/amiri-quran-arabic-400-normal.woff2"),
  path.join(root, "dist/fonts/AmiriQuran-Arabic.woff2")
);
await fs.writeFile(path.join(root, "dist/index.html"), html);
console.log(`Dibangun: ${data.pages.length} halaman -> dist/index.html`);

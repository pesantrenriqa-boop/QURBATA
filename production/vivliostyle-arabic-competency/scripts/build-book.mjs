import fs from "node:fs/promises";
import path from "node:path";

const root = path.resolve(import.meta.dirname, "..");
const data = JSON.parse(await fs.readFile(path.join(root, "data/competencies.json"), "utf8"));
const template = await fs.readFile(path.join(root, "templates/book.html"), "utf8");
const css = await fs.readFile(path.join(root, "styles/book.css"), "utf8");

const esc = (value = "") => String(value)
  .replaceAll("&", "&amp;")
  .replaceAll("<", "&lt;")
  .replaceAll(">", "&gt;")
  .replaceAll('"', "&quot;");

const expected = Array.from({ length: 65 }, (_, index) => `K${String(index + 1).padStart(2, "0")}`);
const actual = data.competencies.map((item) => item.id);
if (JSON.stringify(expected) !== JSON.stringify(actual)) {
  throw new Error("Registry wajib memuat K01-K65 secara urut, unik, dan lengkap.");
}

for (const item of data.competencies) {
  if (!item.code || !item.title || !item.operation || !item.layer || !Array.isArray(item.prerequisites)) {
    throw new Error(`${item.id}: metadata inti tidak lengkap.`);
  }
  for (const prerequisite of item.prerequisites) {
    if (!actual.includes(prerequisite) || Number(prerequisite.slice(1)) >= Number(item.id.slice(1))) {
      throw new Error(`${item.id}: prasyarat ${prerequisite} tidak sah.`);
    }
  }
  for (const example of item.examples ?? []) {
    if (!/^.+ \d{1,3}:\d{1,3}$/.test(example.reference)) {
      throw new Error(`${item.id}: rujukan ${example.reference} tidak mengikuti pola Surah n:n.`);
    }
  }
}

const cover = `
<section class="cover print-page">
  <div class="cover-kicker">BUKU INDUK • QURBATA</div>
  <h1 class="cover-title">${esc(data.book.title)}</h1>
  <p class="cover-subtitle">${esc(data.book.subtitle)}</p>
  <p class="cover-arabic arabic" lang="ar" dir="rtl">سُلَّمُ كَفَايَاتِ اللُّغَةِ الْعَرَبِيَّةِ الْقُرْآنِيَّةِ</p>
  <div class="cover-ladder">${data.layers.map((layer) => `<span>${esc(layer.id)}<br>${esc(layer.title)}</span>`).join("")}</div>
  <div class="cover-brand"><div><strong>QURBATA</strong><br>Qur'an • Bahasa Arab • Tahfidz • Akhlak</div><div>Rumah Ilmu Al-Qur'an<br>${esc(data.book.version)}</div></div>
</section>`;

const frontMatter = `
<section class="print-page">
  <h1 class="front-title">Tentang Buku Ini</h1>
  <p class="front-subtitle">Bahasa Arab Qurani sebagai jalur kompetensi tersendiri</p>
  <p class="lead">Buku ini memaparkan perjalanan bertahap memahami bahasa Al-Qur'an: dari mengenali satu kata, menghubungkan dua unsur, membaca struktur kalimat, sampai memahami hubungan makna antarkalimat. Urutan tidak dibangun dari banyaknya bab nahwu, tetapi dari operasi yang benar-benar dapat dilakukan, dibuktikan, dan dipindahkan peserta ke ayat baru.</p>
  <h2>Landasan Qurani</h2>
  <p class="arabic" lang="ar" dir="rtl" style="font-size:22pt;text-align:center;margin:8mm 0 2mm">إِنَّا أَنْزَلْنَاهُ قُرْآنًا عَرَبِيًّا لَعَلَّكُمْ تَعْقِلُونَ</p>
  <p style="text-align:center">Sesungguhnya Kami menurunkannya berupa Al-Qur'an berbahasa Arab agar kamu memahaminya. QS. Yusuf 12:2</p>
  <h2>Batas Produk</h2>
  <p>Bahasa Arab Qurani dalam buku ini berbeda dari Bahasa Arab pendamping Tartil. Bahasa Arab pendamping Tartil menghidupkan bi'ah kelas melalui ungkapan praktis. Buku ini mengembangkan pemahaman struktur dan makna dari korpus Al-Qur'an melalui K01-K65.</p>
</section>
<section class="print-page">
  <h1 class="chapter-name">Prinsip Penyusunan</h1>
  <div class="principles">
    <div class="principle"><strong>Satu operasi</strong>Satu kompetensi hanya memperkenalkan satu tindakan baru yang dapat diamati.</div>
    <div class="principle"><strong>Korpus sebagai bukti</strong>Contoh harus dilacak ke surah, ayat, target span, dan fungsi yang benar.</div>
    <div class="principle"><strong>Pengenalan dahulu</strong>Bentuk dikenali sebelum hubungan dan amal sintaksisnya dianalisis.</div>
    <div class="principle"><strong>Prasyarat terkendali</strong>Butir target tidak boleh bergantung pada kompetensi yang belum dikuasai.</div>
    <div class="principle"><strong>Transfer</strong>Peserta harus berhasil pada ayat baru, bukan hanya contoh yang dihafal.</div>
    <div class="principle"><strong>Murojaah kumulatif</strong>Kompetensi lama tetap hidup di dalam contoh yang semakin kaya.</div>
    <div class="principle"><strong>Makna dan struktur</strong>Kaidah membantu pemahaman, bukan berhenti pada hafalan istilah.</div>
    <div class="principle"><strong>Validasi ahli</strong>Status siap terbit membutuhkan telaah Bahasa Arab, Al-Qur'an, dan asesmen.</div>
  </div>
</section>`;

const layers = `
<section class="print-page">
  <h1 class="chapter-name">Arsitektur Tangga Kompetensi</h1>
  <p class="lead">Enam puluh lima kompetensi inti dikelompokkan ke dalam lima lapisan. Nomor menunjukkan urutan paparan pedagogis, sedangkan prasyarat membentuk graf yang tidak selalu lurus.</p>
  <div class="layer-grid">${data.layers.map((layer) => `
    <article class="layer-card"><div class="layer-letter">${esc(layer.id)}</div><div><h3>${esc(layer.title)} • ${esc(layer.range)}</h3><p>${esc(layer.description)}</p></div></article>`).join("")}</div>
</section>`;

const registryRows = data.competencies.map((item) => `<tr><td class="id">${esc(item.id)}</td><td>${esc(item.title)}</td><td>${esc(item.operation)}</td><td class="layer">${esc(item.layer)}</td></tr>`).join("");
const registry = `<section class="print-page"><h1 class="chapter-name">Registry Canonical K01-K65</h1><table class="registry"><thead><tr><th>ID</th><th>Kompetensi</th><th>Operasi Peserta</th><th>Lapisan</th></tr></thead><tbody>${registryRows}</tbody></table></section>`;

const renderExamples = (item) => {
  if (!item.examples?.length) return `<div class="pending"><strong>Bukti korpus belum diterbitkan pada gelombang ini.</strong><br>Halaman mempertahankan identitas dan operasi canonical, tetapi contoh ayat menunggu ekstraksi evidence bank, pemeriksaan target span, dan validasi ahli.</div>`;
  return `<h2>Contoh Korpus</h2><table class="examples"><thead><tr><th>Teks</th><th>Rujukan</th><th>Makna</th><th>Bukti</th></tr></thead><tbody>${item.examples.map((example) => `<tr><td class="quran arabic" lang="ar" dir="rtl">${esc(example.arabic)}</td><td>${esc(example.reference)}</td><td>${esc(example.meaning)}</td><td>${esc(example.note)}</td></tr>`).join("")}</tbody></table>`;
};

const competencyPages = data.competencies.map((item) => `
<article class="competency">
  <header class="competency-heading"><div class="competency-id">${esc(item.id)}</div><div><h1 class="competency-title">${esc(item.title)}</h1><div class="competency-code">${esc(item.code)} • LAPISAN ${esc(item.layer)}</div></div></header>
  <p class="competency-summary">${esc(item.operation)}</p>
  <div class="metadata">
    <div class="meta"><span class="meta-label">Prasyarat langsung</span><span class="meta-value">${item.prerequisites.length ? item.prerequisites.map(esc).join(" • ") : "Tidak ada prasyarat Bahasa Arab langsung"}</span></div>
    <div class="meta"><span class="meta-label">Ceiling</span><span class="meta-value">Tidak boleh menuntut operasi di atas ${esc(item.id)}</span></div>
  </div>
  ${item.reason ? `<h2>Mengapa Berada di Posisi Ini</h2><p>${esc(item.reason)}</p>` : ""}
  ${item.boundary ? `<h2>Batas Kompetensi</h2><p>${esc(item.boundary)}</p>` : ""}
  ${renderExamples(item)}
  <p class="status"><strong>Status bukti:</strong> ${esc(item.evidenceStatus ?? "MENUNGGU PENANAMAN EVIDENCE BANK")}</p>
  <div class="next"><p><strong>RIQA OS</strong><br>Materi, audio, latihan, asesmen adaptif, dan riwayat ketuntasan terhubung melalui kode stabil <code>${esc(item.id)}</code>.</p><div class="qr-placeholder">QR RIQA OS<br>${esc(item.id)}</div></div>
</article>`).join("");

const html = template
  .replace("/*__BOOK_CSS__*/", css)
  .replace("<!--__BOOK_CONTENT__-->", [cover, frontMatter, layers, registry, competencyPages].join("\n"));

await fs.mkdir(path.join(root, "dist"), { recursive: true });
await fs.writeFile(path.join(root, "dist/index.html"), html);
console.log(`Dibangun: ${data.competencies.length} kompetensi -> dist/index.html`);

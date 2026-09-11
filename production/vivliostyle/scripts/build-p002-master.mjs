import fs from "node:fs/promises";
import path from "node:path";
import QRCode from "qrcode";

const root = path.resolve(import.meta.dirname, "..");
const sourceDir = path.join(root, "dist-p001");
const out = path.join(root, "dist-p002");
const file = path.join(out, "index.html");
const riqaUrl = "https://www.rumahilmualquran.com/q/QJ1-P002";

await fs.rm(out, { recursive: true, force: true });
await fs.cp(sourceDir, out, { recursive: true });
let html = await fs.readFile(file, "utf8");

// P002 source-of-truth follows the frozen 40-page curriculum, not the older production-data integration copy.
const rows = [
  ["ءَ أَ", "أَ ءَ", "ءَ بَ"],
  ["أَ تَ", "ءَ ثَ", "ءَ أَ"],
  ["ءَ أَ بَ", "أَ ءَ تَ", "ءَ أَ ثَ"],
  ["أَ بَ ءَ", "ءَ تَ أَ", "أَ ثَ ءَ"],
  ["ءَ ءَ بَ", "أَ أَ تَ", "ءَ أَ بَ"],
  ["أَ ءَ ثَ", "ءَ بَ أَ", "أَ تَ ءَ"],
  ["بَ ءَ تَ", "تَ أَ ثَ", "ثَ ءَ بَ"],
  ["بَ تَ ءَ", "تَ ثَ أَ", "ثَ بَ ءَ"]
];
const cells = rows.map(r => `<div class="r">${r.map(x => `<div class="c arabic">${x}</div>`).join("")}</div>`).join("");
const qr = await QRCode.toDataURL(riqaUrl, {
  errorCorrectionLevel: "H",
  margin: 1,
  width: 300,
  color: { dark: "#123f34", light: "#fffdf6" }
});

const exact = (from, to) => {
  if (!html.includes(from)) throw new Error(`P002 transform target not found: ${from}`);
  html = html.replace(from, to);
};

exact('<div class="num">01</div>', '<div class="num">02</div>');
exact('Kompetensi QRT-T01 · Huruf dengan Fathah', 'QJ1-P002 · Hamzah dan Alif dengan Fathah');
exact('Mengenal, membaca, dan membedakan <span class="arabic">بَ تَ ثَ</span>. Hanya huruf lepas berharakat fathah.', 'Membedakan dan membaca <span class="arabic">ءَ أَ</span> bersama murojaah <span class="arabic">بَ تَ ثَ</span>. Hanya huruf lepas berharakat fathah.');
exact('<div class="arabic">بَ تَ ثَ</div></div></section><main class="practice">', '<div class="arabic">ءَ أَ</div></div></section><main class="practice">');
html = html.replace(/<main class="practice">[\s\S]*?<\/main>/, `<main class="practice">${cells}</main>`);

exact('<h3>TAHFIDZ · An-Nas 1</h3><div class="arabic">قُلْ أَعُوذُ بِرَبِّ النَّاسِ</div><small>Talqin dan hafalkan ayat.</small>', '<h3>TAHFIDZ · An-Nas 2</h3><div class="arabic">مَلِكِ النَّاسِ</div><small>Talqin dan hafalkan ayat.</small>');
exact('<h3>BI\'AH ARABIYAH</h3><div class="arabic">السَّلَامُ عَلَيْكُمْ</div><small>Gunakan salam dalam pembelajaran.</small>', '<h3>BI\'AH ARABIYAH</h3><div class="arabic">اُنْظُرْ</div><small>Gunakan instruksi ini dalam pembelajaran.</small>');
exact('<h3>AKHLAK · Rahmah</h3><div class="arabic">مَنْ لَا يَرْحَمْ لَا يُرْحَمْ</div><small>Biasakan menyayangi dan bersikap lembut.</small>', '<h3>AKHLAK · Kalimah Tayyibah</h3><div class="arabic">وَالْكَلِمَةُ الطَّيِّبَةُ صَدَقَةٌ</div><small>Biasakan bertutur dengan kata yang baik.</small>');

// Replace P001 RIQA OS target and embedded QR with the page resolver for P002.
html = html.replace(/href="https:\/\/www\.rumahilmualquran\.com\/peserta\/belajar\/qrt\/QRT-T01\/belajar"/, `href="${riqaUrl}"`);
html = html.replace(/<img src="data:image\/png;base64,[^"]+">/, `<img src="${qr}">`);
exact('<div class="id">QRT-T01</div>', '<div class="id">QJ1-P002</div>');
exact('<span>QJ1-P001</span>', '<span>QJ1-P002</span>');

await fs.writeFile(file, html, "utf8");
console.log("QJ1-P002 deterministic master proof built -> dist-p002/index.html");

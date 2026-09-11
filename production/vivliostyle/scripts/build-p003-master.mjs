import fs from "node:fs/promises";
import path from "node:path";
import QRCode from "qrcode";

const root = path.resolve(import.meta.dirname, "..");
const sourceDir = path.join(root, "dist-p002");
const out = path.join(root, "dist-p003");
const file = path.join(out, "index.html");
const riqaUrl = "https://www.rumahilmualquran.com/q/QJ1-P003";

await fs.rm(out, { recursive: true, force: true });
await fs.cp(sourceDir, out, { recursive: true });
let html = await fs.readFile(file, "utf8");

// P003 follows the frozen 40-page curriculum and the locked Organic Arabesque visual baseline.
// Jilid 1 remains isolated letters only, fathah only at this stage.
const rows = [
  ["جَ حَ", "حَ خَ", "خَ جَ"],
  ["جَ خَ", "حَ جَ", "خَ حَ"],
  ["جَ حَ خَ", "حَ خَ جَ", "خَ جَ حَ"],
  ["جَ بَ حَ", "حَ تَ خَ", "خَ ثَ جَ"],
  ["جَ ءَ خَ", "حَ أَ جَ", "خَ بَ حَ"],
  ["تَ جَ حَ", "ثَ حَ خَ", "أَ خَ جَ"],
  ["جَ حَ بَ", "حَ خَ تَ", "خَ جَ ثَ"],
  ["بَ جَ خَ", "تَ حَ جَ", "ثَ خَ حَ"]
];
const cells = rows.map(r => `<div class="r">${r.map(x => `<div class="c arabic">${x}</div>`).join("")}</div>`).join("");
const qr = await QRCode.toDataURL(riqaUrl, {
  errorCorrectionLevel: "H",
  margin: 1,
  width: 300,
  color: { dark: "#123f34", light: "#fffdf6" }
});

const exact = (from, to) => {
  if (!html.includes(from)) throw new Error(`P003 transform target not found: ${from}`);
  html = html.replace(from, to);
};

exact('<div class="num">02</div>', '<div class="num">03</div>');
exact('QJ1-P002 · Hamzah dan Alif dengan Fathah', 'QJ1-P003 · Jim, Ha, Kha dengan Fathah');
exact('Membedakan dan membaca <span class="arabic">ءَ أَ</span> bersama murojaah <span class="arabic">بَ تَ ثَ</span>. Hanya huruf lepas berharakat fathah.', 'Membedakan dan membaca <span class="arabic">جَ حَ خَ</span> bersama murojaah materi sebelumnya. Hanya huruf lepas berharakat fathah.');
exact('<div class="arabic">ءَ أَ</div></div></section><main class="practice">', '<div class="arabic">جَ حَ خَ</div></div></section><main class="practice">');
html = html.replace(/<main class="practice">[\s\S]*?<\/main>/, `<main class="practice">${cells}</main>`);

exact('<h3>TAHFIDZ · An-Nas 2</h3><div class="arabic">مَلِكِ النَّاسِ</div><small>Talqin dan hafalkan ayat.</small>', '<h3>TAHFIDZ · An-Nas 3</h3><div class="arabic">إِلَٰهِ النَّاسِ</div><small>Talqin dan hafalkan ayat.</small>');
exact('<h3>BI\'AH ARABIYAH</h3><div class="arabic">اُنْظُرْ</div><small>Gunakan instruksi ini dalam pembelajaran.</small>', '<h3>BI\'AH ARABIYAH</h3><div class="arabic">اِسْتَمِعْ</div><small>Gunakan instruksi ini dalam pembelajaran.</small>');
exact('<h3>AKHLAK · Kalimah Tayyibah</h3><div class="arabic">وَالْكَلِمَةُ الطَّيِّبَةُ صَدَقَةٌ</div><small>Biasakan bertutur dengan kata yang baik.</small>', '<h3>AKHLAK · Thaharah</h3><div class="arabic">الطُّهُورُ شَطْرُ الْإِيمَانِ</div><small>Tanamkan kebersihan dan kesucian sebagai bagian dari iman.</small>');

html = html.replace(/href="https:\/\/www\.rumahilmualquran\.com\/q\/QJ1-P002"/, `href="${riqaUrl}"`);
html = html.replace(/<img src="data:image\/png;base64,[^"]+">/, `<img src="${qr}">`);
exact('<div class="id">QJ1-P002</div>', '<div class="id">QJ1-P003</div>');
exact('<span>QJ1-P002</span>', '<span>QJ1-P003</span>');

await fs.writeFile(file, html, "utf8");
console.log("QJ1-P003 deterministic master proof built -> dist-p003/index.html");

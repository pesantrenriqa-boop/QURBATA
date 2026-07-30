# AUD-QJ3-006 — Normalisasi Item P021–P025

**Tanggal:** 30 Juli 2026  
**Tahap:** Audit Tahap II  
**Cakupan:** QJ3-P021–QJ3-P025  
**Sumber:** `books/jilid-3/pages/QJ3-B03A-Materi-P021-P025.md` v0.4.0-id  
**Status:** COMPLETE-STRUCTURAL — MENUNGGU TASHIH AHLI

## 1. Hasil Normalisasi

Sebanyak **120/120 kotak** telah dinormalisasi. Klasifikasi lam ditentukan oleh huruf yang benar-benar menyandang sukun: kata seperti `يَعْلَمُونَ` adalah transfer عْ + mad, bukan fokus لْ.

| Halaman | Item | 3 huruf | 4 huruf | 5 huruf | 6 huruf | Fokus لْ | Transfer | Lulus |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| QJ3-P021 | 24 | 8 | 16 | 0 | 0 | 9 | 8 | 24 |
| QJ3-P022 | 24 | 8 | 12 | 4 | 0 | 16 | 8 | 24 |
| QJ3-P023 | 24 | 8 | 12 | 4 | 0 | 18 | 6 | 24 |
| QJ3-P024 | 24 | 4 | 4 | 8 | 8 | 20 | 4 | 24 |
| QJ3-P025 | 24 | 4 | 4 | 4 | 12 | 0 | 15 | 24 |

## 2. Pemeriksaan Otomatis

| Pemeriksaan | Temuan |
|---|---:|
| Total item | 120 |
| Item multi-kata dalam kotak utama | 0 |
| Selisih jumlah huruf | 0 |
| Fokus lam tanpa لْ | 0 |
| Sukun baru prematur | 0 |
| Tasydid prematur | 0 |
| Alif-lam prematur | 0 |
| Sukun qalqalah prematur | 0 |
| Lulus semua pemeriksaan struktural | 120 |

## 3. Panel Transfer Qurani

| ID | Frasa | Sumber | Kata | لْ | Larangan mekanis | Status |
|---|---:|---|---:|---:|---:|---|
| Q-005-003-LAM-A | أَكْمَلْتُ لَكُمْ | QS 5:3 | 2 | ada | bersih | ELIGIBLE-CANDIDATE |
| Q-007-010-LAM-A | وَجَعَلْنَا لَكُمْ | QS 7:10 | 2 | ada | bersih | ELIGIBLE-CANDIDATE |

- Kedua frasa merupakan potongan berurutan persis: QS Al-Mā’idah 5:3 dan QS Al-A‘rāf 7:10.
- Keduanya berhenti pada `لَكُمْ`, sehingga مْ berada di akhir panel dan tidak membuka hubungan antarkata berikutnya.
- Bentuk `وَجَعَلْنَا لَكُمْ فِيهَا` tetap HOLD karena مْ akan bertemu kata berikutnya.
- Panel berada di luar 24 kotak. Empat kotak dapat dipakai sebagai satu bentang visual frasa setelah format cetak ditetapkan.
- Status kandidat belum menggantikan tashih mushaf acuan, rasm, qira’at, audio, Source-ID final, dan titik berhenti pedagogis.

## 4. Antrean Tashih Leksikal

### Prioritas A — keputusan ganti/pertahankan

- `مِلْحَفٌ`, `مِلْقَطٌ`, `مُلْتَقًى`, dan `مُلْتَحِفٌ`: ضبط, frekuensi, serta kelaziman untuk anak.
- `مُسْتَلْزِمٌ`, `مُسْتَلْهِمٌ`, `مُسْتَلْحَقٌ`, dan `مُسْتَلْطَفٌ`: morfologi dan maknanya relatif lanjut; jangan dipakai hanya demi mencapai enam huruf.
- `مَلْعُوبٌ`, `مَلْحُوظٌ`, dan `مَلْفُوفٌ`: makna dan konteks penggunaan perlu dibuat konkret.

### Prioritas B — transfer enam huruf

- Pola `يَعْلَمُونَ، يَعْمَلُونَ، يَخْرُجُونَ` dan seterusnya relevan untuk keterampilan membaca Al-Qur’an serta mad wāw.
- Setiap verba harus dipastikan ضبط dan maknanya, tetapi pola ـُونَ layak dipertahankan sebagai transfer prioritas.
- `يَسْتَغْفِرُ` layak sebagai puncak kompleksitas apabila peserta telah menguasai seluruh penyandang sukun di dalamnya; tidak boleh disederhanakan menjadi tangga dua huruf.

## 5. Status

Kelulusan mekanis hanya mengesahkan struktur data dan batas materi. Seluruh item dan dua panel frasa tetap menunggu tashih ahli sebelum whitelist, uji, audio produksi, atau cetak.

## 6. Berkas Data

Basis data audit: `data/jilid-3/QJ3-ITEMS-P021-P025.csv`.

Tahap berikutnya: normalisasi P026–P030 untuk alif-lam qamariyah dan checkpoint awā’il kedua `طس`.

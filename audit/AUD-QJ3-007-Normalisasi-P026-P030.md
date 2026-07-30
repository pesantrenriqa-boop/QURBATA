# AUD-QJ3-007 — Normalisasi Item P026–P030

**Tanggal:** 30 Juli 2026  
**Tahap:** Audit Tahap II  
**Cakupan:** QJ3-P026–QJ3-P030  
**Sumber:** `books/jilid-3/pages/QJ3-B03B-Materi-P026-P030.md`  
**Status:** COMPLETE-STRUCTURAL — MENUNGGU TASHIH AHLI

## 1. Hasil Normalisasi

Sebanyak **120/120 kotak** telah dinormalisasi. Bentuk utama batch menggunakan notasi pedagogis `اَلْ` pada posisi mulai; notasi ini belum dianggap rasm mushaf final.

| Halaman | Item | 3 huruf | 4 huruf | 5 huruf | 6 huruf | Qamariyah | Lulus |
|---|---:|---:|---:|---:|---:|---:|---:|
| QJ3-P026 | 24 | 4 | 8 | 8 | 4 | 20 | 24 |
| QJ3-P027 | 24 | 4 | 4 | 8 | 8 | 20 | 24 |
| QJ3-P028 | 24 | 4 | 4 | 8 | 8 | 16 | 24 |
| QJ3-P029 | 24 | 4 | 4 | 8 | 8 | 16 | 24 |
| QJ3-P030 | 24 | 4 | 4 | 8 | 8 | 16 | 24 |

## 2. Pemeriksaan Otomatis

| Pemeriksaan | Temuan |
|---|---:|
| Total item | 120 |
| Item qamariyah | 88 |
| Item multi-kata | 0 |
| Selisih jumlah huruf | 0 |
| Huruf non-qamariyah setelah ال | 0 |
| Lam sukun hilang dari bentuk qamariyah | 0 |
| Tasydid prematur | 0 |
| Sukun qalqalah prematur | 0 |
| Campuran rasm `ٱلْ` dalam kotak pedagogis | 0 |
| Lulus semua pemeriksaan struktural | 120 |
| Checkpoint طس tersedia | 1/1 |
| Pengulangan checkpoint طه | 0 |

## 3. Sebaran Huruf Setelah Alif-Lam

- ء: 12 item
- ب: 2 item
- ج: 1 item
- ح: 6 item
- خ: 5 item
- ع: 8 item
- غ: 6 item
- ف: 9 item
- ق: 7 item
- ك: 6 item
- م: 6 item
- ه: 8 item
- و: 4 item
- ي: 8 item

Sebaran ini merupakan hitungan paparan, bukan bukti pemerataan final. Audit lintas P026–P040 tetap diperlukan karena beberapa kata sengaja diulang untuk evaluasi.

## 4. Tashih Rasm dan Ortografi

- `اَلْ` adalah notasi pedagogis posisi mulai, sedangkan cetakan mushaf dapat menggunakan `ٱلْ` dan tanda rasm lain.
- Jangan mencampur notasi pedagogis dan rasm Utsmani dalam satu lapisan data.
- `اَلْهُدَى` memerlukan keputusan penulisan alif maqṣūrah/tanda alif kecil menurut standar cetak.
- Bentuk dengan hamzah, seperti `اَلْأَبُ`, `اَلْأَمَلُ`, dan `اَلْأَلِيمُ`, memerlukan audit jarak, kursi, dan audio.
- Variasi `اَلْفَمُ/اَلْفَمَ/اَلْفَمِ` dihitung sebagai tiga latihan i‘rab tetapi satu lema kosakata.
- Kata yang serupa dengan lafaz Qurani tidak diberi Source-ID sebelum locator dan rasmnya diverifikasi.

## 5. Antrean Tashih Leksikal–Makna

- Nama/sifat seperti `اَلْحَلِيمُ، اَلْحَكِيمُ، اَلْعَلِيمُ، اَلْغَفُورُ، اَلْهَادِي` memerlukan konteks makna dan akidah yang tepat.
- `اَلْأَلِيمُ` lazim sebagai sifat yang menerangkan sesuatu; penggunaannya sebagai kata tunggal perlu dinilai.
- `اَلْقُعُودُ، اَلْغُرُوبُ، اَلْهَلَاكُ` adalah nomina abstrak/kejadian; pastikan sesuai tingkat usia.
- `يَيْأَسُ` memerlukan tashih ضبط dan keterbacaan bentuk hamzahnya.
- Tiga tanwin pada `هُدًى، هَوًى، وَحْيٌ` harus tetap diperlakukan sebagai kata tunggal, bukan awal hubungan antarkata.

## 6. Keputusan Frasa dan Checkpoint

- Tidak ada frasa baru pada P026–P030 karena kompetensi masih terbatas pada `اَلْ` di posisi mulai.
- Frasa qamariyah ditahan sampai P033 agar penyambungan dan hubungan antarkata tidak prematur.
- Checkpoint `طس — طَا سِينْ` berada di luar 24 kotak, tidak mengulang `طه`, dan tetap memerlukan rasm, panjang bacaan, nama surat, Source-ID, serta audio ahli.
- Nama huruf hijaiyah umum tidak diulang; pelafalan checkpoint merupakan pembelajaran awā’il as-suwar yang telah diprioritaskan.
- Kelulusan struktural tidak berarti SIAP UJI atau SIAP CETAK.

## 7. Berkas Data

Basis data audit: `data/jilid-3/QJ3-ITEMS-P026-P030.csv`.

Tahap berikutnya: normalisasi P031–P035, audit kata 4–8 huruf, kontras tanpa/dengan ال, serta frasa Qurani autentik yang mulai aktif pada P033.

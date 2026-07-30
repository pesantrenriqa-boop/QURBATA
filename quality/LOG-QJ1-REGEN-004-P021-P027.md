# LOG-QJ1-REGEN-004 — Status Regenerasi P021–P027

**Status:** DRAF TERKENDALI  
**Tanggal:** 30 Juli 2026  
**Branch:** `feature/qj1-master-structure`  
**Pengendali:** `DEC-CUR-006`

## 1. Tujuan

Mencatat status aktual regenerasi halaman QJ1-P021–QJ1-P027 setelah kebijakan pemerataan mutlak `DEC-CUR-002` digantikan untuk halaman reguler oleh distribusi materi baru dan murojaah 60:40 pada `DEC-CUR-006`.

## 2. Status Halaman

| Halaman | Fungsi | Status Distribusi | Hasil |
|---|---|---|---|
| QJ1-P021 | Kasrah ص ض ط ظ | PASS-DISTRIBUTION-DRAFT | 39 baru / 25 murojaah |
| QJ1-P022 | Kasrah ف ق ك ل | PASS-DISTRIBUTION-DRAFT | 39 baru / 25 murojaah |
| QJ1-P023 | Kasrah م ن و ي | PASS-DISTRIBUTION-DRAFT | 39 baru / 25 murojaah |
| QJ1-P024 | Integrasi seluruh kasrah | TIDAK TERKENA 60:40 | Halaman integrasi; seluruh token merupakan review |
| QJ1-P025 | Kontras fathah–kasrah | TIDAK TERKENA 60:40 | Halaman integrasi/kontras; seluruh token merupakan review |
| QJ1-P026 | Dhammah awal أ ب ت ث | PASS-DISTRIBUTION-DRAFT | Diregenerasi menjadi 39 baru / 25 murojaah |
| QJ1-P027 | Dhammah ج ح خ ع غ ه | ACTION REQUIRED | Masih memakai 6 baru / 58 review berdasarkan kebijakan lama |

## 3. Perubahan QJ1-P026

QJ1-P026 versi `0.6.0-id` telah:

- memakai 24 latihan unik;
- memakai 64 token;
- membagi Tangga 1–8 menjadi dua huruf dan Tangga 9–24 menjadi tiga huruf;
- memuat 39 token materi baru dan 25 token murojaah;
- mempertahankan larangan bentuk sambung, mad, tanwin, sukun, tasydid, dan materi prematur;
- mempertahankan kontrol bunyi dhammah pendek tanpa tambahan waw;
- tetap berstatus belum siap uji ahli.

Commit perubahan P026: `ef440b28f841008fab8dd86c88cda0a7b18094f7`.

## 4. Temuan Terbuka

QJ1-P027 masih menyatakan:

- 6 token materi baru;
- 58 token review;
- distribusi berdasarkan `DEC-CUR-002`;
- sebaran 27 fathah, 27 kasrah, dan 10 dhammah.

Kondisi tersebut tidak lagi sesuai untuk halaman reguler pengenalan materi baru setelah `DEC-CUR-006` berlaku.

## 5. Antrean Berikutnya

1. Regenerasi QJ1-P027 menjadi 39 token baru dan 25 token murojaah.
2. Audit QJ1-P028 sebagai halaman khusus Bahasa Arab yang tidak tunduk pada rasio 60:40.
3. Lanjutkan regenerasi halaman reguler P029 dan seterusnya.
4. Jalankan audit ulang struktur, whitelist, token, dan rotasi murojaah fase dhammah.

## 6. Batas Klaim

Log ini hanya membuktikan konsistensi struktur draf. Log ini tidak membuktikan validitas akademik, ketepatan makhraj, efektivitas, kesiapan uji, kesiapan cetak, atau aktivasi objek. PR #2 tetap Draft.

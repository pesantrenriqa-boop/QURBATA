# AUD-QJ3-002 — Normalisasi Item P001–P005

**Tanggal:** 30 Juli 2026  
**Tahap:** Audit Tahap II  
**Cakupan:** QJ3-P001–QJ3-P005  
**Sumber:** `books/jilid-3/pages/QJ3-B01B-Regenerasi-P001-P005.md`  
**Status:** COMPLETE-STRUCTURAL — MENUNGGU TASHIH AHLI

## 1. Hasil

Sebanyak **120/120 kotak** telah dinormalisasi menjadi satu baris per item dengan Item-ID stabil. Data menyimpan Page-ID, nomor kotak, teks Arab, jumlah huruf deklaratif dan terhitung, penyandang sukun, target sukun, fungsi pedagogis, jenis mad, jenis tanwin, tipe sumber, status tashih, dan flag validasi.

| Halaman | Target | Item | Fokus | Murojaah | Mad–sukun | Lulus struktural |
|---|---:|---:|---:|---:|---:|---:|
| QJ3-P001 | مْ | 24 | 12 | 6 | 6 | 24 |
| QJ3-P002 | لْ | 24 | 12 | 6 | 6 | 24 |
| QJ3-P003 | فْ | 24 | 12 | 6 | 6 | 24 |
| QJ3-P004 | كْ | 24 | 12 | 6 | 6 | 24 |
| QJ3-P005 | سْ / شْ | 24 | 12 | 6 | 6 | 24 |

## 2. Pemeriksaan Otomatis

| Pemeriksaan | Temuan |
|---|---:|
| Total item | 120 |
| Item multi-kata | 0 |
| Selisih jumlah huruf | 0 |
| Target sukun hilang pada item fokus/integrasi | 0 |
| Tasydid prematur | 0 |
| Alif-lam prematur | 0 |
| Sukun qalqalah prematur | 0 |
| Mad hilang pada kelompok mad–sukun | 0 |
| Lulus semua pemeriksaan struktural | 120 |

## 3. Aturan Status

- `PASS_STRUCTURAL` hanya berarti item lolos batas teknis jilid; bukan pengesahan bahasa, rasm, atau kelayakan cetak.
- Seluruh item tetap `AR-CANDIDATE` dan `PENDING` sampai makna, harakat, ortografi, kelaziman kosakata anak, dan audio ditashih ahli.
- Tidak digunakan istilah hukum pertemuan nun/mim/tanwin pada tahap ini.
- Murojaah mengikuti keputusan aktif: materi baru sekitar 60% dan materi lama sekitar 40%, dengan pemerataan kompetensi yang masih diperlukan untuk membaca Al-Qur’an nyata.
- Tidak ada tangga dua huruf; Jilid 3 dimulai dari kata minimal tiga huruf.

## 4. Berkas Data

Basis data audit: `data/jilid-3/QJ3-ITEMS-P001-P005.csv`.

Tahap berikutnya: tashih item berisiko, lalu normalisasi P006–P010 dengan skema identik.

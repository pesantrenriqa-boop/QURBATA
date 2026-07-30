# AUD-QJ3-008 — Normalisasi Item P031–P035

**Tanggal:** 30 Juli 2026  
**Tahap:** Audit Tahap II  
**Cakupan:** QJ3-P031–QJ3-P035  
**Sumber:** `books/jilid-3/pages/QJ3-B04A-Materi-P031-P035.md`  
**Status:** COMPLETE-STRUCTURAL — MENUNGGU TASHIH AHLI

## 1. Hasil Normalisasi

Sebanyak **120/120 kotak** telah dinormalisasi. Kotak komponen kata dan kotak frasa utuh dibedakan agar pengulangan kelancaran tidak dihitung sebagai frasa atau kosakata baru.

| Halaman | Item | Komponen frasa | Frasa utuh | Panjang huruf tertinggi/item | Lulus |
|---|---:|---:|---:|---:|---:|
| QJ3-P031 | 24 | 0 | 0 | 7 | 24 |
| QJ3-P032 | 24 | 0 | 0 | 7 | 24 |
| QJ3-P033 | 24 | 9 | 7 | 11 | 24 |
| QJ3-P034 | 24 | 0 | 0 | 7 | 24 |
| QJ3-P035 | 24 | 2 | 2 | 9 | 24 |

## 2. Pemeriksaan Otomatis

| Pemeriksaan | Temuan |
|---|---:|
| Total item | 120 |
| Kotak komponen frasa | 11 |
| Kotak frasa utuh | 9 |
| Frasa unik | 5 |
| Multi-kata di luar kotak frasa | 0 |
| Tasydid prematur | 0 |
| Sukun qalqalah prematur | 0 |
| Huruf non-qamariyah setelah ال | 0 |
| Tanwin antarkata prematur | 0 |
| Nun/mim sukun antarkata prematur | 0 |
| Lulus semua pemeriksaan struktural | 120 |

## 3. Audit Lima Frasa Qurani

| ID | Frasa | Sumber | Kata | Kotak frasa utuh | Larangan mekanis | Status |
|---|---:|---|---:|---:|---|---|
| FRQ-QJ3-002 | ٱلْيَوْمَ يَئِسَ | QS 5:3 | 2 | 2 | bersih | ELIGIBLE-CANDIDATE |
| FRQ-QJ3-003 | ٱلْيَوْمَ أَكْمَلْتُ | QS 5:3 | 2 | 2 | bersih | ELIGIBLE-CANDIDATE |
| FRQ-QJ3-004 | ٱلْعَفْوَ وَأْمُرْ | QS 7:199 | 2 | 2 | bersih | ELIGIBLE-CANDIDATE |
| FRQ-QJ3-001 | ٱلْكِتَابُ لَا رَيْبَ | QS 2:2 | 3 | 1 | bersih | ELIGIBLE-CANDIDATE |
| FRQ-QJ3-006 | ٱلْيَوْمَ نَخْتِمُ | QS 36:65 | 2 | 2 | bersih | ELIGIBLE-CANDIDATE |

- Semua frasa merupakan kata berurutan dalam satu ayat dan telah dicocokkan dengan locator sumber.
- Pengulangan frasa utuh pada kotak keempat adalah tikrar kelancaran, bukan materi baru.
- `ٱلْكِتَابُ لَا رَيْبَ` terdiri dari tiga kata; empat kotaknya digunakan untuk tiga komponen dan satu frasa utuh.
- Status kandidat tetap membutuhkan mushaf acuan, rasm, qira’at, audio, Source-ID final, dan pengesahan titik mulai/akhir.

## 4. Audit Tangga dan Kosakata

- Panjang tertinggi mencapai delapan huruf pada P035 tanpa kembali ke huruf tunggal atau tangga dua huruf.
- `يَسْتَغْفِرُونَ، يَسْتَعْمِلُونَ، يَسْتَخْرِجُونَ، يَسْتَخْلِفُونَ` merupakan transfer kompleks yang relevan, tetapi wajib ditashih per morfologi dan makna.
- Variasi tanpa/dengan ال pada P032 adalah pasangan baca; bentuk ma‘rifah kehilangan tanwin. Ini belum dijadikan teori nahwu formal.
- Variasi tanwin P034 dihitung sebagai latihan bentuk, bukan lema kosakata baru.
- Bentuk pasif/abstrak seperti `مَغْفُورٌ، مَخْلُوقٌ، مَظْلُومٌ، مَضْمُونٌ` memerlukan konteks makna ramah anak.
- Nama/sifat seperti `اَلْحَكِيمُ، اَلْغَفُورُ` memerlukan integrasi makna-akidah yang benar.

## 5. Status

Kelulusan mekanis tidak mengesahkan rasm, qira’at, makna, audio, atau kesiapan cetak. Seluruh kata dan lima frasa tetap CANDIDATE/PENDING.

## 6. Berkas Data

Basis data audit: `data/jilid-3/QJ3-ITEMS-P031-P035.csv`.

Tahap berikutnya: normalisasi P036–P040, audit frasa lanjutan, potongan Qurani, simulasi, dan evaluasi akhir Jilid 3.

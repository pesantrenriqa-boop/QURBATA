# QLS-001 — QURBATA Learning Standard

**Status:** ACTIVE DRAFT  
**Branch:** `content/qurbata-jilid-1-8-production`  
**Scope:** Learning content, not Akademi QURBATA 21 marhalah.

## 1. Domain Pembelajaran

- `QT` — QURBATA Tartil
- `QA` — QURBATA Arabic
- `QN` — QURBATA NIDOM/Akhlak

Akademi QURBATA dipisahkan sebagai jalur ujian dan sertifikasi SDM.

## 2. Hierarki Akademik

`Domain → Kompetensi → Unit Kompetensi → Elemen → Learning Outcome → Indikator → Evidence → Materi → Contoh → Stimulus → Halaman → Jilid`

## 3. Aturan Wajib Halaman

Setiap halaman latihan berisi 24 kotak dan wajib memadukan:

- materi baru;
- review halaman sebelumnya;
- review rentang menengah;
- review materi awal/akhir yang sudah lama tidak muncul;
- review global kompetensi inti.

Proporsi awal generator:

- 10 kotak `NEW`;
- 7 kotak `REVIEW_IMMEDIATE`;
- 5 kotak `REVIEW_SPACED`;
- 2 kotak `REVIEW_GLOBAL`.

Proporsi dapat disesuaikan menurut fungsi halaman, tetapi tidak boleh menghilangkan review.

## 4. Aturan Sumber

Iqro' 1–6 digunakan sebagai referensi pedagogis: progression, kepadatan latihan, pengulangan, dan pola transisi. Contoh QURBATA diseleksi dan disusun ulang secara mandiri dari sumber Al-Qur'an, bahasa Arab, dan bank recovery QURBATA.

## 5. Identitas Data

- Kompetensi: `QT-CMP-###`
- Unit: `QT-UK-###`
- Halaman: `QB-J##-H##`
- Kotak: `QB-J##-H##-K##`
- Contoh: `QT-EX-######`
- Stimulus: `QT-ST-######`

## 6. Gate Produksi

Halaman tidak boleh berstatus `APPROVED` sebelum:

1. prerequisite unit terpenuhi;
2. 24 kotak lengkap;
3. komposisi NEW/REVIEW tervalidasi;
4. tidak ada unsur di luar whitelist progression;
5. sumber teks tervalidasi;
6. duplikasi terkontrol;
7. error map dan evidence tersedia.

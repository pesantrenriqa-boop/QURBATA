# QWO Corpus Build Report V1

Tanggal: 4 Agustus 2026
Branch: `content/qurbata-jilid-1-8-production`
Status: GENERATED — PEDAGOGICAL REVIEW REQUIRED

## Sumber

- File: `quran-uthmani.txt`
- Format: `surah|ayah|teks Utsmani`
- Sumber teks: Tanzil Project, Uthmani Quran Text
- SHA-256: `7f30c647331a61100ebf24a80507dc0fcdd9f2df97f1312b5b2dfcb982a7f326`

## Hasil proses

- Ayat valid: 6.236
- Token occurrence: 77.881
- Objek kanonik unik: 18.818
- Kandidat QWO terpilih: 2.500
- Status seluruh kandidat: `CANDIDATE`
- Objek berulang dalam candidate pool: 0 berdasarkan `CanonicalKey`

## Distribusi kompetensi utama kandidat

- MAD_ALIF: 216
- MAD_YA: 216
- MAD_WAWU: 215
- TANWIN_FATH: 215
- TANWIN_DAMM: 215
- TANWIN_KASR: 215
- SUKUN: 215
- TASYDID: 215
- HAMZAH: 215
- NON_CONNECTOR_TRANSITION: 215
- CONNECTED_3_PLUS: 215
- ALIF_MAQSHURAH: 72
- LENGTH_1_2: 46
- TA_MARBUTAH: 8
- ALIF_LAM: 7

## Prinsip yang diterapkan

1. Seluruh objek berasal dari corpus Al-Qur'an.
2. Kompetensi boleh berulang, objek tidak diulang dalam candidate pool.
3. Teks Utsmani asli dipertahankan.
4. Setiap kandidat memiliki referensi surah, ayat, dan indeks token.
5. ID kandidat deterministik berdasarkan objek dan kompetensi utama.
6. Generator tidak menaikkan kandidat menjadi ACTIVE.

## Artefak yang dihasilkan

- `TOKEN_OCCURRENCE.csv` — 77.881 occurrence.
- `LEXEME_ENTRY.csv` — 18.818 objek unik.
- `QWO_CANDIDATES_2500.csv` — candidate pool untuk penyusunan delapan jilid.
- occurrence shards per rentang surah.
- candidate shards per 500 objek.
- `BUILD_REPORT.json`.
- `SOURCE-NOTICE.txt`.
- `build_qwo_from_tanzil.py`.

## Gate berikutnya

Candidate pool belum boleh langsung dipasang ke halaman buku. Tahap berikutnya hanya:

1. audit akurasi label kompetensi;
2. tetapkan dependency dan whitelist setiap jilid;
3. distribusikan objek unik ke halaman Jilid 1–8;
4. pastikan pengulangan hanya pada kompetensi, bukan objek;
5. promosikan objek yang lolos menjadi `PEDAGOGY_REVIEWED` lalu `ACTIVE`.

Tidak ada perluasan ruang lingkup sebelum distribusi Jilid 1–8 selesai.

# Jilid 1 Letter and Fragment Foundation Status V1

Tanggal: 4 Agustus 2026
Branch: `content/qurbata-jilid-1-8-production`
Status: IMPLEMENTED — DRAFT FOR PEDAGOGICAL REVIEW

## Hasil eksekusi corpus

- Ayat sumber valid: 6.236
- Token occurrence: 77.881
- Objek huruf yang memiliki jejak sumber Al-Qur'an: 36 bentuk
- Fragmen dua dan tiga grapheme Jilid-1-safe yang tersedia: lebih dari 10.000
- Fragmen unik yang dialokasikan pada rancangan halaman kerja: 768
- Pengulangan objek utama pada alokasi: 0

## Implementasi GitHub

1. `content/qwo/composer/runtime/letter_fragment_extractor.py`
2. `content/qwo/composer/templates/JILID-1-40-PAGE-BLUEPRINT-V1.csv`

## Prinsip yang diterapkan

1. Seluruh huruf dan fragmen memiliki `SourceRef` surah–ayat.
2. Teks Utsmani sumber tidak diubah.
3. Untuk Jilid 1, fragmen awal dibatasi pada fathah, kasrah, dan dhammah.
4. Sukun, tasydid, tanwin, dan mad tidak dimasukkan ke fragmen awal.
5. Kompetensi dapat diulang, tetapi objek Arab utama tidak diulang.
6. Halaman 20 dan 30 menyediakan slot Awailus Suwar sesuai keputusan kurikulum terdahulu.
7. Halaman evaluasi, hafalan, dan integrasi Bahasa Arab tidak dipaksa menjadi QWO.

## Struktur rancangan 40 halaman

- Halaman 1–4: huruf tunggal dan keluarga visual.
- Halaman 5–12: fragmen dua huruf dengan harakat dasar.
- Halaman 13–16: sambungan dan non-connector dua huruf.
- Halaman 17–30: fragmen tiga huruf bertahap.
- Halaman 31–36: murojaah kompetensi dengan objek baru.
- Halaman 37–40: evaluasi, hafalan, Bahasa Arab, dan evaluasi akhir.

## Gate berikutnya

Rancangan ini belum dianggap isi final buku. Gate berikutnya adalah audit pedagogis per halaman terhadap:

- urutan keluarga huruf;
- proporsi materi baru dan murojaah;
- bentuk yang belum boleh muncul;
- pemerataan huruf;
- kelayakan 24 objek per halaman;
- ketepatan penempatan Awailus Suwar.

Setelah gate ini lolos, Book Composer dapat menghasilkan halaman Jilid 1 dengan objek konkret dari master fragment tanpa memilih manual satu per satu.

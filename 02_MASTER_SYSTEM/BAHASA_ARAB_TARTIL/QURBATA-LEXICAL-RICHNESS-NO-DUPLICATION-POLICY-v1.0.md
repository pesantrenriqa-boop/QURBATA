# QURBATA LEXICAL RICHNESS & NO-DUPLICATION POLICY

**Status:** ACTIVE POLICY — v1.0  
**Tanggal:** 2026-09-25  
**Berlaku untuk:** seluruh pengembangan Bahasa Arab QURBATA, buku, Bi'ah 'Arabiyah, RIQA OS, audio, latihan, asesmen, dan corpus penelitian.

## 1. Prinsip inti

**Repeat for mastery, expand for richness.**

QURBATA membedakan tegas antara:
1. **pengulangan pedagogis** — kemunculan kembali unsur lama untuk penguatan, retrieval, otomatisasi, dan penggunaan dalam konteks baru; dan
2. **duplikasi materi** — memasukkan unsur yang sudah pernah diperkenalkan sebagai seolah-olah materi/kosakata baru.

Pengulangan pedagogis diperbolehkan dan direncanakan. Duplikasi sebagai materi baru harus dicegah.

## 2. Rasio pengembangan

Baseline desain materi:
- **±60% unsur baru**;
- **±40% review/penguatan unsur lama**.

Rasio ini adalah pedoman desain, bukan kewajiban matematis per halaman. Audit dilakukan pada unit pembelajaran yang cukup representatif.

## 3. Unit yang harus dibedakan

Database/master tidak boleh mencampur:
- **LEMMA**: bentuk kamus/akar leksikal yang dihitung sebagai kosakata unik;
- **SURFACE FORM**: bentuk aktual yang muncul karena i'rab, dhamir, gender, jumlah, tashrif, dll.;
- **PHRASE**: frasa/ta'bir;
- **SENTENCE**: kalimat/ungkapan komunikatif;
- **PATTERN**: pola/struktur yang dapat diisi unsur berbeda;
- **PARAGRAPH**: konteks wacana;
- **QURANIC ITEM**: unsur yang benar-benar terverifikasi dari ayat/corpus Al-Qur'an.

## 4. Aturan hitung kosakata baru

Satu lemma hanya dihitung **satu kali** sebagai kosakata baru pada titik introduksi pertama.

Contoh:
- مُصْحَفٌ = lemma baru saat pertama diperkenalkan.
- مُصْحَفِي / مُصْحَفُكَ / فِي الْمُصْحَفِ = bukan tiga kosakata baru; dicatat sebagai bentuk/konstruksi/penggunaan baru.

Bentuk turunan dapat menjadi **target kompetensi morfologis atau gramatikal baru**, tetapi tidak boleh menaikkan angka lemma unik secara palsu.

## 5. Aturan pengulangan yang bernilai

Unsur lama boleh muncul kembali jika minimal salah satu terjadi:
- konteks penggunaan berubah;
- fungsi komunikatif bertambah;
- struktur sintaksis bertambah;
- bentuk morfologis bertambah;
- santri berpindah dari recognition → guided production → independent production;
- unsur lama dikombinasikan dengan unsur baru;
- digunakan untuk retrieval/spaced review;
- digunakan dalam dialog, paragraph, asesmen, atau praktik nyata.

Jika tidak ada nilai tambah di atas, kemunculan ulang dikategorikan **redundant duplication** dan perlu direvisi.

## 6. Tangga pengayaan contoh

Jangan berhenti pada pengulangan:

اِقْرَأْ

Kembangkan secara kumulatif, misalnya:

اِقْرَأْ → اِقْرَأْ مِنْ هُنَا → اِقْرَأْ إِلَى هُنَا → اِقْرَأْ بَعْدَ صَدِيقِكَ → اِقْرَأْ بِصَوْتٍ وَاضِحٍ

Unsur lama tetap berfungsi sebagai jangkar, sedangkan setiap tahap membawa lexical/functional load baru.

## 7. Field wajib registry berikutnya

Setiap item Bahasa Arab baru diarahkan memiliki field:
- `item_id`
- `item_type`
- `arabic_surface`
- `lemma_id`
- `lemma`
- `meaning`
- `first_introduction`
- `source`
- `jilid`
- `page`
- `marhalah`
- `K_ID`
- `usage_context`
- `status_new_review`
- `previous_item_reference`
- `new_value_added`
- `occurrence_count`
- `audio_status`
- `assessment_status`
- `RIQA_OS_status`

## 8. Gate sebelum materi baru disahkan

Sebelum kata/frasa/kalimat diberi status **NEW**, editor/generator wajib mengecek:

1. Apakah lemma sudah ada di master?
2. Apakah frasa/kalimat identik atau sangat dekat sudah pernah digunakan?
3. Jika unsur lama digunakan lagi, apa nilai tambah barunya?
4. Apakah unit menjaga keseimbangan materi baru dan review?
5. Apakah kosakata baru memperluas domain komunikasi santri?
6. Apakah unsur tersebut dapat digunakan secara nyata dalam ekosistem QURBATA?

Jika lemma sudah ada, status default adalah **REVIEW/EXPANSION**, bukan NEW.

## 9. Sasaran kekayaan bahasa

QURBATA tidak mengejar angka kosakata secara artifisial. Sasaran utamanya adalah:

**lemma unik yang terus bertambah + jaringan frasa yang semakin luas + struktur yang semakin kompleks + kemampuan menggunakan bahasa secara nyata.**

Karena itu laporan perkembangan harus membedakan minimal:
- jumlah lemma unik;
- lemma baru per unit;
- lemma review;
- jumlah frasa unik;
- jumlah ungkapan/kalimat unik;
- jumlah pola/struktur;
- tingkat reuse bernilai;
- redundant duplication rate.

## 10. Integrasi RIQA OS

RIQA OS diarahkan memiliki duplicate guard:
- saat editor memasukkan materi, sistem mencari lemma/frasa/kalimat yang sudah ada;
- jika ditemukan, tampilkan lokasi introduksi pertama;
- editor memilih `REVIEW`, `EXPANSION`, atau membuktikan bahwa item memang `NEW`;
- sistem tidak menghitung REVIEW/EXPANSION sebagai lemma baru;
- dashboard dapat menampilkan pertumbuhan lexical richness per Marhalah.

## 11. Aturan governance

1. Master Bank Kosakata & Kalimat adalah sumber rujukan utama registry.
2. Tidak menghapus pengulangan yang memang dibutuhkan untuk belajar.
3. Tidak menghitung pengulangan sebagai kekayaan kosakata baru.
4. Jangan mengubah teks FROZEN hanya demi mengejar variasi; perubahan harus melalui prosedur revisi.
5. Materi REVIEW/RECOVERED dapat diaudit untuk mengurangi redundant duplication sebelum freeze.
6. Setiap ekspansi corpus harus menjaga traceability ke sumber.

## 12. KPI audit awal

KPI yang akan dihitung setelah corpus dinormalisasi:
- `unique_lemma_count`
- `new_lemma_ratio`
- `review_lemma_ratio`
- `unique_phrase_count`
- `unique_sentence_count`
- `valuable_reuse_count`
- `redundant_duplication_count`
- `redundant_duplication_rate`

**Target prinsip:** redundant duplication ditekan serendah mungkin tanpa menghilangkan spaced repetition dan cumulative learning.
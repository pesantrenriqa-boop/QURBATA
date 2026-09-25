# QURBATA LEXICAL NORMALIZATION REGISTER

**Status:** ACTIVE WORKING REGISTER — v0.1  
**Tanggal:** 2026-09-25  
**Policy induk:** `QURBATA-LEXICAL-RICHNESS-NO-DUPLICATION-POLICY-v1.0.md`

## Tujuan
Register ini mengontrol agar pengayaan Bahasa Arab QURBATA tidak menghasilkan angka semu karena bentuk kata, frasa, atau kalimat yang berulang dihitung sebagai materi baru. Prinsip: **Repeat for mastery, expand for richness.**

## Status item
- `NEW-LEMMA` = lemma benar-benar pertama kali diperkenalkan.
- `REVIEW` = lemma lama digunakan kembali tanpa target bentuk/struktur baru.
- `EXPANSION-MORPH` = lemma lama, tetapi bentuk morfologis baru menjadi target.
- `EXPANSION-SYNTAX` = unsur lama masuk struktur sintaksis baru.
- `EXPANSION-FUNCTION` = unsur lama digunakan untuk fungsi komunikatif baru.
- `REDUNDANT` = pengulangan tanpa nilai pedagogis yang jelas; kandidat revisi.

## Normalisasi awal keluarga ق ر أ

| Surface form | Lemma | Status | Nilai tambah |
|---|---|---|---|
| اِقْرَأْ | قَرَأَ | NEW-LEMMA pada introduksi pertama | imperatif mudzakkar |
| أَقْرَأُ | قَرَأَ | EXPANSION-MORPH | orang pertama mudhari' |
| تَقْرَأُ | قَرَأَ | EXPANSION-MORPH | orang kedua / konteks pertanyaan |
| اِقْرَئِي | قَرَأَ | EXPANSION-MORPH | imperatif muannats |
| قِرَاءَةٌ | قَرَأَ | EXPANSION-MORPH | masdar |

Kelima bentuk tersebut tidak boleh dilaporkan sebagai lima lemma unik.

## First-introduction map P001–P012

| Page | Target komunikatif | Klasifikasi utama | Catatan |
|---|---|---|---|
| P001 | مَاذَا تَقْرَأُ؟ | NEW / EXPANSION-MORPH | pertanyaan tentang objek bacaan |
| P002 | أَقْرَأُ الْقُرْآنَ | EXPANSION-MORPH/FUNCTION | jawaban orang pertama |
| P003 | اِقْرَأْ مِنْ هُنَا | EXPANSION-FUNCTION | titik mulai bacaan |
| P004 | اِقْرَأْ إِلَى هُنَا | EXPANSION-FUNCTION | batas akhir bacaan |
| P005 | penguatan P001–P004 | REVIEW | tidak dihitung sebagai target leksikal baru kecuali ada lemma baru dalam paragraf |
| P006 | latihan kumulatif P001–P004 | REVIEW | audit redundansi diperlukan |
| P007 | دَوْرُ مَنْ؟ | NEW-LEMMA/FUNCTION | domain giliran |
| P008 | دَوْرِي | EXPANSION-MORPH/FUNCTION | kepemilikan/giliran diri |
| P009 | الْآنَ دَوْرُكَ | EXPANSION-FUNCTION | menyerahkan giliran |
| P010 | اِقْرَأْ بَعْدَ صَدِيقِكَ | NEW + EXPANSION-FUNCTION | urutan aktivitas dan teman |
| P011 | اِسْمَعْ إِلَى صَدِيقِكَ | NEW + EXPANSION-FUNCTION | menyimak teman |
| P012 | latihan komunikatif kumulatif | REVIEW | tidak otomatis dihitung sebagai materi baru |

## Duplicate guard

Sebelum item baru dimasukkan, cek berurutan:
1. normalisasi harakat dan tanda baca untuk pencocokan;
2. cek surface form identik;
3. cek lemma yang sama;
4. cek frasa yang sama atau hanya berbeda dhamir/gender;
5. cek pola sintaksis yang sama;
6. cek fungsi komunikatif;
7. tentukan `NEW`, `REVIEW`, `EXPANSION-*`, atau `REDUNDANT`.

## Aturan pengayaan

Jika item lama harus muncul kembali, prioritaskan pengayaan bertahap. Contoh:

`اِقْرَأْ` → `اِقْرَأْ مِنْ هُنَا` → `اِقْرَأْ إِلَى هُنَا` → `اِقْرَأْ بَعْدَ صَدِيقِكَ` → `اِقْرَأْ بِصَوْتٍ وَاضِحٍ`

Pengulangan kata `اِقْرَأْ` dipertahankan untuk otomatisasi, tetapi setiap tahap harus membawa fungsi, konstruksi, atau lemma pendamping baru.

## Candidate enrichment pool

Pool ini **belum otomatis menjadi materi FROZEN**; digunakan untuk mengganti redundant duplication setelah audit:

| Kandidat | Makna/fungsi | Domain |
|---|---|---|
| بِصَوْتٍ وَاضِحٍ | dengan suara jelas | performa membaca |
| بِهُدُوءٍ | dengan tenang | adab/performa |
| بِتَرْتِيلٍ | dengan tartil | Qur'an |
| صَحِّحْ | perbaikilah | feedback |
| حَاوِلْ | cobalah | scaffolding |
| اِنْتَظِرْ | tunggulah | manajemen interaksi |
| اِبْدَأْ | mulailah | urutan aktivitas |
| اِنْتَهَيْتُ | saya sudah selesai | respons santri |
| هَلْ أَبْدَأُ؟ | apakah saya mulai? | inisiatif santri |
| مَا الْآيَةُ؟ | ayat berapa/apa ayatnya? | Qur'an |
| أَيُّ سُورَةٍ؟ | surah apa? | Qur'an |
| مَعَ مَنْ؟ | dengan siapa? | interaksi |

## KPI setelah normalisasi penuh

- `unique_lemma_count`
- `unique_surface_form_count`
- `unique_phrase_count`
- `unique_sentence_count`
- `first_introduction_by_page`
- `valuable_reuse_count`
- `redundant_duplication_count`
- `redundant_duplication_rate`
- `new_lemma_ratio`
- `review_ratio`

## Gate berikutnya

1. Tokenisasi seluruh 60 paragraf P001–P012 dari sumber yang tersedia.
2. Buat daftar surface form Arab unik.
3. Normalisasi ke lemma secara hati-hati; jangan melakukan stemming mekanis yang merusak Bahasa Arab.
4. Rekam first introduction setiap lemma/frasa.
5. Tandai pengulangan bernilai vs redundan.
6. Gunakan enrichment pool hanya pada bagian REVIEW/RECOVERED yang layak direvisi; jangan mengubah FROZEN tanpa prosedur revisi.
7. Setelah audit selesai, buat laporan lexical richness per halaman dan rekomendasi pengayaan P004–P012.
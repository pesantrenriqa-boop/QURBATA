# K01 — Mengenali Isim Dasar

**Kode:** REC-N-BASE  
**Layer:** A — Fondasi Pengenalan  
**Status materi:** CONTENT BANK COMPLETE (45 EVIDENCE) / QURAN EVIDENCE VERIFIED / EXPERT REVIEW PENDING  
**Prasyarat:** tidak ada  
**Standar:** COMPETENCY-AUTHORING-STANDARD-v1.1 + BEGINNER-PEDAGOGY-RULES-v1.0

## AHA K01
**Saya bisa mulai menemukan isim dalam Al-Qur'an, meskipun belum mengetahui arti seluruh ayat.**

## Capaian
Peserta mampu mengenali **isim** pada contoh Al-Qur'an sederhana tanpa dituntut mengetahui arti seluruh potongan ayat, menentukan i'rab, atau menjelaskan fungsi sintaksisnya.

# 1. LIHAT — لاحظ
Jangan mulai dengan definisi. Perlihatkan banyak contoh yang jelas. Bank K01 sekarang menyediakan **45 evidence Qurani terverifikasi**; buku memilih subset agar halaman tetap ringan.

Contoh awal:
**ٱللَّهُ — رَبِّ — يَوْمِ — ٱلنَّاسِ — مَلِكِ — شَرِّ — ٱلْفَلَقِ — أَحَدٌ — ٱلصَّمَدُ — نَصْرُ — ٱلْقَلَمِ — مَالُهُۥ**

Instruksi: **lihat, baca, dan perhatikan kata-katanya.** Arti boleh diberikan sebagai bantuan, tetapi tidak menjadi syarat untuk menemukan target.

# 2. TEMUKAN — اكتشف
Gunakan beberapa putaran dan variasi evidence.

Bandingkan isim dengan bentuk perbuatan yang jelas, lalu minta peserta mencari pola pada evidence Qurani lain. Bank TEMUKAN mencakup antara lain **ٱلْإِنسَـٰنَ، عَلَقٍ، ٱلْقَلَمِ، مَالُهُۥ، ٱلْعَصْرِ، خُسْرٍ، ٱلْحَقِّ، ٱلصَّبْرِ**.

Peserta tidak harus menerjemahkan seluruh ayat.

# 3. CIRI MUDAH
1. Isim sering berupa **nama atau sebutan**.
2. Isim dapat menunjuk **orang/makhluk atau sesuatu**.
3. Isim dapat menunjuk **waktu, tempat, keadaan, atau gagasan/konsep**.
4. Jadi, **isim tidak hanya berarti benda**.
5. Pada K01, ciri ini adalah alat bantu pengenalan. Tanda isim yang lebih khusus ditemukan bertahap pada K02 dan seterusnya.

> **Ingat:** belum tahu arti seluruh ayat bukan berarti belum bisa menemukan pola bahasanya.

# 4. PAHAMI — افهم
Nama konsepnya adalah **اَلِاسْمُ — isim**.

Penjelasan pemula: **isim adalah kata yang kita kenali sebagai nama, sebutan, orang/makhluk, benda, waktu, tempat, sifat, keadaan, atau suatu hal/konsep.**

Definisi nahwu akademik tetap tersedia untuk guru/backend dan tidak menjadi hafalan wajib K01.

### Belum perlu
Belum menentukan mubtada, khabar, fa'il, maf'ul, mudhaf, i'rab, ma'rifah–nakirah, atau idhafah.

# 5. COBA — طبّق
Bank COBA menggunakan evidence yang lebih beragam, antara lain dari Al-Fil dan Quraysh: **أَصْحَـٰبِ، ٱلْفِيلِ، كَيْدَهُمْ، طَيْرًا، حِجَارَةٍ، سِجِّيلٍ، قُرَيْشٍ، رِحْلَةَ، ٱلشِّتَآءِ، ٱلصَّيْفِ، ٱلْبَيْتِ**.

Latihan dibuat pendek: pilih, tandai, cari, kelompokkan secara sederhana, lalu recycle evidence lama. Bank 30 assessment beserta jawaban/pembahasan tetap berada di `assessment.json` dan dapat diperluas saat produksi latihan buku/RIQA OS.

# 6. BUKTIKAN — أثبت
Evidence BUKTIKAN disimpan sebagai unseen set dan tidak dipakai pada paparan utama. Set K01 saat ini mencakup:
**جُوعٍ — خَوْفٍ — ٱلتَّكَاثُرُ — ٱلْمَقَابِرَ — ٱلْيَقِينِ — ٱلْجَحِيمَ — ٱلْقَارِعَةُ**.

Peserta membuktikan kemampuan dengan menemukan isim pada evidence baru tanpa bantuan arti penuh. Reserve tambahan tersedia untuk variasi ujian/remedial.

# Bank Materi Backend
`quran-examples.json` sekarang menyimpan **45 evidence Qurani terverifikasi** dengan distribusi pedagogis: **14 LIHAT, 10 TEMUKAN, 11 COBA, 7 BUKTIKAN, 3 RESERVE**. Vocabulary berada di `vocabulary.json`; assessment di `assessment.json`; strategi guru dan QA di `teacher-notes.md`.

## Miskonsepsi yang dicegah
- isim = hanya benda konkret;
- harus mengetahui terjemah seluruh ayat sebelum dapat mengenali struktur;
- hafal definisi = sudah kompeten;
- harus langsung menentukan i'rab setelah menemukan isim.

## Jalur Bi'ah
K01 menjadi rujukan `first_allowed_competency` untuk item Bi'ah yang target produksinya sesuai kemampuan K01. Corpus Bi'ah tetap terpisah dari evidence Qurani.

## Production Gate K01
- [x] capaian dan boundary ditetapkan
- [x] COMPETENCY-AUTHORING-STANDARD-v1.1 diterapkan
- [x] BEGINNER-PEDAGOGY-RULES-v1.0 diterapkan
- [x] LIHAT → TEMUKAN → CIRI MUDAH → PAHAMI → COBA → BUKTIKAN diterapkan
- [x] **45 evidence Qurani tersedia (target v1.1 K01–K10 = 40–50)**
- [x] diversity evidence lintas surah/kosakata/konteks
- [x] unseen BUKTIKAN dipisahkan dari paparan
- [x] bank mufradat tersedia
- [x] seluruh 45 evidence Qurani berstatus verified
- [x] `quran-examples.json` canonical K01
- [x] `vocabulary.json` tersedia
- [x] 30 item latihan/soal tersedia
- [x] answer key + pembahasan tersedia di `assessment.json`
- [x] `teacher-notes.md` tersedia
- [ ] review ahli Bahasa Arab/nahwu
- [ ] review ahli pembelajaran Bahasa Arab
- [ ] validasi mastery threshold melalui pilot
- [ ] K01 FROZEN v1.0

### Aturan status
K01 sudah memenuhi **content/evidence gate v1.1**. Perubahan berikutnya hanya untuk koreksi QA/review ahli, pengayaan yang tidak merusak unseen set, atau hasil pilot.
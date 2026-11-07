# Draft-Freeze Proposal K1–K10 v0.1

**Status:** DRAFT-FREEZE PROPOSAL — RESEARCH LAYER ONLY  
**Authority:** NON-AUTHORITATIVE; belum mengubah `REG-ARB-001` atau stage resmi.  
**Basis:** dependency audit, frontier comparison, clean-yield test, verbal-track test, topological ordering, dan counterexample test.

## 1. Aturan Freeze

Sebuah kandidat hanya dapat dipromosikan dari `CANDIDATE` menjadi `DRAFT-FROZEN` bila:

1. targetnya atomik dan dapat diuji;
2. dependency-nya seluruhnya berada pada K sebelumnya;
3. tersedia unit Qurani yang dapat dipakai tanpa memerlukan K sesudahnya;
4. tidak ada counterexample struktural yang memaksa dependency terbalik;
5. bentuk recognition dipisahkan dari relation/generalization bila diperlukan;
6. evidence bank dapat diperluas tanpa batas tetap; sasaran teaching set 20–30+ hanyalah turunan, bukan batas corpus;
7. belum ada perubahan registry resmi sebelum review/freeze formal.

## 2. Proposed K1–K10

### K1 — REC-N-BASE — Mengenali isim sederhana

**Tipe:** REC  
**Target:** peserta dapat mengenali token nominal Qurani yang sederhana tanpa harus menganalisis fungsi sintaksisnya.

**Allowed:** K1 saja.  
**Belum termasuk:** mubtada', khabar, fa'il, maf'ul, idhafah, na'at, teori i'rab.

**Status proposal:** STRONG.

---

### K2 — REC-AL — Mengenali `الـ` pada isim

**Tipe:** REC  
**Dependency:** K1.

**Target:** mengenali artikel `الـ` sebagai fitur nominal pada contoh Qurani.

**Belum termasuk:** seluruh teori ma'rifah; isim isyarah, dhamir, maushul, dan idhafah tidak disatukan ke K2.

**Status proposal:** STRONG.

---

### K3 — REC-NAK-TAN — Mengenali nakirah/tanwin nominal sederhana

**Tipe:** REC  
**Dependency:** K1.

**Target:** mengenali bentuk nominal sederhana yang tidak memakai `الـ` dan bentuk bertanwin yang relevan.

**Catatan:** K2 dan K3 adalah dua cabang fitur nominal. Linearization K2→K3 dipakai untuk pembelajaran, bukan klaim bahwa K3 secara linguistik bergantung penuh pada K2.

**Status proposal:** STRONG WITH PARALLEL-DEPENDENCY NOTE.

---

### K4 — REC-PREP — Mengenali huruf jar frekuen

**Tipe:** REC  
**Dependency:** minimal; penggunaan relasional tetap menunggu K10.

**Target awal:** mengenali partikel seperti `مِنْ`, `فِي`, `عَلَى`, `إِلَى`, `بِـ`, `لِـ` sebagai unit, dengan clitic segmentation dijaga.

**Belum termasuk:** memahami keseluruhan jar–majrur atau teori majrur.

**Status proposal:** STRONG.

---

### K5 — REC-PRON-SEP — Mengenali dhamir munfashil dasar

**Tipe:** REC  
**Dependency:** tidak memerlukan jumlah ismiyyah sebagai recognition.

**Target:** mengenali bentuk seperti `هُوَ`, `هِيَ`, `أَنْتَ`, `أَنْتُمْ` sebagai pronomina terpisah.

**Belum termasuk:** penggunaannya sebagai mubtada', rujukan dhamir kompleks, atau paradigma penuh sebagai teori.

**Status proposal:** MODERATE-STRONG; posisi masih dapat bergerak tanpa merusak dependency inti.

---

### K6 — REC-V-PERF — Mengenali fi'il madhi sederhana

**Tipe:** REC  
**Dependency:** recognition dasar token; tidak mensyaratkan fa'il sebagai analisis.

**Target:** mengenali bentuk fi'il madhi Qurani sederhana, terutama bentuk yang tidak membawa suffix pronominal kompleks.

**Belum termasuk:** fa'il, maf'ul, tashrif lengkap, bina' majhul, atau derivational form system.

**Status proposal:** STRONG.

---

### K7 — REC-V-IMPF — Mengenali fi'il mudhari' sederhana

**Tipe:** REC  
**Dependency:** pengenalan verbal dasar; dipisahkan dari madhi karena surface cues dan ekspansi sintaksisnya berbeda.

**Belum termasuk:** raf'/nasb/jazm mudhari', af'al khamsah, suffix kompleks, atau governing particles.

**Status proposal:** STRONG.

---

### K8 — REL-NOM-PRED — Jumlah ismiyyah core: mubtada' + khabar isim zhahir sederhana

**Tipe:** REL  
**Dependency:** K1–K3. K5 tidak wajib bila contoh memakai isim zhahir.

**Anchor evidence:**

> اللَّهُ الصَّمَدُ — QS 112:2

Analisis target:

- `اللَّهُ` = mubtada';
- `الصَّمَدُ` = khabar;
- tidak memerlukan fi'il;
- tidak memerlukan dhamir;
- tidak memerlukan jar–majrur, idhafah, na'at, `inna`, atau `kana`.

**Status proposal:** VERY STRONG.

---

### K9 — REL-VS — Fi'il + fa'il isim zhahir sederhana

**Tipe:** REL  
**Dependency:** K1 + K6/K7 sesuai tense contoh.

**Target:** memahami relasi predikasi verbal minimum dengan fa'il isim zhahir.

**Filter wajib:** tahan contoh dengan fa'il dhamir tersembunyi bila itu menuntut analisis tambahan; tahan suffix objek, dua objek, passive, coordination, dan subordinate clause sampai kompetensinya tersedia.

**Status proposal:** STRONG, tetapi evidence bank clean perlu diperbesar.

---

### K10 — REL-PP — Huruf jar + isim zhahir sebagai jar–majrur

**Tipe:** REL  
**Dependency:** K1 + K4; fitur nominal K2/K3 boleh muncul bila sudah dikuasai.

**Target:** memahami relasi lokal `حرف جر + اسم ظاهر` sebagai satu unit jar–majrur.

**Filter wajib:** contoh preposisi + dhamir muttashil belum masuk; clitic tambahan yang belum dipelajari membuat kandidat PREMATURE.

**Status proposal:** VERY STRONG.

## 3. Matriks Dependency

| K | Target | Type | Hard prerequisite | Soft/parallel prerequisite |
|---|---|---|---|---|
| K1 | isim | REC | — | — |
| K2 | `الـ` | REC | K1 | — |
| K3 | nakirah/tanwin | REC | K1 | K2 sebagai kontras |
| K4 | huruf jar | REC | —/K1 untuk contoh relasional | — |
| K5 | dhamir munfashil | REC | — | K1 sebagai pembanding nominal |
| K6 | fi'il madhi | REC | — | — |
| K7 | fi'il mudhari' | REC | — | K6 sebagai kontras verbal |
| K8 | mubtada' + khabar zhahir | REL | K1,K2/K3 sesuai contoh | K5 untuk ekspansi nanti |
| K9 | fi'il + fa'il zhahir | REL | K1,K6/K7 | — |
| K10 | jar–majrur zhahir | REL | K1,K4 | K2/K3 sesuai isim |

## 4. Hasil Gate Review

### Layak DRAFT-FROZEN secara struktural

- K1
- K2
- K3
- K4
- K6
- K7
- K8
- K10

### DRAFT-FROZEN dengan flag evidence expansion

- K5 — posisi linear dapat berubah walau kompetensinya sendiri valid;
- K9 — dependency valid, tetapi perlu bank clean examples lebih besar untuk memastikan kebijakan fa'il zhahir tidak terlalu sempit.

## 5. Prinsip Evidence Bank per K

Setiap K akan memiliki **seluruh kandidat valid yang ditemukan**, bukan hanya lima contoh.

Target operasional awal:

- `Corpus candidates`: unlimited;
- `PASS`: semua yang lolos cumulative filter;
- `Core teaching`: dipilih kemudian, umumnya 20–30+ bila tersedia;
- `Reinforcement`: sisa PASS yang relevan;
- `PREMATURE`: tetap disimpan sebagai bukti mengapa contoh ditunda ke K berikutnya.

## 6. Aturan Contoh Kumulatif

Untuk K8, misalnya:

`ALLOWED = K1..K8`

Tetapi contoh terbaik diprioritaskan yang dependency aktualnya minimum, misalnya hanya K1–K3 + K8.

Sebuah unit yang mengandung idhafah, na'at, dhamir muttashil, `inna`, `kana`, jar–majrur sebagai khabar, atau struktur lain yang belum ditempatkan tetap `PREMATURE`, walaupun di dalamnya terdapat mubtada'–khabar.

## 7. Jangan Salah Memaknai Nomor K

Nomor K adalah **urutan pembelajaran linear yang dipilih dari dependency graph**, bukan klaim bahwa semua K sebelumnya adalah hard prerequisite linguistik langsung.

Karena itu metadata harus menyimpan dua hal sekaligus:

- `sequence_order`;
- `hard_dependencies[]`.

Ini penting agar RIQA OS dan mesin kurikulum kelak dapat melakukan akselerasi/placement tanpa merusak prerequisite.

## 8. Status Integrasi

Belum ada perubahan pada:

- `REG-ARB-001`;
- stage resmi `AR-STG-*`;
- master jilid;
- halaman produksi;
- assessment produksi.

Research layer hanya menyiapkan hasil yang nantinya dapat dipetakan secara aman setelah freeze formal.

## 9. Next Batch

Sebelum freeze formal K1–K10:

1. bangun `EVIDENCE-BANK-K01-K10-v0.1`;
2. isi bukti Qurani awal per K dan status PASS/PREMATURE;
3. prioritaskan perluasan K8, K9, K10 karena merupakan kompetensi relasional pertama;
4. audit ulang K5 apakah posisinya optimal;
5. baru terbitkan `DRAFT-FROZEN-K01-K10` bila evidence gate terpenuhi.

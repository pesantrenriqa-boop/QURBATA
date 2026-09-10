# Frontier Comparison v0.1 — Na'at vs Idhafah vs Jar–Majrur vs Dhamir Munfashil

**Status:** WORKING RESEARCH — NON-AUTHORITATIVE  
**Tujuan:** membandingkan empat kandidat kompetensi setelah jumlah ismiyyah dasar berdasarkan dependency minimum, kompleksitas struktural, dan potensi clean examples Qurani.

## 1. Prinsip

Kandidat yang layak naik lebih awal harus:

1. memiliki dependency lebih sedikit;
2. dapat diekspresikan dalam unit Qurani pendek dan utuh;
3. tidak memerlukan kompetensi yang belum ditempatkan;
4. membuka banyak struktur berikutnya;
5. memiliki representasi yang jelas dalam anotasi Quranic Arabic Corpus.

## 2. Na'at–Man'ut

### Struktur inti

`isim + sifat`

Quranic Arabic Corpus menempatkan adjective sebagai nominal yang mengikuti dan bergantung pada noun yang diterangkan.

### Dependency minimum

- isim;
- kemampuan mengenali adjective sebagai nominal descriptor;
- agreement dasar antara man'ut dan na'at.

### Risiko prematur

Agreement dapat melibatkan definiteness, gender, number, dan case. Jika seluruh agreement diajarkan sekaligus, kompetensi menjadi terlalu berat.

### Kesimpulan sementara

`VIABLE-EARLY`, tetapi harus dibatasi pada **na'at–man'ut sederhana** dengan agreement yang tampak dan tanpa ekspansi lain.

## 3. Idhafah

### Struktur inti

`mudhaf + mudhaf ilaih`

Corpus mendefinisikan possessive construction sebagai iḍāfa dan mengaitkannya dengan genitive case.

### Dependency minimum

- isim;
- dua unsur nominal;
- relasi kepemilikan/penyandaran;
- pengenalan bahwa unsur kedua berada dalam fungsi genitive.

### Risiko prematur

Jika i'rab majrur harus diajarkan penuh sebelum idhafah, dependency menjadi lebih berat. Namun secara pedagogis relasi dua isim dapat dikenalkan lebih dahulu secara struktur, lalu i'rab diperdalam kemudian.

### Kesimpulan sementara

`VIABLE-EARLY`, sangat produktif dan penting, tetapi secara formal sedikit lebih berat dari na'at jika agreement na'at dibatasi sederhana.

## 4. Jar–Majrur

### Struktur inti

`huruf jar + nominal majrur`

Dokumentasi Quranic Arabic Corpus menyatakan preposition datang sebelum noun/nominal dan menempatkannya dalam genitive; keduanya membentuk dependency jar–majrur.

### Dependency minimum

- isim/nominal;
- satu huruf jar tertentu;
- relasi preposition → nominal;
- fungsi majrur minimal.

### Kelebihan

Strukturnya sangat eksplisit dan mudah disegmentasi. Banyak preposition muncul sebagai token atau prefix yang jelas.

### Risiko prematur

Jar–majrur selalu ber-attachment pada unsur lain dalam kalimat secara analisis penuh. Namun untuk kompetensi awal, unit lokal `preposition + nominal` dapat diajarkan tanpa terlebih dahulu menuntut analisis attachment tingkat kalimat.

### Kesimpulan sementara

`VERY-STRONG-EARLY`. Dibanding idhafah, dependency lokal lebih transparan. Kandidat kuat untuk muncul segera setelah struktur nominal dasar.

## 5. Dhamir Munfashil

### Struktur inti

personal pronoun bebas seperti `هو`, `هم`, `أنت`, `أنتم`.

### Dependency minimum

- konsep nominal/pronominal;
- persona/number/gender dasar.

### Kelebihan

Unit satu token; tidak membutuhkan relasi sintaksis untuk tahap pengenalan.

### Risiko prematur

Begitu dipakai dalam jumlah ismiyyah, siswa membutuhkan fungsi mubtada' atau fungsi lain. Tetapi **pengenalan dhamir sebagai kategori** sendiri sangat ringan.

### Kesimpulan sementara

`VERY-STRONG-EARLY-AS-IDENTIFICATION`, tetapi harus dibedakan antara:

- mengenali dhamir munfashil;
- memakai dhamir sebagai mubtada'/unsur struktur.

## 6. Perbandingan Dependency

| Kandidat | Dependency lokal | Kompleksitas awal | Membuka struktur lanjut | Status |
|---|---:|---:|---:|---|
| Dhamir munfashil — identifikasi | sangat rendah | sangat rendah | tinggi | VERY-STRONG |
| Jar + isim zhahir | rendah | rendah | sangat tinggi | VERY-STRONG |
| Na'at–man'ut sederhana | rendah–sedang | rendah–sedang | tinggi | STRONG |
| Idhafah dua isim | rendah–sedang | sedang | sangat tinggi | STRONG |

## 7. Temuan Utama

Empat kandidat ini ternyata tidak berada pada satu jenis kompetensi yang sama.

- `dhamir munfashil` pada tahap awal adalah **identifikasi kategori**;
- `jar + isim`, `na'at–man'ut`, dan `idhafah` adalah **relasi dua unsur**.

Karena itu linearization yang adil sebaiknya memisahkan:

### Layer identifikasi

`isim → fitur nominal dasar → dhamir munfashil`

### Layer relasi

`jumlah ismiyyah sederhana / jar–majrur / na'at / idhafah`

Urutan di dalam layer relasi harus ditentukan oleh clean-example yield.

## 8. Hipotesis Linearization Revisi — BELUM FREEZE

Kandidat urutan untuk diuji selanjutnya:

1. isim sederhana;
2. `الـ` ta'rif / nakirah sebagai fitur nominal dasar;
3. dhamir munfashil — identifikasi;
4. jumlah ismiyyah mubtada' + khabar isim sederhana;
5. jar + isim zhahir sederhana;
6. jar–majrur sebagai unit;
7. na'at–man'ut sederhana;
8. idhafah dua isim sederhana;
9. penggunaan dhamir sebagai mubtada';
10. dhamir muttashil dasar.

Urutan 5–8 masih harus diuji corpus; tidak dianggap final.

## 9. Implikasi Corpus Bank

Untuk setiap kandidat selanjutnya harus dihitung:

- jumlah `PURE`;
- jumlah `MINIMAL-EXTRACTABLE`;
- jumlah `PREMATURE`;
- penyebab prematur dominan;
- dependency paling sering hadir bersama target.

Kandidat dengan clean-example yield tinggi dan dependency rendah lebih layak ditempatkan lebih awal.

## 10. Sumber Linguistik

- Quranic Arabic Corpus — grammar overview: nominals, adjectives, possessives, phrases and clauses;
- Quranic Arabic Corpus — preposition phrase documentation: huruf jar + nominal majrur = jar–majrur;
- Quranic Arabic Corpus — morphology pages menunjukkan preposition dapat berprefiks pada noun atau bergabung dengan pronoun.

## 11. Keputusan Batch Berikutnya

Batch selanjutnya harus membangun **evidence bank pembanding untuk jar–majrur, na'at–man'ut, dan idhafah**. Masing-masing minimal dikumpulkan puluhan kandidat sebelum urutan 5–8 diputuskan. Dhamir munfashil diuji terpisah sebagai kompetensi identifikasi satu-token dan sebagai unsur jumlah.

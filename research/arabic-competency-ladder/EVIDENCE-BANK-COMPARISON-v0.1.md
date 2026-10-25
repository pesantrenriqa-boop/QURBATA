# Evidence Bank Comparison v0.1

**Status:** WORKING RESEARCH — NON-AUTHORITATIVE  
**Scope:** membandingkan kandidat relasi awal: `jar–majrur`, `na‘at–man‘ut`, dan `idhafah` untuk menentukan urutan kompetensi paling bertahap.

## 1. Prinsip

Kandidat yang lebih awal harus:

1. mempunyai dependency minimum;
2. dapat diekstrak sebagai unit Qurani utuh;
3. mempunyai banyak clean examples;
4. tidak menuntut agreement/derivasi/struktur tambahan yang belum dipelajari;
5. membuka jalan bagi kompetensi berikutnya.

## 2. Jar–Majrur

### Dependency minimum

- isim/nominal sudah dikenali;
- satu huruf jar tertentu dikenali;
- konsep bahwa nominal sesudah huruf jar berada dalam relasi majrur.

### Kekuatan pedagogis

Relasi sangat lokal dan eksplisit. Quranic Arabic Corpus mendefinisikan huruf jar sebagai unsur yang mendahului nominal dan menempatkannya dalam kasus genitif; preposisi dan nominal itu membentuk satu preposition phrase / jar–majrur.

### Evidence terverifikasi awal

| Ref | Unit | Status awal | Catatan |
|---|---|---|---|
| 23:89 | `لِلَّهِ` | PURE-CANDIDATE | preposisi `لـ` + proper noun Allah; corpus menandai jar–majrur |
| 4:146 | `لِلَّهِ` | PURE-CANDIDATE | struktur identik; clean secara internal |
| 4:144 | `لِلَّهِ` | PURE-CANDIDATE | struktur identik; clean secara internal |
| 4:171 | `بِاللَّهِ` | PURE-CANDIDATE | `بـ` + Allah; corpus menandai jar–majrur |
| 13:43 | `بِاللَّهِ` | PURE-CANDIDATE | `بـ` + Allah; clean secara internal |
| 1:1 | `بِاسْمِ` | REVIEW | jar–majrur murni secara morfologi, tetapi `اسم` menjadi kepala idhafah dalam konteks berikutnya sehingga untuk clean-example awal perlu aturan segmentasi |
| 53:31 | `وَلِلَّهِ` | PREMATURE-IF-WA-NOT-YET | membawa `و` prefiks sebelum huruf jar |
| 7:180 | `وَلِلَّهِ` | PREMATURE-IF-WA-NOT-YET | membawa unsur penghubung/resumption |
| 4:171 | `لَكُمْ` | PREMATURE | objek preposisi berupa dhamir; membutuhkan dhamir terlebih dahulu |
| 7:158 | `إِلَيْكُمْ` | PREMATURE | objek preposisi berupa dhamir |
| 3:101 | `وَفِيكُمْ` | PREMATURE | conjunction + preposition + pronoun |
| 24:45 | `وَمِنْهُمْ` | PREMATURE | conjunction + preposition + pronoun |

### Implikasi

`جار ومجرور` mempunyai kelas contoh awal yang sangat sederhana ketika objek preposisinya isim zhahir/proper noun dan tidak ada prefiks koordinatif tambahan.

## 3. Na‘at–Man‘ut

### Dependency minimum

- dua nominal/adjectival units;
- konsep noun vs adjective;
- agreement gender;
- agreement number;
- agreement definiteness;
- agreement case.

Quranic Arabic Corpus menyatakan adjective mengikuti nominal yang diterangkan dan menyepakatinya dalam gender, number, definiteness, dan grammatical case.

### Evidence terverifikasi awal

| Ref | Unit | Status awal | Catatan |
|---|---|---|---|
| 1:3 | `الرَّحْمَنِ الرَّحِيمِ` | REVIEW-CANDIDATE | corpus menunjukkan dua adjectives; secara pedagogis contoh bagus untuk adjective sequence, tetapi relasi terhadap head sebelumnya perlu dijaga agar tidak membuat unit palsu |
| 34:37 | adjective `الضِّعْفِ` | REVIEW | corpus menandai adjective tetapi catatan corpus sendiri menunjukkan analisis dapat diperdebatkan; tidak dipakai sebagai anchor awal |

### Implikasi

Na‘at membutuhkan agreement multidimensi. Karena itu walaupun bentuk dua-katanya sederhana, **dependency konseptualnya lebih berat daripada jar–majrur**.

## 4. Idhafah

### Dependency minimum

- dua isim/nominal;
- mudhaf + mudhaf ilaih;
- mudhaf ilaih majrur;
- mudhaf tidak menerima `الـ` dan tanwin dalam konstruksi standar;
- definiteness konstruksi mengikuti mudhaf ilaih secara operasional.

Quranic Arabic Corpus mendefinisikan idhafah sebagai relasi dua nouns dengan noun kedua sebagai dependent dalam kasus genitif. Corpus juga menetapkan tiga batas utama: head tidak memakai definite article, head tidak memakai tanwin, dependent berada dalam genitive case.

### Evidence terverifikasi awal

| Ref | Unit | Status awal | Catatan |
|---|---|---|---|
| 88:1 | `حَدِيثُ الْغَاشِيَةِ` | CANDIDATE | contoh eksplisit dokumentasi corpus untuk possessive construction; tetapi keseluruhan ayat mengandung verba/istifham sehingga unit harus diekstrak sebagai frasa |
| 1:1 | `اسْمِ اللَّهِ` | CANDIDATE | secara Qurani sangat familiar; konteks `باسم` juga membawa jar pada mudhaf sehingga bila target idhafah murni perlu memastikan P-jar sudah dipelajari atau unit extraction dinyatakan sah |

### Implikasi

Idhafah lebih berat daripada jar–majrur karena bukan hanya relation-to-genitive, tetapi juga aturan bentuk kepala konstruksi. Namun setelah jar/majrur dikuasai, idhafah menjadi lebih mudah karena konsep `majrur` pada dependent sudah tersedia.

## 5. Perbandingan Dependency

| Kandidat | Dependency inti | Beban tambahan | Posisi relatif sementara |
|---|---|---|---|
| Jar–majrur | huruf jar + nominal | majrur | PALING RINGAN |
| Na‘at–man‘ut | noun + adjective | agreement gender/number/definiteness/case | LEBIH BERAT |
| Idhafah | noun + noun | majrur + constraints pada mudhaf | MENENGAH |

## 6. Hipotesis Urutan Baru

Berdasarkan dependency, kandidat linearization awal sekarang lebih kuat ke arah:

```text
isim
↓
fitur nominal dasar
↓
[dhamir munfashil — masih diuji posisinya]
↓
jumlah ismiyyah core
↓
huruf jar dasar
↓
jar–majrur dengan isim zhahir
↓
idhafah sederhana
↓
na‘at–man‘ut sederhana
```

Alasan menempatkan idhafah sebelum na‘at sementara: setelah konsep majrur sudah tersedia dari jar–majrur, dependency utama idhafah tinggal relasi dua isim + aturan kepala konstruksi. Na‘at masih menuntut agreement lebih banyak dimensi.

**Status:** HIPOTESIS, BELUM FREEZE.

## 7. Temuan Penting untuk Mesin Filter

Prematurity tidak cukup diperiksa per kata. Mesin harus memeriksa **segmen morfologis** di dalam satu orthographic word. Contoh:

- `ولله` bukan hanya jar–majrur; ada `و` juga;
- `لكم` bukan hanya jar–majrur; objeknya dhamir;
- `وفيكم` membawa conjunction + preposition + pronoun;
- `باسم` secara internal jar–majrur, tetapi token itu juga menjadi kepala idhafah pada konteks `بسم الله`.

Dengan demikian satu candidate example harus memiliki `segment-level competency signature`.

## 8. Keputusan Batch

1. `jar–majrur dengan isim zhahir` dipromosikan menjadi **FRONTIER-STRONG** untuk posisi setelah jumlah ismiyyah core;
2. `idhafah sederhana` menjadi kandidat berikutnya yang kuat;
3. `na‘at–man‘ut` ditahan satu tingkat lebih akhir sampai agreement dasar dimodelkan;
4. dhamir munfashil masih harus dibandingkan: apakah lebih baik sebelum jumlah ismiyyah core atau sebagai ekspansi sesudahnya;
5. batch berikutnya harus menguji urutan ini dengan `clean-example yield`, bukan hanya dependency teoritis.

# Verbal Track Bahasa Arab Qurani v0.1

**Status:** WORKING RESEARCH — NON-AUTHORITATIVE  
**Tujuan:** menguji posisi fi'il dan jumlah fi'liyyah terhadap kandidat tangga nominal awal.

## 1. Prinsip

Jalur verbal tidak boleh menunggu seluruh struktur nominal selesai. Namun setiap kompetensi verbal harus tetap tunduk pada cumulative rule:

`contoh Kn hanya boleh mengandung kompetensi K1..Kn`.

Karena itu pengenalan fi'il dipisahkan dari penggunaan fi'il dalam relasi sintaksis.

## 2. Kandidat Atomik Verbal

### V1 — mengenali fi'il sebagai kategori kata

Tipe: `REC`

Target:
- membedakan token verbal dari isim dan partikel;
- belum membedakan madhi/mudhari'/amr secara penuh;
- belum menuntut fa'il, maf'ul, atau i'rab fi'il.

Dependency minimum:
- tidak ada dependency sintaksis wajib;
- secara pedagogis dapat berjalan segera setelah atau sejajar dengan recognition isim.

### V2 — mengenali fi'il madhi sederhana

Tipe: `REC`

Target:
- mengenali pola fi'il madhi yang tidak membawa suffix persona kompleks;
- belum menganalisis fa'il tersembunyi/terenkode secara rinci.

Dependency:
- V1.

### V3 — mengenali fi'il mudhari' sederhana

Tipe: `REC`

Target:
- mengenali bentuk mudhari' sederhana melalui prefiks verbal dan pola dasar;
- belum masuk raf'/nasb/jazm.

Dependency:
- V1.

### V4 — fi'il + fa'il isim zhahir

Tipe: `REL`

Target minimum:

`فعل + اسم ظاهر`

Dependency:
- V1/V2 atau V3 sesuai tense;
- recognition isim;
- konsep bahwa isim setelah verba dapat berfungsi sebagai fa'il.

### V5 — fi'il + fa'il dhamir terenkode

Tipe: `REL`

Target:
- mengenali bahwa pelaku dapat termuat dalam bentuk fi'il;
- contoh: suffix/prefix persona yang membawa informasi fa'il.

Dependency:
- V2/V3;
- paradigm persona minimum;
- lebih berat daripada V4.

### V6 — fi'il + fa'il + maf'ul bih isim zhahir

Tipe: `REL`

Dependency:
- V4;
- recognition isim;
- distinction pelaku vs objek;
- belum memerlukan maf'ul berupa dhamir.

### V7 — maf'ul bih berupa dhamir muttashil

Tipe: `REL`

Dependency:
- V6;
- dhamir muttashil recognition;
- segmentasi morfologis suffix.

## 3. Perbandingan dengan Nominal Track

Nominal candidate track yang sedang diuji:

`C1 isim → C2 al-ta'rif → C3 nakirah/tanwin → C4 dhamir munfashil-rec → C5 jumlah ismiyyah core → C6 huruf jar-rec → C7 jar–majrur → C9 idhafah → C10 na'at`

Verbal track menunjukkan bahwa `V1 mengenali fi'il` secara dependency lebih ringan daripada sebagian besar C2–C10. Maka tidak logis menempatkan pengenalan fi'il setelah seluruh ekspansi nominal selesai.

## 4. Hipotesis Dua Jalur Paralel

```text
TOKEN RECOGNITION
├── N1 ISIM
│   ├── N2 AL-TA'RIF
│   ├── N3 NAKIRAH/TANWIN
│   ├── N4 DHAMIR MUNFASHIL-REC
│   └── N5 JUMLAH ISMIYYAH CORE
│
└── V1 FI'IL
    ├── V2 MADHI-REC
    ├── V3 MUDHARI'-REC
    └── V4 FI'IL + FA'IL ZHAHIR

N1 + V4
   ↓
V6 FI'IL + FA'IL + MAF'UL ZHAHIR
```

Dengan model ini, jalur nominal dan verbal berkembang paralel lalu mulai terintegrasi pada penggunaan isim sebagai fa'il/maf'ul.

## 5. Implikasi terhadap K Linear

Tangga final tetap harus linear `K1 → Kn`, tetapi dependency graph boleh bercabang. Linearization harus memilih urutan yang:

1. tidak melanggar dependency;
2. memaksimalkan clean-example yield;
3. menjaga kompleksitas bertahap;
4. membuka sebanyak mungkin struktur Qurani berikutnya.

Artinya kita tidak mencari satu jalur linguistik lurus dari isim sampai selesai, tetapi melakukan **topological ordering** terhadap dependency graph.

## 6. Kandidat Linearization Gabungan v0.1 — BELUM FREEZE

Urutan uji berikut lebih masuk akal daripada nominal-only:

1. `L1` — recognition isim sederhana;
2. `L2` — recognition fi'il sederhana;
3. `L3` — recognition `الـ` pada isim;
4. `L4` — recognition nakirah/tanwin;
5. `L5` — recognition fi'il madhi sederhana;
6. `L6` — recognition fi'il mudhari' sederhana;
7. `L7` — jumlah ismiyyah core: mubtada' + khabar isim zhahir;
8. `L8` — fi'il + fa'il isim zhahir;
9. `L9` — recognition huruf jar frekuen;
10. `L10` — jar–majrur dengan isim zhahir;
11. `L11` — dhamir munfashil recognition;
12. `L12` — mubtada' dhamir + khabar sederhana;
13. `L13` — fi'il + fa'il + maf'ul bih isim zhahir;
14. `L14` — idhafah dua isim sederhana;
15. `L15` — na'at–man'ut sederhana.

Urutan ini masih eksperimental. Posisi dhamir dan fi'il madhi/mudhari' harus diuji berdasarkan clean-example availability.

## 7. Temuan Pedagogis Sementara

### 7.1 Recognition harus datang sebelum construction

Contoh:
- siswa mengenali `خَلَقَ` sebagai fi'il madhi sebelum menganalisis `خَلَقَ اللَّهُ`;
- siswa mengenali `هُوَ` sebagai dhamir sebelum memakai `هُوَ` sebagai mubtada'.

### 7.2 Fa'il zhahir lebih sederhana daripada fa'il terenkode

Untuk clean examples awal, prioritaskan verba yang diikuti fa'il isim zhahir. Bentuk dengan suffix persona, wawu jama'ah, alif itsnain, nun niswah, atau fa'il mustatir ditahan sampai kompetensi terkait tersedia.

### 7.3 Maf'ul zhahir sebelum maf'ul dhamir

`فعل + فاعل + مفعول ظاهر` harus diuji lebih awal daripada verba dengan object suffix karena suffix membawa beban morfologi tambahan.

## 8. Filter Prematur Verbal

Kandidat contoh verbal ditolak pada tahap awal jika memerlukan salah satu dari:

- dhamir suffix yang belum dipelajari;
- wawu jama'ah/alif itsnain/ya' mukhathabah/nun niswah;
- fi'il majhul;
- nawasib/jawazim mudhari';
- dua maf'ul;
- jumlah maushul/syarth/hal sebagai pelengkap;
- taqdim–ta'khir kompleks;
- ellipsis yang menuntut analisis lanjutan.

## 9. Keputusan Batch

- verbal track harus dimulai sangat awal;
- recognition fi'il berpotensi masuk dekat dengan recognition isim;
- jumlah fi'liyyah dasar tidak perlu menunggu idhafah/na'at selesai;
- jalur nominal dan verbal harus diperlakukan sebagai dependency graph yang kemudian dilinear-kan;
- belum ada `K` final yang difreeze;
- `REG-ARB-001` tetap tidak diubah.

## 10. Batch Berikutnya

1. bangun `TOPOLOGICAL-CANDIDATE-ORDER-v0.1` dari nominal + verbal track;
2. uji counterexample untuk L1–L15;
3. identifikasi partikel mana yang harus masuk sangat awal karena mengganggu clean-example yield (`و`, `ف`, `من`, `في`, `إلى`, `على`, `ب`, `ل`);
4. tentukan apakah partikel coordination seperti `و` perlu recognition lebih awal dari sebagian construction;
5. setelah itu baru promosi subset awal menjadi kandidat `K1–K10` yang lebih stabil.

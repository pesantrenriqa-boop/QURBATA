# P4 Evidence Expansion v0.2

**Status:** WORKING RESEARCH — NON-AUTHORITATIVE  
**Scope:** memperluas uji `jumlah ismiyyah: mubtada' + khabar isim sederhana` dan mengidentifikasi kompetensi yang paling sering menjadi dependency tambahan.  
**Guardrail:** tidak mengubah `REG-ARB-001`, baseline, master jilid, atau artefak produksi.

## 1. Target P4

Target P4 tetap sempit:

> peserta memahami relasi predikatif `mubtada' + khabar` ketika kedua unsur berupa nominal sederhana dan unit tidak memerlukan struktur baru yang belum dipelajari.

Bukan target P4:

- dhamir sebagai mubtada';
- khabar jar–majrur;
- khabar jumlah;
- na'at ekspansif;
- idhafah kompleks;
- `inna/kana`;
- koordinasi kompleks;
- jumlah bersarang.

## 2. Anchor Terverifikasi

### E-P4-001 — QS 112:2

`اللَّهُ الصَّمَدُ`

- target: mubtada' + khabar;
- corpus grammar: `الله الصمد` dianalisis sebagai `مبتدأ وخبر`;
- status: `PURE / PASS-ANCHOR`;
- dependency minimum: isim + fitur nominal dasar;
- catatan: menjadi anchor formal P4.

### E-P4-002 — QS 4:128

`الصُّلْحُ خَيْرٌ`

- ayat penuh memiliki struktur lain, tetapi grammar corpus menyatakan `والصلح خير` sebagai jumlah mu'taridhah;
- unit inti `الصلح خير` mempertahankan predikasi nominal;
- status: `MINIMAL-EXTRACTABLE / PASS`;
- dependency minimum: isim + definiteness/nakirah dasar.

## 3. Kandidat Ekspansi

### E-P4-003 — QS 64:6

Unit ayat: `وَاللَّهُ غَنِيٌّ حَمِيدٌ`

Kandidat minimal: `اللَّهُ غَنِيٌّ`

- target inti tampak sebagai mubtada' + khabar;
- `حميد` adalah unsur nominal tambahan pada klausa penuh;
- `و` berada di batas kiri unit;
- status: `REVIEW-MINIMAL-EXTRACTABLE`;
- konflik: standardisasi pemotongan predikat tambahan.

### E-P4-004 — QS 47:38

Unit ayat: `وَاللَّهُ الْغَنِيُّ`

Kandidat minimal: `اللَّهُ الْغَنِيُّ`

- bentuk permukaan dua nominal;
- status: `REVIEW` sampai dependency/i'rab spesifik diverifikasi;
- nilai pedagogis potensial tinggi karena sangat pendek.

### E-P4-005 — QS 35:15

Unit: `وَاللَّهُ هُوَ الْغَنِيُّ الْحَمِيدُ`

- mengandung predikasi nominal tetapi memakai `هو` dan ekspansi nominal;
- status: `PREMATURE-P4`;
- dependency blocker: dhamir munfashil / kemungkinan dhamir fashl + ekspansi predikat.

### E-P4-006 — QS 35:15

Unit: `أَنْتُمُ الْفُقَرَاءُ`

- mubtada' berupa dhamir munfashil;
- status: `PREMATURE-P4`;
- blocker utama: dhamir munfashil.

### E-P4-007 — QS 87:17

Unit: `الْآخِرَةُ خَيْرٌ وَأَبْقَى`

- inti predikatif nominal ada;
- status: `PREMATURE-P4`;
- blocker: koordinasi `و` dan predikat tambahan/tafdhil.

### E-P4-008 — QS 39:7

Unit relevan: `فَإِنَّ اللَّهَ غَنِيٌّ عَنْكُمْ`

- secara semantik memiliki predikasi Allah–Ghaniyy, tetapi struktur dikendalikan `إنّ` dan dilengkapi jar–majrur;
- status: `PREMATURE-P4`;
- blocker: `inna` + jar–majrur.

## 4. Temuan Blocker Awal

Dari sampel terverifikasi dan kandidat awal, blocker yang mulai muncul adalah:

| Blocker | Dampak terhadap P4 | Implikasi urutan |
|---|---|---|
| dhamir munfashil | mengubah bentuk mubtada' dari isim zhahir ke pronomina | kandidat kuat untuk kompetensi sesudah P4, bukan prasyarat wajib P4 murni |
| koordinasi `و` | menambah predikat/unsur setara | tidak perlu dipaksakan sebelum P4 karena anchor murni tersedia tanpa koordinasi |
| predikat nominal tambahan | memperluas jumlah ismiyyah dasar | cocok sebagai tahap ekspansi setelah P4 |
| `inna` | mengubah case/function struktur nominal | harus sesudah jumlah ismiyyah dasar |
| jar–majrur | membuka khabar/pelengkap preposisional | tidak wajib sebelum P4 murni, tetapi menjadi frontier dekat setelahnya |
| na'at/ekspansi nominal | menambah dependency agreement | perlu diuji apakah lebih baik sebelum atau sesudah P4 |

## 5. Kesimpulan Dependency P4 v0.2

Evidence yang ada **tidak memaksa** dhamir, `inna`, jar–majrur, atau koordinasi ditempatkan sebelum jumlah ismiyyah dasar. Justru keberadaan anchor `اللَّهُ الصَّمَدُ` dan unit `الصُّلْحُ خَيْرٌ` menunjukkan P4 dapat diajarkan dalam bentuk murni lebih dahulu.

Hipotesis kerja diperkuat:

```text
isim
 ├── al-ta'rif
 └── nakirah/tanwin
        ↓
jumlah ismiyyah murni: mubtada' + khabar isim
        ↓
[frontier ekspansi]
 ├── dhamir sebagai mubtada'
 ├── predikat nominal tambahan
 ├── jar–majrur / khabar شبه جملة
 ├── na'at–man'ut
 └── idhafah
```

Urutan di dalam frontier ekspansi belum ditetapkan.

## 6. Aturan Baru: P4 Core vs P4 Expansion

Untuk mencegah satu kompetensi menjadi terlalu luas:

- `P4-CORE`: mubtada' isim zhahir + khabar isim sederhana;
- `P4-EXP-PRON`: mubtada' berupa dhamir — **bukan P4 core**;
- `P4-EXP-PP`: khabar jar–majrur — **bukan P4 core**;
- `P4-EXP-CLAUSE`: khabar jumlah — **bukan P4 core**;
- `P4-EXP-MULTI`: lebih dari satu predikat/ekspansi — **bukan P4 core**.

Ekspansi tersebut akan menjadi kandidat K tersendiri atau penerapan setelah dependency terkait dikuasai.

## 7. Aturan Evidence Bank yang Diperketat

Sebuah contoh `PURE` harus:

1. contiguous;
2. target relation lengkap;
3. tidak menghapus unsur wajib target;
4. tidak memerlukan kompetensi yang belum ada;
5. tidak mengandalkan reinterpretasi setelah dipotong;
6. memiliki verifikasi i'rab/dependency;
7. mempertahankan teks Qurani persis.

`MINIMAL-EXTRACTABLE` harus memenuhi semua syarat di atas, tetapi berasal dari klausa/ayat yang lebih panjang dan pemotongannya harus dapat dibenarkan secara sintaksis.

## 8. Status Kandidat Awal

- P1 isim: `STRONG`
- P2 `الـ`: `STRONG`
- P3 nakirah/tanwin: `STRONG`
- P4 jumlah ismiyyah core: `STRONGER AFTER v0.2`

Belum difreeze menjadi K1–K4 karena P2/P3 masih mungkin sibling dan corpus bank belum exhaustif.

## 9. Frontier Berikutnya untuk Diuji

Batch berikutnya harus membandingkan empat kandidat dekat:

A. `na'at–man'ut` sederhana;  
B. `idhafah` dua isim sederhana;  
C. huruf jar + isim zhahir / jar–majrur;  
D. dhamir munfashil.

Untuk masing-masing kandidat, ukur:

- minimum dependency;
- jumlah clean examples;
- apakah contoh memerlukan P4 atau dapat berdiri sebelum P4;
- konflik prematur dominan;
- potensi membuka contoh kompetensi berikutnya.

Tujuannya menentukan siapa yang paling layak menjadi frontier setelah kompetensi nominal dasar, bukan memilih berdasarkan urutan kitab nahwu tradisional.

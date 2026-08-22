# Clean-Example Yield Test v0.1

**Status:** WORKING RESEARCH — NON-AUTHORITATIVE  
**Scope:** menguji urutan frontier awal dengan prinsip cumulative-only.  
**Tidak mengubah:** baseline, registry resmi, master jilid, assessment aktif, atau stage produksi.

## 1. Pertanyaan Uji

Setelah pengenalan isim dan fitur nominal dasar, relasi mana yang paling layak diajarkan lebih awal jika seluruh contoh wajib berasal dari Al-Qur'an dan contoh untuk `Kn` tidak boleh memerlukan kompetensi di atas `Kn`?

Kandidat yang dibandingkan:

- jumlah ismiyyah core: mubtada' + khabar isim sederhana;
- huruf jar + isim zhahir / jar–majrur;
- idhafah dua isim sederhana;
- na'at–man'ut sederhana;
- dhamir munfashil sebagai ekspansi nominal.

## 2. Kriteria Yield

`Clean-example yield` tidak hanya berarti jumlah kemunculan. Kandidat dinilai dengan:

1. **dependency depth** — berapa kompetensi prasyarat wajib;
2. **morphological burden** — apakah token membawa clitic/suffix lain;
3. **agreement burden** — apakah perlu gender/number/definiteness/case agreement;
4. **minimal-unit stability** — apakah target dapat diambil sebagai unit contiguous yang tetap sah;
5. **prematurity risk** — seberapa sering contoh membawa kompetensi yang belum ditempatkan;
6. **Quranic reuse potential** — seberapa luas struktur membuka contoh berikutnya.

## 3. Hasil Perbandingan Struktural

### A. Jumlah ismiyyah core

Bentuk target minimum:

`اسم + اسم`

Anchor:

> اللَّهُ الصَّمَدُ — 112:2

Kekuatan:

- predikasi dasar sangat jelas;
- tidak memerlukan fi'il;
- dapat dibangun dari isim + fitur definiteness/nakirah dasar;
- menjadi prasyarat penting untuk `inna`, `kana`, khabar jar–majrur, khabar jumlah, dan ekspansi nominal.

Risiko:

- banyak jumlah ismiyyah Qurani nyata memakai dhamir, jar–majrur, na'at, idhafah, atau ekspansi lain;
- karena itu hanya subset core yang boleh masuk tahap awal.

**Yield judgement:** `HIGH VALUE / MODERATE PURE YIELD`.

### B. Huruf jar + isim zhahir → jar–majrur

Bentuk target minimum:

`حرف جر + اسم ظاهر`

Kekuatan:

- dependency sangat pendek;
- relasi lokal dan mudah dibatasi;
- tidak memerlukan agreement seperti na'at;
- membuka banyak struktur berikutnya: khabar شبه جملة, attachment verbal, keterangan tempat/waktu tertentu, dan konstruksi kompleks.

Risiko:

- banyak bentuk Qurani mengandung clitic tambahan seperti `وَ`, `فَ`, `بِ`, `لِ` yang harus disegmentasi;
- preposisi + dhamir harus ditahan sampai dhamir muttashil diizinkan.

**Yield judgement:** `VERY HIGH POTENTIAL`.

### C. Idhafah dua isim sederhana

Bentuk target minimum:

`مضاف + مضاف إليه`

Kekuatan:

- relasi dua nominal sangat produktif;
- tidak memerlukan partikel penghubung;
- membuka banyak frasa Qurani dan ekspansi mubtada'/khabar.

Beban:

- mudhaf tidak menerima `الـ`/tanwin dalam pola dasar tertentu;
- mudhaf ilaih harus dipahami sebagai majrur;
- jika majrur sebagai fungsi belum diperkenalkan, idhafah membawa dependency i'rab tambahan;
- banyak contoh Qurani memakai dhamir sebagai mudhaf ilaih sehingga harus difilter.

**Yield judgement:** `HIGH`, tetapi dependency lebih berat daripada jar–majrur dasar.

### D. Na'at–man'ut sederhana

Bentuk target minimum:

`اسم + صفة`

Kekuatan:

- sangat penting untuk ekspansi frasa nominal;
- contoh Qurani luas.

Beban:

- agreement gender;
- agreement number;
- agreement definiteness;
- agreement case;
- risiko siswa mengira semua dua isim berurutan adalah mubtada'–khabar atau idhafah.

**Yield judgement:** `HIGH LATER`, tetapi kurang cocok sebagai relasi nominal pertama.

### E. Dhamir munfashil

Bentuk target minimum:

`هو / هي / أنت / أنتم ...`

Kekuatan:

- secara token identification dependency rendah;
- sangat produktif untuk jumlah ismiyyah pronominal.

Beban:

- paradigma persona, gender, dan number;
- jika langsung dipakai dalam jumlah, membawa variasi referensial yang tidak ada pada isim zhahir sederhana.

**Yield judgement:** `EARLY IDENTIFICATION`, tetapi ekspansi sintaksisnya sebaiknya dipisahkan.

## 4. Temuan: Pisahkan “Pengenalan” dari “Pemakaian”

Satu temuan penting adalah bahwa tangga tidak boleh mencampur dua jenis kompetensi:

- **Recognition-K:** mengenali bentuk/kategori;
- **Construction-K:** memahami relasi/fungsi dalam struktur.

Contoh:

- mengenali `هُوَ` dapat lebih awal;
- memakai `هُوَ` sebagai mubtada' dalam jumlah ismiyyah adalah kompetensi berikutnya;
- mengenali huruf `فِي` dapat lebih awal;
- memahami `فِي + اسم` sebagai jar–majrur adalah kompetensi relasional berikutnya.

Ini memungkinkan tangga tetap granular tanpa membuat contoh tahap awal membawa analisis yang belum diajarkan.

## 5. Kandidat Linearization v0.2 — BELUM FREEZE

Berdasarkan dependency, bukan sekadar tradisi urutan kitab:

1. `C1` — mengenali isim sederhana;
2. `C2` — mengenali `الـ` pada isim;
3. `C3` — mengenali bentuk nakirah/tanwin sederhana;
4. `C4` — mengenali dhamir munfashil dasar sebagai token;
5. `C5` — jumlah ismiyyah core: mubtada' + khabar isim zhahir sederhana;
6. `C6` — mengenali huruf jar frekuen secara individual;
7. `C7` — membentuk/memahami huruf jar + isim zhahir sebagai jar–majrur;
8. `C8` — mengenali fungsi majrur yang diperlukan pada relasi lokal;
9. `C9` — idhafah dua isim sederhana;
10. `C10` — na'at–man'ut paling sederhana setelah agreement minimum diperkenalkan/diintegrasikan.

### Catatan penting

`C1–C10` masih **candidate linearization**, bukan `K1–K10` final. Khusus `C8`, perlu diuji apakah i'rab majrur lebih baik menjadi K eksplisit atau atribut yang diperoleh bersamaan dengan C7.

## 6. Dependency Graph v0.2

```text
C1 ISIM
├── C2 AL-TA'RIF
├── C3 NAKIRAH/TANWIN
├── C4 DHAMIR MUNFASHIL (recognition)
│
├──────────────→ C5 JUMLAH ISMIYYAH CORE
│
└── C6 HURUF JAR (recognition)
       ↓
    C7 JAR–MAJRUR
       ↓
    C8 MAJRUR OPERASIONAL (?)
       ↓
    C9 IDHAFAH

C2 + C3 + fitur gender/number/case minimum
       ↓
    C10 NA'AT–MAN'UT
```

## 7. Konflik yang Harus Diuji Sebelum Freeze

### Konflik A — C4 vs C5

Dhamir munfashil secara recognition lebih mudah daripada jumlah ismiyyah, tetapi tidak diperlukan untuk anchor `اللَّهُ الصَّمَدُ`. Maka perlu diputuskan apakah tangga bersifat **strict prerequisite only** atau juga mempertimbangkan **recognition simplicity**.

### Konflik B — C7 vs C8

Secara pedagogis, `فِي الْأَرْضِ` dapat dipahami sebagai satu relasi sebelum siswa menguasai teori i'rab majrur secara abstrak. Maka `majrur` mungkin bukan K sebelum jar–majrur, tetapi **generalization K setelah beberapa pola**.

### Konflik C — C9 vs C10

Idhafah membawa majrur, sedangkan na'at membawa agreement. Data awal mendukung idhafah lebih dahulu, tetapi clean-example bank perlu diperbesar sebelum keputusan final.

## 8. Aturan Baru yang Diusulkan

### Rule R-REC/CON

Setiap kandidat diberi tipe:

- `REC` = recognition;
- `REL` = relation/construction;
- `GEN` = generalization/rule abstraction;
- `INT` = integration/complex analysis.

Urutan K final tidak harus mengikuti bab nahwu, tetapi harus memastikan bahwa `REL` tidak menggunakan `REC` yang belum dikuasai, dan `GEN` muncul setelah cukup evidence konkret.

### Rule R-I'RAB

Jangan otomatis mengajarkan teori i'rab abstrak sebelum struktur. Uji model:

`contoh konkret → relasi → pola perubahan akhir → generalisasi i'rab`.

Ini berpotensi menghasilkan tangga Qurani yang lebih natural dan tetap ilmiah.

## 9. Keputusan Batch

- jar–majrur tetap frontier relasional terkuat setelah jumlah ismiyyah core;
- idhafah sementara ditempatkan sebelum na'at;
- dhamir munfashil dipisahkan antara recognition dan syntactic use;
- i'rab majrur belum difreeze sebagai prerequisite; diuji sebagai generalization sesudah exposure;
- belum ada perubahan pada `REG-ARB-001`.

## 10. Batch Berikutnya

1. uji apakah `C1–C7` sudah cukup stabil untuk dipromosikan menjadi kandidat `K1–K7`;
2. cari counterexample yang memaksa perubahan urutan;
3. uji posisi fi'il sebagai frontier paralel: apakah pengenalan fi'il harus masuk sangat awal sebelum seluruh relasi nominal selesai;
4. mulai bangun dua jalur dependency sementara: **nominal track** dan **verbal track**, lalu cari titik integrasinya;
5. pertahankan semua hasil sebagai research layer sampai review/freeze.

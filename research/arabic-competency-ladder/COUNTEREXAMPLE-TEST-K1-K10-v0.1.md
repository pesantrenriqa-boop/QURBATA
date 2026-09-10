# Counterexample Test K1–K10 v0.1

**Status:** WORKING RESEARCH — NON-AUTHORITATIVE  
**Scope:** stress-test urutan kandidat awal agar tidak dibekukan hanya karena terlihat intuitif.  
**Prinsip:** setiap kandidat harus bertahan terhadap contoh Qurani yang berpotensi menunjukkan dependency lebih rendah/lebih tinggi dari posisi yang diusulkan.

## 1. Urutan yang Diuji

1. K1-CAND — mengenali isim sederhana;
2. K2-CAND — mengenali fi‘il sederhana;
3. K3-CAND — mengenali `الـ` pada isim;
4. K4-CAND — mengenali nakirah/tanwin sederhana;
5. K5-CAND — mengenali fi‘il madhi sederhana;
6. K6-CAND — mengenali fi‘il mudhari‘ sederhana;
7. K7-CAND — jumlah ismiyyah core: mubtada’ + khabar isim zhahir;
8. K8-CAND — fi‘il + fa‘il isim zhahir;
9. K9-CAND — mengenali huruf jar frekuen;
10. K10-CAND — jar–majrur dengan isim zhahir.

## 2. Counterexample A — Apakah huruf jar harus naik lebih awal?

### Dugaan konflik
Huruf jar sebagai token (`في`, `من`, `إلى`, `على`, `عن`, `بـ`, `لـ`, `كـ`) secara recognition sangat sederhana dan secara dependency tidak memerlukan jumlah ismiyyah atau fi‘il + fa‘il.

### Hasil audit
- `K9` sebagai **recognition-only** terlalu rendah jika prinsip linearization murni mengikuti dependency;
- ia tidak bergantung pada K7 atau K8;
- secara topological order, huruf jar dapat ditempatkan segera setelah kategori dasar isim/fi‘il atau setelah fitur nominal awal.

### Keputusan
`K9-CAND` **GAGAL posisi**, bukan gagal sebagai kompetensi.

**Implikasi:** recognition huruf jar harus dipindahkan lebih awal; konstruksi jar–majrur tetap dapat datang setelah isim/fungsi nominal dasar.

## 3. Counterexample B — Apakah dhamir munfashil layak masuk 10 besar?

### Dugaan konflik
Dhamir munfashil (`هو`, `هي`, `أنت`, `أنتم`, `أنا`, `نحن`) dapat dikenali sebagai token sebelum siswa memahami jumlah ismiyyah.

### Hasil audit
- dependency recognition rendah;
- tetapi paradigma persona/gender/number menambah beban klasifikasi;
- banyak contoh Qurani jumlah ismiyyah pronominal menjadi bersih jika recognition dhamir sudah lebih awal.

### Keputusan
Dhamir munfashil **layak masuk frontier awal**, tetapi sebagai `REC`, bukan langsung sebagai mubtada’ pronominal.

**Implikasi:** salah satu slot K awal harus dialokasikan untuk recognition dhamir sebelum ekspansi jumlah ismiyyah pronominal.

## 4. Counterexample C — Haruskah madhi dan mudhari‘ menjadi dua K?

### Dugaan konflik
Jika K2 sudah “mengenali fi‘il”, apakah K5 dan K6 memecah terlalu halus?

### Hasil audit
- bentuk morfologis madhi dan mudhari‘ berbeda jelas;
- konsekuensi sintaksis berikutnya berbeda (mis. prefiks mudhari‘, af‘al khamsah, nasb/jazm);
- corpus filtering membutuhkan kemampuan membedakan keduanya untuk mencegah contoh prematur;
- namun K2 sebagai kategori `fi‘il` mungkin redundan jika K5/K6 sudah sangat awal.

### Keputusan
Madhi dan mudhari‘ **tetap dua kompetensi**, tetapi perlu evaluasi apakah `mengenali fi‘il` sebagai K tersendiri atau sebagai payung/label konseptual non-K.

**Implikasi:** kandidat K2 lama berpotensi dilebur menjadi metadata/umbrella, sehingga urutan awal lebih atomik.

## 5. Counterexample D — Apakah `الـ` dan tanwin perlu menjadi K terpisah?

### Hasil audit
Keduanya adalah fitur permukaan berbeda dan menghasilkan filter corpus yang berbeda. Namun keduanya sibling dependencies setelah isim.

### Keputusan
Tetap dua kandidat K terpisah untuk saat ini, karena:
- satu contoh dapat mengandung `الـ` tanpa tanwin;
- satu contoh dapat mengandung tanwin tanpa `الـ`;
- keduanya membuka kontras definiteness secara bertahap.

## 6. Counterexample E — Apakah jumlah ismiyyah core terlalu awal?

### Anchor
`اللَّهُ الصَّمَدُ` (112:2) menunjukkan bahwa relasi mubtada’–khabar dua isim dapat berdiri tanpa dependency struktural tinggi.

### Hasil audit
Tidak ada counterexample yang memaksa jumlah ismiyyah core turun jauh. Yang berubah adalah prasyarat recognition yang mungkin perlu ditempatkan sebelum K7.

### Keputusan
Jumlah ismiyyah core **LULUS stress-test posisi awal**.

## 7. Counterexample F — Apakah fi‘il + fa‘il harus sebelum jumlah ismiyyah?

### Hasil audit
Keduanya merupakan dua relasi core paralel:
- nominal predication;
- verbal predication.

Tidak ada dependency langsung satu terhadap lainnya. Urutan linear di antara keduanya ditentukan oleh clean-example yield dan beban morfologi, bukan prerequisite keras.

### Keputusan
K7/K8 dapat bertukar secara teoritis. Untuk sementara jumlah ismiyyah core sedikit lebih ringan karena tidak memerlukan identifikasi tense/aspect verbal.

## 8. Revised Topological Candidate Order v0.2

Hasil stress-test mengubah urutan awal menjadi:

1. `R1` — mengenali isim sederhana;
2. `R2` — mengenali `الـ` pada isim;
3. `R3` — mengenali nakirah/tanwin sederhana;
4. `R4` — mengenali huruf jar frekuen secara individual;
5. `R5` — mengenali dhamir munfashil dasar;
6. `R6` — mengenali fi‘il madhi sederhana;
7. `R7` — mengenali fi‘il mudhari‘ sederhana;
8. `R8` — jumlah ismiyyah core: mubtada’ + khabar isim zhahir;
9. `R9` — fi‘il + fa‘il isim zhahir;
10. `R10` — jar–majrur dengan isim zhahir.

### Catatan
- kategori abstrak `fi‘il` dikeluarkan dari kandidat K awal dan menjadi **umbrella concept**;
- recognition huruf jar naik dari posisi 9 ke posisi 4;
- dhamir munfashil masuk 10 besar;
- urutan R6/R7 masih dapat diuji balik bila clean-example yield mudhari‘ ternyata lebih tinggi.

## 9. Status Setelah Stress-Test

| Kandidat | Status |
|---|---|
| R1 isim | STRONG |
| R2 `الـ` | STRONG |
| R3 tanwin/nakirah | STRONG |
| R4 huruf jar recognition | STRONG |
| R5 dhamir munfashil recognition | STRONG-REVIEW |
| R6 fi‘il madhi | STRONG |
| R7 fi‘il mudhari‘ | STRONG |
| R8 jumlah ismiyyah core | STRONG |
| R9 fi‘il + fa‘il zhahir | STRONG-REVIEW |
| R10 jar–majrur zhahir | STRONG |

## 10. Draft-Freeze Gate

Urutan R1–R10 **belum difreeze otomatis**. Untuk promosi ke `DRAFT-FROZEN`, diperlukan:

1. tidak ada dependency keras yang dilanggar;
2. tiap kandidat memiliki clean-example Qurani yang cukup;
3. tidak ada kandidat penting berdependency lebih rendah yang masih tertinggal;
4. segmentation rule konsisten;
5. corpus bank menyimpan PASS/PREMATURE/REVIEW;
6. status tetap research-only dan belum memodifikasi `REG-ARB-001`.

## 11. Keputusan Batch

- urutan lama K1–K10 **direvisi**;
- recognition huruf jar dipindah naik secara signifikan;
- dhamir munfashil masuk frontier awal;
- `fi‘il` generik tidak lagi kandidat K tersendiri;
- jumlah ismiyyah core bertahan sebagai relasi awal;
- next step: bangun **DRAFT-FREEZE-PROPOSAL K1–K10** berdasarkan R1–R10 dan siapkan mapping evidence minimal per K tanpa menyentuh registry resmi.

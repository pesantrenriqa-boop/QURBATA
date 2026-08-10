# Frontier K11+ v0.1

**Status:** WORKING RESEARCH — NON-AUTHORITATIVE  
**Parent baseline:** `DRAFT-FROZEN-K01-K10-v1.0`  
**Rule:** kandidat K11 hanya boleh memakai K1–K11; kandidat sesudahnya tunduk pada cumulative-only rule yang sama.

## 1. Kandidat Frontier

Setelah K1–K10, kandidat terdekat:

- penggunaan dhamir munfashil sebagai mubtada';
- dhamir muttashil sebagai unit morfologis;
- idhafah dua isim sederhana;
- na'at–man'ut sederhana;
- maf'ul bih isim zhahir;
- fa'il mustatir;
- khabar jar–majrur;
- 'athaf dua unsur sederhana.

## 2. Dependency Audit

### A. Dhamir munfashil sebagai mubtada'

Hard dependency: K5 + K8.

Recognition dhamir sudah tersedia pada K5 dan relasi mubtada'–khabar sudah tersedia pada K8. Karena itu ekspansi jumlah ismiyyah dengan mubtada' pronominal memiliki dependency sangat pendek.

**Frontier strength:** VERY HIGH.

### B. Khabar jar–majrur

Hard dependency: K8 + K9.

Jumlah ismiyyah dan jar–majrur sudah tersedia. Menggabungkan keduanya sebagai khabar شبه جملة merupakan integrasi langsung dua kompetensi yang sudah frozen.

**Frontier strength:** VERY HIGH.

### C. Maf'ul bih isim zhahir

Hard dependency: K10 + recognition isim.

Setelah fi'il+fa'il zhahir, ekspansi paling natural adalah menambah objek eksplisit. Tetapi clean examples harus menahan suffix object, dua objek, clause object, dan attachment lain yang belum tersedia.

**Frontier strength:** HIGH.

### D. Idhafah dua isim sederhana

Hard dependency: K1; secara analitis membutuhkan relasi mudhaf–mudhaf ilaih dan genitive pada unsur kedua.

Karena K9 sudah memberi exposure pada majrur melalui huruf jar, idhafah sekarang lebih aman ditempatkan daripada sebelum K9. Generalisasi majrur dapat tumbuh dari dua sumber: prepositional dan genitive construct.

**Frontier strength:** HIGH.

### E. Dhamir muttashil

Hard dependency: recognition isim/fi'il/harf sesuai host. Satu suffix dapat berfungsi sebagai possessive, object, atau object of preposition; karena itu recognition morfologis harus dipisahkan dari fungsi sintaksis.

**Frontier strength:** HIGH AS REC, LOWER AS UNIFIED RELATION.

### F. Na'at–man'ut

Hard dependency: isim + fitur definiteness; membutuhkan agreement gender/number/case sesuai contoh.

Masih lebih berat daripada idhafah karena agreement burden.

**Frontier strength:** MODERATE-HIGH.

### G. Fa'il mustatir

Hard dependency: K6/K7 + K10 dan konsep bahwa subject dapat tidak tampak sebagai token terpisah.

Lebih abstrak daripada fa'il zhahir.

**Frontier strength:** MODERATE.

### H. 'Athaf sederhana

Hard dependency: dua unit sejenis + huruf 'athaf yang dikenali. Masalahnya, conjunct dapat berupa kata, frasa, atau klausa; core harus dibatasi ke dua unsur nominal sederhana dahulu.

**Frontier strength:** MODERATE-HIGH.

## 3. Candidate Ordering K11–K18 — BELUM FREEZE

1. **K11-CAND** — dhamir munfashil sebagai mubtada' dalam jumlah ismiyyah sederhana
2. **K12-CAND** — khabar jar–majrur sederhana
3. **K13-CAND** — maf'ul bih isim zhahir sederhana
4. **K14-CAND** — idhafah dua isim sederhana
5. **K15-CAND** — mengenali dhamir muttashil sebagai segmen
6. **K16-CAND** — na'at–man'ut sederhana
7. **K17-CAND** — 'athaf dua isim/frasa nominal sederhana
8. **K18-CAND** — fa'il mustatir dasar

## 4. Kenapa K11 dan K12 Sangat Kuat

K11 dan K12 tidak memperkenalkan kategori besar baru. Keduanya **mengintegrasikan kompetensi yang sudah ada**:

- K11 = K5 (dhamir recognition) + K8 (jumlah ismiyyah);
- K12 = K8 (jumlah ismiyyah) + K9 (jar–majrur).

Secara dependency graph, keduanya adalah frontier terdekat setelah K10.

## 5. Konflik yang Harus Diuji

### K13 vs K14

Maf'ul bih adalah ekspansi langsung K10, sedangkan idhafah adalah relasi nominal baru. Urutannya harus ditentukan dengan clean-example yield.

### K15 position

Dhamir muttashil recognition mungkin dapat naik sebelum K13/K14 karena secara token-level sederhana, tetapi segmentasi host+suffix membawa beban morfologi. Jangan naikkan hanya karena bentuknya pendek.

### K16 agreement burden

Na'at tidak boleh naik sebelum sistem minimal agreement dapat dipahami dari contoh. Agreement tidak harus menjadi teori abstrak lebih dahulu, tetapi harus tercakup dalam evidence.

## 6. Evidence Rules K11+

- simpan semua PASS, tidak dibatasi 20–30;
- teaching set 20–30+ dipilih kemudian;
- unit boleh berupa potongan ayat yang utuh secara sintaksis;
- seluruh segmen morfologis harus diperiksa;
- jika unit membutuhkan kompetensi sesudah target, status PREMATURE;
- referensi ayat penuh tetap disimpan walau unit pembelajaran hanya frasa/klausa.

## 7. Next Test

Prioritas berikutnya:

1. head-to-head K11 vs K12 untuk memastikan linearization;
2. evidence expansion keduanya;
3. head-to-head maf'ul bih vs idhafah untuk posisi K13/K14;
4. setelah stabil, lanjutkan draft-freeze K11–K20, bukan memaksa blok sepuluh jika dependency menunjukkan ukuran batch berbeda.

# DRAFT-FROZEN K01–K10 v1.0

**Status:** DRAFT-FROZEN — RESEARCH LAYER ONLY  
**Branch:** `agent/quranic-arabic-competency-ladder`  
**Authority:** NON-AUTHORITATIVE terhadap curriculum registry.  
**Scope:** baseline kerja stabil pertama untuk urutan kompetensi Bahasa Arab Qurani berbasis cumulative-only rule.

## 1. Prinsip Pengendali

1. `K1 → K10` adalah urutan pembelajaran linear yang diturunkan dari dependency graph.
2. Nomor K tidak berarti semua K sebelumnya adalah hard prerequisite langsung.
3. Setiap contoh untuk `Kn` hanya boleh memerlukan kompetensi `K1..Kn`.
4. Kompetensi di atas `Kn` membuat contoh berstatus `PREMATURE` untuk tahap tersebut.
5. Unit contoh dapat berupa kata, frasa, klausa, atau ayat penuh selama unit itu contiguous, utuh secara linguistik, dan tidak memalsukan struktur.
6. Semua contoh berasal dari Al-Qur'an dan menyimpan referensi surah:ayat.
7. Corpus bank tidak dibatasi jumlah; 20–30+ adalah target teaching-set bila tersedia, bukan batas evidence.
8. Evidence bank tetap dapat diperluas setelah freeze.
9. Freeze ini belum mengubah `REG-ARB-001`, `AR-STG-*`, master jilid, halaman, atau assessment produksi.

## 2. Urutan DRAFT-FROZEN

### K1 — REC-N-BASE
**Kompetensi:** mengenali isim sederhana.

Batas:
- belum membahas fungsi mubtada', khabar, fa'il, maf'ul, mudhaf, na'at;
- belum membahas teori i'rab.

### K2 — REC-AL
**Kompetensi:** mengenali `الـ` pada isim.

Batas:
- bukan seluruh teori ma'rifah;
- dhamir, isim isyarah, maushul, dan idhafah belum dimasukkan.

### K3 — REC-NAK-TAN
**Kompetensi:** mengenali nakirah/tanwin nominal sederhana.

Catatan:
- K2 dan K3 adalah parallel nominal features yang dilinear-kan untuk pembelajaran.

### K4 — REC-PREP
**Kompetensi:** mengenali huruf jar frekuen.

Target awal antara lain:
- `مِنْ`
- `فِي`
- `عَلَى`
- `إِلَى`
- `بِـ`
- `لِـ`

Batas:
- belum menganalisis keseluruhan jar–majrur.

### K5 — REC-PRON-SEP
**Kompetensi:** mengenali dhamir munfashil dasar.

Contoh bentuk:
- `هُوَ`
- `هِيَ`
- `أَنْتَ`
- `أَنْتُمْ`

Batas:
- belum digunakan sebagai mubtada' dalam target inti;
- belum membahas antecedent/reference kompleks.

### K6 — REC-V-PERF
**Kompetensi:** mengenali fi'il madhi sederhana.

Batas:
- belum membahas fa'il sebagai fungsi;
- belum membahas tashrif lengkap, bina' majhul, suffix kompleks, atau form derivation.

### K7 — REC-V-IMPF
**Kompetensi:** mengenali fi'il mudhari' sederhana.

Batas:
- belum membahas raf'/nasb/jazm;
- belum membahas af'al khamsah dan governing particles.

### K8 — REL-NOM-PRED
**Kompetensi:** jumlah ismiyyah core — mubtada' + khabar isim zhahir sederhana.

Anchor Qurani:

> اللَّهُ الصَّمَدُ — QS 112:2

Target:
- mubtada' isim zhahir;
- khabar isim zhahir;
- tanpa fi'il;
- tanpa dhamir target;
- tanpa jar–majrur sebagai khabar;
- tanpa idhafah, na'at, inna, kana, atau jumlah bersarang.

### K9 — REL-PP
**Kompetensi:** huruf jar + isim zhahir sebagai jar–majrur.

Contoh tipe clean:
- `فِي الْأَرْضِ`
- `فِي السَّمَاوَاتِ`
- `عَنِ النَّبَإِ`
- `بِالْحَقِّ`
- `مِنَ الْأَرْضِ`

Batas:
- preposition + dhamir muttashil ditunda;
- clitic tambahan yang belum dipelajari membuat evidence PREMATURE.

### K10 — REL-VS
**Kompetensi:** fi'il + fa'il isim zhahir sederhana.

Contoh tipe clean:
- `جَاءَ الْحَقُّ`
- `زَهَقَ الْبَاطِلُ`
- `قَالَ مُوسَىٰ`
- `يُرِيدُ اللَّهُ`

Batas:
- core set hanya fa'il zhahir yang benar-benar menjadi subject target;
- fa'il mustatir/suffix ditunda;
- maf'ul bih, quoted-speech dependency, coordination, passive, dan subordinate structure ditunda.

## 3. Dependency Metadata

| K | Type | Hard dependencies | Notes |
|---|---|---|---|
| K1 | REC | — | foundational nominal recognition |
| K2 | REC | K1 | nominal feature |
| K3 | REC | K1 | parallel feature to K2 |
| K4 | REC | — | relational use waits until K9 |
| K5 | REC | — | syntactic use deferred |
| K6 | REC | — | relational use waits until K10 |
| K7 | REC | — | relational use waits until K10 |
| K8 | REL | K1 + nominal features required by evidence | core nominal predication |
| K9 | REL | K1 + K4 | local prepositional relation |
| K10 | REL | K1 + K6/K7 | verbal predication with overt subject |

## 4. Evidence Status

### Strongest anchors
- K8: `اللَّهُ الصَّمَدُ`
- K9: multiple clean local prepositional units
- K10: multiple overt-subject verbal units, with strict evidence flag

### Evidence policy
- `PASS` = seluruh dependency ≤ target K;
- `PREMATURE` = ada dependency di atas target K;
- `REVIEW` = unit/analysis perlu verifikasi tambahan;
- PREMATURE examples disimpan untuk kompetensi berikutnya, tidak dibuang.

## 5. Why K9 Before K10

Head-to-head test menunjukkan jar–majrur lebih layak lebih awal karena:

- hard dependency lebih pendek;
- struktur sangat lokal;
- tidak ada hidden subject;
- clean filtering lebih mudah;
- prematurity risk lebih rendah.

Karena itu urutan research baseline adalah:

`K8 jumlah ismiyyah → K9 jar–majrur → K10 fi'il+fa'il`.

## 6. Freeze Meaning

`DRAFT-FROZEN` berarti:

- urutan cukup stabil untuk menjadi baseline penelitian lanjutan;
- K11+ harus menghormati K1–K10;
- perubahan urutan K1–K10 harus mempunyai counterevidence kuat dan dokumen superseding;
- evidence bank tetap tumbuh;
- belum boleh dianggap sebagai registry kurikulum resmi sebelum review dan mapping formal.

## 7. Integration Contract

Setelah keseluruhan tangga K1–Kn stabil dan tervalidasi:

`research K-order → review → decision/mapping → REG-ARB-001 → AR-STG mapping → master → page/data/assessment → RIQA OS / RIQA Education System / RIQA Formal Competency System / research outputs`.

Tidak boleh membuat sumber kebenaran paralel di luar registry resmi.

## 8. Next Discovery Frontier

K11+ akan diuji dari kandidat berikut tanpa menganggap urutannya sudah final:

- penggunaan dhamir munfashil sebagai mubtada';
- dhamir muttashil;
- idhafah dua isim sederhana;
- na'at–man'ut;
- maf'ul bih isim zhahir;
- fa'il mustatir/encoded;
- khabar jar–majrur;
- 'athaf sederhana.

Rule tetap:

> Contoh K11 hanya boleh mengandung K1–K11; K12+ tidak boleh hadir sebagai dependency yang diperlukan.

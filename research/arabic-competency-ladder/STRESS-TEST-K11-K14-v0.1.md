# Stress Test K11–K14 + Frontier K15–K18 v0.1

**Status:** WORKING RESEARCH — NON-AUTHORITATIVE  
**Parent:** `EVIDENCE-BANK-K11-K14-v0.1.md`  
**Rule:** cumulative-only; unit Qurani terkecil yang utuh; semua segmen morfologis diperiksa.

## 1. Revised Order Under Test

- K11-CAND — dhamir munfashil sebagai mubtada' dalam jumlah ismiyyah sederhana
- K12-CAND — khabar jar–majrur sederhana
- K13-CAND — idhafah dua isim sederhana
- K14-CAND — maf'ul bih isim zhahir sederhana

## 2. Stress Test K11

Formula: `ضمير منفصل + خبر`.

Dependencies already available:
- recognition dhamir: K5;
- jumlah ismiyyah core: K8;
- nominal features: K1–K3 as needed.

Potential blockers:
- khabar berupa jar–majrur → sebenarnya K12, sehingga tidak boleh menjadi core evidence K11;
- khabar berupa jumlah/fi'il → higher structure;
- khabar beridhafah/na'at kompleks → premature.

Conclusion: **PASS**. K11 dapat dipertahankan bila core evidence memakai khabar nominal sederhana.

## 3. Stress Test K12

Formula: jumlah ismiyyah dengan khabar berupa `جار ومجرور`.

Dependencies:
- K8 jumlah ismiyyah;
- K9 jar–majrur.

Potential blockers:
- mubtada' berupa struktur yang belum dikenal;
- preposition + attached pronoun sebelum K15;
- khabar mengandung nested idhafah/na'at yang belum diizinkan.

Conclusion: **PASS**. Dependency bersifat integrasi dua K yang sudah tersedia.

## 4. Stress Test K13

Formula: `مضاف + مضاف إليه` dua isim zhahir sederhana.

Dependencies:
- isim recognition;
- exposure fungsi genitive sudah tersedia melalui K9, tetapi idhafah memperkenalkan penyebab genitive kedua.

Potential blockers:
- mudhaf ilaih berupa dhamir muttashil → tahan sampai K15+;
- chain idhafah tiga unsur → bukan core;
- na'at pada salah satu unsur → premature;
- koordinasi → premature.

Conclusion: **PASS / STRONG**. Struktur lokal, contiguous, dan mudah diekstrak.

## 5. Stress Test K14

Formula minimum: `فعل + فاعل ظاهر + مفعول به ظاهر` atau unit valid dengan subject eksplisit yang sudah dapat dianalisis.

Dependencies:
- K6/K7 recognition verb;
- K10 fi'il + fa'il zhahir;
- isim recognition.

Potential blockers:
- object pronoun suffix;
- subject suffix/mustatir;
- two objects;
- object clause;
- quoted speech;
- prepositional/complement material yang diperlukan untuk makna struktur target.

Conclusion: **PASS CONDITIONALLY**. Kompetensi valid pada posisi ini, tetapi evidence policy harus lebih ketat daripada K13.

## 6. No Dependency Reversal Found

Stress test tidak menemukan alasan struktural untuk mengembalikan maf'ul bih ke K13. Revised order dipertahankan:

`K11 pronoun-mubtada' → K12 PP-khabar → K13 idhafah → K14 maf'ul bih zhahir`.

## 7. Frontier K15–K18

### Candidate A — dhamir muttashil recognition

Pisahkan recognition dari fungsi:
- suffix nominal possessive;
- suffix object pada fi'il;
- suffix setelah preposition.

K15 tidak boleh sekaligus mengajarkan tiga fungsi tersebut. Target awal hanya segment recognition: mengenali host + attached pronoun.

**Strength:** VERY HIGH as REC.

### Candidate B — na'at–man'ut core

Dependency:
- isim;
- definiteness contrast;
- agreement minimum.

Core harus dibatasi pada dua unsur sederhana, tanpa idhafah chain atau coordination.

**Strength:** HIGH, tetapi agreement burden tetap lebih besar daripada K15 recognition.

### Candidate C — 'athaf sederhana

Core: dua isim/frasa nominal sederhana dengan conjunction yang sudah dikenali pada unit tersebut.

Perlu memisahkan recognition huruf 'athaf dari construction. Jika belum ada K recognition, sebaiknya dibuat terlebih dahulu.

**Strength:** HIGH AFTER CONJUNCTION REC.

### Candidate D — fa'il mustatir

Mengharuskan siswa memahami bahwa subject dapat direpresentasikan dalam fitur verba tanpa token isim terpisah.

**Strength:** IMPORTANT BUT ABSTRACT; cenderung sesudah recognition dhamir dan pengalaman fi'il-fa'il zhahir.

## 8. Proposed K15–K19 Candidate Expansion

Stress test menunjukkan 'athaf sebaiknya dipecah menjadi recognition + relation. Maka kandidat menjadi:

- **K15-CAND** — mengenali dhamir muttashil sebagai segmen morfologis
- **K16-CAND** — na'at–man'ut sederhana
- **K17-CAND** — mengenali huruf 'athaf frekuen (`و`, `ف`, `ثم` pada fungsi yang relevan)
- **K18-CAND** — 'athaf dua unsur nominal sederhana
- **K19-CAND** — fa'il mustatir dasar

Belum freeze.

## 9. Critical Issue for K15

Dhamir muttashil sangat produktif tetapi polyfunctional. Karena itu metadata evidence harus mencatat:

- `host_type`: noun / verb / preposition;
- `pronoun_form`;
- `surface_segmentation`;
- `syntactic_function`: withheld / possessive / object / prep-object;
- `function_allowed_at_current_K`: yes/no.

Dengan cara ini siswa dapat belajar **mengenali suffix** di K15 tanpa dipaksa memahami seluruh fungsi sintaksisnya sekaligus.

## 10. Next Batch

1. bangun evidence bank K15 recognition dengan tiga host type tetapi fungsi ditahan;
2. uji na'at core terhadap agreement burden;
3. tentukan apakah recognition huruf 'athaf harus datang sebelum na'at atau sesudahnya;
4. lakukan head-to-head K15/K16/K17;
5. bila K11–K14 tetap stabil setelah evidence expansion, terbitkan `DRAFT-FROZEN-K11-K14-v1.0` secara terpisah dari K15+.

# Audit K05 + Integrity Check K01–K10 v0.1

**Status:** PRE-FREEZE AUDIT — RESEARCH LAYER ONLY  
**Authority:** NON-AUTHORITATIVE. Tidak mengubah `REG-ARB-001`, stage resmi, master jilid, atau produksi.

## 1. Tujuan

Audit ini menjawab dua pertanyaan terakhir sebelum draft-freeze:

1. Apakah `K5 = dhamir munfashil dasar (recognition)` berada pada posisi yang tidak merusak dependency?
2. Apakah seluruh urutan K1–K10 memenuhi cumulative-only rule tanpa dependency reversal?

## 2. Audit K5 — Dhamir Munfashil

### Target

Mengenali bentuk pronomina terpisah Qurani seperti `هُوَ`, `هِيَ`, `أَنْتَ`, `أَنْتُمْ` sebagai token, tanpa langsung menganalisis fungsinya dalam jumlah.

### Hard dependency

Secara recognition, tidak memerlukan K1–K4 sebagai dependency linguistik langsung.

### Mengapa tidak dipindah ke K1?

- urutan K adalah linearization pedagogis dari graph, bukan daftar hard dependency murni;
- isim zhahir dipilih sebagai fondasi karena membuka K2, K3, K8, K9, K10;
- dhamir mempunyai paradigma persona/gender/number yang lebih kompleks walau recognition per token sederhana;
- memasukkan dhamir terlalu awal tidak membuka lebih banyak clean relations dibanding isim zhahir.

### Mengapa tidak ditunda sesudah K8?

- recognition dhamir cukup ringan;
- keberadaannya sebelum K8 menyiapkan ekspansi `mubtada' dhamir` untuk K11+;
- K8 sendiri tetap memakai isim zhahir sehingga K5 tidak menjadi hard prerequisite wajib.

### Keputusan audit

`K5 POSITION ACCEPTED`.

Catatan metadata wajib:
- `sequence_order = 5`;
- `hard_dependencies = []` atau minimal sesuai implementation policy;
- `expansion_dependencies`: digunakan nanti untuk jumlah ismiyyah pronominal.

## 3. Integrity Check K1–K10

### K1 — isim sederhana
No reversal. Atomic recognition.

### K2 — `الـ` pada isim
Depends on K1. No reversal.

### K3 — nakirah/tanwin sederhana
Depends on K1; K2 only contrast/parallel. No reversal.

### K4 — huruf jar frekuen
Recognition can stand alone; relational use waits until K9. No reversal.

### K5 — dhamir munfashil
Recognition independent; syntactic use deferred. No reversal.

### K6 — fi'il madhi sederhana
Recognition atomic; fa'il analysis deferred. No reversal.

### K7 — fi'il mudhari' sederhana
Recognition atomic; governance/i'rab deferred. No reversal.

### K8 — jumlah ismiyyah core
Depends on K1 plus nominal features needed by actual examples. Anchor `اللَّهُ الصَّمَدُ` remains valid. No reversal.

### K9 — jar–majrur zhahir
Depends on K1 + K4. No need for later K. No reversal.

### K10 — fi'il + fa'il zhahir
Depends on K1 + K6/K7. Clean examples require strict filtering but do not require later K by definition. No reversal.

## 4. Cumulative-Only Integrity

For each `Kn`:

`Allowed competencies = K1..Kn`

But example selection prioritizes minimum actual dependency. Therefore:

- a K8 example containing idhafah or na'at is PREMATURE;
- a K9 example with preposition+dhamir muttashil is PREMATURE;
- a K10 example with hidden/suffix fa'il, maf'ul bih, quoted speech dependency, or later structure is PREMATURE for core set;
- all PREMATURE evidence remains stored for later K, not discarded.

## 5. Integrity Result

No dependency reversal found that forces renumbering K1–K10.

### Result

- K1: PASS
- K2: PASS
- K3: PASS
- K4: PASS
- K5: PASS WITH LINEARIZATION NOTE
- K6: PASS
- K7: PASS
- K8: PASS
- K9: PASS
- K10: PASS WITH STRICT-EVIDENCE FLAG

## 6. Freeze Recommendation

The first ten competencies are eligible for **DRAFT-FROZEN v1.0 in the research layer**.

This freeze means:

- order is stable enough to serve as working baseline;
- evidence bank remains expandable;
- future counterevidence can trigger superseding research decision;
- it is NOT yet authoritative curriculum registry;
- integration into `REG-ARB-001` requires separate review/decision.

## 7. Final Order for Draft Freeze

1. K1 — mengenali isim sederhana
2. K2 — mengenali `الـ` pada isim
3. K3 — mengenali nakirah/tanwin nominal sederhana
4. K4 — mengenali huruf jar frekuen
5. K5 — mengenali dhamir munfashil dasar
6. K6 — mengenali fi'il madhi sederhana
7. K7 — mengenali fi'il mudhari' sederhana
8. K8 — jumlah ismiyyah core: mubtada' + khabar isim zhahir
9. K9 — jar–majrur dengan isim zhahir
10. K10 — fi'il + fa'il isim zhahir sederhana

## 8. Next Action

Terbitkan `DRAFT-FROZEN-K01-K10-v1.0.md`, lalu lanjutkan discovery K11+ dengan aturan bahwa K11 examples hanya boleh mengandung K1–K11.

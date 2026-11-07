# Counterexample Test K18–K20 v0.1

**Status:** WORKING RESEARCH — PRE-FREEZE  
**Parent:** `EVIDENCE-EXPANSION-K18-K20-v0.1.md`

## Sequence Under Test

- K18-CAND — dhamir muttashil sebagai mudhaf ilaih
- K19-CAND — 'athaf dua unsur nominal sederhana
- K20-CAND — huruf jar + dhamir muttashil

## K18 Stress Test

Formula inti: `اسم + ضمير متصل` dengan fungsi possessive/genitive.

Hard dependencies:
- K13 idhafah;
- K15 recognition dhamir muttashil.

Potential blockers:
- host berupa verba → object suffix, bukan K18;
- host berupa preposition → prep-object, calon K20;
- chain nominal kompleks → premature;
- na'at/coordination tambahan yang diperlukan → premature.

**Result:** PASS. Tidak ditemukan dependency reversal. K18 adalah integrasi langsung K13+K15.

## K19 Stress Test

Formula inti: `اسم/عبارة اسمية + حرف عطف + اسم/عبارة اسمية` sederhana.

Hard dependencies:
- K16 recognition conjunction;
- recognition/structure kedua conjunct harus <= K19.

Potential blockers:
- conjunction scope terhadap klausa;
- conjunct kedua berupa struktur belum dikenal;
- ellipsis atau coordination kompleks;
- `ف`/`و` dengan fungsi non-'athaf.

**Result:** PASS WITH FUNCTION TAGGING. K19 valid jika evidence hanya mengambil occurrence yang fungsi 'athaf-nya tervalidasi dan kedua unsur sudah dikuasai.

## K20 Stress Test

Formula inti: `حرف جر + ضمير متصل`.

Hard dependencies:
- K9 jar–majrur;
- K15 recognition dhamir muttashil.

Contoh target bentuk:
- `لَهُ`
- `بِهِ`
- `فِيهِ`
- `عَلَيْهِ`
- `مِنْهُ`
- `إِلَيْهِ`

Potential blockers:
- prefiks tambahan yang belum dikenali;
- attached material setelah unit;
- fungsi partikel yang bukan huruf jar;
- embedded clause di luar unit tidak menjadi bagian target.

**Result:** PASS / VERY STRONG. Dependency lokal dan tidak memerlukan fa'il mustatir atau object suffix.

## Counterexample Search Outcome

Tidak ditemukan alasan struktural yang memaksa:
- K20 mendahului K18;
- K19 mendahului K18;
- fa'il mustatir menyela sebelum K20.

Urutan K18 → K19 → K20 dipertahankan.

## Freeze Recommendation

- K18: READY
- K19: READY WITH FUNCTION TAGGING
- K20: READY

Rekomendasi: terbitkan `FINAL-GATE-K18-K20-v1.0` pada research layer.

## Frontier K21+

Kandidat terdekat setelah K20:

1. dhamir muttashil sebagai maf'ul bih;
2. fa'il mustatir dasar;
3. maf'ul bih pronominal setelah fi'il;
4. jumlah ismiyyah dengan mubtada' berupa idhafah/na'at;
5. jumlah fi'liyyah dengan jar–majrur attachment sederhana;
6. plural/dual agreement expansions;
7. isim isyarah sederhana;
8. isim maushul recognition.

Prioritas berikutnya: head-to-head `object suffix` vs `fa'il mustatir` karena keduanya sama-sama ekspansi verbal tetapi dependency dan clean-example burden berbeda.
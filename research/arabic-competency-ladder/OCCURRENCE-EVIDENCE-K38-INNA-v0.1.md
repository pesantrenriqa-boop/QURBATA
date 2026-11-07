# Occurrence-Specific Evidence Bank K38 — `إِنَّ + اسمها + خبرها` v0.1

**Status:** WORKING RESEARCH — EVIDENCE GATE  
**Baseline:** K1–K37 DRAFT-FROZEN  
**Target:** K38-CAND — memahami konstruksi sederhana `إِنَّ + اسم إنّ + خبر إنّ` tanpa membawa kompetensi K39+.

## 1. Core acceptance rule

Sebuah contoh PASS hanya jika:

1. `إِنَّ` occurrence tervalidasi sebagai particle target;
2. اسم إنّ eksplisit dan berada dalam kategori yang sudah tersedia;
3. خبر إنّ sederhana dan dapat dianalisis dengan K sebelumnya;
4. tidak membutuhkan `كان/ليس` construction;
5. tidak membutuhkan silah maushul;
6. tidak membutuhkan clause-level khabar yang belum dibuka;
7. tidak bergantung pada `لام التوكيد` atau particle-government baru yang belum dipetakan;
8. unit target dapat dipotong secara sintaksis tanpa merusak hubungan `إنّ–اسمها–خبرها`;
9. seluruh dependency aktual <= K38.

## 2. Evidence classes

### CLASS A — PURE CORE

Pattern target:

`إِنَّ + اسم ظاهر/ضمير معروف + خبر مفرد بسيط`

Ideal features:
- khabar satu kata atau nominal phrase sangat sederhana;
- tidak ada relative clause;
- tidak ada embedded verb clause;
- tidak ada emphatic lam;
- tidak ada conjunction yang memperluas scope target.

**Use:** core teaching set.

### CLASS B — CUMULATIVE CLEAN

Mengandung struktur lama yang sudah dikuasai, misalnya:
- idhafah K13/K18;
- na'at K17;
- jar–majrur K9/K12/K20;
- attached pronoun recognition/functions yang sudah frozen;
- demonstrative/relative token recognition bila tidak memerlukan relation baru.

**Use:** reinforcement setelah Class A.

### CLASS C — REVIEW / PREMATURE

Hold jika ada:
- `لام التوكيد` sebagai unsur gramatikal aktif yang belum dipetakan;
- خبر berupa jumlah fi'liyyah yang memerlukan subject inference atau attachment baru;
- silah maushul;
- `كان/ليس` di dalam khabar;
- conditional/exception scope yang diperlukan untuk memahami target;
- nested clause atau multiple-governor ambiguity.

## 3. Candidate patterns for corpus extraction

Prioritas pencarian occurrence:

1. `إِنَّ + proper noun + adjective/noun khabar`
2. `إِنَّ + الله + adjective/noun khabar`
3. `إِنَّ + noun phrase already-covered + adjective/noun khabar`
4. `إِنَّهُ + خبر مفرد` only if attached pronoun segmentation/function is already safe and no new relation is imported
5. examples with PP khabar only after confirming K12/K9 makes the relation fully cumulative

## 4. Important distinction: token recognition vs governed construction

K33 already answers: **"ini adalah `إِنَّ`"**.

K38 must answer:
- mana اسم إنّ;
- mana خبر إنّ;
- bagaimana hubungan ketiganya;
- apa perubahan fungsi/case yang dapat diamati pada contoh bersih.

Therefore a mere occurrence of `إِنَّ` is not evidence for K38.

## 5. Lam-emphasis problem

Forms such as:

`إِنَّ ... لَ...`

must not automatically PASS.

Reason:
- the lam is a distinct surface marker;
- if its emphatic/governing relation matters to the sentence analysis, dependency exceeds current target;
- removing it from the teaching unit is allowed only if the remaining unit stays syntactically valid and faithful to the Qur'anic occurrence.

Metadata:
- `has_lam_emphasis: yes/no`
- `lam_required_for_target_analysis: yes/no`
- `status_if_lam_locked: PASS/REVIEW/PREMATURE`

## 6. Evidence ledger schema

Each occurrence should store:

- `surah`
- `ayah`
- `span_ar`
- `inna_form`
- `inna_noun_span`
- `khabar_span`
- `khabar_type`
- `actual_dependencies[]`
- `has_lam_emphasis`
- `has_relative_clause`
- `has_kana_laysa`
- `has_clausal_khabar`
- `status`
- `rejection_reason`
- `teaching_rank`

## 7. Current gate judgement

### Structural viability

**PASS.**

K38 is a genuine new relation, not inventory inflation.

### Evidence sufficiency

**NOT YET CLOSED.**

The gate is not satisfied merely by finding many `إِنَّ` tokens. We need 20–30+ occurrence-level PASS examples whose complete dependency chain is <= K38.

### Most likely clean-yield bottlenecks

1. lam emphasis;
2. clausal khabar;
3. relative-clause material;
4. pronominal اسم إنّ whose reference/function may complicate teaching;
5. long nominal phrase with nested modifiers.

## 8. Teaching-set strategy

Do not force 20–30 examples into one surface pattern.

Build in tiers:

- Tier 1: 8–12 pure-core examples;
- Tier 2: 8–12 cumulative nominal examples;
- Tier 3: remaining PASS examples with already-mastered PP/idhafah/na'at expansions;
- keep all other valid occurrences in reinforcement bank;
- keep PREMATURE examples as negative evidence for later K design.

## 9. Freeze condition

K38 may be DRAFT-FROZEN only when all are true:

- dependency graph stable;
- at least a credible 20–30+ PASS teaching pool exists or corpus audit demonstrates that a smaller finite clean pool is a property of the corpus rather than a search failure;
- no recurring hidden feature forces a missing prerequisite before K38;
- lam-emphasis issue is explicitly resolved;
- distinction between nominal/PP/clausal khabar is encoded.

## 10. Next action

1. expand the actual occurrence ledger from the Quranic corpus;
2. quantify PASS / REVIEW / PREMATURE yield;
3. test whether `لام التوكيد` deserves a recognition K before full K38 or can remain a later locked feature;
4. if yield is sufficient, issue `FINAL-GATE-K38-v1.0`;
5. otherwise revise the frontier rather than forcing freeze.

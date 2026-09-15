# CANONICAL REGISTRY — K58–K67 v0.1

**Status:** CANONICALIZATION IN PROGRESS  
**Source status:** Derived from frozen final-gate decisions already recorded on branch `agent/quranic-arabic-competency-ladder`.

## Purpose

This file normalizes the late-stage core competencies into one canonical registry format before full K1–K67 consolidation.

---

## K58 — Simple Inter-Clausal Coordination
- **Canonical definition:** Mengenali koordinasi dua klausa Qurani yang sama-sama utuh melalui satu penghubung eksplisit, dimulai dari `و` yang tervalidasi sebagai koordinator antarklausa.
- **Primary domain:** CLAUSE / DISCOURSE
- **Learner operation:** identify clause 1, clause 2, overt coordinator, and classify the relation as clause-level coordination.
- **Direct prerequisites:** prior clause-internal analysis through K57.
- **Core exclusion:** phrase-level coordination, nested coordination, ellipsis, disputed wāw functions.
- **Assessment signature:** `أين الجملة الأولى؟ وأين الجملة الثانية؟ وما الرابط بينهما؟`
- **Architecture status:** DRAFT-FROZEN

## K59 — Temporal Sequencing with `ثم`
- **Canonical definition:** Mengenali urutan kejadian antara dua klausa Qurani yang utuh melalui `ثم` yang tervalidasi sebagai penghubung sekuensial.
- **Primary domain:** DISCOURSE / TEMPORAL RELATION
- **Learner operation:** identify two linked clauses and classify clause 2 as following clause 1 in validated sequence.
- **Direct prerequisites:** K58 plus prior clause analysis.
- **Core exclusion:** full `التراخي` theory, rhetorical `ثم`, ambiguous sequencing.
- **Architecture status:** DRAFT-FROZEN

## K60 — Relative-Clause Boundary (`صلة الموصول`)
- **Canonical definition:** Mengenali `صلة الموصول` sebagai klausa yang melekat pada `اسم موصول` eksplisit, dengan menentukan batas awal dan akhirnya dalam konstruksi Qurani sederhana.
- **Primary domain:** CLAUSE / DEPENDENCY
- **Learner operation:** detect the relative marker and delimit the following relative clause.
- **Direct prerequisites:** analyzable clauses through K59.
- **Core exclusion:** advanced `العائد`, nested relative clauses, full relative-pronoun inventory.
- **Architecture status:** DRAFT-FROZEN

## K61 — Explicit Relative Resumptive (`العائد`)
- **Canonical definition:** Mengenali `العائد` eksplisit di dalam `صلة الموصول` dan menghubungkannya kembali kepada `اسم الموصول` dalam konstruksi Qurani sederhana.
- **Primary domain:** REFERENCE / DEPENDENCY
- **Learner operation:** identify one overt resumptive pronoun and resolve its antecedent to the relative expression.
- **Direct prerequisites:** K60.
- **Core exclusion:** omitted resumptive, ambiguous antecedent, long-distance reference, nested relatives.
- **Architecture status:** DRAFT-FROZEN

## K62 — Contrast / Correction
- **Canonical definition:** Mengenali relasi pertentangan atau koreksi antara dua proposisi Qurani melalui `لكن` eksplisit yang tervalidasi, lalu menjelaskan apa yang dibatasi atau dikoreksi oleh proposisi kedua.
- **Primary domain:** DISCOURSE SEMANTICS
- **Learner operation:** identify A and B and explain B as contrastive/corrective relative to A.
- **Direct prerequisites:** analyzable propositions through K61.
- **Core exclusion:** mere particle recognition, ambiguous `لكن` function, concession/counterexpectation.
- **Architecture status:** DRAFT-FROZEN

## K63 — Result / Consequence
- **Canonical definition:** Mengenali relasi hasil/akibat antara dua proposisi Qurani melalui marker eksplisit yang tervalidasi, lalu menetapkan proposisi kedua sebagai hasil/konsekuensi dari proposisi pertama.
- **Primary domain:** DISCOURSE SEMANTICS
- **Learner operation:** identify directional relation `A → RESULT B`.
- **Direct prerequisites:** K58 plus proposition analysis through K62.
- **Core exclusion:** unfiltered `ف`, pure temporal sequence, conditional-response-only cases, tafsir-only inference.
- **Architecture status:** DRAFT-FROZEN

## K64 — Cause / Reason
- **Canonical definition:** Mengenali relasi sebab/alasan antara dua proposisi Qurani melalui marker eksplisit yang tervalidasi, lalu menentukan mana proposisi yang dijelaskan dan mana yang menjadi sebab/alasan.
- **Primary domain:** DISCOURSE SEMANTICS
- **Learner operation:** identify directional explanatory relation `A ← REASON B`.
- **Direct prerequisites:** proposition analysis through K63.
- **Core exclusion:** purpose/goal, conditional dependency, long tafsir-only inference.
- **Architecture status:** DRAFT-FROZEN

## K65 — Exception / Restriction with `إلا`
- **Canonical definition:** Mengenali relasi pengecualian/pembatasan melalui `إلا` eksplisit dengan menentukan domain yang dibatasi dan unsur yang dikecualikan/dikhususkan dalam konstruksi Qurani terkontrol.
- **Primary domain:** SCOPE / DISCOURSE SEMANTICS
- **Learner operation:** identify domain and excluded/restricted element.
- **Direct prerequisites:** local structure and proposition analysis through K64.
- **Core exclusion:** full `باب الاستثناء`, subtype classification, new post-`إلا` i‘rāb rules.
- **Architecture status:** DRAFT-FROZEN

## K66 — Purpose / Goal
- **Canonical definition:** Mengenali relasi tujuan/غاية antara suatu tindakan atau proposisi Qurani dan tujuan yang dinyatakan secara eksplisit melalui konstruksi yang tervalidasi.
- **Primary domain:** DISCOURSE SEMANTICS
- **Learner operation:** identify `ACTION/PROPOSITION A → PURPOSE B`.
- **Direct prerequisites:** proposition analysis through K65; previously mastered morphology/mood as needed.
- **Core exclusion:** hidden `أن` as a new operation, new naṣb mechanism, cause/result ambiguity.
- **Architecture status:** DRAFT-FROZEN

## K67 — Concession / Counterexpectation
- **Canonical definition:** Mengenali relasi konsesif/counterexpectation dalam konstruksi Qurani eksplisit dengan menentukan keadaan yang menimbulkan ekspektasi tertentu dan proposisi yang tetap berlaku meskipun keadaan tersebut.
- **Primary domain:** DISCOURSE SEMANTICS
- **Learner operation:** identify expectation-trigger A and proposition B that nevertheless holds.
- **Direct prerequisites:** proposition/discourse analysis through K66.
- **Core exclusion:** ordinary contrast, implicit rhetoric-only concession, nested concession, new conditional subtype as prerequisite.
- **Architecture status:** DRAFT-FROZEN

---

# Late-Ladder Dependency Skeleton

```text
K57
 ↓
K58 coordination
 ├─→ K59 temporal sequencing
 ├─→ K63 result/consequence
 └─→ supports later discourse relations

K60 relative-clause boundary
 ↓
K61 explicit resumptive reference

K62 contrast/correction
K63 result/consequence
K64 cause/reason
K65 exception/restriction
K66 purpose/goal
K67 concession/counterexpectation
```

Numeric order remains pedagogically useful, but it is **not identical to prerequisite structure**.

# Normalization Rules Confirmed

1. competency names describe learner operations, not chapter titles;
2. particles are evidence/markers, not automatically competencies;
3. one K targets one genuinely new operation;
4. subtype inventories remain mastery unless distinct cognition is demonstrated;
5. DRAFT-FROZEN locks competency identity but does not claim production-ready evidence maturity;
6. K67 remains provisional core endpoint pending final registry/dependency audit.

# Next consolidation task

Recover and normalize K1–K57 from their authoritative frozen source records. Do **not** reconstruct missing definitions from memory when the branch source cannot be retrieved reliably. After that, merge this file into `CANONICAL-REGISTRY-K1-K67-v0.1.md` and run neighbor-overlap audit.
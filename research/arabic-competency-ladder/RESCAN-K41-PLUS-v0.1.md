# Rescan K41+ v0.1

**Status:** WORKING RESEARCH — NON-AUTHORITATIVE  
**Baseline:** K1–K40 DRAFT-FROZEN.

## Purpose

Menentukan operasi struktural berikutnya yang paling ringan setelah K40, dengan aturan anti-inflasi: hanya operasi/category/relation yang benar-benar baru yang mendapatkan K baru.

## Candidate A — fa'il mustatir dasar

New operation:
- infer subjek yang tidak muncul sebagai token isim terpisah;
- gunakan morfologi fi'il dan konteks minimum untuk menentukan person/number/gender sejauh diperlukan.

Dependencies:
- K6/K7 verb recognition;
- K10 fi'il + fa'il zhahir;
- K15 attached-pronoun segmentation helps contrast overt vs bound morphology;
- K26 imperative recognition may provide familiar environments, but imperative subject analysis is not assumed.

Strength:
- sangat fundamental untuk membaca jumlah fi'liyyah Qurani;
- membuka banyak occurrence yang sebelumnya tertahan.

Burden:
- target bersifat inferensial, bukan token-level;
- mudah tercampur dengan suffix subject, attached object, dan omitted discourse subject.

**Judgement: VERY HIGH structural value; abstract but now prerequisite base is mature.**

## Candidate B — isim maushul + silah minimal

New operation:
- hubungkan isim maushul K23 dengan silah;
- tentukan boundary relatif minimal;
- pahami bahwa silah melengkapi referen tanpa menjadi khabar otomatis.

Dependencies:
- K23 relative-pronoun recognition;
- clause type inside silah must itself be <= current K.

Strength:
- sangat produktif dalam Qur'an;
- locality bisa cukup baik bila silah berupa verbal relation sederhana.

Burden:
- clause-boundary/linkage lebih berat daripada relation token-local;
- sering ada dhamir 'aid, PP, or embedded structure.

**Judgement: HIGH, but generally heavier than fa'il mustatir.**

## Candidate C — emphatic lām recognition/function

New operation:
- identify occurrence-validated emphatic lām and its emphasis relation.

Dependencies:
- especially useful after K38 `إنّ` construction.

Strength:
- local marker;
- unlocks many REVIEW-LAM examples.

Risk:
- many lām forms/functions are homographic; a broad “lam” K would violate atomicity.

**Judgement: HIGH only if narrowly defined as lām al-tawkīd/al-ibtidā' occurrence-specific.**

## Candidate D — simple conditional relation

Potentially `لو` or conditional `إنْ` + two clauses.

Dependencies:
- K36 `لو` recognition;
- clause competence on both sides.

Burden:
- protasis/apodosis linkage;
- mood/jazm for conditional `إنْ` may add another operation;
- semantic counterfactuality for `لو` is not trivial.

**Judgement: MODERATE-HIGH, later.**

## Candidate E — demonstrative phrase relation

K22 recognition exists and K24 already uses demonstrative as mubtada'. A separate construction such as `اسم إشارة + اسم معرف` must be grammar-audited because occurrences may be analyzed as badal/'athaf bayan or other appositional relation.

**Judgement: MODERATE until label consistency is proven.**

## Candidate F — expanded khabar types under nawāsikh

Examples: PP/clausal khabar under `إنّ`, `ليس`, `كان`.

This is better treated as **expansion of K38–K40** unless a genuinely new operation appears. Do not create a new K merely because the khabar surface type changes if that surface relation was already learned earlier.

## Head-to-head conclusion

The strongest distinct next operation is **fa'il mustatir**. At K1–K40, students already have enough explicit verbal and pronominal foundation to make hidden-subject inference pedagogically coherent.

Provisional sequence:
- **K41-CAND — fa'il mustatir dasar**
- **K42-CAND — isim maushul + silah minimal**
- **K43-CAND — occurrence-specific emphatic lām** if distinctness/evidence supports a separate K
- conditional relation later.

## K41 atomic definition

K41 must not mean “all hidden subjects”. Core target:

> Given a simple active verbal unit with no overt fa'il token, identify that the fi'il carries/entails a **basic mustatir subject**, and recover only the minimum person/number/gender information required by the occurrence.

Exclude from core:
- passive;
- ambiguous discourse-controlled ellipsis;
- complex coordination;
- nested clauses;
- cases where identifying the subject requires a later relative/conditional relation;
- full conjugational paradigm teaching.

## Next

Build occurrence-specific evidence gate K41 and compare clean yield against K42 before any freeze.
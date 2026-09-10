# L13 Canonical Repair Set — K31–K40 v1.0

**Status:** DRAFT CANONICAL REPAIR — NOT PRODUCTION ENABLED  
**Checkpoint:** L13  
**Canonical band:** K31–K40  
**Source of truth:** `CANONICAL-REGISTRY-K01-K67-v0.1.md`  
**Rule:** one primary new canonical operation per item; earlier competencies may appear only as prerequisites.

## K31 — REC-INT-HAMZA
### ARB-PL-L13-K31-R01-v1.0
- Reference: QS 94:1
- Span: `أَلَمْ نَشْرَحْ لَكَ صَدْرَكَ`
- Target: recognize interrogative hamzah and distinguish it from lexical hamzah.
- Prompt: identifikasi hamzah interrogatif pada awal span dan bedakan dari huruf yang merupakan bagian tetap dari akar/kata.
- Expected: initial `أَ` is the interrogative marker in `ألم`; no full rhetorical interpretation required.
- Response class: recognition/contrast
- Ambiguity: LOW
- production_enabled: false

## K32 — REC-QAD
### ARB-PL-L13-K32-R01-v1.0
- Reference: QS 23:1
- Span: `قَدْ أَفْلَحَ الْمُؤْمِنُونَ`
- Target: recognize validated `قد` occurrence without requiring full aspect semantics.
- Prompt: tunjukkan particle `قد` dan identifikasi bahwa ia berdiri sebelum verba; jangan menuntut penjelasan semantik aspektual rinci.
- Expected: `قد` correctly recognized as the target particle.
- Response class: recognition
- Ambiguity: LOW
- production_enabled: false

## K33 — REC-INNA
### ARB-PL-L13-K33-R01-v1.0
- Reference: QS 2:173
- Span: `إِنَّ اللَّهَ غَفُورٌ رَحِيمٌ`
- Target: recognize `إنّ` while government remains locked.
- Prompt: identifikasi operator `إنّ` saja; jangan beri kredit tambahan untuk i'rab اسمها وخبرها pada item ini.
- Expected: `إنّ` recognized as the target operator.
- Response class: operator recognition
- Ambiguity: LOW
- production_enabled: false

## K34 — REC-ILLA
### ARB-PL-L13-K34-R01-v1.0
- Reference: QS 47:19
- Span: `لَا إِلَٰهَ إِلَّا اللَّهُ`
- Target: recognize validated `إلا` without opening full exception/restriction analysis.
- Prompt: identifikasi particle `إلا`; scope exception/restriction belum dinilai pada K34.
- Expected: `إلا` recognized correctly.
- Response class: recognition/boundary
- Ambiguity: LOW
- production_enabled: false

## K35 — REC-LAYSA
### ARB-PL-L13-K35-R01-v1.0
- Reference: QS 95:8
- Span: `أَلَيْسَ اللَّهُ بِأَحْكَمِ الْحَاكِمِينَ`
- Target: recognize limited `ليس` family.
- Prompt: identifikasi bentuk `ليس` di dalam target tanpa menganalisis seluruh government atau fungsi `بـ`.
- Expected: `ليس` recognized within `أليس`.
- Response class: recognition
- Ambiguity: LOW
- production_enabled: false

## K36 — REC-LAW
### ARB-PL-L13-K36-R01-v1.0
- Reference: QS 59:21
- Span: `لَوْ أَنْزَلْنَا هَٰذَا الْقُرْآنَ عَلَىٰ جَبَلٍ`
- Target: recognize validated `لو` conditional/counterfactual marker.
- Prompt: identifikasi marker `لو`; jangan analisis keseluruhan condition-result structure.
- Expected: `لو` correctly recognized as the target marker.
- Response class: recognition/boundary
- Ambiguity: LOW
- production_enabled: false

## K37 — REC-KANA-FAMILY
### ARB-PL-L13-K37-R01-v1.0
- Reference: QS 4:96
- Span: `وَكَانَ اللَّهُ غَفُورًا رَحِيمًا`
- Target: recognize limited `كان` family.
- Prompt: identifikasi bentuk `كان` saja; analisis اسمها وخبرها ditahan untuk K40.
- Expected: `كان` recognized correctly.
- Response class: recognition/boundary
- Ambiguity: LOW
- production_enabled: false

## K38 — REL-INNA-CORE
### ARB-PL-L13-K38-R01-v1.0
- Reference: QS 2:173
- Span: `إِنَّ اللَّهَ غَفُورٌ رَحِيمٌ`
- Target: analyze simple `إنّ + اسمها + خبرها`.
- Prompt: petakan operator, اسم إنّ, dan khabar inti pada span. Jangan masuk ke tafsir sifat Allah.
- Expected: `إنّ` = operator; `الله` = اسم إنّ; `غفور` = core khabar, with `رحيم` treated according to the review-approved local analysis/rubric.
- Response class: transformed nominal predication
- Ambiguity: MEDIUM
- alternate_analysis_policy: rubric must explicitly state accepted treatment of `رحيم` and score the K38 core independently.
- production_enabled: false

## K39 — REL-LAYSA-PRED
### ARB-PL-L13-K39-R01-v1.0
- Reference: QS 3:113
- Span: `لَيْسُوا سَوَاءً`
- Target: analyze simple `ليس + اسمها + خبرها`.
- Prompt: identifikasi `ليس`, اسمها yang terealisasi sebagai pronoun plural pada bentuk verba, dan khabar overt.
- Expected: `ليس` = operator/copular negative; `واو الجماعة` = اسم ليس; `سواءً` = خبر ليس.
- Response class: transformed nominal predication
- Ambiguity: LOW
- production_enabled: false

## K40 — REL-KANA-CORE
### ARB-PL-L13-K40-R01-v1.0
- Reference: QS 4:96
- Span: `وَكَانَ اللَّهُ غَفُورًا رَحِيمًا`
- Target: analyze simple `كان + اسمها + خبرها`.
- Prompt: petakan `كان`, اسمها, dan khabar inti pada span tanpa menjadikan penjelasan makna sebagai bukti utama.
- Expected: `كان` = operator/copular verb; `الله` = اسم كان; `غفورًا` = core khabar, with `رحيمًا` handled under the review-approved local rubric.
- Response class: transformed nominal predication
- Ambiguity: MEDIUM
- alternate_analysis_policy: score the K40 core relation independently and document accepted treatment of the second adjective/predicate element.
- production_enabled: false

## Coverage audit

Canonical L13 band:
- K31 ✓
- K32 ✓
- K33 ✓
- K34 ✓
- K35 ✓
- K36 ✓
- K37 ✓
- K38 ✓
- K39 ✓
- K40 ✓

**Draft canonical target coverage: 10/10 = 100%.**

## Governance notes

1. Historical L13 replacement P01–P24 remain preserved as prerequisite/out-of-band diagnostic records; they are not counted as primary K31–K40 coverage.
2. K33 versus K38 and K37 versus K40 deliberately reuse the same verse family because the learner operation changes from recognition to relational analysis. Same-form assembly controls still apply.
3. K38 and K40 require Arabic-content review for the treatment of the second predicate/adjectival element so automated scoring does not impose an unnecessarily narrow i'rab.
4. K34 recognition of `إلا` must remain distinct from K65 exception/restriction scope analysis.
5. K36 recognition of `لو` must remain distinct from later full conditional architecture.

No item in this repair set is production-enabled until Arabic-content review, duplicate-function audit, item-quality review, pilot calibration, and registry promotion are complete.
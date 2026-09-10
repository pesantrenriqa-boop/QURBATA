# CANONICAL REGISTRY — K21–K33 v0.1

**Status:** CONSOLIDATION DRAFT — definitions preserved from frozen final gates  
**Sources:** `FINAL-GATE-K21-K23-v1.0.md`, `FINAL-GATE-K24-K25-v1.0.md`, `FINAL-GATE-K26-K27-v1.0.md`, `FINAL-GATE-K28-K29-v1.0.md`, `FINAL-GATE-K30-K31-v1.0.md`, `FINAL-GATE-K32-K33-v1.0.md`  
**Rule:** normalization only; no silent rename, merge, split, or scope expansion.

## K21 — REL-V-OBJ-PRON
- **Canonical competence:** dhamir muttashil sebagai maf'ul bih pada fi'il sederhana.
- **Primary domain:** clause / verbal argument structure.
- **Learner operation:** identify an attached pronoun as the direct object of an already-readable verb occurrence.
- **Hard prerequisites:** K14 + K15 + verbal foundation K6/K7/K10.
- **Exclusions:** possessive suffix; prepositional pronoun; subject/person morphology.
- **Architecture status:** DRAFT-FROZEN.

## K22 — REC-DEM
- **Canonical competence:** mengenali isim isyarah.
- **Primary domain:** recognition / nominal category.
- **Learner operation:** identify a demonstrative token/category without assigning its sentence-level function.
- **Exclusions:** demonstrative phrase analysis; badal/'athaf bayan; mubtada' use.
- **Architecture status:** DRAFT-FROZEN.

## K23 — REC-REL
- **Canonical competence:** mengenali isim maushul.
- **Primary domain:** recognition / nominal category.
- **Learner operation:** identify a relative-pronoun token/category.
- **Exclusions:** silah al-maushul; relative-clause boundary; relative reference dependency.
- **Architecture status:** DRAFT-FROZEN.

## K24 — REL-DEM-PRED
- **Canonical competence:** isim isyarah sebagai mubtada' dengan khabar nominal sederhana.
- **Primary domain:** clause / nominal predication.
- **Learner operation:** identify an already-recognized demonstrative as mubtada' and connect it to a simple nominal predicate.
- **Hard prerequisites:** K22 + K8 + nominal features K1–K3 as required by evidence.
- **Exclusions:** demonstrative phrase/apposition; PP predicate as a new relation; clausal predicate.
- **Architecture status:** DRAFT-FROZEN.

## K25 — REL-V-PP
- **Canonical competence:** jar–majrur sebagai attachment/pelengkap fi'il sederhana.
- **Primary domain:** clause / verbal attachment.
- **Learner operation:** attach a previously mastered PP to a simple verb occurrence.
- **Hard prerequisites:** K9 + K10 + K6/K7.
- **Exclusions:** noun/adjective attachment; ambiguous PP scope; new object/complement/clause structures.
- **Architecture status:** DRAFT-FROZEN WITH STRICT EVIDENCE TAGGING.

## K26 — REC-V-IMP
- **Canonical competence:** mengenali fi'il amr sederhana pada occurrence Qurani tervalidasi.
- **Primary domain:** morphology / verb-form recognition.
- **Learner operation:** identify an imperative verb occurrence without analyzing its hidden subject.
- **Prior basis:** verbal recognition K6/K7.
- **Exclusions:** fa'il mustatir analysis; object suffix as a new target; weak-verb complexity; derivational detail.
- **Architecture status:** DRAFT-FROZEN.

## K27 — REC-NEG
- **Canonical competence:** mengenali fungsi negatif dasar pada partikel nafi dengan occurrence-specific tagging.
- **Primary domain:** particle/function recognition.
- **Learner operation:** identify a particle occurrence as functioning negatively.
- **Exclusions:** unified governance of `لا`, `ما`, `لم`, `لن`; jazm; nasb; `لا النافية للجنس`; later governing effects.
- **Architecture status:** DRAFT-FROZEN.

## K28 — REC-INT-HAL
- **Canonical competence:** mengenali `هَلْ` sebagai penanda istifham pada occurrence yang tervalidasi.
- **Primary domain:** particle/function recognition.
- **Learner operation:** identify `هل` as an interrogative marker.
- **Exclusions:** full interrogative-clause analysis; interrogation scope.
- **Architecture status:** DRAFT-FROZEN.

## K29 — REC-VOC-YA
- **Canonical competence:** mengenali `يَا` sebagai penanda nida' pada occurrence yang tervalidasi.
- **Primary domain:** particle/function recognition.
- **Learner operation:** identify `يا` as a vocative marker.
- **Exclusions:** types of munada; i'rab munada; `يا أيها` construction as a new structure.
- **Architecture status:** DRAFT-FROZEN.

## K30 — REC-FUT
- **Canonical competence:** mengenali future marker `سوف / سـ` pada fi'il mudhari' yang tervalidasi.
- **Primary domain:** morphology/particle recognition.
- **Learner operation:** identify and, for `سـ`, correctly segment an overt future marker on an already-recognized mudhari'.
- **Hard prerequisite:** K7.
- **Exclusions:** detailed tense/aspect interpretation; rhetorical future semantics.
- **Architecture status:** DRAFT-FROZEN.

## K31 — REC-INT-HAMZA
- **Canonical competence:** mengenali hamzah istifham `أَ` pada occurrence yang tervalidasi.
- **Primary domain:** particle/function recognition.
- **Learner operation:** distinguish interrogative hamzah from lexical initial hamzah.
- **Exclusions:** interrogation scope; hamzah taswiyah and specialized functions.
- **Architecture status:** DRAFT-FROZEN.

## K32 — REC-QAD
- **Canonical competence:** recognition `قَدْ` pada occurrence Qurani tervalidasi.
- **Primary domain:** particle recognition.
- **Learner operation:** identify the token/function occurrence of `قد` without opening its aspectual semantics.
- **Exclusions:** taqrib, tahqiq, and broader aspectual interpretation.
- **Architecture status:** DRAFT-FROZEN.

## K33 — REC-INNA
- **Canonical competence:** recognition `إِنَّ` pada occurrence Qurani tervalidasi.
- **Primary domain:** particle/operator recognition.
- **Learner operation:** identify `إنّ` as a token/operator while its government remains locked.
- **Required metadata:** `governing_effect_locked = true`; `ism_inna_analysis_unlocked_at = later`; `khabar_inna_analysis_unlocked_at = later`.
- **Exclusions:** analysis of `اسم إنّ`; analysis of `خبر إنّ`; governing effect as a target.
- **Architecture status:** DRAFT-FROZEN WITH LOCKED GOVERNMENT.

## Dependency / parallelism notes

- K22 and K23 are parallel recognition nodes; K23 does not linguistically depend on K22.
- K28 and K29 are parallel low-dependency marker-recognition nodes.
- K30 depends directly on K7; K31 is a separate interrogative-recognition path.
- K32 precedes K33 by pedagogical linearization and lower latent grammar burden, not because K33 depends on K32.
- K24 integrates K22 with prior nominal predication; K25 integrates K9 with prior verbal structure.

## Consolidation verdict

K21–K33 are now normalized into canonical registry records without changing the frozen research definitions. Next extraction batch: K34–K46.
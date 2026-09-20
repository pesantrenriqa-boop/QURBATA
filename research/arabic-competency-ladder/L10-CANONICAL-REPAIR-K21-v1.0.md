# L10 Canonical Repair — K21 v1.0

**Status:** DRAFT CANONICAL REPAIR — NOT PRODUCTION ENABLED  
**Checkpoint:** L10  
**Canonical target:** K21 `REL-V-OBJ-PRON`  
**Canonical operation:** identify an attached pronoun as direct object of a verb.  
**Prerequisites:** K14 + K15.

## K21-R01 — overt verb + attached object pronoun

- Candidate ID: `ARB-PL-L10-K21-R01-v1.0`
- Qur'an reference: QS 93:7
- Target span: `فَهَدَىٰكَ`
- Target segmentation: `هَدَىٰ + كَ`
- Prompt: segmentasikan bentuk target menjadi verba dan dhamir muttashil, lalu tentukan fungsi lokal dhamir tersebut terhadap verba. Jangan menilai tafsir ayat.
- Expected response: `هدى` is the verb host; `ك` is an attached pronoun functioning as the direct object of the verb.
- Response class: relation-local / argument structure
- Ambiguity: LOW
- Critical distinction: attached pronoun on a verb is not automatically possessive; here `ك` is the verbal object.
- Error codes:
  - `E-K21-NO-SEGMENT` — fails to separate verb and pronoun.
  - `E-K21-POSS` — misclassifies `ك` as possessive/genitive.
  - `E-K21-SUBJ` — misclassifies `ك` as subject.
  - `E-K21-TRANSLATION-ONLY` — gives translation without structural relation.
- Scoring:
  - 1 point: correct segmentation.
  - 1 point: correct attached-pronoun recognition (K15 prerequisite).
  - 1 point: correct direct-object relation (K21 target).
- production_enabled: false

## Canonical coverage decision

This candidate directly instantiates K21 without requiring sentence-level operations above the checkpoint ceiling. It therefore closes the missing **draft canonical coverage** slot for L10.

### L10 K13–K30 draft coverage after this repair

- K13 ✓
- K14 ✓
- K15 ✓
- K16 ✓
- K17 ✓
- K18 ✓
- K19 ✓
- K20 ✓
- K21 ✓ — this repair
- K22 ✓
- K23 ✓
- K24 ✓
- K25 ✓
- K26 ✓
- K27 ✓
- K28 ✓
- K29 ✓
- K30 ✓

**Draft canonical target coverage: 18/18 = 100%.**

This is coverage completeness only, not production readiness. Remaining gates: Arabic-content review, occurrence/function verification, duplicate-function audit, item-quality review, pilot calibration, and registry promotion.
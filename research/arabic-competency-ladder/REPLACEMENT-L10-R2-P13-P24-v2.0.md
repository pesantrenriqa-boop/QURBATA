# L10 R2 Replacement — P13–P24 v2.0

**Status:** DRAFT-REPLACEMENT — NOT PRODUCTION ENABLED  
**Checkpoint:** L10  
**Recovery class:** R2 SUMMARY-ONLY → VERSIONED REPLACEMENT  
**Guardrail:** morphology and phrase-level operations only; sentence-relation mastery L11+ is excluded from required scoring.

## P13 — attached object-pronoun decomposition
- Canonical ID: `ARB-PL-L10-P013-v2.0`
- Reference: QS 1:5
- Span: `نَعْبُدُ`
- Task: compare with a supplied form containing an attached object pronoun and identify attachment morphology only.
- Response class: contrast/decomposition
- Ambiguity: LOW
- production_enabled: false

## P14 — preposition + plural pronoun
- Canonical ID: `ARB-PL-L10-P014-v2.0`
- Reference: QS 1:7
- Span: `عَلَيْهِمْ`
- Task: segment `على` and plural attached pronoun; identify number information without clause parsing.
- Expected: preposition + `هم`, plural pronoun.
- Response class: decomposition
- Ambiguity: LOW
- production_enabled: false

## P15 — idafah transfer
- Canonical ID: `ARB-PL-L10-P015-v2.0`
- Reference: QS 114:1
- Span: `رَبِّ النَّاسِ`
- Task: identify local idafah pair.
- Expected: `رب` mudaf; `الناس` mudaf ilayh.
- Response class: transfer
- Ambiguity: LOW
- production_enabled: false

## P16 — adjective agreement observation
- Canonical ID: `ARB-PL-L10-P016-v2.0`
- Reference: QS 9:72
- Span: `الْفَوْزُ الْعَظِيمُ`
- Task: identify noun–adjective pair and name visible agreement features that are safe at L10.
- Expected: both definite; local noun/adjective pairing recognized; no sentence predication required.
- Response class: morphology/phrase
- Ambiguity: MEDIUM
- production_enabled: false

## P17 — dual morphology transfer
- Canonical ID: `ARB-PL-L10-P017-v2.0`
- Reference: QS 55:17
- Span: `رَبُّ الْمَشْرِقَيْنِ وَرَبُّ الْمَغْرِبَيْنِ`
- Task: identify the two dual forms only; do not require coordination analysis.
- Expected: `المشرقين`, `المغربين` dual.
- Response class: transfer/boundary
- Ambiguity: LOW
- production_enabled: false

## P18 — sound masculine plural recognition
- Canonical ID: `ARB-PL-L10-P018-v2.0`
- Reference: QS 2:3
- Span: `يُؤْمِنُونَ`
- Task: identify plural verbal morphology visible in the target form at the assigned ceiling.
- Expected: plural participant morphology recognized.
- Response class: morphology transfer
- Ambiguity: MEDIUM
- production_enabled: false

## P19 — feminine noun morphology transfer
- Canonical ID: `ARB-PL-L10-P019-v2.0`
- Reference: QS 99:1
- Span: `الْأَرْضُ`
- Task: classify the noun and state whether grammatical gender can always be inferred solely from a visible ta marbutah.
- Expected: noun is feminine lexically; absence of ta marbutah shows visible suffix is not the only gender cue.
- Response class: contrast/boundary
- Ambiguity: MEDIUM
- production_enabled: false

## P20 — definite article versus attached element
- Canonical ID: `ARB-PL-L10-P020-v2.0`
- Reference: QS 17:81
- Span: `الْحَقُّ`
- Task: identify `الـ` and distinguish it from attached pronoun morphology.
- Expected: definite article; not pronoun.
- Response class: contrast
- Ambiguity: LOW
- production_enabled: false

## P21 — phrase segmentation with preposition
- Canonical ID: `ARB-PL-L10-P021-v2.0`
- Reference: QS 3:160
- Span: `لَكُمْ`
- Task: segment the form into prepositional element and attached plural pronoun.
- Expected: `لـ` + `كم`.
- Response class: decomposition/transfer
- Ambiguity: LOW
- production_enabled: false

## P22 — multi-feature local analysis
- Canonical ID: `ARB-PL-L10-P022-v2.0`
- Reference: QS 110:1
- Span: `نَصْرُ اللَّهِ`
- Task: identify definiteness information and idafah structure without analyzing its role in the larger sentence.
- Expected: local idafah recognized; sentence role excluded.
- Response class: integration-lite
- Ambiguity: LOW
- production_enabled: false

## P23 — prerequisite integrity probe
- Canonical ID: `ARB-PL-L10-P023-v2.0`
- References: QS 1:7 / QS 114:1
- Spans: `عَلَيْهِمْ` / `رَبِّ النَّاسِ`
- Task: complete one pronoun decomposition and one idafah analysis. A correct translation alone earns no structural credit.
- Expected: both local operations correct.
- Response class: prerequisite/integration
- Ambiguity: LOW
- scoring: segmented.
- production_enabled: false

## P24 — L10 R2 final discriminator
- Canonical ID: `ARB-PL-L10-P024-v2.0`
- References: QS 2:3; QS 55:17; QS 3:160
- Task: identify (a) one plural verbal marker, (b) one dual form, and (c) one preposition + attached pronoun. Do not assign sentence roles.
- Expected: correct morphology/phrase operations across three different Qur'anic environments.
- Response class: cross-span transfer
- Ambiguity: LOW
- scoring: segmented 3-part rubric.
- production_enabled: false

## Completion audit

L10 R2 replacement coverage:
- P01–P12: batch 01
- P13–P24: this batch

**R2 replacement coverage: 24/24 = 100%.**

Next gates: canonical K-ID alignment against the authoritative K13–K30 definitions, duplicate-function audit against surviving L10 P25–P36, Arabic-content review, quality disposition, and registry normalization. No replacement item is production-enabled.
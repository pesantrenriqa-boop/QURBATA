# L13 R2 Replacement — P13–P24 v2.0

**Status:** DRAFT-REPLACEMENT — NOT PRODUCTION ENABLED  
**Checkpoint:** L13  
**Recovery class:** R2 SUMMARY-ONLY → VERSIONED REPLACEMENT  
**Stage:** S3 — Sentence Relations  
**Guardrail:** sentence-relation operations only; K40+ complex-clause integration is excluded from required scoring.

## P13 — nominal predication transfer
- Canonical ID: `ARB-PL-L13-P013-v2.0`
- Target relation: nominal predication
- Reference: QS 112:2
- Span: `اللَّهُ الصَّمَدُ`
- Task: identify the two nominal elements and state the predicative relation at the L13 ceiling.
- Expected: nominal predication recognized without extended i'rab.
- Response class: transfer
- Ambiguity: LOW
- production_enabled: false

## P14 — verbal subject transfer
- Canonical ID: `ARB-PL-L13-P014-v2.0`
- Target relation: verb–subject
- Reference: QS 54:1
- Span: `اقْتَرَبَتِ السَّاعَةُ`
- Task: identify the verbal predicate and the overt subject relation.
- Expected: `اقتربت` verbal predicate; `الساعة` subject relation.
- Response class: transfer
- Ambiguity: LOW
- production_enabled: false

## P15 — object-fronting relation
- Canonical ID: `ARB-PL-L13-P015-v2.0`
- Target relation: verb–object under fronting
- Reference: QS 1:5
- Span: `إِيَّاكَ نَعْبُدُ`
- Task: map the fronted object to its verb; do not require rhetorical interpretation.
- Expected: `إياك↔نعبد` object relation retained despite surface order.
- Response class: transfer/contrast
- Ambiguity: LOW
- production_enabled: false

## P16 — coordination relation transfer
- Canonical ID: `ARB-PL-L13-P016-v2.0`
- Target relation: coordination
- Reference: QS 17:81
- Span: `جَاءَ الْحَقُّ وَزَهَقَ الْبَاطِلُ`
- Task: identify two local verbal relations and the coordinator.
- Expected: `جاء↔الحق`; `زهق↔الباطل`; `و` coordinates the two units.
- Response class: integration-lite
- Ambiguity: LOW
- production_enabled: false

## P17 — demonstrative local relation
- Canonical ID: `ARB-PL-L13-P017-v2.0`
- Target relation: demonstrative–nominal association
- Reference: QS 2:2
- Span: `ذَٰلِكَ الْكِتَابُ`
- Task: identify the demonstrative and the nominal element associated with it without choosing a single full-sentence i'rab.
- Expected: `ذلك` demonstrative; `الكتاب` nominal element in the local construction.
- Response class: local relation/boundary
- Ambiguity: MEDIUM
- alternate_analysis_policy: full i'rab outside scored target.
- production_enabled: false

## P18 — relative head–silah transfer
- Canonical ID: `ARB-PL-L13-P018-v2.0`
- Target relation: relative head to silah
- Reference: QS 107:1
- Span: `الَّذِي يُكَذِّبُ`
- Task: identify the relative head and the verbal material that completes the local relative unit.
- Expected: `الذي` relative head; `يكذب` inside silah.
- Response class: transfer
- Ambiguity: LOW
- production_enabled: false

## P19 — fronted prepositional predication
- Canonical ID: `ARB-PL-L13-P019-v2.0`
- Target relation: fronted predicate relation
- Reference: QS 45:36
- Span: `لِلَّهِ الْحَمْدُ`
- Task: identify the fronted prepositional element and the nominal element related to it at the L13 ceiling.
- Expected: `لله` fronted predicative element; `الحمد` nominal counterpart.
- Response class: transfer
- Ambiguity: LOW
- production_enabled: false

## P20 — morphology versus relation discriminator
- Canonical ID: `ARB-PL-L13-P020-v2.0`
- Target relation: sentence-relation integrity
- Reference: QS 17:81
- Span: `جَاءَ الْحَقُّ`
- Task: if a learner can label `جاء` as a past verb and `الحق` as a noun but cannot state their relation, has the L13 target been demonstrated?
- Expected: no; form recognition alone does not prove sentence-relation mastery.
- Response class: negative/contrast
- Ambiguity: LOW
- production_enabled: false

## P21 — subject versus object discrimination
- Canonical ID: `ARB-PL-L13-P021-v2.0`
- Target relation: subject/object contrast
- References: QS 54:1 / QS 96:2
- Spans: `اقْتَرَبَتِ السَّاعَةُ` / `خَلَقَ الْإِنسَانَ`
- Task: identify which noun is the subject relation in the first span and which noun is the object relation in the second.
- Expected: `الساعة` subject relation; `الإنسان` object relation.
- Response class: cross-span contrast
- Ambiguity: LOW
- production_enabled: false

## P22 — relative relation with object inside silah
- Canonical ID: `ARB-PL-L13-P022-v2.0`
- Target relation: relative + embedded local object relation
- Reference: QS 107:2
- Span: `الَّذِي يَدُعُّ الْيَتِيمَ`
- Task: identify the relative head and the local verb–object relation inside the silah; do not analyze a wider clause.
- Expected: `الذي` relative head; `يدع↔اليتيم` local object relation inside silah.
- Response class: integrative relation
- Ambiguity: MEDIUM
- ceiling_note: stop at the local relative unit; no K40+ clause integration.
- production_enabled: false

## P23 — prerequisite routing probe
- Canonical ID: `ARB-PL-L13-P023-v2.0`
- References: QS 112:2; QS 17:81; QS 1:5
- Task: complete one nominal relation, one verb–subject relation, and one fronted object relation. If one relation fails, route diagnosis locally rather than giving holistic credit.
- Expected: three relation types independently correct.
- Response class: prerequisite/integration
- Ambiguity: LOW
- scoring: segmented 3-part rubric.
- production_enabled: false

## P24 — L13 R2 final discriminator
- Canonical ID: `ARB-PL-L13-P024-v2.0`
- References: QS 2:2; QS 107:2; QS 45:36
- Task: identify (a) a demonstrative local relation, (b) a relative-unit relation with a local verb–object pair, and (c) fronted prepositional predication. Do not perform complex-clause or discourse analysis.
- Expected: all three sentence-relation operations correct with explicit relation evidence.
- Response class: cross-span transfer/integration
- Ambiguity: MEDIUM
- scoring: segmented.
- production_enabled: false

## Completion audit

L13 R2 replacement coverage:
- P01–P12: batch 01
- P13–P24: this batch

**R2 replacement coverage: 24/24 = 100%.**

Across the full five-checkpoint bank, all previously known summary-only recovery debt is now covered by explicit versioned replacements or by R0 full records. Next gates: authoritative K-ID alignment, consolidated registry normalization, duplicate-function audit, Arabic-content review, final quality disposition, pilot/psychometric validation, and production enablement.
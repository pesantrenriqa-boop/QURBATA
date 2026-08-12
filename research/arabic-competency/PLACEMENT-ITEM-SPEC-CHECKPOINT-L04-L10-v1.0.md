# Placement Item Specification — Checkpoint L04 & L10 v1.0

Status: WORKING VALIDATED
Scope: Arabic competency K01–K30 / Stage 1–2
Architecture: 5 stages / 21 levels / 65 canonical competencies

## 1. Purpose
This specification operationalizes the adaptive placement blueprint at the first two major checkpoints: L04 and L10. It does not change canonical K01–K65 or the frozen stage architecture.

## 2. Universal item schema
Each item record MUST contain:
- item_id
- checkpoint
- target_level
- target_K
- prerequisite_K
- Quran_reference
- target_span
- response_class
- item_role: DIRECT | NEGATIVE_CONTROL | PREREQUISITE | TRANSFER | INTEGRATIVE
- prompt
- expected_response
- scoring_key
- critical_misconception
- feature_ceiling
- ambiguity_flag
- manual_review_rule

No item may require a grammatical feature above the target level to obtain the correct answer.

## 3. L04 checkpoint — Stage 1 exit
Purpose: establish whether the learner can leave Foundation Recognition without hidden gaps in K01–K12.

Core six-item composition:
1. L04-D1 — direct target discriminator: identify/classify a Stage-1 target feature in a minimal Qur'anic span.
2. L04-D2 — second direct discriminator using a different lexical occurrence.
3. L04-N1 — negative/contrast control: distinguish target from a visually or lexically similar non-target.
4. L04-P1 — prerequisite-integrity probe covering an earlier K dependency.
5. L04-T1 — transfer item using a Qur'anic occurrence not used in instruction/demo.
6. L04-I1 — integrative discriminator combining two already-permitted Stage-1 features without introducing Stage-2 reasoning.

Mastery routing (provisional):
- PASS: >=5/6, prerequisite correct, transfer correct, no critical misconception.
- BORDERLINE: 4/6 OR prerequisite/transfer failure without broad collapse -> local diagnostic 3–5 items.
- FAIL: <=3/6 OR repeated critical misconception -> diagnose L01–L04 only.

Feature ceiling: an L04 answer must be recoverable using K01–K12 only.

## 4. L10 checkpoint — Stage 2 exit
Purpose: establish controlled morphosyntactic mastery through K30 and readiness for sentence-relation analysis.

Core six-item composition:
1. L10-D1 — direct morphosyntactic classification.
2. L10-D2 — direct relation/form discriminator from a second independent occurrence.
3. L10-N1 — negative control separating a Stage-2 form/relation from a confusable construction.
4. L10-P1 — prerequisite-integrity probe sampled from L05–L09 dependency chain.
5. L10-T1 — unseen Qur'anic transfer occurrence requiring the same operation, not memorized wording.
6. L10-I1 — integrative item combining two or more K13–K30 features while remaining below Stage-3 relation complexity.

Mastery routing (provisional):
- PASS: >=5/6 + prerequisite + transfer + no critical misconception.
- BORDERLINE: 4/6 or isolated prerequisite/transfer failure -> diagnose L05–L10.
- FAIL: <=3/6 or systematic morphology/syntax confusion -> locate lowest unstable band inside L05–L10.

## 5. Scoring model
Each core item = 1 evidence unit. Raw total is not sufficient for placement.
Required dimensions:
- target accuracy
- prerequisite integrity
- transfer validity
- misconception severity
- consistency across independent occurrences

A learner may not accelerate solely because of a high raw score if prerequisite integrity fails.

## 6. Error taxonomy
E01 lexical guessing
E02 form recognition error
E03 morphological-feature error
E04 syntactic-role confusion
E05 target/non-target contrast failure
E06 prerequisite gap
E07 transfer failure
E08 answer correct but reasoning exceeds feature ceiling
E09 ambiguous occurrence / item defect

E08 and E09 trigger item review rather than automatic learner penalty when the item itself is responsible.

## 7. Quran evidence control
Item construction should use independently verified Qur'anic occurrences. Morphological and syntactic labels may be cross-checked against Quranic Arabic Corpus dependency/i'rab annotation. Corpus labels are evidence controls, not substitutes for pedagogical judgment.

## 8. Item-bank production gates
Before an item becomes PILOT_READY:
- target K and prerequisite K are explicit;
- answer is uniquely recoverable within feature ceiling;
- target span is minimal;
- at least one plausible distractor maps to a known misconception;
- Qur'an reference is verified;
- ambiguity flag is resolved or manual-review rule exists;
- no higher-level feature is necessary to answer.

## 9. Pilot bank target
For each checkpoint produce at minimum:
- 12 direct items
- 6 negative controls
- 6 prerequisite probes
- 6 transfer items
- 6 integrative items
Total minimum pool per checkpoint: 36 items.

The live adaptive form selects six core items from this pool according to role constraints, allowing alternate forms and retest without reusing identical items.

## 10. Next production step
Build verse-level pilot bank for L04 first, then L10, using the canonical K-to-level mapping. Every item receives an immutable item_id and version so RIQA OS can later record exposure, response, error class, mastery evidence, and retest eligibility.

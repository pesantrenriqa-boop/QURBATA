# ADAPTIVE PLACEMENT TEST BLUEPRINT L01-L21 v1.0

Status: FIRST-PASS / PRE-FREEZE
Scope: 65 canonical Arabic competencies, 5 stages, 21 levels

## 1. Purpose
Placement is diagnostic and competency-based. It must locate the highest defensible entry level while preserving prerequisite integrity. Raw percentage alone may not determine placement.

## 2. Routing spine
Primary checkpoints: L04 -> L10 -> L13 -> L19 -> L21.

Routing principle:
- PASS checkpoint: move upward to next checkpoint.
- BORDERLINE: administer local diagnostic probes around the checkpoint.
- FAIL: descend only within the relevant level band; do not reset automatically to L01.
- Apparent high-level PASS must still survive prerequisite-integrity probes.

## 3. Item architecture per checkpoint
Each checkpoint packet uses 6 scored core items plus optional diagnostic probes:
1. two direct target items;
2. one contrast/negative-control item;
3. one prerequisite-integrity item;
4. one transfer item using a new Qur'anic occurrence;
5. one integrative discriminator.

Maximum first routing spine = 30 scored items if all five checkpoints are administered. Adaptive branching normally reduces this substantially.

## 4. Response-operation progression
L01-L04: recognition/classification.
L05-L10: classification + controlled relation.
L11-L13: relation + contrast.
L14-L19: relation + reconstruction + clause analysis.
L20-L21: integration + transfer across authentic Qur'anic structures.

## 5. Provisional mastery gate
Checkpoint PASS requires all of:
- >= 5/6 core items correct;
- prerequisite-integrity item correct;
- transfer item correct;
- no critical misconception flag.

BORDERLINE:
- 4/6, or
- 5/6 with prerequisite/transfer failure.
Action: 3-5 local diagnostic probes.

FAIL:
- <=3/6, or repeated critical misconception.
Action: descend to local band diagnosis.

These thresholds are provisional until item calibration/pilot data exist; they are not yet psychometrically final cut scores.

## 6. Local diagnosis bands
After checkpoint failure, diagnose only the implicated band:
- L04 failure -> L01-L04
- L10 failure -> L05-L10
- L13 failure -> L11-L13
- L19 failure -> L14-L19
- L21 failure -> L20-L21

Use binary search where prerequisite ordering permits; otherwise use adjacent-level probes.

## 7. Acceleration rule
A learner may skip instructional levels when mastery is demonstrated. Acceleration requires:
- checkpoint pass;
- prerequisite integrity;
- successful transfer to an unseen Qur'anic example;
- no unresolved critical misconception.
High S4/S5 placements may be flagged for teacher confirmation when reconstruction/semantic ambiguity is material.

## 8. Remediation and retest
Placement output must include:
- recommended entry level;
- mastered level band;
- unresolved K IDs;
- misconception/error codes;
- remediation targets;
- retest eligibility.
Retest uses parallel items, not the same memorized occurrence.

## 9. Item metadata required for RIQA OS
Each item must carry:
item_id, K_id(s), level_id, stage_id, checkpoint_id, Qur'an reference, target span, operation type, prerequisite tags, positive/negative-control flag, transfer flag, answer key, rationale, distractor/error codes, ambiguity/manual-review flag, evidence maturity, difficulty/calibration fields, version/status.

## 10. Safety against false placement
Do not infer mastery from translation familiarity alone. Do not let one advanced item compensate for prerequisite failure. Do not auto-score structurally ambiguous reconstruction items unless the accepted analysis is uniquely constrained by the evidence standard.

## 11. Pilot bank target
Before operational deployment, build at least:
- 3 parallel forms per checkpoint core slot;
- local diagnostic probes for every L01-L21;
- positive and negative controls;
- unseen transfer items;
- teacher-review items for high-layer ambiguity.

## 12. Freeze gate for 21-level architecture
The 5-stage/21-level model may be FINAL-FROZEN after:
1. all L01-L21 have observable discriminators;
2. checkpoint routing covers all bands;
3. no prerequisite inversion is found;
4. L20-L21 workload remains integrative rather than overloaded;
5. pilot blueprint can place, remediate, retest, and accelerate without requiring 65 flat items.

## 13. Current decision
Architecture remains 5 stages / 21 levels / 65 competencies. This blueprint advances placement architecture to a testable pre-pilot state. Next artifact: checkpoint item specification and first operational item bank, beginning L04 and L10.
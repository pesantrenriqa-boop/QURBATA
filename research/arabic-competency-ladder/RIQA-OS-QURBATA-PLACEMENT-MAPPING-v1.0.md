# RIQA OS / QURBATA Placement Mapping v1.0

**Status:** ARCHITECTURE MAPPING — NON-PRODUCTION

## 1. Purpose

Menghubungkan canonical competency ladder K01–K65, 21 levels, five placement checkpoints, 180-item pilot bank, QURBATA remediation content, dan RIQA OS learner state tanpa mencampur fungsi masing-masing layer.

## 2. Canonical separation

- K01–K65 = competency truth layer.
- L01–L21 = pedagogical/placement progression layer.
- L04/L10/L13/L19/L21 = adaptive checkpoint layer.
- placement items = diagnostic evidence layer.
- QURBATA = instructional/remediation delivery layer.
- RIQA OS = orchestration, state, routing, reporting layer.

No layer may redefine the canonical competency meaning locally.

## 3. RIQA OS learner state

Minimum state per learner:
- `highest_confirmed_level`
- `current_learning_level`
- `mastered_k[]`
- `suspected_gap_k[]`
- `placement_checkpoint_history[]`
- `item_response_history[]`
- `error_code_profile`
- `remediation_assignments[]`
- `acceleration_eligible`
- `manual_review_flag`

## 4. Adaptive placement flow

1. Start from checkpoint routing appropriate to intake context.
2. Assemble six-item form from production-enabled registry.
3. Evaluate score + prerequisite integrity + transfer + critical misconceptions.
4. PASS → move upward to next checkpoint or confirm band.
5. BORDERLINE → draw 3–5 local diagnostic items.
6. FAIL → route only to relevant lower band unless prerequisite probes show deeper gaps.
7. At L21, pass still requires prerequisite integrity; capstone success alone cannot hide foundation gaps.

## 5. Checkpoint routing

- L04 failure diagnostics → L01–L04.
- L10 failure diagnostics → L05–L10, with lower-stage fallback only when prerequisites fail.
- L13 failure diagnostics → L11–L13.
- L19 failure diagnostics → L14–L19.
- L21 failure diagnostics → L20–L21 plus targeted lower prerequisite diagnostics when indicated.

## 6. Error-to-remediation mapping

Error codes are not merely labels. RIQA OS maps each error to:
- suspect competency;
- recommended QURBATA lesson/page cluster;
- practice type;
- minimum corrective evidence;
- retest eligibility.

Examples:
- recognition/classification error → focused recognition practice;
- relation confusion → contrastive parsing practice;
- prerequisite gap → return to prerequisite K cluster;
- transfer failure → novel Qur'anic examples at same ceiling;
- ambiguity/scoring defect → manual review, not learner penalty.

## 7. QURBATA mapping rule

A QURBATA unit may teach or remediate several related K, but every unit should publish:
- `target_k[]`
- `prerequisite_k[]`
- `max_feature_ceiling`
- `practice_operations[]`
- `mastery_evidence`
- `placement_relevance`

QURBATA page/lesson number is never treated as the competency identity itself.

## 8. Acceleration

Learners may skip instructional units when placement provides sufficient evidence of mastery. Acceleration must not skip unresolved prerequisite gaps. RIQA OS records skipped instructional content separately from mastered competencies.

## 9. Retest

Retest must draw alternate item IDs and preferably alternate Qur'anic references while preserving the same target operation. Repeating identical items is not valid evidence of transfer.

## 10. Manual review triggers

Automatic placement pauses when:
- high-ambiguity item is decisive;
- alternate analysis is plausible but rubric incomplete;
- learner pattern is internally inconsistent;
- suspected item defect appears;
- capstone answer is semantically strong but structurally contradictory.

## 11. Data contract to production

RIQA OS may consume an item only when registry fields include:
- immutable item ID/version;
- reviewed target K;
- production_enabled=true;
- scoring rubric;
- routing metadata;
- remediation mapping;
- source provenance.

## 12. Next implementation packages

1. quality-screen 180 items;
2. create reviewed machine-readable registry;
3. map each K to QURBATA remediation cluster;
4. define RIQA OS database/API tables;
5. run adaptive placement simulation with synthetic learner profiles;
6. pilot with human learners before final cut-score freeze.
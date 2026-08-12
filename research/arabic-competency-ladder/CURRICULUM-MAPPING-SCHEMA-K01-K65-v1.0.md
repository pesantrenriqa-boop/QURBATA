# CURRICULUM MAPPING SCHEMA — K01–K65 v1.0

Status: ACTIVE / FORMAL MAPPING WORKSTREAM
Architecture: K01–K65 FROZEN
Evidence baseline: 45.23% verified; all K minimum E2; 17 K at E3.

## Purpose
Translate the frozen linguistic competency ladder into a curriculum engine without changing competency definitions or allowing later structures to leak into earlier instructional examples.

## Mapping dimensions
Every K01–K65 record will receive these fields:
1. Competency ID
2. Frozen competency statement
3. Linguistic domain
4. Prerequisite K IDs
5. Instructional stage
6. RIQA/QURBATA level band
7. Entry observable
8. Mastery observable
9. Qur'anic evidence maturity (E2/E3/...)
10. Allowed example ceiling
11. Forbidden later-feature leakage
12. Teaching operation
13. Practice operation
14. Assessment operation
15. Placement-test observability
16. Remediation route
17. Acceleration route
18. QURBATA module/page target
19. RIQA OS state/event
20. Governance/status note

## Stage architecture — provisional mapping layer
The stage layer does NOT renumber K01–K65. It groups the frozen ladder for instruction.

### S1 — Foundation Recognition
Goal: identify foundational forms/categories with minimal syntactic load.
Rule: examples may contain only already-mastered or non-target background features that do not need learner analysis.

### S2 — Controlled Morphosyntax
Goal: connect recognized forms to local grammatical behavior.
Rule: one principal operation per item; local span preferred.

### S3 — Sentence Relations
Goal: analyze subject/predicate, verb arguments, governance, attachment, coordination and controlled clause relations.
Rule: prerequisite closure required before productive analysis.

### S4 — Complex Clause Integration
Goal: integrate conditional, relative, subordinate, circumstantial and higher local relations.
Rule: multi-feature items must label target versus supporting features.

### S5 — Qur'anic Integration / Capstone
Goal: analyze authentic multi-feature Qur'anic spans, justify classifications, identify ambiguity, and transfer competence to unseen passages.
Rule: no capstone item may substitute translation intuition for grammatical evidence.

## Level mapping constraints
1. K order is prerequisite evidence, not automatically one K = one commercial level.
2. Multiple K may share one instructional level when cognitive load and assessment observability permit.
3. A difficult K may span more than one learning unit without creating a new competency ID.
4. Placement may skip already-mastered K through observable evidence.
5. Acceleration changes route/time, never mastery threshold.
6. No learner is forced to repeat mastered K merely to preserve book order.

## Evidence-to-curriculum rule
E2 = safe for controlled curriculum use.
E3 = preferred for diversified teaching, placement and item-generation pools.
Higher evidence states may later support automated generation at larger scale.

## Assessment observability classes
O1 Recognition — select/identify/classify target.
O2 Local analysis — state grammatical relation/function in a minimal span.
O3 Contrast — distinguish target from a near-neighbor/negative control.
O4 Transfer — apply operation to unseen Qur'anic occurrence.
O5 Integration — coordinate multiple mastered competencies in one span.

## Placement policy
A K can be placement-tested only when its mastery observable can be sampled without requiring an unmastered later K. Placement items must therefore carry:
- target K;
- prerequisite set;
- observable class;
- leakage check;
- scoring rule;
- confidence flag.

## QURBATA mapping policy
QURBATA pages/modules are delivery artifacts, not the canonical competency architecture. One page may teach/review several already-permitted features, but each new target must point back to one frozen K and its prerequisite-safe evidence bank.

## RIQA OS mapping policy
For each K, RIQA OS should eventually store at minimum:
NOT_STARTED → LEARNING → PRACTICING → ASSESSMENT_READY → MASTERED.
Additional states may represent REMEDIATION and ACCELERATED_ROUTE without altering competency mastery semantics.

## Next mapping batch
Create K01–K15 curriculum records first, assigning provisional S-stage, observability class, prerequisite relation, placement eligibility, and QURBATA/RIQA OS hooks. Then validate leakage before expanding K16–K30.

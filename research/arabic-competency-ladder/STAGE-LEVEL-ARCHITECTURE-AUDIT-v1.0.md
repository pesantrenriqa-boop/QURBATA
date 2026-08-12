# STAGE / LEVEL ARCHITECTURE AUDIT v1.0

Status: FIRST-PASS FREEZE
Canonical competency architecture: K01–K65 FROZEN
Evidence baseline: 65/65 minimum E2; 17/65 E3; maturity 45.23%
Curriculum mapping: K01–K65 complete first pass

## Purpose
Convert the 65 canonical competencies into a teachable and assessable progression without equating competency IDs with instructional levels, meetings, pages, or books.

## Governing rules
1. K = canonical competency; K is not a level.
2. A level may bundle multiple tightly related competencies when prerequisites and assessment observability remain safe.
3. A competency may recur across later levels as review/integration without changing its canonical ID.
4. Placement may skip already-mastered levels, but mastery standards are never reduced.
5. Examples used to assess a level may not require unresolved higher-level features.
6. Stage boundaries reflect a qualitative change in learner operation, not equal numerical division.

## Frozen five-stage architecture
### S1 — Foundation Recognition
Primary operation: recognize and distinguish foundational Qur'anic Arabic forms and elementary relations.
Provisional competency span: K01–K12.

### S2 — Controlled Morphosyntax
Primary operation: identify and manipulate controlled morphology and local grammatical relations.
Provisional competency span: K13–K30.

### S3 — Sentence Relations
Primary operation: analyze sentence-internal relations and combine local grammatical evidence.
Provisional competency span: K31–K39.

### S4 — Complex Clause Integration
Primary operation: analyze subordinate, conditional, circumstantial and other multi-relation structures while controlling boundaries.
Provisional competency span: K40–K57.

### S5 — Qur'anic Integration / Capstone
Primary operation: integrate multiple previously mastered features in authentic Qur'anic spans with explicit uncertainty and boundary control.
Provisional competency span: K58–K65; K65 capstone.

## First-pass level clustering
The following 21-level model is adopted as the working architecture because it balances prerequisite safety, assessment observability, acceleration, and compatibility with RIQA program operations. It remains subject to item-level validation before final freeze.

### Stage 1 — Levels 1–4
- L01: K01–K03
- L02: K04–K06
- L03: K07–K09
- L04: K10–K12

### Stage 2 — Levels 5–10
- L05: K13–K15
- L06: K16–K18
- L07: K19–K21
- L08: K22–K24
- L09: K25–K27
- L10: K28–K30

### Stage 3 — Levels 11–13
- L11: K31–K33
- L12: K34–K36
- L13: K37–K39

### Stage 4 — Levels 14–19
- L14: K40–K42
- L15: K43–K45
- L16: K46–K48
- L17: K49–K51
- L18: K52–K54
- L19: K55–K57

### Stage 5 — Levels 20–21
- L20: K58–K61
- L21: K62–K65, with K65 as capstone integrative gate

## Why 21 levels
The 21-level structure is not derived by dividing 65 mechanically. It emerges from a practical clustering rule of roughly three related competencies per level, with larger bundles only at the integrative top layer where the learner is expected to coordinate previously mastered features. It also allows clean checkpoints for placement, remediation, acceleration, certification, and RIQA OS state transitions.

## Stage exit checkpoints
- S1 exit: learner can recognize foundational forms/relations without relying on advanced parsing.
- S2 exit: learner can analyze controlled morphology and local syntax reliably.
- S3 exit: learner can resolve sentence relations and discriminate nearby structures.
- S4 exit: learner can analyze complex clauses with boundary and dependency control.
- S5 exit: learner can integrate multiple Qur'anic Arabic features and justify analysis; K65 is the capstone gate.

## Placement-test consequence
Placement should be hierarchical, not a 65-item flat test. Proposed checkpoint ladder:
L04 → L10 → L13 → L19 → L21.
If a learner passes a stage checkpoint, testing advances upward; if not, branch downward to diagnostic level bundles. This reduces test length while preserving competency-level diagnosis.

## QURBATA consequence
A QURBATA book/page is a delivery artifact. It may teach, review, or assess one or more level bundles. Therefore 21 levels do not imply 21 books, and 65 competencies do not imply 65 pages.

## RIQA OS consequence
Minimum state model:
competency_state (K01–K65) + level_state (L01–L21) + stage_state (S1–S5).
Level completion is computed from competency mastery; stage completion is computed from required level/checkpoint mastery. Acceleration records skipped instruction but never fabricated competency mastery.

## Validation still required before FINAL freeze
1. dependency audit across every adjacent level;
2. workload/equivalence audit for L20 and L21;
3. placement observability audit for each level;
4. assessment item minimum per K and per L;
5. mapping from L01–L21 to QURBATA delivery sequence;
6. RIQA OS state-transition specification.

## Current decision
Five stages are FROZEN as the architecture frame.
Twenty-one levels are WORKING-FROZEN for validation and downstream blueprinting; level membership may move only if prerequisite/assessment evidence requires it.

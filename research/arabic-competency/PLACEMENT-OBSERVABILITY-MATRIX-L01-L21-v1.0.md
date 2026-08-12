# Placement Observability Matrix L01–L21 v1.0

Status: production research artifact
Scope: 65 canonical Qur'anic Arabic competencies mapped into 5 stages / 21 levels.
Purpose: convert the frozen/working-frozen level architecture into observable placement decisions without testing all 65 competencies linearly.

## Core rules
1. Placement measures observable performance, not prior attendance or book completion.
2. Every level has a minimum observable discriminator and a mastery signal.
3. A higher-level pass may accelerate routing, but cannot erase prerequisite failures detected by diagnostic probes.
4. Examples must remain inside the feature ceiling of the tested level.
5. Ambiguous semantic/discourse judgments require fallback/manual review rather than forced auto-scoring.
6. Checkpoint routing uses L04 → L10 → L13 → L19 → L21, followed by local diagnosis when needed.

## Matrix
| Level | Canonical K range | Primary observable | Placement evidence | Decision role |
|---|---|---|---|---|
| L01 | K01–K03 | recognizes foundational nominal/particle/form distinctions in controlled Qur'anic spans | identify/classify | local diagnosis |
| L02 | K04–K06 | distinguishes early morphological categories without importing later syntax | classify + contrast | local diagnosis |
| L03 | K07–K09 | recognizes controlled form/function contrasts | identify + minimal explanation | local diagnosis |
| L04 | K10–K12 | integrates S1 recognition reliably across unseen examples | mixed recognition set | S1 checkpoint |
| L05 | K13–K15 | identifies controlled morphosyntactic roles | label relation/role | local diagnosis |
| L06 | K16–K18 | distinguishes coordination/basic relation patterns | classify relation | local diagnosis |
| L07 | K19–K21 | resolves controlled inflection/function contrasts | select + justify | local diagnosis |
| L08 | K22–K24 | recognizes expanding nominal/verbal constructions | parse constrained span | local diagnosis |
| L09 | K25–K27 | connects form with sentence function under bounded complexity | relation mapping | local diagnosis |
| L10 | K28–K30 | integrates S2 operations on unseen Qur'anic spans | mixed morphosyntax task | S2 checkpoint |
| L11 | K31–K33 | identifies core sentence relations | dependency/role mapping | local diagnosis |
| L12 | K34–K36 | distinguishes related sentence structures and distractors | contrastive analysis | local diagnosis |
| L13 | K37–K39 | integrates sentence relations across bounded clauses | constrained parse | S3 checkpoint |
| L14 | K40–K42 | recognizes complex-clause entry patterns | clause boundary + relation | local diagnosis |
| L15 | K43–K45 | resolves relative/subordinate structure; K45 requires safe reconstruction | analysis + manual fallback | local diagnosis |
| L16 | K46–K48 | tracks dependencies across more complex local spans | relation graph/task | local diagnosis |
| L17 | K49–K51 | integrates multiple syntactic cues | multi-feature analysis | local diagnosis |
| L18 | K52–K54 | distinguishes higher-order clause/function alternatives | contrast + justification | local diagnosis |
| L19 | K55–K57 | integrates S4 structures under unseen-item conditions | mixed complex-clause task | S4 checkpoint |
| L20 | K58–K61 | integrates earlier competencies in authentic Qur'anic contexts; no translation-only scoring | multi-feature authentic span | S5 gateway |
| L21 | K62–K65 | capstone integration, boundary control, uncertainty handling, transfer | capstone set + targeted probes | final checkpoint |

## Adaptive routing
### Initial checkpoint ladder
L04 → L10 → L13 → L19 → L21.

### Routing logic
- Fail L04: diagnose L01–L04; placement cannot exceed unresolved foundational ceiling.
- Pass L04, fail L10: diagnose L05–L10.
- Pass L10, fail L13: diagnose L11–L13.
- Pass L13, fail L19: diagnose L14–L19.
- Pass L19, fail L21: diagnose L20–L21.
- Pass L21: run prerequisite integrity probes before final accelerated placement/capstone qualification.

## Observable response classes
A. Recognition: point to/identify the target feature.
B. Classification: assign the correct grammatical category.
C. Relation: identify head-dependent / sentence-role relation.
D. Contrast: reject a near-neighbour or distractor and explain the decisive cue.
E. Reconstruction: recover a locally licensed omitted element only where evidence is unique.
F. Integration: combine two or more already-mastered competencies in one Qur'anic span.
G. Transfer: apply the same operation to an unseen but level-compliant example.

## Scoring architecture (blueprint, not yet psychometrically calibrated)
Each checkpoint must include at least:
- direct positive items,
- contrast/negative-control items,
- unseen transfer items,
- prerequisite probes,
- manual-review flag for structurally/semantically ambiguous cases.

Do not convert raw percentage alone into level placement. Placement must combine checkpoint performance, prerequisite integrity, and local diagnostic results.

## Safety against false acceleration
A learner may skip instructional material when mastery is demonstrated, but cannot skip a prerequisite merely because a harder item was guessed correctly. At least one independent prerequisite probe is required for acceleration across a stage boundary.

## RIQA OS implications
Minimum state fields:
- learner_id
- checkpoint_attempt
- checkpoint_level
- item_id
- competency_ids
- response_class
- correctness
- confidence/uncertainty flag
- manual_review_required
- prerequisite_probe_result
- diagnosed_floor
- diagnosed_ceiling
- recommended_entry_level
- acceleration_eligible
- remediation_targets

## QURBATA implications
Placement level is not identical to book/page number. QURBATA content should consume the canonical competency/level map and generate practice/remediation according to diagnosed gaps.

## Freeze status
- Five-stage architecture: retained.
- 21-level architecture: dependency/workload validated; remains pending final freeze until placement blueprint stress-test.
- Placement observability: first-pass complete for L01–L21.
- Next artifact: adaptive placement-test blueprint with checkpoint modules, item allocation, routing rules, mastery gates, and retest/remediation policy.

# Authoritative K-ID Alignment Correction v1.0

**Status:** ACTIVE CORRECTION CONTROL  
**Authoritative source:** `CANONICAL-REGISTRY-K01-K67-v0.1.md` from PR #4  
**Scope:** placement architecture, replacement items, registry normalization, progress accounting

## 1. Critical finding

The authoritative competency ladder is **K01–K67**, not K01–K65. The source registry explicitly defines K66 `REL-PURPOSE-GOAL` and K67 `REL-CONCESSION` and states K67 as the provisional core endpoint.

Therefore any previous placement artifacts that assumed K01–K65 as the full canonical universe must be treated as provisional architecture and realigned before production freeze.

## 2. Canonical stage-relevant bands

For placement alignment, the source registry establishes these operation families:
- K01–K12: recognition foundations + simple local relations
- K13–K37: phrase/local clause relations and additional recognition/operator skills
- K38–K46: transformed predication, reference, embedding, controlled ellipsis
- K47–K57: conditional architecture + mood morphology
- K58–K67: interclausal/discourse-semantic relations

This supersedes any placement artifact that labeled K58–K65 as the complete capstone band.

## 3. Immediate mismatch findings

### L04 replacements
L04 replacement items were intentionally written around low-level operations. They must now map exactly to canonical K01–K12. Several labels in draft replacement prose used an offset/renamed interpretation and require mechanical K-ID correction before registry promotion.

### L10 replacements
L10 replacements were drafted by operation names because the authoritative map was unavailable. They must now be aligned only to canonical K13–K37 operations actually represented at the checkpoint. No item may receive a K-ID solely because its draft operation sounds similar.

### L13 replacements
L13 replacements were drafted as generic sentence relations. Canonical K31–K39 are actually a mixed band of recognition nodes plus `REL-INNA-CORE` and `REL-LAYSA-PRED`; therefore the provisional L13 assumption “K31–K39 = Sentence Relations” is not authoritative and requires architecture correction.

### L19/L21
The previous placement assumption `L19 = K40–K57 complex clause` and `L21 = K58–K65 capstone` only partially matches the canonical registry. K40–K46 are transformed predication/reference/embedding, K47–K57 conditional+mood, and the capstone/discourse endpoint extends through K67.

## 4. Non-destructive correction policy

1. Do not delete prior research artifacts; preserve them as historical design iterations.
2. Mark their competency-band labels as **PROVISIONAL / SUPERSEDED FOR K-ID MAPPING** where needed.
3. Rebuild the placement checkpoint-to-K map from the authoritative registry and prerequisite graph.
4. Reassign replacement items by canonical learner operation, not by old numeric assumptions.
5. Add coverage for K66–K67 before claiming full canonical placement coverage.
6. Recompute progress after realignment; prior 180/180 remains an item-slot milestone, not canonical K01–K67 coverage proof.

## 5. Required next artifacts

1. `PLACEMENT-CHECKPOINT-CANONICAL-K-MAP-v1.0.md`
2. corrected K-ID tables for L04 replacements
3. corrected K-ID tables for L10/L13 replacements
4. canonical audit of L19/L21 items against K38–K67
5. new K66/K67 placement evidence/items if absent
6. revised master registry and progress ledger

## 6. Governance decision

**Authoritative K01–K67 registry is now the source of truth for competency identity.**

No production registry row may be enabled until its `target_competency_ids` are aligned to this source and the associated prerequisite/feature ceiling is verified.
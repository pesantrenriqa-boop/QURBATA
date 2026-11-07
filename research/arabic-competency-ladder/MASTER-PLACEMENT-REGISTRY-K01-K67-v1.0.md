# Master Placement Registry K01–K67 v1.0

**Status:** DRAFT CANONICAL CONSOLIDATION — NOT PRODUCTION ENABLED  
**Authority:** `CANONICAL-REGISTRY-K01-K67-v0.1.md` plus checkpoint canonical remap/repair artifacts  
**Purpose:** single placement-facing control surface after canonical realignment.

## 1. Canonical checkpoint bands

| Checkpoint | Canonical band | Count | Draft candidate coverage |
|---|---|---:|---:|
| L04 | K01–K12 | 12 | 12/12 |
| L10 | K13–K30 | 18 | 18/18 |
| L13 | K31–K40 | 10 | 10/10 |
| L19 | K41–K57 | 17 | 17/17 |
| L21 | K58–K67 | 10 | 10/10 |
| **TOTAL** | **K01–K67** | **67** | **67/67 = 100%** |

## 2. Source-of-truth chain

Canonical identity and sequence:
- `CANONICAL-REGISTRY-K01-K67-v0.1.md`
- `AUTHORITATIVE-K-ID-ALIGNMENT-CORRECTION-v1.0.md`
- `PLACEMENT-CHECKPOINT-CANONICAL-K-MAP-v1.0.md`

Checkpoint repair/closure:
- L04: `CANONICAL-REMAP-L04-v1.0.md`
- L10: `CANONICAL-REMAP-L10-v1.0.md`, `L10-CANONICAL-REPAIR-BATCH-01-v1.0.md`, `L10-CANONICAL-REPAIR-K21-v1.0.md`
- L13: `CANONICAL-REMAP-L13-v1.0.md`, `L13-CANONICAL-REPAIR-K31-K40-v1.0.md`
- L19: `CANONICAL-AUDIT-L19-K41-K57-v1.0.md`, `L19-CANONICAL-FUNCTION-MATRIX-K41-K57-v1.0.md`, repair batches 01–03
- L21: `CANONICAL-AUDIT-L21-K58-K67-v1.0.md`, `L21-CANONICAL-FUNCTION-MATRIX-K58-K67-v1.0.md`, repair/closure artifacts including `L21-CANONICAL-CLOSURE-K63-K64-v1.0.md`

## 3. Registry state model

Every competency row is controlled by these fields before production promotion:

- `competency_id`
- `checkpoint`
- `canonical_operation`
- `primary_item_id`
- `alternate_item_ids`
- `quran_reference`
- `target_span`
- `function_signature`
- `prerequisite_ids`
- `ambiguity_level`
- `arabic_review_status`
- `duplicate_audit_status`
- `pilot_status`
- `production_enabled`

Current global default:

`production_enabled = false`

Coverage completeness must never automatically flip production enablement.

## 4. Consolidated competency rows

### L04 — K01–K12
K01, K02, K03, K04, K05, K06, K07, K08, K09, K10, K11, K12  
State: `CANONICAL-CANDIDATE-COVERED`  
Primary source: L04 canonical remap.  
Special controls: out-of-band legacy item P25 excluded from L04 target credit; K12 rewrite requirement inherited from remap artifact until final item review.

### L10 — K13–K30
K13, K14, K15, K16, K17, K18, K19, K20, K21, K22, K23, K24, K25, K26, K27, K28, K29, K30  
State: `CANONICAL-CANDIDATE-COVERED`  
Primary sources: L10 repair Batch 01 + dedicated K21 closure.  
Legacy morphology/number/gender diagnostics that do not instantiate K13–K30 remain research diagnostics and do not provide canonical target credit.

### L13 — K31–K40
K31, K32, K33, K34, K35, K36, K37, K38, K39, K40  
State: `CANONICAL-CANDIDATE-COVERED`  
Primary source: L13 K31–K40 repair set.  
Legacy L13 replacements are retained as prerequisite/out-of-band diagnostics unless separately remapped.

### L19 — K41–K57
K41, K42, K43, K44, K45, K46, K47, K48, K49, K50, K51, K52, K53, K54, K55, K56, K57  
State: `CANONICAL-CANDIDATE-COVERED`  
Primary sources: function matrix + repair batches.  
Special controls: morphology and ellipsis nodes require occurrence/function review; any medium/high ambiguity item requires approved alternate-analysis rubric before automated scoring.

### L21 — K58–K67
K58, K59, K60, K61, K62, K63, K64, K65, K66, K67  
State: `CANONICAL-CANDIDATE-COVERED`  
Primary sources: L21 function matrix, repair batch, K63/K64 closure, K66/K67 dedicated coverage.  
Late-ladder legacy evidence is mapped by operation identity rather than obsolete K-number where the old K01–K65 architecture conflicts with current K01–K67.

## 5. Coverage declaration

**Draft canonical placement candidate coverage: 67/67 = 100%.**

This declaration means every current canonical competency K01–K67 has a placement-facing candidate path. It does **not** mean:
- every candidate is Arabic-review approved;
- every candidate is duplicate-free;
- every item has empirical difficulty/discrimination estimates;
- cut scores are final;
- the registry is production enabled.

## 6. Fast-track next gates

To accelerate without weakening validity, remaining work is compressed into four gates rather than many serial documents:

### Gate A — Duplicate + Function Audit
Run one matrix across all 67 primary candidates. Resolve only actual conflicts; do not rewrite clean items.

### Gate B — Arabic Content Review
Review by exception first: HIGH/MEDIUM ambiguity, reconstructed morphology, hidden elements, relative-return links, condition/result boundaries, discourse relations. LOW ambiguity items can be batch-approved if no exception is found.

### Gate C — Machine-Readable Assembly Registry
Generate one machine-readable registry for RIQA OS with checkpoint routing, prerequisite ceilings, scoring key, review state, and `production_enabled` flag.

### Gate D — Pilot
Pilot the approved subset, estimate item behavior, then freeze cut scores and promote eligible rows.

## 7. Governance acceleration rule

From this point forward:
1. no new competency architecture is opened unless a defect is demonstrated;
2. no new placement item is created when an existing canonical candidate passes the gate;
3. documentation is consolidated rather than multiplied;
4. review is exception-driven;
5. research completeness and production readiness remain separately reported.

## 8. Immediate status

- Canonical competency universe: **K01–K67 locked as current source of truth**.
- Draft placement candidate coverage: **67/67 = 100%**.
- Historical 180-item pool: preserved as research/pilot bank; not automatically production-enabled.
- Production registry: **next gate**.
- Final psychometric validation: pending pilot data.

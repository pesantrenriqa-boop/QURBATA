# Canonical Registry + Dependency Protocol v0.1

**Status:** CONSOLIDATION STANDARD  
**Applies to:** Qur'anic Arabic Competency Ladder K1–K67  
**Baseline:** K1–K67 DRAFT-FROZEN; K67 provisional core endpoint.

## 1. Purpose

This document defines the canonical format for converting the discovery-phase ladder into a stable architecture suitable for audit, curriculum generation, assessment design, RIQA OS integration, and future corpus expansion.

A competency number is not sufficient. Every K must have an explicit identity, learner operation, domain, prerequisite structure, evidence status, and boundary against neighboring competencies.

## 2. Canonical registry record

Every K1–K67 must be represented with the following fields:

```text
ID:
Canonical name:
One-line competency:
Primary domain:
Secondary domain(s):
Core learner operation:
Direct prerequisites:
Inherited prerequisites:
Positive evidence:
Excluded operations:
Assessment signature:
Evidence maturity:
Architecture status:
Mastery/transfer extensions:
Neighbor-overlap notes:
```

## 3. Domain taxonomy

Each competency receives exactly one **primary domain** and zero or more secondary domains.

### FORM
Surface recognition of lexical/morphological form or overt marker.

### MORPHOLOGY
Inflection, deletion, retention, overt/estimated endings, form-conditioned grammatical evidence.

### PHRASE
Local constituent construction below full clause level.

### CLAUSE
Internal architecture of a nominal/verbal or otherwise complete clause.

### DEPENDENCY
A grammatical or referential relation requiring linking two elements, such as governor→target or antecedent→pronoun.

### INTERCLAUSE
Structural linkage between two clauses/propositions.

### DISCOURSE
Semantic/pragmatic relation between propositions: sequence, contrast, result, reason, restriction, purpose, concession, etc.

No K should receive a new number merely because it has a different textbook label inside the same learner operation.

## 4. Dependency types

### P1 — HARD prerequisite
The target K cannot be assessed meaningfully without this prior operation.

### P2 — NORMAL prerequisite
Normally mastered earlier, but occurrence-specific scaffolding can sometimes compensate.

### P3 — TRANSFER support
Not required for the core definition, but improves generalization or more complex evidence items.

### PX — EXCLUDED dependency
A later operation that must not be required by a core K item.

## 5. Dependency graph rule

Numeric order is **not identical** to prerequisite structure.

Canonical representation:

`Kx <- {hard prerequisites}`

Example from the late ladder:

- `K59 <- {K58}` because temporal sequencing presupposes recognition of two linked clauses.
- `K61 <- {K60}` because explicit `العائد` resolution presupposes identification of the relative-clause structure.
- `K63 <- {K58}` with K59 as P2/contrastive support, because result relation requires proposition linkage but not necessarily temporal sequencing competence in every occurrence.
- `K67 <- {K58}` with K62 as strong conceptual support, because concession is an interpropositional relation whose distinctness is tested against contrast.

The final dependency graph must therefore be a DAG-like pedagogical graph, not a simple K1→K2→…→K67 chain.

## 6. Evidence maturity scale

Architecture freeze and corpus maturity are separated.

### E0 — DEFINITION ONLY
Competency identity exists but no clean bank is established.

### E1 — SEEDED
A small validated evidence set exists.

### E2 — CLEAN BANK
Enough clean examples exist for basic teaching/assessment.

### E3 — DIVERSE BANK
Evidence spans multiple surahs/forms/contexts without changing the target operation.

### E4 — STRESS-TESTED
Negative, ambiguous, and near-neighbor cases have been tested.

### E5 — PRODUCTION READY
Bank is sufficiently mature for automatic curriculum/question generation under governance controls.

`DRAFT-FROZEN` refers to architecture, not automatically to E4/E5 evidence maturity.

## 7. Architecture status scale

- **CANDIDATE** — under discovery.
- **GATED** — conceptual/evidence gate passed.
- **DRAFT-FROZEN** — competency identity locked against casual change.
- **V1-FROZEN** — included in ratified canonical architecture.
- **DEPRECATED** — retained for traceability but removed from active ladder.

Current K1–K67 baseline: **DRAFT-FROZEN** pending registry/dependency/overlap consolidation.

## 8. One-operation rule

A core item should be solvable by:

`earlier mastered operations + exactly one target operation`.

If an item requires two unmastered operations, it must be:
- rejected from the core bank;
- decomposed;
- moved to transfer/mastery;
- or reserved for a later competency.

This remains the strongest anti-overload rule in the ladder.

## 9. Neighbor-overlap audit

Every K must be compared with at least:
- K-1;
- K+1 where applicable;
- any nonadjacent K with the same marker or semantic neighborhood.

Audit questions:
1. Can the two K be assessed with different prompts?
2. Does each require a different learner judgment?
3. Can one be solved completely using the other without a new operation?
4. Is the distinction merely terminology, marker inventory, or difficulty?

If answer 3 is yes and no new operation exists, merge/reclassify rather than preserve artificial fragmentation.

## 10. Late-ladder canonical anchor records

The following entries serve as normalization anchors for the full registry.

### K58
**Primary domain:** INTERCLAUSE  
**Operation:** identify two independently analyzable clauses connected at the same structural level by one overt validated coordinator.  
**Assessment signature:** identify clause 1, clause 2, and linker.  
**Key boundary:** phrase-level coordination does not count.

### K59
**Primary domain:** DISCOURSE  
**Operation:** identify validated temporal sequencing between two linked clauses, core-first with transparent `ثم`.  
**Direct prerequisite:** K58.  
**Key boundary:** sequencing is more specific than neutral coordination.

### K60
**Primary domain:** DEPENDENCY / CLAUSE  
**Operation:** identify `اسم موصول` and determine the beginning/end of its `صلة الموصول`.  
**Key boundary:** no advanced `العائد` analysis required.

### K61
**Primary domain:** DEPENDENCY  
**Operation:** identify an overt `العائد` inside `صلة الموصول` and resolve it back to the relative antecedent.  
**Direct prerequisite:** K60.  
**Key boundary:** omitted resumptive is outside core.

### K62
**Primary domain:** DISCOURSE  
**Operation:** identify explicit contrast/correction (`استدراك`) relation between two propositions.  
**Key boundary:** not every contrast is concession.

### K63
**Primary domain:** DISCOURSE  
**Operation:** identify B as the explicit result/consequence of A.  
**Key boundary:** marker function must be prevalidated; surface `ف` alone is insufficient.

### K64
**Primary domain:** DISCOURSE  
**Operation:** identify which proposition is being explained and which supplies the reason/cause.  
**Key boundary:** cause is not purpose.

### K65
**Primary domain:** DISCOURSE / DEPENDENCY  
**Operation:** identify the relevant domain and the element restricted/excepted by overt `إلا`.  
**Key boundary:** full `باب الاستثناء` subtype/i‘rab taxonomy is mastery, not core K65.

### K66
**Primary domain:** DISCOURSE  
**Operation:** identify an action/proposition and its explicitly encoded intended purpose/goal.  
**Key boundary:** intended end is not consequence; no new hidden-`أن` operation may be required.

### K67
**Primary domain:** DISCOURSE  
**Operation:** identify an expectation-triggering circumstance A and proposition B that nevertheless remains valid.  
**Key boundary:** concession requires defeated expectation, not merely contrast.

## 11. Consolidation workflow

The full canonicalization is performed in five passes:

### Pass 1 — Registry extraction
Extract the final frozen definition of every K1–K67 from its authoritative final-gate artifact.

### Pass 2 — Domain tagging
Assign one primary domain and secondary tags.

### Pass 3 — Dependency mapping
Replace simple numerical sequence with P1/P2/P3 prerequisite edges.

### Pass 4 — Neighbor-overlap audit
Test adjacent and semantically related K pairs for redundancy.

### Pass 5 — Evidence maturity
Assign E0–E5 independently from architecture status.

No wording of a frozen K is to be silently rewritten during extraction. Proposed normalization changes must be recorded as audit findings first.

## 12. Output artifacts required before architecture v1.0

1. `CANONICAL-REGISTRY-K1-K67-v0.1.md`
2. `DEPENDENCY-GRAPH-K1-K67-v0.1.md`
3. `DOMAIN-MAP-K1-K67-v0.1.md`
4. `OVERLAP-AUDIT-K1-K67-v0.1.md`
5. `FRONTIER-MASTERY-REGISTER-v0.1.md`
6. `EVIDENCE-MATURITY-K1-K67-v0.1.md`
7. `LADDER-ARCHITECTURE-v1.0.md`

## 13. Decision

**Protocol accepted for consolidation.**

K67 remains the provisional core endpoint. No K68+ work resumes during consolidation unless a formal frontier-reopen gate demonstrates a genuinely distinct learner operation with sufficient Qur'anic evidence.
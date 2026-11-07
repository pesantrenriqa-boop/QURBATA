# K63–K64 Evidence Discovery Workpackage v1.0

**Status:** ACTIVE RESEARCH WORKPACKAGE — NON-PRODUCTION  
**Scope:** close the final two current L21 canonical placement evidence gaps without inventing Qur'anic references.  
**Canonical registry:** K01–K67.

## 1. Current state

- K63 `REL-RESULT-CONSEQUENCE`: definition DRAFT-FROZEN; exact normalized placement occurrence still missing.
- K64 `REL-CAUSE-REASON`: definition DRAFT-FROZEN; exact normalized placement occurrence still missing.
- L21 definition-level coverage: 10/10.
- L21 current item-level candidate coverage: 8/10.
- Historical L21 records remain R0 FULL 36/36.

## 2. K63 acceptance gate — Result / Consequence

A candidate may be promoted only when all are true:
1. two overt proposition spans A and B are locally recoverable;
2. one overt linker is present;
3. the linker's function is occurrence-specifically validated as result/consequence;
4. B is a consequence/result of A, not merely temporally later;
5. the item is not merely a K47/K48 condition→response occurrence;
6. no ellipsis reconstruction is needed;
7. no tafsir-only causal inference is required;
8. marker-function ambiguity is resolved before learner scoring.

Required normalized fields:
- surah:ayah;
- exact target span;
- proposition A boundary;
- proposition B boundary;
- overt marker;
- marker-function validation note;
- competing-function rejection note;
- ambiguity;
- Arabic-content reviewer disposition;
- canonical item ID.

## 3. K64 acceptance gate — Cause / Reason

A candidate may be promoted only when all are true:
1. two overt proposition spans are locally recoverable;
2. an overt explanatory/reason signal is present;
3. the signal's function is occurrence-specifically validated;
4. the learner can distinguish the explained proposition from the proposition giving the reason;
5. purpose/goal reading does not compete strongly;
6. result/consequence reading does not replace the reason relation;
7. no hidden `أن`, new mood mechanism, or ellipsis is required as a new operation;
8. no tafsir-only causal inference is required.

Required normalized fields mirror K63, plus an explicit cause-vs-purpose rejection note.

## 4. Candidate search order

Search by **operation identity**, not legacy K number:

### K63
1. old `RESULT-CONSEQUENCE` evidence/clean-bank artifacts;
2. distinctness records involving result vs sequence/condition;
3. any occurrence-level notes with overt prevalidated result linker;
4. historical L21/L19 items only if their function survives the current canonical gate.

### K64
1. old `CAUSE-REASON` evidence/clean-bank artifacts;
2. distinctness records involving cause vs purpose/result;
3. any occurrence-level notes with overt explanatory marker;
4. historical placement items only if they provide an overt, local reason relation.

## 5. Explicit non-acceptable shortcuts

Do not close K63/K64 using:
- a plausible verse remembered from outside the repository without occurrence validation;
- a conditional response relabeled as generic result;
- a simple `فـ` occurrence without validated function;
- an inferred theological reason that depends on tafsir;
- a purposive construction relabeled as cause;
- an unnormalized legacy K number.

## 6. Closure rule

The L21 canonical candidate layer becomes **10/10 = 100%** only after one K63 candidate and one K64 candidate each satisfy the full normalized acceptance gate above.

Until then, the truthful state remains:
- canonical definitions: 10/10;
- placement candidates: 8/10;
- unresolved evidence-normalization debt: 2 nodes;
- production enabled: 0.

## 7. Next artifact after successful discovery

Create `L21-CANONICAL-COVERAGE-CLOSURE-K58-K67-v1.0.md` containing the final 10-node mapping, source evidence, canonical IDs, review state, and explicit distinction between draft coverage and production readiness.
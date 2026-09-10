# Placement Quality Disposition Ledger v1.0

**Scope:** L04/L10/L13/L19/L21 placement bank
**Total pilot items:** 180
**Status:** CONSOLIDATED QUALITY LEDGER — NON-PRODUCTION

## 1. Purpose

Consolidate the first formal quality-screen results across all five checkpoints without inventing PASS status for summarized records whose complete item data is not present in the current consolidated sources.

## 2. Defensible reviewed subset

### L04 P31–P36
- PASS-CANDIDATE: 1
- PASS-WITH-NOTE: 4
- REWRITE: 1
- reviewed: 6
- normalization/recovery pending: P01–P30 (30)

### L10 P25–P36
- PASS-CANDIDATE: 4
- PASS-WITH-NOTE: 6
- REWRITE: 1
- HOLD-PREMATURE: 1
- reviewed: 12
- normalization/recovery pending: P01–P24 (24)

### L13 P25–P36
- PASS-CANDIDATE: 6
- PASS-WITH-NOTE: 5
- HOLD-AMBIGUOUS: 1
- reviewed: 12
- normalization/recovery pending: P01–P24 (24)

### L19 P25–P36
- PASS-CANDIDATE: 7
- PASS-WITH-NOTE: 3
- HOLD-AMBIGUOUS: 2
- reviewed: 12
- earlier high-ambiguity records explicitly HOLD-REVIEW: Batch-01 P07/P12; Batch-02 P18/P19/P21
- other earlier records remain review-pending

### L21 P25–P36
- PASS-CANDIDATE: 6
- PASS-WITH-NOTE: 5
- HOLD-AMBIGUOUS: 1
- reviewed: 12
- normalization/recovery pending: P01–P24 (24)

## 3. Current first-pass totals

Among the **54 item records directly dispositioned** in formal quality screens:
- PASS-CANDIDATE: **24**
- PASS-WITH-NOTE: **23**
- REWRITE: **2**
- HOLD-PREMATURE: **1**
- HOLD-AMBIGUOUS: **4**

Additional explicitly identified earlier L19 high-ambiguity HOLD-REVIEW records: **5**.

No item is `production_enabled=true` yet.

## 4. Recovery debt

The pilot bank is 180/180 complete as a research pool, but a material number of early records were consolidated by summary rather than full schema. Recovery therefore means reconstructing the **already-created research records from repository history/patches where available**, not inventing new replacements under old IDs.

Rules:
1. If original full record can be recovered, preserve the item ID and content history.
2. If only a summary exists and original wording cannot be recovered, create a new versioned reconstruction candidate and mark provenance `RECONSTRUCTED-FROM-SUMMARY`.
3. Reconstructed candidates cannot silently inherit pilot validity.
4. Any substantive rewrite increments version and preserves predecessor status.

## 5. Priority remediation queue

Immediate rewrite/HOLD queue:
- L04-P34 — rewrite nominal-relation rubric.
- L10-P30 — rewrite marker/operation target to avoid relation ambiguity.
- L10-P34 — HOLD-PREMATURE; simplify conditional boundary so Stage-3 reasoning is unnecessary.
- L13-P28 — HOLD-AMBIGUOUS; narrow coordination-scope claim.
- L19-P28 — HOLD-AMBIGUOUS; expert rubric required.
- L19-P36 — HOLD-AMBIGUOUS; split/segment capstone response.
- L21-P31 — HOLD-AMBIGUOUS/meta-evaluative; convert to objective learner task or evaluator-training item.

## 6. Duplicate-risk families for next audit

Near-duplicate functional families already visible across checkpoints:
1. `جاء الحق وزهق الباطل` — appears as subject/coordination, complexity contrast, prerequisite integrity, and capstone integration.
2. `إياك نعبد وإياك نستعين` — appears as object recognition, fronting, scope, reconstruction, and capstone.
3. `الذين يؤمنون... ويقيمون...` — appears as relative scope, embedded integration, prerequisite integrity, and capstone.
4. `لله الأمر / لله الحمد / لله الدين` — repeated fronted-predicate family.
5. conditional environments QS 110 / 3:160 / 4:59 / 8:29 — repeated condition-result transfer family.

These repeats are not automatically duplicates: a repeated verse is acceptable only when the **scored construct and response operation are demonstrably different**. Otherwise the lower-value item should be retired or replaced with a new transfer verse.

## 7. Production gate

An item may enter production registry only after:
- full canonical record exists;
- Arabic-content review complete;
- item-quality status PASS or approved PASS-WITH-NOTE;
- duplicate-function audit cleared;
- immutable version assigned;
- scoring rubric operationalized;
- `production_enabled` changed explicitly by governance.

## 8. Current interpretation

The bank is no longer in an item-generation phase. The active bottleneck is **normalization + expert-quality assurance + deduplication + operationalization**.
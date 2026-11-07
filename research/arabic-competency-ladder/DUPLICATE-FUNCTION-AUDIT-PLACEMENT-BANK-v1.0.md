# Duplicate-Function Audit — Placement Bank v1.0

**Status:** INTERNAL AUDIT — NON-AUTHORITATIVE  
**Scope:** L04, L10, L13, L19, L21 placement pools  
**Purpose:** distinguish valid pedagogical reuse from redundant measurement.

## 1. Rule

Repeated Qur'anic spans are not automatically duplicates. A repeated span may remain when at least one of the following differs materially:
- primary competency target;
- response operation;
- prerequisite diagnosis purpose;
- transfer vs direct role;
- feature ceiling;
- scoring evidence required.

A repeated span should be retired/replaced when the same span measures substantially the same construct with substantially the same response demand and adds little transfer value.

## 2. High-reuse families

### A. `جاء الحق وزهق الباطل` — QS 17:81
Observed across L13/L19/L21.
- L13 use: explicit local verb–subject + coordination relation.
- L19 use: coordinated-vs-nested complexity discriminator.
- L21 use: capstone prerequisite-integrated structural mapping / translation-leakage guard.
**Decision:** KEEP-CROSS-LEVEL, but cap total active forms using this exact span. At least one L21 form should eventually be replaced by unseen transfer if pilot exposure creates memorization risk.

### B. `إياك نعبد وإياك نستعين` — QS 1:5
Observed across L10/L13/L19/L21.
- L10: controlled morphosyntax/local object recognition.
- L13: explicit verb–object relation.
- L19: fronting inside integrated frame/local scope.
- L21: reconstruction/capstone.
**Decision:** KEEP-AS-VERTICAL-ANCHOR. This is a deliberately useful invariant anchor across levels, but no checkpoint should use more than one core-scored item from the same span in a single administration.

### C. `الذين يؤمنون...` / relative-scope family — QS 2:3 and QS 103:3
Observed L10/L13/L19/L21.
**Decision:** KEEP-MIXED. The family supports vertical progression from relative-form recognition to scope integration. Require alternate verses for at least 50% of transfer items so mastery is not passage-specific.

### D. Fronted PP predication `لله ...`
Observed with QS 30:4, 39:3, 45:36 and related spans.
**Decision:** KEEP-FAMILY, not duplicate. Different lexical/surface contexts are valuable transfer evidence. Avoid using two `لله...` items in the same six-item form unless one is explicitly a contrast/boundary item.

### E. Conditional families — QS 110, 3:160, 4:59, 8:29, 65:2
Observed heavily L10/L13/L19/L21.
**Decision:** KEEP-AS-PROGRESSION-FAMILY. This is a core vertical construct family. However, any item that only asks marker recognition at L19/L21 should be RETIRE/REWRITE because it under-targets the checkpoint.

### F. `الله الصمد` — QS 112:2
Observed L04/L13/L21.
**Decision:** KEEP-LIMITED. L04 nominal anchor and L21 translation-leakage control are distinct. Avoid additional production duplicates unless they test a new relation or misconception.

## 3. Duplicate-risk rules for registry

Every canonical item row must include:
- `verse_family_id`
- `function_signature`
- `vertical_anchor=true/false`
- `same_span_active_count`
- `same_function_active_count`

Proposed function signature format:
`checkpoint|primary_K|response_class|relation_operation|ceiling`

Example:
`L13|K32|relation|verb-subject|K39`

Two items with the same verse family and near-identical function signature are duplicate candidates.

## 4. Current audit decision

No automatic mass retirement is justified yet because many repeated passages intentionally represent vertical progression. The immediate production policy is:
1. keep vertical anchors;
2. retire only same-span + same-function redundancy;
3. require unseen-transfer alternatives;
4. restrict repeated exact spans within one administration;
5. recompute duplicate risk after all 180 records are normalized.

## 5. Recovery dependency

Full duplicate audit remains incomplete until summarized records (especially earlier P-ranges) are recovered into complete canonical records. Therefore no exact count of RETIRE-DUPLICATE is claimed yet.

## 6. Gate

**Status: DUPLICATE-FUNCTION POLICY COMPLETE; ITEM-LEVEL RETIREMENT PENDING FULL NORMALIZATION.**
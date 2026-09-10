# Clean Bank + Stress Test K44 — `لام التوكيد` in Simple `إنّ` v0.1

**Status:** WORKING RESEARCH — PRE-FREEZE  
**Baseline:** K1–K43 DRAFT-FROZEN.

## Target

K44 tests one narrow operation:

> identify a validated emphatic lām inside an already-analyzable `إنّ` construction and state that it adds emphasis without changing the underlying `إنّ + اسمها + خبرها` parse.

## Why this is not lexical inflation

The learner is not merely memorizing another particle. The new operation is **functional disambiguation**: distinguish emphatic lām from other lām types while preserving the K38 syntactic analysis.

## Core PASS profile

A K44 PASS occurrence must satisfy all of the following:
- `إنّ` construction is analyzable with K38;
- lām is overt;
- occurrence-specific grammar identifies it as emphatic lām / lām associated with emphasis in the `إنّ` structure;
- constituent carrying the lām is otherwise analyzable with K1–K43;
- no conditional, oath-response, command, or other lām function is needed;
- no clausal predicate or higher dependency is required solely to explain the example.

## False-positive stress matrix

### 1. `لام الأمر`
Reject from K44. It governs/marks command-like verbal behavior and is a different learnable operation.

### 2. `لام جواب القسم`
Reject from K44. Its function depends on oath-response structure.

### 3. `لام جواب الشرط`
Reject from K44. Its function belongs to conditional linkage.

### 4. lexical initial `لـ` / prepositional `لـ`
Reject from K44 unless occurrence parser independently identifies emphatic function. Surface prefix alone is never enough.

### 5. ambiguous/disputed lām
Classify REVIEW-FUNCTION, not PASS.

## Evidence classes

### PASS-A
Simple `إنّ` core + validated emphatic lām + no extra operation beyond K44.

### PASS-B
Same function, with only cumulative structures from K1–K43.

### REVIEW-SCOPE
Lām function is emphatic, but exact scope/focus requires advanced analysis not needed for K44 core.

### REVIEW-FUNCTION
Surface lām is present but function tagging is ambiguous or disputed.

### PREMATURE
Requires:
- oath-response analysis;
- conditional response;
- command lām;
- complex clausal khabar;
- another new discourse/scope relation.

## Atomicity test

K44 remains atomic if assessment can be framed as:

1. identify the `إنّ` structure;
2. locate the lām;
3. classify it as emphatic in this occurrence;
4. state that the underlying syntactic roles from K38 remain unchanged.

No full balaghah theory is required.

## Dependency reversal check

No hard dependency forces omitted `عائد` or conditional linkage before K44. In fact both require non-overt reconstruction or two-clause relation, while K44 operates on an overt marker inside an already-frozen construction.

**Result: PASS.**

## Freeze recommendation

K44 is eligible for DRAFT-FREEZE provided the production boundary remains unchanged and evidence records retain occurrence-specific `lam_function` tags.

## Metadata rule

Each K44 evidence item should eventually store:
- `surface_lam`;
- `lam_function`;
- `host_constituent`;
- `inna_structure_id`;
- `scope_status`;
- `ambiguity_flag`;
- `dependency_max_k`.

This prevents later systems from retrieving every token beginning with lām as if it were K44.

## Next frontier

After K44 freeze, rescan rather than auto-assign K45. Strong candidates remain:
- omitted/estimated `عائد` basic;
- simple conditional linkage;
- expansion of predicate/clause types;
- other distinct corpus-driven operations.
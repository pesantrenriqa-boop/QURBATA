# Evidence Gate K44 — Restricted `لام التوكيد` in Simple `إنّ` Construction v0.1

**Status:** WORKING RESEARCH — EVIDENCE GATE  
**Baseline:** K1–K43 DRAFT-FROZEN.

## K44 target

Learner can identify a **validated emphatic lām** inside an already-mastered simple `إنّ` construction and state that it adds emphasis without changing the underlying K38 parse.

Core operation:

`إنّ + اسم إنّ + خبر إنّ` → identify **لام التوكيد** → preserve the same underlying syntactic relation while adding emphasis.

## Why K44 is distinct

K38 already teaches the basic `إنّ` construction. K44 adds one new operation: distinguishing an overt emphasis marker from the underlying nominal syntax.

This is not lexical inventory expansion because the learner must classify the function of lām in occurrence and separate it from other lām categories.

## Hard prerequisites

- K33 recognition `إنّ`;
- K38 simple `إنّ + اسم + خبر` construction;
- all internal nominal/adjectival/PP relations used in the occurrence must already be ≤ K43.

## Evidence policy

### PASS-A — pure emphatic lām
Occurrence contains:
- simple `إنّ` construction already analyzable by K38;
- one overt lām validated as emphatic in this construction;
- no new clause relation;
- no omitted element needed for the core parse.

### PASS-B — cumulative clean
Additional structure is allowed only when all required operations are already frozen through K43.

### REVIEW-LAM-TYPE
Surface lām is present but function could be confused with another lām category. Keep out of core until occurrence-specific tagging resolves it.

### REVIEW-SCOPE
Lām is emphatic, but its exact scope over a complex predicate or embedded constituent is not pedagogically transparent.

### PREMATURE
Exclude if the example requires:
- lām jawab al-qasam;
- lām al-amr;
- lām in conditional response;
- nested relative/conditional clause beyond current scope;
- complex ellipsis;
- later rhetoric/scope theory.

## Anti-false-positive rule

A token beginning with `لـ` is **never** automatically K44.

Every candidate must store:
- surface token;
- corpus/POS tag;
- lām function;
- host constituent;
- whether underlying `إنّ` parse is already K38-clean;
- ambiguity flag.

## Pedagogical prompt

At K44 the learner should be able to answer:

> `أين لام التوكيد؟ وما وظيفتها؟ وهل تغيّر أصل تركيب إنّ واسمها وخبرها؟`

Expected concept: the lām adds emphasis; it does not replace the already-known `إنّ + اسم + خبر` relation.

## Freeze criteria

Freeze K44 only if:
1. enough occurrences are unambiguously emphatic lām in an `إنّ` construction;
2. the underlying K38 parse is cumulative-clean;
3. false positives from other lām types are excluded;
4. examples show structural diversity without importing K45+ operations;
5. K44 remains independently assessable as function classification + scope recognition.

## Next

Build curated occurrence bank, stress-test lām-type classification, then decide whether K44 can freeze. After that, rescan K45 among omitted `عائد`, simple conditional linkage, and other corpus-discovered structural operations.
# Quality Screen — L04 Placement Pool v1.0

**Status:** INTERNAL QUALITY SCREEN — NOT PRODUCTION APPROVAL  
**Checkpoint:** L04  
**Pool:** 36 items  
**Source:** `PLACEMENT-PILOT-L04-BATCH-01-v1.0.md`

## 1. Purpose

First structured quality screen of the completed L04 pool before canonical item-registry promotion. This screen evaluates construct fit, feature-ceiling leakage, ambiguity, scoring objectivity, diagnostic value, and duplication risk. It does **not** replace Arabic-content expert review or pilot/psychometric validation.

## 2. Screen rules

- **PASS-CANDIDATE**: structurally suitable for reviewer promotion.
- **PASS-WITH-NOTE**: usable only with explicit ceiling/rubric note.
- **REWRITE**: construct useful but prompt/span/rubric needs correction.
- **HOLD-AMBIGUOUS**: objective scoring not yet secure.
- **HOLD-PREMATURE**: likely requires operation above L04 ceiling.
- **RETIRE-DUPLICATE**: redundant function without meaningful transfer value.

No item receives `production_enabled=true` from this screen.

## 3. Item-level screen

### P01–P30
The earlier batch is retained as **REVIEW-PENDING** because the current consolidated source preserves P01–P30 by reference rather than reproducing every full item record. They must not be assigned PASS merely from summary coverage. Required action: recover/full-normalize each original item record into registry rows before item-level approval.

### P31 — `بَطْشَ رَبِّكَ شَدِيدٌ`
**Decision: PASS-WITH-NOTE.** Useful boundary control for K08, but scoring must remain binary boundary judgment. Do not require full i'rab. MEDIUM ambiguity retained.

### P32 — `فِيهِ هُدًى`
**Decision: PASS-WITH-NOTE.** Strong K09 boundary probe if scoring asks only whether the pattern is direct harf-jarr + isim-zahir. Attached pronoun analysis is explicitly outside ceiling.

### P33 — `اقْتَرَبَتِ السَّاعَةُ`
**Decision: PASS-CANDIDATE.** Clear integration of K06/K10; low ambiguity and strong diagnostic value.

### P34 — `هُوَ اللَّهُ`
**Decision: REWRITE.** The phrase is pedagogically useful, but the expected description `الله = predicate` risks oversimplifying a structure with legitimate analytical nuance in the wider verse. Rewrite rubric to score recognition of `هو` plus a ceiling-safe nominal relation without claiming one exclusive full i'rab.

### P35 — `لِلَّهِ الْأَمْرُ`
**Decision: PASS-WITH-NOTE.** Good integration K04/K09/K12. Rubric must state that only fronted prepositional predication at the target ceiling is scored; no semantic exclusivity claim.

### P36 — QS 112:1–2 integrative discriminator
**Decision: PASS-WITH-NOTE.** Valuable capstone for L04 but requires segmented scoring. Full verse analysis is forbidden; score only the sampled K01–K12 operations.

## 4. Current disposition count

Because P01–P30 are not fully reproduced in the consolidated source, this first screen intentionally avoids false precision.

- PASS-CANDIDATE: **1** (P33)
- PASS-WITH-NOTE: **4** (P31, P32, P35, P36)
- REWRITE: **1** (P34)
- REVIEW-PENDING full normalization: **30** (P01–P30)
- production-enabled: **0**

## 5. Structural findings

1. **Do not infer quality from pool completeness.** 36/36 means coverage target achieved, not that 36 items are production-valid.
2. **Consolidation debt exists.** P01–P30 must be materialized as complete records; summary references are insufficient for registry ingestion.
3. **Boundary items are valuable but fragile.** P31/P32 should never trigger scoring on features intentionally excluded by ceiling.
4. **Nominal-analysis overclaim is a recurring risk.** P34 demonstrates why alternate-analysis discipline must begin even at low checkpoints.
5. **Integrative items need segmented rubrics.** A single all-or-nothing score would hide which prerequisite failed.

## 6. Required next actions

1. Normalize P01–P30 into complete canonical records.
2. Rewrite P34 as v1.1 candidate while preserving original item history.
3. Add `review_status`, `ambiguity`, `ceiling_note`, and `production_enabled=false` to all 36 registry rows.
4. After normalization, run duplicate-function screen across all L04 records.
5. Arabic-content reviewer then validates Qur'anic span, grammatical claim, and acceptable alternatives.

## 7. Gate decision

**L04 remains QUALITY-REVIEW READY but NOT PRODUCTION-FROZEN.**

This screen establishes the first defensible item-level dispositions without fabricating approval for records that are not fully present in the consolidated source.
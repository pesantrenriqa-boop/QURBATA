# Quality Screen — L13 Placement Pool v1.0

**Status:** INTERNAL QUALITY SCREEN — NOT PRODUCTION APPROVAL  
**Checkpoint:** L13  
**Pool:** 36 items  
**Source:** `PLACEMENT-PILOT-L13-BATCH-01-v1.0.md`

## 1. Purpose

First structured quality screen of the L13 pool before registry promotion. L13 is the first checkpoint whose construct is explicit sentence-relation mastery, so the primary risks are relation overclaim, scope leakage into K40+, and ambiguous scoring.

## 2. P01–P24 normalization state

P01–P24 are preserved in the final source only by summary reference rather than full item records. They remain **REVIEW-PENDING / NORMALIZATION-RECOVERY**. No PASS status is inferred from coverage summary.

## 3. Item-level screen P25–P36

### P25 — QS 39:62 `اللَّهُ خَالِقُ كُلِّ شَيْءٍ`
**Decision: PASS-WITH-NOTE.** Strong K31 transfer. Score only the main nominal predication; inner idhafah remains outside target.

### P26 — QS 61:14 `قَالَ الْحَوَارِيُّونَ`
**Decision: PASS-CANDIDATE.** Clear verb–fa'il relation, low ambiguity.

### P27 — QS 93:9 `فَلَا تَقْهَرْ الْيَتِيمَ`
**Decision: PASS-CANDIDATE.** Clear verb–object transfer when `فـ` is excluded from higher-level scoring.

### P28 — QS 93:9–10 coordination-scope discriminator
**Decision: HOLD-AMBIGUOUS.** Current wording asks the learner to distinguish coordination scope across different markers and adjacent structures. This is potentially valid but needs a more explicit target span and rubric before automated scoring.

### P29 — QS 54:1 `اقْتَرَبَتِ السَّاعَةُ`
**Decision: PASS-CANDIDATE.** Good prerequisite-routing probe; low ambiguity.

### P30 — QS 30:4 `لِلَّهِ الْأَمْرُ`
**Decision: PASS-CANDIDATE.** Strong L12→L13 routing item with a clear two-step prerequisite then relation operation.

### P31 — QS 96:1–2 `خَلَقَ الْإِنسَانَ`
**Decision: PASS-CANDIDATE.** Strong subject-vs-object misconception detector.

### P32 — QS 107:1–2 relative + object integration
**Decision: PASS-WITH-NOTE.** Useful integrated relation item; discourse link between the spans must remain explicitly unscored.

### P33 — QS 45:36 `فَلِلَّهِ الْحَمْدُ`
**Decision: PASS-WITH-NOTE.** Suitable predicate-fronting transfer, but rubric must avoid semantic exclusivity claims and score only structural relation.

### P34 — QS 99:1 `إِذَا زُلْزِلَتِ الْأَرْضُ`
**Decision: PASS-WITH-NOTE.** Valid if only local `إذا` domain recognition plus internal verbal relation is scored. Full condition-result analysis is forbidden.

### P35 — QS 17:81 `جَاءَ الْحَقُّ وَزَهَقَ الْبَاطِلُ`
**Decision: PASS-CANDIDATE.** Strong cross-relation discriminator with low ambiguity.

### P36 — mixed final discriminator
**Decision: PASS-WITH-NOTE.** High value but segmented scoring is mandatory; no aggregate all-or-nothing score and no K40+ inference.

## 4. Current disposition count

For P25–P36:
- PASS-CANDIDATE: **6** — P26, P27, P29, P30, P31, P35
- PASS-WITH-NOTE: **5** — P25, P32, P33, P34, P36
- HOLD-AMBIGUOUS: **1** — P28

For P01–P24:
- REVIEW-PENDING / NORMALIZATION-RECOVERY: **24**

Production-enabled: **0/36**.

## 5. Structural findings

1. L13 items are generally stronger when a single relation is explicit and local.
2. Multi-marker scope items require manual/segmented scoring unless target boundaries are sharply specified.
3. Predicate-fronting items need structural-only rubrics to prevent semantic claims from entering grammar scoring.
4. Conditional markers may appear at L13 only when full condition-result integration is not required.
5. Mixed final discriminators should produce sub-scores by relation type.

## 6. Next actions

1. Recover/normalize P01–P24 into full canonical records.
2. Rewrite P28 into a narrower versioned item.
3. Create registry rows for all 36 with review state and `production_enabled=false`.
4. Continue screening L19 and L21.
5. Run duplicate-function audit after all checkpoint normalization.

## 7. Gate decision

**L13 remains QUALITY-REVIEW READY, NOT PRODUCTION-FROZEN.**
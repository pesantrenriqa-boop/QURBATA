# Quality Screen — L10 Placement Pool v1.0

**Status:** INTERNAL QUALITY SCREEN — NOT PRODUCTION APPROVAL  
**Checkpoint:** L10  
**Pool:** 36 items  
**Source:** `PLACEMENT-PILOT-L10-BATCH-01-v1.0.md`

## 1. Purpose

First structured quality screen of the completed L10 pool before canonical registry promotion. This screen evaluates construct fit, feature-ceiling leakage, ambiguity, scoring objectivity, diagnostic value, and duplication risk. It does not replace Arabic-content expert review or pilot/psychometric validation.

## 2. Screen rules

- **PASS-CANDIDATE**: structurally suitable for reviewer promotion.
- **PASS-WITH-NOTE**: usable only with explicit ceiling/rubric note.
- **REWRITE**: useful construct but prompt/span/rubric needs correction.
- **HOLD-AMBIGUOUS**: objective scoring not yet secure.
- **HOLD-PREMATURE**: likely requires K31+ operation.
- **RETIRE-DUPLICATE**: redundant function without meaningful transfer value.

No item receives `production_enabled=true` from this screen.

## 3. P01–P24 normalization state

P01–P24 are preserved in the final source only by summary reference rather than full records. Therefore they remain **REVIEW-PENDING / NORMALIZATION-RECOVERY**. No PASS status is inferred from the coverage summary.

## 4. Item-level screen P25–P36

### P25 — QS 94:7 `فَإِذَا فَرَغْتَ فَانصَبْ`
**Decision: PASS-WITH-NOTE.** Useful marker-recognition boundary item. Scoring must stop at recognizing `إذا`; any condition/sequence relation beyond that is outside L10 ceiling.

### P26 — QS 93:3 `مَا وَدَّعَكَ رَبُّكَ`
**Decision: PASS-CANDIDATE.** Clear negation-marker contrast; low ambiguity if temporal/semantic interpretation is excluded.

### P27 — QS 2:2 `لَا رَيْبَ`
**Decision: PASS-WITH-NOTE.** Useful nominal-negation classifier. Rubric must not require advanced case/governance analysis beyond the defined K19 operation.

### P28 — QS 35:3 `هَلْ مِنْ خَالِقٍ غَيْرُ اللَّهِ`
**Decision: PASS-WITH-NOTE.** Good prerequisite-depth test if only `من` + following nominal recognition is scored. Full rhetorical/predicative analysis is explicitly excluded.

### P29 — QS 108:2 `فَصَلِّ لِرَبِّكَ وَانْحَرْ`
**Decision: PASS-CANDIDATE.** Strong coordination + verbal-unit transfer; low ambiguity at the stated ceiling.

### P30 — QS 108:1 `إِنَّا أَعْطَيْنَاكَ`
**Decision: REWRITE.** The current expected response is too broad because `إنّا` contains the particle plus attached pronoun and the item risks mixing nominal governance with later verbal structure. Rewrite to a narrower observable operation and segmented scoring.

### P31 — QS 107:3 `وَلَا يَحُضُّ عَلَىٰ طَعَامِ الْمِسْكِينِ`
**Decision: PASS-WITH-NOTE.** Diagnostic value is good, but `object/prepositional complement boundary` must be explicitly scored so the item does not drift into Stage-3 relation analysis.

### P32 — QS 2:5 `أُولَٰئِكَ` vs QS 1:7 `الَّذِينَ`
**Decision: PASS-CANDIDATE.** Clean closed-class nominal contrast: demonstrative vs relative pronoun.

### P33 — QS 107:1 `الَّذِي يُكَذِّبُ بِالدِّينِ`
**Decision: PASS-WITH-NOTE.** Suitable only if relation-lite scoring stops at identifying isim maushul and local silah boundary; no referential dependency required.

### P34 — QS 110:1–2 conditional boundary
**Decision: HOLD-PREMATURE.** Asking which verbal units remain inside the condition risks requiring interclausal scope judgment that belongs at K31+/Stage 3. Keep out of automated L10 routing until rewritten to pure marker/local-form recognition.

### P35 — QS 2:2–3 mixed prerequisite probe
**Decision: PASS-CANDIDATE.** Clean multi-form classification with explicit ban on full sentence relation.

### P36 — QS 1:5–7 final discriminator
**Decision: PASS-WITH-NOTE.** High diagnostic value but segmented rubric is mandatory. Score only explicit K13–K30 operations; do not infer mastery from one aggregate answer.

## 5. Current disposition count

For P25–P36:
- PASS-CANDIDATE: **4** — P26, P29, P32, P35
- PASS-WITH-NOTE: **6** — P25, P27, P28, P31, P33, P36
- REWRITE: **1** — P30
- HOLD-PREMATURE: **1** — P34

For P01–P24:
- REVIEW-PENDING / NORMALIZATION-RECOVERY: **24**

Production-enabled: **0/36**.

## 6. Structural findings

1. The biggest L10 risk is not authenticity but **scope leakage into Stage 3**.
2. Marker-recognition items remain useful when the prompt explicitly forbids full clause-relation analysis.
3. Mixed items require segmented rubrics so one correct label does not conceal another failed prerequisite.
4. P30 and P34 should be versioned rather than silently overwritten once pilot IDs are canonicalized.
5. Pool completeness and production readiness remain separate metrics.

## 7. Next actions

1. Recover/normalize P01–P24 as complete registry records.
2. Create rewrite candidates for P30 and P34.
3. Add review fields to all 36 L10 registry rows with `production_enabled=false`.
4. Run duplicate-function audit after normalization.
5. Continue quality screen to L13 while recovery work proceeds in parallel.

## 8. Gate decision

**L10 remains QUALITY-REVIEW READY, NOT PRODUCTION-FROZEN.**
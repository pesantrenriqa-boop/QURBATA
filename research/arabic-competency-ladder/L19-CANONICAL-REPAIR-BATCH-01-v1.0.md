# L19 Canonical Repair — Batch 01 (K41–K48) v1.0

**Status:** DRAFT CANONICAL REPAIR — NOT PRODUCTION ENABLED  
**Checkpoint:** L19  
**Scope:** canonical K41–K48  
**Policy:** one explicit operation per target; prerequisite success alone does not earn target credit.

## K41 — hidden/implicit verbal subject
- ID: `ARB-PL-L19-K41-R01-v1.0`
- Reference: QS 96:1
- Span: `اقْرَأْ`
- Task: identify the subject of the imperative although no separate noun/pronoun is overtly written.
- Expected: implicit second-person singular subject (`أنت`) encoded by the imperative form.
- Ambiguity: LOW
- Action: NEW

## K42 — relative-clause / silah relation
- ID: `ARB-PL-L19-K42-R01-v1.0`
- Reference: QS 1:7
- Span: `الَّذِينَ أَنْعَمْتَ عَلَيْهِمْ`
- Task: identify the relative head and the unit functioning as its silah.
- Expected: `الذين` = relative head; `أنعمت عليهم` = silah.
- Ambiguity: LOW–MEDIUM
- Action: REWRITE from legacy P03 with narrower rubric.

## K43 — return-link / ‘āid relation
- ID: `ARB-PL-L19-K43-R01-v1.0`
- Reference: QS 1:7
- Span: `الَّذِينَ أَنْعَمْتَ عَلَيْهِمْ`
- Task: locate the element inside the silah that links back to the relative head.
- Expected: attached pronoun `هم` in `عليهم` functions as the return-link to `الذين` under the target analysis.
- Ambiguity: MEDIUM
- Action: NEW/REWRITE; Arabic-content review mandatory.

## K44 — conditional marker/domain recognition
- ID: `ARB-PL-L19-K44-R01-v1.0`
- Reference: QS 110:1
- Span: `إِذَا جَاءَ نَصْرُ اللَّهِ وَالْفَتْحُ`
- Task: identify the conditional/temporal opener and delimit the local domain opened by it without supplying the response.
- Expected: `إذا` opens the domain; following verbal material remains inside that domain.
- Ambiguity: MEDIUM
- Action: NEW from legacy conditional material.

## K45 — protasis relation
- ID: `ARB-PL-L19-K45-R01-v1.0`
- Reference: QS 3:160
- Span: `إِن يَنصُرْكُمُ اللَّهُ`
- Task: identify the conditional protasis as a structural unit and its marker.
- Expected: `إن` = condition marker; `ينصركم الله` = protasis unit.
- Ambiguity: LOW
- Action: NEW

## K46 — result/jawab relation
- ID: `ARB-PL-L19-K46-R01-v1.0`
- Reference: QS 3:160
- Span: `إِن يَنصُرْكُمُ اللَّهُ فَلَا غَالِبَ لَكُمْ`
- Task: identify the response/result unit and the explicit linker.
- Expected: `فلا غالب لكم` = result/jawab; `فـ` links it to the condition.
- Ambiguity: LOW
- Action: NEW

## K47 — full condition-result mapping
- ID: `ARB-PL-L19-K47-R01-v1.0`
- Reference: QS 4:59
- Span: `فَإِن تَنَازَعْتُمْ فِي شَيْءٍ فَرُدُّوهُ إِلَى اللَّهِ`
- Task: map protasis and response as two related units; internal PP material must not break the relation.
- Expected: `إن تنازعتم في شيء` = protasis; `فردوه إلى الله` = response.
- Ambiguity: LOW
- Action: KEEP/REMAP from legacy P20/P14 family.

## K48 — conditional integration transfer
- ID: `ARB-PL-L19-K48-R01-v1.0`
- Reference: QS 110:1–3
- Span: `إِذَا جَاءَ نَصْرُ اللَّهِ ... فَسَبِّحْ بِحَمْدِ رَبِّكَ`
- Task: retain the conditional domain across coordinated/internal material and identify the later response.
- Expected: the `إذا` domain remains active through the preceding material; `فسبح...` is mapped as the response at the target structural ceiling.
- Ambiguity: MEDIUM
- Action: REWRITE from legacy P02/P12 with segmented rubric.

## Batch result

K41–K48 now have **8/8 explicit draft canonical candidates**.

Legacy items remain traceable but do not receive canonical credit unless promoted through these narrowed function definitions.

Remaining L19 repair: **K49–K57**, with special care for mood-sensitive morphology and ellipsis/dependency nodes. All items remain `production_enabled=false` pending Arabic-content review and pilot validation.
# L21 Canonical Repair — Batch 01 K58–K67 v1.0

**Status:** DRAFT CANONICAL REPAIR — NOT PRODUCTION ENABLED  
**Checkpoint:** L21  
**Canonical band:** K58–K67  
**Evidence basis:** authoritative K58–K67 registry + repository clean-bank/evidence-gate records + surviving L21 historical items.  
**Rule:** relation validity outranks historical slot numbering; ambiguous discourse relations remain HOLD/REVIEW rather than being forced into coverage.

## K58 — Simple Inter-Clausal Coordination
- Candidate ID: `ARB-PL-L21-K58-R01-v1.0`
- Source: legacy L21-P25.
- Reference: QS 17:81
- Span: `جَاءَ الْحَقُّ وَزَهَقَ الْبَاطِلُ`
- Operation: identify clause 1, clause 2, overt `و`, and classify the link as clause-level coordination.
- Expected: `جاء الحق` and `زهق الباطل` are two complete local clauses linked by `و`.
- Decision: **KEEP/REMAP**.
- Ambiguity: LOW.

## K59 — Temporal Sequencing with `ثم`
- Candidate ID: `ARB-PL-L21-K59-R01-v1.0`
- Reference: QS 80:21–22
- Span: `ثُمَّ أَمَاتَهُ فَأَقْبَرَهُ ۝ ثُمَّ إِذَا شَاءَ أَنشَرَهُ`
- Operation: identify two clause/event units linked by overt `ثم` and state the ordered succession only; do not require full `التراخي` theory.
- Expected: later clause/event is presented after the earlier event through overt `ثم` sequencing.
- Decision: **NEW — ARABIC CONTENT REVIEW REQUIRED**.
- Ambiguity: MEDIUM because the exact scored clause boundaries must be fixed before pilot use.

## K60 — Relative-Clause Boundary (`صلة الموصول`)
- Candidate ID: `ARB-PL-L21-K60-R01-v1.0`
- Source family: legacy L21-P27/P04.
- Reference: QS 2:3
- Span: `الَّذِينَ يُؤْمِنُونَ بِالْغَيْبِ وَيُقِيمُونَ الصَّلَاةَ`
- Operation: identify `الذين` and delimit the following `صلة الموصول`; no explicit-`عائد` scoring is required.
- Expected: relative marker is `الذين`; the coordinated verbal material belongs inside its silah in the selected span.
- Decision: **REWRITE/REMAP**.
- Ambiguity: MEDIUM.

## K61 — Explicit Relative Resumptive (`العائد`)
- Candidate ID: `ARB-PL-L21-K61-R01-v1.0`
- Reference: QS 1:7
- Span: `الَّذِينَ أَنْعَمْتَ عَلَيْهِمْ`
- Operation: after delimiting the silah, identify the overt resumptive pronoun and resolve it to the relative expression.
- Expected: `هم` in `عليهم` is the overt local resumptive referring back to `الذين` under the target analysis.
- Decision: **NEW/REUSE FROM EARLIER RELATIVE EVIDENCE**.
- Ambiguity: MEDIUM; reviewer must approve the pedagogical wording.

## K62 — Contrast / Correction with `لكن`
- Candidate ID: `ARB-PL-L21-K62-R01-v1.0`
- Reference: QS 2:260
- Span: `قَالَ بَلَىٰ وَلَٰكِن لِّيَطْمَئِنَّ قَلْبِي`
- Operation: identify proposition A and the proposition introduced by `لكن`, then state what expectation/claim B qualifies or corrects. Translation of `لكن` alone earns no target credit.
- Expected: `بلى` affirms the prior proposition; `ولكن ليطمئن قلبي` introduces the corrective/qualifying proposition in the local discourse relation.
- Decision: **NEW — REVIEW REQUIRED**.
- Ambiguity: MEDIUM because prompt must avoid requiring theological interpretation.

## K63 — Result / Consequence
- Candidate state: **HOLD-EVIDENCE-SELECTION**.
- Reason: a surface `فـ` cannot be admitted by form alone; repository policy explicitly excludes cases that are merely `فاء جواب الشرط`, simple sequencing, or discourse continuation.
- Required next action: select an occurrence from the K63 evidence/clean bank where A→RESULT B is independently prevalidated.
- Coverage credit: **NOT YET**.

## K64 — Cause / Reason
- Candidate state: **HOLD-EVIDENCE-SELECTION**.
- Reason: canonical policy requires an overt validated explanatory/reason relation and excludes purpose, condition-response, and tafsir-only causal inference.
- Required next action: select an occurrence from the K64 evidence/clean bank with stable `A ← REASON B` direction.
- Coverage credit: **NOT YET**.

## K65 — Exception / Restriction with `إلا`
- Candidate ID: `ARB-PL-L21-K65-R01-v1.0`
- Reference: QS 103:2–3
- Span: `إِنَّ الْإِنسَانَ لَفِي خُسْرٍ ۝ إِلَّا الَّذِينَ آمَنُوا ...`
- Operation: identify the left-side general domain and the overt restricted/excluded group after `إلا`; do not require full `باب الاستثناء` subtype or post-`إلا` i‘rab theory.
- Expected: general domain concerns `الإنسان` in loss; `الذين آمنوا...` is the overt restricted/excepted group for the target relation.
- Decision: **NEW/REWRITE FROM LEGACY SURAH-103 CAPSTONE MATERIAL**.
- Ambiguity: MEDIUM; exact scope rubric must be content-reviewed.

## K66 — Purpose / Goal
- Retained dedicated candidates from `L21-CANONICAL-COVERAGE-K66-K67-v1.0.md`:
  - `ARB-PL-L21-K66-A-v1.0` — QS 20:44 `فَقُولَا لَهُ قَوْلًا لَيِّنًا لَعَلَّهُ يَتَذَكَّرُ أَوْ يَخْشَىٰ`
  - `ARB-PL-L21-K66-B-v1.0` — QS 2:21 `اعْبُدُوا رَبَّكُمُ ... لَعَلَّكُمْ تَتَّقُونَ`
- Decision: **RETAIN AS REVIEW CANDIDATES**.
- Gate: reviewer must confirm that the selected `لعل` constructions are appropriate for the canonical purpose/goal operation rather than a different semantic label in the specific pedagogical framing.
- production_enabled: false.

## K67 — Concession / Counterexpectation
- Retained dedicated candidates from `L21-CANONICAL-COVERAGE-K66-K67-v1.0.md`:
  - `ARB-PL-L21-K67-A-v1.0` — QS 2:216 `وَعَسَىٰ أَن تَكْرَهُوا شَيْئًا وَهُوَ خَيْرٌ لَّكُمْ`
  - `ARB-PL-L21-K67-B-v1.0` — QS 2:216 `وَعَسَىٰ أَن تُحِبُّوا شَيْئًا وَهُوَ شَرٌّ لَّكُمْ`
- Decision: **RETAIN AS REVIEW CANDIDATES**.
- Gate: reviewer must verify that the item elicits defeated expectation/counterexpectation, not ordinary contrast or theological interpretation.
- production_enabled: false.

## Batch result

Canonical item state after this batch:
- K58: explicit candidate ✓
- K59: explicit review candidate ✓
- K60: explicit candidate ✓
- K61: explicit review candidate ✓
- K62: explicit review candidate ✓
- K63: HOLD — clean result occurrence still required
- K64: HOLD — clean cause/reason occurrence still required
- K65: explicit review candidate ✓
- K66: two review candidates retained ✓
- K67: two review candidates retained ✓

**Explicit candidate coverage: 8/10.**  
**Strict canonical coverage claim: 8/10 provisional, not 10/10.**

## Next execution

1. fetch K63 result/consequence evidence bank and choose one prevalidated occurrence;
2. fetch K64 cause/reason clean bank and choose one prevalidated occurrence;
3. content-review K59/K61/K62/K65/K66/K67 ambiguity;
4. after K63/K64 closure, issue `L21-CANONICAL-COVERAGE-CLOSURE-v1.0.md` and only then declare L21 10/10 draft coverage.

All records remain `production_enabled=false`.
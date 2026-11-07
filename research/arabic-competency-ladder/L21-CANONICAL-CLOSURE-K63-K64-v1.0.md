# L21 Canonical Closure — K63–K64 v1.0

**Status:** DRAFT CANONICAL CANDIDATE CLOSURE — NOT PRODUCTION ENABLED  
**Checkpoint:** L21  
**Purpose:** close the last two evidence-normalization gaps using externally validated occurrence-level linguistic evidence.  
**External evidence source:** Quranic Arabic Corpus (word morphology / syntactic annotation).  
**Rule:** these records are new evidence-normalized candidates, not recovered historical wording.

## K63 — Result / Consequence

- Candidate ID: `ARB-PL-L21-K63-R01-v1.0`
- Canonical target: K63 `REL-RESULT-CONSEQUENCE`
- Qur'an reference: QS 80:4
- Target span: `أَوْ يَذَّكَّرُ فَتَنفَعَهُ الذِّكْرَىٰ`
- Proposition A: `يَذَّكَّرُ`
- Explicit linker: `فـ` in `فَتَنفَعَهُ`
- Proposition B: `تَنفَعَهُ الذِّكْرَىٰ`
- External linguistic validation: Quranic Arabic Corpus annotates the prefixed `فـ` in `فَتَنفَعَهُ` as **CAUS / فاء سببية** and describes it as a particle used in a resultative sense; the following mudhari‘ is analyzed as mansub.
- Learner operation: identify A and B, locate the overt prevalidated linker, and state B as the result/consequence enabled by A. The learner is not asked to derive the taxonomy of `فـ`.
- Critical boundary:
  - not K59 mere temporal sequencing;
  - not K47/K48 condition→jawab architecture;
  - not a particle-identification item only.
- Prompt: `حدد المعنى الأول والمعنى الناتج عنه، ثم عيّن الرابط الظاهر بينهما.`
- Expected: `يذكر` supplies the preceding event/proposition; `فتنفعه الذكرى` is the result/consequence unit; `فـ` is the prevalidated resultative/causal linker in this occurrence.
- Ambiguity: LOW–MEDIUM
- Reviewer gate: Arabic-content reviewer must confirm proposition-boundary wording and that K63 scoring does not accidentally retest K52 nasb morphology.
- Source URL: `https://corpus.quran.com/wordmorphology.jsp?location=(80:4:3)`
- production_enabled: false

## K64 — Cause / Reason

- Candidate ID: `ARB-PL-L21-K64-R01-v1.0`
- Canonical target: K64 `REL-CAUSE-REASON`
- Qur'an reference: QS 2:61
- Target span: `ذَٰلِكَ بِأَنَّهُمْ كَانُوا يَكْفُرُونَ بِآيَاتِ اللَّهِ`
- Explained proposition/anaphoric proposition pointer: `ذَٰلِكَ` refers locally to the preceding stated condition/state in the discourse.
- Explicit reason construction: `بِأَنَّهُمْ كَانُوا يَكْفُرُونَ بِآيَاتِ اللَّهِ`
- External linguistic validation: Quranic Arabic Corpus glosses `بِأَنَّهُمْ` in QS 2:61 as “because they” and analyzes it morphologically as preposition `بـ` + accusative particle `أنّ` + attached pronoun; its treebank displays `ذَٰلِكَ` followed by the `بِأَنَّهُمْ ...` reason construction.
- Learner operation: identify what is being explained and identify the overt reason proposition, then state the direction `A ← REASON B`.
- Critical boundary:
  - not K66 purpose/goal;
  - not K63 result/consequence direction;
  - no tafsir-only causal inference is needed because the reason construction is overt.
- Prompt: `ما المعنى الذي يفسَّر هنا؟ وما العبارة التي تبيّن سببه؟`
- Expected: `ذلك` points to the preceding explained state/proposition; `بأنهم كانوا يكفرون بآيات الله` supplies the explicit reason/grounds.
- Ambiguity: MEDIUM
- Reviewer gate: human review must verify the chosen left-domain boundary so scoring does not require broad tafsir or the full preceding verse discourse.
- Source URLs:
  - `https://corpus.quran.com/wordbyword.jsp?chapter=2&verse=61`
  - `https://corpus.quran.com/treebank.jsp?chapter=2&token=45&verse=61`
- production_enabled: false

## Closure result

L21 current canonical candidate coverage after this file:
- K58 ✓
- K59 ✓
- K60 ✓
- K61 ✓
- K62 ✓
- K63 ✓ — this closure
- K64 ✓ — this closure
- K65 ✓
- K66 ✓
- K67 ✓

**L21 draft canonical candidate coverage: 10/10 = 100%.**

## End-to-end ladder state

With the previous L04, L10, L13, and L19 canonical repair work:
- K01–K12: draft candidate coverage established;
- K13–K30: draft candidate coverage established;
- K31–K40: draft candidate coverage established;
- K41–K57: draft candidate coverage established;
- K58–K67: draft candidate coverage established.

Therefore **K01–K67 now has end-to-end draft placement candidate coverage**.

This is **not** production readiness. Required next gates remain:
1. Arabic-content review and alternate-analysis review;
2. duplicate-function/verse-family audit across canonical candidates;
3. normalized master item registry;
4. machine-readable checkpoint assembly rules;
5. pilot response collection;
6. item statistics / psychometric calibration;
7. cut-score validation;
8. controlled production enablement.

# L19 Canonical Repair — Batch 03 Evidence Items K49–K57 v1.0

**Status:** DRAFT EVIDENCE-GROUNDED PLACEMENT CANDIDATES — NOT PRODUCTION ENABLED  
**Checkpoint:** L19  
**Canonical range:** K49–K57  
**Authority:** canonical definitions recovered from `CANONICAL-REGISTRY-K47-K57-v0.1.md`; occurrence selection cross-checked against Qur'anic text and remains subject to Arabic-content review before promotion.

## K49 — MORPH-JAZM-SUKUN
- ID: `ARB-PL-L19-K49-R01-v1.0`
- Reference: QS 47:7
- Span: `إِن تَنصُرُوا اللَّهَ يَنصُرْكُمْ`
- Target token: `يَنصُرْكُمْ`
- Operation: identify mudhari‘ in validated conditional response and connect the transparent sukūn on final root consonant to jazm.
- Expected: `ينصرْ` is mudhari‘ majzum; visible sukūn is the target K49 effect.
- Exclusion: do not score `تنصروا` here because its jazm realization is deletion of nūn (K51).
- Ambiguity: LOW–MEDIUM
- production_enabled: false

## K50 — MORPH-JAZM-DELETE-WEAK
- ID: `ARB-PL-L19-K50-R01-v1.0`
- Reference: QS 7:178
- Span: `مَن يَهْدِ اللَّهُ فَهُوَ الْمُهْتَدِي`
- Target token: `يَهْدِ`
- Operation: recognize the familiar weak-final base and reconstruct the deleted final weak segment as the jussive effect.
- Expected: target is a weak-final mudhari‘ in jussive condition environment; the missing final weak letter is the K50 realization.
- Ambiguity: MEDIUM
- reviewer_note: verify base-form reconstruction and pedagogical orthography before production.
- production_enabled: false

## K51 — MORPH-JAZM-DELETE-NUN
- ID: `ARB-PL-L19-K51-R01-v1.0`
- Reference: QS 47:7
- Span: `إِن تَنصُرُوا اللَّهَ يَنصُرْكُمْ`
- Target token: `تَنصُرُوا`
- Operation: compare with the familiar nūn-bearing indicative pattern and identify absence of inflectional nūn as jazm effect.
- Expected: conditional environment validates jazm; deletion of nūn is the target sign.
- Ambiguity: MEDIUM
- reviewer_note: rubric must distinguish inflectional nūn from lexical material.
- production_enabled: false

## K52 — MORPH-NASB-FATHA
- ID: `ARB-PL-L19-K52-R01-v1.0`
- Reference: QS 20:91
- Span: `لَن نَّبْرَحَ عَلَيْهِ عَاكِفِينَ`
- Target token: `نَبْرَحَ`
- Operation: identify overt nāṣib `لن`, identify the mudhari‘, and connect visible final fatḥah to nasb.
- Expected: `لن` governs the target occurrence; `نبرحَ` is mansub with transparent fatḥah.
- Ambiguity: LOW
- production_enabled: false

## K53 — SYN-ELLIPSIS-HIDDEN-AN
- ID: `ARB-PL-L19-K53-R01-v1.0`
- Reference: QS 48:2
- Span: `لِّيَغْفِرَ لَكَ اللَّهُ`
- Target token: `لِيَغْفِرَ`
- Operation: identify the controlled trigger context, reconstruct one hidden `أن`, and connect it to nasb of the mudhari‘.
- Expected: pedagogical analysis treats the purposive lām construction as containing a governed mudhari‘ through reconstructed `أن` at the K53 ceiling.
- Ambiguity: MEDIUM–HIGH
- reviewer_note: mandatory traditional-grammar content review; alternate analysis policy must be explicit before automated scoring.
- production_enabled: false

## K54 — REL-FA-JAWAB-PREDICT
- ID: `ARB-PL-L19-K54-R01-v1.0`
- Reference: QS 3:160
- Span: `إِن يَنصُرْكُمُ اللَّهُ فَلَا غَالِبَ لَكُمْ`
- Operation: classify the response as nominal, predict that fā’ al-jawāb is required, then verify the overt `فـ`.
- Expected: `لا غالب لكم` is a nominal response frame; learner predicts/verifies initial `فـ` as jawab linker.
- Ambiguity: LOW–MEDIUM
- production_enabled: false

## K55 — MORPH-RAF-DAMMA
- ID: `ARB-PL-L19-K55-R01-v1.0`
- Reference: QS 2:216
- Span: `وَاللَّهُ يَعْلَمُ وَأَنتُمْ لَا تَعْلَمُونَ`
- Target token: `يَعْلَمُ`
- Operation: validate absence of an active local nāṣib/jāzim and identify overt final ḍammah as raf‘.
- Expected: `يعلمُ` is a familiar sound-final mudhari‘ in raf‘ environment; overt ḍammah is the K55 sign.
- Ambiguity: LOW
- production_enabled: false

## K56 — MORPH-RAF-THUBUT-NUN
- ID: `ARB-PL-L19-K56-R01-v1.0`
- Reference: QS 2:3
- Span: `الَّذِينَ يُؤْمِنُونَ بِالْغَيْبِ`
- Target token: `يُؤْمِنُونَ`
- Operation: validate raf‘ environment and identify retained inflectional nūn as the raf‘ sign in a familiar nūn-bearing pattern.
- Expected: nūn is retained; this retention is the target K56 evidence.
- Ambiguity: LOW–MEDIUM
- reviewer_note: rubric must not reduce the task to generic plural recognition.
- production_enabled: false

## K57 — MORPH-RAF-ESTIMATED-DAMMA
- ID: `ARB-PL-L19-K57-R01-v1.0`
- Reference: QS 28:20
- Span: `وَجَاءَ رَجُلٌ مِّنْ أَقْصَى الْمَدِينَةِ يَسْعَىٰ`
- Target token: `يَسْعَىٰ`
- Operation: identify familiar weak-final mudhari‘, validate raf‘ environment, note absence of overt final ḍammah, and classify the raf‘ sign as estimated.
- Expected: `يسعى` is marfu‘ with estimated ḍammah on the alif-final form at this controlled ceiling.
- Ambiguity: MEDIUM
- reviewer_note: mandatory morphology review before production.
- production_enabled: false

## Batch completion

K49–K57 now have **9/9 explicit evidence-grounded draft placement candidates**.

Combined with Batch 01:
- K41–K48: 8/8 candidates
- K49–K57: 9/9 candidates
- **L19 K41–K57 draft canonical item coverage: 17/17 = 100%**

This is not production readiness. Required next gates:
1. re-audit K41–K48 against exact authoritative definitions, especially K44–K46;
2. Arabic-content review of K43, K50, K51, K53, K54, K56, K57;
3. duplicate/function-signature audit;
4. pilot calibration and routing validation;
5. production registry promotion.
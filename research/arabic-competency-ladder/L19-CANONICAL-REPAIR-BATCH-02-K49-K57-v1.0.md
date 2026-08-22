# L19 Canonical Repair — Batch 02 K49–K57 v1.0

**Status:** AUTHORITATIVE-DEFINITION-ALIGNED REPAIR PLAN — NOT PRODUCTION ENABLED  
**Checkpoint:** L19  
**Authoritative source:** `CANONICAL-REGISTRY-K47-K57-v0.1.md` recovered from PR #4 patch.  
**Rule:** no item receives canonical credit unless the Qur'anic occurrence visibly/defensibly instantiates the exact mood/ellipsis operation.

## Corrected authoritative definitions

### K49 — MORPH-JAZM-SUKUN
Recognize transparent final sukūn as jazm on a familiar mudhari‘ inside a validated simple conditional/jussive environment.

### K50 — MORPH-JAZM-DELETE-WEAK
Recognize jazm through deletion of the final weak segment on a familiar weak-final mudhari‘.

### K51 — MORPH-JAZM-DELETE-NUN
Recognize jazm through deletion of inflectional nūn on a familiar nūn-bearing mudhari‘ pattern.

### K52 — MORPH-NASB-FATHA
Recognize transparent final fatḥah as nasb after an overt validated nāṣib.

### K53 — SYN-ELLIPSIS-HIDDEN-AN
Reconstruct one validated hidden `أن` as governor of a mudhari‘ in a controlled trigger construction.

### K54 — REL-FA-JAWAB-PREDICT
Given a K47-valid condition whose response is nominal, predict that fā’ al-jawāb is required and verify the overt marker.

### K55 — MORPH-RAF-DAMMA
Recognize overt final ḍammah as raf‘ on a familiar sound-final mudhari‘ in an environment with no active nāṣib/jāzim.

### K56 — MORPH-RAF-THUBUT-NUN
Recognize raf‘ through retention of inflectional nūn on a familiar nūn-bearing mudhari‘ pattern.

### K57 — MORPH-RAF-ESTIMATED-DAMMA
Recognize raf‘ on a familiar weak-final mudhari‘ through estimated ḍammah, beginning with alif-final forms.

## Repair decisions

The legacy L19 pool was designed mainly around clause integration and therefore does **not** safely provide canonical K49–K57 coverage merely because old item numbers carried those labels. K49–K57 require morphology/ellipsis evidence at token level.

Accordingly:
- K49: **NEW ITEM REQUIRED**
- K50: **NEW ITEM REQUIRED**
- K51: **NEW ITEM REQUIRED**
- K52: **NEW ITEM REQUIRED**
- K53: **NEW ITEM REQUIRED**
- K54: **NEW/REWRITE REQUIRED** using a nominal conditional response with overt fā’
- K55: **NEW ITEM REQUIRED**
- K56: **NEW ITEM REQUIRED**
- K57: **NEW ITEM REQUIRED**

## Evidence sources already present in repository

The repository already contains dedicated evidence/stress artifacts for these nodes, including:
- `EVIDENCE-GATE-K49-JAZM-SUKUN-v0.1.md`
- `EVIDENCE-GATE-K50-JAZM-DELETE-WEAK-v0.1.md`
- `EVIDENCE-GATE-K51-DELETE-NUN-v0.1.md`
- `EVIDENCE-GATE-K52-NASB-FATHA-v0.1.md`
- `EVIDENCE-GATE-K53-HIDDEN-AN-v0.1.md`
- `DISTINCTNESS-EVIDENCE-K54-PREDICTIVE-FA-JAWAB-v0.1.md`
- `EVIDENCE-GATE-K55-RAF-DAMMA-v0.1.md`
- `EVIDENCE-GATE-K56-THUBUT-NUN-v0.1.md`
- `EVIDENCE-GATE-K57-ESTIMATED-DAMMA-v0.1.md`

These evidence artifacts, not memory or guessed examples, are the mandatory source for the final nine placement records.

## Coverage state after authoritative recovery

- K41–K48: 8/8 explicit draft candidates already created in Batch 01, but K44–K46 must be rechecked against their own authoritative definitions before final promotion because earlier summary labels may differ.
- K49–K57: 0/9 production candidates; **9/9 definitions recovered and repair actions fixed**.
- L19 definition-level alignment: **17/17 = 100%**.
- L19 item-level canonical coverage: **8/17 provisional; 9 evidence-grounded item builds still required**.
- production_enabled: 0.

## Next execution

Fetch the nine repository evidence artifacts, extract their validated Qur'anic occurrences and boundary notes, then create `L19-CANONICAL-REPAIR-BATCH-03-EVIDENCE-ITEMS-v1.0.md` with one placement candidate per K49–K57. No verse/reference may be invented to accelerate completion.
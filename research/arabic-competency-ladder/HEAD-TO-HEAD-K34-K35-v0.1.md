# Head-to-Head K34–K35 v0.1

**Status:** WORKING RESEARCH — NON-AUTHORITATIVE  
**Baseline:** K1–K33 DRAFT-FROZEN.

## Candidates

- K34-CAND — recognition `إِلَّا`
- K35-CAND — recognition `لَيْسَ`

## A. `إِلَّا` Recognition

Target:
- recognize the invariant token `إِلَّا` on occurrence;
- tag its exception/restriction role at recognition level only.

Strengths:
- invariant surface token;
- very local segmentation;
- no person/number/gender inflection;
- full exception construction can remain locked;
- does not require prior mastery of nominal or verbal inflection paradigms.

Risks:
- occurrences inside negation + restriction (`ما ... إلا`, `لا ... إلا`) can create broader scope;
- mustatsna i'rab and types of istitsna' are higher competencies and must remain locked;
- not every teaching example should include complex clause scope.

Judgement: **VERY STRONG EARLY RECOGNITION NODE.**

## B. `لَيْسَ` Recognition

Target:
- recognize `ليس` and carefully selected inflected forms as a negative copular verb family;
- do not yet analyze اسم ليس / خبر ليس.

Strengths:
- function relatively distinctive;
- links naturally to nominal predication already learned;
- Qur'anic use is pedagogically valuable.

Burden:
- inflected forms can carry person/number/gender morphology;
- full competence risks expanding into agreement/paradigm analysis;
- syntactically tied to a nominal predication frame, increasing latent complexity.

Judgement: **HIGH, BUT HEAVIER THAN `إِلَّا`.**

## Head-to-head result

Winner for earlier sequence position: **`إِلَّا`**.

Reasons:
1. lower morphological burden;
2. invariant token;
3. shorter hard-dependency chain;
4. cleaner separation between recognition and later construction;
5. lower risk of smuggling agreement/paradigm competence.

## Proposed order

- **K34-CAND — recognition `إِلَّا`**
- **K35-CAND — recognition `لَيْسَ`**

No dependency reversal found.

## Freeze gate status

### K34
`READY-FOR-DRAFT-FREEZE`

Conditions:
- occurrence must be tagged as `إلا` function;
- construction-level exception analysis remains locked;
- clean teaching set should prefer contexts whose surrounding dependencies are <= K34.

### K35
`CONDITIONALLY READY`

Conditions:
- define a restricted recognition family;
- do not require full conjugational paradigm;
- اسم ليس / خبر ليس remain locked;
- attached subject/person morphology must be tagged but not over-taught.

## Next

1. issue final gate K34;
2. build a restricted evidence policy for K35;
3. compare K35 `ليس` vs K36 limited `كان` family;
4. continue keeping construction effects separate from recognition.
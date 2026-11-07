# Counterexample Test K30–K31 v0.1

**Status:** WORKING RESEARCH — PRE-FREEZE  
**Baseline:** K1–K29 draft-frozen in research layer.

## Order under test

- K30-CAND — recognition future marker `سوف / سـ`
- K31-CAND — recognition hamzah istifham `أَ`

## K30 — Future marker recognition

Target:
- recognize occurrence-validated `سوف` or prefixed `سـ` marking futurity with mudhari'.

Dependencies:
- K7 mudhari' recognition;
- clitic segmentation for `سـ`.

Locked:
- detailed tense/aspect theory;
- rhetorical nuance;
- fa'il analysis;
- clause-level prediction.

Counterexample risks:
- `سـ` segmentation errors;
- assuming every future reading is marked by `سـ/سوف`;
- treating `سوف` and `سـ` as fully interchangeable semantically.

Result: **PASS WITH SEGMENTATION TAGGING**.

## K31 — Interrogative hamzah recognition

Target:
- recognize prefixed/initial hamzah functioning as interrogative marker on validated occurrences.

Dependencies:
- minimal token/clitic segmentation.

Locked:
- scope of question;
- hamzah taswiyah and other specialized uses;
- clause analysis after the marker.

Counterexample risks:
- orthographic/surface ambiguity;
- confusing lexical initial hamzah with interrogative hamzah;
- complex clitic stacks.

Result: **PASS WITH OCCURRENCE-SPECIFIC FUNCTION TAGGING**.

## Head-to-head conclusion

K30 remains earlier because it composes directly with already-frozen K7 mudhari' recognition. K31 is also lightweight, but its surface/function disambiguation burden is slightly higher.

No dependency reversal found.

## Freeze recommendation

- K30 READY FOR DRAFT-FREEZE
- K31 READY FOR DRAFT-FREEZE

## Next lightweight rescan

Before returning to fa'il mustatir or silah maushul, inspect:
- `قد` recognition with tense/aspect effects locked;
- `إنّ` recognition before its government effect;
- `كان` recognition before defective-verb syntax;
- `ليس` recognition;
- `لعلّ` / `لكنّ` only if atomicity and corpus yield justify separate nodes;
- adverbial/time-place recognition only if not too semantically broad.

Do not assume traditional chapter order; each node must still pass cumulative-only evidence.
# QURBATA Learning Progression Engine (LPE) v1 — Contract

Status: **REVIEW CANDIDATE — NOT FINAL BOOK CONTENT**

## Purpose

LPE determines *what should be taught next* before the Composer selects Quran objects. It sits between the pedagogical validity layer and the page composer.

Pipeline:

`Quran Corpus -> Candidate Engine -> Pedagogical Engine -> LPE -> Composer -> Semantic Gate -> Layout -> Render`

## Governing principle

A Quran object being technically valid is not enough. The object must also be appropriate for the learner's current progression stage.

## Jilid 1 hard constraints

1. Total instructional pages: **40**.
2. Jilid 1 uses staged reading objects of **1, 2, and 3 pedagogical letter-units** according to page progression.
3. The Composer MUST NOT force every reading slot to contain two letters.
4. `AWAIL_AL_SUWAR` is **forbidden in Jilid 1**.
5. Page **20** contains a `LETTER_NAMES` instructional injection.
6. Page **40** contains a `LETTER_NAMES` instructional/review injection.
7. Letter-name content is distinct from reading-object content and MUST NOT be mislabeled as Awailus Suwar.
8. Layout remains generative; the pedagogical contract, not the visual grid, determines object length.

## Page metadata contract

Every generated page MUST expose human-readable learning metadata in addition to codes:

- competency code(s), e.g. `C0005`;
- competency description(s);
- memorization target code/reference if present;
- memorization target description;
- Arabic-language target code/reference if present;
- Arabic-language target description;
- page role;
- new-material/review status.

A code without its description is insufficient for production output.

## Learning-object progression

LPE distinguishes object length from object type.

- `L1`: one pedagogical letter-unit;
- `L2`: two pedagogical letter-units;
- `L3`: three pedagogical letter-units.

A page MAY mix previously mastered lengths with the current target length. Review objects must come only from material already introduced.

The exact new/review ratio is controlled by the progression blueprint and MUST NOT be inferred by the renderer.

## Injection layer

Instructional injections are independent of reading-object selection. Supported injection categories begin with:

- `LETTER_NAMES`;
- `MEMORIZATION`;
- `ARABIC_LANGUAGE`;
- `AKHLAQ`;
- `HADITH`;
- `ASSESSMENT`.

For Jilid 1 v2, the only page-number injection fixed by this contract is:

- Page 20: `LETTER_NAMES`;
- Page 40: `LETTER_NAMES`.

Other injections require an explicit content registry and are not to be invented by the Composer.

## Content prohibitions

For Jilid 1:

- no Awailus Suwar;
- no object length above the page's LPE allowance;
- no unsupported mark introduced ahead of its competency;
- no fabricated Quran source text;
- no manually patched PDF content outside the source engines.

## Typography / harakat responsibility

LPE does not draw Arabic marks. It declares pedagogical intent only.

Harakat rendering is delegated to the Arabic typography/harakat engine, which must preserve:

- recognizable canonical mark shape;
- appropriate stroke weight;
- correct anchor relative to each base letter;
- visual distinction between fathah, kasrah, and dhammah;
- no dot-like substitute for a vowel mark;
- no excessively thick generic line used as a final harakat glyph.

## System anti-regression rules

A Jilid 1 production build MUST fail if any of these occur:

- page count != 40;
- Awailus Suwar appears anywhere in Jilid 1;
- page 20 lacks `LETTER_NAMES`;
- page 40 lacks `LETTER_NAMES`;
- a reading object violates its allowed pedagogical unit length;
- competency code is printed without a description;
- a declared memorization or Arabic-language target is printed without a description;
- generated content bypasses the LPE contract.

## Freeze policy

The previous 36-page canonical build remains a technical renderer milestone only. It is **not** the final pedagogical Jilid 1 specification.

No Jilid 1 final-production tag may be created until the 40-page LPE blueprint, content registries, harakat typography, semantic gate, and visual QA all pass.
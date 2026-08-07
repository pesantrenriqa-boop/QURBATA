# QURBATA Content Registry Engine (CRE) v1 — Contract

Status: **REVIEW CANDIDATE — NOT FINAL BOOK CONTENT**

## Purpose

CRE separates instructional content metadata from the Composer. The Composer selects and orders reading objects; CRE provides the human-readable content that surrounds those objects on a page.

Pipeline:

`Quran Corpus -> Candidate Engine -> Pedagogical Engine -> GLE -> LPE -> CRE -> Composer -> Semantic Gate -> Layout -> Renderer`

## Registry principle

No production renderer or composer may invent instructional metadata. Codes, descriptions, page injections, memorization targets, Arabic-language targets, assessment targets, and footer labels must come from versioned registries.

## Core registries

CRE v1 recognizes these domains:

- `COMPETENCY` — code plus human-readable description;
- `LETTER_NAMES` — canonical letter-name instructional content;
- `MEMORIZATION` — memorization target code/reference plus description;
- `ARABIC_LANGUAGE` — Arabic-language target code/reference plus description;
- `AKHLAQ` — akhlaq/adab target code plus description;
- `ASSESSMENT` — assessment target and mastery rule;
- `INJECTION` — page-numbered special instructional blocks;
- `FOOTER_PROFILE` — which registry fields must be rendered on a page.

## Jilid 1 v1 rules

1. Jilid 1 defines instructional pages 1–40.
2. Page 20 injection is `LETTER_NAMES`.
3. Page 40 injection is `LETTER_NAMES`.
4. No `AWAIL_AL_SUWAR` injection is allowed in Jilid 1.
5. Page 20 and page 40 letter-name content must be sourced from `JILID-1-LETTER-NAME-REGISTRY-V1.csv`.
6. Competency codes must resolve to non-empty descriptions.
7. A memorization code, Arabic-language code, akhlaq code, or assessment code may be `UNASSIGNED` during review-candidate development, but the corresponding description must explicitly state that it is not yet assigned.
8. A final-production build MUST reject every `UNASSIGNED` instructional target.
9. The renderer must display code **and** description together for all assigned instructional targets.
10. CRE does not decide the reading-object progression; that remains LPE/GLE responsibility.

## Footer profile

Jilid 1 uses footer profile `J1_STANDARD_V1`. At minimum, a rendered instructional page must be able to expose:

- competency code(s);
- competency description(s);
- memorization code/reference and description;
- Arabic-language code/reference and description;
- page role;
- special injection when present.

Additional fields such as akhlaq and assessment may be enabled when their registries are populated.

## Anti-regression rules

A CRE review build fails if:

- page-content registry does not define pages 1–40 exactly once;
- page 20 or 40 does not resolve to `LETTER_NAMES`;
- another Jilid 1 page is incorrectly assigned `LETTER_NAMES` unless explicitly ratified in a later contract;
- `AWAIL_AL_SUWAR` appears as an injection;
- any assigned content code has an empty description;
- an unknown footer profile is referenced;
- letter-name registry does not contain 28 canonical letters split 14/14 across pages 20 and 40.

A CRE final-production build additionally fails if any instructional target remains `UNASSIGNED`.

## Freeze policy

Passing CRE v1 means the registry architecture is executable. It does **not** mean memorization, Arabic-language, akhlaq, or assessment content has been pedagogically finalized.

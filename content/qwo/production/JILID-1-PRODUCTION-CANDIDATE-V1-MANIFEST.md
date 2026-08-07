# QURBATA Jilid 1 — Production Candidate v1 Manifest

Status: **PRODUCTION CANDIDATE — NOT FINAL**

## Candidate scope

This candidate represents the first 40-page Jilid 1 build in which the pedagogical, Arabic typography, layout, review-distribution, and micro-progression rules are integrated.

## Hard pedagogical rules

- Total pages: **40**.
- Pages **20** and **40** are dedicated `LETTER_NAMES` checkpoints.
- All other pages contain **24 reading practice objects**.
- Slot pattern on every reading page:
  - slots 1–8: L1 (one independent letter-unit),
  - slots 9–16: L2 (two independent letter-units),
  - slots 17–24: L3 (three independent letter-units).
- L2/L3 are **not Arabic words** and must never be shaped as connected Arabic.
- Display policy: `DISCONNECTED_NO_SPACE`.
- Page 1 active letters: `ا ب ت ث` only.
- Future-letter leakage is forbidden.
- Page 1 is fathah-only.
- Harakat progression is controlled by the Jilid 1 pedagogical progression registry.
- After foundation, the target distribution is 50% current/new competency and 50% cumulative review.
- Review means prior competency with a different surface example where reasonably available; it does not mean copying identical examples by default.

## Current technical evidence

Expected/currently verified by local gates:

- `JILID1_COMPOSER_MICRO_PROGRESSION_GATE_V5=PASS`
- `JILID1_REVIEW_DISTRIBUTION_GATE_V1=PASS`
- `LAYOUT_YAML_V3_GATE=PASS`
- `QAE_TYPOGRAPHY_GATE_V2=PASS`
- `CANONICAL_RENDERER_V4=PASS`
- 40 pages rendered
- 912 reading objects rendered
- 28 letter-name entries rendered
- layout overflow = 0

## Arabic typography

Primary renderer: QAE native combining-mark profile.

Profile:

`content/qwo/arabic-engine/anchors/jilid-1-short-vowels-native-v2.yaml`

Human visual review has accepted the current Arabic glyph/harakat appearance as readable and non-overlapping.

## Candidate pipeline

`LPE/GLE -> PGE -> Composer v7 -> Review Distribution Gate -> Layout YAML v3 -> QAE Native v2 -> Canonical Renderer v4 -> PDF`

## Human QA still required before final freeze

Review at minimum these pages:

- 1–5: initial letter-family progression and L1/L2/L3 practice pattern;
- 16: first kasrah-stage page;
- 20: first letter-name checkpoint;
- 26: first dhammah-stage page;
- 37: mixed-harakat stage;
- 40: final letter-name checkpoint.

Check:

1. pedagogical order feels natural;
2. NEW/REVIEW balance is appropriate in practice, not only numerically;
3. no future letter or harakat appears early;
4. L2/L3 remain visually disconnected but close together;
5. target/metadata text is accurate and readable;
6. memorization/Arabic/akhlaq metadata are accurate;
7. no unwanted repetition pattern is visually distracting.

## Freeze rule

Do **not** create a final Jilid 1 tag until human QA explicitly approves the production candidate.

A production-candidate tag may be created after candidate verification, but it must not be named or described as final.

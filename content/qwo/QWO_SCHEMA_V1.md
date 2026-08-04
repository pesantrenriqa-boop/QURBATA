# QURBATA Word Object Schema V1

## Status
- Version: 1.0
- Scope: MASTER_QWO
- State: ACTIVE

## Purpose
This schema defines the minimum canonical structure for every QURBATA Word Object (QWO). A QWO represents one verified Qur'anic surface-form occurrence or one normalized lexical object linked to one or more verified occurrences.

## Required fields

| Field | Type | Rule |
|---|---|---|
| QWO_ID | string | Permanent unique identifier: `QWO-000001` |
| ArabicWord | string | Arabic surface form as used in the source occurrence |
| NormalizedWord | string | Search-normalized form without changing the canonical source text |
| Surah | integer | Surah number 1-114 |
| Ayah | integer | Ayah number in the cited surah |
| TokenPosition | integer | Position of the token inside the ayah when verified |
| Morphology | enum | `ISM`, `FIIL`, `HARF`, or `UNRESOLVED` |
| TargetCompetency | string | Primary QCI competency ID |
| RequiredCompetencies | list | Prerequisite QCI competency IDs separated by `|` |
| CumulativeCompetencies | list | All competencies exercised by the object |
| ReadingPattern | string | Pedagogical reading pattern such as CV, CVC, CVVC |
| ShapePattern | string | Connection and glyph-shape pattern |
| VisualFamily | string | Dominant visual-letter family |
| Difficulty | integer | Scale 1-5 |
| ReviewPriority | integer | Scale 1-5 |
| GeneratorWeight | decimal | Relative selection weight |
| DuplicateKey | string | Stable normalized grouping key |
| WhitelistLevel | string | Earliest approved curriculum level |
| Status | enum | `ACTIVE`, `REVIEW`, `HOLD`, `RETIRED` |
| SourceStatus | enum | `VERIFIED`, `PENDING`, `REJECTED` |
| Notes | string | Reviewer and pedagogical notes |

## Optional fields

- FrequencyQuran
- Root
- Lemma
- OrthographyClass
- TajwidTags
- ErrorRisks
- ReviewInterval
- LastReviewedAt
- ReviewedBy

## Validation gates

A QWO may become `ACTIVE` only when:

1. Arabic text and surah-ayah reference are verified.
2. `QWO_ID` is unique and permanent.
3. `TargetCompetency` exists in QCI.
4. Every required competency exists in QCI.
5. `WhitelistLevel` does not violate the dependency graph.
6. Difficulty, review priority, and generator weight are populated.
7. Duplicate grouping has been checked.

## Generator rule

The generator must never select a QWO solely because its Arabic form matches a level. Selection must also satisfy prerequisite competency, source verification, whitelist, review balance, and duplication rules.

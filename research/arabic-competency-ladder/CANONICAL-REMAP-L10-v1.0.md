# Canonical Remap — L10 Placement v1.0

**Status:** CANONICAL ALIGNMENT CONTROL — NON-PRODUCTION  
**Checkpoint:** L10  
**Authoritative band:** K13–K30 from `CANONICAL-REGISTRY-K01-K67-v0.1.md`  
**Scope:** R2 replacement P01–P24  
**Rule:** historical item text/version remains immutable; this file controls canonical targeting and live eligibility.

## 1. Canonical band K13–K30

- K13 REL-IDHAFAH-2N
- K14 REL-MAFUL-ZHAHIR
- K15 REC-PRON-ATT
- K16 REC-CONJ
- K17 REL-ADJ
- K18 REL-POSS-PRON
- K19 REL-CONJ-NOM
- K20 REL-PREP-PRON
- K21 REL-V-OBJ-PRON
- K22 REC-DEM
- K23 REC-REL
- K24 REL-DEM-PRED
- K25 REL-V-PP
- K26 REC-V-IMP
- K27 REC-NEG
- K28 REC-INT-HAL
- K29 REC-VOC-YA
- K30 REC-FUT

## 2. Item-level remap P01–P24

| Slot | Existing operation | Canonical disposition | Canonical target | Reason |
|---|---|---|---|---|
| P01 | attached pronoun recognition | CANONICAL-MATCH | K15 | Exact segmentation of attached pronoun. |
| P02 | noun + attached pronoun / possessive boundary | CANONICAL-REMAP-WITH-REWRITE | K18 | To score K18, the actual target must contain noun-host + attached possessive pronoun; current primary span `رب` is insufficient without comparator. |
| P03 | idafah | CANONICAL-MATCH | K13 | Exact local two-noun idafah. |
| P04 | noun–adjective | CANONICAL-MATCH | K17 | Exact na'at–man'ut relation. |
| P05 | preposition + attached pronoun | CANONICAL-MATCH | K20 | Exact PP-pronoun dependency. |
| P06 | plural verbal morphology | OUT-OF-BAND-HOLD | — | No K13–K30 core node for generic plural verbal morphology. |
| P07 | dual morphology | OUT-OF-BAND-HOLD | — | No canonical K13–K30 node for generic dual recognition. |
| P08 | feminine marker | OUT-OF-BAND-HOLD | — | No canonical node for generic feminine morphology in this band. |
| P09 | imperfect verbal prefix | OUT-OF-BAND-REMAP | K07 | This is earlier imperfect-verb recognition, not L10-band content. |
| P10 | idafah segmentation | CANONICAL-MATCH | K13 | Exact K13 transfer. |
| P11 | definiteness / ceiling control | OUT-OF-BAND-REMAP | K02 | Primarily tests earlier `الـ` recognition, not K13–K30. |
| P12 | attached pronoun + idafah + dual morphology | REWRITE-FOR-CANONICAL | K13/K15 + new in-band operation | Dual component has no canonical target; integrative item must be rebuilt with only K13–K30 operations. |
| P13 | attached object-pronoun decomposition | CANONICAL-REMAP-WITH-REWRITE | K21 primary, K15 prerequisite | K21 requires an actual verb + attached object-pronoun occurrence, not merely a comparator mentioned in prompt. |
| P14 | preposition + plural attached pronoun | CANONICAL-MATCH | K20 | Exact K20. |
| P15 | idafah transfer | CANONICAL-MATCH | K13 | Exact K13. |
| P16 | adjective agreement observation | CANONICAL-MATCH-WITH-NOTE | K17 | Score relation, not generic agreement morphology beyond K17. |
| P17 | dual morphology | OUT-OF-BAND-HOLD | — | No canonical K13–K30 node. |
| P18 | plural verbal morphology | OUT-OF-BAND-HOLD | — | No canonical K13–K30 node. |
| P19 | feminine noun morphology | OUT-OF-BAND-HOLD | — | No canonical K13–K30 node. |
| P20 | definite article contrast | OUT-OF-BAND-REMAP | K02 | Earlier-band recognition. |
| P21 | preposition + attached pronoun | CANONICAL-MATCH | K20 | Exact K20. |
| P22 | idafah + definiteness | CANONICAL-MATCH-WITH-NOTE | K13 primary | Definiteness is prerequisite/observable only; K13 is scored target. |
| P23 | pronoun decomposition + idafah | CANONICAL-REMAP | K15/K20 + K13 | Valid in-band prerequisite/integration item if `عليهم` scores K20, not generic pronoun only. |
| P24 | plural + dual + PP-pronoun | REWRITE-FOR-CANONICAL | K20 + two replacement K13–K30 operations | Two of three current operations have no canonical node in the band. |

## 3. Disposition totals

For P01–P24:
- CANONICAL-MATCH / MATCH-WITH-NOTE: **10** — P01, P03, P04, P05, P10, P14, P15, P16, P21, P22
- CANONICAL-REMAP / REMAP-WITH-REWRITE: **4** — P02, P13, P23, plus P09/P11/P20 are out-of-band remaps tracked separately
- OUT-OF-BAND-HOLD: **6** — P06, P07, P08, P17, P18, P19
- OUT-OF-BAND-REMAP TO EARLIER K: **3** — P09→K07, P11→K02, P20→K02
- REWRITE-FOR-CANONICAL: **2** — P12, P24

No item becomes production-enabled through remapping.

## 4. Canonical coverage audit

Current R2 replacement set is heavily concentrated on K13/K15/K17/K20. It does **not** yet provide adequate canonical independent coverage for the full K13–K30 band.

### Adequately represented or recoverable with minor rewrite
- K13 idafah
- K15 attached-pronoun recognition
- K17 adjective relation
- K18 possessive pronoun — after P02 rewrite
- K20 preposition + attached pronoun
- K21 verb + object pronoun — after P13 rewrite

### Missing / insufficient canonical targets requiring new replacement candidates
- **K14** overt direct object
- **K16** conjunction recognition
- **K19** nominal coordination
- **K22** demonstrative recognition
- **K23** relative-pronoun recognition
- **K24** demonstrative predication
- **K25** verb + PP attachment
- **K26** imperative recognition
- **K27** negative particle
- **K28** `هل` interrogative
- **K29** `يا` vocative
- **K30** future `سوف / سـ`

This is a major correction: historical pool size 36/36 cannot be treated as canonical coverage of K13–K30 until these missing operations receive valid items.

## 5. Salvage policy for out-of-band items

Out-of-band items are not deleted. They may be:
1. retained as auxiliary morphology diagnostics outside the core K ladder;
2. remapped to earlier checkpoint/prerequisite probes when an exact canonical K exists;
3. retired from live placement if they add no unique routing value.

They must not occupy a K13–K30 coverage slot merely to preserve historical counts.

## 6. Required corrective authoring

Create an L10 canonical repair batch with at least one clean candidate for each missing target K14, K16, K19, K22, K23, K24, K25, K26, K27, K28, K29, K30, plus rewrites for K18 and K21. Prefer 2 independent items per high-routing-value K before pilot freeze.

## 7. Gate decision

**L10 historical slot-state completeness remains 100%, but canonical competency coverage is NOT yet 100%.**

L10 may not be production-frozen until canonical repair authoring, duplicate audit, Arabic-content review, and routing validation are complete.
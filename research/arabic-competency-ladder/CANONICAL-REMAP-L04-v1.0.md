# Canonical Remap — L04 v1.0

**Status:** CANONICAL ALIGNMENT CONTROL — NON-PRODUCTION  
**Checkpoint:** L04  
**Authoritative band:** K01–K12  
**Canonical source:** `CANONICAL-REGISTRY-K01-K67-v0.1.md` from PR #4  
**Rule:** historical item/version identity is preserved; canonical target labels are corrected in the registry layer.

## 1. Canonical band

K01 REC-N-BASE; K02 REC-AL; K03 REC-NAK-TAN; K04 REC-PREP; K05 REC-PRON-SEP; K06 REC-V-PERF; K07 REC-V-IMPF; K08 REL-NOM-PRED; K09 REL-PP; K10 REL-VS; K11 REL-PRON-MUBTADA; K12 REL-KHABAR-PP.

Anything whose scored target is K13+ is **OUT-OF-BAND-HOLD** for L04 even when the Qur'anic span is otherwise suitable.

## 2. Remap status — replacement P01–P06

| Item | Old label | Canonical target | Decision | Note |
|---|---|---|---|---|
| P01 | K01/K02 | K02 primary, K01 prerequisite | CANONICAL-REMAP | asks overt `الـ` on noun; K02 is the scored operation |
| P02 | K03 | K03 | CANONICAL-MATCH | tanwin/indefiniteness |
| P03 | K04 | K04 | CANONICAL-MATCH | preposition recognition |
| P04 | K05 | K05 | CANONICAL-MATCH | detached pronoun |
| P05 | K06 | K06 | CANONICAL-MATCH | perfect verb |
| P06 | K07 | K07 | CANONICAL-MATCH | imperfect verb |

## 3. Remap status — replacement P07–P18

| Item | Old label | Canonical target | Decision | Note |
|---|---|---|---|---|
| P07 | K07 | K04 primary | CANONICAL-REMAP | prompt scores recognition of `على`; attached-pronoun analysis remains excluded |
| P08 | K08 | K08 | CANONICAL-MATCH | simple nominal predication |
| P09 | K09 | K09 | CANONICAL-MATCH | overt PP relation |
| P10 | K10 | K10 | CANONICAL-MATCH | verb + overt fa'il |
| P11 | K11 | K11 | CANONICAL-MATCH-WITH-NOTE | score detached pronoun as mubtada' only with alternate-analysis-safe rubric |
| P12 | K12 | K12 | CANONICAL-MATCH | mastered PP as khabar |
| P13 | K01/K02 | K02 + K03 contrast | CANONICAL-REMAP | `الصمد` tests overt `الـ`; `خسرٍ` tests tanwin/nakirah |
| P14 | K04/K09 | K04 prerequisite + K09 boundary | CANONICAL-MATCH | negative control: attached pronoun means not overt prep+noun K09 pattern |
| P15 | K06/K10 | K06 prerequisite + K10 primary | CANONICAL-MATCH | perfect verbs with overt fa'il transfer |
| P16 | K05/K11 | K05 prerequisite + K11 primary | CANONICAL-MATCH-WITH-NOTE | avoid full verse i'rab |
| P17 | K08/K12 | K12 primary + K08/K09 prerequisites | CANONICAL-MATCH | fronted PP khabar |
| P18 | sampled K01–K12 | sampled K05/K10/K12 | CANONICAL-REMAP | explicitly score only three canonical operations, not an undefined whole-band integration target |

## 4. Remap status — replacement P19–P30

| Item | Old label | Canonical target | Decision | Note |
|---|---|---|---|---|
| P19 | K01 | K02 | CANONICAL-REMAP | definiteness with overt `الـ` is K02, not base noun recognition K01 |
| P20 | K02 | K03 | CANONICAL-REMAP | nakirah/tanwin is K03 |
| P21 | K03 | K04 | CANONICAL-REMAP | preposition recognition is K04 |
| P22 | K04 | K05 | CANONICAL-REMAP | detached pronoun is K05 |
| P23 | K05 | K06 | CANONICAL-REMAP | perfect verb is K06 |
| P24 | K06 | K07 | CANONICAL-REMAP | imperfect verb is K07 |
| P25 | K07 | K26 | **OUT-OF-BAND-HOLD** | imperative recognition is canonically K26; cannot be scored at L04 |
| P26 | K08 | K08 | CANONICAL-MATCH-WITH-NOTE | prompt should score predication, not merely 'two nouns', otherwise it falls back toward K01 |
| P27 | K09 | K09 | CANONICAL-MATCH | PP recognition; extended idafah excluded |
| P28 | K10 | K10 | CANONICAL-MATCH | verb + overt fa'il |
| P29 | K11 | K11 | CANONICAL-MATCH-WITH-NOTE | full exclusive i'rab not required |
| P30 | K12 sampled | K05 + K08/K11 sampled; **not K12 as written** | REWRITE-FOR-CANONICAL | current prompt identifies amr (`قل`, K26), detached pronoun, and nominal elements; it does not actually test PP-as-khabar K12 |

## 5. Surviving historical P31–P36

The earlier quality screen remains valid as a quality layer, but each surviving item must be registry-aligned using the same authoritative definitions before production. In particular:
- any item scoring attached pronouns belongs K15+ and cannot be a primary L04 target;
- command recognition belongs K26;
- idafah belongs K13;
- adjective relation belongs K17;
- full object relation belongs K14;
- L04 may contain these only as **unscored surface material**, never as required operations.

## 6. Immediate remediation

1. Keep P25 historical/version record, set `canonical_status=OUT-OF-BAND-HOLD`, `production_enabled=false`.
2. Rewrite P30 as v2.1 to genuinely sample L04 canonical operations; remove command recognition from required scoring and include an actual K12 PP-as-khabar operation if K12 remains primary.
3. Registry-normalize all remapped labels without overwriting source research files.
4. Re-run duplicate-function audit after remap because several apparent duplicates change once their true K identity is corrected.
5. Arabic-content review remains mandatory for MEDIUM ambiguity records.

## 7. L04 alignment verdict

For P01–P30 replacement records:
- CANONICAL-MATCH / MATCH-WITH-NOTE: 17
- CANONICAL-REMAP: 11
- OUT-OF-BAND-HOLD: 1 (P25)
- REWRITE-FOR-CANONICAL: 1 (P30)

**Canonical alignment state for the 30 replacement slots: 30/30 classified = 100%.**

This is classification completeness, not production readiness.
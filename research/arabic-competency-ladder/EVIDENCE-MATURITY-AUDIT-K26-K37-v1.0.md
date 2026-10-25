# EVIDENCE MATURITY AUDIT — K26–K37 v1.0

**Status:** COMPLETED CONSERVATIVE AUDIT  
**Architecture:** canonical K01–K65 FROZEN  
**Sources:** final gates K26–K37  
**Rule:** maturity credit is based on evidence explicitly documented in authoritative artifacts; missing normalized surah:ayah metadata prevents promotion to full E2/E3.

## Audit table

| K | Competency | Evidence posture | Maturity | Decision |
|---|---|---|---|---|
| K26 | fi'il amr recognition | occurrence-validated recognition; clear exclusions for hidden subject, object suffix, weak-verb complexity | E1+ | strong recognition gate; expand referenced bank |
| K27 | basic negation-particle recognition | occurrence-specific function tagging; polyfunction control; governance explicitly locked | E1+ | strong ambiguity controls; normalize examples |
| K28 | `هل` interrogative recognition | validated occurrence; scope/question-clause analysis locked | E1 | anchor-level gate; expand bank |
| K29 | `يا` vocative recognition | validated occurrence; complex vocative structure held out | E1 | anchor-level gate; expand bank |
| K30 | `سوف/سـ` future recognition | segmentation rule + occurrence-specific future validation | E1+ | strong form/function gate; expand forms |
| K31 | interrogative hamzah | lexical-vs-interrogative disambiguation explicitly required | E1+ | strong false-positive control |
| K32 | `قد` recognition | validated occurrence with semantic interpretation locked | E1 | anchor-level recognition; expand diversity |
| K33 | `إنّ` recognition | validated token with governing effect explicitly locked in metadata | E1+ | strong bridge node; downstream K38 bank already richer |
| K34 | `إلا` recognition | invariant token; occurrence validation + scope/istitsna analysis locked | E1+ | strong recognition/relational separation |
| K35 | limited `ليس` family recognition | family membership validation + strict construction lock | E1+ | sufficient architecture evidence; expand forms |
| K36 | `لو` recognition | validated conditional/counterfactual marker; clause linkage locked | E1 | marker anchor; expand clean contexts |
| K37 | limited `كان` family recognition | occurrence-specific family whitelist, metadata requirements, reinforcement/premature policy | E1+ | strongest family-recognition posture in this wave |

## Findings

### Recognition nodes are not evidence-free
All K26–K37 final gates contain occurrence-level validation rules and explicit exclusion boundaries. This is enough to confirm at least anchor-level evidence posture for all 12 competencies.

### Strongest nodes in Wave D
K27, K30, K31, K33, K34, K35, and K37 have explicit ambiguity/segmentation/family controls that make them stronger than simple token recognition.

### Why none is promoted to E2 in this audit
The final-gate summaries do not themselves provide a normalized small bank with exact surah:ayah metadata and multiple credited examples per K. Under the v1.0 maturity framework, E2 requires several clean referenced occurrences, not merely a strong gate definition.

## Wave D verdict

- K26–K37 audited: **12/12**;
- minimum evidence posture: **E1 for all 12**;
- E1+ stronger gate posture: **8/12**;
- full E2 claimed: **0/12 pending normalized multi-example banks**;
- architecture changes required: **none**.

## Global audit coverage after this file

Formal evidence-maturity audit coverage now includes:
- K01–K10;
- K11–K20;
- K21–K25;
- K26–K37;
- K38–K57;
- K58–K65.

Therefore **all canonical K01–K65 now have an explicit audit status**.

## Next phase

1. consolidate all per-wave audit results into one `EVIDENCE-MATURITY-MATRIX-K01-K65-v1.0.md`;
2. compute audited evidence progress using a declared scoring method;
3. launch exact surah:ayah recovery/normalization, beginning with foundational K01–K25;
4. promote K units from E1/E1+ toward E2/E3 based on committed evidence records.

**WAVE D AUDIT COMPLETE.**
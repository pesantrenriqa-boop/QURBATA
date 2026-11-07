# PREREQUISITE GRAPH — Qur'anic Arabic Competency Ladder K01–K65 v1.0

**Status:** FROZEN SUPPORTING ARCHITECTURE  
**Parent:** `LADDER-ARCHITECTURE-v1.0.md`  
**Canonical core:** 65 distinct learner operations

## Dependency legend

- **P1** = hard prerequisite: learner cannot execute target operation without it.
- **P2** = normal prerequisite: expected in ordinary core examples, but not identity-defining in every occurrence.
- **P3** = transfer support: raises complexity/fluency, not required to define the competency.
- Numeric order remains pedagogical linearization, not a universal direct dependency chain.

## Canonical prerequisite matrix

| K | P1 hard prerequisite | P2 normal prerequisite / support |
|---|---|---|
| K01 | — | — |
| K02 | K01 | — |
| K03 | K01 | — |
| K04 | — | K01 for PP construction later |
| K05 | — | — |
| K06 | — | — |
| K07 | — | — |
| K08 | K01 | K02/K03 as encountered |
| K09 | K04 + K01 | K02/K03 |
| K10 | K06 or K07 + K01 | K02/K03 |
| K11 | K05 + K08 | — |
| K12 | K08 + K09 | — |
| K13 | K01 | K02/K03 + genitive exposure |
| K14 | K10 | K01 |
| K15 | prior token segmentation | K05 as pronoun concept support |
| K16 | — | — |
| K17 | K01 | K02/K03 |
| K18 | K13 + K15 | — |
| K19 | K16 + mastered nominal units | K01/K13/K17 as conjunct types |
| K20 | K04 + K15 | K09 |
| K21 | K10 + K15 | K14 |
| K22 | — | K01 category awareness |
| K23 | — | K01 category awareness |
| K24 | K22 + K08 | — |
| K25 | K09 + K10 | — |
| K26 | verbal-form awareness | K06/K07 |
| K27 | — | clause recognition |
| K28 | — | clause recognition |
| K29 | — | nominal recognition |
| K30 | K07 | — |
| K31 | — | clause recognition |
| K32 | verbal recognition | K06/K07 |
| K33 | — | K08 for later relational use |
| K34 | — | — |
| K35 | — | K08 for later relational use |
| K36 | — | clause recognition |
| K37 | — | K08 for later relational use |
| K38 | K33 + K08 | K12 where PP khabar occurs |
| K39 | K35 + K08 | K12 where PP khabar occurs |
| K40 | K37 + K08 | K12 where PP khabar occurs |
| K41 | K06/K07 + verbal predication awareness | K10 |
| K42 | K23 + clause recognition | K41 where hidden subject occurs |
| K43 | K42 + relevant pronoun relation | K15/K20/K21 as occurrence demands |
| K44 | K38 | — |
| K45 | K42 + K43 | transitivity/local slot awareness |
| K46 | K08 + short verbal clause competence | K41 + reference linkage |
| K47 | clause competence through K46 | K36 where `لو` is used |
| K48 | K47 | K16 marker segmentation support |
| K49 | K07 + local jussive environment | K47 |
| K50 | K49 + familiar weak-final base | — |
| K51 | jussive environment + familiar nūn-bearing base | K49 |
| K52 | K07 + overt nāṣib environment | prior mood distinction |
| K53 | K52 + validated trigger family | — |
| K54 | K47 + K48 + nominal-clause recognition | K08/K38 as response form requires |
| K55 | K07 + absence of active nāṣib/jāzim | K49/K52 contrast support |
| K56 | K55 + familiar nūn-bearing base | — |
| K57 | K55 + weak-final familiarity | — |
| K58 | complete clause analysis | K16/K19 coordination background |
| K59 | K58 | temporal interpretation |
| K60 | analyzable propositions | K58 |
| K61 | analyzable propositions | K58 |
| K62 | analyzable propositions | K61 contrast of semantic direction |
| K63 | K34 + local scope/proposition analysis | negation/coordination as encountered |
| K64 | analyzable action/proposition | K52/K53 only where already required by surface form |
| K65 | analyzable propositions | K60 contrast awareness |

## Major dependency pathways

### Nominal pathway
`K01 → K08 → K12`  
`K01 → K13 → K18`  
`K01 → K17`  
`K22 + K08 → K24`

### Verbal pathway
`K06/K07 → K10 → K14`  
`K10 + K15 → K21`  
`K09 + K10 → K25`  
`K06/K07 → K41`

### Pronoun/reference pathway
`K05 → K11`  
`K15 → K18/K20/K21`  
`K23 → K42 → K43 → K45`

### Operator/transformed-predication pathway
`K33 + K08 → K38 → K44`  
`K35 + K08 → K39`  
`K37 + K08 → K40`

### Conditional/mood pathway
`K47 → K48 → K54`  
`K07 + jussive environment → K49 → K50/K51`  
`K07 + nāṣib → K52 → K53`  
`K07 + no nāṣib/jāzim → K55 → K56/K57`

### Discourse pathway
`clause analysis → K58 → K59`  
`proposition analysis → K60/K61/K62/K65`  
`K34 + scope analysis → K63`  
`action/proposition analysis → K64`

## Transfer nodes retained from discovery history

- `TRANSFER-T42`: longer/denser relative-clause boundary transfer; depends on K42.
- `TRANSFER-T43`: longer/denser explicit resumptive resolution; depends on K43 and normally T42/K42.

These are not canonical core K numbers.

## Dependency integrity rules

1. A teaching item may contain earlier competencies cumulatively, but only one operation is newly targeted.
2. A P2/P3 feature may not become a hidden new P1 inside a supposedly clean core item.
3. New surface vocabulary does not equal a new grammatical prerequisite.
4. Tafsir knowledge may clarify meaning but must not be required to identify a core linguistic operation unless the item is explicitly tagged advanced/interpretive.
5. If an item requires a later K to solve the target K, the item is premature and must be moved upward or rejected.

## Verdict

**PREREQUISITE GRAPH: FROZEN v1.0**  
The graph supports the 65-core architecture and replaces the false assumption of a purely linear K01→K65 prerequisite chain.
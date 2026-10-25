# CANONICAL REGISTRY — Qur'anic Arabic Competency Ladder K01–K67 v0.1

**Status:** FULL CONSOLIDATION DRAFT  
**Architecture baseline:** K01–K67 DRAFT-FROZEN  
**Endpoint:** K67 provisional core endpoint  
**Source policy:** this registry consolidates the authoritative frozen definitions through normalized batch registries. It does not silently rename, merge, split, or expand competencies.

## Canonical compact registry

| K | Code / short name | Canonical learner operation | Primary domain | Direct prerequisite anchor |
|---|---|---|---|---|
| K01 | REC-N-BASE | Recognize a simple Qur'anic token as isim. | Recognition / nominal | — |
| K02 | REC-AL | Detect overt `الـ` on an already recognizable noun. | Nominal feature | K01 |
| K03 | REC-NAK-TAN | Recognize simple nominal indefiniteness/tanwin evidence. | Nominal feature | K01 |
| K04 | REC-PREP | Recognize frequent overt prepositions. | Function-word recognition | — |
| K05 | REC-PRON-SEP | Recognize basic detached pronouns. | Pronoun recognition | — |
| K06 | REC-V-PERF | Recognize a simple perfect verb. | Verb recognition | — |
| K07 | REC-V-IMPF | Recognize a simple imperfect verb. | Verb recognition | — |
| K08 | REL-NOM-PRED | Identify simple mubtada' + overt nominal khabar. | Clause / nominal predication | K01 |
| K09 | REL-PP | Build/identify overt preposition + noun as jar–majrur. | Phrase / PP | K01 + K04 |
| K10 | REL-VS | Identify simple verb + overt noun fa'il. | Clause / verbal predication | K01 + K06/K07 |
| K11 | REL-PRON-MUBTADA | Use recognized detached pronoun as mubtada' in simple nominal predication. | Clause | K05 + K08 |
| K12 | REL-KHABAR-PP | Identify a mastered PP as khabar. | Clause / nominal predication | K08 + K09 |
| K13 | REL-IDHAFAH-2N | Identify two overt nouns in simple idhafah. | Phrase / nominal dependency | K01 + genitive exposure |
| K14 | REL-MAFUL-ZHAHIR | Identify overt noun as direct object of readable verb. | Clause / argument structure | K10 |
| K15 | REC-PRON-ATT | Segment an attached pronoun from its host. | Morphology / recognition | prior recognition |
| K16 | REC-CONJ | Recognize validated frequent coordinating particles. | Linkage-marker recognition | — |
| K17 | REL-ADJ | Identify simple na'at–man'ut relation. | Phrase / modification | nominal recognition |
| K18 | REL-POSS-PRON | Assign attached pronoun on noun host as possessive/genitive. | Phrase / dependency | K13 + K15 |
| K19 | REL-CONJ-NOM | Coordinate two mastered nominal units with validated conjunction. | Phrase / coordination | K16 |
| K20 | REL-PREP-PRON | Identify attached pronoun as complement of preposition. | Phrase / PP dependency | K09 + K15 |
| K21 | REL-V-OBJ-PRON | Identify attached pronoun as direct object of verb. | Clause / argument structure | K14 + K15 |
| K22 | REC-DEM | Recognize isim isyarah. | Nominal-category recognition | — |
| K23 | REC-REL | Recognize isim maushul. | Nominal-category recognition | — |
| K24 | REL-DEM-PRED | Use demonstrative as mubtada' with simple nominal predicate. | Clause / nominal predication | K22 + K08 |
| K25 | REL-V-PP | Attach mastered PP to a simple verb occurrence. | Clause / verbal attachment | K09 + K10 |
| K26 | REC-V-IMP | Recognize simple imperative verb occurrence. | Verb-form recognition | K06/K07 basis |
| K27 | REC-NEG | Recognize occurrence-specific basic negative-particle function. | Particle/function recognition | — |
| K28 | REC-INT-HAL | Recognize `هل` as interrogative marker. | Particle/function recognition | — |
| K29 | REC-VOC-YA | Recognize `يا` as vocative marker. | Particle/function recognition | — |
| K30 | REC-FUT | Recognize/segment `سوف / سـ` on mudhari'. | Particle/morphology | K07 |
| K31 | REC-INT-HAMZA | Recognize interrogative hamzah and distinguish it from lexical hamzah. | Particle/function recognition | — |
| K32 | REC-QAD | Recognize validated `قد` occurrence without full aspect semantics. | Particle recognition | — |
| K33 | REC-INNA | Recognize `إنّ` while government remains locked. | Operator recognition | — |
| K34 | REC-ILLA | Recognize validated `إلا` without opening full exception analysis. | Particle recognition | — |
| K35 | REC-LAYSA | Recognize limited `ليس` family. | Verbal/copular recognition | — |
| K36 | REC-LAW | Recognize validated `لو` conditional/counterfactual marker. | Conditional-marker recognition | — |
| K37 | REC-KANA-FAMILY | Recognize limited `كان` family. | Verbal/copular recognition | — |
| K38 | REL-INNA-CORE | Analyze simple `إنّ + اسمها + خبرها`. | Clause / transformed nominal predication | K33 + K08 |
| K39 | REL-LAYSA-PRED | Analyze simple `ليس + اسمها + خبرها`. | Clause / negative nominal transformation | K35 + K08 |
| K40 | REL-KANA-CORE | Analyze simple `كان + اسمها + خبرها`. | Clause / transformed nominal predication | K37 + K08 |
| K41 | REL-V-SUBJ-HIDDEN | Recover basic hidden fa'il in simple active verb. | Clause / subject dependency | prior verbal morphology |
| K42 | REL-MAWSUL-SILAH | Identify isim maushul and delimit minimal silah. | Relative-clause boundary | K23 + prior clause relations |
| K43 | REL-RELATIVE-EXPLICIT-AID | Identify overt `عائد` inside silah and link it to maushul. | Reference / dependency | K42 + relevant pronoun relation |
| K44 | EMPHATIC-LAM-INNA | Identify validated emphatic lām inside mastered simple `إنّ` frame. | Clause semantics / emphasis | K38 |
| K45 | BASIC-OMITTED-AID | Recover one locally omitted resumptive slot in simple relative construction. | Dependency / controlled ellipsis | K42 + K43 |
| K46 | CLAUSAL-KHABAR-VERBAL | Identify short verbal clause as khabar of explicit mubtada' with mastered local link. | Clause embedding | K08 + prior reference/subject skills |
| K47 | REL-SHART-CORE | Delimit marker, condition clause, response clause, and condition→result dependency. | Interclausal dependency | internal grammar ≤ K46 |
| K48 | REL-FA-JAWAB-EXPLICIT | Classify overt `فـ` as فاء جواب الشرط and mark response onset. | Conditional response marker | K47 |
| K49 | MORPH-JAZM-SUKUN | Connect transparent final sukūn on mudhari' to local jazm. | Mood morphology | K47 + K07 |
| K50 | MORPH-JAZM-DELETE-WEAK | Reconstruct one deleted final weak segment as jazm effect. | Reconstructive mood morphology | K49 + familiar weak-final base |
| K51 | MORPH-JAZM-DELETE-NUN | Detect deletion of expected inflectional nūn as jazm effect. | Reconstructive mood morphology | jussive environment + familiar base |
| K52 | MORPH-NASB-FATHA | Connect overt nāṣib + transparent final fatḥah to nasb. | Mood morphology | K07 + prior mood control |
| K53 | SYN-ELLIPSIS-HIDDEN-AN | Reconstruct one validated hidden `أن` and connect it to nasb. | Syntax / controlled ellipsis | K52 + trigger family |
| K54 | REL-FA-JAWAB-PREDICT | Predict fā' for nominal conditional response, then verify it. | Conditional generative reasoning | K47 + K48 + nominal-clause recognition |
| K55 | MORPH-RAF-DAMMA | Identify visible ḍammah as raf' where no active nāṣib/jāzim applies. | Mood morphology | K07 + mood-environment control |
| K56 | MORPH-RAF-THUBUT-NUN | Identify retained inflectional nūn as raf' sign. | Mood morphology | K55 + familiar nūn-bearing base |
| K57 | MORPH-RAF-ESTIMATED-DAMMA | Identify estimated ḍammah as raf' on familiar weak-final mudhari'. | Abstract i'rab representation | K55 + weak-final familiarity |
| K58 | REL-CLAUSE-COORD | Identify two complete clauses and validated overt coordinator as clause-level coordination. | Clause / discourse | prior clause analysis through K57 |
| K59 | REL-TEMP-SEQUENCE | Identify validated `ثم` relation as temporal sequence between clauses. | Discourse / temporal relation | K58 |
| K60 | REL-RELATIVE-BOUNDARY-LATE | Delimit explicit relative clause in controlled late-ladder transfer. | Clause / dependency transfer | analyzable clauses |
| K61 | REL-RELATIVE-AID-LATE | Resolve one overt resumptive to relative antecedent in controlled transfer. | Reference / dependency transfer | K60 |
| K62 | REL-CONTRAST-CORRECTION | Identify validated contrast/correction and what B limits/corrects in A. | Discourse semantics | analyzable propositions |
| K63 | REL-RESULT-CONSEQUENCE | Identify directional `A → RESULT B`. | Discourse semantics | K58 + proposition analysis |
| K64 | REL-CAUSE-REASON | Identify directional `A ← REASON B`. | Discourse semantics | proposition analysis through K63 |
| K65 | REL-EXCEPTION-RESTRICTION | Identify domain and element excepted/restricted by explicit `إلا`. | Scope / discourse semantics | local/proposition analysis |
| K66 | REL-PURPOSE-GOAL | Identify action/proposition and explicitly expressed intended goal. | Discourse semantics | prior proposition + mood analysis as needed |
| K67 | REL-CONCESSION | Identify expectation-trigger A and B that nevertheless remains valid. | Discourse semantics | prior discourse analysis |

## Architecture layers

### Layer 1 — recognition foundations
K01–K07 plus later low-dependency recognition nodes K15–K16, K22–K23, K26–K37.

### Layer 2 — local phrase and clause relations
K08–K14, K17–K21, K24–K25, K38–K41.

### Layer 3 — dependency, reference, embedding, ellipsis
K42–K46, with controlled transfer/revisit at K60–K61.

### Layer 4 — conditional architecture and mood morphology
K47–K57.

### Layer 5 — interclausal/discourse-semantic relations
K58–K59 and K62–K67.

## Important overlap flag for final audit

K42/K43 and K60/K61 occupy closely related relative-clause/resumptive territory. This registry **does not silently merge them**, because all four are already frozen source records. They are therefore explicitly flagged for the final overlap audit to determine whether K60/K61 represent:

1. genuine higher-level transfer/re-entry operations;
2. redundant duplicate identities requiring architecture correction before v1.0; or
3. the same operation at different complexity bands that should be represented through mastery levels rather than separate core K numbers.

Until that audit is complete, K60/K61 retain their frozen IDs but are labeled **LATE TRANSFER / OVERLAP REVIEW** in the canonical architecture.

## Dependency principles

1. Numeric order is pedagogical linearization, not a claim that K(n−1) is always a hard prerequisite.
2. Recognition and relational use remain distinct operations where source gates explicitly separated them.
3. A core item may contain cumulative earlier complexity, but exactly one new target operation.
4. Particle identity alone does not define a competence; occurrence-specific function validation remains mandatory.
5. Traditional subtypes do not automatically receive new K numbers.
6. DRAFT-FROZEN locks identity provisionally; it does not mean evidence-bank maturity is production-ready.

## Endpoint status

K67 remains the **provisional core endpoint**. K68+ remains closed unless new corpus evidence demonstrates a genuinely distinct learner operation with clean evidence, manageable prerequisites, and non-redundancy.

## Next required gate before v1.0

Run `FINAL-DEPENDENCY-OVERLAP-AUDIT-K01-K67` with special attention to:
- K42 ↔ K60;
- K43 ↔ K61;
- K16/K19 ↔ K58;
- K47 conditional result ↔ K63 consequence;
- K34 recognition `إلا` ↔ K65 exception/restriction;
- K44 emphasis ↔ discourse-semantic layer;
- K45 omitted `عائد` and whether later frontier notes incorrectly re-defer an already-frozen operation;
- K49–K57 mood morphology as a coherent but non-overfragmented subsystem.

Only after that audit should `LADDER-ARCHITECTURE-v1.0` be issued.
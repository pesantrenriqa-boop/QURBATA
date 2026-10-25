# LADDER ARCHITECTURE — Qur'anic Arabic Competency Ladder v1.0

**Status:** ARCHITECTURE FROZEN — RESEARCH LAYER  
**Core operations:** 65 distinct competencies  
**Legacy discovery span:** K01–K67  
**Resolved duplicate discovery nodes:** legacy K60/K61 → transfer nodes, not new core competencies  
**Endpoint:** canonical K65

## 1. Governing principle

The ladder is organized by **distinct learner operations**, not by chapter count, traditional grammar inventory, or a predetermined target number.

A new competence exists only when it introduces a genuinely new operation that:
- is non-redundant with earlier competencies;
- has manageable prerequisites;
- can be evidenced through cumulative-clean Qur'anic occurrences;
- can be assessed independently;
- does not require silently importing several new rules at once.

## 2. Canonical architecture

### Layer A — Recognition foundations
Core recognition of nouns, verbs, pronouns, particles, and limited operator/family forms.

Canonical range: **K01–K07**, with additional recognition nodes interleaved later where dependency cost is low.

### Layer B — Local phrase and clause relations
Learners combine previously recognized forms into simple nominal/verbal relations, PP, idhafah, adjective, object, pronoun-function, demonstrative-predication, and verbal attachment structures.

### Layer C — Operators, transformed predication, reference, and embedding
Learners analyze simple `إنّ/ليس/كان` frames, hidden subjects, relative-clause boundaries, explicit/omitted resumptives, emphasis, and short clausal predicates.

### Layer D — Conditional architecture and mood morphology
Learners identify شرط→جواب linkage, explicit فاء الجواب, then connect governing environments with visible, deleted, retained, hidden, and estimated mood realizations.

### Layer E — Interclausal and discourse-semantic relations
Learners move from clause coordination and temporal sequencing to contrast/correction, result, reason, exception/restriction, purpose, and concession/counterexpectation.

## 3. Canonical K01–K65 sequence

K01 REC-N-BASE — simple isim recognition  
K02 REC-AL — definite article recognition  
K03 REC-NAK-TAN — simple nakirah/tanwin recognition  
K04 REC-PREP — frequent preposition recognition  
K05 REC-PRON-SEP — detached pronoun recognition  
K06 REC-V-PERF — simple fi'il madhi recognition  
K07 REC-V-IMPF — simple fi'il mudhari' recognition  
K08 REL-NOM-PRED — simple mubtada' + nominal khabar  
K09 REL-PP — preposition + overt noun  
K10 REL-VS — verb + overt fa'il  
K11 REL-PRON-MUBTADA — detached pronoun as mubtada'  
K12 REL-KHABAR-PP — PP as khabar  
K13 REL-IDHAFAH-2N — simple two-noun idhafah  
K14 REL-MAFUL-ZHAHIR — overt direct object  
K15 REC-PRON-ATT — attached pronoun segmentation  
K16 REC-CONJ — validated conjunction recognition  
K17 REL-ADJ — simple na'at–man'ut  
K18 REL-POSS-PRON — attached pronoun as mudhaf ilaih  
K19 REL-CONJ-NOM — nominal coordination  
K20 REL-PREP-PRON — preposition + attached pronoun  
K21 REL-V-OBJ-PRON — attached pronoun as object  
K22 REC-DEM — demonstrative recognition  
K23 REC-REL — relative-pronoun recognition  
K24 REL-DEM-PRED — demonstrative as mubtada'  
K25 REL-V-PP — PP attached to simple verb  
K26 REC-V-IMP — imperative recognition  
K27 REC-NEG — basic negative-particle function  
K28 REC-INT-HAL — `هل` interrogative recognition  
K29 REC-VOC-YA — `يا` vocative recognition  
K30 REC-FUT — `سوف/سـ` future marker  
K31 REC-INT-HAMZA — interrogative hamzah  
K32 REC-QAD — `قد` recognition  
K33 REC-INNA — `إنّ` recognition with government locked  
K34 REC-ILLA — `إلا` recognition  
K35 REC-LAYSA — limited `ليس` family recognition  
K36 REC-LAW — `لو` conditional/counterfactual marker recognition  
K37 REC-KANA-FAMILY — limited `كان` family recognition  
K38 REL-INNA-CORE — simple `إنّ + اسمها + خبرها`  
K39 REL-LAYSA-PRED — simple `ليس + اسمها + خبرها`  
K40 REL-KANA-CORE — simple `كان + اسمها + خبرها`  
K41 REL-V-SUBJ-HIDDEN — basic hidden fa'il  
K42 REL-MAWSUL-SILAH — relative-clause boundary  
K43 REL-RELATIVE-EXPLICIT-AID — overt resumptive reference  
K44 EMPHATIC-LAM-INNA — emphatic lām in simple `إنّ` frame  
K45 BASIC-OMITTED-AID — one locally omitted resumptive  
K46 CLAUSAL-KHABAR-VERBAL — short verbal clause as khabar  
K47 REL-SHART-CORE — simple condition→response linkage  
K48 REL-FA-JAWAB-EXPLICIT — explicit فاء جواب الشرط  
K49 MORPH-JAZM-SUKUN — jazm by visible sukūn  
K50 MORPH-JAZM-DELETE-WEAK — jazm by deletion of final weak segment  
K51 MORPH-JAZM-DELETE-NUN — jazm by deletion of inflectional nūn  
K52 MORPH-NASB-FATHA — nasb by visible fatḥah  
K53 SYN-ELLIPSIS-HIDDEN-AN — one validated hidden `أن` as nāṣib  
K54 REL-FA-JAWAB-PREDICT — predict fā' for nominal conditional response  
K55 MORPH-RAF-DAMMA — raf' by visible ḍammah  
K56 MORPH-RAF-THUBUT-NUN — raf' by retained inflectional nūn  
K57 MORPH-RAF-ESTIMATED-DAMMA — raf' by estimated ḍammah  
K58 REL-CLAUSE-COORD — simple interclausal coordination  
K59 REL-TEMP-SEQUENCE — temporal sequencing with validated `ثم`  
K60 REL-CONTRAST-CORRECTION — contrast/correction  
K61 REL-RESULT-CONSEQUENCE — result/consequence  
K62 REL-CAUSE-REASON — cause/reason  
K63 REL-EXCEPTION-RESTRICTION — exception/restriction with explicit `إلا`  
K64 REL-PURPOSE-GOAL — explicit purpose/goal relation  
K65 REL-CONCESSION — concession/counterexpectation

## 4. Legacy discovery ID resolution

The discovery process originally reached K67 before final overlap audit.

Two late discovery nodes were found not to introduce new learner operations:

- **legacy K60** = advanced/late revisit of K42 relative-clause boundary;
- **legacy K61** = advanced/late revisit of K43 explicit resumptive reference.

They are therefore preserved historically as:

- `TRANSFER-T42` — advanced relative-clause boundary transfer;
- `TRANSFER-T43` — advanced explicit-resumptive transfer.

All later legacy IDs shift by -2 in the canonical architecture:

- legacy K62 → canonical K60 contrast/correction;
- legacy K63 → canonical K61 result/consequence;
- legacy K64 → canonical K62 cause/reason;
- legacy K65 → canonical K63 exception/restriction;
- legacy K66 → canonical K64 purpose/goal;
- legacy K67 → canonical K65 concession/counterexpectation.

Historical files retain their original discovery IDs for traceability. New downstream mapping must use **canonical IDs**.

## 5. Dependency policy

Numeric order is a pedagogical linearization, not a universal direct-prerequisite chain.

Dependency metadata should distinguish:
- **P1 hard prerequisite** — required to execute the target operation;
- **P2 normal prerequisite** — normally needed for typical examples;
- **P3 transfer support** — increases complexity but is not identity-defining;
- **forbidden dependency** — would make the item premature for the target K.

Core evidence rule:

> An item may contain cumulative earlier complexity, but it should introduce only one new target operation.

## 6. Recognition vs relational use

Recognition of a form and structural/semantic use of that form are separate only when the learner operation is demonstrably different.

Examples:
- K33 `إنّ` recognition → K38 full simple `إنّ` construction;
- K34 `إلا` recognition → K63 exception/restriction interpretation;
- K35 `ليس` recognition → K39 full simple `ليس` construction;
- K37 `كان` family recognition → K40 full simple `كان` construction;
- K16 conjunction recognition → K19 nominal coordination → K58 clause coordination.

This separation is deliberate, not duplication.

## 7. Mood subsystem integrity

K49–K57 are retained as separate competencies because each requires a distinct observable/inferential operation:

- visible sukūn;
- deleted weak segment;
- deleted inflectional nūn;
- visible fatḥah under overt nāṣib;
- reconstruction of hidden `أن`;
- predictive fā' reasoning for nominal jawab;
- visible ḍammah;
- retained inflectional nūn;
- estimated ḍammah.

The ladder does not claim that this equals the complete traditional mood system. Full paradigms and subtype inventories belong to mastery/advanced layers.

## 8. Core / mastery / transfer / advanced layers

### CORE
The 65 canonical competencies in this document.

### MASTERY
Broader inventories, subtype distinctions, paradigms, denser example families, and production fluency built on an existing core operation.

Examples:
- full `باب الاستثناء` subtype system;
- full `الأفعال الخمسة` paradigms;
- full nawasikh families;
- full conjunction inventories;
- detailed conditions for فاء جواب الشرط.

### TRANSFER
Existing core operations applied to longer, denser, nested, or discourse-richer Qur'anic material.

Includes `TRANSFER-T42` and `TRANSFER-T43`.

### ADVANCED
Operations requiring heavier reconstruction, disputed parsing, advanced balaghah, broad discourse inference, or specialist morphology beyond the core ladder.

## 9. Endpoint rule

Canonical K65 is the frozen core endpoint for v1.0.

K66+ must not be created merely to continue numbering. Reopening the frontier requires:
1. a genuinely distinct learner operation;
2. enough clean Qur'anic evidence;
3. manageable prerequisites;
4. independent assessability;
5. non-redundancy with CORE/MASTERY/TRANSFER.

## 10. Evidence maturity remains separate

Architecture freeze does not imply that all evidence banks are equally mature.

Each K should later carry an evidence maturity status such as:
- E0 — definition only;
- E1 — anchor evidence;
- E2 — small clean bank;
- E3 — diversified validated bank;
- E4 — teaching-ready bank;
- E5 — assessment-ready bank.

Corpus expansion should normally improve maturity **inside** K01–K65 rather than generate new Ks.

## 11. Downstream integration contract

This file remains research-layer architecture until formal mapping is approved.

Canonical flow:

`LADDER-ARCHITECTURE-v1.0`
→ prerequisite graph
→ evidence maturity matrix
→ formal curriculum mapping
→ `REG-ARB-001`
→ `AR-STG-*`
→ QURBATA master content / assessments
→ RIQA OS and related systems.

No downstream artifact should use legacy K62–K67 numbering after canonical mapping is activated without an explicit legacy-ID field.

## 12. Freeze verdict

**ARCHITECTURE: FROZEN v1.0**  
**CORE COUNT: 65 DISTINCT LEARNER OPERATIONS**  
**LEGACY DISCOVERY RECORD: 67 IDs PRESERVED**  
**DUPLICATE DISCOVERY NODES: RESOLVED AS TRANSFER**  
**FRONTIER: CLOSED**  
**NEXT PHASE: EVIDENCE MATURITY + PREREQUISITE GRAPH + CURRICULUM MAPPING.**
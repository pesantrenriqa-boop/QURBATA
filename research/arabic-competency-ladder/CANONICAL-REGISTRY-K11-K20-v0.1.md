# CANONICAL REGISTRY — K11–K20 v0.1

**Status:** CONSOLIDATION DRAFT — definitions preserved from frozen final gates  
**Sources:** `FINAL-GATE-K11-K14-v1.0.md`, `FINAL-GATE-K15-K17-v1.0.md`, `FINAL-GATE-K18-K20-v1.0.md`  
**Rule:** normalization only; no silent rename, merge, split, or scope expansion.

## K11 — REL-PRON-MUBTADA
- **Canonical competence:** dhamir munfashil sebagai mubtada' dalam jumlah ismiyyah sederhana.
- **Primary domain:** clause / nominal predication.
- **Learner operation:** identify an already-recognized detached pronoun as mubtada' and identify its simple predicative relation.
- **Hard prerequisites:** K5 + K8.
- **Exclusions:** khabar jar–majrur; khabar jumlah; complex pronoun reference.
- **Architecture status:** DRAFT-FROZEN.

## K12 — REL-KHABAR-PP
- **Canonical competence:** khabar jar–majrur sederhana.
- **Primary domain:** clause / nominal predication + PP.
- **Learner operation:** identify a previously mastered jar–majrur unit as the predicate of a simple nominal sentence.
- **Hard prerequisites:** K8 + K9.
- **Exclusions:** preposition + attached pronoun as a new construction; clausal predicate.
- **Architecture status:** DRAFT-FROZEN.

## K13 — REL-IDHAFAH-2N
- **Canonical competence:** idhafah dua isim zhahir sederhana.
- **Primary domain:** phrase / nominal dependency.
- **Learner operation:** identify a two-overt-noun possessive/genitive idhafah relation.
- **Hard prerequisites:** K1 + genitive exposure through K9.
- **Exclusions:** three-member idhafah chain; attached-pronoun mudhaf ilaih; adjective attached to an idhafah member.
- **Architecture status:** DRAFT-FROZEN.

## K14 — REL-MAFUL-ZHAHIR
- **Canonical competence:** maf'ul bih isim zhahir sederhana.
- **Primary domain:** clause / verbal argument structure.
- **Learner operation:** identify an overt noun as the direct object of an already-readable verbal predication.
- **Hard prerequisites:** K10 + nominal recognition.
- **Exclusions:** object pronoun; two objects; object clause; higher embedded object structure.
- **Architecture status:** DRAFT-FROZEN WITH STRICT EVIDENCE FILTER.

## K15 — REC-PRON-ATT
- **Canonical competence:** mengenali dhamir muttashil sebagai segmen morfologis pada host.
- **Primary domain:** morphology / recognition.
- **Learner operation:** segment an attached pronoun from its host without yet assigning all syntactic functions.
- **Hard prerequisites:** prior form-recognition capacity; no later functional relation is required.
- **Evidence metadata:** retain `host_type` and `pronoun_form`.
- **Exclusions:** possessive, object, and prepositional functions are not collapsed into this recognition competence.
- **Architecture status:** DRAFT-FROZEN.

## K16 — REC-CONJ
- **Canonical competence:** mengenali huruf 'athaf frekuen pada fungsi koordinatif yang tervalidasi.
- **Primary domain:** morphology/function recognition / linkage marker.
- **Learner operation:** recognize a frequent conjunction only when its occurrence is validated as coordinative.
- **Core forms:** `و`, `ف`, `ثم` on validated coordinative occurrences.
- **Exclusions:** identical surface tokens with non-coordinative functions; construction of two conjuncts is deferred.
- **Architecture status:** DRAFT-FROZEN.

## K17 — REL-ADJ
- **Canonical competence:** na'at–man'ut sederhana.
- **Primary domain:** phrase / nominal modification.
- **Learner operation:** identify a clear two-token adjective–modified-noun relation and observe relevant agreement visible in the evidence.
- **Agreement dimensions in evidence:** gender, number, definiteness, case as applicable.
- **Exclusions:** nested idhafah; coordination; multiple adjective chains; higher structures.
- **Architecture status:** DRAFT-FROZEN.

## K18 — REL-POSS-PRON
- **Canonical competence:** dhamir muttashil sebagai mudhaf ilaih.
- **Primary domain:** phrase / possessive-genitive dependency.
- **Learner operation:** assign an already-recognized attached pronoun on a noun host to the possessive/genitive role.
- **Hard prerequisites:** K13 + K15.
- **Exclusions:** object suffix; prepositional pronoun.
- **Architecture status:** DRAFT-FROZEN.

## K19 — REL-CONJ-NOM
- **Canonical competence:** 'athaf dua unsur nominal sederhana.
- **Primary domain:** phrase / coordination.
- **Learner operation:** identify two already-mastered nominal units as conjuncts linked by a validated coordinating particle.
- **Hard prerequisites:** K16 + mastery of both conjunct units.
- **Exclusions:** clause coordination; ellipsis; non-'athaf functions of `و`, `ف`, `ثم`.
- **Architecture status:** DRAFT-FROZEN.

## K20 — REL-PREP-PRON
- **Canonical competence:** huruf jar + dhamir muttashil.
- **Primary domain:** phrase / prepositional dependency.
- **Learner operation:** identify an attached pronoun as the complement of a preposition.
- **Hard prerequisites:** K9 + K15.
- **Typical clean forms:** `له`, `به`, `فيه`, `عليه`, `منه`, `إليه` when cumulative prerequisites are satisfied.
- **Exclusions:** unresolved additional prefixes/particles; functions other than prepositional pronoun.
- **Architecture status:** DRAFT-FROZEN.

## Dependency scaffold K11–K20

```text
K5 + K8  ───────────────→ K11
K8 + K9  ───────────────→ K12
K1 + genitive exposure ─→ K13
K10 + K1 ───────────────→ K14
prior recognition ──────→ K15
validated marker recog. ─→ K16
nominal recognition ────→ K17
K13 + K15 ──────────────→ K18
K16 + mastered conjuncts → K19
K9 + K15 ───────────────→ K20
```

The numeric sequence remains pedagogical linearization; it must not be mistaken for a claim that every preceding K is a direct hard prerequisite.

## Consolidation verdict

K11–K20 are now normalized into canonical registry records without changing the frozen research definitions. Next extraction batch: K21–K33.
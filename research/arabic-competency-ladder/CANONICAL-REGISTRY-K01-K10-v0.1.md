# CANONICAL REGISTRY — K01–K10 v0.1

**Status:** CONSOLIDATION DRAFT  
**Source of truth for extraction:** `DRAFT-FROZEN-K01-K10-v1.0.md`  
**Rule:** definitions are normalized in format only; competency meaning is not expanded, merged, split, or renamed beyond preserving existing IDs/codes.

## K01 — REC-N-BASE
- **Canonical competency:** mengenali isim sederhana.
- **Primary domain:** form recognition — nominal.
- **Learner operation:** classify a simple Qur'anic token as an `isim` without yet assigning sentence function or i‘rāb role.
- **Hard prerequisite:** none.
- **Core exclusions:** mubtada’, khabar, fā‘il, maf‘ūl, muḍāf, na‘t, i‘rāb theory.
- **Architecture status:** DRAFT-FROZEN.

## K02 — REC-AL
- **Canonical competency:** mengenali `الـ` pada isim.
- **Primary domain:** nominal feature recognition.
- **Learner operation:** detect overt `الـ` as a nominal feature on an already recognizable noun.
- **Hard prerequisite:** K01.
- **Core exclusions:** full ma‘rifah theory; pronouns, demonstratives, relative nouns, iḍāfah as competing definiteness systems.
- **Architecture status:** DRAFT-FROZEN.

## K03 — REC-NAK-TAN
- **Canonical competency:** mengenali nakirah/tanwin nominal sederhana.
- **Primary domain:** nominal feature recognition.
- **Learner operation:** recognize simple nominal indefiniteness/tanwīn evidence without expanding into full i‘rāb theory.
- **Hard prerequisite:** K01.
- **Dependency note:** K02 and K03 are parallel nominal features that are linearized pedagogically.
- **Architecture status:** DRAFT-FROZEN.

## K04 — REC-PREP
- **Canonical competency:** mengenali huruf jar frekuen.
- **Primary domain:** function-word recognition.
- **Learner operation:** identify frequent overt prepositions such as `مِنْ`, `فِي`, `عَلَى`, `إِلَى`, `بِـ`, `لِـ`.
- **Hard prerequisite:** none.
- **Core exclusion:** full jar–majrūr relation analysis; that relational operation waits until K09.
- **Architecture status:** DRAFT-FROZEN.

## K05 — REC-PRON-SEP
- **Canonical competency:** mengenali ḍamīr munfaṣil dasar.
- **Primary domain:** pronoun form recognition.
- **Learner operation:** identify familiar detached pronoun forms such as `هُوَ`, `هِيَ`, `أَنْتَ`, `أَنْتُمْ` without yet resolving complex reference or assigning target syntactic function.
- **Hard prerequisite:** none.
- **Core exclusions:** use as target mubtada’; complex antecedent/reference analysis.
- **Architecture status:** DRAFT-FROZEN.

## K06 — REC-V-PERF
- **Canonical competency:** mengenali fi‘il māḍī sederhana.
- **Primary domain:** verbal form recognition.
- **Learner operation:** identify a simple perfect verb form.
- **Hard prerequisite:** none.
- **Core exclusions:** fā‘il function, full taṣrīf, passive, complex suffixes, derivational-form theory.
- **Architecture status:** DRAFT-FROZEN.

## K07 — REC-V-IMPF
- **Canonical competency:** mengenali fi‘il muḍāri‘ sederhana.
- **Primary domain:** verbal form recognition.
- **Learner operation:** identify a simple imperfect verb form.
- **Hard prerequisite:** none.
- **Core exclusions:** raf‘/naṣb/jazm, af‘āl khamsah, governing-particle theory.
- **Architecture status:** DRAFT-FROZEN.

## K08 — REL-NOM-PRED
- **Canonical competency:** jumlah ismiyyah core — mubtada’ + khabar isim ẓāhir sederhana.
- **Primary domain:** clause structure — nominal predication.
- **Learner operation:** identify a simple overt noun as mubtada’ and another overt noun as khabar in a basic verb-free nominal clause.
- **Hard prerequisite:** K01 plus only nominal features required by the occurrence.
- **Anchor:** `اللَّهُ الصَّمَدُ` — QS 112:2.
- **Core exclusions:** pronoun target; PP khabar; iḍāfah; na‘t; `إنّ`; `كان`; embedded/nested clause.
- **Architecture status:** DRAFT-FROZEN.

## K09 — REL-PP
- **Canonical competency:** huruf jar + isim ẓāhir sebagai jar–majrūr.
- **Primary domain:** local phrase relation — prepositional phrase.
- **Learner operation:** combine an already recognized preposition with an overt noun and identify the local jar–majrūr unit.
- **Hard prerequisite:** K01 + K04.
- **Typical clean forms:** `فِي الْأَرْضِ`, `فِي السَّمَاوَاتِ`, `عَنِ النَّبَإِ`, `بِالْحَقِّ`, `مِنَ الْأَرْضِ`.
- **Core exclusions:** preposition + attached pronoun; additional unmastered clitics.
- **Architecture status:** DRAFT-FROZEN.

## K10 — REL-VS
- **Canonical competency:** fi‘il + fā‘il isim ẓāhir sederhana.
- **Primary domain:** clause structure — verbal predication.
- **Learner operation:** identify a simple verb and its overt noun subject/fā‘il.
- **Hard prerequisite:** K01 + K06/K07 as required by the verb form.
- **Typical clean forms:** `جَاءَ الْحَقُّ`, `زَهَقَ الْبَاطِلُ`, `قَالَ مُوسَىٰ`, `يُرِيدُ اللَّهُ`.
- **Core exclusions:** hidden/suffix subject; maf‘ūl bih; quotation dependency; coordination; passive; subordination.
- **Architecture status:** DRAFT-FROZEN.

# Dependency skeleton K01–K10

- K01 → K02
- K01 → K03
- K04 → K09
- K01 → K09
- K06/K07 → K10
- K01 → K10
- K01 (+ occurrence-specific nominal features) → K08

K04, K05, K06, and K07 are foundational recognitions that are not all chained linearly to one another.

# Consolidation note

The extraction confirms the early ladder contains two different classes:

1. **REC** competencies K01–K07: recognizing forms/features without yet assigning the full relational function;
2. **REL** competencies K08–K10: combining previously recognized forms into local clause/phrase relations.

This distinction must be preserved in the full K01–K67 registry and dependency graph.
# EVIDENCE ANCHOR RECOVERY — K01–K10 v1.0

**Status:** CANONICAL ANCHORS RECOVERED  
**Architecture:** K01–K65 FROZEN  
**Purpose:** promote K01–K10 to explicit anchor-backed evidence with exact surah:ayah and minimal target spans.

## Recovery rule

- Target span is kept minimal so later competencies are not silently imported.
- A whole verse may contain higher structures; the K target is only the explicitly delimited span.
- Recognition Ks may use one token from a larger verse when token identity is the target operation.
- Relational Ks use a contiguous syntactic unit sufficient to instantiate the relation.

## Canonical anchors

### K01 — REC-N-BASE
- **Reference:** QS Al-Ikhlas 112:1
- **Target span:** `اللَّهُ`
- **Operation:** recognize a simple Qur'anic token as isim.
- **Why clean:** target is token-level noun recognition only.
- **Maturity after recovery:** E1.

### K02 — REC-AL
- **Reference:** QS Al-Fatihah 1:2
- **Target span:** `الْحَمْدُ`
- **Operation:** detect overt `الـ` on an already recognizable noun.
- **Why clean:** only the prefixed definite article is targeted.
- **Maturity after recovery:** E1.

### K03 — REC-NAK-TAN
- **Reference:** QS Al-Ikhlas 112:1
- **Target span:** `أَحَدٌ`
- **Operation:** recognize simple nominal tanwin/nakirah evidence.
- **Why clean:** token-level nominal feature; no clause function is required.
- **Maturity after recovery:** E1.

### K04 — REC-PREP
- **Reference:** QS Al-Baqarah 2:164
- **Target span:** `فِي`
- **Operation:** recognize a frequent overt preposition.
- **Why clean:** recognition target is the particle itself; PP relation remains K09.
- **Maturity after recovery:** E1.

### K05 — REC-PRON-SEP
- **Reference:** QS Al-Ikhlas 112:1
- **Target span:** `هُوَ`
- **Operation:** recognize a basic detached pronoun.
- **Why clean:** syntactic role/reference analysis is not required at K05.
- **Maturity after recovery:** E1.

### K06 — REC-V-PERF
- **Reference:** QS Al-Isra 17:81
- **Target span:** `جَاءَ`
- **Operation:** recognize a simple perfect verb.
- **Why clean:** fa'il relation is not required for the recognition target.
- **Maturity after recovery:** E1.

### K07 — REC-V-IMPF
- **Reference:** QS An-Nisa 4:26
- **Target span:** `يُرِيدُ`
- **Operation:** recognize a simple imperfect verb.
- **Why clean:** mood/governance and argument structure are not required for recognition.
- **Maturity after recovery:** E1.

### K08 — REL-NOM-PRED
- **Reference:** QS Al-Ikhlas 112:2
- **Target span:** `اللَّهُ الصَّمَدُ`
- **Operation:** identify simple overt mubtada' + overt nominal khabar.
- **Why clean:** minimal nominal predication with no PP, idhafah, or nested clause needed for the target.
- **Maturity after recovery:** E1 (confirmed canonical anchor; next step E2 bank expansion).

### K09 — REL-PP
- **Reference:** QS Al-Baqarah 2:164
- **Target span:** `فِي الْبَحْرِ`
- **Operation:** identify overt preposition + overt noun as jar–majrur.
- **Why clean:** contiguous two-token PP; no attached pronoun or new relation is required.
- **Maturity after recovery:** E1.

### K10 — REL-VS
- **Reference:** QS Al-Isra 17:81
- **Target span:** `جَاءَ الْحَقُّ`
- **Operation:** identify simple verb + overt noun fa'il.
- **Why clean:** overt subject immediately follows a familiar perfect verb; the later coordinated clause is outside the target span.
- **Maturity after recovery:** E1.

## Batch result

Before recovery:
- K01–K07 included E0/E0+ gaps;
- K09/K10 had clean spans but incomplete normalized references;
- K08 already had a fully referenced anchor.

After recovery:
- **K01–K10 all have explicit canonical E1 anchors.**
- No architecture changes were required.
- The next maturity task for this batch is E1→E2: several clean examples per K plus negative/boundary items.

## Management impact

This recovery raises the formal evidence maturity score of K01–K10. The global matrix should be recalculated only after committed recovery batches are incorporated.

**K01–K10 ANCHOR RECOVERY: COMPLETE.**
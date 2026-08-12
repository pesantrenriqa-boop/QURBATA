# L10 Canonical Repair Batch 01 v1.0

**Status:** CANONICAL REPAIR DRAFT — NOT PRODUCTION ENABLED  
**Checkpoint:** L10  
**Authoritative band:** K13–K30  
**Source:** `CANONICAL-REGISTRY-K01-K67-v0.1.md`  
**Purpose:** replace false coverage with explicit canonical-target items. Historical/research items remain preserved separately.

## Repair principles

1. Each repair item targets exactly one canonical learner operation unless explicitly marked integration.
2. Morphology not represented by K13–K30 does not count toward canonical coverage.
3. Earlier competencies may appear as prerequisites but cannot substitute for the target operation.
4. All items remain `production_enabled=false` pending Arabic-content review, duplicate audit, item-quality review, and pilot evidence.

## Canonical repair items

### CR13 — K13 REL-IDHAFAH-2N
- ID: `ARB-PL-L10-CR013-v1.0`
- Reference: QS 110:1
- Span: `نَصْرُ اللَّهِ`
- Prompt: identifikasi dua isim pada idafah sederhana dan tentukan mudaf serta mudaf ilayh.
- Expected: `نصر` = mudaf; `الله` = mudaf ilayh.
- Ambiguity: LOW

### CR14 — K14 REL-MAFUL-ZHAHIR
- ID: `ARB-PL-L10-CR014-v1.0`
- Reference: QS 96:2
- Span: `خَلَقَ الْإِنسَانَ`
- Prompt: tentukan isim zhahir yang menjadi objek langsung dari verba target.
- Expected: `الإنسان` = maf'ul bih zhahir.
- Prerequisite: K10
- Ambiguity: LOW

### CR15 — K15 REC-PRON-ATT
- ID: `ARB-PL-L10-CR015-v1.0`
- Reference: QS 1:7
- Span: `عَلَيْهِمْ`
- Prompt: segmentasikan pronomina terikat dari host-nya tanpa menetapkan fungsi sintaksis lanjutan.
- Expected: host `على`; attached pronoun `هم`.
- Ambiguity: LOW

### CR16 — K16 REC-CONJ
- ID: `ARB-PL-L10-CR016-v1.0`
- Reference: QS 112:3
- Span: `لَمْ يَلِدْ وَلَمْ يُولَدْ`
- Prompt: identifikasi marker koordinasi yang tampak; jangan analisis clause-level coordination penuh.
- Expected: `و` = coordinating particle.
- Ambiguity: LOW

### CR17 — K17 REL-ADJ
- ID: `ARB-PL-L10-CR017-v1.0`
- Reference: QS 9:72
- Span: `الْفَوْزُ الْعَظِيمُ`
- Prompt: identifikasi na'at–man'ut sederhana pada span.
- Expected: `الفوز` = man'ut; `العظيم` = na'at.
- Ambiguity: LOW

### CR18 — K18 REL-POSS-PRON
- ID: `ARB-PL-L10-CR018-v1.0`
- Reference: QS 110:3
- Span: `رَبِّكَ`
- Prompt: tentukan fungsi attached pronoun pada noun host.
- Expected: `ك` = attached pronoun in possessive/genitive relation to `رب`.
- Prerequisite: K13 + K15
- Ambiguity: LOW

### CR19 — K19 REL-CONJ-NOM
- ID: `ARB-PL-L10-CR019-v1.0`
- Reference: QS 55:17
- Span: `الْمَشْرِقَيْنِ ... الْمَغْرِبَيْنِ`
- Prompt: pada dua nominal units yang telah dikenali, tentukan marker yang mengoordinasikan keduanya pada target relation.
- Expected: nominal units are coordinated by `و` in the selected wider span/rubric.
- Prerequisite: K16
- Ambiguity: MEDIUM; exact target span must include the overt coordinator in production form.

### CR20 — K20 REL-PREP-PRON
- ID: `ARB-PL-L10-CR020-v1.0`
- Reference: QS 1:7
- Span: `عَلَيْهِمْ`
- Prompt: tentukan fungsi attached pronoun sebagai complement dari preposition.
- Expected: `هم` = pronominal complement of `على`.
- Prerequisite: K09 + K15
- Ambiguity: LOW

### CR21 — K21 REL-V-OBJ-PRON
- ID: `ARB-PL-L10-CR021-v1.0`
- Reference: QS 93:7
- Span: `فَهَدَىٰ`
- Status: HOLD-CANDIDATE
- Note: this span does not overtly realize an attached object pronoun and therefore cannot yet serve K21. Replacement evidence required from a verified Qur'anic occurrence containing verb + attached object pronoun.
- production_enabled: false

### CR22 — K22 REC-DEM
- ID: `ARB-PL-L10-CR022-v1.0`
- Reference: QS 2:2
- Span: `ذَٰلِكَ`
- Prompt: klasifikasikan target sebagai isim isyarah.
- Expected: demonstrative.
- Ambiguity: LOW

### CR23 — K23 REC-REL
- ID: `ARB-PL-L10-CR023-v1.0`
- Reference: QS 107:1
- Span: `الَّذِي`
- Prompt: klasifikasikan target sebagai isim maushul.
- Expected: relative pronoun/isim maushul.
- Ambiguity: LOW

### CR24 — K24 REL-DEM-PRED
- ID: `ARB-PL-L10-CR024-v1.0`
- Reference: QS 2:2
- Span: `ذَٰلِكَ الْكِتَابُ`
- Prompt: pada ceiling K24, tunjukkan demonstrative sebagai unsur awal nominal dan unsur nominal predicate yang diterima rubric canonical.
- Expected: demonstrative frame recognized as simple nominal predication according to expert-approved rubric.
- Prerequisite: K22 + K08
- Ambiguity: HIGH; Arabic-content review mandatory because full i'rab alternatives must be handled carefully.

### CR25 — K25 REL-V-PP
- ID: `ARB-PL-L10-CR025-v1.0`
- Reference: QS 2:3
- Span: `يُؤْمِنُونَ بِالْغَيْبِ`
- Prompt: tentukan PP yang melekat pada verba target.
- Expected: `بالغيب` = mastered PP attached to `يؤمنون`.
- Prerequisite: K09 + K10
- Ambiguity: LOW

### CR26 — K26 REC-V-IMP
- ID: `ARB-PL-L10-CR026-v1.0`
- Reference: QS 112:1
- Span: `قُلْ`
- Prompt: klasifikasikan target sebagai fi'il amr.
- Expected: imperative verb.
- Ambiguity: LOW

### CR27 — K27 REC-NEG
- ID: `ARB-PL-L10-CR027-v1.0`
- Reference: QS 112:3
- Span: `لَمْ يَلِدْ`
- Prompt: identifikasi particle negatif pada occurrence ini tanpa membuka seluruh analisis jazm.
- Expected: `لم` = negative particle in validated occurrence-specific function.
- Ambiguity: LOW

### CR28 — K28 REC-INT-HAL
- ID: `ARB-PL-L10-CR028-v1.0`
- Reference: QS 76:1
- Span: `هَلْ أَتَىٰ`
- Prompt: identifikasi `هل` sebagai marker interogatif.
- Expected: interrogative marker.
- Ambiguity: LOW

### CR29 — K29 REC-VOC-YA
- ID: `ARB-PL-L10-CR029-v1.0`
- Reference: QS 2:21
- Span: `يَا أَيُّهَا النَّاسُ`
- Prompt: identifikasi `يا` sebagai marker vocative.
- Expected: vocative marker.
- Ambiguity: LOW

### CR30 — K30 REC-FUT
- ID: `ARB-PL-L10-CR030-v1.0`
- Reference: QS 93:5
- Span: `وَلَسَوْفَ يُعْطِيكَ رَبُّكَ`
- Prompt: identifikasi future marker `سوف` dan hubungkan secara lokal ke mudhari' tanpa semantic elaboration.
- Expected: `سوف` = future marker; `يعطيك` = imperfect host verb.
- Prerequisite: K07
- Ambiguity: LOW

## Coverage result after repair batch

Canonical K13–K30 targets explicitly represented: **17/18**.

- Ready as repair candidates: K13, K14, K15, K16, K17, K18, K19, K20, K22, K23, K24, K25, K26, K27, K28, K29, K30.
- Still unresolved: **K21 REL-V-OBJ-PRON** because the repair batch intentionally refuses to invent or use an unverified Qur'anic example.

## Gate decision

L10 canonical repair is **94.44% target-covered (17/18)** at draft level. It is not production-ready. K21 must be closed with verified Qur'anic evidence, then all 18 targets require Arabic-content review and duplicate/function audit.
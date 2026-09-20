# L10 R2 Replacement — P01–P12 v2.0

**Status:** DRAFT-REPLACEMENT — NOT PRODUCTION ENABLED  
**Checkpoint:** L10  
**Recovery class:** R2 SUMMARY-ONLY → VERSIONED REPLACEMENT  
**Rule:** new records; not reconstructions of lost historical wording.  
**Guardrail:** target morphology/phrase operations assigned to L05–L10; no sentence-relation mastery that belongs to L11+ may be required for full credit.

## P01 — attached pronoun recognition
- Canonical ID: `ARB-PL-L10-P001-v2.0`
- Target operation: attached-pronoun recognition
- Reference: QS 1:7
- Span: `عَلَيْهِمْ`
- Prompt: identifikasi unsur pronominal yang melekat dan host-nya tanpa menganalisis seluruh clause.
- Expected: `هم` attached to `على`; local morphology only.
- Response class: recognition
- Ambiguity: LOW
- production_enabled: false

## P02 — possessive attachment boundary
- Canonical ID: `ARB-PL-L10-P002-v2.0`
- Target operation: noun + attached pronoun
- Reference: QS 1:2
- Span: `رَبِّ`
- Prompt: gunakan target span bersama bentuk pembanding `رَبِّكَ` untuk menentukan apa yang berubah ketika pronoun melekat; jangan meminta i'rab sentence-level.
- Expected: recognition of pronominal attachment in comparator; base noun retained.
- Response class: contrast
- Ambiguity: LOW
- production_enabled: false

## P03 — idafah recognition
- Canonical ID: `ARB-PL-L10-P003-v2.0`
- Target operation: idafah
- Reference: QS 110:1
- Span: `نَصْرُ اللَّهِ`
- Prompt: identifikasi dua unsur idafah pada span.
- Expected: `نصر` mudaf; `الله` mudaf ilayh; no wider clause analysis.
- Response class: relation-local
- Ambiguity: LOW
- production_enabled: false

## P04 — adjective phrase recognition
- Canonical ID: `ARB-PL-L10-P004-v2.0`
- Target operation: noun–adjective local relation
- Reference: QS 9:72
- Span: `الْفَوْزُ الْعَظِيمُ`
- Prompt: identifikasi unsur noun dan sifat lokal pada span tanpa menganalisis predikasi ayat.
- Expected: `الفوز` noun/head; `العظيم` adjective/modifier.
- Response class: relation-local
- Ambiguity: LOW
- production_enabled: false

## P05 — prepositional phrase with attached pronoun
- Canonical ID: `ARB-PL-L10-P005-v2.0`
- Target operation: jar phrase + attached pronoun
- Reference: QS 2:2
- Span: `فِيهِ`
- Prompt: pecah bentuk target menjadi prepositional element dan attached pronoun.
- Expected: `في` + `ه`.
- Response class: morphology decomposition
- Ambiguity: LOW
- production_enabled: false

## P06 — plural marker recognition
- Canonical ID: `ARB-PL-L10-P006-v2.0`
- Target operation: plural morphology recognition
- Reference: QS 2:3
- Span: `يُؤْمِنُونَ`
- Prompt: identifikasi marker yang menunjukkan plural participant pada bentuk verba tanpa menentukan seluruh syntax.
- Expected: recognition of plural morphology/ending at assigned ceiling.
- Response class: morphology
- Ambiguity: MEDIUM
- ceiling_note: do not require full conjugational paradigm.
- production_enabled: false

## P07 — dual/plural contrast boundary
- Canonical ID: `ARB-PL-L10-P007-v2.0`
- Target operation: number contrast
- Reference: QS 55:17
- Span: `الْمَشْرِقَيْنِ ... الْمَغْرِبَيْنِ`
- Prompt: tentukan number category yang ditandai oleh kedua bentuk target.
- Expected: dual forms.
- Response class: morphology transfer
- Ambiguity: LOW
- production_enabled: false

## P08 — feminine marker recognition
- Canonical ID: `ARB-PL-L10-P008-v2.0`
- Target operation: feminine morphology recognition
- Reference: QS 54:1
- Span: `السَّاعَةُ`
- Prompt: identifikasi marker bentuk feminin yang tampak pada noun target; jangan menyimpulkan fungsi sintaksisnya.
- Expected: ta marbutah/feminine-form recognition.
- Response class: morphology
- Ambiguity: LOW
- production_enabled: false

## P09 — verbal prefix recognition
- Canonical ID: `ARB-PL-L10-P009-v2.0`
- Target operation: imperfect verbal morphology
- Reference: QS 2:3
- Span: `يُقِيمُونَ`
- Prompt: tunjukkan prefix verbal yang tampak dan bedakan dari noun marker.
- Expected: initial `يـ` as part of imperfect verbal form; no sentence role required.
- Response class: morphology contrast
- Ambiguity: LOW
- production_enabled: false

## P10 — local phrase segmentation
- Canonical ID: `ARB-PL-L10-P010-v2.0`
- Target operation: phrase segmentation
- Reference: QS 1:2
- Span: `رَبِّ الْعَالَمِينَ`
- Prompt: segmentasikan span menjadi dua unsur phrase dan tentukan relation lokal yang dapat dikenali pada ceiling L10.
- Expected: idafah relation; no predication analysis.
- Response class: segmentation
- Ambiguity: LOW
- production_enabled: false

## P11 — morphology versus sentence-role negative control
- Canonical ID: `ARB-PL-L10-P011-v2.0`
- Target operation: feature-ceiling control
- Reference: QS 17:81
- Span: `الْحَقُّ`
- Prompt: jika peserta mengenali noun definiteness/ending tetapi belum menentukan subject/predicate role, apakah target morphology L10 otomatis gagal?
- Expected: tidak; sentence role is outside this item's scored target.
- Response class: negative/boundary
- Ambiguity: LOW
- production_enabled: false

## P12 — first L10 integrative discriminator
- Canonical ID: `ARB-PL-L10-P012-v2.0`
- Target operations: attached pronoun + idafah + modifier/number morphology sampled
- References: QS 1:7; QS 110:1; QS 55:17
- Prompt: lakukan tiga operasi terpisah: pecah attached pronoun, identifikasi idafah, dan tentukan dual morphology. Jangan melakukan parsing sentence-level.
- Expected: three local analyses correctly completed.
- Response class: integrative morphology/phrase
- Ambiguity: LOW
- scoring: segmented 3-part rubric.
- production_enabled: false

## Batch audit

Replacement coverage opened: **12/24 = 50%** of L10 R2 debt.

All records remain draft until canonical K-ID alignment, Arabic-content review, duplicate-function audit, and quality screening are completed.
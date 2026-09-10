# Placement Pilot L10 — Batch 01 v1.0

**Status:** WORKING RESEARCH — QUALITY-REVIEW READY, NON-AUTHORITATIVE  
**Branch:** `agent/quranic-arabic-competency-ladder`  
**Scope:** adaptive placement checkpoint L10  
**Competency band:** K13–K30  
**Guardrail:** item hanya boleh menuntut operasi sampai checkpoint L10. Struktur Stage 3+ boleh tampak pada ayat hanya jika tidak diperlukan untuk memperoleh jawaban benar; jika tidak, item harus HOLD/PREMATURE.

## 1. Tujuan

Membangun verse-level pilot bank L10 setelah pool L04 mencapai 36/36. L10 menguji controlled morphosyntax: relasi bentuk–fungsi yang lebih kaya daripada L04, tetapi belum mengandalkan sentence-relation reasoning Stage 3.

## 2. Item schema

Setiap item menyimpan: Item ID; target K; prerequisite K; Qur'anic reference; target span; response class; prompt; expected response; scoring key; critical misconception; error code; feature ceiling; ambiguity; review status.

## 3. Pilot items P01–P24

P01–P24 dipertahankan dari batch sebelumnya. Coverage mencakup K13–K30: verbal morphology, object recognition, coordination, negation/governance boundaries, nominal markers, demonstratives, relative pronouns/silah, conditional markers, prerequisite probes, transfer, dan integrative local analysis. Seluruh item tetap tunduk pada feature ceiling L10 dan tidak boleh memerlukan Stage-3 reasoning untuk jawaban benar.

## 4. Final expansion P25–P36

### L10-P25 — Independent K17 governance recognition
- Target: K17
- Prerequisite: K13
- Reference: QS 94:7
- Target span: `فَإِذَا فَرَغْتَ فَانصَبْ`
- Response class: recognition/boundary
- Prompt: identifikasi marker pembuka pada span dan jangan analisis hubungan antarklausa secara penuh.
- Expected: `إذا` dikenali sebagai marker pembuka konstruksi; scoring tidak meminta hubungan result/sequence Stage 3.
- Critical misconception: mengubah item lokal menjadi analisis discourse.
- Error: E02/E07
- Feature ceiling: marker recognition only.
- Ambiguity: MEDIUM
- Status: PILOT WITH CEILING NOTE

### L10-P26 — Independent K18 negative-marker contrast
- Target: K18
- Prerequisite: K13/K17
- Reference: QS 93:3
- Target span: `مَا وَدَّعَكَ رَبُّكَ`
- Response class: contrast/classification
- Prompt: identifikasi marker negasi dan bedakan dari `لم` tanpa membahas seluruh temporal semantics.
- Expected: `ما` = marker negasi; bukan `لم` dan tidak boleh diperlakukan sebagai governance yang identik.
- Critical misconception: semua negasi dianggap satu kelas operasional.
- Error: E03/E07
- Ambiguity: LOW
- Status: PILOT CONTRAST

### L10-P27 — Independent K19 nominal-negation boundary
- Target: K19
- Prerequisite: K08
- Reference: QS 2:2
- Target span: `لَا رَيْبَ`
- Response class: transfer/classification
- Prompt: identifikasi marker negatif pada struktur nominal dan nyatakan bahwa target bukan negasi verbal biasa.
- Expected: `لا` = marker negatif pada struktur nominal; tidak menuntut analisis case lanjutan.
- Critical misconception: memaksakan model verbal ke semua `لا`.
- Error: E03/E06
- Ambiguity: LOW
- Status: PILOT TRANSFER

### L10-P28 — Independent K20 prerequisite depth
- Target: K20
- Prerequisite: K08/K19
- Reference: QS 35:3
- Target span: `هَلْ مِنْ خَالِقٍ غَيْرُ اللَّهِ`
- Response class: prerequisite/boundary
- Prompt: identifikasi marker preposisional dan unsur nominal lokal; jangan meminta analisis rhetorical question atau full predicate structure.
- Expected: `مِنْ` = huruf jar; `خالق` = unsur nominal sesudahnya pada target lokal.
- Critical misconception: gagal mempertahankan recognition ketika struktur permukaan kompleks.
- Error: E05/E07
- Feature ceiling: no Stage-3 sentence relation.
- Ambiguity: MEDIUM
- Status: PILOT PREREQUISITE WITH CEILING NOTE

### L10-P29 — Independent K21 coordination + verb transfer
- Target: K21
- Prerequisite: K13/K16
- Reference: QS 108:2
- Target span: `فَصَلِّ لِرَبِّكَ وَانْحَرْ`
- Response class: transfer/integration
- Prompt: identifikasi marker penghubung dan dua unit verbal tanpa menganalisis discourse relation.
- Expected: `و` = koordinasi; `صلِّ` dan `انحر` = dua unit verbal.
- Critical misconception: menyebut urutan makna tanpa mengenali marker koordinasi.
- Error: E04/E06
- Ambiguity: LOW
- Status: PILOT INTEGRATIVE TRANSFER

### L10-P30 — Independent K22/K23 marker discrimination
- Target: K22/K23
- Prerequisite: K08
- Reference: QS 108:1
- Target span: `إِنَّا أَعْطَيْنَاكَ`
- Response class: integration/classification
- Prompt: identifikasi marker pembuka dan bentuk verbal sesudah unsur pronominal tanpa meminta analisis clause relation lebih tinggi.
- Expected: `إنّ` dikenali sebagai marker pembuka; `أعطيناك` dikenali sebagai verbal form; hubungan penuh tidak dinilai.
- Critical misconception: gagal memisahkan marker nominal-governing dari bentuk verbal sesudah struktur pembuka.
- Error: E03/E05
- Ambiguity: MEDIUM
- Status: PILOT INTEGRATIVE WITH CEILING NOTE

### L10-P31 — Integrative K13 + K14 + K16
- Target: K13/K14/K16
- Prerequisite: K10
- Reference: QS 107:3
- Target span: `وَلَا يَحُضُّ عَلَىٰ طَعَامِ الْمِسْكِينِ`
- Response class: integration
- Prompt: identifikasi marker penghubung/negasi, fi'il mudhari', dan batas objek/prepositional complement tanpa menganalisis discourse.
- Expected: `و` = penghubung; `لا` = marker negatif; `يحض` = fi'il mudhari'; `على` membuka prepositional complement.
- Critical misconception: menganggap seluruh unsur sesudah fi'il sebagai satu objek langsung.
- Error: E03/E04/E05
- Feature ceiling: no semantic/discourse scoring.
- Ambiguity: MEDIUM
- Status: PILOT INTEGRATIVE

### L10-P32 — Integrative K24 + K26 contrast
- Target: K24/K26
- Prerequisite: nominal recognition
- Reference: QS 2:5
- Target spans: `أُولَٰئِكَ` / QS 1:7 `الَّذِينَ`
- Response class: contrast/integration
- Prompt: klasifikasikan dua bentuk dan jelaskan perbedaannya hanya pada tingkat jenis bentuk.
- Expected: `أولئك` = isim isyarah; `الذين` = isim maushul.
- Critical misconception: menyamakan bentuk closed-class nominal karena keduanya merujuk referen.
- Error: E02/E07
- Ambiguity: LOW
- Status: PILOT CONTRAST INTEGRATIVE

### L10-P33 — Integrative K26 + K27
- Target: K26/K27
- Prerequisite: K13
- Reference: QS 107:1
- Target span: `الَّذِي يُكَذِّبُ بِالدِّينِ`
- Response class: integration/relation-lite
- Prompt: identifikasi isim maushul dan batas silah pada span; jangan melacak referential dependency di atas ceiling.
- Expected: `الذي` = isim maushul; `يكذب بالدين` = silah pada target span.
- Critical misconception: mengharuskan antecedent/resumptive analysis untuk menjawab operasi lokal.
- Error: E04/E05
- Ambiguity: LOW
- Status: PILOT INTEGRATIVE

### L10-P34 — Integrative K29/K30 conditional boundary
- Target: K29/K30
- Prerequisite: K13
- Reference: QS 110:1–2
- Target span: `إِذَا جَاءَ نَصْرُ اللَّهِ ... وَرَأَيْتَ النَّاسَ`
- Response class: integration/boundary
- Prompt: identifikasi marker pembuka dan unit-unit verbal yang masih berada dalam bagian kondisi tanpa menuntut analisis jawab lengkap.
- Expected: `إذا` = marker kondisional; `جاء` dan `رأيت` dikenali sebagai unit verbal dalam konstruksi yang dibuka marker tersebut; jawaban penuh belum menjadi target.
- Critical misconception: menganggap setiap unit setelah `إذا` sebagai jawab syarat.
- Error: E04/E07
- Feature ceiling: no full interclause relation scoring.
- Ambiguity: MEDIUM
- Status: PILOT INTEGRATIVE BOUNDARY

### L10-P35 — Prerequisite integrity mixed probe
- Target: K13/K16/K24/K26
- Prerequisite: K01–K12
- Reference: QS 2:2–3
- Target spans: `ذَٰلِكَ الْكِتَابُ` / `الَّذِينَ يُؤْمِنُونَ`
- Response class: prerequisite/integration
- Prompt: klasifikasikan bentuk demonstratif, relative pronoun, dan verbal form yang tampak; jangan menganalisis hubungan ayat penuh.
- Expected: `ذلك` = isim isyarah; `الذين` = isim maushul; `يؤمنون` = fi'il mudhari'.
- Critical misconception: kehilangan klasifikasi dasar ketika beberapa operasi tampil berdekatan.
- Error: E05/E06
- Ambiguity: LOW
- Status: PILOT PREREQUISITE INTEGRATIVE

### L10-P36 — Final six-operation discriminator
- Target: sampled K13–K30 integration
- Prerequisite: L04 mastery
- Reference: QS 1:5–7
- Target spans: `إِيَّاكَ نَعْبُدُ` / `وَإِيَّاكَ نَسْتَعِينُ` / `الَّذِينَ أَنْعَمْتَ`
- Response class: integration/discrimination
- Prompt: dari tiga span, tunjukkan (a) objek didahulukan, (b) fi'il mudhari', (c) marker koordinasi, dan (d) isim maushul + awal silah. Tidak ada skor untuk tafsir/discourse.
- Expected: `إياك` = objek; `نعبد/نستعين` = fi'il mudhari'; `و` = koordinasi; `الذين` = isim maushul; `أنعمت` = awal silah.
- Critical misconception: mampu menghafal label tunggal tetapi gagal mempertahankan beberapa operasi lokal secara simultan.
- Error: E04/E05/E06
- Feature ceiling: scoring hanya operasi K13–K30 yang eksplisit.
- Ambiguity: MEDIUM; wajib rubric tersegmentasi.
- Status: PILOT FINAL DISCRIMINATOR

## 5. Final distribution audit — 36 items

Pool size: **36/36 = 100% target minimum**.

Functional coverage (multi-tag allowed):
- direct/classification: >=12 exposures;
- negative/contrast/boundary: >=6;
- prerequisite-integrity: >=6;
- transfer: >=6;
- integrative: >=6.

Competency coverage: **K13–K30 all represented**. Final 12 deliberately increase independent evidence for K17–K23 and multi-operation integration.

## 6. PREMATURE / feature-ceiling audit

### PASS
An item is usable at L10 when the correct response can be obtained entirely with operations at or below K30.

### PASS WITH CEILING NOTE
Higher Stage-3+ structure may appear on the surface only if:
1. it is outside the scored target;
2. the prompt explicitly limits the learner operation;
3. the expected response does not require naming the higher relation;
4. the rubric records what is intentionally ignored.

This applies particularly to P10, P12, P17, P20, P23, P25, P28, P30, P31, P34, and P36.

### HOLD / PREMATURE trigger
If Arabic-content review determines that a correct answer necessarily requires Stage-3 sentence relation, interclause reasoning, discourse interpretation, or another K31+ operation, the item must be removed from automated routing until rewritten. Authentic Qur'anic provenance alone does not make an item level-valid.

## 7. Six-item assembly simulation rule

A valid L10 routing assembly must contain exactly six scored core items satisfying all of the following:
- at least 4 distinct target competencies;
- at least 1 prerequisite-integrity probe;
- at least 1 contrast/negative-control item;
- at least 1 transfer item;
- at least 1 integrative item;
- no more than 2 items sharing the same primary target K;
- at least 2 different surahs where feasible.

Working mastery gate remains provisional: **>=5/6 plus prerequisite and transfer integrity, with no critical misconception**. A 4/6 or prerequisite/transfer failure opens 3–5 local diagnostics across L05–L10.

## 8. Quality-review decision

**Decision: L10 POOL COMPLETE — READY FOR CONTENT QUALITY REVIEW, NOT YET PRODUCTION-FROZEN.**

Before operational use:
1. Arabic-content review validates labels, spans, and ceiling assumptions;
2. item-quality review checks prompt clarity and scoring leakage;
3. MEDIUM ambiguity items receive explicit rubrics;
4. assembly simulations test adaptive balance;
5. pilot data is required before final cut-score freeze.

## 9. Next work package

1. Keep L04 and L10 in quality-review queue.
2. Open **L13 placement pilot** for Stage-3 sentence relations.
3. Preserve item IDs once pilot data collection starts; substantive revisions then require versioning.

## 10. Governance

Dokumen berada di research layer PR #4. Tidak mengubah registry produksi. Production freeze membutuhkan Arabic-content review, item-quality review, pilot data, dan mapping RIQA OS.
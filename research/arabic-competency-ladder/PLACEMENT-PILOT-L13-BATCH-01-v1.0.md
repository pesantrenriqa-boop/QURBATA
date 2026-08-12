# Placement Pilot L13 — Batch 01 v1.0

**Status:** WORKING RESEARCH — QUALITY-REVIEW READY, NON-AUTHORITATIVE  
**Branch:** `agent/quranic-arabic-competency-ladder`  
**Scope:** adaptive placement checkpoint L13  
**Competency band:** K31–K39  
**Stage:** S3 — Sentence Relations  
**Guardrail:** item boleh menguji relasi sintaksis sampai K39, tetapi tidak boleh membutuhkan Complex Clause Integration K40+ untuk memperoleh jawaban benar.

## 1. Tujuan

Membangun bank placement L13 setelah L04 dan L10 mencapai pool minimum 36/36. L13 adalah checkpoint pertama yang secara eksplisit menilai hubungan antarkomponen kalimat, bukan hanya pengenalan bentuk dan controlled morphosyntax.

Target pool minimum: **36 item — COMPLETE**.

## 2. Item schema

Item ID; target K; prerequisite; Qur'anic reference; target span; response class; prompt; expected response; scoring key; critical misconception; error code; feature ceiling; ambiguity; review status.

## 3. Pilot items P01–P24

P01–P24 dipertahankan dari batch sebelumnya. Coverage mencakup K31 nominal predication, K32 verbal subject relation, K33 verb–object relation, K34 coordination, K35 demonstrative relation, K36 relative local relation, K37 predicate fronting, K38 multi-local integration, K39 conditional boundary, plus transfer, contrast, prerequisite routing, and morphology-vs-relation discrimination.

## 4. Final balancing P25–P36

### L13-P25 — Surface-order variation K31
- Target: K31
- Prerequisite: K08/K12
- Reference: QS 39:62
- Target span: `اللَّهُ خَالِقُ كُلِّ شَيْءٍ`
- Response class: relation/transfer
- Prompt: identifikasi unsur nominal awal dan predikat nominal utamanya tanpa menganalisis seluruh idhafah secara rinci.
- Expected: `الله` = mubtada'/unsur nominal awal; `خالق` = inti khabar/predikat nominal.
- Critical misconception: gagal mengenali predikasi karena khabar diikuti complement tambahan.
- Error: E05/E06
- Feature ceiling: inner idhafah not scored.
- Ambiguity: MEDIUM
- Status: PILOT TRANSFER WITH CEILING NOTE

### L13-P26 — Surface-order variation K32
- Target: K32
- Prerequisite: K06/K10
- Reference: QS 61:14
- Target span: `قَالَ الْحَوَارِيُّونَ`
- Response class: relation/transfer
- Prompt: tentukan relasi verba–fa'il pada span.
- Expected: `قال` = fi'il; `الحواريون` = fa'il zhahir.
- Critical misconception: kesulitan ketika fa'il berbentuk jamak.
- Error: E05/E06
- Ambiguity: LOW
- Status: PILOT TRANSFER

### L13-P27 — Surface-order variation K33
- Target: K33
- Prerequisite: K14
- Reference: QS 93:9
- Target span: `فَلَا تَقْهَرْ الْيَتِيمَ`
- Response class: relation/transfer
- Prompt: identifikasi verba dan objek langsung pada span tanpa menganalisis fungsi `فـ` di atas target.
- Expected: `تقهر` = verba; `اليتيم` = maf'ul bih/objek langsung.
- Critical misconception: semua nomina pascaverba dianggap fa'il.
- Error: E05/E06/E07
- Ambiguity: LOW
- Status: PILOT TRANSFER

### L13-P28 — Coordination scope discriminator K34
- Target: K34
- Prerequisite: K16/K32/K33
- Reference: QS 93:9–10
- Target spans: `فَلَا تَقْهَرْ` / `وَأَمَّا السَّائِلَ فَلَا تَنْهَرْ`
- Response class: contrast/integration
- Prompt: identifikasi marker koordinatif yang benar-benar menghubungkan unit target; bedakan dari marker lain yang hanya membuka struktur lokal.
- Expected: peserta tidak menyamakan setiap `فـ/و` sebagai fungsi identik; koordinasi harus dibuktikan dari unit yang dihubungkan.
- Critical misconception: marker recognition tanpa scope relation.
- Error: E05/E07/E08
- Feature ceiling: no discourse interpretation.
- Ambiguity: MEDIUM
- Status: PILOT INTEGRATIVE REVIEW

### L13-P29 — L11 routing probe
- Target: K31/K32
- Prerequisite: K08/K10
- Reference: QS 54:1
- Target span: `اقْتَرَبَتِ السَّاعَةُ`
- Response class: prerequisite-routing
- Prompt: sebelum menetapkan relation, klasifikasikan dulu jenis unit verbal dan identifikasi isim zhahir yang terkait.
- Expected: prerequisite recognition benar; `الساعة` kemudian ditetapkan sebagai fa'il.
- Critical misconception: relation guess benar tetapi parsing dasar salah.
- Error: E05/E08
- Ambiguity: LOW
- Status: PILOT ROUTING PROBE

### L13-P30 — L12 routing probe
- Target: K37
- Prerequisite: K09/K12/K31
- Reference: QS 30:4
- Target span: `لِلَّهِ الْأَمْرُ`
- Response class: prerequisite-routing/transfer
- Prompt: identifikasi PP lebih dulu, lalu tentukan apakah PP itu berfungsi predikatif pada span.
- Expected: `لله` dikenali sebagai jar-majrur; lalu dipetakan sebagai unsur predikatif depan terhadap `الأمر`.
- Critical misconception: prerequisite benar tetapi tidak mampu naik ke relation, atau relation ditebak tanpa segmentasi benar.
- Error: E05/E08
- Ambiguity: LOW
- Status: PILOT ROUTING TRANSFER

### L13-P31 — Integrative subject + object contrast
- Target: K32/K33
- Prerequisite: K10/K14
- Reference: QS 96:1–2
- Target spans: `اقْرَأْ` / `خَلَقَ الْإِنسَانَ`
- Response class: integration/contrast
- Prompt: pada unit kedua, tentukan apakah `الإنسان` subjek atau objek, lalu jelaskan mengapa posisi setelah verba tidak cukup menentukan fungsi.
- Expected: `الإنسان` = objek pada target `خلق الإنسان`; fungsi ditentukan relation, bukan posisi saja.
- Critical misconception: semua isim setelah fi'il = fa'il.
- Error: E05/E07/E08
- Ambiguity: LOW
- Status: PILOT INTEGRATIVE

### L13-P32 — Integrative relative + verbal relation
- Target: K36/K32/K33
- Prerequisite: K26/K27/K10/K14
- Reference: QS 107:1–2
- Target span: `الَّذِي يُكَذِّبُ بِالدِّينِ فَذَٰلِكَ الَّذِي يَدُعُّ الْيَتِيمَ`
- Response class: integration/discrimination
- Prompt: tunjukkan satu relative relation dan satu verb–object relation yang dapat dipastikan tanpa menilai discourse link antarbagian.
- Expected: `الذي` dihubungkan dengan silah lokalnya; `اليتيم` dihubungkan sebagai objek dengan `يدع`.
- Critical misconception: hanya menyebut labels tanpa relation atau masuk ke discourse interpretation.
- Error: E05/E08
- Feature ceiling: discourse relation excluded.
- Ambiguity: MEDIUM
- Status: PILOT INTEGRATIVE WITH CEILING NOTE

### L13-P33 — Integrative predicate-fronting + nominal relation
- Target: K31/K37
- Prerequisite: K09/K12
- Reference: QS 45:36
- Target span: `فَلِلَّهِ الْحَمْدُ`
- Response class: integration/transfer
- Prompt: identifikasi unsur PP depan dan relasi predikatifnya dengan isim utama.
- Expected: `لله` = unsur predikatif depan; `الحمد` = unsur nominal utama.
- Critical misconception: mampu mengenali kedua bentuk tetapi gagal menghubungkannya.
- Error: E05/E06/E08
- Ambiguity: LOW
- Status: PILOT INTEGRATIVE TRANSFER

### L13-P34 — Conditional-domain integrative boundary
- Target: K39/K32
- Prerequisite: K29/K30/K10
- Reference: QS 99:1
- Target span: `إِذَا زُلْزِلَتِ الْأَرْضُ`
- Response class: integration/boundary
- Prompt: identifikasi domain lokal `إذا` dan relation verbal internalnya; jangan menilai jawab/result yang belum ada.
- Expected: `إذا` membuka domain; `زلزلت الأرض` dianalisis sebagai unit verbal lokal pada ceiling L13.
- Critical misconception: gagal memisahkan relation internal dari full condition-result relation.
- Error: E05/E07/E08
- Ambiguity: MEDIUM
- Status: PILOT INTEGRATIVE BOUNDARY

### L13-P35 — Cross-relation discriminator
- Target: K31/K32/K33/K34
- Prerequisite: L10 operations
- Reference: QS 17:81
- Target span: `جَاءَ الْحَقُّ وَزَهَقَ الْبَاطِلُ`
- Response class: integration/discrimination
- Prompt: petakan dua verba, dua fa'il, dan marker koordinasi; jelaskan bahwa tidak ada objek langsung pada dua unit target.
- Expected: `جاء–الحق` dan `زهق–الباطل` masing-masing verba–fa'il; `و` mengoordinasikan; tidak ada maf'ul bih pada target.
- Critical misconception: satu nomina dipaksa menjadi objek karena pola hafalan.
- Error: E05/E07/E08
- Ambiguity: LOW
- Status: PILOT FINAL INTEGRATION

### L13-P36 — Final checkpoint discriminator
- Target: K31–K39 sampled integration
- Prerequisite: K31/K32/K33/K34/K36/K37
- Reference: mixed short spans from QS 112:2, 17:81, 107:1–2, 45:36
- Response class: integration/discrimination
- Prompt: dari empat span pendek, pilih dan jelaskan (a) satu predikasi nominal, (b) satu verba–fa'il, (c) satu verba–objek, (d) satu relative relation, dan (e) satu predicate-fronting relation. Translation-only answer tidak cukup.
- Expected: peserta dapat menunjukkan relation yang tepat pada masing-masing contoh tanpa membutuhkan K40+.
- Critical misconception: category knowledge without relation mastery.
- Error: E01/E05/E08
- Feature ceiling: all scoring capped at K39.
- Ambiguity: MEDIUM; segmented rubric mandatory.
- Status: PILOT FINAL DISCRIMINATOR

## 5. Final distribution audit — 36 items

Pool size: **36/36 = 100% target minimum**.

Coverage:
- K31–K34: multiple direct, transfer, contrast, and integrative exposures;
- K35–K37: independent anchors + negative controls + transfer;
- K38: multi-local prerequisite/integration probes;
- K39: multiple conditional environments + incomplete-relation boundaries + integrative domain item.

Functional minimums satisfied:
- direct relation >= 6;
- contrast/negative/boundary >= 6;
- prerequisite-routing >= 6 when multi-tag probes are counted;
- transfer >= 6;
- integrative/discrimination >= 6.

Tags overlap by design; counts do not need to sum to 36.

## 6. PREMATURE / feature-ceiling audit

### PASS
Item is usable when the correct answer can be obtained entirely with K31–K39 plus prerequisites.

### PASS WITH CEILING NOTE
Item may contain surface K40+ material only when:
1. that material is outside the scored target;
2. no K40+ label/reconstruction is needed;
3. rubric explicitly states what is ignored.

### HOLD/PREMATURE
Any item must be removed from automated routing if:
- full subordinate/complex-clause integration is necessary;
- discourse relation is required to distinguish the answer;
- referential reconstruction above K39 is necessary;
- multiple plausible analyses remain without manual review.

Items P28, P32, P34, P36 remain especially dependent on segmented rubrics and Arabic-content review.

## 7. Six-item assembly simulation

A valid L13 form can be assembled with:
- 1 K31/K37 predication item;
- 1 K32 subject-relation item;
- 1 K33 object-relation item;
- 1 K36 relative-relation item;
- 1 contrast/boundary item;
- 1 integrative discriminator.

Gate:
- >=4 distinct primary K;
- >=1 prerequisite-routing probe;
- >=1 contrast/negative control;
- >=1 transfer item;
- >=1 integrative relation item;
- >=1 explicit relation response, not category-only.

Failure on prerequisite or relation integrity routes locally to L11/L12/L13 diagnosis, not to L01.

## 8. Quality-review decision

**Decision: L13 POOL COMPLETE — READY FOR CONTENT QUALITY REVIEW, NOT PRODUCTION-FROZEN.**

Before operational use:
1. Arabic-content review validates every relation and target span;
2. medium-ambiguity items receive segmented scoring rubrics;
3. item-quality review checks prompt clarity and ceiling leakage;
4. six-item assembly simulations are repeated on multiple forms;
5. pilot data is required before cut-score freeze.

## 9. Next work package

Open **L19 Placement Pilot** for S4 Complex Clause Integration, maintaining the same separation between authentic Qur'anic complexity and what is actually scored.

## 10. Governance

Research layer only. No production freeze. Promotion requires Arabic-content review, item-quality review, pilot evidence, cut-score validation, and RIQA OS mapping.
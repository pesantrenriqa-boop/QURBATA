# Placement Pilot L13 — Batch 01 v1.0

**Status:** WORKING RESEARCH — NON-AUTHORITATIVE  
**Branch:** `agent/quranic-arabic-competency-ladder`  
**Scope:** adaptive placement checkpoint L13  
**Competency band:** K31–K39  
**Stage:** S3 — Sentence Relations  
**Guardrail:** item boleh menguji relasi sintaksis sampai K39, tetapi tidak boleh membutuhkan Complex Clause Integration K40+ untuk memperoleh jawaban benar.

## 1. Tujuan

Membangun bank placement L13 setelah L04 dan L10 mencapai pool minimum 36/36. L13 adalah checkpoint pertama yang secara eksplisit menilai hubungan antarkomponen kalimat, bukan hanya pengenalan bentuk dan controlled morphosyntax.

Target pool minimum: **36 item**.

## 2. Item schema

Item ID; target K; prerequisite; Qur'anic reference; target span; response class; prompt; expected response; scoring key; critical misconception; error code; feature ceiling; ambiguity; review status.

## 3. Pilot items P01–P12

P01–P12 dipertahankan dari batch awal. Coverage mencakup K31 nominal predication, K32 verbal subject relation, K33 verb–object relation, K34 coordination, K35 demonstrative relation, K36 relative local relation, K37 predicate fronting, K38 multi-local integration, K39 conditional boundary, plus transfer/contrast and an integrative discriminator.

Anchor yang dipertahankan antara lain QS 112:2 `اللَّهُ الصَّمَدُ`, QS 17:81 `جَاءَ الْحَقُّ`, QS 1:5 `إِيَّاكَ نَعْبُدُ`, QS 112:3 `لَمْ يَلِدْ وَلَمْ يُولَدْ`, QS 2:2 `ذَٰلِكَ الْكِتَابُ`, QS 107:1 `الَّذِي يُكَذِّبُ`, QS 45:36 `لِلَّهِ الْحَمْدُ`, dan QS 110:1 `إِذَا جَاءَ نَصْرُ اللَّهِ`.

## 4. Expansion P13–P24

### L13-P13 — K35 independent demonstrative relation
- Target: K35
- Prerequisite: K24/K25
- Reference: QS 2:5
- Target span: `أُولَٰئِكَ عَلَىٰ هُدًى`
- Response class: relation/transfer
- Prompt: identifikasi demonstratif dan unsur predikatif lokal sesudahnya tanpa memasuki discourse interpretation.
- Expected: `أولئك` = demonstratif/unsur nominal awal; `على هدى` = unsur predikatif lokal pada ceiling L13.
- Critical misconception: hanya mengklasifikasikan `أولئك` tanpa menunjukkan relasi.
- Error: E04/E06
- Ambiguity: MEDIUM
- Status: PILOT TRANSFER WITH CEILING NOTE

### L13-P14 — K35 contrast control
- Target: K35
- Reference: QS 1:7
- Target span: `الَّذِينَ أَنْعَمْتَ`
- Response class: negative/contrast
- Prompt: apakah bentuk awal target merupakan demonstratif yang berelasi dengan isim sesudahnya?
- Expected: tidak; `الذين` adalah isim maushul dan membuka relasi relative.
- Critical misconception: semua bentuk nominal tertutup dianggap demonstratif.
- Error: E02/E07
- Ambiguity: LOW
- Status: PILOT NEGATIVE CONTROL

### L13-P15 — K36 independent relative relation
- Target: K36
- Prerequisite: K26/K27
- Reference: QS 2:3
- Target span: `الَّذِينَ يُؤْمِنُونَ`
- Response class: relation/transfer
- Prompt: tentukan hubungan isim maushul dengan unit verbal sesudahnya.
- Expected: `الذين` membuka relative construction; `يؤمنون` berada pada silah yang melengkapinya secara lokal.
- Critical misconception: mengidentifikasi bentuk tetapi tidak menghubungkannya dengan silah.
- Error: E04/E06
- Ambiguity: LOW
- Status: PILOT TRANSFER

### L13-P16 — K36 boundary against antecedent/resumptive analysis
- Target: K36
- Prerequisite: K26/K27
- Reference: QS 107:1
- Target span: `الَّذِي يُكَذِّبُ`
- Response class: boundary
- Prompt: apakah untuk menjawab target ini peserta harus merekonstruksi seluruh referential dependency dari antecedent sampai resumptive element?
- Expected: tidak; L13 hanya menilai local relative relation. Analisis referential yang lebih tinggi ditahan.
- Critical misconception: mengira setiap relative item wajib dianalisis sampai dependency referensial penuh.
- Error: E07/E08
- Ambiguity: LOW
- Status: PILOT BOUNDARY

### L13-P17 — K37 independent predicate-fronting transfer
- Target: K37
- Prerequisite: K09/K12/K31
- Reference: QS 39:3
- Target span: `لِلَّهِ الدِّينُ`
- Response class: relation/transfer
- Prompt: tentukan relasi predikatif lokal antara jar-majrur depan dan unsur nominal sesudahnya.
- Expected: `لله` = unsur predikatif depan; `الدين` = unsur nominal yang dipredikasikan pada ceiling L13.
- Critical misconception: semua jar-majrur hanya dianggap keterangan tambahan.
- Error: E05/E06
- Ambiguity: LOW
- Status: PILOT TRANSFER

### L13-P18 — K37 contrast boundary
- Target: K37
- Prerequisite: K09
- Reference: QS 113:1
- Target span: `بِرَبِّ الْفَلَقِ`
- Response class: negative/contrast
- Prompt: apakah span ini dengan sendirinya merupakan predikasi jar-majrur depan seperti `لله الحمد`?
- Expected: tidak; hanya adanya jar-majrur tidak cukup membuktikan fungsi predikatif.
- Critical misconception: menyamakan bentuk PP dengan fungsi predicate-fronting.
- Error: E05/E07
- Ambiguity: LOW
- Status: PILOT NEGATIVE CONTROL

### L13-P19 — K38 multi-local relation transfer
- Target: K38
- Prerequisite: K32/K33/K34
- Reference: QS 2:3
- Target span: `يُؤْمِنُونَ بِالْغَيْبِ وَيُقِيمُونَ الصَّلَاةَ`
- Response class: integration/transfer
- Prompt: identifikasi dua relasi verbal lokal dan marker koordinasi tanpa memberi analisis discourse antarklausa.
- Expected: `يؤمنون` membentuk unit verbal dengan complement lokal; `يقيمون الصلاة` memuat verba + objek; `و` mengoordinasikan dua unit.
- Critical misconception: mampu mengenali marker tetapi gagal mempertahankan dua relasi lokal sekaligus.
- Error: E05/E06/E08
- Feature ceiling: discourse relation excluded.
- Ambiguity: MEDIUM
- Status: PILOT INTEGRATIVE TRANSFER

### L13-P20 — K38 prerequisite routing probe
- Target: K38
- Prerequisite: K32/K33
- Reference: QS 17:81
- Target span: `جَاءَ الْحَقُّ وَزَهَقَ الْبَاطِلُ`
- Response class: prerequisite/integration
- Prompt: petakan subjek verbal masing-masing unit dan marker koordinasi.
- Expected: `الحق` berelasi sebagai fa'il dengan `جاء`; `الباطل` berelasi sebagai fa'il dengan `زهق`; `و` menghubungkan dua unit.
- Critical misconception: relasi lokal runtuh ketika dua unit diletakkan berdampingan.
- Error: E05/E08
- Ambiguity: LOW
- Status: PILOT PREREQUISITE INTEGRATION

### L13-P21 — K39 independent conditional marker relation
- Target: K39
- Prerequisite: K29/K30
- Reference: QS 99:1
- Target span: `إِذَا زُلْزِلَتِ الْأَرْضُ`
- Response class: relation/transfer
- Prompt: identifikasi marker pembuka dan unit yang berada dalam domain awalnya; jangan menilai result clause yang belum muncul.
- Expected: `إذا` membuka konstruksi kondisional/temporal; `زلزلت الأرض` berada pada domain awal.
- Critical misconception: marker dikenali tetapi domain lokal tidak dapat ditentukan.
- Error: E05/E06
- Ambiguity: MEDIUM
- Status: PILOT TRANSFER WITH CEILING NOTE

### L13-P22 — K39 negative control: incomplete condition-result
- Target: K39
- Prerequisite: K29/K30
- Reference: QS 110:1
- Target span: `إِذَا جَاءَ نَصْرُ اللَّهِ`
- Response class: negative/boundary
- Prompt: apakah span ini sudah cukup untuk menyatakan relation lengkap syarat–jawab?
- Expected: tidak; marker dan domain awal ada, tetapi result/jawab belum berada dalam target span.
- Critical misconception: marker + protasis dianggap otomatis sama dengan seluruh condition-result relation.
- Error: E05/E07
- Ambiguity: LOW
- Status: PILOT NEGATIVE CONTROL

### L13-P23 — L11/L12 prerequisite-routing probe
- Target: K31/K37
- Prerequisite: K08/K09/K12
- Reference: QS 30:4
- Target span: `لِلَّهِ الْأَمْرُ`
- Response class: prerequisite/relation
- Prompt: pertama identifikasi jar-majrur dan isim; kemudian tentukan apakah keduanya membentuk relasi predikatif pada span.
- Expected: prerequisite recognition benar lebih dulu; `لله` kemudian dihubungkan secara predikatif dengan `الأمر`.
- Critical misconception: jawaban relation benar secara tebak tetapi prerequisite parsing salah.
- Error: E05/E08
- Ambiguity: LOW
- Status: PILOT ROUTING PROBE

### L13-P24 — Morphology-vs-relation discriminator
- Target: K32/K33/K36
- Prerequisite: L10 operations
- Reference: QS 107:1–2
- Target spans: `الَّذِي يُكَذِّبُ بِالدِّينِ` / `فَذَٰلِكَ الَّذِي يَدُعُّ الْيَتِيمَ`
- Response class: discrimination/integration
- Prompt: jangan hanya klasifikasikan bentuk. Tunjukkan satu relative relation dan satu verb–object relation yang dapat dipastikan dari target spans pada ceiling L13.
- Expected: peserta menunjukkan `الذي` dengan silah lokalnya serta relasi verbal–objek yang sah pada span kedua; jawaban berbasis label kata saja tidak cukup.
- Critical misconception: menganggap morphology recognition sudah sama dengan sentence-relation mastery.
- Error: E04/E05/E08
- Feature ceiling: no K40+ complex-clause/discourse inference.
- Ambiguity: MEDIUM; Arabic-content review wajib memastikan target object relation dipilih pada token yang tepat.
- Status: PILOT INTEGRATIVE REVIEW

## 5. Distribution audit after P24

Pool size: **24/36 = 66.67%**.

Coverage status:
- K31–K34 already have multiple anchors and contrasts;
- K35 now has independent transfer + contrast;
- K36 now has independent transfer + boundary;
- K37 now has two fronted-predicate anchors + negative control;
- K38 now has multiple multi-local integration/prerequisite probes;
- K39 now has more than one conditional environment plus incomplete-relation negative controls.

Functional balance:
- direct relation: adequate;
- negative/contrast: strengthened;
- prerequisite routing: strengthened through P20/P23;
- transfer: strengthened across QS 2, 17, 39, 99;
- integrative/discrimination: P19/P20/P24 plus earlier items.

## 6. Remaining gaps P25–P36

1. add at least 3 more integrative items with 2–3 local relations;
2. add at least 2 more prerequisite-routing probes to distinguish L11 vs L12 gaps;
3. add surface-order variation for K31–K37;
4. perform final PREMATURE/feature-ceiling audit;
5. simulate a six-item L13 form with >=4 primary K, >=1 prerequisite, >=1 contrast, >=1 transfer, >=1 integrative relation item;
6. HOLD any item requiring K40+ complex-clause interpretation.

## 7. Working six-item assembly gate

A selected L13 checkpoint form must include:
- >=4 distinct primary K;
- >=1 prerequisite probe;
- >=1 contrast/negative control;
- >=1 transfer item;
- >=1 integrative relation item;
- >=1 item requiring an explicit relation, not merely category recognition.

Failure on prerequisite or relation-integrity opens local diagnosis within L11–L13 rather than resetting to L01.

## 8. Governance

Research layer only. No production freeze. Promotion requires Arabic-content review, item-quality review, pilot evidence, cut-score validation, and RIQA OS mapping.
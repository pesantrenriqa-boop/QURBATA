# Placement Pilot L13 — Batch 01 v1.0

**Status:** WORKING RESEARCH — NON-AUTHORITATIVE  
**Branch:** `agent/quranic-arabic-competency-ladder`  
**Scope:** adaptive placement checkpoint L13  
**Competency band:** K31–K39  
**Stage:** S3 — Sentence Relations  
**Guardrail:** item boleh menguji relasi sintaksis sampai K39, tetapi tidak boleh membutuhkan Complex Clause Integration K40+ untuk memperoleh jawaban benar.

## 1. Tujuan

Membuka bank placement L13 setelah L04 dan L10 mencapai pool minimum 36/36. L13 berfungsi sebagai checkpoint pertama yang secara eksplisit menguji hubungan antarkomponen kalimat, bukan hanya pengenalan bentuk dan controlled morphosyntax.

Target pool minimum: **36 item**. Batch pertama: **12 item**.

## 2. Item schema

Item ID; target K; prerequisite; Qur'anic reference; target span; response class; prompt; expected response; scoring key; critical misconception; error code; feature ceiling; ambiguity; review status.

## 3. Pilot items P01–P12

### L13-P01 — Nominal relation anchor
- Target: K31
- Prerequisite: K08/K11
- Reference: QS 112:2
- Target span: `اللَّهُ الصَّمَدُ`
- Response class: relation
- Prompt: tentukan dua unsur utama predikasi nominal pada span.
- Expected: `الله` sebagai unsur nominal awal/mubtada'; `الصمد` sebagai predikat/khabar pada analisis dasar.
- Critical misconception: hanya menyebut dua isim tanpa relasi.
- Error: E04/E05
- Ambiguity: LOW
- Status: PILOT

### L13-P02 — Negative nominal-relation control
- Target: K31
- Prerequisite: K09
- Reference: QS 2:2
- Target span: `فِيهِ هُدًى`
- Response class: contrast/boundary
- Prompt: apakah span ini identik dengan pola dua isim berurutan seperti `الله الصمد`?
- Expected: tidak; relasi permukaannya berbeda dan mengandung unsur preposisional.
- Critical misconception: semua predikasi nominal dipaksa menjadi pola dua isim berurutan.
- Error: E05/E07
- Ambiguity: MEDIUM
- Status: PILOT NEGATIVE CONTROL

### L13-P03 — Verbal subject relation
- Target: K32
- Prerequisite: K06/K10
- Reference: QS 17:81
- Target span: `جَاءَ الْحَقُّ`
- Response class: relation
- Prompt: tentukan relasi antara fi'il dan isim sesudahnya.
- Expected: `جاء` = fi'il; `الحق` = fa'il/subjek verbal zhahir.
- Critical misconception: isim setelah fi'il otomatis objek.
- Error: E04/E05
- Ambiguity: LOW
- Status: PILOT

### L13-P04 — Verb-object relation
- Target: K33
- Prerequisite: K14
- Reference: QS 1:5
- Target span: `إِيَّاكَ نَعْبُدُ`
- Response class: relation
- Prompt: tentukan hubungan fungsi antara `إياك` dan `نعبد`.
- Expected: `إياك` berfungsi sebagai objek langsung yang didahulukan terhadap fi'il `نعبد`.
- Critical misconception: posisi awal dianggap selalu subjek nominal.
- Error: E04/E05
- Feature ceiling: tidak menilai balaghah taqdim.
- Ambiguity: LOW
- Status: PILOT

### L13-P05 — Coordination relation
- Target: K34
- Prerequisite: K16
- Reference: QS 112:3
- Target span: `لَمْ يَلِدْ وَلَمْ يُولَدْ`
- Response class: relation
- Prompt: jelaskan relasi lokal dua unit verbal yang dihubungkan `و`.
- Expected: dua unit verbal terkoordinasi dengan `و` sebagai marker 'athaf.
- Critical misconception: hanya mengenali `و` tanpa memahami unit yang dihubungkan.
- Error: E04/E05
- Ambiguity: LOW
- Status: PILOT

### L13-P06 — Demonstrative relation boundary
- Target: K35
- Prerequisite: K24/K25
- Reference: QS 2:2
- Target span: `ذَٰلِكَ الْكِتَابُ`
- Response class: relation/boundary
- Prompt: identifikasi demonstratif dan unsur nominal terkait; jangan memaksakan analisis relasi di atas ceiling K35.
- Expected: `ذلك` = demonstratif; `الكتاب` = unsur nominal terkait pada konstruksi lokal.
- Critical misconception: berhenti pada label demonstratif tanpa menunjukkan relasi lokal atau sebaliknya memasuki analisis lanjutan yang tidak diperlukan.
- Error: E04/E05
- Ambiguity: MEDIUM
- Status: PILOT WITH CEILING NOTE

### L13-P07 — Relative-clause local relation
- Target: K36
- Prerequisite: K26/K27
- Reference: QS 107:1
- Target span: `الَّذِي يُكَذِّبُ`
- Response class: relation
- Prompt: tentukan hubungan lokal isim maushul dengan unit verbal sesudahnya.
- Expected: `الذي` membuka konstruksi relative; `يكذب` berada dalam silah yang melengkapinya pada target lokal.
- Critical misconception: hanya mengklasifikasikan `الذي` tanpa menghubungkannya dengan silah.
- Error: E04/E05
- Ambiguity: LOW
- Status: PILOT

### L13-P08 — Predicate-fronting relation
- Target: K37
- Prerequisite: K09/K12/K31
- Reference: QS 45:36
- Target span: `لِلَّهِ الْحَمْدُ`
- Response class: relation/transfer
- Prompt: tentukan relasi predikatif antara jar-majrur depan dan unsur nominal sesudahnya.
- Expected: `لله` berfungsi predikatif di depan; `الحمد` menjadi unsur nominal yang dipredikasikan pada analisis ceiling L13.
- Critical misconception: mengenali jar-majrur tetapi gagal melihat fungsi predikatifnya.
- Error: E05/E06
- Ambiguity: LOW
- Status: PILOT TRANSFER

### L13-P09 — Multi-local relation prerequisite probe
- Target: K38
- Prerequisite: K31/K32/K33
- Reference: QS 1:5
- Target span: `إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ`
- Response class: prerequisite/integration
- Prompt: petakan dua relasi objek–verba dan relasi koordinasi di antara dua unit tanpa memberi analisis discourse.
- Expected: masing-masing `إياك` berelasi sebagai objek dengan verba lokalnya; `و` mengoordinasikan dua unit.
- Critical misconception: dapat mengenali bentuk tetapi tidak dapat mempertahankan relasi ketika dua unit digabung.
- Error: E05/E08
- Feature ceiling: discourse/rhetorical relation excluded.
- Ambiguity: LOW
- Status: PILOT PREREQUISITE INTEGRATION

### L13-P10 — Conditional local dependency boundary
- Target: K39
- Prerequisite: K29/K30
- Reference: QS 110:1
- Target span: `إِذَا جَاءَ نَصْرُ اللَّهِ`
- Response class: relation/boundary
- Prompt: identifikasi marker pembuka dan unit lokal yang berada dalam domain awalnya; apakah target sudah cukup untuk menganalisis seluruh condition-result relation?
- Expected: `إذا` membuka konstruksi kondisional; unit `جاء نصر الله` berada pada domain awal; span belum cukup untuk menilai keseluruhan condition-result.
- Critical misconception: menyamakan pengenalan marker dengan penguasaan relasi kompleks penuh.
- Error: E05/E07
- Ambiguity: MEDIUM
- Status: PILOT BOUNDARY

### L13-P11 — Transfer subject/object discrimination
- Target: K32/K33
- Prerequisite: K10/K14
- Reference: QS 54:1
- Target span: `اقْتَرَبَتِ السَّاعَةُ`
- Response class: transfer/contrast
- Prompt: tentukan apakah `الساعة` berelasi sebagai subjek verbal atau objek.
- Expected: `الساعة` = fa'il/subjek verbal, bukan objek.
- Critical misconception: posisi pascaverba selalu dianggap maf'ul bih.
- Error: E05/E06/E07
- Ambiguity: LOW
- Status: PILOT TRANSFER CONTRAST

### L13-P12 — Integrative sentence-relation discriminator
- Target: K31–K39 sampled integration
- Prerequisite: K31/K32/K33/K34
- Reference: QS 112:1–3
- Target spans: `هُوَ اللَّهُ أَحَدٌ` / `اللَّهُ الصَّمَدُ` / `لَمْ يَلِدْ وَلَمْ يُولَدْ`
- Response class: integration/discrimination
- Prompt: dari tiga span, tunjukkan satu relasi predikatif nominal, satu relasi verbal yang dapat dianalisis pada ceiling L13, dan satu koordinasi; jangan menggunakan terjemahan sebagai bukti utama.
- Expected: peserta menunjukkan relasi nominal yang sah dari span 1/2, mengidentifikasi struktur verbal lokal pada span 3, dan `و` sebagai penghubung koordinatif dua unit verbal.
- Critical misconception: menyebut kategori kata tanpa relasi atau menjawab berdasarkan hafalan makna.
- Error: E01/E05/E08
- Feature ceiling: no K40+ complex-clause/discourse analysis.
- Ambiguity: MEDIUM; rubric tersegmentasi wajib.
- Status: PILOT INTEGRATIVE WITH CEILING NOTE

## 4. Batch-01 distribution audit

Pool size: **12/36 = 33.33%**.

Coverage awal:
- K31 nominal predication: P01/P02/P12
- K32 verbal subject: P03/P11
- K33 object relation: P04/P09/P11
- K34 coordination: P05/P09/P12
- K35 demonstrative relation: P06
- K36 relative relation: P07
- K37 fronted predicate: P08
- K38 multi-local integration: P09
- K39 conditional boundary: P10

Functional classes already present: direct relation, negative/contrast, prerequisite, transfer, boundary, integrative.

## 5. Expansion priorities P13–P24

1. independent evidence for K35–K39;
2. adjective/possessive/local dependency contrasts where they belong to the canonical K31–K39 definitions;
3. prerequisite probes capable of routing failures back toward L11/L12;
4. transfer across surahs and different surface orders;
5. explicit contrast between morphological recognition and true relation identification;
6. HOLD any item whose correct answer requires K40+ complex-clause integration.

## 6. Working six-item assembly gate

A selected L13 checkpoint form must include:
- >=4 distinct primary K;
- >=1 prerequisite probe;
- >=1 contrast/negative control;
- >=1 transfer item;
- >=1 integrative relation item;
- >=1 item requiring an explicit relation, not merely category recognition.

Failure on prerequisite or relation-integrity opens local diagnosis within L11–L13 rather than resetting to L01.

## 7. Governance

Research layer only. No production freeze. Promotion requires Arabic-content review, item-quality review, pilot evidence, cut-score validation, and RIQA OS mapping.
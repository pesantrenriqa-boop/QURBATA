# Placement Pilot L10 — Batch 01 v1.0

**Status:** WORKING RESEARCH — NON-AUTHORITATIVE  
**Branch:** `agent/quranic-arabic-competency-ladder`  
**Scope:** adaptive placement checkpoint L10  
**Competency band:** K13–K30  
**Guardrail:** item hanya boleh menuntut operasi sampai checkpoint L10. Struktur Stage 3+ boleh tampak pada ayat hanya jika tidak diperlukan untuk memperoleh jawaban benar; jika tidak, item harus HOLD/PREMATURE.

## 1. Tujuan

Membuka verse-level pilot bank L10 setelah pool L04 mencapai 36/36. L10 menguji controlled morphosyntax: relasi bentuk–fungsi yang lebih kaya daripada L04, tetapi belum mengandalkan sentence-relation reasoning Stage 3.

## 2. Item schema

Setiap item menyimpan: Item ID; target K; prerequisite K; Qur'anic reference; target span; response class; prompt; expected response; scoring key; critical misconception; error code; feature ceiling; ambiguity; review status.

## 3. Pilot items P01–P12

### L10-P01 — Direct morphology recognition
- Target: K13
- Reference: QS 1:5
- Target span: `نَعْبُدُ`
- Response class: classification
- Prompt: klasifikasikan bentuk verbal target pada batas operasi L10.
- Expected: fi'il mudhari' dengan subjek yang ditandai dalam bentuk verbal; tidak meminta analisis clause lanjutan.
- Critical misconception: mengandalkan terjemahan waktu tanpa membaca bentuk.
- Error: E02/E03
- Ambiguity: LOW
- Status: PILOT

### L10-P02 — Object recognition
- Target: K14
- Prerequisite: K06/K10/K13
- Reference: QS 1:5
- Target span: `إِيَّاكَ نَعْبُدُ`
- Response class: relation
- Prompt: identifikasi unsur yang berfungsi sebagai objek langsung pada span.
- Expected: `إياك` sebagai objek langsung yang didahulukan.
- Critical misconception: menganggap unsur pertama otomatis mubtada'.
- Error: E04/E05
- Feature ceiling: tidak meminta analisis balaghah taqdim.
- Ambiguity: LOW
- Status: PILOT

### L10-P03 — Negative control object vs subject
- Target: K14
- Prerequisite: K10
- Reference: QS 17:81
- Target span: `جَاءَ الْحَقُّ`
- Response class: negative control
- Prompt: apakah `الحق` merupakan maf'ul bih?
- Expected: tidak; pada span ini `الحق` adalah fa'il zhahir.
- Critical misconception: semua isim setelah fi'il dianggap objek.
- Error: E04/E07
- Ambiguity: LOW
- Status: PILOT NEGATIVE CONTROL

### L10-P04 — Coordination recognition
- Target: K16
- Reference: QS 2:2
- Target span: `هُدًى لِّلْمُتَّقِينَ`
- Response class: boundary
- Prompt: apakah target ini merupakan koordinasi dengan huruf 'athaf?
- Expected: tidak; tidak ada huruf 'athaf pada span.
- Critical misconception: menganggap dua unit berurutan selalu terkoordinasi.
- Error: E03/E07
- Ambiguity: LOW
- Status: PILOT NEGATIVE CONTROL

### L10-P05 — Direct coordination
- Target: K16
- Reference: QS 112:3
- Target span: `لَمْ يَلِدْ وَلَمْ يُولَدْ`
- Response class: relation/classification
- Prompt: tunjukkan marker koordinasi yang menghubungkan dua unit verbal.
- Expected: `وَ` sebagai huruf 'athaf/koordinasi.
- Critical misconception: fokus pada `لم` dan mengabaikan penghubung.
- Error: E02/E04
- Feature ceiling: tidak meminta analisis penuh jazm sebagai target utama.
- Ambiguity: LOW
- Status: PILOT WITH CEILING NOTE

### L10-P06 — Direct demonstrative recognition
- Target: K24
- Reference: QS 2:2
- Target span: `ذَٰلِكَ الْكِتَابُ`
- Response class: recognition/relation-lite
- Prompt: identifikasi isim isyarah dan unsur nominal yang ditunjuk pada span minimal.
- Expected: `ذلك` = isim isyarah; `الكتاب` = unsur nominal terkait pada span.
- Critical misconception: hanya menerjemahkan `itu` tanpa klasifikasi bentuk.
- Error: E01/E04
- Ambiguity: MEDIUM — scoring tidak meminta analisis badal/apposition lanjutan.
- Status: PILOT WITH CEILING NOTE

### L10-P07 — Contrast demonstrative vs relative pronoun
- Target: K24
- Reference: QS 1:7
- Target span: `الَّذِينَ`
- Response class: negative control/contrast
- Prompt: apakah target merupakan isim isyarah?
- Expected: tidak; target adalah isim maushul, bukan demonstratif.
- Critical misconception: menyamakan semua closed-class nominal forms.
- Error: E02/E07
- Feature ceiling: tidak meminta analisis relative clause.
- Ambiguity: LOW
- Status: PILOT NEGATIVE CONTROL

### L10-P08 — Relative-pronoun recognition
- Target: K26
- Reference: QS 1:7
- Target span: `الَّذِينَ أَنْعَمْتَ`
- Response class: recognition/relation-lite
- Prompt: identifikasi isim maushul pada span dan batas awal silahnya tanpa menganalisis dependency lanjutan.
- Expected: `الذين` = isim maushul; `أنعمت` memulai silah pada span.
- Critical misconception: menganggap `الذين` sebagai demonstratif atau artikel + isim biasa.
- Error: E02/E04
- Ambiguity: LOW
- Status: PILOT

### L10-P09 — Transfer relative-pronoun recognition
- Target: K26
- Reference: QS 107:1
- Target span: `الَّذِي يُكَذِّبُ`
- Response class: transfer
- Prompt: terapkan pengenalan isim maushul pada contoh baru.
- Expected: `الذي` = isim maushul; `يكذب` bagian awal silah pada ceiling L10.
- Critical misconception: transfer gagal ketika bentuk berubah dari plural ke singular.
- Error: E06
- Ambiguity: LOW
- Status: PILOT TRANSFER

### L10-P10 — Conditional marker boundary
- Target: K29/K30 boundary
- Reference: QS 110:1
- Target span: `إِذَا جَاءَ نَصْرُ اللَّهِ`
- Response class: recognition/boundary
- Prompt: identifikasi marker pembuka konstruksi kondisional tanpa meminta analisis jawab syarat lengkap.
- Expected: `إذا` dikenali sebagai marker kondisional/temporal conditional pada ceiling L10.
- Critical misconception: menganggap `إذا` sekadar adverb waktu tanpa fungsi penghubung struktur.
- Error: E02/E04
- Ambiguity: MEDIUM
- Status: PILOT WITH CEILING NOTE

### L10-P11 — Integrative morphology + relation
- Target: K13/K14/K16
- Reference: QS 1:5
- Target span: `إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ`
- Response class: integration
- Prompt: identifikasi dua objek yang didahulukan, dua fi'il mudhari', dan marker koordinasi di antara dua unit.
- Expected: `إياك` pada masing-masing unit sebagai objek; `نعبد/نستعين` sebagai fi'il mudhari'; `و` sebagai penghubung koordinatif.
- Critical misconception: peserta mampu mengenali bentuk satuan tetapi gagal mengintegrasikan fungsi lokal.
- Error: E03/E04/E05
- Feature ceiling: tidak meminta analisis retorika pengulangan atau discourse relation.
- Ambiguity: LOW
- Status: PILOT INTEGRATIVE

### L10-P12 — Integrative demonstrative/nominal boundary
- Target: K24 + prerequisite nominal operations
- Reference: QS 3:58
- Target span: `ذَٰلِكَ نَتْلُوهُ`
- Response class: integration/transfer
- Prompt: identifikasi isim isyarah dan klasifikasikan bentuk verbal sesudahnya tanpa memaksa analisis sentence relation Stage 3.
- Expected: `ذلك` = isim isyarah; `نتلوه` = bentuk verbal; hubungan penuh antarunit tidak menjadi target scoring.
- Critical misconception: mencoba menyelesaikan item melalui terjemahan keseluruhan atau analisis wacana.
- Error: E02/E06
- Ambiguity: MEDIUM
- Status: PILOT INTEGRATIVE WITH CEILING NOTE

## 4. Batch-01 distribution audit

Pool size: **12/36 = 33.33%**.

Coverage sementara:
- direct/classification: P01, P02, P05, P06, P08
- negative/contrast: P03, P04, P07
- transfer: P09, P12
- boundary/prerequisite: P06, P10
- integrative: P11, P12

Current coverage is intentionally incomplete. K13–K30 must not be represented only by a handful of salient structures.

## 5. Expansion priorities P13–P24

1. tambah direct items untuk kompetensi K15, K17–K23, K25, K27–K30;
2. tambah negative controls yang membedakan surface similarity dari target relation;
3. tambah prerequisite probes agar failure dapat dirouting ke L05–L09 secara lokal;
4. tambah transfer dari surah berbeda;
5. audit setiap occurrence yang memerlukan Stage 3 relation dan tandai PREMATURE bila operasi itu wajib untuk menjawab.

## 6. Working routing gate

Untuk pilot nanti, selected six dari pool L10 harus memuat:
- minimal 4 target K berbeda;
- 1 prerequisite integrity probe;
- 1 contrast/negative control;
- 1 transfer item;
- 1 integrative item.

Mastery sementara tetap bukan skor mentah saja. Kegagalan prerequisite atau transfer membuka diagnosis lokal L05–L10.

## 7. Governance

Dokumen berada di research layer PR #4. Tidak mengubah registry produksi. Production freeze membutuhkan Arabic-content review, item-quality review, pilot data, dan mapping RIQA OS.
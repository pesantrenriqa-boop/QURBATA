# QCI MAPPER RULES V1

Tanggal: 4 Agustus 2026
Status: DRAFT IMPLEMENTABLE

## 1. Tujuan

QCI Mapper membaca setiap `LEXEME_ENTRY` dan menghasilkan profil kompetensi baca yang terukur. Mapper tidak menentukan kelayakan pedagogis akhir; ia hanya mendeteksi fitur secara konsisten dan dapat diaudit.

## 2. Input

Input minimum:
- `LexemeID`
- `PrimaryUthmaniForm`
- `UthmaniVariants`
- `SearchForm`
- `SourceRefs`
- `OccurrenceCount`

## 3. Output utama

Setiap hasil mapper memiliki:
- `MappingID`
- `LexemeID`
- `DetectedFeatures`
- `CandidatePrimaryCompetencies`
- `SecondaryCompetencies`
- `RequiredCompetencies`
- `VisualLetterFamilies`
- `ConnectionPattern`
- `ComplexitySignals`
- `RuleTrace`
- `ConfidenceScore`
- `ReviewFlags`
- `MapperVersion`

## 4. Kelompok deteksi V1

### A. Harakat
- fathah
- kasrah
- dhammah
- tanwin fathah
- tanwin kasrah
- tanwin dhammah

### B. Pemanjangan
- mad fathah + alif
- mad kasrah + ya sukun
- mad dhammah + wawu sukun
- alif maqshurah

### C. Sukun dan tasydid
- sukun dasar
- sukun hamzah
- sukun ain
- sukun ghain
- sukun huruf tebal
- tasydid

### D. Struktur visual
- jumlah huruf dasar
- jumlah cluster grafem
- bentuk awal
- bentuk tengah
- bentuk akhir
- huruf non-connector
- transisi sesudah non-connector
- ta marbuthah
- hamzah qatha
- alif lam

### E. Keluarga huruf
Mapper memberi label keluarga visual berdasarkan kemiripan bentuk, bukan nama huruf semata. Daftar keluarga harus mengacu pada MASTER_QCI resmi dan tidak boleh dibuat bebas oleh generator.

## 5. Aturan kompetensi utama

Mapper dapat menghasilkan lebih dari satu kandidat kompetensi utama, tetapi belum memilih final secara mutlak.

Prioritas awal:
1. fitur baru paling dominan;
2. fitur yang paling menentukan keterbacaan;
3. fitur dengan dependency terdalam;
4. fitur yang paling jarang terwakili dalam bank aktif;
5. fitur visual sebagai tie-breaker.

Pemilihan akhir dilakukan oleh generator berdasarkan target level dan whitelist kompetensi.

## 6. RequiredCompetencies

`RequiredCompetencies` diturunkan dari seluruh fitur yang harus sudah dikuasai sebelum kata dapat digunakan.

Contoh prinsip:
- kata dengan tasydid juga membutuhkan penguasaan huruf dan harakat terkait;
- kata dengan mad ya membutuhkan kasrah sebelum ya sukun;
- kata dengan sambungan setelah ra membutuhkan kompetensi transisi non-connector;
- kata dengan alif lam tidak otomatis dianggap satu kompetensi tunggal apabila mengandung fitur lain yang lebih berat.

## 7. ConnectionPattern

Format ringkas:
- `FULLY_CONNECTED`
- `START_BREAK`
- `MIDDLE_BREAK`
- `MULTI_BREAK`
- `NON_CONNECTING_FINAL`
- `SINGLE_CLUSTER`

Field tambahan:
- `BreakPositions`
- `NonConnectorLetters`
- `JoinCount`

## 8. ConfidenceScore

Skala 0.00-1.00.

- `>= 0.95`: dapat masuk antrean generator otomatis;
- `0.80-0.94`: generator boleh membuat kandidat dengan flag review;
- `< 0.80`: tidak boleh digenerasikan otomatis.

Confidence tidak menggantikan verifikasi sumber dan review pedagogis.

## 9. ReviewFlags

Flag minimum:
- `UNICODE_ANOMALY`
- `ORTHOGRAPHIC_VARIANT`
- `AMBIGUOUS_MAD`
- `AMBIGUOUS_HAMZAH`
- `MIXED_PRIMARY_FEATURES`
- `RARE_CONNECTION_PATTERN`
- `QCI_NOT_FOUND`
- `DEPENDENCY_CONFLICT`

## 10. RuleTrace

Setiap label wajib mempunyai jejak aturan:
- `RuleID`
- `InputSegment`
- `DetectedFeature`
- `StartIndex`
- `EndIndex`
- `Evidence`

Tidak boleh ada kompetensi hasil mapper yang tidak dapat dijelaskan oleh `RuleTrace`.

## 11. Gate kelulusan mapper

Lexeme berstatus `MAPPED` apabila:
- semua grafem dapat dibaca mapper;
- minimal satu kandidat kompetensi terdeteksi;
- dependency ditemukan di MASTER_QCI;
- tidak ada konflik fatal;
- versi aturan tercatat.

Lexeme berstatus `REVIEW_REQUIRED` apabila memiliki flag ambigu. Lexeme berstatus `BLOCKED` apabila sumber atau struktur Unicode tidak dapat dipastikan.

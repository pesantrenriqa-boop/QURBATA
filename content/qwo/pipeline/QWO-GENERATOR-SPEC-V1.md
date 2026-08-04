# QWO GENERATOR SPEC V1

Tanggal: 4 Agustus 2026
Status: DRAFT IMPLEMENTABLE

## 1. Tujuan

QWO Generator mengubah hasil MASTER_LEXICON dan QCI Mapper menjadi kandidat QWO yang konsisten, dapat dilacak, dan siap melewati gate validasi. Generator tidak boleh langsung mengaktifkan objek.

## 2. Pipeline resmi

`MASTER_LEXICON -> QCI_MAPPER -> QWO_GENERATOR -> SOURCE_VERIFIED -> QCI_MAPPED -> PEDAGOGY_REVIEWED -> ACTIVE`

Status awal seluruh keluaran generator adalah `CANDIDATE`.

## 3. Input

Input wajib:
- lexeme berstatus `APPROVED_FOR_GENERATION`;
- hasil mapper dengan `ConfidenceScore >= 0.80`;
- referensi MASTER_QCI;
- dependency graph QCI;
- whitelist kompetensi per level;
- aturan distribusi dan kuota produksi.

## 4. Struktur QWO V1

Field minimum:
- `QWOID`
- `ArabicWord`
- `NormalizedWord`
- `LexemeID`
- `SourceRefs`
- `OccurrenceCount`
- `TargetCompetency`
- `SecondaryCompetencies`
- `RequiredCompetencies`
- `VisualLetterFamilies`
- `ConnectionPattern`
- `DifficultySignals`
- `SuggestedLevelRange`
- `GenerationReason`
- `RuleTraceRef`
- `SourceStatus`
- `QCIStatus`
- `PedagogyStatus`
- `LifecycleStatus`
- `GeneratorVersion`
- `GeneratedAt`

## 5. Pemilihan TargetCompetency

Generator memilih satu `TargetCompetency` berdasarkan:
1. kompetensi masuk whitelist level;
2. seluruh dependency tersedia pada level sebelumnya atau sesi sebelumnya;
3. fitur tersebut dominan menurut mapper;
4. kebutuhan distribusi bank QWO;
5. tidak terjadi konflik dengan batas kompleksitas;
6. keputusan dapat dijelaskan dalam `GenerationReason`.

Fitur lain masuk `SecondaryCompetencies`.

## 6. Penentuan level

Generator hanya memberi `SuggestedLevelRange`, bukan level final.

Level saran dihitung dari:
- dependency terdalam;
- jumlah huruf dan cluster;
- pola sambungan;
- jumlah fitur aktif;
- keberadaan mad, sukun, tanwin, atau tasydid;
- keluarga visual;
- frekuensi kemunculan;
- kebijakan tangga materi QURBATA.

## 7. Filter otomatis

Objek tidak dibuat apabila:
- SourceRefs kosong;
- lexeme belum terverifikasi;
- mapper gagal;
- QCI tidak ditemukan;
- dependency conflict;
- kata melampaui whitelist seluruh level target;
- bentuk sama sudah memiliki QWO ekuivalen tanpa alasan varian;
- confidence di bawah 0.80.

## 8. Deduplikasi

Deduplikasi dilakukan pada tiga tingkat:
- `EXACT_UTHMANI`: bentuk Utsmani identik;
- `CANONICAL_EQUIVALENT`: canonical key sama;
- `PEDAGOGICAL_EQUIVALENT`: fitur dan target kompetensi sama.

Varian boleh dipertahankan apabila:
- memiliki bentuk Utsmani berbeda yang relevan;
- memiliki pola sambungan berbeda;
- memiliki target kompetensi berbeda yang sah;
- diperlukan untuk distribusi pedagogis.

Setiap varian wajib memiliki `GenerationReason`.

## 9. Mode produksi

### A. Full Corpus Build
Menghasilkan seluruh kandidat yang memenuhi syarat dari corpus.

### B. Level Targeted Build
Menghasilkan kandidat untuk level atau kompetensi tertentu.

### C. Gap Fill Build
Mengisi kekurangan distribusi berdasarkan laporan coverage.

### D. Rebuild
Menghasilkan ulang kandidat setelah versi mapper, QCI, atau whitelist berubah.

## 10. Output laporan

Setiap run menghasilkan:
- `RUN_MANIFEST`;
- jumlah lexeme dibaca;
- jumlah kandidat dibuat;
- jumlah ditolak dan alasannya;
- distribusi per kompetensi;
- distribusi per level saran;
- daftar duplikasi;
- daftar review flags;
- versi corpus, mapper, QCI, dan generator;
- checksum output.

## 11. Identitas dan reproducibility

`QWOID` harus stabil untuk input dan versi aturan yang sama.

Run wajib mencatat:
- `CorpusVersion`
- `CorpusChecksum`
- `MapperVersion`
- `QCIVersion`
- `GeneratorVersion`
- `WhitelistVersion`

Perubahan versi tidak boleh menimpa hasil lama tanpa audit trail.

## 12. Gate aktivasi

Generator hanya menghasilkan `CANDIDATE`.

Promosi mengikuti urutan:
1. `CANDIDATE`
2. `SOURCE_VERIFIED`
3. `QCI_MAPPED`
4. `PEDAGOGY_REVIEWED`
5. `ACTIVE`

Tidak ada jalur pintas menuju `ACTIVE`.

## 13. Definition of Done V1

V1 selesai apabila:
- schema MASTER_LEXICON tersedia;
- minimal satu corpus sumber dapat diimpor;
- mapper mendeteksi seluruh fitur V1;
- generator menghasilkan kandidat deterministik;
- laporan coverage dan rejection tersedia;
- 100 sampel lolos audit manual tanpa kesalahan kritis;
- proses dapat dijalankan ulang dengan hasil yang sama.

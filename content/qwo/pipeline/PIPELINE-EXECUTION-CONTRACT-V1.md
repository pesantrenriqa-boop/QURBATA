# QWO Pipeline Execution Contract V1

Tanggal: 4 Agustus 2026
Status: ACTIVE FOUNDATION CONTRACT

## 1. Tujuan

Dokumen ini mengikat urutan eksekusi pipeline QWO agar data corpus, hasil analisis teknis, dan keputusan pedagogis tidak tercampur.

## 2. Urutan eksekusi wajib

1. `IMPORT_CORPUS`
2. `VALIDATE_OCCURRENCES`
3. `BUILD_LEXEMES`
4. `RUN_QCI_MAPPER`
5. `BUILD_REVIEW_QUEUE`
6. `GENERATE_QWO_CANDIDATES`
7. `SOURCE_VERIFICATION`
8. `QCI_REVIEW`
9. `PEDAGOGY_REVIEW`
10. `ACTIVATE_APPROVED_QWO`

Tahap tidak boleh dilompati.

## 3. Kontrak input corpus

Input minimum setiap token:

- SurahNumber;
- AyahNumber;
- TokenIndex;
- UthmaniToken;
- SourceEdition;
- SourceChecksum.

Impor ditolak apabila:

- referensi ayat tidak valid;
- token kosong;
- kombinasi surah, ayat, dan indeks duplikat;
- edisi sumber tidak disebutkan;
- checksum corpus tidak tersedia.

## 4. Kontrak normalisasi

Normalisasi wajib:

- mempertahankan UthmaniToken asli;
- menghasilkan SearchToken secara deterministik;
- menghasilkan CanonicalKey secara deterministik;
- mencatat versi normalizer;
- mencatat kegagalan tanpa menghapus token sumber.

Normalizer dilarang:

- mengganti bentuk asli;
- menyamakan dua token hanya berdasarkan dugaan morfologi;
- menetapkan level QURBATA;
- menetapkan kompetensi utama.

## 5. Kontrak mapper

Setiap hasil mapper wajib berisi:

- MapperVersion;
- detected features;
- RuleTrace;
- ConfidenceScore;
- ReviewFlag;
- RequiredCompetencies;
- SecondaryCompetencies.

Hasil mapper dengan konflik aturan atau confidence di bawah ambang masuk `REVIEW_REQUIRED`.

## 6. Kontrak generator

Generator hanya menerima lexeme dengan status:

`APPROVED_FOR_GENERATION`

Generator wajib:

- menggunakan whitelist kompetensi;
- menghasilkan QWO_ID deterministik;
- menautkan seluruh SourceRefs;
- menyimpan versi mapper dan generator;
- menghasilkan checksum output;
- menjalankan deduplikasi;
- menetapkan status awal `CANDIDATE`.

Generator dilarang:

- membuat kata yang tidak ada dalam corpus;
- mengubah UthmaniToken;
- menaikkan status langsung menjadi ACTIVE;
- menghapus objek gagal tanpa laporan;
- memilih level hanya berdasarkan frekuensi kata.

## 7. Gate aktivasi

QWO hanya dapat menjadi ACTIVE apabila:

1. occurrence sumber terverifikasi;
2. SourceRef lengkap;
3. TargetCompetency valid;
4. dependency QCI lengkap;
5. SecondaryCompetencies tercatat;
6. tidak melampaui whitelist level;
7. tidak merupakan duplikasi aktif;
8. lolos review pedagogis;
9. memiliki audit trail reviewer;
10. checksum objek final tercatat.

## 8. Artefak keluaran setiap run

Setiap run wajib menghasilkan:

- RunID;
- waktu proses;
- versi input corpus;
- versi normalizer;
- versi mapper;
- versi generator;
- jumlah token masuk;
- jumlah token valid dan gagal;
- jumlah lexeme unik;
- jumlah review required;
- jumlah kandidat QWO;
- jumlah duplikasi ditahan;
- checksum output;
- error log.

## 9. Strategi subset pertama

Implementasi tidak langsung memproses seluruh corpus. Tahap pertama menggunakan subset terverifikasi untuk menguji:

- kestabilan Unicode;
- indeks token;
- normalisasi;
- RuleTrace;
- deduplikasi;
- determinisme ID;
- reproduksibilitas checksum.

Subset pertama bukan dasar urutan pedagogis dan bukan berarti surah-first. Ia hanya corpus pengujian teknis.

## 10. Kriteria promosi ke produksi penuh

Pipeline dapat diperluas ke seluruh corpus apabila:

- dua run berulang menghasilkan output dan checksum identik;
- tidak ada kehilangan UthmaniToken;
- seluruh error dapat ditelusuri;
- mapper memiliki review queue yang jelas;
- generator tidak menghasilkan objek tanpa SourceRef;
- reviewer menyetujui struktur audit.

# MASTER LEXICON SPEC V1

Tanggal: 4 Agustus 2026
Status: DRAFT IMPLEMENTABLE

## 1. Tujuan

MASTER_LEXICON adalah corpus induk seluruh token kata Al-Qur'an yang menjadi sumber tunggal produksi QWO. Sistem tidak lagi menambah kandidat kata secara manual sebagai jalur utama.

MASTER_LEXICON bertugas:
- menyimpan bentuk kata persis sebagaimana sumber mushaf;
- menyediakan bentuk normalisasi untuk pencarian dan deduplikasi;
- menyimpan seluruh lokasi kemunculan kata;
- memisahkan data tekstual dari keputusan pedagogis;
- menyediakan input deterministik bagi QCI Mapper dan QWO Generator.

## 2. Prinsip

1. Teks mushaf adalah sumber kebenaran utama.
2. Bentuk Utsmani tidak boleh ditimpa oleh hasil normalisasi.
3. Normalisasi hanya digunakan untuk pencarian, pengelompokan, dan analisis.
4. Satu bentuk normalisasi dapat memiliki beberapa bentuk Utsmani.
5. Setiap token harus dapat ditelusuri kembali ke surah, ayat, dan posisi token.
6. Lexicon tidak menentukan level buku secara langsung.
7. Data yang belum terverifikasi tidak boleh menghasilkan QWO ACTIVE.

## 3. Unit data

MASTER_LEXICON memiliki dua lapisan:

### A. TOKEN_OCCURRENCE

Satu baris untuk setiap kemunculan token di dalam mushaf.

Field wajib:
- `OccurrenceID`
- `SurahNumber`
- `AyahNumber`
- `TokenIndex`
- `UthmaniToken`
- `SearchToken`
- `CanonicalKey`
- `SourceEdition`
- `SourceChecksum`
- `VerificationStatus`

### B. LEXEME_ENTRY

Satu objek agregat untuk token yang memiliki `CanonicalKey` sama.

Field wajib:
- `LexemeID`
- `CanonicalKey`
- `PrimaryUthmaniForm`
- `UthmaniVariants`
- `SearchForm`
- `OccurrenceCount`
- `SourceRefs`
- `MapperStatus`
- `ReviewPriority`

## 4. Aturan normalisasi

Normalisasi harus bersifat lossless pada tingkat arsip: bentuk asli selalu disimpan.

`SearchToken` dapat:
- menghapus tanda waqaf dan simbol non-huruf yang disepakati;
- menyatukan representasi Unicode ekuivalen;
- mempertahankan huruf dasar;
- mempertahankan informasi harakat pada field analisis terpisah;
- tidak mengubah bentuk asli `UthmaniToken`.

`CanonicalKey` digunakan untuk deduplikasi teknis, bukan untuk menyatakan dua kata selalu identik secara morfologis atau pedagogis.

## 5. Status verifikasi

Status TOKEN_OCCURRENCE:
- `IMPORTED`
- `SOURCE_VERIFIED`
- `SOURCE_REJECTED`

Status LEXEME_ENTRY:
- `UNMAPPED`
- `MAPPED`
- `REVIEW_REQUIRED`
- `APPROVED_FOR_GENERATION`
- `BLOCKED`

## 6. Validasi minimum

Setiap occurrence harus memenuhi:
- nomor surah valid;
- nomor ayat valid;
- indeks token unik dalam ayat;
- token Utsmani tidak kosong;
- referensi sumber tersedia;
- checksum sumber tercatat;
- tidak ada duplikasi `SurahNumber + AyahNumber + TokenIndex`.

## 7. Output

MASTER_LEXICON menghasilkan:
- daftar occurrence terverifikasi;
- daftar lexeme unik;
- distribusi frekuensi;
- antrean mapper;
- laporan token gagal normalisasi;
- laporan varian Utsmani;
- checksum corpus.

## 8. Batasan V1

V1 belum memutuskan:
- akar kata;
- wazan;
- i'rab;
- makna;
- level QURBATA;
- kompetensi utama.

Semua keputusan tersebut berada di lapisan berikutnya agar corpus tetap netral dan dapat diaudit.

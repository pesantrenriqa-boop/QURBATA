# QWO Production Status V2

Tanggal pembaruan: 4 Agustus 2026
Branch: `content/qurbata-jilid-1-8-production`
Status: PIPELINE FOUNDATION ACTIVE

## Keputusan strategis

Produksi kandidat QWO manual dihentikan sebagai jalur utama. Produksi berikutnya menggunakan pipeline corpus-driven:

`MASTER_LEXICON -> QCI_MAPPER -> QWO_GENERATOR -> CANDIDATE -> SOURCE_VERIFIED -> QCI_MAPPED -> PEDAGOGY_REVIEWED -> ACTIVE`

## Aset yang sudah tersedia

- Candidate pool lama: 210 objek pada riwayat produksi sebelumnya.
- MASTER Lexicon Specification V1.
- QCI Mapper Rules V1.
- QWO Generator Specification V1.

## Status candidate pool lama

Candidate pool A-001 dan A-002 tidak dihapus, tetapi dipindahkan fungsi menjadi:

- sampel audit mapper;
- data uji regresi;
- pembanding hasil generator;
- sumber kandidat manual cadangan;
- bukan sumber kebenaran utama corpus.

Tidak ada kandidat lama yang otomatis menjadi ACTIVE.

## Sprint aktif

### Sprint P1 — Corpus Foundation

Target:

1. menetapkan format input corpus;
2. membuat tabel TOKEN_OCCURRENCE;
3. membuat tabel LEXEME_ENTRY;
4. menetapkan checksum dan source edition;
5. menguji impor pada subset terbatas;
6. menghasilkan laporan token gagal normalisasi.

Gate kelulusan:

- setiap token memiliki SourceRef;
- indeks token unik per ayat;
- UthmaniToken asli tetap tersimpan;
- SearchToken dan CanonicalKey dapat direproduksi;
- tidak ada aktivasi QWO otomatis.

### Sprint P2 — Mapper Foundation

Target:

1. menjalankan aturan deteksi harakat;
2. mendeteksi mad, tanwin, sukun, tasydid, alif lam, hamzah, ta marbuthah;
3. menyimpan RuleTrace;
4. menyimpan confidence score;
5. membuat antrean REVIEW_REQUIRED.

### Sprint P3 — Generator Foundation

Target:

1. menghasilkan QWO_ID deterministik;
2. deduplikasi bentuk, sumber, dan kompetensi;
3. menghasilkan kandidat berdasarkan whitelist kompetensi;
4. menghasilkan laporan distribusi;
5. menahan semua objek pada status CANDIDATE sampai lolos gate.

## Prinsip kualitas

1. Teks mushaf adalah sumber kebenaran.
2. Bentuk Utsmani tidak boleh ditimpa normalisasi.
3. Semua hasil mapper harus dapat diaudit melalui RuleTrace.
4. Semua QWO harus dapat ditelusuri ke occurrence sumber.
5. Generator tidak boleh menaikkan status menjadi ACTIVE.
6. Keputusan pedagogis tetap membutuhkan review manusia.

## Definisi selesai tahap fondasi

Tahap fondasi dianggap selesai apabila:

- skema data disepakati;
- subset corpus berhasil diimpor;
- mapper menghasilkan label yang dapat diaudit;
- generator menghasilkan objek deterministik;
- hasil pengulangan dengan input dan versi aturan sama menghasilkan checksum sama;
- laporan error dan review queue tersedia.

## Target berikutnya

Membangun implementasi awal berbasis subset corpus terverifikasi sebelum memperluas ke seluruh Al-Qur'an.

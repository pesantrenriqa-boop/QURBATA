# Quranic Arabic Competency Ladder — Working Research Layer

**Status:** WORKING DRAFT — NON-AUTHORITATIVE  
**Branch:** `agent/quranic-arabic-competency-ladder`  
**Repository:** `pesantrenriqa-boop/QURBATA`  
**Purpose:** menemukan urutan kompetensi Bahasa Arab Qurani dari yang paling elementer sampai paling kompleks berdasarkan struktur nyata Al-Qur'an.

## 1. Kedudukan Dokumen

Dokumen ini bukan sumber kebenaran baru dan tidak mengganti `QURBATA-BASELINE.md`, ACP, QCF, DEC-CUR, atau registry resmi.

Seluruh hasil penelitian pada folder ini bersifat kandidat. Setelah lolos validasi akademik dan tata kelola, hasil yang diterima harus dipetakan atau diturunkan ke struktur resmi yang sudah ada, terutama:

- `curriculum/REG-ARB-001-Register-Objek-Kompetensi-Bahasa-Arab.md`;
- `curriculum/REG-ARB-002-Master-Contoh-Kalimat.md`;
- registry Source-ID Qurani yang relevan;
- matriks keterlacakan resmi QURBATA.

Tidak dibuat sistem kode kompetensi permanen baru di folder penelitian ini.

## 2. Tujuan Penelitian

Menemukan urutan kompetensi linguistik Qurani:

`K1 → K2 → K3 → ... → Kn`

berdasarkan hubungan prasyarat, kompleksitas linguistik, keterulangan/frekuensi dalam Al-Qur'an, dan ketersediaan contoh Qurani yang dapat digunakan secara kumulatif.

Jumlah akhir kompetensi tidak dipaksakan menjadi 20. Jumlah `Kn` ditentukan oleh hasil analisis. Slot `AR-STG-001–020` pada registry yang sudah ada diperlakukan sebagai struktur tahap yang dapat dipetakan kemudian, bukan pembatas jumlah temuan kompetensi.

## 3. Aturan Kumulatif Inti

Untuk kompetensi `Kn`, contoh Qurani yang digunakan pada tahap tersebut hanya boleh mengandung:

`{K1, K2, ..., Kn}`

Contoh yang membutuhkan kompetensi `K(n+1)` atau lebih tinggi dinyatakan **PREMATURE** untuk tahap `Kn`, walaupun contoh tersebut benar secara gramatikal dan mengandung target `Kn`.

Secara operasional:

- **TARGET:** `Kn`;
- **ALLOWED:** `K1...Kn`;
- **FORBIDDEN:** semua kompetensi yang belum dipelajari;
- **PASS:** target ada dan seluruh struktur lain sudah termasuk `ALLOWED`;
- **REJECT-PREMATURE:** terdapat minimal satu kompetensi di atas `Kn`.

## 4. Unit Contoh Qurani

Contoh tidak harus selalu berupa satu ayat penuh. Unit yang dapat digunakan:

1. kata Qurani;
2. frasa Qurani;
3. klausa Qurani;
4. ayat penuh.

Unit harus merupakan potongan yang sah dari mushaf, utuh secara linguistik untuk menunjukkan target, memiliki referensi surah:ayat, dan tidak mengubah susunan lafaz Al-Qur'an.

## 5. Corpus Bank dan Teaching Set

Jumlah contoh per kompetensi tidak dibatasi lima.

### Corpus Bank

Menyimpan sebanyak mungkin contoh Qurani yang lolos cumulative-filter.

### Teaching Set

Dipilih kemudian dari Corpus Bank. Jumlah dapat 20–30 atau lebih sesuai kebutuhan pedagogis. Pemilihan Teaching Set bukan bagian dari fase penemuan tangga saat ini.

## 6. Prinsip Penyusunan Urutan

Urutan kompetensi tidak ditetapkan hanya berdasarkan susunan kitab nahwu klasik atau intuisi pengembang.

Setiap kandidat diperiksa melalui minimal empat dimensi:

1. **dependency/prasyarat** — kompetensi apa yang wajib dipahami lebih dahulu;
2. **kompleksitas linguistik** — jumlah dan kedalaman relasi morfologis/sintaksis;
3. **cakupan Qurani** — seberapa luas struktur digunakan dalam Al-Qur'an;
4. **cumulative-example yield** — berapa banyak contoh Qurani bersih yang tersedia ketika kandidat ditempatkan pada posisi tertentu.

Jika suatu urutan menghasilkan sangat sedikit contoh bersih sementara pertukaran urutan menghasilkan jauh lebih banyak tanpa melanggar dependency, urutan perlu dievaluasi kembali.

## 7. Lingkup Fase Aktif

Fase aktif saat ini hanya:

1. inventarisasi kandidat kompetensi linguistik Qurani;
2. pemetaan dependency antarkompetensi;
3. penyusunan kandidat urutan dari mudah ke sulit;
4. pengujian urutan dengan contoh Qurani kumulatif;
5. revisi urutan sampai stabil.

Fase ini tidak mencakup penentuan jilid, kelas, jumlah pertemuan, biaya, modul, desain buku, aplikasi, soal, atau produk turunan.

## 8. Integrasi Lintas Proyek

Hasil akhir dirancang agar dapat dikonsumsi oleh proyek lain tanpa membuat sumber data tandingan:

- **QURBATA:** sumber kompetensi dan contoh Qurani;
- **RIQA Education System:** pemetaan kurikulum/jenjang setelah tangga stabil;
- **RIQA OS:** konsumsi data kompetensi, progres, asesmen, dan rekomendasi;
- **RIQA Research Center:** dokumentasi metodologi, validasi, dan publikasi ilmiah;
- **RIQA Formal Competency System:** integrasi hanya melalui mapping setelah kompetensi Qurani stabil.

Prinsip integrasi: satu sumber kompetensi resmi, banyak konsumen.

## 9. Guardrails

- tidak mengubah `main` selama eksplorasi;
- tidak mengubah registry resmi dalam fase inventaris awal;
- tidak menciptakan ID permanen baru tanpa keputusan governance;
- setiap contoh Qurani harus memiliki referensi sumber;
- setiap kandidat urutan harus dapat diaudit ulang;
- tidak menyebut urutan sebagai final sebelum validasi corpus, ahli bahasa Arab, dan governance selesai.

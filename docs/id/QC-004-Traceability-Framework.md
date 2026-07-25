# QC-004 — Traceability Framework

**Kode Dokumen:** QC-004  
**Judul:** Kerangka Ketertelusuran Kebijakan, Proses, Sistem, dan Bukti  
**Bahasa Master:** Indonesia  
**Status:** Draft terkendali  
**Induk:** QC-000 QURBATA Konstitusi  
**Dokumen Terkait:** QC-001, QC-002, QC-003

---

## 1. Tujuan

Dokumen ini menetapkan kerangka ketertelusuran menyeluruh agar setiap kebijakan QURBATA dapat ditelusuri dari sumber normatif tertinggi sampai implementasi operasional, konfigurasi digital, data, bukti pelaksanaan, temuan audit, dan tindakan perbaikan.

Kerangka ini mencegah adanya fitur, proses, formulir, keputusan, atau data di RIQA OS yang tidak memiliki dasar resmi dan pemilik yang jelas.

## 2. Prinsip Dasar

1. Setiap aturan wajib memiliki sumber normatif.
2. Setiap proses wajib memiliki pemilik proses.
3. Setiap fitur digital wajib memiliki dasar kebijakan dan tujuan operasional.
4. Setiap data wajib memiliki definisi, pemilik, sumber, dan aturan penggunaan.
5. Setiap pengendalian wajib menghasilkan bukti yang dapat diaudit.
6. Setiap perubahan wajib dapat ditelusuri ke alasan, persetujuan, versi, dan dampaknya.
7. Tidak boleh ada lompatan ketertelusuran antara konstitusi, manual, SOP, sistem, data, dan bukti.

## 3. Rantai Ketertelusuran Wajib

Rantai standar QURBATA adalah:

```text
QC-000 Konstitusi
        ↓
Dokumen Governance / Manual
        ↓
Kebijakan atau Standar
        ↓
SOP / Instruksi Kerja
        ↓
Formulir / Template / Rubrik
        ↓
Modul dan Fitur RIQA OS
        ↓
Entitas Database / API / Konfigurasi
        ↓
Log, Rekaman, dan Bukti Pelaksanaan
        ↓
Indikator Kinerja dan Pengendalian
        ↓
Audit, Temuan, dan Tindakan Perbaikan
```

Hubungan sebaliknya juga wajib dapat dilakukan. Auditor harus dapat memulai dari satu data, tombol, transaksi, sertifikat, atau laporan, lalu menelusurinya kembali sampai pasal induk yang menjadi dasar keberadaannya.

## 4. Objek yang Wajib Memiliki Traceability ID

Objek berikut wajib memiliki pengenal ketertelusuran unik:

- pasal dan ayat dalam QC-000;
- kebijakan dan standar;
- manual dan pedoman;
- SOP dan instruksi kerja;
- formulir, template, rubrik, dan checklist;
- proses bisnis;
- peran dan kewenangan;
- modul, menu, halaman, dan fitur RIQA OS;
- tabel, kolom, relasi, dan aturan validasi database;
- endpoint API dan integrasi eksternal;
- laporan, dashboard, indikator, dan notifikasi;
- kontrol internal;
- rekaman audit;
- temuan, koreksi, dan tindakan perbaikan.

## 5. Format Traceability ID

Format umum:

```text
[DOMAIN]-[TYPE]-[NUMBER]
```

Contoh:

```text
GOV-POL-001     Kebijakan governance
ACA-SOP-012     SOP akademik
ASM-RUB-004     Rubrik asesmen
SYS-FTR-027     Fitur sistem
DAT-ENT-009     Entitas data
API-END-003     Endpoint API
AUD-CTL-015     Kontrol audit
```

Untuk referensi pasal digunakan format:

```text
QC000-P[NomorPasal]-A[NomorAyat]
```

Contoh:

```text
QC000-P12-A3
```

Format rinci dan register kode mengikuti QC-002.

## 6. Jenis Relasi

Setiap hubungan antarobjek wajib menggunakan salah satu jenis relasi berikut:

| Kode | Relasi | Makna |
|---|---|---|
| DERIVES_FROM | diturunkan dari | Objek turunan memperoleh dasar dari objek induk |
| IMPLEMENTS | mengimplementasikan | Proses atau sistem menjalankan suatu aturan |
| CONTROLS | mengendalikan | Kontrol membatasi atau memastikan kepatuhan objek |
| PRODUCES | menghasilkan | Proses menghasilkan rekaman, laporan, atau data |
| CONSUMES | menggunakan | Proses atau fitur menggunakan data atau keluaran lain |
| VERIFIED_BY | diverifikasi oleh | Kepatuhan dibuktikan melalui audit, tes, atau review |
| REPLACES | menggantikan | Versi baru menggantikan versi lama |
| DEPENDS_ON | bergantung pada | Objek tidak dapat berjalan tanpa objek lain |
| EXCEPTION_TO | pengecualian terhadap | Objek menetapkan pengecualian yang disahkan |
| CORRECTED_BY | diperbaiki oleh | Temuan ditutup melalui tindakan perbaikan |

## 7. Matriks Ketertelusuran

Setiap domain wajib memiliki Traceability Matrix minimum dengan kolom:

| Kolom | Keterangan |
|---|---|
| Traceability ID | Pengenal unik objek |
| Domain | Governance, akademik, SDM, keuangan, sistem, dan lainnya |
| Jenis Objek | Pasal, kebijakan, SOP, fitur, tabel, kontrol, bukti |
| Nama Objek | Nama resmi |
| Versi | Versi aktif |
| Sumber Induk | Pasal atau dokumen asal |
| Relasi | Jenis hubungan |
| Objek Turunan | Dokumen, proses, fitur, atau data terkait |
| Pemilik | Penanggung jawab substantif |
| Pengelola | Penanggung jawab administrasi atau teknis |
| Status | Draft, review, berlaku, ditangguhkan, dicabut, arsip |
| Bukti | Lokasi log, laporan, dokumen, atau rekaman |
| Tanggal Review | Jadwal pemeriksaan terakhir |
| Risiko | Dampak bila relasi tidak terpenuhi |

## 8. Ketertelusuran Modul RIQA OS

Setiap modul RIQA OS wajib memiliki Manifest Ketertelusuran yang memuat:

1. nama dan kode modul;
2. tujuan bisnis;
3. pasal dan dokumen kebijakan yang menjadi dasar;
4. proses bisnis yang diimplementasikan;
5. aktor dan matriks kewenangan;
6. daftar fitur;
7. daftar entitas data;
8. aturan validasi;
9. integrasi dan endpoint API;
10. keluaran, laporan, dan notifikasi;
11. kontrol keamanan dan audit;
12. bukti pengujian;
13. pemilik produk dan pemilik proses;
14. riwayat perubahan.

Fitur yang belum memiliki dasar kebijakan tidak boleh berstatus produksi. Fitur tersebut hanya boleh berada pada status eksperimen, prototipe, atau menunggu pengesahan.

## 9. Ketertelusuran Data

Setiap entitas dan atribut data wajib memiliki:

- nama bisnis dan nama teknis;
- definisi resmi;
- sumber data;
- tujuan pengumpulan;
- dasar kebijakan;
- pemilik data;
- klasifikasi kerahasiaan;
- aturan akses;
- aturan validasi;
- masa retensi;
- tujuan penggunaan;
- hubungan dengan laporan dan indikator;
- riwayat perubahan skema.

Data yang tidak memiliki definisi dan pemilik resmi tidak boleh dijadikan sumber keputusan strategis.

## 10. Ketertelusuran Asesmen dan Sertifikasi

Setiap nilai, status kelulusan, rekomendasi, dan sertifikat wajib dapat ditelusuri ke:

1. standar kompetensi;
2. capaian pembelajaran;
3. instrumen atau rubrik;
4. butir asesmen;
5. identitas asesor;
6. tanggal dan konteks asesmen;
7. bukti jawaban atau performa;
8. metode perhitungan;
9. aturan kelulusan;
10. persetujuan penerbitan;
11. nomor sertifikat;
12. log perubahan atau pembatalan.

Sertifikat yang kehilangan salah satu mata rantai utama tersebut dinyatakan tidak memenuhi standar audit QURBATA.

## 11. Ketertelusuran Keputusan

Keputusan strategis dan perubahan kebijakan wajib mencatat:

- masalah atau kebutuhan awal;
- data pendukung;
- alternatif yang dipertimbangkan;
- dasar normatif;
- pihak yang mereview;
- pihak yang menyetujui;
- tanggal efektif;
- unit terdampak;
- risiko dan mitigasi;
- dokumen dan fitur yang harus diperbarui;
- hasil evaluasi pasca-implementasi.

## 12. Pengendalian Perubahan

Setiap perubahan terhadap objek yang telah memiliki Traceability ID wajib melalui analisis dampak.

Analisis dampak minimum mencakup:

- dokumen induk dan turunan;
- SOP dan formulir;
- fitur dan antarmuka;
- tabel dan migrasi data;
- API dan integrasi;
- kewenangan pengguna;
- laporan dan indikator;
- pelatihan pengguna;
- risiko kepatuhan;
- kebutuhan uji ulang.

Perubahan tidak boleh dinyatakan selesai sebelum seluruh relasi terdampak diperbarui.

## 13. Validasi Ketertelusuran

Validasi dilakukan melalui:

1. review dokumen;
2. inspeksi matriks traceability;
3. pengujian fitur;
4. pemeriksaan log;
5. sampling rekaman;
6. audit data;
7. wawancara pemilik proses;
8. uji telusur maju dari pasal ke bukti;
9. uji telusur balik dari bukti ke pasal.

## 14. Klasifikasi Ketidaksesuaian

| Tingkat | Kondisi |
|---|---|
| Kritis | Tidak ada dasar normatif untuk proses atau fitur berisiko tinggi |
| Mayor | Satu atau lebih mata rantai utama tidak tersedia atau tidak konsisten |
| Minor | Metadata atau referensi pendukung belum lengkap, tetapi dasar utama tersedia |
| Observasi | Potensi kelemahan yang belum menjadi ketidaksesuaian |

Ketidaksesuaian kritis dapat menjadi dasar penghentian sementara proses, fitur, penerbitan dokumen, atau transaksi sampai kontrol minimum dipenuhi.

## 15. Tanggung Jawab

### 15.1 Pemilik Dokumen

Memastikan isi normatif, hubungan induk-turunan, dan status berlaku tetap benar.

### 15.2 Pemilik Proses

Memastikan SOP, formulir, pelaksanaan, dan bukti sesuai dengan kebijakan.

### 15.3 Pemilik Produk RIQA OS

Memastikan setiap fitur dan perubahan produk mempunyai dasar kebijakan serta manifest ketertelusuran.

### 15.4 Pengelola Data

Memastikan definisi, kualitas, akses, retensi, dan penggunaan data dapat ditelusuri.

### 15.5 Quality Assurance

Memeriksa kelengkapan matriks, menguji relasi, dan mencatat ketidaksesuaian.

### 15.6 Auditor

Melakukan uji telusur maju dan balik secara independen.

## 16. Kriteria Kepatuhan Minimum

Suatu proses atau fitur dinyatakan memenuhi QC-004 apabila:

- memiliki Traceability ID;
- memiliki dasar pasal atau dokumen induk;
- memiliki pemilik yang ditetapkan;
- hubungan dengan SOP, data, kontrol, dan bukti terdokumentasi;
- versi yang digunakan konsisten;
- dapat ditelusuri maju dan balik;
- perubahan terakhir telah melalui analisis dampak;
- tidak memiliki ketidaksesuaian kritis yang terbuka.

## 17. Implementasi Bertahap

Penerapan dilakukan dengan urutan:

1. menetapkan register Traceability ID;
2. memetakan dokumen QC yang telah ada;
3. memetakan proses utama;
4. memetakan modul RIQA OS;
5. memetakan entitas data;
6. menghubungkan kontrol dan bukti;
7. melakukan audit kesenjangan;
8. menutup relasi yang hilang;
9. mengotomatisasi validasi melalui RIQA OS.

## 18. Ketentuan Penutup

QC-004 menjadi standar wajib bagi seluruh dokumen, proses, fitur, data, integrasi, asesmen, sertifikasi, laporan, dan audit dalam ekosistem QURBATA.

Setiap dokumen turunan wajib merujuk pada kerangka ini ketika menetapkan hubungan antara aturan, pelaksanaan, sistem, dan bukti.
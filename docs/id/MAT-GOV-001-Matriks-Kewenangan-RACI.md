# MAT-GOV-001 — Matriks Kewenangan RACI QURBATA

**Kode Dokumen:** MAT-GOV-001  
**Status:** Draf Terkendali  
**Versi:** 0.1.0-id  
**Bahasa Induk:** Bahasa Indonesia  
**Induk Normatif:** QC-000, QC-006, QC-007, QC-008

## 1. Tujuan

Matriks ini menetapkan pembagian tanggung jawab untuk pekerjaan tata kelola QURBATA dan menjadi dasar konfigurasi peran serta izin pada RIQA OS.

## 2. Definisi

- **R — Responsible:** pelaksana utama pekerjaan.
- **A — Accountable:** pemegang akuntabilitas akhir dan pemberi keputusan.
- **C — Consulted:** pihak yang wajib dimintai pertimbangan.
- **I — Informed:** pihak yang wajib diberi informasi.

Satu aktivitas idealnya hanya memiliki satu `A`. Pihak yang memiliki konflik kepentingan tidak boleh menjadi `A` untuk keputusan terkait.

## 3. Peran Baku

| Kode | Peran |
|---|---|
| GOV | Otoritas/Pimpinan Tata Kelola |
| DOC | Pengelola Dokumen |
| ACA | Pemilik Akademik dan Kurikulum |
| QA | Penjaminan Mutu/Auditor Internal |
| SAFE | Penanggung Jawab Perlindungan Peserta Didik |
| DATA | Pemilik Data dan Informasi |
| TECH | Pemilik RIQA OS/Teknologi |
| OPS | Pemilik Proses Operasional |
| LEG | Penelaah Hukum/Kepatuhan bila tersedia |

## 4. Matriks RACI

| Aktivitas | GOV | DOC | ACA | QA | SAFE | DATA | TECH | OPS | LEG |
|---|---|---|---|---|---|---|---|---|---|
| Menetapkan atau mengubah QC-000 | A | R | C | C | C | C | C | I | C |
| Menyusun dokumen QC turunan | A | R | C | C | C | C | C | C | C |
| Memberi nomor dan metadata dokumen | I | A/R | C | C | I | C | C | I | I |
| Menelaah konsistensi konstitusional | A | R | C | R | C | C | C | I | C |
| Menetapkan istilah resmi | A | R | C | C | C | C | I | C | C |
| Menetapkan kurikulum dan urutan materi | I | C | A/R | C | C | I | C | C | I |
| Menetapkan standar asesmen | I | C | A/R | R | C | I | C | C | I |
| Mengesahkan materi yang berdampak pada peserta didik | I | C | A/R | C | R | I | I | C | I |
| Menyetujui perubahan skema data | I | C | C | C | C | A/R | R | I | C |
| Menyetujui perubahan arsitektur RIQA OS | I | I | C | C | C | C | A/R | C | I |
| Menetapkan klasifikasi akses dan privasi | A | C | I | C | C | R | C | I | C |
| Menangani pengaduan peserta didik | I | I | C | C | A/R | C | I | C | C |
| Menerima risiko residual strategis | A | I | C | C | C | C | C | R | C |
| Melakukan audit internal | I | C | C | A/R | C | C | C | C | I |
| Menutup temuan audit | A | C | R | R | C | C | C | R | I |
| Menerbitkan versi efektif | A | R | C | C | C | C | C | I | I |
| Mengarsipkan versi lama | I | A/R | I | C | I | C | C | I | I |
| Membekukan Governance v1.0 | A | R | C | R | C | C | C | I | C |

## 5. Aturan Eskalasi

1. Apabila `A` tidak tersedia, delegasi harus tertulis, berbatas waktu, dan tercatat.
2. Apabila terjadi sengketa kewenangan, QC-006 dan QC-007 mengendalikan.
3. Aktivitas perlindungan peserta didik tidak boleh berjalan tanpa keterlibatan `SAFE`.
4. Perubahan yang menyentuh data pribadi wajib melibatkan `DATA`.
5. Perubahan yang berpotensi mengubah makna normatif wajib melibatkan `DOC` dan `QA`.
6. Auditor tidak boleh mengaudit pekerjaan yang sepenuhnya ia susun sendiri tanpa reviewer independen.

## 6. Pemetaan Izin RIQA OS

| Peran | Izin Minimum |
|---|---|
| GOV | approve, ratify, suspend, revoke, accept-risk |
| DOC | create-document, assign-id, manage-version, publish, archive |
| ACA | create-curriculum, approve-learning-content, manage-assessment |
| QA | review, audit, raise-finding, verify-corrective-action |
| SAFE | safeguarding-review, restrict-access, manage-case |
| DATA | classify-data, approve-schema, manage-retention |
| TECH | manage-system-specification, deploy, rollback |
| OPS | execute-process, create-record, implement-action |

Hak akses aktual harus mengikuti prinsip least privilege, separation of duties, dan audit trail.

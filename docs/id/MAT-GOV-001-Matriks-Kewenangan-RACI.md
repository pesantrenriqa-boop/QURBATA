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

## 7. Register Penetapan Peran

| Assignment-ID | Peran | Personel | Dasar Penetapan | Pengganti | Kompetensi Diverifikasi | Konflik Diperiksa | Status |
|---|---|---|---|---|---|---|---|
| ASN-GOV-001 | Otoritas Konstitusional Awal | Aris Liswanto, S.Pd., M.Pd. | QC-000 tahap pendirian | Menunggu | Menunggu bukti formal | Wajib diperiksa per keputusan | DRAFT |
| ASN-GOV-002 | Document Controller | Aris Liswanto | QC-000 tahap pendirian dan penetapan pengguna 26 Juli 2026 | Menunggu | Perlu dilengkapi | Wajib diperiksa per keputusan | ACTIVE |
| ASN-GOV-003 | QA Lead | Aris Liswanto | QC-000 tahap pendirian dan penetapan pengguna 26 Juli 2026 | Menunggu | Perlu dilengkapi | Perangkapan dengan Document Controller; verifikasi independen diwajibkan | ACTIVE |
| ASN-GOV-004 | Knowledge Architect | Menunggu | Menunggu surat penetapan | Menunggu | Belum | Belum | VACANT |
| ASN-GOV-005 | Safeguarding Lead | Ainul Yakin | Penetapan pengguna 26 Juli 2026 untuk tahap pendirian | Menunggu | Perlu dilengkapi | Wajib diperiksa per perkara dan keputusan | ACTIVE |
| ASN-GOV-006 | Risk/Continuity Lead | Arif Nasruddin | Penetapan pengguna 26 Juli 2026 untuk tahap pendirian | Menunggu | Perlu dilengkapi | Merangkap Penelaah Independen; tidak boleh memvalidasi sendiri bukti/keputusan risiko yang dikelola | ACTIVE |
| ASN-GOV-007 | Penelaah Independen | Arif Nasruddin | Penetapan pengguna 26 Juli 2026 untuk telaah Governance v1.0 | Menunggu | Dosen UNIRA dan UIN Maulana Malik Ibrahim Malang; REC-GOV-001 | Tidak ada konflik yang dinyatakan; REC-GOV-001 | ACTIVE |

Status yang diizinkan: DRAFT, ACTIVE, SUSPENDED, EXPIRED, REVOKED, dan VACANT. Peran kritis berstatus VACANT menggagalkan gate yang membutuhkan kewenangan atau independensi tersebut.

## 8. Kontrol Pemisahan Tugas

1. Penyusun tidak menjadi satu-satunya penelaah atau pengesah karyanya sendiri.
2. Pelaksana CAPA tidak memverifikasi efektivitas tindakannya sendiri.
3. Pemilik risiko tidak menjadi satu-satunya pihak yang menerima risiko kritis.
4. Pengambil keputusan awal tidak menjadi satu-satunya pemutus banding.
5. Administrator sistem tidak otomatis memperoleh kewenangan normatif.
6. Akses RIQA OS harus diturunkan dari Assignment-ID aktif dan dicabut ketika status tidak aktif.

## 9. Uji RACI dan Akses

Sebelum freeze, dilakukan uji skenario untuk persetujuan dokumen, perubahan material, konflik kepentingan, pengaduan, insiden safeguarding, CAPA, penerimaan risiko, pemulihan, dan pembukaan kembali freeze. Setiap uji menghasilkan Evidence-ID.


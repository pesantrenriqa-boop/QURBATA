# REG-GOV-002 — Register Siklus Hidup Dokumen QURBATA

**Kode Dokumen:** REG-GOV-002  
**Status:** Draf Terkendali  
**Versi:** 0.1.0-id  
**Bahasa Induk:** Bahasa Indonesia  
**Induk Normatif:** QC-000, QC-002, QC-003, QC-007

## 1. Tujuan

Register ini mengendalikan status, versi, pemilik, persetujuan, tanggal berlaku, peninjauan, penggantian, pengarsipan, dan penghentian seluruh dokumen resmi QURBATA.

## 2. Status Siklus Hidup

| Status | Makna | Boleh digunakan sebagai dasar keputusan? |
|---|---|---|
| PROPOSED | Usulan awal, belum menjadi draf resmi | Tidak |
| DRAFT | Sedang disusun | Tidak |
| CONTROLLED-DRAFT | Draf terdaftar dan dapat ditelaah | Terbatas untuk review |
| IN-REVIEW | Sedang ditelaah | Tidak |
| APPROVED | Telah disetujui, belum berlaku | Belum |
| EFFECTIVE | Berlaku resmi | Ya |
| SUSPENDED | Penerapan ditangguhkan sementara | Tidak, kecuali keputusan khusus |
| SUPERSEDED | Digantikan versi atau dokumen baru | Tidak |
| RETIRED | Dihentikan permanen | Tidak |
| ARCHIVED | Disimpan sebagai rekaman historis | Tidak |

## 3. Aturan Perubahan Status

| Dari | Ke | Otoritas Minimum | Bukti Wajib |
|---|---|---|---|
| PROPOSED | DRAFT | Pemilik dokumen | Mandat penyusunan |
| DRAFT | CONTROLLED-DRAFT | Pengelola dokumen | Metadata minimum lengkap |
| CONTROLLED-DRAFT | IN-REVIEW | Pemilik dokumen | Permintaan review |
| IN-REVIEW | APPROVED | Otoritas persetujuan | Catatan review dan keputusan |
| APPROVED | EFFECTIVE | Otoritas ratifikasi/penerbitan | Tanggal berlaku dan publikasi |
| EFFECTIVE | SUSPENDED | Otoritas sesuai QC-007 | Alasan, risiko, masa penangguhan |
| EFFECTIVE | SUPERSEDED | Otoritas persetujuan | Dokumen/versi pengganti |
| EFFECTIVE | RETIRED | Otoritas persetujuan | Analisis dampak dan keputusan |
| SUPERSEDED | ARCHIVED | Pengelola dokumen | Rekaman migrasi |
| RETIRED | ARCHIVED | Pengelola dokumen | Rekaman penutupan |

## 4. Kolom Register Minimum

| Kolom | Keterangan |
|---|---|
| Document-ID | Kode resmi dokumen |
| Knowledge-ID | ID objek pengetahuan terkait |
| Judul | Judul resmi |
| Versi | Versi semantik |
| Status | Status siklus hidup |
| Pemilik | Penanggung jawab substansi |
| Reviewer | Penelaah |
| Approver | Pemberi persetujuan |
| Ratifier | Pemberi pengesahan akhir bila diperlukan |
| Tanggal Berlaku | Awal keberlakuan |
| Review Berikutnya | Batas peninjauan |
| Menggantikan | Dokumen/versi sebelumnya |
| Digantikan Oleh | Dokumen/versi baru |
| Lokasi Resmi | Path repositori atau lokasi terkendali |
| Bukti Persetujuan | Keputusan, PR, atau rekaman persetujuan |
| Catatan | Keterangan tambahan |

## 5. Register Awal

| Document-ID | Judul | Versi | Status | Lokasi Resmi | Catatan |
|---|---|---:|---|---|---|
| QC-000 | Konstitusi QURBATA | 0.1.0-id | CONTROLLED-DRAFT | docs/id/QC-000-QURBATA-Konstitusi.md | Dokumen normatif tertinggi |
| QC-001 | Arsitektur Tata Kelola | 0.1.0-id | CONTROLLED-DRAFT | docs/id/QC-001-Governance-Architecture.md | Turunan QC-000 |
| QC-002 | Standar Penomoran dan Pengkodean | 0.1.0-id | CONTROLLED-DRAFT | docs/id/QC-002-Standar-Penomoran-dan-Pengkodean-Dokumen.md | Pengendali identitas dokumen |
| QC-003 | Proses Penyusunan dan Pengelolaan Dokumen | 0.1.0-id | CONTROLLED-DRAFT | docs/id/QC-003-Proses-Penyusunan-dan-Pengelolaan-Dokumen.md | Pengendali siklus hidup |
| QC-004 | Kerangka Keterlacakan | 0.1.0-id | CONTROLLED-DRAFT | docs/id/QC-004-Traceability-Framework.md | Pengendali traceability |
| QC-005 | Terminologi dan Definisi Resmi | 0.1.0-id | CONTROLLED-DRAFT | docs/id/QC-005-Terminologi-dan-Definisi-Resmi-QURBATA.md | Pengendali istilah |
| QC-006 | Peran, Kewenangan, dan Akuntabilitas | 0.1.0-id | CONTROLLED-DRAFT | docs/id/QC-006-Peran-Kewenangan-dan-Akuntabilitas.md | Pengendali peran |
| QC-007 | Keputusan, Persetujuan, dan Ratifikasi | 0.1.0-id | CONTROLLED-DRAFT | docs/id/QC-007-Mekanisme-Pengambilan-Keputusan-Persetujuan-dan-Ratifikasi.md | Pengendali keputusan |
| QC-008 | Konflik Kepentingan, Etika, dan Independensi | 0.1.0-id | CONTROLLED-DRAFT | docs/id/QC-008-Konflik-Kepentingan-Etika-dan-Independensi.md | Pengendali integritas |
| QC-009 | Pengaduan, Keberatan, Banding, dan Perlindungan Pelapor | 0.1.0-id | CONTROLLED-DRAFT | docs/id/QC-009-Pengaduan-Keberatan-Banding-dan-Perlindungan-Pelapor.md | Pengendali keadilan prosedural |
| QC-010 | Manajemen Risiko dan Keberlangsungan Bisnis | 0.1.0-id | CONTROLLED-DRAFT | docs/id/QC-010-Manajemen-Risiko-dan-Keberlangsungan-Bisnis.md | Pengendali risiko |
| QC-011 | Analisis Dampak Bisnis dan Pemulihan Bencana | 0.1.0-id | CONTROLLED-DRAFT | docs/id/QC-011-Analisis-Dampak-Bisnis-dan-Pemulihan-Bencana.md | Pengendali pemulihan |
| QC-012 | Perlindungan Peserta Didik, Keselamatan, dan Kesejahteraan | 0.1.0-id | CONTROLLED-DRAFT | docs/id/QC-012-Perlindungan-Peserta-Didik-Keselamatan-dan-Kesejahteraan.md | Pengendali safeguarding |

## 6. Aturan Audit

Register harus diperiksa untuk mendeteksi dokumen tanpa pemilik, versi ganda, status tidak sah, review kedaluwarsa, dokumen efektif tanpa bukti persetujuan, dan dokumen yang digantikan tetapi masih dirujuk sebagai versi berlaku.

## 7. Integrasi RIQA OS

RIQA OS harus menyediakan objek Document, DocumentVersion, LifecycleTransition, ApprovalEvidence, ReviewSchedule, dan SupersessionLink. Setiap perubahan status wajib menghasilkan audit trail yang tidak dapat dihapus oleh pengguna biasa.

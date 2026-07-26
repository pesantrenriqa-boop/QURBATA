# REG-GOV-004 — Register Dokumen Terkendali QURBATA

## 1. Tujuan
Register ini menjadi daftar induk seluruh dokumen resmi QURBATA yang wajib dikendalikan versi, status, pemilik, otoritas persetujuan, masa berlaku, dan keterlacakan perubahannya.

## 2. Aturan Pengendalian
1. Setiap dokumen resmi wajib memiliki ID unik sesuai QC-002.
2. Hanya versi berstatus `Efektif` yang boleh menjadi rujukan operasional.
3. Dokumen `Draf`, `Dalam Telaah`, atau `Dicabut` tidak boleh dipakai sebagai dasar keputusan final.
4. Setiap perubahan material wajib memiliki Decision-ID dan catatan perubahan.
5. Salinan lokal dianggap tidak terkendali kecuali identik dengan versi repositori.

## 3. Status Dokumen
- Usulan
- Draf
- Dalam Telaah
- Menunggu Persetujuan
- Disetujui
- Efektif
- Ditangguhkan
- Dicabut
- Diarsipkan

## 4. Register Induk Awal
| ID | Judul | Jenis | Pemilik | Otoritas Persetujuan | Status | Versi | Bahasa Induk | Review Berikutnya |
|---|---|---|---|---|---|---|---|---|
| QC-000 | Konstitusi QURBATA | Konstitusi | Pimpinan QURBATA | Otoritas Ratifikasi | Draf lanjut | 0.9.0 | Indonesia | Sebelum ratifikasi |
| QC-001 | Arsitektur Tata Kelola | Kebijakan | Governance Lead | Pimpinan QURBATA | Draf terkendali | 0.8.0 | Indonesia | Sebelum Governance Freeze |
| QC-002 | Standar Penomoran dan Pengkodean Dokumen | Standar | Document Controller | Governance Lead | Draf terkendali | 0.8.0 | Indonesia | Sebelum Governance Freeze |
| QC-003 | Proses Penyusunan dan Pengelolaan Dokumen | Prosedur | Document Controller | Governance Lead | Draf terkendali | 0.8.0 | Indonesia | Sebelum Governance Freeze |
| QC-004 | Kerangka Keterlacakan | Kerangka | QA Lead | Governance Lead | Draf terkendali | 0.8.0 | Indonesia | Sebelum Governance Freeze |
| QC-005 | Terminologi dan Definisi Resmi | Standar | Knowledge Architect | Governance Lead | Draf terkendali | 0.8.0 | Indonesia | Sebelum Governance Freeze |
| QC-006 | Peran, Kewenangan, dan Akuntabilitas | Kebijakan | Governance Lead | Pimpinan QURBATA | Draf terkendali | 0.8.0 | Indonesia | Sebelum Governance Freeze |
| QC-007 | Pengambilan Keputusan, Persetujuan, dan Ratifikasi | Prosedur | Governance Lead | Pimpinan QURBATA | Draf terkendali | 0.8.0 | Indonesia | Sebelum Governance Freeze |
| QC-008 | Konflik Kepentingan, Etika, dan Independensi | Kebijakan | Ethics Officer | Pimpinan QURBATA | Draf terkendali | 0.8.0 | Indonesia | Sebelum Governance Freeze |
| QC-009 | Pengaduan, Keberatan, Banding, dan Perlindungan Pelapor | Prosedur | Complaints Officer | Pimpinan QURBATA | Draf terkendali | 0.8.0 | Indonesia | Sebelum Governance Freeze |
| QC-010 | Manajemen Risiko dan Keberlangsungan Bisnis | Kerangka | Risk Owner | Pimpinan QURBATA | Draf terkendali | 0.8.0 | Indonesia | Sebelum Governance Freeze |
| QC-011 | Analisis Dampak Bisnis dan Pemulihan Bencana | Kerangka | Technology & Data Lead | Pimpinan QURBATA | Draf terkendali | 0.8.0 | Indonesia | Sebelum Governance Freeze |
| QC-012 | Perlindungan Peserta Didik, Keselamatan, dan Kesejahteraan | Kebijakan | Safeguarding Lead | Pimpinan QURBATA | Draf terkendali | 0.8.0 | Indonesia | Sebelum Governance Freeze |
| REG-GOV-001 | Register Knowledge-ID | Register | Knowledge Architect | Governance Lead | Draf terkendali | 0.1.0 | Indonesia | Bersamaan dengan QC-005 |
| REG-GOV-002 | Register Siklus Hidup Dokumen | Register | Document Controller | Governance Lead | Draf terkendali | 0.1.0 | Indonesia | Bulanan selama pengembangan |
| REG-GOV-003 | Register Keputusan Tata Kelola | Register | Governance Secretariat | Governance Lead | Draf terkendali | 0.1.0 | Indonesia | Setiap keputusan material |
| MAT-GOV-001 | Matriks Kewenangan RACI | Matriks | Governance Lead | Pimpinan QURBATA | Draf terkendali | 0.1.0 | Indonesia | Saat struktur berubah |
| CHK-GOV-001 | Checklist Kepatuhan Konstitusional | Checklist | QA Lead | Governance Lead | Draf terkendali | 0.1.0 | Indonesia | Setiap audit/ratifikasi |
| REG-GOV-004 | Register Dokumen Terkendali | Register | Document Controller | Governance Lead | Draf terkendali | 0.1.0 | Indonesia | Mingguan selama pengembangan |

## 5. Kolom Minimum RIQA OS
`document_id`, `title`, `type`, `owner`, `approver`, `status`, `version`, `language_master`, `effective_date`, `next_review`, `repository_path`, `decision_id`, `supersedes`, `access_class`, `last_modified_at`.

## 6. Kontrol Otomatis
RIQA OS harus menandai:
- ID ganda;
- versi mundur;
- dokumen efektif tanpa persetujuan;
- tanggal review lewat;
- rujukan ke dokumen dicabut;
- dokumen tanpa pemilik;
- dokumen tanpa riwayat perubahan.

## 7. Catatan Perubahan
| Versi | Tanggal | Perubahan | Keputusan |
|---|---|---|---|
| 0.1.0 | 2026-07-26 | Register awal dokumen governance dibuat | Pengembangan PR #1 |

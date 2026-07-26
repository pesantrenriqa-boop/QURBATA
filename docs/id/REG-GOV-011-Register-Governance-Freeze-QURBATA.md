# REG-GOV-011 — Register Governance Freeze QURBATA

**Kode Dokumen:** REG-GOV-011  
**Judul:** Register Governance Freeze QURBATA  
**Bahasa Induk:** Bahasa Indonesia  
**Status:** Draf Terkendali  
**Versi:** 0.2.0-id  
**Pemilik Dokumen:** Fungsi Tata Kelola dan Penjaminan Mutu QURBATA  
**Otoritas Persetujuan:** Pendiri dan Peneliti Utama/Dewan Konstitusi setelah aktif  
**Tanggal Berlaku:** Setelah persetujuan sesuai kewenangan  
**Tinjauan Berikutnya:** Pada setiap permohonan freeze atau perubahan material  
**Klasifikasi Akses:** Internal; ringkasan keputusan dapat dipublikasikan  
**Induk Normatif:** QC-000 — Konstitusi QURBATA  
**Dokumen Pengendali:** QC-003, QC-004, QC-006, QC-007, CHK-GOV-001, MAT-GOV-001, dan REG-GOV-010

---

## 1. Tujuan

Register ini menjadi sumber tunggal untuk menilai, mencatat, menyetujui, menolak, menunda, membatalkan, atau membuka kembali Governance Freeze. Freeze menetapkan baseline stabil untuk tata kelola, bukan menyatakan seluruh proyek QURBATA selesai dan bukan menghapus kewajiban perbaikan.

## 2. Ruang Lingkup Freeze

Objek freeze dapat berupa:

1. QC-000;
2. keluarga QC-001–QC-012;
3. toolkit tata kelola;
4. skema Knowledge-ID dan keterlacakan;
5. paket Governance v1.0; atau
6. baseline khusus yang ditetapkan melalui Decision-ID.

Setiap permohonan harus menyebutkan daftar dokumen, versi, commit SHA atau identitas arsip, serta pengecualian yang tidak termasuk.

## 3. Status Permohonan

| Status | Makna |
|---|---|
| DRAFT | Permohonan sedang disusun |
| UNDER-REVIEW | Bukti dan gate sedang diperiksa |
| BLOCKED | Terdapat kegagalan gate kritis |
| CONDITIONAL | Dapat dilanjutkan dengan syarat terbatas yang tidak menyentuh gate kritis |
| APPROVED | Disetujui tetapi belum efektif |
| FROZEN | Baseline telah efektif dan dikunci |
| REOPENED | Baseline dibuka kembali melalui keputusan sah |
| REVOKED | Status freeze dicabut |

## 4. Gerbang Wajib

| Gate | Kriteria | Kritis |
|---|---|---|
| GF-01 | QC-000 lengkap secara substantif | Ya |
| GF-02 | QC-001–QC-012 tidak bertentangan dengan QC-000 | Ya |
| GF-03 | Metadata minimum seluruh dokumen lengkap | Ya |
| GF-04 | ID dokumen dan Knowledge-ID tidak ganda atau yatim | Ya |
| GF-05 | Rujukan silang dan tautan sumber valid | Ya |
| GF-06 | Terminologi material konsisten dengan QC-005 | Ya |
| GF-07 | Kewenangan, RACI, quorum, dan ratifikasi konsisten | Ya |
| GF-08 | Perlindungan peserta didik dan proses pengaduan tersedia | Ya |
| GF-09 | Risiko kritis tidak dibiarkan tanpa pengendalian | Ya |
| GF-10 | Temuan kritis dan mayor ditutup atau mempunyai keputusan risiko sah | Ya |
| GF-11 | CAPA yang diselesaikan telah diuji efektivitasnya | Ya |
| GF-12 | Matriks keterlacakan mempunyai pemilik, kontrol, dan bukti yang dapat diverifikasi | Ya |
| GF-13 | Naskah Bahasa Indonesia lulus telaah substantif dan editorial | Ya |
| GF-14 | Daftar keberatan material serta penyelesaiannya tersedia | Ya |
| GF-15 | Baseline commit/hash, lokasi resmi, dan paket arsip ditetapkan | Ya |
| GF-16 | Decision-ID, tanggal efektif, transisi, dan tinjauan berikutnya ditetapkan | Ya |

Satu kegagalan gate kritis menggagalkan freeze meskipun skor agregat tinggi.

## 5. Bukti Minimum

Setiap gate mencatat:

- status PASS, PARTIAL, FAIL, atau NOT-APPLICABLE;
- alasan;
- Evidence-ID;
- tautan bukti;
- pemilik bukti;
- validator;
- tanggal validasi;
- temuan terkait;
- risiko terkait;
- CAPA terkait; dan
- catatan pengecualian.

NOT-APPLICABLE hanya sah apabila alasan dan otoritas penetapannya terdokumentasi.

## 6. Register Permohonan

| Freeze-ID | Objek | Versi/Baseline | Status | PASS | PARTIAL | FAIL | Pemilik | Decision-ID |
|---|---|---|---|---:|---:|---:|---|---|
| GF-2026-001 | Governance v1.0 | PR #1 / branch feature/f001-constitution | BLOCKED | 4 | 10 | 2 | Fungsi Tata Kelola | Menunggu |

Angka gate pada register hanya diperbarui setelah bukti dinilai, bukan berdasarkan keberadaan dokumen semata.

## 7. Rekaman Penilaian Gate

| Freeze-ID | Gate | Status | Evidence-ID | Validator | Tanggal | Catatan |
|---|---|---|---|---|---|---|
| GF-2026-001 | GF-01 | PASS | EVD-AUD-000002 | Audit internal awal | 2026-07-26 | Master substantif lengkap |
| GF-2026-001 | GF-02 | PARTIAL | EVD-AUD-000003 | Audit internal awal | 2026-07-26 | Telaah konflik independen belum selesai |
| GF-2026-001 | GF-03 | PASS | EVD-AUD-000003 | Audit internal awal | 2026-07-26 | Metadata minimum tersedia |
| GF-2026-001 | GF-04 | PARTIAL | EVD-AUD-000006 | Audit internal awal | 2026-07-26 | Audit orphan dan populasi penuh belum selesai |
| GF-2026-001 | GF-05 | PASS | EVD-AUD-000001 | Audit internal awal | 2026-07-26 | Tidak ada tautan relatif rusak |
| GF-2026-001 | GF-06 | PARTIAL | EVD-AUD-000006 | Audit internal awal | 2026-07-26 | Audit penggunaan istilah belum selesai |
| GF-2026-001 | GF-07 | PARTIAL | EVD-AUD-000005 | Audit internal awal | 2026-07-26 | Penetapan personel belum dibuktikan |
| GF-2026-001 | GF-08 | PASS | EVD-AUD-000009 | Audit internal awal | 2026-07-26 | Dokumen safeguarding dan pengaduan tersedia |
| GF-2026-001 | GF-09 | PARTIAL | EVD-AUD-000010 | Audit internal awal | 2026-07-26 | Mitigasi risiko belum seluruhnya diverifikasi |
| GF-2026-001 | GF-10 | FAIL | EVD-AUD-000007 | Audit internal awal | 2026-07-26 | Temuan mayor masih terbuka |
| GF-2026-001 | GF-11 | PARTIAL | EVD-AUD-000010 | Audit internal awal | 2026-07-26 | Efektivitas CAPA belum diverifikasi |
| GF-2026-001 | GF-12 | PARTIAL | EVD-AUD-000006 | Audit internal awal | 2026-07-26 | Bukti implementasi CTM belum lengkap |
| GF-2026-001 | GF-13 | PARTIAL | EVD-AUD-000002 | Audit internal awal | 2026-07-26 | Telaah independen belum selesai |
| GF-2026-001 | GF-14 | PARTIAL | EVD-AUD-000008 | Audit internal awal | 2026-07-26 | Register keberatan belum tersedia |
| GF-2026-001 | GF-15 | PARTIAL | EVD-AUD-000008 | Audit internal awal | 2026-07-26 | Baseline hash final belum ditetapkan |
| GF-2026-001 | GF-16 | FAIL | EVD-AUD-000008 | Audit internal awal | 2026-07-26 | Decision-ID dan tanggal efektif belum ada |

## 8. Keputusan Freeze

Keputusan sekurang-kurangnya memuat:

1. Freeze-ID;
2. ruang lingkup dan pengecualian;
3. daftar versi serta baseline commit/hash;
4. ringkasan hasil gate;
5. temuan dan risiko sisa;
6. keberatan yang dicatat;
7. syarat sebelum efektif;
8. tanggal persetujuan dan tanggal efektif;
9. masa transisi;
10. pihak yang berwenang;
11. Decision-ID; dan
12. jadwal tinjauan atau pemicu pembukaan kembali.

## 9. Pembukaan Kembali

Freeze wajib ditinjau untuk dibuka kembali apabila terjadi perubahan konstitusional, perubahan hukum material, insiden kritis, temuan audit kritis, bukti ilmiah penting, kegagalan perlindungan peserta didik, perubahan arsitektur, atau kebutuhan koreksi yang tidak dapat dilakukan sebagai perubahan editorial.

Pembukaan kembali tidak menghapus baseline lama. Baseline lama dipertahankan sebagai arsip dan hubungan penggantinya dicatat.

## 10. Integrasi RIQA OS

RIQA OS harus mendukung Freeze-ID, daftar objek dan versi, gate, bukti, validator, temuan, CAPA, risiko, keberatan, keputusan, quorum, baseline hash, status, tanggal efektif, transisi, tinjauan, serta audit trail.

Sistem harus mencegah status FROZEN apabila ada gate kritis FAIL, Evidence-ID wajib kosong, Decision-ID belum sah, atau baseline tidak mempunyai identitas yang dapat diverifikasi.

## 11. Riwayat Perubahan

| Versi | Tanggal | Ringkasan |
|---|---|---|
| 0.1.0-id | 26 Juli 2026 | Register awal Governance Freeze dan 16 gate wajib |
| 0.2.0-id | 26 Juli 2026 | Penilaian audit awal: 4 PASS, 10 PARTIAL, 2 FAIL; status BLOCKED |

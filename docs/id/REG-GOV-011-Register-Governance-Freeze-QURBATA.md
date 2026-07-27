# REG-GOV-011 — Register Governance Freeze QURBATA

**Kode Dokumen:** REG-GOV-011  
**Judul:** Register Governance Freeze QURBATA  
**Bahasa Induk:** Bahasa Indonesia  
**Status:** Draf Terkendali  
**Versi:** 0.10.0-id  
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
| GF-2026-001 | Governance v1.0 | `20892fbd5892dc2a79f23012ed6c98d0685a6eaa` | BLOCKED | 14 | 0 | 2 | Fungsi Tata Kelola | Menunggu |

Angka gate pada register hanya diperbarui setelah bukti dinilai, bukan berdasarkan keberadaan dokumen semata.

## 7. Rekaman Penilaian Gate

| Freeze-ID | Gate | Status | Evidence-ID | Validator | Tanggal | Catatan |
|---|---|---|---|---|---|---|
| GF-2026-001 | GF-01 | PASS | EVD-AUD-000002 | Audit internal awal | 2026-07-26 | Master substantif lengkap |
| GF-2026-001 | GF-02 | PASS | EVD-GOV-000002/EVD-GOV-000003 | Arif Nasruddin | 2026-07-26 | QC-001–QC-012 dinilai bagus, valid, dapat dilanjutkan, dan tanpa keberatan material |
| GF-2026-001 | GF-03 | PASS | EVD-AUD-000003 | Audit internal awal | 2026-07-26 | Metadata minimum tersedia |
| GF-2026-001 | GF-04 | PASS | EVD-AUD-000006 | Audit internal | 2026-07-27 | Tidak ditemukan ID ganda atau referensi CTM yatim; kelengkapan pemetaan dinilai terpisah pada GF-12 |
| GF-2026-001 | GF-05 | PASS | EVD-AUD-000001 | Audit internal awal | 2026-07-26 | Tidak ada tautan relatif rusak |
| GF-2026-001 | GF-06 | PASS | EVD-GOV-000015/EVD-GOV-000002 | Document Controller/Arif Nasruddin | 2026-07-27 | Istilah material diselaraskan dengan QC-005 dan seri QC lulus telaah independen tanpa keberatan material |
| GF-2026-001 | GF-07 | PASS | EVD-AUD-000005/EVD-GOV-000013/EVD-GOV-000014/EVD-GOV-000018 | Audit internal | 2026-07-27 | Peran, pengganti, pemisahan tugas, quorum, dan ratifikasi konsisten dalam delapan skenario uji meja |
| GF-2026-001 | GF-08 | PASS | EVD-AUD-000009 | Audit internal awal | 2026-07-26 | Dokumen safeguarding dan pengaduan tersedia |
| GF-2026-001 | GF-09 | PASS | EVD-GOV-000016 | Audit internal | 2026-07-27 | Sepuluh risiko terdaftar; skor maksimum 16 dan tidak terdapat risiko kritis tanpa pengendalian |
| GF-2026-001 | GF-10 | FAIL | EVD-AUD-000007 | Audit internal awal | 2026-07-26 | Temuan mayor masih terbuka |
| GF-2026-001 | GF-11 | PASS | EVD-GOV-000017 | Audit internal | 2026-07-27 | Seluruh CAPA berstatus ditutup mempunyai bukti efektivitas yang dapat diperiksa |
| GF-2026-001 | GF-12 | PASS | EVD-GOV-000019 | Audit internal | 2026-07-27 | Dua puluh dari dua puluh baris CTM memiliki ID, kontrol, bukti minimum, pemilik, dan objek implementasi lengkap |
| GF-2026-001 | GF-13 | PASS | EVD-GOV-000004 | Arif Nasruddin | 2026-07-26 | QC-000 dinilai valid dan layak dilanjutkan |
| GF-2026-001 | GF-14 | PASS | EVD-GOV-000003 | Arif Nasruddin | 2026-07-26 | Tidak ada keberatan material yang dinyatakan |
| GF-2026-001 | GF-15 | PASS | EVD-GOV-000020 | Document Controller | 2026-07-27 | Commit SHA kandidat, lokasi resmi, dan paket arsip ZIP/TAR.GZ berbasis SHA telah ditetapkan |
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
| 0.2.0-id | 26 Juli 2026 | Penilaian audit awal diperbarui: 6 PASS, 8 PARTIAL, 2 FAIL; status BLOCKED |
| 0.3.0-id | 27 Juli 2026 | GF-09 dinaikkan menjadi PASS berdasarkan audit profil risiko; total 7 PASS, 7 PARTIAL, 2 FAIL |
| 0.4.0-id | 27 Juli 2026 | GF-02 dinaikkan menjadi PASS berdasarkan REC-GOV-002 dan REC-GOV-003; total 8 PASS, 6 PARTIAL, 2 FAIL |
| 0.5.0-id | 27 Juli 2026 | GF-06 dinaikkan menjadi PASS setelah harmonisasi dan pembakuan terminologi; total 9 PASS, 5 PARTIAL, 2 FAIL |
| 0.6.0-id | 27 Juli 2026 | GF-04 dinaikkan menjadi PASS setelah audit duplikasi dan orphan; total 10 PASS, 4 PARTIAL, 2 FAIL |
| 0.7.0-id | 27 Juli 2026 | GF-11 dinaikkan menjadi PASS setelah verifikasi CAPA tertutup; total 11 PASS, 3 PARTIAL, 2 FAIL |
| 0.8.0-id | 27 Juli 2026 | GF-07 dinaikkan menjadi PASS setelah uji meja RACI dan kewenangan; total 12 PASS, 2 PARTIAL, 2 FAIL |
| 0.9.0-id | 27 Juli 2026 | GF-12 dinaikkan menjadi PASS setelah validasi desain CTM; total 13 PASS, 1 PARTIAL, 2 FAIL |
| 0.10.0-id | 27 Juli 2026 | GF-15 dinaikkan menjadi PASS setelah attestasi baseline kandidat; total 14 PASS, 0 PARTIAL, 2 FAIL |

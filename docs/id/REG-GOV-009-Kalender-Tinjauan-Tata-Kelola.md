# REG-GOV-009 — Kalender Tinjauan Tata Kelola QURBATA

**Kode Dokumen:** REG-GOV-009  
**Judul:** Kalender Tinjauan Tata Kelola QURBATA  
**Bahasa Induk:** Bahasa Indonesia  
**Status:** Draf Terkendali  
**Versi:** 0.2.0-id  
**Pemilik Dokumen:** Fungsi Tata Kelola QURBATA  
**Otoritas Persetujuan:** Pendiri dan Peneliti Utama/Dewan Konstitusi setelah aktif  
**Tanggal Berlaku:** Setelah persetujuan sesuai kewenangan  
**Tinjauan Berikutnya:** Tahunan atau ketika terdapat perubahan material  
**Klasifikasi Akses:** Internal; ringkasan dapat dipublikasikan  
**Induk Normatif:** QC-000 — Konstitusi QURBATA  
**Dokumen Pengendali:** QC-001, QC-003, QC-004, QC-006, dan QC-007  


## 1. Tujuan
Kalender ini menetapkan kapan dokumen, risiko, keputusan, audit, CAPA, safeguarding, data, dan kesiapan sistem harus ditinjau agar pengendalian tidak bergantung pada ingatan individu.

## 2. Prinsip
1. Tinjauan berbasis risiko dan peristiwa.
2. Tenggat tidak boleh dihapus; hanya dapat diubah dengan alasan dan persetujuan.
3. Tinjauan menghasilkan rekaman: tidak berubah, direvisi, ditangguhkan, atau dicabut.
4. Peristiwa material dapat memicu tinjauan lebih awal.

## 3. Kalender Pengembangan 2026
| Periode/Pemicu | Objek | Kegiatan | Pemilik | Keluaran |
|---|---|---|---|---|
| Mingguan selama PR #1 Draft | Dokumen governance | Audit metadata, rujukan silang, istilah, status | Document Controller | Register dokumen diperbarui |
| Setiap Jumat selama Governance Freeze preparation | Temuan dan CAPA | Review keterlambatan dan efektivitas | QA Lead | Status AUD/CAPA terbaru |
| Akhir setiap bulan | Risk Register | Review risiko tinggi/kritis | Risk Owner | Nilai residual dan mitigasi |
| Sebelum PR Ready for Review | QC-000–QC-012 | Audit konstitusional penuh | Governance Lead | CHK-GOV-001 lengkap |
| Sebelum ratifikasi Governance v1.0 | Seluruh governance toolkit | Stage-gate dan keputusan freeze | Pimpinan QURBATA | Decision-ID ratifikasi |
| Sebelum Curriculum Freeze | Ontologi, competency graph, Knowledge-ID | Validasi kelengkapan dan prasyarat | Curriculum & Knowledge Leads | Baseline kurikulum |
| Sebelum Book Jilid 1 Freeze | Halaman, latihan, asesmen | Audit pedagogis dan keterlacakan | Curriculum/QA Leads | Persetujuan buku |
| Sebelum pilot peserta didik | Safeguarding, data, operasional | Simulasi respons dan uji akses | Safeguarding/Data Leads | Bukti kesiapan pilot |
| Setelah pilot | Data hasil belajar dan insiden | Evaluasi efektivitas | Research & QA Leads | Keputusan revisi |

## 4. Siklus Setelah Sistem Efektif
| Frekuensi | Objek |
|---|---|
| Bulanan | Risiko tinggi/kritis, CAPA terbuka, insiden, safeguarding |
| Triwulanan | Audit sampel dokumen, akses sistem, kualitas data, asesmen |
| Semesteran | Kurikulum, buku, hasil belajar, beban guru, pengalaman peserta |
| Tahunan | QC-000–QC-012, RACI, kebijakan data, BCP/DR, lisensi aset |
| Tiga tahunan | Tinjauan arsitektur konstitusional dan strategi sistem |

## 5. Pemicu Tinjauan Luar Jadwal
- perubahan hukum atau standar;
- insiden keselamatan/privasi;
- temuan audit kritis;
- perubahan struktur organisasi;
- perubahan kurikulum mayor;
- kegagalan hasil belajar yang signifikan;
- teknologi atau format distribusi baru;
- keluhan sistemik;
- perubahan lisensi atau kepemilikan aset.

## 6. Data Wajib RIQA OS
`review_id`, `object_id`, `review_type`, `planned_at`, `trigger`, `owner`, `participants`, `status`, `result`, `decision_id`, `next_review_at`, `evidence_links`, `overdue_days`.

## 7. Eskalasi Keterlambatan
- lewat 7 hari: peringatan pemilik;
- lewat 14 hari: eskalasi Governance/QA Lead;
- lewat 30 hari: masuk Audit Finding dan Risk Register;
- dokumen kritis lewat review dapat ditangguhkan penggunaannya.

## 8. Catatan Perubahan
| Versi | Tanggal | Perubahan |
|---|---|---|
| 0.1.0 | 2026-07-26 | Kalender tinjauan awal dibuat |

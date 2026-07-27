# REG-GOV-007 — Register Tindakan Korektif dan Pencegahan QURBATA

**Kode Dokumen:** REG-GOV-007  
**Judul:** Register Tindakan Korektif dan Pencegahan QURBATA  
**Bahasa Induk:** Bahasa Indonesia  
**Status:** Draf Terkendali  
**Versi:** 0.5.0-id  
**Pemilik Dokumen:** Fungsi Tata Kelola QURBATA  
**Otoritas Persetujuan:** Pendiri dan Peneliti Utama/Dewan Konstitusi setelah aktif  
**Tanggal Berlaku:** Setelah persetujuan sesuai kewenangan  
**Tinjauan Berikutnya:** Tahunan atau ketika terdapat perubahan material  
**Klasifikasi Akses:** Internal; ringkasan dapat dipublikasikan  
**Induk Normatif:** QC-000 — Konstitusi QURBATA  
**Dokumen Pengendali:** QC-001, QC-003, QC-004, QC-006, dan QC-007  


## 1. Tujuan
Register CAPA ini memastikan setiap ketidaksesuaian, insiden, keluhan, temuan audit, atau risiko berulang ditangani sampai akar masalah dan efektivitas perbaikannya terbukti.

## 2. Jenis Tindakan
- **Koreksi:** memperbaiki masalah yang sedang terjadi.
- **Tindakan korektif:** menghilangkan akar penyebab agar tidak berulang.
- **Tindakan pencegahan:** mengurangi kemungkinan masalah serupa pada area lain.
- **Pengendalian sementara:** membatasi dampak sebelum solusi permanen diterapkan.

## 3. Metode Analisis Akar Masalah
Gunakan salah satu atau kombinasi:
- 5 Why;
- fishbone;
- fault tree;
- analisis proses;
- analisis prasyarat pembelajaran;
- analisis data kesalahan peserta/guru/sistem.

Kesimpulan “human error” tidak diterima tanpa pemeriksaan desain proses, instruksi, beban kerja, pelatihan, akses, dan kontrol sistem.

## 4. Register Awal
| CAPA-ID | Sumber | Masalah | Akar Masalah Awal | Tindakan | Pemilik | Tenggat | Verifikator | Status |
|---|---|---|---|---|---|---|---|---|
| CAPA-2026-001 | AUD-2026-001 | Metadata governance tidak seragam | Belum ada register dokumen tunggal | REG-GOV-004 diterapkan dan metadata 13/13 QC diaudit | Document Controller | 27 Juli 2026 | QA Lead independen | Menunggu Verifikasi |
| CAPA-2026-002 | AUD-2026-002 | Ketidakharmonisan bahasa | Terjemahan berkembang sebelum master stabil | Harmonisasikan terjemahan per pasal setelah baseline Indonesia stabil | Translation Lead | Sebelum publikasi terjemahan resmi | Governance Lead | Terbuka; Non-blocking untuk Ready for Review |
| CAPA-2026-003 | AUD-2026-003 | Knowledge-ID objek isi belum lengkap | Ontologi dan domain kurikulum belum dibekukan | Selesaikan ontologi baseline dan validasi ID yatim/ganda | Knowledge Architect | Sebelum Curriculum Freeze | QA Lead | Terbuka; Non-blocking untuk Governance Freeze |
| CAPA-2026-004 | AUD-2026-004 | Safeguarding belum diuji | Instrumen operasional belum dipilotkan | Kanal, 2FA, penerimaan, eskalasi, target respons, dan Case-ID diuji; lanjutkan audit efektivitas berkala | Safeguarding Lead | 27 Juli 2026 | Pimpinan QURBATA | Ditutup |


| CAPA-2026-006 | AUD-2026-006 | Tutup atau putuskan risiko seluruh temuan mayor | Governance/QA Lead | Sebelum freeze | OPEN |
| CAPA-2026-007 | AUD-2026-007 | Penelaah independen ditunjuk, telaah dicatat, dan register keberatan dibuka | Governance Lead | 27 Juli 2026 | CLOSED |
| CAPA-2026-008 | AUD-2026-008 | Tetapkan baseline final, Decision-ID, tanggal efektif, dan transisi | Otoritas Konstitusional | Setelah gate lain PASS | OPEN |
| CAPA-2026-009 | AUD-2026-009 | Pengganti SAFE dan DOC telah ditetapkan; lengkapi kompetensi peran lain, kontrol pemisahan tugas, dan uji akses RACI | Governance Lead | Sebelum implementasi | IN-PROGRESS |
| CAPA-2026-010 | AUD-2026-010 | Lengkapi dan validasi Evidence-ID untuk CTM, risiko, CAPA, safeguarding, dan RIQA OS | QA Lead | Sebelum freeze | OPEN |

## 5. Data Wajib
`capa_id`, `source_type`, `source_id`, `problem`, `containment`, `root_cause`, `corrective_action`, `preventive_action`, `owner`, `due_date`, `evidence`, `verifier`, `effectiveness_method`, `effectiveness_result`, `status`, `closed_at`.

## 6. Uji Efektivitas
Efektivitas dinilai melalui salah satu atau lebih cara:
1. audit ulang;
2. pengukuran penurunan kesalahan;
3. uji pengguna/pilot;
4. simulasi insiden;
5. pemeriksaan sampel dokumen;
6. validasi otomatis pada RIQA OS;
7. tidak berulang dalam periode yang ditetapkan.

## 7. Eskalasi
- CAPA kritis yang terlambat harus otomatis dieskalasikan kepada Pimpinan.
- CAPA mayor yang terlambat lebih dari 7 hari harus masuk Risk Register.
- Perpanjangan tenggat harus memiliki alasan, risiko residual, dan persetujuan.
- Pemilik tindakan tidak boleh menjadi satu-satunya verifikator.

## 8. Penutupan
CAPA ditutup hanya setelah bukti, verifikasi independen, dan hasil uji efektivitas tercatat. Penutupan administratif tanpa uji efektivitas dilarang.

## 9. Catatan Perubahan
| Versi | Tanggal | Perubahan |
|---|---|---|
| 0.1.0 | 2026-07-26 | Register CAPA awal dibuat |
| 0.3.0-id | 2026-07-27 | Menyelaraskan CAPA bahasa, safeguarding, dan telaah independen dengan keputusan ruang lingkup serta bukti terbaru |
| 0.4.0-id | 2026-07-27 | Memperbarui CAPA RACI berdasarkan penetapan pengganti SAFE dan DOC |
| 0.5.0-id | 2026-07-27 | Memindahkan CAPA metadata ke Menunggu Verifikasi dan memperjelas CAPA objek isi sebagai non-blocking governance |

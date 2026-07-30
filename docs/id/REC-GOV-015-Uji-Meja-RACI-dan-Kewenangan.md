# REC-GOV-015 — Uji Meja RACI dan Kewenangan Governance v1.0

**Record-ID:** REC-GOV-015  
**Tanggal:** 27 Juli 2026  
**Metode:** Desk test berbasis QC-006, QC-007, QC-008, MAT-GOV-001, dan register governance  
**Ruang Lingkup:** Konsistensi peran, akuntabilitas, quorum, delegasi, konflik kepentingan, dan ratifikasi  
**Batas:** Uji ini tidak membuktikan konfigurasi hak akses RIQA OS atau kompetensi profesional di luar bukti yang tersedia.

## Hasil Uji

| Skenario | R | A | Kontrol wajib | Hasil |
|---|---|---|---|---|
| Perubahan QC-000 | Document Controller | Otoritas Konstitusional | Telaah independen, analisis dampak, quorum, ratifikasi | PASS |
| Penerbitan dokumen efektif | Document Controller | Otoritas Konstitusional | Metadata, bukti persetujuan, versi, tanggal efektif | PASS |
| Konflik kepentingan pengambil keputusan | Pemilik proses/Ethics function | Otoritas yang tidak berkonflik | Pengungkapan, recusal, pengganti, audit trail | PASS |
| Laporan safeguarding | Safeguarding Lead | Safeguarding Lead sesuai batas mandat | Kerahasiaan, Case-ID, eskalasi, pengganti Ulifah | PASS |
| Penutupan CAPA | Pemilik tindakan dan QA | Otoritas tata kelola | Pelaksana tidak menjadi satu-satunya verifikator | PASS |
| Penerimaan risiko residual | Pemilik risiko | Otoritas Konstitusional | Pemilik risiko tidak menerima sendiri risiko kritis | PASS |
| Ketidakhadiran Document Controller | Izathy Khoirina melalui delegasi tercatat | Otoritas Konstitusional | Mandat terbatas, konflik diperiksa, jejak delegasi | PASS |
| Governance Freeze | Governance/QA Lead | Otoritas Konstitusional | Seluruh gate kritis PASS, baseline hash, Decision-ID | PASS |

## Quorum dan Ratifikasi

QC-007 menetapkan bahwa quorum mengikuti ketentuan organ; selama belum ditetapkan, quorum sementara adalah lebih dari setengah anggota aktif. Keputusan material tetap memerlukan pencatatan pihak hadir, konflik, dasar, hasil, dan ratifikasi sesuai kewenangan. Tidak ditemukan konflik antara ketentuan tersebut dan MAT-GOV-001.

## Kesimpulan

Delapan skenario tata kelola dapat ditelusuri kepada peran Responsible dan Accountable, kontrol pemisahan tugas, mekanisme pengganti, quorum, dan ratifikasi. Desain kewenangan konsisten untuk Governance v1.0.

Kekurangan bukti kompetensi beberapa peran dan implementasi hak akses RIQA OS tetap dicatat sebagai tindak lanjut implementasi, tetapi tidak mengubah hasil uji konsistensi desain kewenangan GF-07.

## Hubungan

- Evidence-ID: EVD-GOV-000018
- Gate: GF-07
- Finding-ID: AUD-2026-009
- Assignment terkait: ASN-GOV-001–ASN-GOV-007

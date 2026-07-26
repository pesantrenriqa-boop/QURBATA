# REG-GOV-006 — Register Temuan Audit QURBATA

**Kode Dokumen:** REG-GOV-006  
**Judul:** Register Temuan Audit QURBATA  
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
Register ini mencatat seluruh temuan audit tata kelola, kurikulum, buku, asesmen, data, teknologi, operasional, dan perlindungan peserta didik.

## 2. Klasifikasi Temuan
| Tingkat | Definisi | Batas Respons |
|---|---|---|
| Kritis | Risiko langsung terhadap keselamatan, legalitas, integritas data, atau validitas sistem | Segera; pengendalian sementara maksimal 24 jam |
| Mayor | Kegagalan sistemik atau ketidakpatuhan material | Rencana tindakan maksimal 7 hari |
| Minor | Ketidaksesuaian terbatas yang tidak bersifat sistemik | Rencana tindakan maksimal 30 hari |
| Observasi | Peluang peningkatan tanpa ketidaksesuaian langsung | Ditinjau pada siklus perbaikan berikutnya |

## 3. Status Temuan
`Terbuka` → `Dalam Analisis` → `Tindakan Disetujui` → `Dalam Pelaksanaan` → `Menunggu Verifikasi` → `Ditutup`.

Status tambahan: `Ditangguhkan dengan Risiko Diterima`, hanya dengan keputusan berwenang.

## 4. Register Awal
| Finding-ID | Area | Referensi | Tingkat | Temuan | Pemilik | Tenggat | Status |
|---|---|---|---|---|---|---|---|
| AUD-2026-001 | Governance | QC-000–QC-012 | Mayor | Metadata versi, tanggal berlaku, dan review belum seragam pada seluruh dokumen | Document Controller | Sebelum Governance Freeze | Terbuka |
| AUD-2026-002 | Bahasa | QC-000 | Mayor | Naskah Inggris belum sepenuhnya harmonis dengan master Indonesia | Translation Lead | Sebelum keluar dari Draft | Terbuka |
| AUD-2026-003 | Knowledge-ID | REG-GOV-001 | Mayor | Register awal belum mencakup seluruh objek kurikulum dan buku | Knowledge Architect | Sebelum Curriculum Freeze | Terbuka |
| AUD-2026-004 | Safeguarding | QC-012 | Mayor | Bukti implementasi dan kanal respons belum diuji operasional | Safeguarding Lead | Sebelum pilot peserta didik | Terbuka |
| AUD-2026-005 | Keterlacakan | QC-004/CTM | Minor | Sejumlah persyaratan belum memiliki bukti dan pemilik final | QA Lead | Sebelum ratifikasi | Terbuka |

## 5. Data Wajib
- Finding-ID;
- tanggal dan jenis audit;
- auditor dan ruang lingkup;
- kriteria audit;
- bukti objektif;
- uraian ketidaksesuaian;
- tingkat temuan;
- risiko;
- pemilik;
- tindakan sementara;
- CAPA-ID;
- tenggat;
- hasil verifikasi;
- keputusan penutupan.

## 6. Aturan Penutupan
Temuan hanya boleh ditutup apabila:
1. akar masalah telah dianalisis;
2. tindakan korektif telah selesai;
3. bukti implementasi tersedia;
4. efektivitas telah diverifikasi oleh pihak yang tidak melaksanakan tindakan;
5. tidak ada dampak turunan yang belum ditangani.

## 7. Integrasi RIQA OS
RIQA OS harus menyediakan pengingat tenggat, eskalasi temuan kritis/mayor, relasi ke CAPA dan Risk-ID, lampiran bukti, serta histori yang tidak dapat dihapus tanpa jejak audit.

## 8. Catatan Perubahan
| Versi | Tanggal | Perubahan |
|---|---|---|
| 0.1.0 | 2026-07-26 | Register temuan audit awal dibuat |

# REG-GOV-006 — Register Temuan Audit QURBATA

**Kode Dokumen:** REG-GOV-006  
**Judul:** Register Temuan Audit QURBATA  
**Bahasa Induk:** Bahasa Indonesia  
**Status:** Draf Terkendali  
**Versi:** 0.7.0-id  
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
| AUD-2026-001 | Governance | QC-000–QC-012 | Minor | Metadata minimum 13/13 dokumen dan versi register telah diselaraskan; validasi editorial independen masih diperlukan | Document Controller | Sebelum Governance Freeze | Menunggu Verifikasi |
| AUD-2026-002 | Bahasa | Terjemahan QC-000 | Minor | Naskah Inggris belum sepenuhnya harmonis dengan master Indonesia; tidak termasuk baseline Governance v1.0 Bahasa Indonesia | Translation Lead | Sebelum publikasi terjemahan resmi | Terbuka; Non-blocking untuk Ready for Review |
| AUD-2026-003 | Knowledge-ID | REG-GOV-001 | Minor | Register objek kurikulum dan buku belum dipopulasi; tidak termasuk baseline Governance v1.0 | Knowledge Architect | Sebelum Curriculum Freeze | Terbuka; Non-blocking untuk Governance Freeze |
| AUD-2026-004 | Safeguarding | QC-012 | Mayor | Uji awal kanal, 2FA, penerimaan email, eskalasi WhatsApp, target respons, dan Case-ID telah dilaksanakan | Safeguarding Lead | 27 Juli 2026 | Ditutup; audit efektivitas berkala tetap wajib |
| AUD-2026-005 | Keterlacakan | QC-004/CTM | Minor | Sejumlah persyaratan belum memiliki bukti dan pemilik final | QA Lead | Sebelum ratifikasi | Terbuka |
| AUD-2026-006 | Governance Freeze | REG-GOV-011 | Mayor | Temuan mayor terbuka menghalangi GF-10 | QA Lead | Sebelum Governance Freeze | Terbuka |
| AUD-2026-007 | Review | QC-000/REG-GOV-011/REG-GOV-012 | Mayor | Telaah independen dan register keberatan material telah tersedia melalui REC-GOV-001–REC-GOV-004 | Governance Lead | 27 Juli 2026 | Ditutup |
| AUD-2026-008 | Ratifikasi | QC-007/REG-GOV-011 | Mayor | Baseline final, Decision-ID, tanggal efektif, dan transisi belum ditetapkan | Otoritas Konstitusional | Sebelum Governance Freeze | Terbuka |
| AUD-2026-009 | RACI | MAT-GOV-001/REC-GOV-015 | Minor | Pengganti SAFE dan DOC telah ditetapkan dan uji meja delapan skenario PASS; bukti kompetensi beberapa peran dan uji akses RIQA OS tetap diperlukan sebelum implementasi produksi | Governance Lead | Sebelum implementasi produksi | Dalam Pelaksanaan; Non-blocking untuk Governance Freeze |
| AUD-2026-010 | Bukti | CTM/CHK-GOV-001 | Minor | Bukti implementasi belum lengkap pada CTM, risiko, CAPA, safeguarding, dan RIQA OS | QA Lead | Sebelum Governance Freeze | Terbuka |

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
| 0.2.0-id | 2026-07-26 | Metadata kendali dan temuan audit kesiapan freeze ditambahkan |
| 0.3.0-id | 2026-07-27 | Terjemahan dipindahkan menjadi tindak lanjut non-blocking; temuan safeguarding dan telaah independen diselaraskan dengan bukti |
| 0.4.0-id | 2026-07-27 | Menyelaraskan temuan RACI dengan penetapan Ulifah dan Izathy Khoirina serta menyisakan verifikasi yang benar-benar belum selesai |
| 0.5.0-id | 2026-07-27 | Mencatat penyelarasan versi dan terminologi serta mempersempit sisa temuan metadata/editorial |
| 0.6.0-id | 2026-07-27 | Memvalidasi metadata 13/13 dokumen dan memisahkan populasi objek kurikulum/buku dari baseline Governance v1.0 |
| 0.7.0-id | 2026-07-27 | Mencatat uji meja RACI yang lulus dan memisahkan uji akses RIQA OS sebagai tindak lanjut implementasi |

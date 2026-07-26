# REG-GOV-003 — Register Keputusan Tata Kelola QURBATA

**Kode Dokumen:** REG-GOV-003  
**Status:** Draf Terkendali  
**Versi:** 0.1.0-id  
**Bahasa Induk:** Bahasa Indonesia  
**Induk Normatif:** QC-000, QC-006, QC-007, QC-008

## 1. Tujuan

Register ini mencatat keputusan material QURBATA agar alasan, kewenangan, bukti, dampak, pelaksana, dan riwayat perubahan dapat ditelusuri.

## 2. Format ID Keputusan

```text
DEC-[DOMAIN]-[NNN]
```

Contoh: `DEC-GOV-001`, `DEC-CUR-001`, `DEC-OS-001`, `DEC-RSK-001`.

## 3. Klasifikasi Keputusan

| Kelas | Contoh | Otoritas Minimum |
|---|---|---|
| Konstitusional | Perubahan QC-000 | Ratifikasi tertinggi sesuai QC-007 |
| Strategis | Ruang lingkup produk, arah lembaga | Pimpinan berwenang |
| Akademik | Urutan kurikulum, standar kelulusan | Pemilik akademik dan QA |
| Operasional | Proses kerja, SOP, jadwal | Pemilik proses |
| Teknologi/Data | Arsitektur, skema data, keamanan | Pemilik sistem dan otoritas data |
| Risiko/Insiden | Penerimaan risiko, pemulihan | Pemilik risiko dan otoritas terkait |

## 4. Metadata Wajib

- Decision-ID;
- judul keputusan;
- kelas dan domain;
- tanggal keputusan;
- pemohon;
- pengambil keputusan;
- pihak yang dikonsultasikan;
- konflik kepentingan yang dinyatakan;
- masalah yang hendak diselesaikan;
- pilihan yang dipertimbangkan;
- keputusan akhir dan alasan;
- dasar normatif dan Evidence-ID;
- dampak terhadap dokumen, kurikulum, data, sistem, biaya, dan perlindungan peserta didik;
- pemilik implementasi;
- tenggat;
- status implementasi;
- tanggal review;
- keputusan yang digantikan atau terkait.

## 5. Status Keputusan

`PROPOSED`, `UNDER-REVIEW`, `APPROVED`, `RATIFIED`, `IMPLEMENTING`, `IMPLEMENTED`, `SUSPENDED`, `SUPERSEDED`, `REVOKED`, `ARCHIVED`.

## 6. Register Awal

| Decision-ID | Keputusan | Status | Dasar | Dampak Utama |
|---|---|---|---|---|
| DEC-GOV-001 | Bahasa Indonesia ditetapkan sebagai bahasa induk normatif QURBATA | APPROVED-DRAFT | QC-000, QC-002 | Terjemahan tidak mengendalikan sebelum harmonisasi |
| DEC-GOV-002 | QC-000 menjadi norma tertinggi dan QC-001–QC-012 menjadi dokumen turunan | APPROVED-DRAFT | QC-000, QC-001 | Menetapkan hierarki tata kelola |
| DEC-GOV-003 | Knowledge-ID digunakan untuk objek pengetahuan dan keterlacakan | APPROVED-DRAFT | QC-002, QC-004, REG-GOV-001 | Dasar integrasi RIQA OS |
| DEC-GOV-004 | Governance v1.0 dibekukan setelah audit final dan kriteria keluar draf terpenuhi | PROPOSED | QC-003, README Governance | Mencegah perluasan governance tanpa batas |
| DEC-PRD-001 | Buku QURBATA tetap menjadi produk utama tahap pertama | APPROVED-DRAFT | Arah proyek QURBATA | Turunan digital mengikuti setelah struktur dan isi buku stabil |
| DEC-DAT-001 | Master data menjadi sumber tunggal bagi buku dan keluaran turunannya | APPROVED-DRAFT | QC-004, arsitektur produk | Mengurangi duplikasi dan inkonsistensi |

## 7. Aturan Pengendalian

1. Keputusan material tidak boleh hanya tersimpan dalam percakapan, pesan pribadi, atau ingatan individu.
2. Keputusan yang mengubah norma harus diikuti revisi dokumen normatif terkait.
3. Keputusan yang memengaruhi peserta didik wajib melalui pemeriksaan safeguarding.
4. Keputusan yang menimbulkan risiko residual wajib menyatakan penerima risiko.
5. Keputusan tidak boleh dihapus; koreksi dilakukan melalui keputusan pengganti atau pencabutan.
6. Konflik kepentingan wajib dicatat sebelum persetujuan.

## 8. Integrasi RIQA OS

Objek minimum: Decision, DecisionOption, DecisionAuthority, ConflictDeclaration, EvidenceLink, ImpactAssessment, ImplementationAction, Review, dan Supersession. Sistem harus menolak status APPROVED apabila otoritas, alasan, atau bukti wajib belum lengkap.

# REG-GOV-013 — Register Bukti Governance QURBATA

**Kode Dokumen:** REG-GOV-013  
**Judul:** Register Bukti Governance QURBATA  
**Bahasa Induk:** Bahasa Indonesia  
**Status:** Draf Terkendali  
**Versi:** 0.1.0-id  
**Pemilik Dokumen:** Fungsi Penjaminan Mutu QURBATA  
**Otoritas Persetujuan:** Pendiri dan Peneliti Utama/Dewan Konstitusi setelah aktif  
**Tanggal Berlaku:** Setelah persetujuan sesuai kewenangan  
**Tinjauan Berikutnya:** Pada setiap audit, gate, atau perubahan material  
**Klasifikasi Akses:** Internal  
**Induk Normatif:** QC-000 — Konstitusi QURBATA

## 1. Tujuan

Register ini menjadi sumber tunggal Evidence-ID untuk mendukung atau membantah klaim kepatuhan, keputusan, gate, temuan, risiko, CAPA, dan hasil audit.

## 2. Aturan

1. Keberadaan file tidak otomatis menjadi bukti kecukupan atau efektivitas.
2. Bukti harus relevan, dapat diperiksa, mempunyai pemilik, sumber, tanggal, versi, klasifikasi, dan status validasi.
3. Satu bukti dapat mendukung beberapa objek; hubungan dicatat eksplisit.
4. Bukti yang kedaluwarsa, berubah, atau ditolak tetap dipertahankan dalam audit trail.
5. Validator tidak boleh memvalidasi bukti buatannya sendiri untuk gate berisiko tinggi.

## 3. Status

PROPOSED, COLLECTED, UNDER-VALIDATION, VALID, REJECTED, EXPIRED, SUPERSEDED, dan RETIRED.

## 4. Register Awal

| Evidence-ID | Objek | Sumber | Status | Pemilik | Validator |
|---|---|---|---|---|---|
| EVD-AUD-000001 | Audit tautan 28 Markdown | AUD-GOV-001 | UNDER-VALIDATION | QA Lead | Penelaah independen belum ditetapkan |
| EVD-AUD-000002 | Kelengkapan substantif QC-000 | QC-000 v0.5.0-id | UNDER-VALIDATION | Pemilik QC-000 | Penelaah independen belum ditetapkan |
| EVD-AUD-000003 | Metadata QC-000–QC-012 | Repository PR #1 | UNDER-VALIDATION | Document Controller | Penelaah independen belum ditetapkan |
| EVD-AUD-000004 | Checklist 44 butir | CHK-GOV-001 | COLLECTED | QA Lead | Belum ditetapkan |
| EVD-AUD-000005 | Matriks RACI | MAT-GOV-001 | COLLECTED | Governance Lead | Belum ditetapkan |
| EVD-AUD-000006 | Model Knowledge-ID dan CTM | QC-004/QC-005/REG-GOV-001/CTM | UNDER-VALIDATION | Knowledge Architect | Belum ditetapkan |
| EVD-AUD-000007 | Temuan mayor terbuka | REG-GOV-006 | VALID | QA Lead | Audit internal awal |
| EVD-AUD-000008 | Ketiadaan keputusan freeze | REG-GOV-011 | VALID | Sekretariat Tata Kelola | Audit internal awal |
| EVD-AUD-000009 | Norma safeguarding/pengaduan | QC-009/QC-012 | COLLECTED | Safeguarding Lead | Belum ditetapkan |
| EVD-AUD-000010 | Register risiko dan CAPA | REG-GOV-007/REG-GOV-008 | COLLECTED | Risk/QA Lead | Belum ditetapkan |
| EVD-GOV-000001 | Pernyataan independensi Arif Nasruddin | REC-GOV-001 | COLLECTED | Sekretariat Tata Kelola | Memerlukan pemeriksaan formal/tanda tangan |
| EVD-GOV-000002 | Hasil telaah independen awal QC-001–QC-012 | REC-GOV-002 | COLLECTED | Sekretariat Tata Kelola | Pernyataan penelaah |
| EVD-GOV-000003 | Konfirmasi tidak ada keberatan material | REC-GOV-003 | VALID | Sekretariat Tata Kelola | Konfirmasi penelaah independen |

## 5. Data Minimum

Evidence-ID, judul, jenis, objek didukung, objek dibantah, sumber, lokasi, versi/hash, tanggal, periode berlaku, pemilik, klasifikasi, validator, metode validasi, hasil, keterbatasan, status, dan supersesi.

## 6. Integrasi RIQA OS

RIQA OS mencegah gate PASS bila Evidence-ID wajib tidak berstatus VALID, telah kedaluwarsa, konflik dengan bukti lain yang belum diselesaikan, atau divalidasi oleh pihak yang tidak independen ketika independensi diwajibkan.

## 7. Riwayat Perubahan

| Versi | Tanggal | Ringkasan |
|---|---|---|
| 0.1.0-id | 26 Juli 2026 | Register bukti awal untuk AUD-GOV-001 |

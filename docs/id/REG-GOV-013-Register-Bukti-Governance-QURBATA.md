# REG-GOV-013 — Register Bukti Governance QURBATA

**Kode Dokumen:** REG-GOV-013  
**Judul:** Register Bukti Governance QURBATA  
**Bahasa Induk:** Bahasa Indonesia  
**Status:** Draf Terkendali  
**Versi:** 0.15.0-id  
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
| EVD-AUD-000002 | Kelengkapan substantif QC-000 | QC-000 v0.5.0-id | VALID | Pemilik QC-000 | Arif Nasruddin; REC-GOV-004 |
| EVD-AUD-000003 | Metadata QC-000–QC-012 | Repository PR #1 | UNDER-VALIDATION | Document Controller | Penelaah independen belum ditetapkan |
| EVD-AUD-000004 | Checklist 44 butir | CHK-GOV-001 | COLLECTED | QA Lead | Belum ditetapkan |
| EVD-AUD-000005 | Matriks RACI | MAT-GOV-001 | COLLECTED | Governance Lead | Belum ditetapkan |
| EVD-AUD-000006 | Model Knowledge-ID dan CTM | QC-004/QC-005/REG-GOV-001/CTM | UNDER-VALIDATION | Knowledge Architect | Belum ditetapkan |
| EVD-AUD-000007 | Temuan mayor terbuka | REG-GOV-006 | VALID | QA Lead | Audit internal awal |
| EVD-AUD-000008 | Ketiadaan keputusan freeze | REG-GOV-011 | VALID | Sekretariat Tata Kelola | Audit internal awal |
| EVD-AUD-000009 | Norma dan kesiapan operasional awal safeguarding/pengaduan | QC-009/QC-012/REC-GOV-005–REC-GOV-012 | VALID | Safeguarding Lead | Kanal, 2FA, penerimaan, eskalasi, target respons, dan Case-ID tersedia; audit berkala tetap wajib |
| EVD-AUD-000010 | Register risiko dan CAPA | REG-GOV-007/REG-GOV-008 | COLLECTED | Risk/QA Lead | Belum ditetapkan |
| EVD-GOV-000001 | Pernyataan independensi Arif Nasruddin | REC-GOV-001 | COLLECTED | Sekretariat Tata Kelola | Memerlukan pemeriksaan formal/tanda tangan |
| EVD-GOV-000002 | Hasil telaah independen awal QC-001–QC-012 | REC-GOV-002 | COLLECTED | Sekretariat Tata Kelola | Pernyataan penelaah |
| EVD-GOV-000003 | Konfirmasi tidak ada keberatan material | REC-GOV-003 | VALID | Sekretariat Tata Kelola | Konfirmasi penelaah independen |
| EVD-GOV-000004 | Validasi substantif awal QC-000 | REC-GOV-004 | VALID | Pemilik QC-000 | Arif Nasruddin |
| EVD-GOV-000005 | Penerimaan mandat Safeguarding Lead dan deklarasi tidak ada kasus terbuka | REC-GOV-005 | VALID | Ainul Yakin | Pernyataan langsung; efektivitas operasional belum diuji |
| EVD-GOV-000006 | Kanal safeguarding safeguardingqurbata@gmail.com dan Aris Liswanto sebagai pemegang akses awal | REC-GOV-006–REC-GOV-012 | VALID | Aris Liswanto | Kanal, 2FA, penerimaan, eskalasi, target respons, dan Case-ID tersedia; efektivitas berkelanjutan perlu diaudit |
| EVD-GOV-000007 | Aktivasi autentikasi dua faktor kanal safeguarding | REC-GOV-007 | VALID | Aris Liswanto | Konfirmasi langsung pemegang akses; rahasia autentikasi tidak dicatat |
| EVD-GOV-000008 | Uji penerimaan email kanal safeguarding | REC-GOV-008 | VALID | Aris Liswanto | Pesan uji diterima; tidak memuat kasus nyata atau identitas santri |
| EVD-GOV-000009 | Penetapan WhatsApp sebagai jalur eskalasi kepada Ainul Yakin | REC-GOV-009/REC-GOV-010 | VALID | Aris Liswanto | Pesan diterima dan kesiapan tindak lanjut dikonfirmasi Ainul Yakin |
| EVD-GOV-000010 | Uji eskalasi WhatsApp kepada Safeguarding Lead | REC-GOV-010 | VALID | Ainul Yakin | Konfirmasi langsung penerima; tanpa kasus nyata atau data santri |
| EVD-GOV-000011 | Target waktu respons safeguarding | REC-GOV-011 | VALID | Ainul Yakin | Disetujui Aris Liswanto; efektivitas waktu aktual belum diuji |
| EVD-GOV-000012 | Format nomor perkara safeguarding | REC-GOV-012 | VALID | Aris Liswanto | Format disetujui; identitas santri dilarang dalam Case-ID dan subjek email |
| EVD-GOV-000013 | Penunjukan, penerimaan mandat, dan deklarasi konflik Ulifah sebagai pengganti Safeguarding Lead | REC-GOV-013 | VALID | Aris Liswanto | Tidak ada konflik umum yang dinyatakan; konflik wajib diperiksa dan diungkap per perkara |
| EVD-GOV-000014 | Penunjukan, penerimaan mandat, dan deklarasi konflik Izathy Khoirina sebagai pengganti Document Controller | REC-GOV-014 | VALID | Aris Liswanto | Mandat, kerahasiaan, kontrol versi, metadata, arsip, audit trail, dan deklarasi konflik dikonfirmasi |

## 5. Data Minimum

Evidence-ID, judul, jenis, objek didukung, objek dibantah, sumber, lokasi, versi/hash, tanggal, periode berlaku, pemilik, klasifikasi, validator, metode validasi, hasil, keterbatasan, status, dan supersesi.

## 6. Integrasi RIQA OS

RIQA OS mencegah gate PASS bila Evidence-ID wajib tidak berstatus VALID, telah kedaluwarsa, konflik dengan bukti lain yang belum diselesaikan, atau divalidasi oleh pihak yang tidak independen ketika independensi diwajibkan.

## 7. Riwayat Perubahan

| Versi | Tanggal | Ringkasan |
|---|---|---|
| 0.1.0-id | 26 Juli 2026 | Register bukti awal untuk AUD-GOV-001 |
| 0.2.0-id | 27 Juli 2026 | Menambahkan EVD-GOV-000005 dan memperjelas batas validasi bukti safeguarding |
| 0.3.0-id | 27 Juli 2026 | Menambahkan EVD-GOV-000006 untuk penetapan kanal awal pelaporan safeguarding |
| 0.4.0-id | 27 Juli 2026 | Mencatat alamat kanal safeguarding dan menaikkan bukti ke UNDER-VALIDATION |
| 0.5.0-id | 27 Juli 2026 | Mencatat aktivasi 2FA sebagai EVD-GOV-000007 dan menyisakan uji operasional kanal |
| 0.6.0-id | 27 Juli 2026 | Mencatat keberhasilan uji penerimaan sebagai EVD-GOV-000008 |
| 0.7.0-id | 27 Juli 2026 | Menetapkan jalur eskalasi WhatsApp sebagai EVD-GOV-000009 |
| 0.8.0-id | 27 Juli 2026 | Mencatat uji eskalasi WhatsApp yang lulus sebagai EVD-GOV-000010 |
| 0.9.0-id | 27 Juli 2026 | Menetapkan target waktu respons sebagai EVD-GOV-000011 |
| 0.10.0-id | 27 Juli 2026 | Menetapkan format Case-ID dan memvalidasi kesiapan operasional awal safeguarding |
| 0.11.0-id | 27 Juli 2026 | Mencatat penunjukan awal Ulifah sebagai pengganti Safeguarding Lead |
| 0.12.0-id | 27 Juli 2026 | Memvalidasi penerimaan mandat dan komitmen kerahasiaan Ulifah |
| 0.13.0-id | 27 Juli 2026 | Mencatat deklarasi tidak ada konflik umum dari Ulifah |
| 0.14.0-id | 27 Juli 2026 | Mencatat penunjukan awal Izathy Khoirina sebagai pengganti Document Controller |
| 0.15.0-id | 27 Juli 2026 | Memvalidasi penerimaan mandat dan kontrol Document Controller pengganti |

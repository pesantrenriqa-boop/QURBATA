# REG-ARB-004 — Master Siklus Pembelajaran Bahasa Arab

**Register-ID:** REG-ARB-004  
**Status:** DRAF TERKENDALI  
**Tanggal:** 28 Juli 2026  
**Cakupan:** QURBATA Jilid 1–8  
**Pengendali:** DEC-CUR-003, ACP-QUR-001, MAT-ARB-002, STD-ARB-002  
**Register terkait:** REG-ARB-001, REG-ARB-002, REG-ARB-003

## 1. Fungsi Register

REG-ARB-004 adalah sumber kendali Cycle-ID. Register ini menghubungkan tahap, inventaris prasyarat, paket pembelajaran, gerbang ketuntasan, Text-ID, Evidence-ID, retensi, dan status pemetaan halaman.

Register tidak menyatakan efektivitas dan tidak menggantikan review manusia. Status hanya boleh dinaikkan berdasarkan bukti yang memenuhi protokol validasi.

## 2. Status Siklus

| Urut | Cycle-ID | Stage | Paket kompetensi | Paket integrasi | Text-ID | Gate-Item | Status gerbang | Pemetaan halaman |
|---:|---|---|---|---|---|---:|---|---|
| 1 | AR-CYC-000001 | 1–3 | BAT-ARB-001 | BAT-ARB-005 | AR-TXT-000002 | 6 | GATE NOT RUN | UNMAPPED |
| 2 | AR-CYC-000002 | 4–6 | BAT-ARB-002 | BAT-ARB-006 | AR-TXT-000003 | 7 | GATE NOT RUN | UNMAPPED |
| 3 | AR-CYC-000003 | 7 | BAT-ARB-003 | BAT-ARB-004 | AR-TXT-000001 | 7 | GATE NOT RUN | UNMAPPED |

**Total siklus pilot:** 3.  
**Total Gate-Item:** 20.  
**Text-ID tersedia:** 3.  
**Siklus SIAP INTEGRASI:** 0.

## 3. Dependency Antar-Siklus

| Cycle-ID | Prasyarat siklus | Fokus perkembangan | Murojaah wajib |
|---|---|---|---|
| AR-CYC-000001 | kesiapan menyimak dan objek konkret | identifikasi dengan هٰذَا | lema konkret dan pola identifikasi |
| AR-CYC-000002 | AR-CYC-000001 minimal memiliki bukti prasyarat yang relevan | deskripsi, lokasi, idhafah | هٰذَا, isim lama, benda kelas, persona |
| AR-CYC-000003 | unsur relevan dari AR-CYC-000001–2 | tindakan kini dalam paragraf | isim, sifat, lokasi, pelaku, objek |

Siklus berikutnya tidak boleh menganggap semua materi siklus sebelumnya otomatis dikuasai. Hanya unsur yang memiliki Evidence-ID memadai yang boleh menjadi prasyarat aktif.

## 4. Slot Bukti

| Cycle-ID | Akuisisi | Pemantapan | Pola/kalimat | Gerbang | Transfer | Retensi |
|---|---|---|---|---|---|---|
| AR-CYC-000001 | AR-EVD-CYC01-A | AR-EVD-CYC01-B | AR-EVD-CYC01-D | AR-EVD-CYC01-GATE | AR-EVD-CYC01-TR | AR-EVD-CYC01-RET |
| AR-CYC-000002 | AR-EVD-CYC02-A | AR-EVD-CYC02-B | AR-EVD-CYC02-D | AR-EVD-CYC02-GATE | AR-EVD-CYC02-TR | AR-EVD-CYC02-RET |
| AR-CYC-000003 | AR-EVD-CYC03-A | AR-EVD-CYC03-B | AR-EVD-CYC03-D | AR-EVD-CYC03-GATE | AR-EVD-CYC03-TR | AR-EVD-CYC03-RET |

Semua ID pada tabel adalah slot calon. Slot kosong atau ID yang belum berisi artefak bukti tidak boleh dihitung sebagai bukti tersedia.

## 5. Aturan Perubahan Status

| Dari | Ke | Syarat minimum |
|---|---|---|
| GATE NOT RUN | BELUM SIAP | instrumen dijalankan dan prasyarat inti belum terpenuhi |
| GATE NOT RUN | BERKEMBANG | instrumen dijalankan dan bukti awal tersedia tetapi belum stabil |
| BELUM SIAP/BERKEMBANG | SIAP INTEGRASI | seluruh prasyarat Text-ID memiliki pola bukti memadai dan review wajib selesai |
| SIAP INTEGRASI | TERPELIHARA | transfer dan retensi tertunda terbukti |
| status apa pun | BLOCKED | ditemukan masalah bahasa, sumber, dependency, asesmen, aksesibilitas, atau safeguarding |

Satu jawaban benar, selesai halaman, atau terpenuhinya jumlah pertemuan tidak cukup untuk menaikkan status.

## 6. Kendali Pemetaan Buku

Cycle-ID belum sama dengan Page-ID. Pemetaan final hanya boleh dilakukan setelah:

- DEC-CUR-003 dan progression terkait mendapat otorisasi;
- dependency serta beban belajar ditelaah;
- kosa kata, vokalisasi, i‘rab, dan naturalitas disahkan;
- instrumen gerbang serta rubrik divalidasi;
- whitelist literasi halaman dipenuhi;
- jadwal murojaah dan retensi ditetapkan;
- safeguarding dan aksesibilitas ditelaah.

## 7. Temuan Terbuka

- jumlah pelajaran per siklus belum ditetapkan;
- ambang keputusan belum divalidasi;
- jadwal jeda retensi belum dipilih;
- bentuk bukti guru/peserta belum dibakukan;
- penempatan lisan versus tertulis belum dipetakan;
- seluruh tiga siklus masih GATE NOT RUN;
- tidak ada klaim kesiapan final atau efektivitas.

## 8. Riwayat

| Versi | Tanggal | Ringkasan |
|---|---|---|
| 0.1.0-id | 28 Juli 2026 | Register induk untuk tiga siklus pilot dan 20 Gate-Item |

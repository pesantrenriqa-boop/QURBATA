# DSP-VAL-QJ1-001 — Paket Pengiriman Validasi Ahli Jilid 1

**Dispatch-ID:** DSP-VAL-QJ1-001  
**Status:** READY-FOR-DISPATCH — BELUM ADA KEPUTUSAN AHLI  
**Tanggal:** 29 Juli 2026  
**Pemilik:** Document Controller QURBATA  
**Cakupan:** Tahfidz, Bahasa Arab, Qira’at, asesmen, safeguarding, dan editorial QURBATA Jilid 1  
**Keputusan arah:** DEC-CUR-004 dan DEC-CUR-005  
**Paket sumber:** REV-HAF-QJ1-001, VAL-ARB-001, REV-ARB-QJ1-002, REV-QJ1-001

## 1. Tujuan

Dokumen ini mengubah kumpulan draf validasi menjadi satu antrean pengiriman yang operasional. Paket ini tidak menggantikan keputusan ahli, tidak menerbitkan Evidence-ID, dan tidak mengaktifkan objek kurikulum.

## 2. Paket A — Ahli Al-Qur’an, Qira’at, Tajwid, dan Tahfidz

**Objek:** HAF-000001, HAF-000002, HAF-000003.  
**Kandidat yang telah disetujui pemilik untuk validasi:**

- Al-Fatihah ayat 1–3 untuk checkpoint P018;
- Al-Fatihah ayat 4–7 untuk checkpoint P036;
- integrasi dan retensi Al-Fatihah ayat 1–7 untuk fase akhir sampai P040.

**Dokumen wajib dikirim:**

1. DEC-CUR-004;
2. PROP-CUR-QJ1-001;
3. MAP-HAF-QJ1-001;
4. REV-HAF-QJ1-001;
5. RUB-HAF-QJ1-001;
6. FRM-HAF-QJ1-001;
7. QJ1-P018, QJ1-P036, dan QJ1-P040.

**Keputusan yang diminta:** sumber master, rasm, riwayat/qiraah, harakat, tajwid, makhraj, waqaf-ibtida’, pembagian potongan talqin, beban, model bacaan, rubrik, dan kelayakan pilot.

## 3. Paket B — Ahli Bahasa Arab

**Objek:** 40 target kosa kata, AR-FUN-000001–000008, AR-SEN-000001–000096, AR-TXT-000001–000003, dan AR-CYC-000001–000003.

**Arah yang telah disetujui pemilik untuk validasi:**

- pembelajaran lisan terdistribusi pada P001–P040;
- P028 sebagai kandidat gerbang dan integrasi Siklus 3;
- AR-TXT-000001 hanya boleh digunakan setelah AR-CYC-000003 berstatus SIAP INTEGRASI;
- seluruh materi tetap Audience GURU dan HOLD-PARTICIPANT sampai gate lengkap.

**Dokumen wajib dikirim:**

1. DEC-CUR-005;
2. ACP-QUR-001;
3. MAT-ARB-002;
4. REG-ARB-001–004;
5. LEX-ARB-001–003;
6. BAT-ARB-001–006;
7. MAP-ARB-QJ1-001;
8. GDE-ARB-QJ1-001;
9. VAL-ARB-001;
10. REV-ARB-QJ1-002;
11. RUB-ARB-001 dan FRM-ARB-001;
12. QJ1-P028.

**Keputusan yang diminta:** ketepatan bentuk, vokalisasi, makna, fungsi, struktur, konteks, urutan tahap, kealamian kalimat, keterpaduan teks, beban lima menit, model pelafalan, dan kelayakan tiga gerbang.

## 4. Paket C — Asesmen dan Safeguarding

**Dokumen wajib dikirim:**

- seluruh rubrik dan form Tahfidz/Bahasa Arab;
- REV-QJ1-001;
- BLK-QJ1-001;
- contoh halaman P018, P028, P036, dan P040;
- aturan privasi audio, hak jeda, koreksi rahmah, akomodasi, dan larangan mempermalukan.

**Keputusan yang diminta:** kelayakan bukti, kejelasan kategori keputusan, risiko tekanan, beban, privasi, akses, retensi data, dan penggunaan hasil untuk remedial tanpa stigma.

## 5. Paket D — Editorial dan Produksi

**Dokumen wajib dikirim:**

- PRINT-SPEC-QURBATA-v1;
- AUD-PRN-QJ1-001;
- build PDF peserta 40 halaman;
- aturan Audience GURU/HOLD-PARTICIPANT;
- sumber font dan lisensi;
- halaman khusus P018, P028, P036, dan P038.

**Keputusan yang diminta:** tidak ada kebocoran naskah guru, keterbacaan A5, konsistensi RTL, clipping/harakat, placeholder draf, lisensi, dan daftar kebutuhan proof fisik.

## 6. Format Identitas Reviewer

Setiap reviewer wajib mengisi:

| Elemen | Isian |
|---|---|
| Nama lengkap |  |
| Keahlian dan pengalaman relevan |  |
| Institusi/afiliasi |  |
| Cakupan yang ditelaah |  |
| Konflik kepentingan | TIDAK ADA / ADA — jelaskan |
| Keputusan | SETUJU / SETUJU DENGAN KOREKSI / REVISI / TOLAK / BLOCKED |
| Temuan material |  |
| Koreksi wajib |  |
| Evidence-ID |  |
| Tanggal |  |
| Tanda tangan/paraf |  |

## 7. Aturan Evidence-ID

Evidence-ID diterbitkan hanya setelah bukti benar-benar diterima dan disimpan. Pola yang disiapkan:

- `EVD-HAF-QJ1-YYYYMMDD-001` untuk Tahfidz/Qira’at;
- `EVD-ARB-QJ1-YYYYMMDD-001` untuk Bahasa Arab;
- `EVD-ASG-QJ1-YYYYMMDD-001` untuk asesmen/safeguarding;
- `EVD-EDT-QJ1-YYYYMMDD-001` untuk editorial/produksi.

Nomor tidak boleh dipakai ulang. File bukti harus mempunyai asal, tanggal, pemilik, cakupan, dan status akses.

## 8. Urutan Eksekusi

1. kirim Paket A dan B;
2. terima keputusan serta koreksi ahli;
3. terapkan koreksi pada objek sumber;
4. kirim hasil terkoreksi ke asesmen/safeguarding;
5. jalankan gate Tahfidz dan tiga gate Bahasa Arab;
6. tanam hanya objek yang lulus ke halaman khusus;
7. bangun ulang PDF peserta dan edisi guru;
8. lakukan review editorial/render dan proof fisik;
9. jalankan audit konsistensi;
10. turunkan atau tutup blocker berdasarkan Evidence-ID.

## 9. Status Antrean

| Paket | Kesiapan dokumen | Keputusan pemilik | Keputusan ahli | Status |
|---|---|---|---|---|
| A — Tahfidz/Qira’at | COMPLETE-DRAFT | AVAILABLE — DEC-CUR-004 | NOT PROVIDED | READY-FOR-DISPATCH |
| B — Bahasa Arab | COMPLETE-DRAFT | AVAILABLE — DEC-CUR-005 | NOT PROVIDED | READY-FOR-DISPATCH |
| C — Asesmen/Safeguarding | COMPLETE-DRAFT | NOT REQUIRED FOR DISPATCH | NOT PROVIDED | READY-AFTER-A/B |
| D — Editorial/Produksi | BUILD TEKNIS TERSEDIA | NOT REQUIRED FOR DISPATCH | NOT PROVIDED | READY-AFTER-CONTENT |

## 10. Dampak Status

Penyusunan paket pengiriman menutup gap administrasi antara keputusan arah dan proses review. Namun:

- BLOCKED-CUR-HAF-001/002 tetap OPEN;
- BLOCKED-CUR-ARB-001/002 tetap OPEN;
- objek Tahfidz dan Bahasa Arab tetap inactive;
- P018, P028, P036, dan P040 belum boleh menjadi materi final;
- PR #2 tetap Draft;
- kesiapan makro tidak boleh dinaikkan hanya karena paket siap dikirim.

## 11. Riwayat

| Versi | Tanggal | Ringkasan |
|---|---|---|
| 0.1.0-id | 29 Juli 2026 | Mengonsolidasikan paket Tahfidz, Bahasa Arab, asesmen/safeguarding, serta editorial menjadi antrean validasi operasional |
# QURBATA TARTIL — ATURAN PENYUSUNAN BUKU

Status: **FROZEN v1.2**
Effective: 2026-09-17
Authority: **BOOK COMPOSITION MASTER**
Scope: penyusunan isi dan prinsip layout seluruh Buku QURBATA Tartil
Supersedes: `QURBATA_TARTIL_BOOK_COMPOSITION_RULES_FROZEN-v1.1.md`

## 1. Urutan kerja wajib

Setiap pembuatan/revisi buku mengikuti urutan:
1. Master kurikulum.
2. Master masing-masing domain: Tartil, Bi'ah Arabiyah, Tahfidz, Akhlak.
3. Page register/lesson register.
4. Audit integrasi isi.
5. Freeze konten.
6. Baru generator/layout.
7. Audit visual.
8. FINAL.

**Layout tidak boleh dipakai untuk menentukan atau memperbaiki kurikulum.**

## 2. Empat domain QURBATA

QURBATA pada buku ini terdiri dari:
- **Quran/Tartil** — kompetensi membaca Al-Qur'an; domain utama.
- **Bi'ah Arabiyah** — bahasa Arab instruksional untuk membangun lingkungan bahasa Arab selama pembelajaran Al-Qur'an.
- **Tahfidz** — hafalan Al-Qur'an bertahap dan berurutan.
- **Akhlak** — pembiasaan adab melalui ayat, hadis, atau nasihat ringkas.

Keempatnya terintegrasi dalam satu pertemuan, tetapi tidak boleh saling mencampur fungsi.

## 3. Fungsi per halaman/pertemuan

Setiap halaman harus menjawab empat pertanyaan sebelum layout:
- **Tartil:** kompetensi membaca apa yang ditanam/dilatih?
- **Bi'ah:** instruksi/interaksi Arab apa yang benar-benar dipakai dalam pertemuan?
- **Tahfidz:** bagian hafalan apa yang ditargetkan?
- **Akhlak:** adab apa yang dibiasakan?

Jika salah satu jawaban belum jelas, halaman belum boleh masuk tahap layout.

## 4. Aturan integrasi

- Tartil mengendalikan urutan kompetensi membaca.
- Bi'ah mengendalikan bahasa komunikasi pembelajaran, bukan materi decoding.
- Tahfidz tidak boleh dipilih karena kebetulan cocok dengan huruf Tartil; ia mengikuti urutan hafalan master.
- Akhlak dipilih karena relevan dengan pembiasaan belajar/kehidupan santri dan boleh berulang.
- Integrasi berarti keempat domain hadir dalam satu ekosistem pertemuan, **bukan dipaksa menjadi satu jenis latihan**.

## 5. Aturan Bi'ah Arabiyah

Wajib mengikuti `QURBATA_BIAH_ARABIYAH_INSTRUCTION_MASTER_FROZEN-v1.0.md`.

Khusus buku Tartil:
- jalur utama adalah **bahasa instruksional kelas**;
- prioritas: salam → baca → ulangi → dengarkan/perhatikan → buka/tutup → sekali lagi → berhenti/lanjut → respons → interaksi;
- ungkapan bersifat kumulatif dan dipraktikkan;
- kalimat benda seperti `هَذَا كِتَابٌ`, `هَذَا قَلَمٌ`, `هَذِهِ صَفْحَةٌ` tidak menjadi urutan utama kecuali digunakan dalam dialog/instruksi yang nyata;
- tidak ada bab nahwu/sharaf di panel Bi'ah.

## 6. Aturan page register

Setiap entry halaman wajib mempunyai field minimal:
- ID halaman/pertemuan;
- kompetensi Tartil baru/aktif;
- pool murojaah;
- jenis halaman: materi / penguatan / evaluasi / checkpoint;
- Bi'ah Arabiyah: kategori + ungkapan + makna + fungsi praktik;
- Tahfidz: surat/ayat atau status review;
- Akhlak: tema + nash;
- catatan larangan/premature competency bila relevan.

Page register tidak boleh hanya mencantumkan label `Bahasa Arab` tanpa fungsi instruksional.

## 7. Audit sebelum layout

### Audit Tartil
- tangga kompetensi benar;
- materi baru/review benar;
- tidak ada kompetensi prematur;
- murojaah kumulatif;
- checkpoint benar.

### Audit Bi'ah
- benar-benar instruksional/interaktif;
- urutan kumulatif;
- dapat dipraktikkan di kelas;
- bukan mufradat/nahwu terpisah.

### Audit Tahfidz
- urutan hafalan benar;
- ayat tidak lompat tanpa keputusan master;
- evaluasi/review ditandai jelas.

### Audit Akhlak
- nash dan tema benar;
- ringkas;
- pembiasaan jelas;
- pengulangan disengaja, bukan duplikasi tak terkendali.

**Semua audit isi harus lulus sebelum editing layout.**

## 8. Freeze dan perubahan

Setelah register dinyatakan CONTENT FROZEN:
- layout hanya mengatur presentasi, bukan substansi;
- perubahan isi harus kembali ke master/register;
- setiap perubahan kurikulum menaikkan versi dan memiliki changelog;
- PDF lama otomatis menjadi AUDIT/OBSOLETE jika bertentangan dengan master baru.

## 9. Prinsip desain setelah konten frozen

Baru setelah isi benar:
- Tartil mendapat ruang paling besar;
- panel Bi'ah/Tahfidz/Akhlak ringkas tetapi terbaca;
- KFGQPC Uthman Taha untuk Arab produksi sesuai master tipografi;
- Tanggal–Nilai–TTD dan integrasi RIQA OS tetap tersedia;
- layout tidak boleh menghapus konteks praktik Bi'ah.

### 9.1 Zona kerja guru — Tanggal, Nilai, TTD

Ketentuan ini **WAJIB** untuk seluruh halaman latihan/pertemuan yang memakai `Tanggal – Nilai – TTD`.

1. `Tanggal`, `Nilai`, dan `TTD` adalah **label di bagian bawah area kerja guru**, bukan judul yang diletakkan di atas ruang tulis.
2. **Ruang kosong untuk menulis wajib berada DI ATAS tulisan/label `Tanggal`, `Nilai`, dan `TTD`, bukan di bawahnya.** Ini adalah orientasi baku seluruh Buku QURBATA.
3. Guru menulis tanggal, nilai, dan terutama tanda tangan pada ruang kosong yang tersedia **di atas label masing-masing**. Karena itu ruang kosong di bawah label tidak dihitung sebagai ruang kerja.
4. Antara konten `Aktivitas Bi'ah QURBATA`/panel di atas dan awal ruang kerja guru harus ada pemisahan visual yang jelas. Target jarak efektif adalah **5–7 mm**; minimum **4 mm** bila halaman sangat padat.
5. Area tanda tangan di atas label `TTD` harus menyediakan tinggi bersih minimum **12 mm**, dengan target nyaman **14–18 mm** bila ruang memungkinkan.
6. Area `Tanggal` dan `Nilai` dapat lebih kompak daripada TTD, tetapi tetap harus mempunyai ruang tulis yang nyata **di atas labelnya**.
7. Di bawah label `Tanggal – Nilai – TTD` hanya disediakan ruang proporsional untuk baseline/garis isian, identitas halaman, slogan/footer, dan safe area cetak. **Dilarang menyisakan ruang kosong besar di bawah label sementara ruang di atas label sempit.**
8. Bila halaman kekurangan ruang, urutan kompresi adalah: padding dekoratif → gap panel → heading/footer → elemen pendukung. **Ruang kerja TTD di atas label tidak boleh menjadi korban pertama.**
9. Posisi vertikal ketiga label harus konsisten antarahalaman. Garis/baseline isian harus sejajar dan tidak bertabrakan dengan footer atau QR RIQA OS.
10. Generator/Vivliostyle wajib menerapkan orientasi ini sebagai **layout invariant** pada semua halaman, bukan koreksi manual per halaman.
11. Audit visual wajib memeriksa secara eksplisit: (a) ruang terbesar berada di atas label, (b) TTD realistis untuk tanda tangan pena, (c) ruang bawah label tidak berlebihan, (d) footer/slogan tidak bertabrakan, dan (e) halaman tetap tepat satu halaman per pertemuan.

**Prinsip utama:** `Tanggal – Nilai – TTD` adalah **ruang kerja guru**. Secara visual dan fungsional, **spasi untuk menulis berada di atas tulisan, bukan di bawahnya**.

### 9.2 Invariant proporsi halaman

- Perubahan zona kerja guru tidak boleh mengubah kompetensi, jumlah latihan, atau urutan materi.
- Satu pertemuan tetap satu halaman sesuai page register.
- Tartil tetap menjadi area dominan.
- Penyesuaian layout harus dilakukan dengan redistribusi ruang di dalam ukuran halaman tetap, bukan dengan membuat overflow/halaman tambahan.
- PDF audit harus tetap memenuhi jumlah halaman yang ditentukan register.

## 10. Gate FINAL

Buku hanya dapat berstatus FINAL jika berurutan:
**CURRICULUM PASS → DOMAIN PASS → PAGE REGISTER PASS → CONTENT FREEZE → LAYOUT PASS → PDF PASS.**

Untuk `LAYOUT PASS`, zona `Tanggal – Nilai – TTD` wajib lulus §9.1 dan invariant proporsi §9.2.

Jika kurikulum/domain atau aturan layout frozen berubah, status layout/PDF sebelumnya kembali menjadi AUDIT sampai diturunkan ulang dari master terbaru.

## 11. Changelog

### v1.2 — 2026-09-17
- Mengoreksi orientasi zona kerja guru: **spasi tulis berada di atas label `Tanggal`, `Nilai`, dan `TTD`, bukan di bawahnya**.
- Menetapkan bahwa ruang kosong di bawah label tidak dihitung sebagai area tanda tangan.
- Menetapkan larangan ruang bawah yang berlebihan sementara ruang atas sempit.
- Menambahkan audit visual khusus orientasi atas-label dan invariant proporsi satu pertemuan/satu halaman.
- PDF/layout berbasis v1.1 otomatis kembali berstatus **AUDIT/OBSOLETE** sampai dibangun ulang dari v1.2.

### v1.1 — 2026-09-17
- Menetapkan zona `Tanggal – Nilai – TTD` sebagai ruang kerja guru.
- Menetapkan celah vertikal wajib dari panel di atas.
- Menetapkan area TTD minimum 12 mm dan target nyaman 14–18 mm.
- Menambahkan gate audit visual khusus untuk ruang tanda tangan.

### v1.0 — 2026-09-15
- Freeze awal aturan penyusunan Buku QURBATA Tartil.

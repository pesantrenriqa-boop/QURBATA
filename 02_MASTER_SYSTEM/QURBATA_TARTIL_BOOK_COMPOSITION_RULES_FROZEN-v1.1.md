# QURBATA TARTIL — ATURAN PENYUSUNAN BUKU

Status: **FROZEN v1.1**
Effective: 2026-09-17
Authority: **BOOK COMPOSITION MASTER**
Scope: penyusunan isi dan prinsip layout seluruh Buku QURBATA Tartil
Supersedes: `QURBATA_TARTIL_BOOK_COMPOSITION_RULES_FROZEN-v1.0.md`

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

### 9.1 Zona penilaian bawah halaman — Tanggal, Nilai, TTD

Ketentuan ini **WAJIB** untuk seluruh halaman latihan/pertemuan yang memakai panel `Tanggal – Nilai – TTD`:

1. Panel penilaian ditempatkan pada **zona paling bawah halaman**, setelah seluruh panel materi utama selesai.
2. Panel **tidak boleh menempel** pada panel Bi'ah Arabiyah, Tahfidz, Akhlak, grid latihan, atau elemen di atasnya. Harus ada **celah vertikal yang terlihat jelas** sebelum zona penilaian.
3. Kolom **TTD wajib mempunyai ruang kosong vertikal yang cukup untuk tanda tangan nyata dengan pena**. Label `TTD` tidak boleh berhimpitan dengan batas bawah halaman dan tidak boleh dipadatkan hanya demi memasukkan elemen lain.
4. Secara layout, zona TTD harus mempunyai **tinggi minimum 12 mm** untuk area tanda tangan bersih, di luar label/border. Target nyaman produksi adalah **14–18 mm** bila ruang halaman memungkinkan.
5. Jarak aman antara konten/panel di atas dan zona `Tanggal – Nilai – TTD` adalah **minimum 4 mm**, dengan target **5–7 mm** pada halaman normal.
6. Jarak zona penilaian terhadap batas bawah area cetak/safe area adalah **minimum 5 mm**. Dilarang menempatkan garis, label, atau ruang tanda tangan terlalu dekat trim/batas bawah halaman.
7. `Tanggal` dan `Nilai` boleh dibuat kompak, tetapi **ruang TTD tidak boleh dikorbankan**. Bila ruang sempit, yang dikompakkan terlebih dahulu adalah padding panel pendukung, bukan area tanda tangan.
8. Posisi vertikal panel harus konsisten antarahalaman sehingga buku terasa stabil saat dibuka dan dinilai guru.
9. Generator/Vivliostyle harus memakai aturan ini sebagai **layout invariant**, bukan koreksi manual per halaman.
10. Audit visual wajib memeriksa: (a) ada celah sebelum panel penilaian, (b) TTD dapat ditulis secara realistis, (c) tidak mepet batas bawah, dan (d) tidak bertabrakan/menekan panel lain.

**Prinsip utama:** area `Tanggal – Nilai – TTD` bukan sekadar footer dekoratif, tetapi **ruang kerja guru**. Karena itu keterbacaan dan ruang fisik untuk menulis/tanda tangan lebih penting daripada memadatkan halaman sampai penuh.

## 10. Gate FINAL

Buku hanya dapat berstatus FINAL jika berurutan:
**CURRICULUM PASS → DOMAIN PASS → PAGE REGISTER PASS → CONTENT FREEZE → LAYOUT PASS → PDF PASS.**

Untuk `LAYOUT PASS`, zona `Tanggal – Nilai – TTD` juga harus lulus ketentuan §9.1.

Jika kurikulum/domain berubah, status layout/PDF sebelumnya kembali menjadi AUDIT sampai diturunkan ulang dari master terbaru.

## 11. Changelog

### v1.1 — 2026-09-17
- Menetapkan zona `Tanggal – Nilai – TTD` sebagai ruang kerja guru.
- Memindahkan/menjaga panel lebih ke bawah dengan safe area yang memadai.
- Menetapkan celah vertikal wajib dari panel di atas.
- Menetapkan area TTD minimum 12 mm dan target nyaman 14–18 mm.
- Menambahkan gate audit visual khusus untuk ruang tanda tangan.

### v1.0 — 2026-09-15
- Freeze awal aturan penyusunan Buku QURBATA Tartil.

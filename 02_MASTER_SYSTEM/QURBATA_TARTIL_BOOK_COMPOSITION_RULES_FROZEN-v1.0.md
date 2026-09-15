# QURBATA TARTIL — ATURAN PENYUSUNAN BUKU

Status: **FROZEN v1.0**
Effective: 2026-09-15
Authority: **BOOK COMPOSITION MASTER**
Scope: penyusunan isi sebelum layout seluruh Buku QURBATA Tartil

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

## 10. Gate FINAL

Buku hanya dapat berstatus FINAL jika berurutan:
**CURRICULUM PASS → DOMAIN PASS → PAGE REGISTER PASS → CONTENT FREEZE → LAYOUT PASS → PDF PASS.**

Jika kurikulum/domain berubah, status layout/PDF sebelumnya kembali menjadi AUDIT sampai diturunkan ulang dari master terbaru.

# QURBATA TARTIL — ATURAN PENYUSUNAN BUKU

Status: **FROZEN v1.4.1**
Effective: 2026-09-17
Authority: **BOOK COMPOSITION MASTER**
Scope: penyusunan isi, tipografi latihan, glyph Arab, dan prinsip layout seluruh Buku QURBATA Tartil
Supersedes: `QURBATA_TARTIL_BOOK_COMPOSITION_RULES_FROZEN-v1.4.md` pada aspek footer/zona bawah.

> Seluruh generator, layout, PDF, dan audit visual setelah keputusan ini WAJIB mengikuti v1.4.1. PDF sebelum penerapan footer v1.4.1 berstatus AUDIT/OBSOLETE sampai diregenerasi.

## 1. Urutan kerja wajib
Master kurikulum → domain masters → page register → audit integrasi isi → content freeze → generator/layout → audit visual → FINAL. Layout tidak boleh mengubah substansi kurikulum.

## 2. Empat domain QURBATA
QURBATA tetap terdiri dari Quran/Tartil, Bi'ah Arabiyah, Tahfidz, dan Akhlak. Tartil adalah domain utama. Bi'ah tetap hadir sebagai bahasa instruksional pada panel materi/pertemuan, tetapi **tidak memerlukan zona aktivitas tambahan di bagian bawah halaman**.

## 3. Struktur latihan Jilid 1
- 8 baris per halaman.
- 3 kelompok per baris = 24 kelompok.
- Satu pertemuan = satu halaman.
- Materi baru/review mengikuti master dan page register.
- Tartil wajib menjadi elemen visual terbesar dan paling dominan.

## 4. Proporsi dan breathing room — WAJIB
1. Tidak boleh ada teks Arab/Latin yang mepet garis, panel, teks lain, atau tepi aman cetak.
2. Tidak boleh ada clipping harakat, overlap, baseline bertabrakan, atau panel terasa sesak.
3. Setiap blok mempunyai clear space yang cukup secara visual, khususnya di atas/bawah glyph Arab dan harakat.
4. Jika halaman terlalu padat, yang dikompresi lebih dahulu adalah ornamen, padding dekoratif, heading, gap panel pendukung, footer, QR/elemen digital; **bukan latihan Tartil**.
5. Audit layout tidak cukup hanya memastikan 40 halaman; setiap halaman harus proporsional pada ukuran cetak A5.

## 5. Ukuran contoh dan latihan Tartil — PRIORITAS UTAMA
1. Tulisan contoh/penanaman kompetensi baru wajib besar, jelas, dan mudah ditiru santri.
2. Tulisan latihan membaca wajib lebih besar daripada build v1.3 yang terakhir diaudit; tidak boleh semakin kecil akibat pagination.
3. Ruang yang diperoleh dari penyederhanaan zona bawah wajib dialihkan terutama untuk memperbesar glyph latihan, tinggi efektif 8 baris, breathing room vertikal, dan jarak antarkelompok.
4. Ukuran font ditentukan bersama bounding box aktual KFGQPC Uthman Taha pada A5.
5. Generator dilarang memakai auto-shrink pada latihan sebagai solusi pertama.
6. Prioritas ruang: **Latihan Tartil → contoh/penanaman → panel materi inti → administrasi footer → QR/dekorasi**.

## 6. Ha dua lubang — GLYPH GATE
1. Seluruh **ه tunggal/detached** pada materi Tartil wajib tampil sebagai **ha dua lubang** sesuai standar visual QURBATA.
2. Ha satu lubang/bulat pada latihan, judul kompetensi, penanaman, evaluasi, atau checkpoint dilarang.
3. Pemeriksaan Unicode saja tidak cukup; gate wajib memeriksa hasil render/glyph visual.
4. Bila shaping menghasilkan satu lubang, generator wajib memakai sequence/glyph/konstruksi tervalidasi tanpa mengubah bunyi/kompetensi.
5. PDF tidak boleh LAYOUT PASS sebelum Ha relevan diaudit visual.

## 7. Panel Tahfidz – Bi'ah Arabiyah – Akhlak
- Tetap ringkas dan terbaca.
- Teks Arab berpasangan dengan arti Indonesia yang tepat.
- Repetisi pedagogis Bi'ah/Akhlak mengikuti master.
- Panel tidak boleh mengambil ruang berlebihan dari latihan Tartil.

## 8. PENGHAPUSAN ZONA `AKTIVITAS BI'AH QURBATA` DI BAGIAN BAWAH
Keputusan ini **FROZEN**:
1. Heading/tulisan `AKTIVITAS BI'AH QURBATA` di bagian bawah DIHAPUS.
2. Seluruh kotak/panel kosong lebar berwarna biru/mint atau area kosong khusus aktivitas di antara latihan dan footer DIHAPUS.
3. Penghapusan tidak menghapus domain Bi'ah dari kurikulum; Bi'ah tetap berada pada panel materi dan praktik pembelajaran.
4. Ruang hasil penghapusan dialihkan ke latihan Tartil.
5. Generator tidak boleh mengganti ruang tersebut dengan ornamen/padding baru.

## 9. FOOTER RESMI QURBATA JILID 1 — FROZEN v1.4.1
Footer wajib mengikuti referensi visual yang disetujui pada 17 September 2026 dan menjadi komponen resmi seluruh halaman isi Jilid 1.

### 9.1 Susunan horizontal
Dari kiri ke kanan secara visual:
1. **ID halaman** dalam badge kecil, contoh `QJ1-P002`.
2. **Tanggal** dengan area tulis yang jelas.
3. **Nilai** dengan area tulis yang lebih kompak.
4. **TTD** dengan area tanda tangan paling lebar.
5. **QR RIQA OS**.
6. Identitas digital di kanan QR: motto Arab `تَعَلَّمْ – اِعْمَلْ – عَلِّمْ`, arti `Belajar, Mengamalkan, Mengajarkan`, dan label **RIQA OS**.

### 9.2 Aturan visual
- Seluruh komponen berada pada satu footer horizontal yang rapi dan satu baseline visual.
- **Dilarang ada kotak biru/mint kosong di atas footer.**
- Tidak ada heading `Aktivitas Bi'ah QURBATA`.
- Tanggal, Nilai, dan TTD menggunakan field ringan/outline tipis; bukan garis panjang yang saling bertabrakan.
- Label berada di bagian atas field; ruang menulis berada di bawah label di dalam field.
- TTD paling lebar dan harus realistis untuk tanda tangan pena.
- QR berdiri pada kolom sendiri dan **tidak boleh menimpa TTD, motto, nomor halaman, footer text, atau elemen lain**.
- QR harus mempunyai quiet zone putih bersih di keempat sisi dan tetap dapat dipindai.
- Motto/RIQA OS berada di sebelah kanan QR, bukan di belakang/di bawah QR.
- Footer audit teknis/page-register tidak boleh dicetak menyeberangi QR atau field administrasi. Metadata audit hanya boleh menjadi metadata file/log atau ditempatkan di area aman yang tidak mengganggu desain buku.
- Warna mengikuti identitas QURBATA: biru/teal ringan; QR tetap hitam-putih.
- Footer tidak boleh lebih dominan daripada latihan Tartil.

### 9.3 Prioritas ruang
Jika footer tidak muat: kecilkan teks sekunder, gap, badge ID, atau QR secara proporsional terlebih dahulu. Jangan mengecilkan latihan Tartil dan jangan menumpuk elemen.

## 10. Audit page register dan isi
Page register tetap memuat kompetensi Tartil, murojaah, jenis halaman, Bi'ah, Tahfidz, Akhlak, status repetisi, dan catatan glyph/premature competency. Perubahan v1.4.1 adalah perubahan presentasi/footer; isi domain tetap tunduk pada master yang berlaku.

## 11. Visual gate v1.4.1
Sebelum PDF dinyatakan LAYOUT PASS, audit visual wajib membuktikan:
- satu pertemuan/satu halaman;
- 8×3 latihan utuh;
- latihan contoh dan latihan membaca besar/lapang;
- tidak ada clipping, overlap, teks mepet, atau tabrakan harakat;
- Ha tunggal dua lubang secara visual;
- tidak ada heading maupun kotak kosong `Aktivitas Bi'ah QURBATA`;
- footer horizontal = ID halaman + Tanggal + Nilai + TTD + QR + motto/RIQA OS;
- QR mempunyai quiet zone dan tidak overlap;
- tidak ada metadata audit yang menyeberangi footer;
- panel integrasi terbaca;
- KFGQPC Uthman Taha tertanam;
- jumlah PDF tepat sesuai register.

Kegagalan satu poin = **LAYOUT FAIL**.

## 12. Gate FINAL
**CURRICULUM PASS → DOMAIN PASS → PAGE REGISTER PASS → CONTENT FREEZE → GLYPH PASS → LAYOUT PASS → PDF PASS.**

## 13. Changelog
### v1.4.1 — 2026-09-17
- Menetapkan desain footer referensi pengguna sebagai **footer resmi QURBATA Jilid 1**.
- Menghapus kotak biru/mint kosong di atas footer.
- Menetapkan urutan footer: ID halaman → Tanggal → Nilai → TTD → QR → motto/RIQA OS.
- Menetapkan quiet zone QR dan larangan overlap QR dengan elemen apa pun.
- Melarang metadata audit/page-register melintas pada footer cetak.
- Menetapkan TTD sebagai field administrasi terlebar.

### v1.4 — 2026-09-17
- Memperbesar latihan Tartil dan menghapus zona Aktivitas Bi'ah bawah.
- Memperkuat Ha dua lubang sebagai visual glyph gate.
- Menetapkan prioritas ruang yang melindungi latihan Tartil.

# QURBATA TARTIL — ATURAN PENYUSUNAN BUKU

Status: **FROZEN v1.4.3**
Effective: 2026-09-17
Authority: **BOOK COMPOSITION MASTER**
Scope: penyusunan isi, tipografi latihan, glyph Arab, dan prinsip layout seluruh Buku QURBATA Tartil

> Seluruh generator, layout, PDF, dan audit visual setelah keputusan ini WAJIB mengikuti v1.4.3. PDF footer versi sebelumnya berstatus AUDIT/OBSOLETE sampai diregenerasi.

## 1. Urutan kerja wajib
Master kurikulum → domain masters → page register → audit integrasi isi → content freeze → generator/layout → audit visual → FINAL. Layout tidak boleh mengubah substansi kurikulum.

## 2. Empat domain QURBATA
QURBATA tetap terdiri dari Quran/Tartil, Bi'ah Arabiyah, Tahfidz, dan Akhlak. Tartil adalah domain utama. Bi'ah tetap hadir sebagai bahasa instruksional pada panel materi/pertemuan, tanpa zona aktivitas tambahan di bawah.

## 3. Struktur latihan Jilid 1
- 8 baris per halaman; 3 kelompok per baris = 24 kelompok.
- Satu pertemuan = satu halaman.
- Materi baru/review mengikuti master dan page register.
- Tartil wajib menjadi elemen visual terbesar dan paling dominan.

## 4. Proporsi dan breathing room
Tidak boleh ada clipping, overlap, baseline collision, teks mepet, atau panel sesak. Jika ruang kurang, kompres ornamen/footer/QR lebih dahulu, bukan latihan Tartil. Ukuran latihan tidak boleh diperkecil sebagai solusi pertama.

## 5. Ha dua lubang — GLYPH GATE
Seluruh ه tunggal/detached pada materi Tartil wajib tampil sebagai Ha dua lubang. Audit harus visual; Unicode scan saja tidak cukup. Ha satu lubang pada latihan, judul, penanaman, evaluasi, atau checkpoint = FAIL.

## 6. Panel Tahfidz – Bi'ah Arabiyah – Akhlak
Tetap ringkas, terbaca, Arab berpasangan dengan arti Indonesia, dan tidak mengambil ruang berlebihan dari Tartil.

## 7. Zona Aktivitas Bi'ah bawah DIHAPUS
Heading `Aktivitas Bi'ah QURBATA`, kotak biru/mint kosong, dan ruang kosong khusus aktivitas di antara latihan dan footer dilarang. Ruang hasil penghapusan menjadi milik latihan Tartil.

# 8. FOOTER RESMI QURBATA JILID 1 — FROZEN v1.4.3
Referensi visual footer yang disetujui pengguna pada 17 September 2026 menjadi **authority visual resmi**. Tujuannya: sederhana, proporsional, mudah diisi dengan pena, mudah dipindai, dan tidak mengganggu dominasi latihan Tartil.

## 8.1 Prinsip utama
Footer wajib **selalu tampil pada setiap halaman isi**. Elemen Tanggal, Nilai, dan TTD tidak boleh hilang karena pagination, overflow, clipping, selector, transformasi DOM, atau penggabungan PDF.

Footer merupakan **satu pita horizontal tunggal** di bawah latihan. Tidak boleh pecah menjadi dua baris dan tidak boleh ada elemen footer tercecer di bagian bawah halaman.

Urutan visual kiri → kanan:
**ID halaman | Tanggal | Nilai | TTD | QR | identitas RIQA OS**.

## 8.2 Proporsi footer pada halaman A5
Gunakan proporsi relatif, bukan ukuran yang memaksa overflow:
- ID halaman: ±9% lebar footer.
- Tanggal: ±21%.
- Nilai: ±14%.
- TTD: ±23%.
- QR + quiet zone: ±11%.
- Brand RIQA OS: ±22%.

Gap antarkolom kecil dan konsisten. Total seluruh kolom + gap wajib <= 100% area aman halaman.

Tinggi keseluruhan footer target **16–19 mm**, termasuk label dan field, dan wajib masuk di area cetak halaman tanpa mendorong konten keluar.

## 8.3 ID halaman
- Bentuk badge kecil/pill berwarna biru muda.
- Contoh `QJ1-P002`.
- Teks tebal, kontras, dan satu baris.
- Badge tidak boleh mengambil ruang lebih besar daripada field administrasi.

## 8.4 Tanggal, Nilai, TTD — WAJIB TAMPIL
Ketiga field adalah elemen administrasi wajib dan tidak boleh dihapus.

Struktur masing-masing kolom:
1. label di atas: `Tanggal:`, `Nilai:`, `TTD:`;
2. kotak tulis tepat di bawah label;
3. outline tipis biru/teal;
4. sudut membulat ringan;
5. latar putih;
6. garis/titik bantu tulis boleh berada dekat dasar kotak.

Proporsi:
- Tanggal cukup untuk tanggal lengkap.
- Nilai paling kompak.
- TTD paling lebar untuk tanda tangan pena.

Field harus mempunyai tinggi efektif tulis sekitar **9–11 mm** dan tidak boleh terpotong.

## 8.5 QR RIQA OS
- QR hitam-putih.
- QR berada pada kolom sendiri, center secara vertikal.
- Ukuran target sekitar **13–15 mm**, disesuaikan agar seluruh footer tetap muat.
- Quiet zone putih bersih minimal ±1 mm di setiap sisi.
- QR tidak boleh menyentuh TTD atau brand.
- QR tidak boleh menimpa teks, berada di belakang teks, atau turun ke baris kedua.

## 8.6 Identitas RIQA OS
Di sebelah kanan QR, tersusun vertikal dan center:
1. `تَعَلَّمْ – اِعْمَلْ – عَلِّمْ`
2. `Belajar, Mengamalkan, Mengajarkan`
3. **RIQA OS**

Arab menggunakan KFGQPC Uthman Taha. Brand tidak boleh berada di bawah QR atau tercecer di kiri bawah halaman.

## 8.7 Ornamen bawah
Boleh ada **strip ornamen geometris/arabesque yang sangat tipis dan ringan** di tepi bawah halaman sebagai penutup visual, dengan syarat:
- tinggi maksimum ±3–4 mm;
- warna biru sangat muda;
- tidak memuat teks;
- tidak mengurangi ruang Tanggal/Nilai/TTD;
- tidak mengganggu QR;
- menjadi elemen dekoratif terakhir, sehingga harus dihapus lebih dahulu bila halaman kekurangan ruang.

## 8.8 Metadata teknis
String `AUDIT`, path repository, nama `PAGE_REGISTER`, debug text, source marker, SHA, dan metadata build **DILARANG dicetak pada halaman buku**. Hanya boleh tersimpan pada log/artifact metadata.

## 8.9 Larangan eksplisit
- Dilarang menghilangkan Tanggal, Nilai, atau TTD.
- Dilarang kotak biru/mint kosong di atas footer.
- Dilarang footer lebih dari satu row.
- Dilarang QR berdiri sendiri di tengah bawah halaman.
- Dilarang QR overlap dengan TTD/brand.
- Dilarang motto Arab jatuh ke kiri bawah.
- Dilarang metadata audit/path tercetak.
- Dilarang footer keluar dari area aman cetak.
- Dilarang mengurangi ukuran latihan Tartil hanya untuk mempertahankan ornamen footer.

# 9. Aturan implementasi generator
Generator wajib membangun footer sebagai **komponen mandiri per halaman**, misalnya `.qurbata-footer`, dan menempatkannya **di dalam struktur halaman sebelum penutup page/article**, bukan setelah page container.

Komponen footer harus dibuat per halaman dan tidak boleh bergantung pada pencarian selector QR lama yang mungkin gagal. Sumber QR harus eksplisit/stabil. Jika QR tidak tersedia, field administrasi tetap wajib tampil; kegagalan QR tidak boleh menghapus seluruh footer.

Gunakan CSS Grid/Flex proporsional dengan `box-sizing:border-box`, `min-width:0`, dan tanpa `position:absolute`, negative margin, atau transform yang dapat menyebabkan overlap. Footer wajib `break-inside:avoid` dan seluruh dimensinya harus dihitung terhadap content-box A5.

Pipeline wajib melakukan assertion sebelum render:
- setiap halaman memiliki tepat 1 footer resmi;
- setiap footer memiliki `Tanggal`, `Nilai`, `TTD`;
- setiap footer memiliki ID halaman;
- tidak ada string metadata teknis tercetak;
- tidak ada legacy footer kedua.

Jika assertion gagal, build harus FAIL, bukan menghasilkan PDF tanpa administrasi.

# 10. Visual gate v1.4.3
LAYOUT PASS hanya jika pada sampel P001, P002, P010, P014, P020, P030, dan P040 terbukti:
- satu pertemuan/satu halaman dan 8×3 utuh;
- latihan Tartil besar/lapang;
- Ha detached dua lubang;
- tidak ada zona Aktivitas Bi'ah bawah;
- footer tampil lengkap dan proporsional;
- Tanggal + Nilai + TTD semuanya terlihat dan bisa ditulis;
- footer satu row: ID + Tanggal + Nilai + TTD + QR + RIQA OS;
- QR scan-safe dan tidak overlap;
- motto hanya di kanan QR;
- tidak ada metadata audit/path;
- footer tidak terpotong di tepi bawah;
- panel integrasi terbaca;
- KFGQPC Uthman Taha tertanam;
- jumlah halaman sesuai register.

Satu kegagalan = **LAYOUT FAIL**.

# 11. Gate FINAL
**CURRICULUM PASS → DOMAIN PASS → PAGE REGISTER PASS → CONTENT FREEZE → GLYPH PASS → LAYOUT PASS → PDF PASS.**

# 12. Changelog
## v1.4.3 — 2026-09-17
- Mengunci Tanggal, Nilai, TTD sebagai elemen wajib yang tidak boleh hilang.
- Menetapkan proporsi footer berbasis persentase agar muat pada A5.
- Menetapkan tinggi field tulis dan QR yang realistis.
- Mengizinkan strip arabesque tipis sebagai ornamen paling bawah/non-prioritas.
- Mewajibkan footer dibuat di dalam setiap page/article.
- Mewajibkan build assertion agar PDF tanpa Tanggal/Nilai/TTD otomatis FAIL.
- Menetapkan sampel audit visual P001/P002/P010/P014/P020/P030/P040.

## v1.4.2 — 2026-09-17
- Mengunci footer sebagai satu row tunggal dan melarang metadata audit tercetak.

## v1.4.1 — 2026-09-17
- Menetapkan urutan ID → Tanggal → Nilai → TTD → QR → brand.

## v1.4 — 2026-09-17
- Memperbesar latihan Tartil dan menghapus zona Aktivitas Bi'ah bawah.
- Memperkuat Ha dua lubang sebagai visual glyph gate.

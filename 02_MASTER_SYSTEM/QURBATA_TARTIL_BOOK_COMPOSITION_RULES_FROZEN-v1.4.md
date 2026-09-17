# QURBATA TARTIL — ATURAN PENYUSUNAN BUKU

Status: **FROZEN v1.5**
Effective: 2026-09-17
Authority: **BOOK COMPOSITION MASTER**
Scope: penyusunan isi, tipografi latihan, glyph Arab, proporsi halaman, dan layout seluruh Buku QURBATA Tartil

> v1.5 menggantikan aturan layout v1.4.x. Seluruh PDF lama berstatus AUDIT/OBSOLETE sampai diregenerasi dan lolos visual gate v1.5.

# 1. Prinsip utama: HALAMAN BELAJAR, BUKAN HALAMAN KOSONG
Setiap halaman A5 harus terasa penuh, lapang, dan proporsional untuk belajar. Ruang putih hanya boleh menjadi breathing room fungsional, bukan area kosong besar tanpa fungsi.

**Dilarang ada dead space vertikal besar** antara latihan Tartil dan bagian bawah halaman. Bila terdapat ruang kosong, ruang tersebut WAJIB dialokasikan kembali dengan urutan:
1. memperbesar contoh/penanaman kompetensi;
2. memperbesar latihan Tartil;
3. menambah tinggi efektif baris latihan;
4. memperbesar jarak aman antar-glyph/harakat;
5. memperjelas panel Tahfidz–Bi'ah–Akhlak;
6. baru sisanya menjadi breathing room.

# 2. Hierarki visual halaman
Urutan dominasi wajib:
**Contoh/Penanaman Kompetensi + Latihan Tartil → panel integrasi → footer administrasi/RIQA OS → ornamen.**

Tartil harus menguasai mayoritas area belajar halaman. Footer tidak boleh terlihat sebagai blok utama halaman.

# 3. Contoh / penanaman materi baru — WAJIB BESAR
Contoh materi baru adalah objek pertama yang ditiru santri, sehingga tidak boleh kecil seperti teks penjelasan.

Aturan:
- Arab contoh/penanaman menggunakan KFGQPC Uthman Taha.
- Target ukuran visual **minimum 30 pt**, ideal **32–36 pt** pada A5 selama tidak clipping.
- Pada halaman pengenalan harakat/kompetensi baru, contoh boleh lebih besar daripada latihan reguler.
- Minimal dua baris penanaman bila master halaman mensyaratkan penanaman.
- Harakat harus jelas, tidak bertabrakan dengan border atau baris di atas/bawah.
- Contoh tidak boleh diperkecil otomatis untuk menyelamatkan footer/ornamen.

# 4. Latihan Tartil — WAJIB BESAR DAN DOMINAN
- Struktur tetap **8 baris × 3 kelompok = 24 kelompok**.
- Satu pertemuan = satu halaman.
- Font Arab latihan KFGQPC Uthman Taha.
- Target ukuran visual latihan **minimum 28 pt**, ideal **30–34 pt** pada A5 jika glyph/harakat aman.
- Tinggi baris harus memanfaatkan ruang vertikal halaman, bukan dipadatkan di bagian atas.
- Setiap cell memiliki breathing room atas/bawah yang cukup agar harakat tidak menyentuh garis.
- Tiga kelompok per baris harus terbaca dari jarak belajar normal.
- Dilarang auto-shrink latihan sebagai solusi pagination pertama.

# 5. Distribusi tinggi halaman A5
Generator wajib menghitung tinggi halaman sebagai sistem, bukan menumpuk komponen dengan margin bebas.

Target proporsi vertikal area isi:
- header/judul/kompetensi: ±8–10%;
- contoh/penanaman: ±10–14%;
- latihan Tartil 8 baris: **±50–58%**;
- panel Tahfidz–Bi'ah–Akhlak: ±10–13%;
- footer administrasi + QR/brand: ±8–10%;
- gap/breathing room total: maksimum ±5% dan harus tersebar, bukan satu blok kosong.

Toleransi boleh berubah pada checkpoint/evaluasi, tetapi **tidak boleh menghasilkan dead space besar**.

# 6. Aturan anti-dead-space
LAYOUT FAIL bila terdapat area kosong vertikal tanpa fungsi yang secara visual lebih tinggi daripada kira-kira satu baris latihan reguler.

Generator harus menggunakan layout grid halaman dengan row terkontrol, misalnya:
`header | planting | practice | integration | footer`

dengan `practice` sebagai `minmax(0,1fr)` / area fleksibel utama. Margin/padding antarbagian harus kecil dan konsisten. Dilarang fixed-height lama yang meninggalkan lubang besar setelah practice.

# 7. Ha dua lubang — GLYPH GATE
Seluruh ه detached pada Tartil wajib tampil sebagai Ha dua lubang. Audit harus visual. Ha satu lubang pada latihan, judul, penanaman, evaluasi, atau checkpoint = FAIL.

# 8. Panel Tahfidz – Bi'ah Arabiyah – Akhlak
- Tetap tiga domain pendukung yang ringkas dan terbaca.
- Arab + arti Indonesia harus terbaca tanpa crowding.
- Panel tidak boleh menjadi penyebab latihan Tartil mengecil.
- Bi'ah adalah bahasa instruksional, bukan daftar kosakata dekoratif.
- Tidak ada lagi zona `Aktivitas Bi'ah QURBATA` atau kotak kosong khusus aktivitas di bawah latihan.

# 9. Footer resmi — ringkas dan proporsional
Footer wajib selalu tampil tetapi **harus kompak** agar tidak menciptakan dead space.

Urutan horizontal:
**ID halaman | Tanggal | Nilai | TTD | QR | RIQA OS**.

Aturan:
- satu row, tidak pecah;
- target tinggi total **14–17 mm**;
- Tanggal/Nilai/TTD wajib terlihat dan bisa ditulis;
- TTD paling lebar;
- QR target **12–14 mm** + quiet zone putih;
- brand RIQA OS di kanan QR;
- tidak ada metadata AUDIT/path/PAGE_REGISTER/debug pada halaman cetak;
- tidak ada motto/brand tercecer di area lain;
- footer tidak boleh memakai ruang lebih besar daripada yang dibutuhkan.

# 10. Ornamen
Ornamen adalah prioritas terakhir. Jika halaman belum proporsional atau latihan masih terlalu kecil, ornamen bawah harus dihapus. Ornamen tidak boleh menciptakan margin kosong tambahan.

# 11. Aturan implementasi generator
Generator wajib menggunakan satu page-layout terukur dan footer berada di dalam setiap article/page.

Wajib:
- `box-sizing:border-box` pada komponen utama;
- `overflow` tidak boleh menyembunyikan materi wajib;
- practice menjadi area fleksibel utama;
- tidak memakai absolute positioning untuk mengisi layout utama;
- tidak memakai negative margin/transform untuk mengejar tampilan;
- semua halaman tetap tepat satu page A5.

Pipeline wajib assertion:
- tepat 8×3 latihan pada halaman reguler;
- contoh/penanaman ada dan memenuhi ukuran minimum pada halaman yang membutuhkan;
- Tanggal/Nilai/TTD ada;
- tepat satu footer per halaman;
- tidak ada legacy activity box;
- tidak ada metadata teknis tercetak;
- tidak ada overflow ke halaman berikutnya.

# 12. Visual density gate
Selain assertion DOM, audit visual wajib menilai **kepadatan halaman**.

PASS bila:
- tidak ada blok kosong besar;
- contoh materi tampak besar/utama;
- latihan Tartil jelas dominan;
- 8 baris menyebar proporsional pada area latihan;
- bagian bawah kompak dan rapi;
- halaman terasa sebagai lembar belajar yang utuh, bukan konten yang menumpuk di atas dengan ruang kosong di bawah.

# 13. Sampel audit wajib
Audit minimal P001, P002, P010, P014, P020, P030, P040.

Pada setiap sampel periksa:
- ukuran contoh ≥30 pt secara aturan CSS/render;
- latihan ≥28 pt secara aturan CSS/render;
- harakat tidak clipping;
- Ha dua lubang bila muncul;
- tidak ada dead space > kira-kira satu baris latihan;
- footer lengkap dan tidak dominan;
- tidak ada overlap;
- panel integrasi terbaca;
- KFGQPC Uthman Taha tertanam.

# 14. Gate FINAL
**CURRICULUM PASS → DOMAIN PASS → PAGE REGISTER PASS → CONTENT FREEZE → GLYPH PASS → DENSITY PASS → LAYOUT PASS → PDF PASS.**

Satu kegagalan = belum FINAL.

# 15. Changelog
## v1.5 — 2026-09-17
- Menetapkan anti-dead-space sebagai aturan resmi.
- Memindahkan ruang kosong kembali ke contoh dan latihan Tartil.
- Menetapkan contoh/penanaman minimum 30 pt, ideal 32–36 pt.
- Menetapkan latihan Tartil minimum 28 pt, ideal 30–34 pt.
- Menetapkan latihan sebagai area fleksibel utama ±50–58% halaman.
- Memadatkan footer menjadi 14–17 mm.
- Menambah DENSITY PASS sebelum LAYOUT PASS.

## v1.4.3 — 2026-09-17
- Mengunci Tanggal, Nilai, TTD dan footer proporsional.

## v1.4.2 — 2026-09-17
- Mengunci footer satu row dan melarang metadata audit tercetak.

## v1.4 — 2026-09-17
- Menghapus zona Aktivitas Bi'ah bawah dan memperkuat glyph gate Ha dua lubang.

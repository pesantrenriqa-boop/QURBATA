# QURBATA TARTIL — ATURAN PENYUSUNAN BUKU

Status: **FROZEN v1.5.1**
Effective: 2026-09-17
Authority: **BOOK COMPOSITION MASTER**
Scope: penyusunan isi, tipografi latihan, glyph Arab, proporsi halaman, dan layout seluruh Buku QURBATA Tartil

> v1.5.1 menggantikan aturan layout v1.5 dan seluruh v1.4.x. Seluruh PDF sebelumnya berstatus AUDIT/OBSOLETE sampai diregenerasi dan lolos visual gate v1.5.1.

# 1. Prinsip utama — LATIHAN BACA HARUS BESAR, JELAS, DAN PROPORSIONAL
Tujuan halaman adalah membuat santri mudah melihat, menirukan, dan membaca latihan Tartil pada ukuran cetak A5. Ukuran huruf tidak dinilai dari angka pt semata, tetapi dari hasil render nyata.

Prinsip resmi:
**besar ≠ memenuhi halaman secara paksa. Besar berarti glyph dan harakat mudah dibaca, memiliki ruang aman, seimbang dengan grid, dan tetap nyaman dipandang.**

# 2. Hierarki visual wajib
Urutan dominasi:
**Contoh/Penanaman Kompetensi → Latihan Tartil → Panel Tahfidz–Bi'ah–Akhlak → Footer administrasi/RIQA OS → Ornamen.**

Contoh dan latihan Tartil bersama-sama harus menguasai sekitar **60–65% area belajar efektif** pada halaman reguler.

# 3. Contoh / penanaman kompetensi — BESAR DAN MENONJOL
Contoh adalah objek pertama yang ditiru santri.

Aturan:
- font Arab wajib KFGQPC Uthman Taha;
- target awal **36–40 pt** pada A5;
- boleh lebih besar daripada latihan reguler;
- minimal dua baris penanaman pada halaman yang memang membutuhkan penanaman menurut page register;
- harakat harus utuh dan jelas;
- tidak boleh menyentuh border;
- tidak boleh diperkecil demi mempertahankan ornamen/footer yang terlalu besar;
- ukuran final ditentukan melalui render audit, bukan hanya nilai CSS.

# 4. Latihan Tartil — BESAR, JELAS, PROPORSIONAL
Struktur tetap **8 baris × 3 kelompok = 24 kelompok** pada halaman reguler.

## 4.1 Target ukuran
- target awal render **32–36 pt**;
- angka tersebut bukan kewajiban kaku: generator boleh menyesuaikan dalam rentang aman berdasarkan bentuk glyph dan harakat;
- tidak boleh turun di bawah **30 pt** pada halaman reguler tanpa alasan khusus yang terdokumentasi;
- bila masih ada dead space dan glyph aman, ukuran/tinggi row harus dinaikkan sebelum ruang dibiarkan kosong.

## 4.2 Proporsi cell dan row
- 3 kolom harus memiliki lebar seimbang;
- 8 row harus menyebar merata secara vertikal;
- tinggi row mengikuti area latihan yang tersedia, bukan tinggi konten minimum;
- glyph harus center horizontal dan vertikal;
- setiap glyph memiliki breathing room atas/bawah agar fathah/kasrah/dhammah tidak menyentuh garis;
- garis grid tipis dan tidak mengalahkan visual huruf;
- padding tidak boleh terlalu sempit dan tidak boleh terlalu besar sampai menciptakan ruang mubazir.

## 4.3 Visual reading gate
Latihan dinyatakan PASS hanya bila pada PDF A5 100%:
- glyph dapat dikenali dengan cepat;
- harakat dapat dibedakan tanpa zoom digital;
- tiga kelompok per baris tidak terasa sesak;
- jarak glyph ke border aman;
- ukuran antarhalaman konsisten secara visual;
- tidak ada clipping/overlap;
- ukuran tidak tampak kecil sementara halaman masih memiliki ruang kosong besar.

# 5. Distribusi vertikal halaman reguler
Target area efektif:
- header/judul/kompetensi: **±6–8%**;
- contoh/penanaman: **±12–15%**;
- latihan Tartil 8×3: **±50–55%**;
- panel Tahfidz–Bi'ah–Akhlak: **±10–12%**;
- footer: **±8–10%**;
- breathing room/gap total: **maksimum ±5%**, tersebar antarbagian.

Proporsi dapat bergeser sedikit sesuai halaman, tetapi contoh + latihan harus tetap sekitar **60–65%** dari area belajar efektif.

# 6. Anti-dead-space — RUANG KOSONG DIKEMBALIKAN KE PEMBELAJARAN
Dilarang ada blok kosong vertikal tanpa fungsi yang lebih tinggi dari kira-kira satu row latihan.

Jika ruang tersisa, alokasi wajib berurutan:
1. tambah tinggi row latihan;
2. naikkan ukuran latihan dalam rentang aman;
3. perbesar contoh/penanaman;
4. tambah breathing room glyph/harakat;
5. perjelas panel integrasi;
6. sisanya baru menjadi whitespace fungsional.

Tidak boleh mengisi dead space dengan ornamen baru.

# 7. Sistem layout halaman
Generator wajib memakai layout vertikal terukur:
`header | planting/example | integration | practice | footer`
atau urutan ekuivalen yang ditetapkan master halaman, dengan **practice sebagai area fleksibel utama**.

Dilarang fixed-height/margin lama yang menyebabkan konten menumpuk di atas dan meninggalkan ruang putih besar di bawah.

# 8. Ha dua lubang — GLYPH GATE
Seluruh ه detached pada materi Tartil wajib tampil sebagai Ha dua lubang. Audit harus visual; Unicode scan saja tidak cukup. Ha satu lubang pada latihan, judul, contoh/penanaman, evaluasi, atau checkpoint = FAIL.

# 9. Panel Tahfidz – Bi'ah Arabiyah – Akhlak
- ringkas dan terbaca;
- Arab + arti Indonesia jelas;
- tidak boleh menyebabkan contoh/latihan mengecil;
- Bi'ah adalah bahasa instruksional;
- tidak ada zona `Aktivitas Bi'ah QURBATA` atau kotak aktivitas kosong.

# 10. Footer resmi — KOMPAK, LENGKAP, TIDAK MENGAMBIL AREA LATIHAN
Urutan satu row:
**ID halaman | Tanggal | Nilai | TTD | QR | RIQA OS**.

Aturan:
- tinggi target **14–16 mm**;
- Tanggal/Nilai/TTD wajib tampil dan bisa ditulis;
- TTD paling lebar;
- QR target **12–13 mm** + quiet zone;
- brand/motto hanya satu kali, di kanan QR;
- tidak ada brand/motto duplikat di kiri/kanan bawah;
- tidak ada metadata AUDIT/PAGE_REGISTER/path/debug pada halaman;
- footer tidak boleh mendorong latihan menjadi kecil atau menciptakan dead space.

# 11. Ornamen
Ornamen adalah prioritas terakhir. Jika latihan belum besar/proporsional atau masih ada masalah density, ornamen dihapus. Tidak boleh ada margin tambahan hanya untuk ornamen.

# 12. Implementasi generator
Wajib:
- satu page-layout terukur per article;
- `box-sizing:border-box`;
- practice menggunakan area fleksibel (`minmax(0,1fr)`/flex-grow ekuivalen);
- 8 row memakai distribusi tinggi merata;
- glyph center pada cell;
- tidak memakai absolute positioning/negative margin/transform untuk layout utama;
- footer berada di dalam page/article;
- satu halaman tepat satu A5.

Generator tidak boleh mengunci satu ukuran font sebagai satu-satunya kebenaran. Target 32–36 pt harus divalidasi terhadap render. Bila 36 pt clipping, turun seperlunya; bila 32 pt masih tampak kecil dan ada ruang, naikkan.

# 13. Build assertions
Pipeline wajib memeriksa:
- tepat 8×3 pada halaman reguler;
- contoh/penanaman ada pada halaman yang membutuhkannya;
- aturan CSS latihan tidak di bawah 30 pt tanpa exception terdokumentasi;
- Tanggal/Nilai/TTD ada;
- tepat satu footer;
- tidak ada activity box lama;
- tidak ada metadata teknis tercetak;
- tidak overflow ke halaman berikutnya.

# 14. Visual audit wajib
Sampel minimal: **P001, P002, P010, P014, P020, P030, P040**.

Audit dilakukan pada render A5, bukan hanya source/CSS. Periksa:
- contoh tampak jelas lebih menonjol;
- latihan besar dan nyaman dibaca;
- harakat jelas pada tampilan 100%;
- 8 row tersebar proporsional;
- tidak ada dead space besar;
- Ha dua lubang bila muncul;
- panel integrasi terbaca;
- footer lengkap tetapi tidak dominan;
- QR tidak overlap;
- tidak ada motto/brand duplikat;
- KFGQPC Uthman Taha tertanam.

# 15. Gate FINAL
**CURRICULUM PASS → DOMAIN PASS → PAGE REGISTER PASS → CONTENT FREEZE → GLYPH PASS → READING-SIZE PASS → DENSITY PASS → LAYOUT PASS → PDF PASS.**

Satu kegagalan = belum FINAL.

# 16. Changelog
## v1.5.1 — 2026-09-17
- Mengunci prinsip `besar, jelas, proporsional`, bukan sekadar font sebesar mungkin.
- Target contoh/penanaman 36–40 pt.
- Target latihan 32–36 pt; minimum reguler 30 pt tanpa exception.
- Contoh + latihan ditargetkan 60–65% area belajar efektif.
- Memprioritaskan tinggi row dan ukuran glyph ketika terdapat dead space.
- Menambah READING-SIZE PASS pada gate FINAL.
- Mewajibkan audit keterbacaan pada PDF A5 100%.
- Mempertegas penghapusan brand/motto footer duplikat.

## v1.5 — 2026-09-17
- Anti-dead-space dan latihan sebagai area fleksibel utama.

## v1.4.3 — 2026-09-17
- Mengunci Tanggal, Nilai, TTD dan footer proporsional.

## v1.4 — 2026-09-17
- Menghapus zona Aktivitas Bi'ah bawah dan memperkuat glyph gate Ha dua lubang.

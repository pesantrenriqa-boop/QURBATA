# QURBATA TARTIL — ATURAN PENYUSUNAN BUKU

Status: **FROZEN v1.5.3**
Effective: 2026-09-17
Authority: **BOOK COMPOSITION MASTER**
Scope: penyusunan isi, tipografi latihan, glyph Arab, proporsi halaman, dan layout seluruh Buku QURBATA Tartil

> v1.5.3 menggantikan layout v1.5.2 dan seluruh versi sebelumnya. PDF sebelumnya berstatus AUDIT/OBSOLETE sampai diregenerasi dan lolos visual gate v1.5.3.

# 1. Prinsip utama — BACAAN BESAR DIPERTAHANKAN, RUANG HALAMAN YANG DIPERBAIKI
Hasil audit visual v1.5.1 menunjukkan ukuran bacaan Tartil sudah mendekati ukuran yang diinginkan. Karena itu koreksi berikutnya **tidak boleh menyelesaikan masalah layout dengan mengecilkan huruf latihan**.

Prinsip resmi v1.5.3:
**pertahankan keterbacaan glyph; perbaiki distribusi tinggi row dan struktur vertikal halaman.**

# 2. Hierarki visual
Urutan dominasi:
**Contoh/Penanaman → Latihan Tartil → Panel Tahfidz–Bi'ah–Akhlak → Footer administrasi/RIQA OS → Ornamen.**

Contoh + latihan harus menjadi mayoritas area belajar efektif dan halaman tidak boleh terlihat `padat di atas – kosong di bawah`.

# 3. Contoh / penanaman
- KFGQPC Uthman Taha wajib.
- Target **36–40 pt**.
- Contoh harus lebih menonjol daripada teks pendukung.
- Harakat utuh, tidak clipping, dan tidak menyentuh border.
- Beri ruang vertikal yang cukup agar tahap `lihat/tirukan` terasa jelas.
- Jangan memperbesar panel pendukung dengan mengambil ruang contoh.


# 3A. CONTOH/PENANAMAN ADALAH KOMPONEN WAJIB — TIDAK BOLEH HILANG
Hasil audit PDF v1.5.2 menunjukkan bahwa koreksi density dapat mendesak atau menghilangkan contoh/penanaman. Hal ini dinyatakan **EXAMPLE GATE FAIL**.

Aturan resmi:
- setiap halaman yang menurut page register memiliki materi/kompetensi baru WAJIB menampilkan blok contoh/penanaman;
- blok contoh harus berada di antara Header/Kompetensi dan Panel Integrasi, sebelum latihan 8×3;
- blok contoh memiliki **reserved row/track sendiri** dan tidak boleh digabung ke track auto yang dapat runtuh;
- tinggi efektif minimum blok contoh reguler **18 mm**, target **20–24 mm** bila dua baris penanaman diperlukan;
- glyph contoh target **36–40 pt** dan tidak boleh lebih kecil daripada 34 pt tanpa exception terdokumentasi;
- minimal isi contoh mengikuti page register; generator dilarang membuat placeholder kosong;
- contoh tidak boleh dihapus oleh normalisasi DOM, selector legacy, overflow, clipping, atau optimasi density;
- overflow hidden pada ancestor tidak boleh memotong contoh/harakat;
- jika ruang halaman kurang, kompres ornamen/footer/gap lebih dahulu, lalu tinggi row latihan secara proporsional; **contoh tidak boleh dikorbankan**;
- halaman review/evaluasi yang memang tidak mensyaratkan penanaman harus mengikuti page register dan tidak dipaksa memiliki contoh palsu.

## 3A.1 Assertion wajib contoh
Sebelum render, generator harus memeriksa setiap halaman terhadap page register:
1. apakah halaman membutuhkan contoh/penanaman;
2. bila ya, blok contoh harus ada dan berisi teks Arab non-kosong;
3. declared/computed font-size memenuhi minimum;
4. blok tidak display:none, tidak memiliki tinggi nol, dan tidak berada di luar article;
5. kegagalan satu poin harus membuat build **FAIL**, bukan menghasilkan PDF.

## 3A.2 Visual gate contoh
Pada audit PDF A5 100%, contoh harus langsung terlihat sebagai tahap lihat/tirukan sebelum latihan, lebih menonjol daripada panel integrasi, memiliki harakat utuh dan breathing room, tidak terpotong, serta tetap hadir setelah koreksi density.

# 4. Latihan Tartil — ukuran v1.5.1 dipertahankan sebagai baseline
Struktur reguler tetap **8 baris × 3 kelompok = 24 kelompok**.

## 4.1 Ukuran bacaan
- Baseline visual hasil v1.5.1 sekitar **34 pt** dipertahankan sebagai titik awal.
- Rentang audit aman **32–36 pt**.
- Minimum reguler **30 pt** hanya bila benar-benar diperlukan karena glyph/harakat tertentu dan harus terdokumentasi.
- Koreksi dead space **tidak boleh dimulai dengan menambah atau mengurangi font secara agresif**.

## 4.2 Yang diperbesar adalah tinggi area latihan
Bila terdapat ruang putih besar setelah tabel latihan:
1. **perpanjang tinggi keseluruhan practice-grid**;
2. distribusikan tambahan tinggi itu secara merata ke 8 row;
3. pertahankan glyph center vertikal/horizontal;
4. pertahankan ukuran font sekitar baseline;
5. gunakan tambahan ruang sebagai breathing room atas/bawah glyph dan harakat.

Dengan demikian bacaan tetap besar tetapi tidak tampak sesak atau terlalu besar.

## 4.3 Tinggi row
- Delapan row harus mengisi area latihan dari awal sampai mendekati footer/panel berikutnya.
- Semua row reguler memiliki tinggi visual yang konsisten.
- Target tinggi row ditentukan dari sisa area halaman, bukan `content-height` glyph.
- Tidak boleh ada blok kosong setelah row ke-8 yang lebih tinggi daripada kira-kira **0,5 row latihan**.
- Gap antara akhir practice-grid dan footer/panel berikutnya target **2–5 mm**, kecuali checkpoint memerlukan struktur khusus.

# 5. Distribusi vertikal halaman — dikoreksi dari hasil audit v1.5.1
Halaman reguler A5 harus menggunakan tinggi efektif secara nyata, bukan sekadar persentase teoritis.

Target:
- header + judul kompetensi: **±7–9%**;
- contoh/penanaman: **±11–14%**;
- panel Tahfidz–Bi'ah–Akhlak: **±10–12%**;
- latihan Tartil: **±52–58%**;
- footer: **±7–9%**;
- seluruh gap/breathing room di luar cell: **maksimum ±4%**.

Practice-grid adalah **row fleksibel utama** dan harus menerima sisa tinggi halaman setelah komponen lain dihitung.

# 6. ANTI-DEAD-SPACE GATE — diperketat
Hasil seperti v1.5.1 yang memiliki ruang putih besar antara akhir latihan dan footer dinyatakan **DENSITY FAIL**.

Aturan:
- tidak boleh ada blank vertical band > ±0,5 tinggi row latihan reguler;
- tidak boleh ada `spacer`, min-height, fixed grid track, legacy footer slot, atau margin yang menyimpan ruang kosong tersembunyi;
- ruang sisa wajib masuk ke `practice-grid`/tinggi row;
- ornamen tidak boleh dipakai untuk menyamarkan ruang kosong.

# 7. Urutan struktur halaman
Untuk halaman reguler, struktur visual harus konsisten:
**Header/Kompetensi → Contoh/Penanaman (reserved, wajib bila page register mensyaratkan) → Panel Integrasi → Latihan Tartil → Footer.**

Bila source lama mempunyai urutan berbeda, generator boleh menormalisasi DOM selama substansi kurikulum tidak berubah.

Tidak boleh ada elemen kosong/legacy di antara Practice dan Footer.

# 8. Panel Tahfidz – Bi'ah Arabiyah – Akhlak
Hasil v1.5.1 menunjukkan ukuran panel sudah cukup. Maka:
- panel **tidak perlu diperbesar** hanya untuk mengisi halaman;
- tetap ringkas dan terbaca;
- Arab + arti Indonesia jelas;
- tinggi panel konsisten;
- tidak mengambil ruang yang seharusnya menjadi practice-grid.

# 9. Ha dua lubang — GLYPH GATE
Seluruh ه detached pada materi Tartil wajib tampil sebagai Ha dua lubang. Audit visual wajib; Unicode scan tidak cukup. Satu Ha detached satu-lubang = GLYPH FAIL.

# 10. Footer — satu sistem, tidak mengambang
Footer wajib menjadi **satu komponen visual utuh** dan berada segera setelah practice-grid dengan gap kecil.

Urutan:
**ID | Tanggal | Nilai | TTD | QR | RIQA OS**.

Aturan:
- target tinggi **14–16 mm**;
- Tanggal/Nilai/TTD tetap wajib;
- field cukup untuk tulisan pena, TTD paling lebar;
- QR **12–13 mm** + quiet zone;
- motto + RIQA OS hanya **satu kali**, di dalam kolom brand resmi;
- **hapus seluruh motto/brand legacy di luar footer**;
- tidak boleh ada identitas kecil mengambang di kiri bawah, kanan atas footer, atau kanan bawah terpisah;
- QR yang gagal dimuat tidak boleh menyebabkan seluruh footer hilang;
- tidak ada metadata AUDIT/PAGE_REGISTER/path/debug.

# 11. Footer QR gate
Jika desain resmi halaman mensyaratkan QR, visual audit harus memastikan QR benar-benar terlihat pada PDF. Selector/source QR yang gagal sehingga kolom QR kosong = **FOOTER FAIL**. Sumber QR harus stabil dan eksplisit di generator, bukan bergantung pada pencarian elemen legacy yang sudah dihapus.

# 12. Ornamen
Ornamen prioritas terakhir dan boleh dihilangkan sepenuhnya. Tidak boleh membuat ruang bawah tambahan.

# 13. Implementasi generator — koreksi wajib sebelum produksi berikutnya
Generator berikutnya harus:
- menghitung tinggi page/article yang benar-benar tersedia pada A5;
- memakai satu grid vertikal terukur;
- memastikan `practice` adalah `minmax(0,1fr)` / flex-grow utama;
- memastikan parent/container practice juga memiliki tinggi yang dapat diwariskan; `height:100%` tanpa definite parent height tidak dianggap solusi;
- menghapus fixed/min-height/margin/spacer legacy yang berada setelah practice;
- menempatkan footer sebagai row terakhir di grid halaman, bukan elemen yang mengambang di flow lain;
- mendistribusikan 8 row dengan `repeat(8,minmax(0,1fr))` setelah tinggi practice definitif tersedia;
- tidak memakai absolute positioning/negative margin/transform untuk menutup dead space;
- mempertahankan ukuran bacaan sekitar 34 pt sebagai baseline audit.

# 14. Build assertions
Sebelum PDF dibuat, pipeline wajib memeriksa:
- tepat 8×3 pada halaman reguler;
- contoh/penanaman tersedia sesuai page register, berisi Arab non-kosong, memiliki reserved height, dan tidak collapse/hidden;
- font latihan tidak di bawah 30 pt tanpa exception;
- tepat satu footer resmi;
- Tanggal/Nilai/TTD ada;
- QR ada bila diwajibkan;
- tidak ada legacy activity box;
- tidak ada legacy motto/brand di luar footer;
- tidak ada metadata teknis tercetak;
- tidak overflow ke halaman berikutnya.

# 15. Visual audit v1.5.3
Sampel wajib: **P001, P002, P010, P014, P020, P030, P040**.

Pada setiap sampel:
- ukuran bacaan harus setara/lebih nyaman daripada v1.5.1, bukan lebih kecil secara mencolok;
- contoh besar dan jelas;
- 8 row lebih tinggi dan tersebar merata;
- gap setelah latihan maksimal sekitar 2–5 mm pada halaman reguler;
- tidak ada blank band besar;
- footer tampak satu sistem utuh;
- Tanggal/Nilai/TTD nyaman digunakan;
- QR terlihat dan tidak overlap;
- hanya satu motto/brand RIQA OS;
- Ha detached dua lubang bila muncul;
- panel integrasi terbaca;
- KFGQPC Uthman Taha tertanam;
- halaman tepat A5 dan tidak overflow.

# 16. Status gate berdasarkan audit v1.5.1
- **READING-SIZE:** mendekati PASS / baseline dipertahankan.
- **DENSITY:** FAIL — dead space besar setelah latihan.
- **FOOTER:** FAIL — sistem brand/QR belum stabil dan elemen masih terfragmentasi.
- **LAYOUT:** FAIL sampai Density + Footer lulus.

# 17. Gate FINAL
**CURRICULUM PASS → DOMAIN PASS → PAGE REGISTER PASS → CONTENT FREEZE → GLYPH PASS → EXAMPLE PASS → READING-SIZE PASS → DENSITY PASS → FOOTER PASS → LAYOUT PASS → PDF PASS.**

Satu kegagalan = belum FINAL.

# 18. Changelog
## v1.5.3 — 2026-09-17
- Membekukan hasil evaluasi visual v1.5.1 sebagai dasar koreksi.
- Mempertahankan baseline latihan sekitar 34 pt; koreksi difokuskan pada tinggi row.
- Menetapkan blank band > ±0,5 row sebagai DENSITY FAIL.
- Menetapkan gap practice→footer target 2–5 mm.
- Menegaskan practice membutuhkan definite available height; `height:100%` tanpa parent height tidak cukup.
- Panel integrasi dipertahankan ringkas, tidak dibesarkan untuk mengisi ruang.
- Footer wajib satu sistem; semua brand/motto legacy di luar footer dihapus.
- QR wajib benar-benar tampil bila disyaratkan; kolom QR kosong = FOOTER FAIL.
- Menambahkan FOOTER PASS ke gate FINAL.

## v1.5.1 — 2026-09-17
- Prinsip besar, jelas, proporsional; target latihan 32–36 pt.

## v1.5 — 2026-09-17
- Anti-dead-space dan practice sebagai area fleksibel utama.

## v1.4.3 — 2026-09-17
- Tanggal/Nilai/TTD dan footer proporsional.


## v1.5.3 — 2026-09-18
- Membekukan temuan audit v1.5.2 bahwa contoh/penanaman dapat terdesak atau hilang.
- Menjadikan contoh/penanaman sebagai reserved layout track yang tidak boleh collapse.
- Menetapkan tinggi minimum 18 mm dan target 20–24 mm untuk blok contoh reguler.
- Menetapkan contoh 36–40 pt, minimum 34 pt tanpa exception.
- Menambahkan assertion berbasis page register: contoh wajib ada, non-kosong, visible, dan berada di dalam article.
- Menambahkan **EXAMPLE PASS** ke gate FINAL sebelum READING-SIZE dan DENSITY.

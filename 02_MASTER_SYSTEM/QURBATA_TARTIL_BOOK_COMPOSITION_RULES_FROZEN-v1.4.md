# QURBATA TARTIL — ATURAN PENYUSUNAN BUKU

Status: **FROZEN v1.5.4**
Effective: 2026-09-17
Authority: **BOOK COMPOSITION MASTER**
Scope: penyusunan isi, tipografi latihan, glyph Arab, proporsi halaman, dan layout seluruh Buku QURBATA Tartil

> v1.5.4 menggantikan layout v1.5.3 dan seluruh versi sebelumnya. PDF sebelumnya berstatus AUDIT/OBSOLETE sampai diregenerasi dan lolos visual gate v1.5.4.

# 1. Prinsip utama — BACAAN BESAR DIPERTAHANKAN, RUANG HALAMAN YANG DIPERBAIKI
Hasil audit visual v1.5.1 menunjukkan ukuran bacaan Tartil sudah mendekati ukuran yang diinginkan. Karena itu koreksi berikutnya **tidak boleh menyelesaikan masalah layout dengan mengecilkan huruf latihan**.

Prinsip resmi v1.5.4:
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


# 3B. SOURCE-CONTENT GATE — BLOK ADA TETAPI KOSONG = FAIL
Audit PDF v1.5.3 membuktikan bahwa keberadaan class/box contoh tidak membuktikan adanya materi contoh. Karena itu v1.5.4 membedakan **struktur** dan **isi**.

Aturan wajib:
- contoh/penanaman harus bersumber dari materi kompetensi pada Page Register/Master Curriculum, bukan dibuat sebagai box kosong oleh layout;
- generator wajib memasukkan/menjaga **teks Arab contoh yang nyata** sebelum tahap layout;
- untuk halaman yang membutuhkan contoh, setelah normalisasi DOM isi teks blok contoh harus memiliki minimal satu karakter Arab (rentang Unicode Arab), bukan hanya label, whitespace, `<br>`, border, atau placeholder;
- assertion tidak boleh hanya menghitung class `planting`, `intro-pair`, atau `lesson-heading`;
- bila source halaman belum mempunyai materi contoh, build harus berhenti dengan `EXAMPLE_CONTENT_MISSING` dan menyebut nomor halaman;
- layout tidak boleh mengarang contoh yang tidak tercatat pada Page Register; jika mapping belum tersedia, mapping Page Register harus diperbaiki dahulu;
- P001 wajib menjadi sentinel visual/content: contoh kompetensi awal harus benar-benar terlihat sebagai **بَ تَ ثَ** sesuai materi awal; kegagalan P001 otomatis menggagalkan seluruh build;
- halaman penanaman Kasrah/Dhammah wajib menampilkan contoh perubahan harakat sesuai Page Register, bukan hanya judul kosong;
- checkpoint/evaluasi mengikuti Page Register dan boleh tidak memiliki blok penanaman hanya jika secara eksplisit ditandai demikian.

## 3B.1 Assertion konten minimum
Untuk setiap halaman `exampleRequired=true`:
1. temukan blok contoh yang benar;
2. ambil `textContent` setelah tag dibersihkan;
3. normalisasi whitespace;
4. pastikan terdapat karakter Arab `/[\\u0600-\\u06FF]/`;
5. pastikan isi bukan hanya label generik;
6. P001 harus memuat بَ, تَ, ثَ;
7. jika gagal: **BUILD FAIL — EXAMPLE_CONTENT_MISSING**.

Gate ini harus dijalankan **sebelum PDF render** dan diverifikasi lagi secara visual sesudah render.

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
- contoh/penanaman tersedia sesuai page register, memiliki teks Arab nyata non-kosong, reserved height, dan tidak collapse/hidden;
- P001 sentinel memuat contoh بَ تَ ثَ;
- font latihan tidak di bawah 30 pt tanpa exception;
- tepat satu footer resmi;
- Tanggal/Nilai/TTD ada;
- QR ada bila diwajibkan;
- tidak ada legacy activity box;
- tidak ada legacy motto/brand di luar footer;
- tidak ada metadata teknis tercetak;
- tidak overflow ke halaman berikutnya.

# 15. Visual audit v1.5.4
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
**CURRICULUM PASS → DOMAIN PASS → PAGE REGISTER PASS → CONTENT FREEZE → SOURCE-CONTENT PASS → GLYPH PASS → EXAMPLE PASS → READING-SIZE PASS → DENSITY PASS → FOOTER PASS → LAYOUT PASS → PDF PASS.**

Satu kegagalan = belum FINAL.

# 18. Changelog
## v1.5.4 — 2026-09-17
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


## v1.5.4 — 2026-09-18
- Membekukan temuan audit v1.5.2 bahwa contoh/penanaman dapat terdesak atau hilang.
- Menjadikan contoh/penanaman sebagai reserved layout track yang tidak boleh collapse.
- Menetapkan tinggi minimum 18 mm dan target 20–24 mm untuk blok contoh reguler.
- Menetapkan contoh 36–40 pt, minimum 34 pt tanpa exception.
- Menambahkan assertion berbasis page register: contoh wajib ada, non-kosong, visible, dan berada di dalam article.
- Menambahkan **EXAMPLE PASS** ke gate FINAL sebelum READING-SIZE dan DENSITY.


## v1.5.4 — 2026-09-18
- Menyatakan v1.5.3 gagal karena blok contoh dapat ada secara struktural tetapi kosong secara isi.
- Menambahkan SOURCE-CONTENT GATE berbasis teks Arab nyata, bukan keberadaan class.
- Menetapkan P001 sebagai sentinel: wajib memuat contoh بَ تَ ثَ.
- Build wajib berhenti dengan EXAMPLE_CONTENT_MISSING bila materi contoh yang diwajibkan kosong.
- Layout dilarang mengarang materi; sumber contoh harus berasal dari Page Register/Master Curriculum.


## v1.6.0 — 2026-09-20 — P001 PAGED.JS VISUAL MASTER FROZEN

Status: **APPROVED / FROZEN**  
Approved reference: **QURBATA Jilid 1 P001 — Paged.js Build #21**  
Reference commit: `13e3c0cc3805b52f45076fcf918c2a19c5efa982`

P001 Build #21 ditetapkan sebagai **master visual produksi** untuk halaman reguler Jilid 1. Proporsi yang telah disetujui tidak boleh diubah ketika memproduksi halaman berikutnya.

Komponen yang dibekukan:
- header satu baris: logo QURBATA + wordmark QURBATA;
- sublabel kecil: `Quran · Bahasa Arab · Tahfidz · Akhlak`;
- badge Jilid dan nomor halaman;
- proporsi header, margin, frame, dan ornamen;
- blok contoh/penanaman;
- panel integrasi Tahfidz–Bahasa Arab–Akhlak;
- area latihan Tartil **8 baris × 3 kelompok**;
- font Arab **KFGQPC Uthman Taha** dan skala visual yang telah lolos P001;
- footer Tanggal–Nilai–TTD, QR/RIQA OS, motto, serta jarak vertikalnya;
- distribusi ruang halaman dan keseluruhan komposisi A5.

Untuk P002 dan seterusnya, **layout tidak didesain ulang**. Renderer wajib memakai master P001 ini dan hanya mengganti konten yang ditentukan oleh Master Curriculum, Page Register, dan Content Freeze halaman terkait. Perubahan layout master memerlukan audit visual baru dan persetujuan eksplisit.

Gate tambahan:
**P001 VISUAL MASTER MATCH → CONTENT-SPECIFIC PAGE GATES → PDF PASS.**


## v1.6.1 — 2026-09-20 — KOREKSI WAJIB SEBELUM PRODUKSI LANJUT

Berdasarkan audit visual PDF P001–P010, master P001 v1.6.0 tetap menjadi basis dan seluruh elemen yang tidak disebut di bawah tetap **FROZEN**. Tiga koreksi berikut wajib diterapkan pada renderer sebelum PDF produksi berikutnya:

1. **Kompaksi area atas.** Header, blok contoh/penanaman, dan panel integrasi Tahfidz–Bi'ah Arabiyah–Akhlak harus ditata lebih hemat tinggi tanpa mengurangi keterbacaan. Ruang yang diperoleh dialihkan ke area latihan Tartil sehingga latihan menjadi lebih besar/dominan.
2. **Safe area glyph latihan.** Huruf/harakat latihan tidak boleh menyentuh, tertutup, atau terpotong garis kotak/grid. Setiap cell wajib memiliki ruang aman vertikal dan horizontal; line-height, alignment, padding, dan tinggi row harus diuji pada glyph berharakat. **GLYPH PASS gagal bila satu huruf/harakat pun bersinggungan dengan border.**
3. **Logo QURBATA.** Mark QURBATA di header wajib memakai bentuk QOf/Q yang **berlubang (counter terbuka/terlihat)** sesuai identitas logo yang disetujui; bentuk dengan lubang tertutup/terisi dilarang.

Setelah ketiga koreksi diterapkan, halaman P001 menjadi sentinel audit ulang. Produksi P001–P010 hanya dilanjutkan setelah sentinel memenuhi: **HEADER-DENSITY PASS → LOGO PASS → GLYPH-SAFE PASS → LAYOUT PASS → PDF PASS**.


---

## FREEZE v1.6.2 — APPROVED P001–P010 PRODUCTION BASELINE

**Effective:** 2026-09-21  
**Approved reference:** Paged.js Build #31  
**Approved commit:** `4c4ccf623f092e67c34bfff393a50be92d7d673b`

Build #31 ditetapkan sebagai baseline baku untuk kelanjutan produksi Jilid 1. Ketentuan berikut **FROZEN** dan tidak boleh berubah tanpa keputusan revisi master terlebih dahulu:

1. **Arsitektur halaman**
   - A5 portrait.
   - Urutan: Header → Penanaman → panel Tahfidz/Bi'ah/Akhlak → latihan Tartil 8×3 → footer.
   - Tartil tetap domain visual paling dominan.
   - Layout atas menggunakan komposisi compact yang telah disetujui pada Build #31.

2. **Tipografi Arab**
   - Font produksi Arab wajib **KFGQPC Uthman Taha**.
   - Ukuran latihan dan safe-area mengikuti Build #31.
   - Glyph latihan tidak boleh menyentuh, tertutup, atau terpotong garis kotak.
   - Bentuk `ج ح خ ع غ` pada latihan menggunakan koreksi posisi vertikal seperti Build #31 agar ekor/badan bawah tidak menabrak garis.

3. **Penanaman kompetensi**
   - Ukuran penanaman halaman normal mengikuti baseline Build #31.
   - P010 `تَقْيِيمُ الْفَتْحَةِ` menggunakan ukuran khusus **33 pt**; aturan ini tidak mengubah ukuran penanaman P001–P009.

4. **Bi'ah Arabiyah**
   - Authority isi: `PAGE_REGISTER_P001-P040_INTEGRATION_FROZEN-v1.3.md`.
   - Satu materi dipertahankan **1–3 pertemuan**; tidak mengganti ungkapan baru setiap halaman.
   - Untuk P001–P010: P001–P003 salam; P004–P006 `اُنْظُرْ`; P007–P009 `اِسْتَمِعْ`; P010 reinforcement.
   - Baris kecil panel adalah **arti Indonesia**, bukan instruksi aktivitas.

5. **Akhlak**
   - Authority isi: `PAGE_REGISTER_P001-P040_INTEGRATION_FROZEN-v1.3.md`.
   - Materi Akhlak dibiasakan selama **2–3 pertemuan**, bukan nash baru setiap halaman.
   - Untuk P001–P010: P001–P003 adab salam; P004–P006 doa tambah ilmu; P007–P009 adab mendengar; P010 reinforcement.
   - Baris kecil panel adalah arti Indonesia.

6. **Footer**
   - Tanggal, Nilai, dan TTD tetap satu baseline.
   - QR mempunyai area sendiri dan tidak boleh mengganggu ruang latihan.
   - Motto bawah tetap `تَعَلَّمْ — اِعْمَلْ — عَلِّمْ`.

7. **Gate produksi lanjutan**
   - P001–P010 Build #31 menjadi **visual/content sentinel** untuk P011–P040.
   - Produksi berikut tidak boleh mengubah komponen frozen di atas secara diam-diam.
   - Setiap blok berikut wajib melewati: `REGISTER PASS → CONTENT PASS → GLYPH-SAFE PASS → LAYOUT PASS → PDF PASS`.


---

## REVISION v1.6.3 — OPEN PRACTICE FIELD + SEMANTICALLY INFORMED GROUPING

**Effective:** 2026-09-21  
**Status:** FROZEN — supersedes any earlier rule that requires visible internal cell borders in the Tartil practice area.

### 1. Practice field without internal boxes
- Area latihan tetap memiliki batas luar sebagai pengendali komposisi halaman.
- **Garis kotak/grid di antara kelompok latihan dihilangkan.**
- Struktur pedagogis **8 baris × 3 kelompok = 24 kelompok** tetap berlaku sebagai grid tak terlihat untuk alignment dan distribusi.
- Jarak putih, baseline, dan alignment menjadi pemisah antarkelompok; bukan garis kotak.
- Penghilangan garis internal tidak boleh menyebabkan kelompok huruf saling berhimpitan atau mengurangi safe-area glyph.

### 2. Semantic-first selection for 2–3 letter groups
- Pemilihan kelompok huruf **tidak boleh hanya bersifat algoritmik/acak**.
- Setelah whitelist kompetensi halaman diterapkan, generator/editor wajib terlebih dahulu mencari susunan 2–3 huruf yang:
  1. membentuk kata Arab/Qurani yang sah bila seluruh huruf dan harakatnya sudah legal pada tahap tersebut;
  2. bila kata penuh belum mungkin, **mendekati pola atau potongan bermakna** yang wajar dalam bahasa Arab/Qur'an tanpa mengklaimnya sebagai kata penuh;
  3. baru menggunakan kombinasi latihan fonetik netral untuk slot yang tersisa.
- Harakat pada kelompok tidak dibubuhkan secara sembarang untuk mengejar variasi visual. **Pilihan harakat mempertimbangkan bentuk leksikal/makna** sejauh tidak melompati kompetensi yang belum diajarkan.
- Prinsip ini berlaku terutama pada kelompok 3 huruf; kelompok 2 huruf tetap boleh berfungsi sebagai latihan diskriminasi bunyi.
- **Makna tidak boleh dipaksakan.** Jika kata bermakna memerlukan huruf, harakat, sambungan, sukun, tasydid, mad, tanwin, atau fitur yang belum legal, bentuk tersebut tidak boleh dimasukkan.
- Urutan prioritas produksi: `CURRICULUM LEGALITY → SEMANTIC VALUE → PHONETIC VARIETY → VISUAL DISTRIBUTION`.

### 3. Semantic audit metadata
Setiap halaman produksi mulai revisi ini harus dapat diaudit dengan tiga kelas kelompok:
- `WORD` = kata Arab/Qurani yang sah;
- `NEAR-SEMANTIC` = susunan yang mendekati pola/potongan bermakna tetapi tidak diklaim sebagai kata;
- `PHONETIC` = kombinasi murni untuk latihan bunyi.

Generator boleh tetap menghasilkan 24 kelompok, tetapi daftar akhir harus melewati **SEMANTIC-GROUP PASS** sebelum PDF diberi status FINAL.

### 4. Updated production gate
`REGISTER PASS → CONTENT PASS → SEMANTIC-GROUP PASS → GLYPH-SAFE PASS → OPEN-GRID PASS → LAYOUT PASS → PDF PASS`.


---

## REVISION v1.6.4 — MEANINGFUL 3-LETTER ONLY + DETACHED HA TWO-HOLE HARD GATE

**Effective:** 2026-09-21  
**Status:** FROZEN — supersedes the v1.6.3 allowance for `NEAR-SEMANTIC` three-letter groups.

### 1. Three-letter groups must be meaningful
- Setiap kelompok latihan **3 huruf wajib membentuk kata Arab yang sah dan bermakna** dengan harakat yang benar-benar tercetak.
- Prioritas kosakata: **kata yang terdapat dalam Al-Qur'an → kata Arab fusha yang sah → bentuk lain yang terverifikasi secara leksikal**.
- `NEAR-SEMANTIC` dan kombinasi fonetik acak **dilarang untuk kelompok 3 huruf**.
- Jika kompetensi halaman belum memungkinkan cukup banyak kata 3 huruf yang sah, **jangan mengarang kombinasi**. Ulangi kata sah yang tersedia dengan distribusi terkontrol, atau gunakan kelompok 2 huruf untuk latihan fonetik.
- Tidak boleh menambahkan harakat/fitur yang belum diajarkan hanya untuk membuat kata: sukun, tasydid, tanwin, mad, sambung, atau harakat tahap berikutnya tetap mengikuti whitelist kompetensi.
- Harakat dipilih karena bentuk katanya, bukan untuk variasi visual.
- Gate: setiap kelompok 3 huruf harus mempunyai metadata `WORD` dan makna/glos audit internal sebelum masuk PDF.

### 2. Detached ha must be two-hole
- Seluruh kemunculan **ha terpisah** pada latihan Tartil (`هَ / هِ / هُ / ه`) wajib tampil sebagai **ha dua lubang** sesuai master QURBATA.
- Bentuk ha satu lubang pada latihan adalah **FAIL**, walaupun berasal dari glyph default font.
- Identitas Unicode huruf tetap `ه`; dilarang mengganti dengan karakter mirip seperti `ھ / ہ / ۀ / ە`.
- Renderer wajib memakai solusi glyph/sequence/style yang mempertahankan identitas `ه` tetapi menghasilkan bentuk visual dua lubang yang disetujui.
- Sentinel audit wajib: P013, P019, P020 dan seluruh halaman yang mengandung detached ha.

### 3. P019/P020 composition
- P019 dan P020 tidak boleh menggunakan pool algoritmik mentah yang membuat latihan tampak acak/berantakan.
- P019 disusun sebagai **curated Kasrah completion page** dengan ritme visual 8×3 yang seimbang.
- P020 disusun sebagai **curated checkpoint Fathah + Kasrah**, coverage merata, bukan random cycling.
- Gate khusus: `P019-CURATED PASS → P020-CURATED PASS → HA-TWO-HOLE PASS → 3-LETTER-WORD PASS`.

### 4. Updated FINAL gate
`REGISTER PASS → CONTENT PASS → 3-LETTER-WORD PASS → HA-TWO-HOLE PASS → OPEN-GRID PASS → P019/P020-CURATED PASS → LAYOUT PASS → PDF PASS`.

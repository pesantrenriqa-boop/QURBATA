# QURBATA TARTIL — ATURAN PENYUSUNAN BUKU

Status: **FROZEN v1.4**
Effective: 2026-09-17
Authority: **BOOK COMPOSITION MASTER**
Scope: penyusunan isi, tipografi latihan, glyph Arab, dan prinsip layout seluruh Buku QURBATA Tartil
Supersedes: `QURBATA_TARTIL_BOOK_COMPOSITION_RULES_FROZEN-v1.3.md`

> Seluruh generator, layout, PDF, dan audit visual setelah keputusan ini WAJIB mengikuti v1.4. PDF v1.3 dan sebelumnya kembali berstatus AUDIT/OBSOLETE sampai diregenerasi.

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
2. Tulisan latihan membaca wajib **lebih besar daripada build v1.3 yang terakhir diaudit**; tidak boleh semakin kecil akibat pagination.
3. Ruang yang diperoleh dari penyederhanaan zona bawah wajib dialihkan terutama untuk:
   - memperbesar glyph latihan;
   - memperbesar tinggi efektif 8 baris latihan;
   - menambah jarak vertikal antarglyph/harakat;
   - menjaga jarak antarkelompok agar tidak mepet.
4. Ukuran font ditentukan bersama bounding box aktual KFGQPC Uthman Taha pada A5. Targetnya sebesar mungkin selama harakat utuh dan tidak menyentuh garis.
5. Generator dilarang memakai auto-shrink pada latihan sebagai solusi pertama untuk memenuhi satu halaman.
6. Bila konflik ruang terjadi, prioritas ruang: **Latihan Tartil → contoh/penanaman → panel materi inti → Tanggal/Nilai/TTD → footer/QR/dekorasi**.

## 6. Ha dua lubang — GLYPH GATE
1. Seluruh **ه tunggal/detached** pada materi Tartil wajib tampil sebagai **ha dua lubang** sesuai standar visual QURBATA yang telah disetujui.
2. Ha satu lubang/bulat pada latihan, judul kompetensi, penanaman, evaluasi, atau checkpoint **dilarang**.
3. Pemeriksaan Unicode saja tidak cukup. Gate harus memeriksa **hasil render/glyph visual**.
4. Bila karakter/font/shaping yang dipakai menghasilkan satu lubang, generator wajib mengganti sequence/glyph/konstruksi yang tervalidasi dua lubang tanpa mengubah bunyi/kompetensi.
5. PDF tidak boleh berstatus LAYOUT PASS sebelum contoh Ha pada halaman yang relevan diaudit visual dan benar dua lubang.

## 7. Panel Tahfidz – Bi'ah Arabiyah – Akhlak
- Tetap ringkas dan terbaca.
- Teks Arab berpasangan dengan arti Indonesia yang tepat.
- Repetisi pedagogis Bi'ah/Akhlak mengikuti master v1.3: dapat diulang 1–3 pertemuan.
- Panel tidak boleh mengambil ruang berlebihan dari latihan Tartil.

## 8. PENGHAPUSAN ZONA `AKTIVITAS BI'AH QURBATA` DI BAGIAN BAWAH
Keputusan ini **FROZEN**:
1. Heading/tulisan **`AKTIVITAS BI'AH QURBATA` di bagian bawah halaman DIHAPUS**.
2. Spasi/area kosong khusus untuk `Aktivitas Bi'ah QURBATA` di bagian bawah **DIHAPUS**.
3. Penghapusan ini tidak menghapus domain Bi'ah dari kurikulum; Bi'ah tetap berada pada panel materi dan praktik pembelajaran.
4. Ruang vertikal hasil penghapusan zona tersebut dialihkan ke latihan Tartil agar latihan lebih besar dan lebih lapang.
5. Generator tidak boleh mengganti ruang yang dibebaskan dengan ornamen atau padding baru yang tidak esensial.

## 9. Zona bawah baru — hanya Tanggal, Nilai, TTD
1. Zona administrasi bawah cukup memuat **Tanggal – Nilai – TTD**.
2. Ketiga label berada pada baseline vertikal yang konsisten.
3. Ruang tulis berada **di atas label**, bukan di bawahnya.
4. Area TTD harus realistis untuk tanda tangan pena; minimum bersih 12 mm bila memungkinkan dalam proporsi halaman.
5. Tanggal dan Nilai memiliki ruang tulis nyata tetapi boleh lebih kompak.
6. Tidak boleh ada ruang kosong besar di bawah label.
7. Tidak ada heading aktivitas di atas ketiga field.
8. QR/RIQA OS tidak boleh mengurangi latihan atau menggeser baseline TTD; bila konflik, QR/elemen digital dikompresi/dipindah lebih dahulu.

## 10. Audit page register dan isi
Page register tetap memuat kompetensi Tartil, murojaah, jenis halaman, Bi'ah, Tahfidz, Akhlak, status repetisi, dan catatan glyph/premature competency. Perubahan v1.4 adalah perubahan presentasi/layout; isi domain tetap tunduk pada master yang berlaku.

## 11. Visual gate v1.4
Sebelum PDF dinyatakan LAYOUT PASS, audit visual wajib membuktikan:
- seluruh halaman satu pertemuan/satu halaman;
- 8×3 latihan utuh;
- latihan contoh dan latihan membaca besar serta lebih lapang;
- tidak ada teks mepet, clipping, overlap, atau tabrakan harakat;
- Ha tunggal tampil **dua lubang** secara visual;
- tidak ada tulisan maupun spasi khusus `Aktivitas Bi'ah QURBATA` di zona bawah;
- zona bawah hanya Tanggal–Nilai–TTD plus footer/identitas minimal bila diperlukan;
- ruang TTD berada di atas label;
- panel integrasi tetap terbaca;
- KFGQPC Uthman Taha tertanam;
- jumlah PDF tepat sesuai register.

Kegagalan satu poin = **LAYOUT FAIL**.

## 12. Gate FINAL
**CURRICULUM PASS → DOMAIN PASS → PAGE REGISTER PASS → CONTENT FREEZE → GLYPH PASS → LAYOUT PASS → PDF PASS.**

## 13. Changelog
### v1.4 — 2026-09-17
- Mengunci koreksi layout agar tidak ada tulisan mepet/tidak proporsional.
- Menetapkan latihan contoh dan latihan membaca harus diperbesar; tidak boleh semakin kecil akibat pagination.
- Memperkuat Ha dua lubang sebagai **visual glyph gate**; Ha satu lubang dilarang.
- Menghapus heading dan seluruh spasi khusus `Aktivitas Bi'ah QURBATA` dari bagian bawah.
- Menetapkan bagian bawah cukup `Tanggal – Nilai – TTD`.
- Mengalihkan ruang hasil penghapusan zona Bi'ah bawah ke area latihan Tartil.
- Menetapkan urutan prioritas ruang yang melindungi latihan Tartil dari auto-shrink.

### v1.3 — 2026-09-17
- Repetisi pedagogis Bi'ah/Akhlak 1–3 pertemuan.
- Teks Arab panel dipasangkan dengan arti Indonesia.
- Ha tunggal dua lubang dan glyph pass.
- Tanggal–Nilai–TTD satu baseline; ruang tulis di atas label.

### v1.2 dan sebelumnya
- Riwayat aturan sebelumnya tetap tersimpan sebagai dokumen governance/obsolete.

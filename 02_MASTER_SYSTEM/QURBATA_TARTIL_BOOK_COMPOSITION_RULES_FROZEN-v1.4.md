# QURBATA TARTIL — ATURAN PENYUSUNAN BUKU

Status: **FROZEN v1.4.2**
Effective: 2026-09-17
Authority: **BOOK COMPOSITION MASTER**
Scope: penyusunan isi, tipografi latihan, glyph Arab, dan prinsip layout seluruh Buku QURBATA Tartil

> Seluruh generator, layout, PDF, dan audit visual setelah keputusan ini WAJIB mengikuti v1.4.2. PDF footer versi sebelumnya berstatus AUDIT/OBSOLETE sampai diregenerasi.

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

## 8. FOOTER RESMI QURBATA JILID 1 — FROZEN v1.4.2
Referensi visual yang disetujui pengguna pada 17 September 2026 adalah authority visual footer.

### 8.1 Satu baris tunggal — tidak boleh pecah
Footer WAJIB berupa **SATU ROW horizontal** dan satu baseline visual. Tidak boleh ada komponen footer turun ke baris kedua.

Urutan kiri → kanan:
**badge ID halaman | Tanggal | Nilai | TTD | QR | brand RIQA OS**.

### 8.2 Geometri wajib
- Footer memakai satu container grid/flex khusus, bukan memanfaatkan footer lama yang terpisah-pisah.
- Tinggi efektif footer maksimum sekitar 18 mm pada A5.
- Badge ID kompak.
- Tanggal: field sedang.
- Nilai: field paling sempit.
- TTD: field administrasi paling lebar.
- QR: satu kolom tetap dengan quiet zone putih.
- Brand: satu kolom tetap di kanan QR.
- Semua kolom align-center secara vertikal.
- Tidak boleh memakai `position:absolute` untuk QR, motto, badge, atau metadata footer.
- Tidak boleh ada transform/negative margin yang menyebabkan tumpang tindih.

### 8.3 Field administrasi
- Label `Tanggal:`, `Nilai:`, `TTD:` berada tepat di atas kotak masing-masing, masih di dalam kolom footer yang sama.
- Kotak outline tipis biru/teal, sudut membulat ringan, latar putih.
- Ruang tulis berada di dalam kotak.
- TTD harus cukup luas untuk tanda tangan pena.
- Field tidak boleh menyentuh QR.

### 8.4 QR dan brand
- QR hitam-putih, ukuran konsisten, quiet zone putih bersih minimal sekitar 1 mm di setiap sisi.
- QR tidak boleh memiliki teks yang menempel/bertumpuk di bawahnya selain bila berada dalam kolom brand terpisah.
- Di kanan QR terdapat brand tersusun vertikal: motto Arab `تَعَلَّمْ – اِعْمَلْ – عَلِّمْ`, arti `Belajar, Mengamalkan, Mengajarkan`, lalu `RIQA OS`.
- Motto tidak boleh muncul di kiri bawah atau pada baris lain.
- Brand tidak boleh berada di bawah QR.

### 8.5 Metadata teknis DILARANG di halaman cetak
String seperti `AUDIT`, nama file page register, path repository, debug text, source marker, atau metadata build **tidak boleh dicetak di halaman buku**. Metadata tersebut hanya boleh ada pada log/build artifact metadata.

### 8.6 Larangan eksplisit
- Dilarang kotak biru/mint kosong di atas footer.
- Dilarang footer dua/lebih baris.
- Dilarang QR berada di tengah halaman sendiri.
- Dilarang ID halaman terpisah jauh dari row footer.
- Dilarang motto Arab jatuh ke kiri bawah.
- Dilarang metadata audit melintas di samping QR.
- Dilarang QR/brand/field saling overlap.

## 9. Implementasi generator
Generator harus menormalisasi DOM footer menjadi satu komponen resmi, bukan hanya menambal CSS class lama. Bila struktur HTML lama memisahkan `.study-fields`, QR, ID, motto, atau audit metadata, pipeline wajib memindahkan/menyusun ulang elemen tersebut ke satu `.qurbata-footer-v142` sebelum render.

## 10. Visual gate v1.4.2
LAYOUT PASS hanya jika:
- satu pertemuan/satu halaman dan 8×3 utuh;
- latihan Tartil besar/lapang;
- Ha detached dua lubang;
- tidak ada zona Aktivitas Bi'ah bawah;
- footer benar-benar satu row: ID + Tanggal + Nilai + TTD + QR + brand;
- QR scan-safe dan tidak overlap;
- motto hanya di kanan QR;
- tidak ada metadata audit/path di halaman;
- panel integrasi terbaca;
- KFGQPC Uthman Taha tertanam;
- jumlah halaman sesuai register.

Satu kegagalan = **LAYOUT FAIL**.

## 11. Gate FINAL
**CURRICULUM PASS → DOMAIN PASS → PAGE REGISTER PASS → CONTENT FREEZE → GLYPH PASS → LAYOUT PASS → PDF PASS.**

## 12. Changelog
### v1.4.2 — 2026-09-17
- Mengunci footer sebagai satu row tunggal.
- Mewajibkan normalisasi DOM footer, bukan CSS patch saja.
- Menghapus seluruh metadata audit/path dari halaman cetak.
- Mengunci QR dan brand dalam kolom terpisah di kanan.
- Melarang motto jatuh ke baris kedua/kiri bawah.
- Menetapkan referensi visual pengguna sebagai authority layout footer.

### v1.4.1 — 2026-09-17
- Menetapkan urutan ID → Tanggal → Nilai → TTD → QR → brand.
- Menghapus kotak aktivitas kosong dan menetapkan quiet zone QR.

### v1.4 — 2026-09-17
- Memperbesar latihan Tartil dan menghapus zona Aktivitas Bi'ah bawah.
- Memperkuat Ha dua lubang sebagai visual glyph gate.

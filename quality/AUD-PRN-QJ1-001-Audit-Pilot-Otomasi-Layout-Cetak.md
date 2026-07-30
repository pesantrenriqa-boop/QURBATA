# AUD-PRN-QJ1-001 — Audit Otomasi Layout Cetak Jilid 1

**Audit-ID:** AUD-PRN-QJ1-001  
**Status:** BUILD A5 POTRET 42 HALAMAN LULUS TEKNIS — FINAL PRINT APPROVAL OPEN
**Tanggal:** 28 Juli 2026  
**Objek:** `production/print/generate_qurbata_pdf.py`  
**Edisi:** Buku peserta  
**Sumber:** QJ1-P001–QJ1-P040 pada cabang `feature/qj1-master-structure`  
**Keputusan:** PR #2 tetap Draft

## 1. Cakupan

Generator dijalankan terhadap seluruh 40 sumber nyata Jilid 1. Keluaran merupakan PDF peserta **A5 potret** dengan bleed 3 mm, safe area 7 mm pada halaman pelajaran, font **Amiri Quran 1.003** tertanam, cover contoh, halaman identitas, crop marks, metadata Draft, dan pemisahan konten guru–peserta.

## 2. Hasil Build

| Pemeriksaan | Hasil |
|---|---|
| sumber ditemukan | 40/40 |
| halaman PDF | 42 total: cover + identitas + 40 halaman sumber |
| halaman latihan/evaluasi | 36 halaman × 24 butir |
| halaman khusus | P018, P028, P036, P038 |
| tata latihan | 3 kolom × 8 baris |
| urutan halaman | P001–P040 lengkap |
| urutan tangga | kanan atas menuju kiri, lalu turun |
| urutan token Arab | token pertama sumber selalu paling kanan |
| ukuran MediaBox | A5 potret 148 × 210 mm + bleed 3 mm |
| crop marks | hadir pada 42/42 |
| font Arab | Amiri Quran 1.003; SHA-256 tercatat; lisensi OFL disimpan |
| ukuran font Arab | 16 pt baseline A5 potret; wajib proof keterbacaan fisik |
| marker konten guru | tidak ditemukan pada PDF peserta |
| clipping/overlap/kotak hitam | tidak ditemukan pada render 42 halaman |
| render sampel rinci | cover, identitas, P001, dan P018 diperiksa pada resolusi asli |
| status khusus | placeholder Draft; materi belum disahkan tidak dicetak |
| rekam pembelajaran | nomor halaman, tanggal, nilai, lulus/ulang, dan paraf/TTD guru tersedia |
| panel integrasi | Bahasa Arab dan Tahfidz/Murojaah tersedia tanpa menerbitkan materi yang belum disahkan |

## 3. Koreksi Teknis

1. Generator pertama hanya menerima halaman dengan tepat 24 butir.
2. Generator diperluas untuk empat halaman khusus tanpa memaksakan grid latihan.
3. Urutan kotak dikoreksi agar Tangga 1 dimulai dari kanan atas.
4. Mesin bidi sempat membalik rangkaian huruf terpisah.
5. Render diubah menjadi per-token: token pertama sumber ditempatkan paling kanan secara deterministik.
6. PDF dibangkitkan ulang, dirender 40 halaman, dan diperiksa ulang.
7. Profil diubah menjadi A5 potret; grid diubah menjadi 3 × 8.
8. Cover contoh, identitas peserta, panel integrasi, dan rekam guru ditambahkan.
9. PDF 42 halaman dibangkitkan dan dirender ulang; preflight dan pemeriksaan visual sampel lulus.

## 4. Kontrol Halaman Khusus

P018, P028, P036, dan P038 tidak memperoleh materi peserta buatan. Selama keputusan kurikulum belum sah, halaman hanya menampilkan:

- identitas halaman;
- label `HALAMAN KHUSUS`;
- keterangan bahwa materi peserta menunggu keputusan dan pengesahan;
- status Draft dari sumber;
- nasihat akhlak bila tersedia.

## 5. Preflight Otomatis

Build gagal apabila:

- halaman biasa tidak memiliki tepat 24 butir;
- halaman tanpa latihan bukan salah satu dari empat halaman khusus;
- kode/judul tidak ditemukan;
- butir tidak memuat karakter Arab;
- jumlah halaman PDF berbeda dari jumlah sumber;
- MediaBox tidak sesuai;
- marker guru ditemukan dalam PDF peserta.

## 6. Batas Kelulusan

Kelulusan teknis ini membuktikan pipeline dapat menghasilkan PDF peserta lengkap dan konsisten. Kelulusan ini belum mencakup:

1. validasi akademik, Arab/Qira’at, asesmen, dan safeguarding;
2. keputusan materi P018, P028, P036, dan P038;
3. verifikasi ahli atas `ءُ` pada P033;
4. konfirmasi final ukuran font melalui proof fisik;
5. finalisasi desain cover, halaman legal, daftar isi, punggung, dan edisi guru;
6. profil CMYK/mesin cetak, jenis kertas, binding, serta finishing;
7. proof print fisik dan Evidence-ID editorial/render;
8. otorisasi Document Controller.

## 7. Keputusan Audit

- Build sumber nyata P001–P040: **LULUS TEKNIS**.
- Pemeriksaan render A5 potret 42 halaman: **LULUS INTERNAL PROTOTIPE**.
- Pemisahan naskah guru dari PDF peserta: **LULUS STRUKTURAL**.
- Persetujuan siap cetak final: **OPEN**.
- GATE-RND-QJ1: **OPEN — BUILD LULUS, PROOF/APPROVAL BELUM ADA**.
- PR #2: **tetap Draft**.

PDF saat ini adalah **contoh layout A5 potret**, bukan produk final terotorisasi. Finishing desain ditahan atas arahan Pemilik Akademik agar progres kembali berfokus pada isi dan gate keilmuan.

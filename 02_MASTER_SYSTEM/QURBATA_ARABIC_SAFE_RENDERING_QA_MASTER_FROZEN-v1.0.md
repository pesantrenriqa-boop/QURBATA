# QURBATA — Arabic Safe Rendering & Quality Gate

**Kode:** QRT-ARB-RENDER-QA-v1.0  
**Status:** FROZEN — disetujui pengguna, 8 Oktober 2026  
**Cakupan:** Seluruh produksi buku Bahasa Arab QURBATA Jilid 1–8 (P001–P320).  
**Rujukan:** `02_MASTER_SYSTEM/QURBATA_BAHASA_ARAB_BOOK_LAYOUT_MASTER_FROZEN-v1.0.md` dan `curriculum/QURBATA-BAHASA-ARAB-J1-J8-320-SLOT-MATERI-REGISTER-v0.1.md`.

## 1. Aturan pokok yang tidak boleh dilanggar

1. **AI generatif gambar tidak boleh menggambar/menuliskan teks Arab final**, termasuk judul, instruksi, dialog, harakat, soal, latihan menebali, atau ayat. AI hanya untuk ilustrasi tanpa tulisan; komposisi final dilakukan oleh mesin layout.
2. **Satu sumber teks Arab tervalidasi per Page-ID**. Semua kemunculan (judul, dialog, latihan, pengulangan, lembar menebali) mengambil string sumber yang sama. Jangan mengetik ulang secara manual atau meminta AI menebak harakat.
3. Font Arab wajib **KFGQPC Uthman Taha** resmi yang sudah diverifikasi penggunaannya. Render dengan mesin shaping Arab (HarfBuzz/Chromium), arah **RTL**, dan pemeriksaan ligatur serta posisi harakat. Jangan mengganti font diam-diam.
4. Kutipan ayat Al-Qur'an harus mengikuti rasm Utsmani terverifikasi dan diberi surah/ayat. Ungkapan kelas tetap ejaan Arab yang tepat dengan font Utsmani; tidak diklaim sebagai ayat.
5. Logo wajib aset QURBATA asli; jangan buat ulang logo dengan AI. QR RIQA OS harus mengarah ke URL yang diketahui, dapat dipindai, dan tidak diklaim sebagai latihan Pxxx khusus jika belum diverifikasi.
6. Layout B5, palet, margin, hierarki dan materi mengikuti dua master yang dirujuk; status FROZEN master lama tidak berubah.

## 2. Alur produksi deterministik

1. Ambil teks sesuai **Page-ID** dari register resmi, lalu verifikasi teks/harakat secara editorial.
2. Simpan satu sumber Unicode kanonis per ungkapan; rekam versi dan hash. Pisahkan materi baru, murojaah, dan kalimat pendukung.
3. Jalankan pemeriksaan Unicode (normalisasi, karakter yang dilarang, pengulangan tanda diakritik tak sah), tanda baca, ejaan, dan RTL. **Pemeriksaan otomatis tidak menggantikan validasi bahasa Arab**.
4. Render semua teks Arab melalui HTML/CSS `direction:rtl`, `unicode-bidi:isolate`, `lang=ar`, font KFGQPC Uthman Taha, Chromium/HarfBuzz. Gunakan engine yang sama untuk latihan menebali, dengan warna abu-abu muda/outline yang berasal dari teks identik.
5. Gabungkan dengan ilustrasi bebas teks dan logo asli dalam layout B5, lalu ekspor PDF dan/atau PNG dari renderer yang sama.
6. Uji kesamaan sumber dengan teks yang diekstrak dari PDF. **Jika ekstraksi tidak identik**, hentikan rilis dan diagnosis (misalnya urutan glyph/ToUnicode) — jangan otomatis mengklaim teks salah atau benar hanya dari ekstraksi.
7. Periksa secara visual posisi harakat, arah baca, sambungan huruf, keterbacaan latihan, tidak ada teks terpotong atau halaman meluber, serta kesesuaian QR.
8. Minta pemeriksaan ahli bahasa Arab dan penanggung jawab QURBATA. Hanya hasil yang lolos semua gate dapat menjadi APPROVED/FROZEN.

## 3. Quality gates

| Gate | Pemeriksaan | Gagal berarti |
|---|---|---|
| SOURCE | Page-ID, teks, status dan hash sumber | BLOCKED-SOURCE |
| UNICODE | huruf, harakat, pengulangan tanda, urutan kode | BLOCKED-TEXT |
| TYPOGRAPHY | font terpakai, shaping, RTL, posisi harakat | BLOCKED-FONT |
| CONSISTENCY | semua salinan teks identik sumber | BLOCKED-CONSISTENCY |
| OUTPUT | satu halaman B5, tidak meluber, ekstraksi dibandingkan | BLOCKED-OUTPUT |
| VISUAL | audit ahli bentuk huruf dan harakat | REVIEW-REQUIRED |
| CONTENT | pedagogi, sumber ayat, ketepatan bahasa | REVIEW-REQUIRED |
| BRAND/QR | logo asli dan QR terbaca, URL tepat | BLOCKED-ASSET |

## 4. Kebijakan rilis dan perubahan

- Hasil awal selalu **DRAF**. Bukti uji render P001/P002 sebelumnya adalah prototipe, bukan bukti bahwa semua gate sudah lulus.
- **Tidak ada jaminan otomatis 100%** hanya karena memakai font yang benar; validasi visual dan ahli wajib.
- Mesin tidak boleh memodifikasi register materi yang sudah FROZEN untuk menyesuaikan hasil gambar. Perbaiki renderer atau ajukan revisi sumber melalui proses terpisah.
- Perubahan aturan setelah v1.0 harus melalui dokumen versi baru dengan changelog dan persetujuan; jangan mengedit master FROZEN diam-diam.

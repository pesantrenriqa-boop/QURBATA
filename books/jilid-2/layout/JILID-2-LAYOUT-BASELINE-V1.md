# QURBATA Jilid 2 — Layout Baseline V1

**Status:** ACTIVE — PRODUCTION BASELINE  
**Sumber visual:** Jilid 1 `V22_FROZEN`, tervalidasi sampai kandidat V25  
**Ruang lingkup:** Jilid 2 P001–P040  
**Prinsip:** wariskan mesin visual yang berhasil; jangan menyalin struktur pedagogis Jilid 1.

## 1. Kontrak Visual yang Diwariskan

Jilid 2 wajib memakai baseline visual Jilid 1 yang telah stabil:

- format halaman A5;
- header QURBATA/JILID sejajar dengan judul materi;
- area baca memakai grid geometris tetap, RTL, dan alignment optik berbasis ink bounds;
- `CANVAS_INK_BOUNDS_COLLISION_SAFE_V2` sebagai model alignment;
- validasi collision sesudah scaling (`POST_SCALE_INK_BOUNDS`);
- ukuran huruf latihan baseline 36 pt dan fokus baseline 44 pt, kecuali gate Jilid 2 membuktikan unit sambung memerlukan profil khusus;
- koreksi mikro posisi dhammah/kasrah diwariskan;
- bentuk display ha tunggal mengikuti kebijakan dua-mata yang telah disahkan pada Jilid 1, tanpa mengubah data canonical;
- footer bawah memuat keterangan Kompetensi, Hafalan Al-Qur'an, Bahasa Arab, dan NIDOM secara terbaca;
- footer tidak boleh mepet garis bawah;
- nomor/garis/debug label tidak masuk artefak cetak;
- `LAYOUT_OVERFLOW=0` wajib sebelum kandidat PDF dinyatakan PASS.

## 2. Bagian yang Dibekukan

Hal berikut tidak boleh dirombak hanya karena berpindah ke Jilid 2:

1. proporsi umum header–materi–footer;
2. filosofi grid lurus kanan/kiri;
3. optical alignment berbasis canvas ink bounds;
4. collision-safe fitting;
5. prinsip jarak antarkotak dan keterbacaan harakat;
6. tipografi dan hierarki footer;
7. mekanisme gate overflow.

Perubahan hanya boleh berupa **profil unit Jilid 2** untuk mengakomodasi bentuk sambung 3/4 huruf, bukan redesign halaman.

## 3. Adaptasi Pedagogis Jilid 2

Layout tidak boleh memaksa Jilid 2 kembali ke pola isi Jilid 1. Master Jilid 2 menetapkan:

- P001–P020: 24 tangga × 3 huruf;
- P021–P040: 8 tangga × 3 huruf + 16 tangga × 4 huruf;
- fokus utama bentuk sambung; bentuk terpisah hanya remedial;
- P001–P020: keluarga bentuk dan pemutus sambungan;
- P021–P024: tiga tanwin;
- P025–P040: kontras pendek–panjang dan tiga mad asli;
- tidak ada regresi ke tangga dua huruf;
- komponen Tahfidz, Bahasa Arab, akhlak/NIDOM, evaluasi, dan remedial terintegrasi, tidak mengambil halaman baca.

## 4. Aturan Review

Review Jilid 2 harus bekerja pada **unit kompetensi aktif**, bukan menyalin blok/kotak lama. Materi baru tetap dominan pada halaman akuisisi, sedangkan review mengambil unit yang telah dipelajari menurut progression dan kebijakan N+1/N+2/N+4/N+8 yang berlaku pada master.

## 5. Gate Sebelum Renderer Jilid 2

Sebelum layout produksi dibuat, dataset harus membuktikan:

- tepat 40 halaman;
- P001–P020 seluruhnya memakai unit 3 huruf sesuai master;
- P021–P040 memiliki 8 unit 3 huruf dan 16 unit 4 huruf per halaman;
- tidak ada tangga 2 huruf;
- keluarga bentuk/pemutus mengikuti urutan master;
- tanwin hanya masuk P021–P024;
- mad mengikuti urutan alif → ya → waw pada P025–P040;
- materi khusus footer tidak mengurangi jumlah latihan baca;
- data peserta terpisah dari naskah guru/audit/blocker.

## 6. Status Sumber Saat Baseline Ini Dibuat

Mengikuti register recovery dan master aktif:

- P001–P020: `COMPLETE-DRAFT`, perlu review ahli;
- P021–P024: `STAGED-BLOCKED`, belum boleh diotorisasi cetak;
- P025–P040 versi lama: `SUPERSEDED`;
- P025–P040 versi baru: `PENDING-REGENERATION` berdasarkan master 0.25.0-id.

Karena itu, penerapan layout Jilid 1 pada Jilid 2 dimulai sebagai **production architecture**, bukan klaim bahwa 40 halaman Jilid 2 sudah siap cetak.

## 7. Freeze Rule

`JILID-2-LAYOUT-BASELINE-V1` menjadi titik awal resmi. Jika unit sambung 4 huruf memerlukan penyesuaian, perubahan dibuat sebagai profil/variant Jilid 2 yang terukur dan diuji, sementara mesin visual Jilid 1 tetap menjadi induk. Dilarang memulai eksperimen layout dari nol.

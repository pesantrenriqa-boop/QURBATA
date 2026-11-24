# QURBATA Jilid 1 — P023 Dhammah 1 (DRAF REKONSILIASI)

Status: DRAF, bukan FROZEN. 24 November 2026.

## Tartil — الضَّمَّةُ ١

Kompetensi baru: بُ تُ ثُ. Penanaman dua baris: بِ → بُ, تِ → تُ; ثِ → ثُ. Jim Dhammah جُ ditunda ke P024 bersama حُ خُ; ذُ dari blok resmi Dhammah 2 tetap perlu pemetaan berikutnya, tidak dihapus.

| Baris | Kolom 1 | Kolom 2 | Kolom 3 |
|---|---|---|---|
| 1 | بُ تُ كِ | ثُ بُ لِ | تُ ثُ مِ |
| 2 | بُ تُ نِ | ثُ بُ هِ | تُ ثُ وِ |
| 3 | بُ تُ يِ | ثُ بُ بَ | تُ ثُ تَ |
| 4 | بُ تُ ثَ | ثُ بُ ءَ | تُ ثُ أَ |
| 5 | بُ جَ حَ | تُ خَ دَ | ثُ ذَ رَ |
| 6 | بُ زَ سَ | بُ تُ | ثُ عِ |
| 7 | تُ عِ | ثُ غِ | بُ غِ |
| 8 | ثُ فِ | تُ ثُ | ثُ قِ |

Sumber algoritme: production/vivliostyle/scripts/build-p021-p030-from-frozen.mjs blob cdcbdf5f0e126baca0e89ca2747ba4874af9252e, rowsFor(spec n=21), seed a=63, r=105, pola AA/AR dan AAR/ARR. Adaptasi deterministik active pool menjadi بُ تُ ثُ. Urutan 16 triples lalu 8 pairs. Duplikasi akibat pool tiga huruf diperbaiki menggunakan pasangan legal yang sudah ada pada draf sebelumnya (blob d1b9db635b6d7d70110ef979a9a05b8f37494aa4): S19: بُ تُ → تُ عِ; S21: بُ تُ → بُ غِ; S23: بُ تُ → تُ ثُ. Bukan salinan literal seluruh keluaran FROZEN, bukan contoh karangan manual. Audit: 24/24 unik, 64 token, 38 Dhammah aktif, 26 review, 0 token ilegal, 0 جُ. Cakupan review per halaman bukan seluruh 29 huruf.

## Bahasa Arab

مَرَّةً أُخْرَى — Sekali lagi. INTRODUCE usulan dari overlay integrasi FROZEN v1.3 P024–P026 setelah blok penutupan buku pada draf P019–P021. Bukan perubahan overlay. Register Tartil lama P021 memuat صَحِيحٌ; konflik domain perlu rekonsiliasi.

## Akhlak

وَلَا تُسْرِفُوا — Janganlah berlebih-lebihan. INTRODUCE usulan dari overlay integrasi FROZEN v1.3 P024–P026 setelah blok amanah draf P019–P021. Bukan perubahan overlay.

## Tahfidz

An-Nasr ayat 1 — إِذَا جَاءَ نَصْرُ اللَّهِ وَالْفَتْحُ — Apabila telah datang pertolongan Allah dan kemenangan. Sumber generator n=21 dan register FROZEN P021. Penempatan P023 bersyarat: Al-Lahab ayat 5 harus dikembalikan pada draf P022 sesuai kesinambungan yang dibahas pengguna; perubahan P022 belum dilakukan dalam commit ini.

## Gate

FROZEN P023 tetap Dhammah 3, Tahfidz An-Nasr 3, overlay BA/Akhlak blok penutupan buku/amanah. Usulan P023 Dhammah 1 mengikuti pergeseran +2 setelah checkpoint. Rekonsiliasi seluruh P020–P040, audit master Tahfidz dan font Utsmani, render A5 masih terbuka. Tidak mengubah FROZEN maupun generator.

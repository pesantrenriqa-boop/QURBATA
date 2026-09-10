# Buku Tangga Kompetensi Bahasa Arab Qurani QURBATA

Proyek ini adalah buku induk yang memaparkan 65 kompetensi inti Bahasa Arab Qurani berdasarkan operasi pembelajar dan bukti korpus Al-Qur'an.

## Identitas

- Judul: Tangga Kompetensi Bahasa Arab Qurani QURBATA
- Subjudul: Panduan Bertahap Memahami Struktur dan Makna Al-Qur'an Berdasarkan Analisis Korpus
- Kode buku: `BAQ-QURBATA-INDUK`
- Arsitektur: K01-K65 canonical
- Status: draf produksi berbasis bukti
- Mesin tata letak: Vivliostyle

## Batas produk

Buku ini berbeda dari Bahasa Arab pendamping Tartil. Buku ini membahas kompetensi Bahasa Arab Qurani yang tersusun dari pengenalan kata, hubungan frasa, struktur kalimat, ketergantungan antarklausa, hingga hubungan makna wacana Al-Qur'an.

## Sumber kebenaran

1. `data/competencies.json` pada proyek produksi adalah registry buku.
2. `research/arabic-competency-ladder/LADDER-ARCHITECTURE-v1.0.md` pada cabang riset menjadi sumber arsitektur canonical.
3. Bukti ayat harus memiliki surah, ayat, target span, alasan fungsi, dan status validasi sebelum berstatus siap terbit.
4. Seluruh ID mengikuti resolusi canonical K01-K65. Legacy K60/K61 tetap disimpan sebagai catatan transfer, bukan kompetensi inti baru.

## Status isi

- Registry K01-K65: tersedia.
- Desain halaman buku: tersedia.
- Bab landasan: tersedia dalam prototipe.
- Paparan contoh K01-K10: tersedia sebagai gelombang pertama.
- Bukti K11-K65: ditampilkan sebagai kandidat sampai evidence bank korpus ditanam dan divalidasi.

## Produksi

Produk Vivliostyle berada di `production/vivliostyle-arabic-competency`.

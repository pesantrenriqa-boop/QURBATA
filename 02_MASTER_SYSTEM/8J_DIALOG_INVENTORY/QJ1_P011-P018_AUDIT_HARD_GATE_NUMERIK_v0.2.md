# QURBATA J1 — Audit Numerik Hard Gate P011–P018 v0.2

Status: QA BLOCKED, berdasarkan pembacaan langsung file kandidat `QJ1_P011-P018_GRID_PATCH_APPLIED_v0.2.md` dan aturan register Tartil FROZEN v1.1.

| Halaman | Kelompok identik tambahan | Sel penanaman salah panjang/target | Sel latihan salah panjang/tanpa target |
|---|---:|---:|---:|
| P011 | 6 | 0 | 10 |
| P012 | 6 | 0 | 10 |
| P013 | 2 | 0 | 10 |
| P014 | 6 | 0 | 6 |
| P015 | 6 | 0 | 6 |
| P016 | 6 | 0 | 6 |
| P017 | 6 | 0 | 6 |
| P018 | 6 | 0 | 6 |

Metode: untuk tiap halaman baca 8 baris × 3 sel; hitung duplikasi string sel (jumlah total dikurangi jumlah unik); sel 1–6 harus dua token TARGET-only; sel 7–24 harus tiga token dan memuat setidaknya satu TARGET. Satu sel dapat gagal lebih dari satu kriteria, sehingga angka tidak boleh dijumlahkan sebagai jumlah sel unik bermasalah.

**Konflik desain:** P011 dan P012 masing-masing hanya dua TARGET. Enam pasangan dua huruf TARGET-only unik mustahil karena hanya ada empat pasangan berurutan dengan pengulangan diizinkan. P013 tiga TARGET memiliki sembilan kemungkinan pasangan, sehingga dapat diperbaiki tanpa mengubah register. P014–P018 empat TARGET juga dapat diperbaiki.

**Tindak lanjut:** jangan ubah register FROZEN otomatis. Siapkan grid kandidat baru P013–P018 dengan hard gates terpenuhi; P011–P012 perlu keputusan pengecualian yang eksplisit atas syarat enam pasangan unik atau revisi kebijakan yang berwenang. Jangan nyatakan PASS hanya berdasarkan rasio 60/40.

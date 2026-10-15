# Verifikasi ulang grid J1 P011–P018

Status: PASS TERBATAS (struktur grid, rasio token, whitelist). Bukan persetujuan cetak. Sumber yang diperiksa: `QJ1_P011-P018_GRID_PATCH_APPLIED_v0.2.md` pada branch `renderer/pagedjs-p001-prototype`.

Metode: membaca setiap baris tabel grid 8×3, memecah token berdasarkan spasi, menghitung bentuk baru yang diperkenalkan pada halaman bersangkutan dan review dari kompetensi kumulatif. Penanaman dan panel tidak termasuk hitungan.

| Halaman | Baris | Kelompok | Total | Baru | Review | % baru | Token prematur |
|---|---:|---:|---:|---:|---:|---:|---|
| P011 | 8 | 24 | 64 | 38 | 26 | 59,38% | 0 |
| P012 | 8 | 24 | 64 | 38 | 26 | 59,38% | 0 |
| P013 | 8 | 24 | 64 | 38 | 26 | 59,38% | 0 |
| P014 | 8 | 24 | 66 | 40 | 26 | 60,61% | 0 |
| P015 | 8 | 24 | 66 | 40 | 26 | 60,61% | 0 |
| P016 | 8 | 24 | 66 | 40 | 26 | 60,61% | 0 |
| P017 | 8 | 24 | 66 | 40 | 26 | 60,61% | 0 |
| P018 | 8 | 24 | 66 | 40 | 26 | 60,61% | 0 |

Semua delapan halaman lulus pemeriksaan angka 60:40 dengan toleransi pembulatan yang wajar; P011–P013 59,375%, P014–P018 60,606%. Token di luar whitelist kumulatif: tidak ada.

## Gate yang belum selesai
- Audit sebaran setiap grafem dan variasi fonetik.
- Review pedagogis penanaman dua baris dan latihan, termasuk kelayakan untuk pemula.
- Validasi teks dan arti Tahfidz serta sumber Akhlak.
- Rendering KFGQPC Uthman Taha, ha dua lubang, RTL, A5, QR dan ruang nilai/tanggal/paraf.

Keputusan: gunakan grid v0.2 sebagai kandidat QA, jangan nyatakan FROZEN/print-ready sebelum seluruh gate selesai.

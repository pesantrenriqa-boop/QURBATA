# QURBATA J1 P011–P020 — Audit Terpadu Kandidat v0.1

Status: QA PARSIAL; **bukan izin cetak**. Audit membedakan sumber kandidat P011–P012 v0.1, P013–P018 v0.3, P019 v0.2, dan P020 pilot bagian C.

| Halaman | Sumber | Kelompok | Kelompok unik | Catatan |
|---|---|---:|---:|---|
| P011 | kandidat exception pending | 24 | 22 | Dua duplikasi penanaman; exception belum disahkan |
| P012 | kandidat exception pending | 24 | 20 | Empat duplikasi, melebihi dua duplikasi penanaman yang diusulkan |
| P013–P018 | kandidat curated v0.3 | 24 per halaman | 24 per halaman | Struktur dasar dan whitelist sudah lolos audit kandidat sebelumnya |
| P019 | kandidat Kasrah v0.2 | 24 | 24 | Struktur dasar dan whitelist sudah lolos audit kandidat sebelumnya |
| P020 | pilot bagian C (checkpoint) | 24 | 24 | 72 token, 58 bentuk token berbeda, tanpa Dhammah; gunakan hanya bagian C untuk grid |

**Koreksi penting:** P020 memiliki tabel identitas huruf di bagian A dan tabel latihan di bagian C. Parser yang menggabungkan semua tabel akan menghasilkan hitungan palsu. Audit P020 harus dibatasi ke bagian C.

**Keputusan:** P012 harus direvisi lagi; P011 dan P012 tetap memerlukan keputusan berwenang terkait pengecualian enam pasangan TARGET-only unik untuk dua TARGET. Jangan mengubah register FROZEN secara diam-diam. P013–P020 belum lulus tashih teks, urutan pedagogis manusia, dan proof visual A5/KFGQPC/RTL.

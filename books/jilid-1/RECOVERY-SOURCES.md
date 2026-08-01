# QJ1 — Register Sumber Recovery

**Status:** ACTIVE  
**Induk:** `books/RECOVERY-CONSOLIDATION-INDEX-JILID-1-3.md`

## Sumber Utama

- Master struktur dan isi sampai P040: commit `c820ca4c0504185bf5e63d7765089fbd7c4b4e2b`.
- Kontrol freeze: `books/jilid-1/QJ1-FREEZE.md`.
- Halaman kanonik: `books/jilid-1/pages/QJ1-P001.md` sampai `QJ1-P040.md`.
- Sumber pembanding recovery P001: `03_BOOKS/JILID-1/PAGE-001.md`.

## Status

| Rentang | Status | Tindakan |
|---|---|---|
| P001 | SOURCE-VERIFIED | Urutan 64 token cocok dengan sumber recovery dan telah dibentuk menjadi 24 tangga. Bersihkan rujukan aturan 60:40 yang sudah tidak berlaku. |
| P002 | SOURCE-VERIFIED-WITH-GATE | Versi 0.4.0-id pada commit `b43a8b2d1fc67f893bad2e7bd987850d70eaf514` memiliki 24 tangga, 64 token, whitelist ءَ أَ بَ تَ ثَ, dan pemerataan 12–13 token per identitas. Terminologi serta penyajian ءَ/أَ tetap menunggu verifikasi ahli. |
| P003 | SOURCE-CONFLICT | Ada sedikitnya dua kandidat sah: versi pemerataan mutlak 0.4.0-id pada commit `91ad43999a26f594c1134271c02b827e93c8cc8c`, lalu versi lebih baru 0.5.0-id dengan distribusi 60:40 pada commit `50929c460774677b5e9170f143ce0ce7b41b2771`. Jangan freeze sebelum keputusan kebijakan distribusi final diterapkan secara konsisten. |
| P004–P040 | FOUND-UNASSESSED | Verifikasi isi contoh satu per satu terhadap master, whitelist, progression, dan versi terakhir yang tidak superseded/invalid. |

## Catatan Audit P002

- Pola halaman: tangga 1–8 masing-masing dua huruf; tangga 9–24 masing-masing tiga huruf.
- Total: 64 token.
- Tidak ditemukan mad, tanwin, sukun, tasydid, bentuk sambung, atau rangkaian lebih dari tiga huruf dalam sumber latihan.
- Status `SOURCE-VERIFIED-WITH-GATE` bukan berarti siap cetak; render, makhraj, metadata ahli, dan safeguarding masih terbuka.

## Catatan Konflik P003

Versi 0.4.0-id dan 0.5.0-id sama-sama memuat 24 latihan dan 64 token, tetapi memakai kebijakan distribusi berbeda:

1. `91ad439...`: seluruh delapan identitas sampai P003 dibagi sama rata, masing-masing 8 token.
2. `50929c4...`: materi baru جَ حَ خَ sebanyak 39 token dan review sebanyak 25 token (sekitar 60:40).

Karena keputusan terbaru proyek mengarah pada 50:50 dan murojaah kumulatif, versi 0.5.0-id tidak boleh otomatis dianggap pemenang hanya karena tanggalnya lebih baru. Isi kedua versi dipertahankan sebagai kandidat sampai audit kebijakan lintas halaman selesai.

## Larangan

- Jangan membuat contoh baru untuk menggantikan isi recovery sebelum audit selesai.
- Jangan memakai file PDF/slide sebagai sumber mandiri.
- Jangan memilih versi hanya berdasarkan tanggal commit; status superseded, keputusan kurikulum, whitelist, dan konsistensi lintas halaman lebih tinggi prioritasnya.
- Jangan menyatakan Jilid 1 selesai recovery hanya berdasarkan keberadaan struktur 40 halaman.

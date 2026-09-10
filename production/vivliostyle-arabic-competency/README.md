# Produksi Vivliostyle Buku Bahasa Arab Qurani

Pipeline ini menghasilkan buku B5 dari registry K01-K65 dan data bukti korpus.

## Menjalankan

```bash
npm install
npm run build
```

Hasil:

- `dist/index.html`
- `dist/TANGGA-KOMPETENSI-BAHASA-ARAB-QURANI-QURBATA-v0.1.pdf`

## Aturan produksi

- Arab menggunakan KFGQPC Uthman Taha. Font lain hanya fallback pratinjau dan bukan keluaran produksi.
- Satu halaman kompetensi memperkenalkan satu operasi pembelajar.
- Contoh yang belum lolos pemeriksaan korpus diberi status `KANDIDAT`.
- Target span tidak boleh menuntut kompetensi di atas ceiling halaman.
- URL RIQA OS menggunakan kontrak `/kompetensi/baq/{K-ID}`.

## Font

Letakkan font berlisensi yang telah disahkan sebagai `fonts/KFGQPC-Uthman-Taha-Naskh.woff2` sebelum produksi final.


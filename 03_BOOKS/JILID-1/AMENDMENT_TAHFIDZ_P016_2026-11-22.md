# QURBATA Jilid 1 — Ketetapan Revisi Tahfidz P016 (22 November 2026)

**Status:** KEPUTUSAN PENGGUNA — ATURAN PRODUKSI TERBARU UNTUK P016; rekonsiliasi ke seluruh register FROZEN dan generator masih diperlukan.

## Ketetapan

- **Halaman:** P016, Jilid 1.
- **Target hafalan yang ditetapkan:** **QS. Al-Ikhlas ayat 3**.
- **Teks ayat:** **لَمْ يَلِدْ وَلَمْ يُولَدْ**.
- **Arti Indonesia:** **Dia tidak beranak dan tidak pula diperanakkan.**
- **Prioritas produksi:** Ketetapan ini harus digunakan dalam **draf produksi P016**; jangan kembali mengambil QS. Al-Masad:1 dari generator lama ketika menyiapkan halaman 16.

## Dasar dan riwayat perubahan

1. Pengguna menetapkan P014 telah selesai sebagai pengayaan Fathah, P015 Kasrah 1, dan P016 Kasrah 2 dalam alur draf rekonsiliasi.
2. Pada 22 November 2026, pengguna mengoreksi hafalan P016 secara eksplisit menjadi **Al-Ikhlas ayat 3**, serta memerintahkan pencatatan pada repo dan aturan resmi terbaru.
3. Generator terdahulu `production/vivliostyle/scripts/build-p011-p020-from-frozen.mjs` memuat P014 = Al-Ikhlas:3, P015 = Al-Ikhlas:4, P016 = Al-Masad:1. **Mapping lama tersebut tidak berlaku sebagai acuan draf P016 setelah keputusan ini**, tetapi sumber historisnya tidak dihapus.
4. Register integrasi `PAGE_REGISTER_P001-P040_INTEGRATION_FROZEN-v1.3.md` menyatakan Tahfidz tetap mengikuti baseline FROZEN; karena itu **amendemen ini belum otomatis mengesahkan revisi seluruh baseline**, yang harus direkonsiliasi terpisah.

## Kendali pelaksanaan

- Halaman P016 menampilkan ayat Arab dan arti Indonesia di panel Tahfidz.
- Tidak boleh mengklaim bahwa generator PDF, baseline FROZEN, atau seluruh halaman P014–P020 telah otomatis dimigrasikan.
- Sebelum cetak final: verifikasi tidak ada benturan dengan hafalan P015/P017, update generator dan master setelah keputusan rekonsiliasi, lalu audit render.

## Dokumen terkait

- `03_BOOKS/JILID-1/QJ1-P016_KASRAH2_REKONSILIASI_DRAFT.md`
- `03_BOOKS/JILID-1/PAGE_REGISTER_P001-P040_INTEGRATION_FROZEN-v1.3.md`
- `production/vivliostyle/scripts/build-p011-p020-from-frozen.mjs`

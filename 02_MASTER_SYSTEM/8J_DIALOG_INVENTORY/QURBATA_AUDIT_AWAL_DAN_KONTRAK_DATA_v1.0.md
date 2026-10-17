# Audit nyata dan rencana migrasi terstruktur QURBATA — 17 Oktober 2026

## Bukti inventaris berkas
- Direktori GitHub `02_MASTER_SYSTEM/8J_DIALOG_INVENTORY` pada branch `renderer/pagedjs-p001-prototype` diperiksa melalui listing API.
- **40/40 file** `QJ2_P001...P040_PAKET_KONTEN_TERPADU_SIAP_REVIEW_v1.0.md` ditemukan.
- `QURBATA_CONTENT_PIPELINE_v1.0.py` dan README ditemukan.
- **Belum menjalankan** script terhadap salinan lengkap repository. Listing file bukan pengganti audit isi.
- Pemeriksaan sampel file P028 dan P040 menunjukkan catatan G1–G5 belum PASS; pembaruan hadis batch pada kedua halaman ini belum terbukti tersimpan.

## Kontrak data per halaman (rencana untuk produksi batch)
```json
{
  "id":"QJ2-P001",
  "tartil":{"focus":"","cards":[],"exercises":[],"answer_key":[],"quran_tokens":[]},
  "dialog":{"turns":[],"review_status":"REVIEW"},
  "akhlaq":{"hadith_id":"","source_ref":"","matn":"","application":"","review_status":"REVIEW"},
  "tahfidz":{"frozen_ref":"","source_crosswalk":"","review_status":"REVIEW"},
  "gates":{"G1":"BLOCKED","G2":"BLOCKED","G3":"BLOCKED","G4":"BLOCKED","G5":"BLOCKED"},
  "content_final":false
}
```
**Jangan isi bidang kosong dengan tebakan.** Token mushaf wajib diverifikasi terhadap corpus primer yang disahkan. Hadis harus merujuk ke bank takhrij dan menjaga perbedaan matan/varian.

## Langkah operasional
1. Buat export terstruktur dari Markdown yang sudah ada; tandai data yang tidak dapat diekstrak, jangan menciptakan konten.
2. Jalankan script audit terhadap checkout repository lengkap untuk menghasilkan CSV/JSON.
3. Kelompokkan perbaikan per 10–20 halaman dengan SHA commit dan daftar pengecualian.
4. Validasi G1–G5 secara independen; hanya penashih berwenang mengesahkan.
5. Ulangi mekanisme untuk J1 dan J3–J8 setelah memastikan struktur file inventaris yang sesungguhnya, karena penamaan berbeda.

**Status akhir: 40/40 file J2 ada; 0 halaman disahkan CONTENT-FINAL.**

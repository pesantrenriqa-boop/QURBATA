# QJ8 — Hasil pemeriksaan aktual 33 konteks ayat
Tanggal: 29 Oktober 2026. Status: **PASS REFERENSI / HOLD TEKS UTSMANI**.

## Bukti pemeriksaan
Berkas sumber diperoleh langsung dari GitHub: `scripts/qj8_validate_context_manifest.py` dan `books/jilid-8/QJ8-MANIFEST-KONTEKS-AYAT-2026-10-29.csv`.

Pemeriksaan independen menggunakan JavaScript terhadap daftar LENGTHS dan seluruh baris CSV:
- Panjang array surah: **114**.
- Jumlah seluruh ayat dari LENGTHS: **6236**.
- Jumlah kasus CSV: **33**.
- Seluruh rujukan sebelum (n−1 atau N/A pada awal surah) dan sesudah (n+1 atau N/A pada akhir surah) cocok dengan interval target: **33/33 PASS**.
- Ketidaksesuaian yang ditemukan: **0**.

**Batas klaim:** Pemeriksaan ini belum menjalankan GitHub Actions, belum membuktikan teks ayat dari sumber, dan belum mengesahkan fenomena Gharib. Rujukan yang konsisten tidak otomatis menunjukkan setiap kasus autentik atau berbeda.

## Status pengambilan sumber
Percobaan HTTP GET ke `raw.githubusercontent.com` dari container kerja gagal akibat DNS `NameResolutionError`. Tidak ada teks Utsmani yang berhasil diunduh, sehingga tidak ada teks Arab yang boleh diisi secara perkiraan.

## Pekerjaan yang tetap wajib
1. Dapatkan teks Utsmani resmi dari Tanzil, simpan berkas sumber dan SHA-256.
2. Jalankan pengimpor dan pembuat pratinjau, cek seluruh konteks sebelum–target–sesudah.
3. Pastikan target Saktah lintas 18:1–2, dan tiga lokasi lain, benar-benar ditandai menurut edisi mushaf dan jalur Hafs yang ditetapkan.
4. Review ahli dan Decision-ID sebelum menyusun halaman cetak.
5. Register 360 slot lama dan master tetap tidak diubah.

## Referensi
- https://tanzil.net/docs/download
- https://tanzil.net/pub/download/index.php

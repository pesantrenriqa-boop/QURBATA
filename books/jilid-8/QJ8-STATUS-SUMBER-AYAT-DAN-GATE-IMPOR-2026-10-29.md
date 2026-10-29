# QJ8 — Gate pengambilan teks Utsmani dan status eksekusi
Tanggal: 29 Oktober 2026. Status: **HOLD — belum ada teks ayat lengkap yang sah di register konteks**.

## Pemeriksaan yang benar-benar dilakukan
- Manifest `QJ8-MANIFEST-KONTEKS-AYAT-2026-10-29.csv` berisi **33 baris kasus rujukan** dengan 10 kolom per baris.
- `scripts/qj8_import_tanzil_context.py` tersedia sebagai pengimpor offline dari TXT Tanzil (format `surah|ayah|text`).
- `scripts/qj8_build_context.py` tersedia sebagai penyusun pratinjau dari JSON berisi teks per ayat.
- Upaya mengunduh teks Tanzil melalui HTTP POST pada lingkungan eksekusi saat ini **gagal karena DNS `Could not resolve host: tanzil.net`**. Tidak ada file sumber yang berhasil diperoleh, tidak ada ayat yang boleh dianggap sudah diimpor.
- Sumber resmi: https://tanzil.net/docs/download dan https://tanzil.net/pub/download/index.php. Ketentuan: salin verbatim, cantumkan atribusi, jangan ubah teks.

## Prosedur eksekusi aman di komputer yang memiliki akses internet
1. Buka halaman resmi Tanzil dan unduh teks **Uthmani** dengan tanda waqaf, output TXT **surah|ayah|text**.
2. Catat pilihan ekspor (marks/sajdah/tatweel), tanggal dan SHA-256; jangan normalisasi atau mengubah teks.
3. Jalankan:
```bash
python scripts/qj8_import_tanzil_context.py --tanzil /path/to/quran-uthmani.txt --output /tmp/qj8-verses.json
python scripts/qj8_build_context.py --verses /tmp/qj8-verses.json --output /tmp/qj8-context-preview.md
```
4. Periksa bahwa 33/33 kasus memiliki referensi sebelum, target, sesudah yang tersedia. **Lulus integritas data bukan lulus tashih**.
5. Periksa khusus target lintas ayat 18:1–2, penanda saktah, imalah, tashil, isymam, dan variasi tanda baca. Jika tanda tidak ada di edisi, HOLD, jangan menyisipkan ke teks sumber.
6. Reviewer ahli harus menyetujui teks dan bacaan sebelum pemetaan halaman final atau PDF.

## Kekurangan yang harus tetap terbuka
- 33 baris manifest berasal dari bentuk rujukan dalam register lama, **bukan** daftar lengkap kasus Gharib autentik.
- Beberapa rujukan merujuk ayat yang sama (mis. 18:1, 18:2, 18:1–2); deduplikasi fenomena perlu Case-ID.
- Contoh dari surat/ayat yang beragam untuk setiap kompetensi masih perlu seleksi ahli; jangan memaksa contoh yang tidak ada.
- **Jangan menampilkan label `SOURCE_IMPORTED`, `TASHIH_PASS`, atau `PRINT_READY` sebelum ada bukti.**
- Register lama 360 slot, master 40 halaman, dan PDF draf lama tidak diubah.

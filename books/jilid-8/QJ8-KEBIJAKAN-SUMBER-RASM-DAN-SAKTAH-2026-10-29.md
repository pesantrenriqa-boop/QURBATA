# QJ8 — Kebijakan sumber rasm, tanda saktah, dan provenance
Tanggal: 2026-10-29
Status: **DRAFT POLICY / HOLD UNTIL VERIFIED**.

## Risiko yang ditemukan
Repositori publik `nuqayah/quran-text` memiliki `scripts/update.py` yang menjelaskan transformasi atas `quran-uthmani-pause-marks.txt` milik Tanzil untuk mendekati ortografi mushaf Madinah terbaru. Transformasi itu mencakup penggantian karakter ya, sukun, mad, tanwin, tanda waqaf, dan spasi. Dengan demikian, **hasil transformasi tidak identik byte demi byte dengan sumber Tanzil** dan tidak boleh digabung diam-diam.

Bukti: https://github.com/nuqayah/quran-text/blob/main/scripts/update.py

## Keputusan sementara
1. Tetapkan **satu** edisi mushaf sebagai sumber dasar sebelum impor.
2. Simpan `source_name`, `source_url`, `edition`, `downloaded_at`, `sha256`, dan `license/attribution` bersama data impor.
3. Dilarang melakukan Unicode normalization, substitusi karakter, penghapusan tanda waqaf, atau rekonstruksi teks pada kolom `*_text_uthmani` tanpa versi sumber terpisah dan audit.
4. Jika mushaf pilihan memiliki tanda saktah berbeda dari edisi pembanding, tampilkan konflik untuk tashih ahli; jangan melakukan koreksi otomatis.
5. Untuk 4 lokasi Saktah, seluruh **12 ayat unik** harus tersedia verbatim sebelum status `HOLD_NO_SOURCE` boleh diubah.
6. Tanda fokus pembelajaran boleh ditambahkan pada layer desain, tetapi **tidak** pada isi teks mushaf.
7. Status `READY_FOR_PRINT` hanya setelah verifikasi sumber, pemeriksaan lintas ayat, dan persetujuan reviewer.

## Catatan
Repositori alternatif baru ditemukan dan skrip transformasinya dibaca. **Teks ayat belum berhasil diperoleh dan belum diimpor.** Dokumen ini tidak mengesahkan edisi atau riwayat bacaan tertentu dan tidak mengganti master Jilid 8.

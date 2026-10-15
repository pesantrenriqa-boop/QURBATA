# Audit grid dan panel J1 P001–P010 v0.1

Status DRAF QA, bukan perubahan register FROZEN.

## Temuan
1. P001–P009 sudah memiliki grid 8 baris × 3 kelompok pada QJ1_P001-P009_LATIHAN_TARTIL_REVISI_RASIO_8x3_v0.2.md. Dokumen mencantumkan rasio token: P001 60/60 baru (pengecualian awal); P002–P003 34/57 baru; P004 39/65 baru; P005–P009 38/63 baru. Angka ini merupakan klaim dokumen sumber dan memerlukan verifikasi mesin independen sebelum dinyatakan PASS.
2. P010 memiliki grid 8×3 evaluasi 22 bentuk Fathah tanpa kompetensi baru pada QJ1_P010_GRID_EVALUASI_FATHAH_8x3_DRAF_v0.1.md.
3. **Koreksi wajib P010:** header pilot lama menyebut panel Bi'ah هُنَا dan Akhlak وَتَعَاوَنُوا عَلَى الْبِرِّ وَالتَّقْوَى. Keduanya tidak berlaku sebagai panel utama menurut integrasi FROZEN v1.3. Panel resmi P010 adalah Bi'ah اِسْتَمِعْ (REINFORCE) dan Akhlak أَفْشُوا السَّلَامَ بَيْنَكُمْ (REINFORCE). Tahfidz tetap Al-Falaq 4.
4. Panel Bi'ah/Akhlak P001–P009 wajib mengambil QJ1_P001-P010_OVERLAY_4_INVENTARIS_AUTHORITY_v0.2.md, bukan panel lama pada pilot atau dialog guru.
5. Status grid dan dialog guru tetap DRAF; contoh lokasi huruf dalam dialog hanya boleh dipakai jika cocok dengan layout aktual.

## Gerbang produksi
- [ ] Hitung ulang token baru/review dari sel grid, cek whitelist kumulatif dan kemunculan semua grafem
- [ ] Tashih teks ayat, terjemah, serta sumber Akhlak
- [ ] Audit grafem hamzah/alif dan font KFGQPC Uthman Taha
- [ ] Render A5 RTL, ruang tanggal–nilai–paraf, QR, dan proof cetak

Keputusan: panel P010 dikoreksi di lapisan otoritas QA tanpa menimpa pilot historis; tidak boleh memakai header P010 lama untuk generator.

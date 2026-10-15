# QURBATA — KEPUTUSAN PENYELESAIAN 4 INVENTARIS J1–J8 v0.2

**Status: AUDIT KEPUTUSAN / BELUM FINAL ISI.** Cakupan 320 halaman (8 jilid × 40). Tidak boleh menyebut inventaris final hanya karena 320 baris matriks tersedia. Renderer dan desain ditunda sampai keempat inventaris lolos gerbang substansi.

## Empat produk akhir wajib per halaman
1. **Tartil:** fokus/kompetensi legal, latihan aktual terkurasi (atau aktivitas/rubrik untuk jilid lanjut), kunci/standar baca, validasi fonetik dan harakat, identitas sumber.
2. **Bi'ah Arabiyah:** dialog Arab guru–santri yang relevan dengan objek Tartil/Akhlak/Tahfidz, respons natural, instruksi lisan dan catatan pedagogis.
3. **Akhlak:** teks nash Arab yang benar-benar terpilih, jenis nash (ayat/hadis/atsar/maqolah/motto), arti, rujukan spesifik, verifikasi atribusi dan tashih. **Tema bukan hadis; nash kosong bukan final.**
4. **Tahfidz:** surat–ayat per halaman sesuai baseline yang ditunjuk, teks mushaf dan terjemah terverifikasi, target talqin–murajaah–setoran, audit kesinambungan dan konflik lintas register.

## Bukti yang telah ditemukan
| Jilid | Tartil | Dialog | Akhlak | Tahfidz | Status akhir |
|---|---|---|---|---|---|
| J1 | FROZEN urutan 40 kompetensi; grid kandidat P001–P040 tersedia dengan sejumlah QA; CC-001 P002/P005–P009/P011/P012 belum disahkan | Panel Bi'ah FROZEN v1.3 dan skenario 40P; perlu tashih dialog | Panel 40P tersedia; klasifikasi ayat/hadis/motto dan sumber masih perlu verifikasi | Crosswalk 40P tersedia, konflik register/opsi B harus diselesaikan; teks mushaf belum ditashih | **BELUM FINAL** |
| J2 | Fokus 40P tersedia, grid aktual belum disahkan | Pengayaan dan dialog draf | Nash spesifik 40P belum terverifikasi | Crosswalk 40P tersedia; teks belum ditashih | **BELUM FINAL** |
| J3 | Fokus 40P tersedia, contoh sukun perlu tashih fonetik | Pengayaan dan dialog draf | Nash spesifik 40P belum terverifikasi | Crosswalk 40P tersedia; teks belum ditashih | **BELUM FINAL** |
| J4 | Fokus 40P tersedia, latihan/rubrik perlu verifikasi | Pengayaan dan dialog draf | Nash spesifik 40P belum terverifikasi | Crosswalk 40P tersedia; teks belum ditashih | **BELUM FINAL** |
| J5 | Fokus 40P tersedia, latihan/rubrik perlu verifikasi | Pengayaan dan dialog draf | Nash spesifik 40P belum terverifikasi | Crosswalk 40P tersedia; teks belum ditashih | **BELUM FINAL** |
| J6 | Fokus 40P tersedia, latihan/rubrik perlu verifikasi | Pengayaan dan dialog draf | Nash spesifik 40P belum terverifikasi | Crosswalk 40P tersedia; teks belum ditashih | **BELUM FINAL** |
| J7 | Fokus 40P tersedia, latihan/rubrik perlu verifikasi | Pengayaan dan dialog draf | Nash spesifik 40P belum terverifikasi | Crosswalk 40P tersedia; teks belum ditashih | **BELUM FINAL** |
| J8 | Fokus 40P tersedia; aktivitas portofolio/remedial belum memiliki rubrik final | Dialog kontekstual draf | Tema akhlak banyak berupa deskripsi aktivitas, bukan nash terverifikasi | Crosswalk 40P tersedia; teks belum ditashih | **BELUM FINAL** |

## Hierarki otoritas, tanpa perubahan diam-diam
- Tartil J1: `02_MASTER_SYSTEM/QURBATA-J1-TARTIL-PAGE-REGISTER-FROZEN-v1.0.md` (header internal FROZEN v1.1 SOURCE-ALIGNED).
- Bi'ah/Akhlak J1: `03_BOOKS/JILID-1/PAGE_REGISTER_P001-P040_INTEGRATION_FROZEN-v1.3.md`.
- Tahfidz 320P: `02_MASTER_SYSTEM/TAHFIDZ/QURBATA-TAHFIDZ-AYAT-DISTRIBUTION-FROZEN-v1.0.md` dan transkripsi `QURBATA_8J_TAHFIDZ_CROSSWALK_FROZEN_320P_v0.1.md`.
- J2–J8: `QJ2`–`QJ8_MATRIKS_4_INVENTARIS_40P_STAGING_v0.1.md`, tiga berkas pengayaan per jilid, dan bank dialog. **DRAF, bukan FROZEN**.

## Gerbang penyelesaian per halaman
- **G1 Tartil**: semua contoh/latihan nyata tersedia; whitelist kompetensi, struktur, ketepatan makhraj/harakat dan rubrik PASS.
- **G2 Bi'ah**: percakapan dan respons relevan dengan objek aktual serta telah ditashih penutur ahli.
- **G3 Akhlak**: nash spesifik, jenis, arti, sumber, atribusi/takhrij dan tashih lengkap. Dilarang mengisi nash dengan teks generik atau menisbatkan motto sebagai hadis.
- **G4 Tahfidz**: rujukan ayat, teks dan terjemah telah dicocokkan mushaf otoritatif; tidak ada konflik register yang belum diselesaikan.
- **G5 Integrasi**: keempat domain selaras dalam halaman yang sama; review ahli Qur'an, Arab dan pedagogi ditandatangani.

**Aturan final:** hanya halaman dengan G1–G5 PASS dapat diberi `CONTENT-FINAL`; halaman lain `BLOCKED` disertai sebab. Finalisasi tidak sama dengan persetujuan cetak.

## Urutan kerja tanpa mengulang materi
1. Kunci audit sumber dan konflik J1, terutama CC-001 dan baseline Tahfidz versus Opsi B.
2. Susun **bank nash Akhlak 320P** dengan takhrij/atribusi terverifikasi; ini gap terbesar yang jelas dari pengayaan J2–J8.
3. Tashih dan lengkapi latihan Tartil/aktivitas serta rubrik per jilid berdasarkan fokus yang sudah tersusun.
4. Tautkan dialog Arab ke objek latihan final; perbaiki respons yang tidak natural.
5. Cocokkan teks ayat Tahfidz dan arti dengan mushaf, lalu audit kesinambungan 320P.
6. Jalankan G1–G5 per halaman, terbitkan daftar perubahan dan pengesahan sebelum mengaktifkan renderer.

## Keputusan pengendalian
**Tidak ada jilid yang dinyatakan CONTENT-FINAL pada audit ini.** Keputusan CC-001 memerlukan persetujuan pemilik kurikulum; nash/takhrij dan mushaf memerlukan pemeriksaan ahli. Berkas staging tetap dipertahankan, tidak ditimpa.

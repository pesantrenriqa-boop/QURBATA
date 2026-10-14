# DRAF KEPUTUSAN — Penyelarasan Tahfidz QURBATA Jilid 1

**ID usulan:** DEC-TAHFIDZ-J1-ALIGNMENT-001  
**Status:** PROPOSED / MENUNGGU PERSETUJUAN PEMILIK AKADEMIK  
**Sifat:** Naskah untuk ditinjau; **bukan** keputusan aktif, bukan revisi FROZEN, bukan izin cetak.

## 1. Masalah yang diputuskan

Ada ketidaksesuaian antara (A) `DEC-CUR-004` yang menyetujui objek Al-Fatihah untuk validasi ahli tetapi belum mengaktifkannya, (B) distribusi ayat WORKING-v0.1 yang dirujuk FROZEN v1.0, (C) register halaman J1 FROZEN v1.0, dan (D) kandidat J1 page map v0.2 NOT FROZEN. Pada P040, misalnya, distribusi B berisi Al-Ma'un 5–7, register C menghendaki murojaah J1, dan D juga menghendaki konsolidasi.

## 2. Batas kewenangan

- Tartil: empat PAGE_REGISTER J1 FROZEN v1.0 tetap berlaku tanpa perubahan.
- Bi'ah dan Akhlak: PAGE_REGISTER INTEGRATION FROZEN v1.3 tetap berlaku tanpa perubahan.
- Tahfidz: **belum ada pemetaan tunggal yang sah untuk cetak** akibat konflik sumber.
- DEC-CUR-004: objek HAF-000001–000003 tetap kandidat validasi ahli, INACTIVE.

## 3. Opsi yang diajukan kepada pemilik

| Opsi | Penjelasan | Konsekuensi |
|---|---|---|
| A | Pertahankan distribusi Tahfidz WORKING-v0.1 yang dirujuk dokumen FROZEN | Konsistensi rujukan freeze; namun bertentangan dengan target Tahfidz di beberapa register halaman, termasuk P040 |
| B | Gunakan kandidat J1 map v0.2 sebagai dasar revisi berversi, dengan P010/P020/P030/P040 untuk review | Selaras dengan kebutuhan checkpoint Tartil; butuh uji beban P039, validasi ahli, dan perubahan resmi terhadap distribusi lama |
| C | Jadikan objek Al-Fatihah DEC-CUR-004 sebagai jalur utama buku | Perlu desain ulang pemetaan 40 halaman dan keputusan tentang corpus surah lain; DEC-CUR-004 sendiri hanya menyetujui validasi, bukan aktivasi |

**Rekomendasi penyusun (bukan keputusan):** kaji opsi B sebagai *baseline calon revisi*, bukan langsung diterapkan. Alasannya menjaga ruang evaluasi dan konsolidasi, tetapi tidak boleh disahkan sebelum beban P039 dan hubungan dengan DEC-CUR-004 diperiksa. Bila validasi beban tidak lulus, susun opsi B-revisi dengan sebagian target dialihkan ke J2 secara terkendali.

## 4. Hal yang wajib dinyatakan dalam keputusan pemilik

1. Pilih opsi A, B, C, atau opsi revisi yang dijelaskan tertulis.
2. Tegaskan apakah DEC-CUR-004 merupakan jalur objek validasi tersendiri atau pengganti pemetaan Tahfidz buku J1.
3. Tetapkan status hafalan baru pada checkpoint P010, P020, P030, P040.
4. Tentukan dampak terhadap target awal J2, beban hafalan P039, dan RIQA OS.
5. Tetapkan tim validasi qiraah/tahfidz, evidence ID, kriteria kelulusan, dan penanggung jawab.
6. Instruksikan penerbitan register versi baru melalui change control, tanpa mengedit FROZEN lama diam-diam.

## 5. Form keputusan

- **Opsi dipilih:** [BELUM DIISI]
- **Alasan:** [BELUM DIISI]
- **Hubungan dengan DEC-CUR-004:** [BELUM DIISI]
- **Kebijakan checkpoint:** [BELUM DIISI]
- **Dampak J2/RIQA OS:** [BELUM DIISI]
- **Penanggung jawab validasi:** [BELUM DIISI]
- **Evidence-ID:** [BELUM DIISI]
- **Tanggal persetujuan:** [BELUM DIISI]
- **Pengesahan pemilik akademik:** [BELUM ADA]

## 6. Gate pascapersetujuan

Hanya setelah keputusan eksplisit: buat pemetaan 40 halaman baru, lakukan review ahli, tashih nash dan arti, takhrij materi Akhlak, uji retensi dan beban, audit glyph/RTL/layout A5, serta periksa dampak integrasi J2 dan RIQA OS. Sampai gate tersebut selesai, status tetap **NOT PRINT READY**.

## 7. Jejak audit

Dasar: `02_MASTER_SYSTEM/8J_DIALOG_INVENTORY/AUDIT_OTORITAS_TAHFIDZ_J1_v0.1.md` dan `AUDIT_KONFLIK_TAHFIDZ_J1_BLOKER_v0.1.md`. Naskah ini tidak menggantikan kedua audit tersebut.

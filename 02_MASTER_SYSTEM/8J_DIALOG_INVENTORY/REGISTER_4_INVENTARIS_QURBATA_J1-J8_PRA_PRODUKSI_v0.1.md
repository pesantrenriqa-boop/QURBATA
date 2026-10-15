# QURBATA — REGISTER KERJA EMPAT INVENTARIS JILID 1–8

**Status: INVENTARIS DAN KONTROL PENYELESAIAN v0.1; bukan kurikulum baru, bukan keputusan freeze baru.**
**Cakupan:** 8 jilid × 40 halaman = 320 halaman. **Prioritas tetap:** (1) latihan Tartil, (2) dialog guru–santri yang melekat pada Tartil, Akhlak dan Tahfidz, (3) nash Hadis/Akhlak, (4) distribusi surat/ayat Tahfidz. Dokumen sumber tidak boleh diganti dengan materi generik.

## 1. Latihan Tartil J1–J8

- **Inventaris materi 320 halaman tersedia:** `02_MASTER_SYSTEM/QURBATA_8J_INVENTARIS_TARTIL_PRA_PRODUKSI_v0.1.md`. Ini peta kompetensi, **bukan bukti 320 grid latihan telah siap cetak**.
- **J1 P001–P040 FROZEN (urutan kompetensi):** `03_BOOKS/JILID-1/PAGE_REGISTER_P001-P010_FROZEN-v1.0.md`, `PAGE_REGISTER_P011-P020_FROZEN-v1.0.md`, `PAGE_REGISTER_P021-P030_FROZEN-v1.0.md`, `PAGE_REGISTER_P031-P040_FROZEN-v1.0.md`.
- **J1 pilot 8×3 P001–P020:** terdapat berkas terpisah `QJ1_P001-P003_PILOT_LATIHAN_TARTIL_8x3_v0.1.md`, `QJ1_P004-P006_PILOT_LATIHAN_TARTIL_8x3_v0.1.md`, `QJ1_P007-P009_PILOT_LATIHAN_TARTIL_8x3_v0.1.md`, `QJ1_P010_EVALUASI_FATHAH_8x3_v0.1.md`, `QJ1_P011-P013_PILOT_LATIHAN_TARTIL_8x3_v0.1.md`, `QJ1_P014-P018_PILOT_LATIHAN_KASRAH_8x3_v0.1.md`, `QJ1_P019-P020_KASRAH_CHECKPOINT_8x3_v0.1.md` di `02_MASTER_SYSTEM/8J_DIALOG_INVENTORY/`. Semua **DRAFT**, tidak otomatis menggantikan latihan yang mungkin sudah diproduksi dan divalidasi.
- **J2–J8:** master kompetensi 40 halaman/jilid masih DRAFT. Kumpulkan latihan yang telah dibuat di repo sebelum membuat baru. Gate: cek setiap halaman, whitelist huruf/harakat/hukum, jumlah latihan, sumber contoh Qurani, dan render.

## 2. Dialog QURBATA J1–J8

- **J1 P001–P040:** lima berkas `QJ1_P001-P005_SKENARIO_4_DOMAIN_OPSI_B_v0.1.md`, `QJ1_P006-P010_SKENARIO_4_DOMAIN_OPSI_B_v0.1.md`, `QJ1_P011-P020_SKENARIO_4_DOMAIN_OPSI_B_v0.1.md`, `QJ1_P021-P030_SKENARIO_4_DOMAIN_OPSI_B_v0.1.md`, `QJ1_P031-P040_SKENARIO_4_DOMAIN_OPSI_B_v0.1.md` di `02_MASTER_SYSTEM/8J_DIALOG_INVENTORY/`. Panel Bi'ah/Akhlak otoritatif J1: `03_BOOKS/JILID-1/PAGE_REGISTER_P001-P040_INTEGRATION_FROZEN-v1.3.md`.
- **J2–J8:** `02_MASTER_SYSTEM/8J_DIALOG_INVENTORY/QJ{2..8}_P001-P040_DIALOG_TERINTEGRASI_v0.1.md`; respons kontekstual tersedia pada `QJ{2..8}_P001-P040_JAWABAN_KONTEKSTUAL_v0.2.md`. Berkas ini **draf**; respons harus diikat ke **contoh Tartil dan target Tahfidz serta nash Akhlak yang benar-benar terpilih**, bukan pertanyaan generik.
- **Gate dialog per halaman:** instruksi guru Arab + respons santri Arab + objek/contoh Tartil yang tepat + instruksi Tahfidz talqin/setoran + pengantar Akhlak + validasi jawaban posisi (على / فوق / تحت) hanya jika sesuai objek. Percakapan **lisan**, bukan bacaan Tartil mandiri.

## 3. Inventaris Hadis/Akhlak J1–J8

- **J1:** 40 panel Akhlak tersedia di overlay FROZEN v1.3 (ayat, ungkapan hadis, dan motto pedagogis bercampur). **Jangan labeli semuanya sebagai hadis**. Contoh `تَعَلَّمْ — اِعْمَلْ — عَلِّمْ` pada P040 adalah motto, bukan hadis.
- **J2–J8:** tema Akhlak dapat dilacak pada master, tetapi **daftar 40 nash per jilid beserta takhrij/rujukan dan arti belum terbukti lengkap dari berkas yang diperiksa**.
- **Gate nash:** `jilid | halaman | tema | jenis (Qur'an/hadis/atsar/maqolah/motto) | teks Arab | arti Indonesia | sumber kitab/surah/ayat | kualitas/atribusi | status tashih`. Jangan mengarang hadis, sumber, atau status sahih.

## 4. Distribusi surat dan ayat Tahfidz J1–J8

- **FROZEN v1.0:** `02_MASTER_SYSTEM/TAHFIDZ/QURBATA-TAHFIDZ-AYAT-DISTRIBUTION-FROZEN-v1.0.md`.
- **Crosswalk 320 halaman sudah tersedia:** `02_MASTER_SYSTEM/8J_DIALOG_INVENTORY/QURBATA_8J_TAHFIDZ_CROSSWALK_FROZEN_320P_v0.1.md`. Baseline J1–J3: WORKING-v0.1; J4–J7: REBALANCE-v0.2; J8: CORRECTED-v0.3, sesuai instruksi freeze.
- **Cakupan baseline:** Al-Fatihah, Juz 30–27 lengkap, Juz 26 sampai QS Muhammad [47]:12. Ini **klaim audit dari dokumen freeze**, bukan verifikasi mushaf baru.
- **Konflik J1:** opsi B `02_MASTER_SYSTEM/TAHFIDZ/QURBATA-TAHFIDZ-J1-P001-P040-MAP-v0.2.md` hanya **OWNER-APPROVED-FOR-VALIDATION / NOT FROZEN / NOT ACTIVE**; tidak boleh mengganti baseline 320 halaman secara diam-diam. Khusus P039 lima ayat Al-Ma'un 3–7 memerlukan field test.

## Aturan pengerjaan selanjutnya

1. **Inventaris dahulu, deduplikasi, lalu isi celah.** Jangan menulis ulang konten yang telah tersedia.
2. Jangan mengubah empat register Tartil J1 FROZEN, overlay J1 FROZEN v1.3, atau distribusi Tahfidz FROZEN tanpa change control.
3. Target penyelesaian bukan hanya jumlah baris 320, melainkan **isi latihan valid + dialog terikat contoh + nash Akhlak terverifikasi + ayat Tahfidz terlacak**.
4. Label setiap komponen `EXISTING`, `DRAFT-NEEDS-QA`, `MISSING`, atau `FROZEN`; jangan menyebut seluruh 8 jilid selesai sebelum audit.
5. Tahap desain PDF/RIQA OS **ditunda** sampai empat inventaris lengkap dan gerbang verifikasi dilalui.

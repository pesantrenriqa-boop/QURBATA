# AUDIT LATIHAN TARTIL J1 P001–P020 — GRID AKTUAL v0.1

**Status:** hasil inspeksi isi tujuh berkas latihan yang sudah ada, **bukan** produksi ulang dan **bukan** status siap cetak. Branch `renderer/pagedjs-p001-prototype`. Pemeriksaan dilakukan terhadap baris tabel latihan aktual, bukan hanya peta kompetensi.

## Temuan terukur

| Halaman | Baris bernomor 1–8 yang ditemukan | Kelompok pada baris 1–8 | Token Arab pada baris 1–8 | Sumber |
|---|---:|---:|---:|---|
| P001 | 8 | 24 | 60 | [Pilot](./QJ1_P001-P003_PILOT_LATIHAN_TARTIL_8x3_v0.1.md) |
| P002 | 8 | 24 | 57 | [Pilot](./QJ1_P001-P003_PILOT_LATIHAN_TARTIL_8x3_v0.1.md) |
| P003 | 8 | 24 | 57 | [Pilot](./QJ1_P001-P003_PILOT_LATIHAN_TARTIL_8x3_v0.1.md) |
| P004 | 8 | 24 | 65 | [Pilot](./QJ1_P004-P006_PILOT_LATIHAN_TARTIL_8x3_v0.1.md) |
| P005 | 8 | 24 | 63 | [Pilot](./QJ1_P004-P006_PILOT_LATIHAN_TARTIL_8x3_v0.1.md) |
| P006 | 8 | 24 | 63 | [Pilot](./QJ1_P004-P006_PILOT_LATIHAN_TARTIL_8x3_v0.1.md) |
| P007 | 8 | 24 | 63 | [Pilot](./QJ1_P007-P009_PILOT_LATIHAN_TARTIL_8x3_v0.1.md) |
| P008 | 8 | 24 | 63 | [Pilot](./QJ1_P007-P009_PILOT_LATIHAN_TARTIL_8x3_v0.1.md) |
| P009 | 8 | 24 | 63 | [Pilot](./QJ1_P007-P009_PILOT_LATIHAN_TARTIL_8x3_v0.1.md) |
| P010 | 8 | 24 | 72 | [Pilot](./QJ1_P010_EVALUASI_FATHAH_8x3_v0.1.md) |
| P011 | 8 | 24 | 64 | [Pilot](./QJ1_P011-P013_PILOT_LATIHAN_TARTIL_8x3_v0.1.md) |
| P012 | 8 | 24 | 64 | [Pilot](./QJ1_P011-P013_PILOT_LATIHAN_TARTIL_8x3_v0.1.md) |
| P013 | 8 | 24 | 64 | [Pilot](./QJ1_P011-P013_PILOT_LATIHAN_TARTIL_8x3_v0.1.md) |
| P014 | 8 | 24 | 66 | [Pilot](./QJ1_P014-P018_PILOT_LATIHAN_KASRAH_8x3_v0.1.md) |
| P015 | 8 | 24 | 66 | [Pilot](./QJ1_P014-P018_PILOT_LATIHAN_KASRAH_8x3_v0.1.md) |
| P016 | 8 | 24 | 66 | [Pilot](./QJ1_P014-P018_PILOT_LATIHAN_KASRAH_8x3_v0.1.md) |
| P017 | 8 | 24 | 66 | [Pilot](./QJ1_P014-P018_PILOT_LATIHAN_KASRAH_8x3_v0.1.md) |
| P018 | 8 | 24 | 66 | [Pilot](./QJ1_P014-P018_PILOT_LATIHAN_KASRAH_8x3_v0.1.md) |
| P019 | 8 | 24 | 66 | [Pilot](./QJ1_P019-P020_KASRAH_CHECKPOINT_8x3_v0.1.md) |
| P020 | 8 | 24 | 66 | [Pilot](./QJ1_P019-P020_KASRAH_CHECKPOINT_8x3_v0.1.md) |

**Metode hitung:** hanya baris tabel yang kolom pertamanya bernomor 1–8, tiga sel latihan per baris; token dihitung sebagai unit dipisah spasi. P020 memiliki tabel lain berisi identitas huruf tanpa harakat, sehingga tabel tersebut **tidak** dihitung sebagai grid 8×3. Hitungan token bukan bukti kebenaran bacaan.

## QA yang belum lulus

- **P001–P020:** seluruh 20 halaman punya 8 baris × 3 kelompok; struktur ini **PASS (format tabel saja)**. Tidak berarti isi latihan, font atau rasio sudah lulus.
- **P014:** register FROZEN mewajibkan transisi Kasrah; pilot menunjukkan penanaman Kasrah dan 8×3. **Perlu audit** whitelist per halaman dan proporsi token materi baru/murojaah.
- **P019:** 9 bentuk Kasrah baru, termasuk hamzah/alif, membutuhkan audit bentuk grafem; belum final.
- **P020:** checkpoint Fathah+Kasrah, 29 identitas huruf dan nama dua harakat. **Perlu audit terpisah** cakupan 29 identitas, keterbacaan dan kapasitas A5; tidak boleh disederhanakan menjadi grid saja.
- **P021–P040:** tidak termasuk tujuh berkas pilot yang diaudit; **belum dapat dinyatakan tidak ada di seluruh repo**, harus telusuri renderer/master produksi sebelum menulis latihan pengganti.
- **Bi'ah/Akhlak/Tahfidz:** penautan 4 domain masih perlu cek skenario guru–santri terhadap token latihan aktual, nash Akhlak dan target Tahfidz. Baseline FROZEN tidak diganti oleh Opsi B kandidat.

## Tindak lanjut langsung

Audit whitelist seluruh token per halaman, sebaran review kumulatif (termasuk `ءَ / أَ`), lalu tautkan tanya-jawab Arab ke huruf atau tanda yang benar-benar ada pada latihan. Catat hasil `PASS/REVISE` per halaman. Jangan klaim buku siap cetak sampai pemeriksaan teks Qur'an, sumber Akhlak, font, RTL, dan layout selesai.

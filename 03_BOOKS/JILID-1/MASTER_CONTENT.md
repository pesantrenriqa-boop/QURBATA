# QURBATA JILID 1 — MASTER CONTENT

Status: **CONTENT FROZEN / FULL AUDIT BUILD READY**

Dokumen ini menjadi tempat resmi konsolidasi isi Jilid 1 dan tunduk pada:
- `02_MASTER_SYSTEM/QURBATA_TARTIL_J1_MASTER_CURRICULUM_FROZEN-v1.0.md`
- `02_MASTER_SYSTEM/QURBATA-J1-CUMULATIVE-MUROJAAH-FROZEN-v1.0.md`

## Prinsip
- Master/register adalah sumber kebijakan; generator/PDF bukan sumber kebijakan.
- Sumber lama hanya bahan recovery dan tidak otomatis menjadi authority.
- Setiap blok harus tunduk pada register frozen masing-masing.
- Status FINAL CETAK hanya dapat diberikan setelah audit substansi dan visual satu buku disahkan.

## Struktur
- PAGE-001 sampai PAGE-040.

## Register resmi

### P001–P010
Sumber resmi:
- `03_BOOKS/JILID-1/PAGE_REGISTER_P001-P010_FROZEN-v1.0.md`

Keputusan kunci:
- P001–P009: Fathah bertahap sampai `فَ قَ`.
- P002 memperkenalkan `ءَ أَ`; keduanya tetap berada di review pool kumulatif dan tidak boleh hilang setelah P005.
- P010: evaluasi 22 bentuk Fathah yang legal P001–P009.
- Tidak ada `كَ لَ مَ نَ هَ وَ يَ` sebelum P011–P013.

Status produksi:
- Generator P001–P010: MERGED TO MAIN.
- Variety gate halaman awal: AKTIF.
- Cumulative review: AKTIF.
- Audit P001/P005/P010: LULUS.
- KFGQPC Uthman Taha: EMBEDDED.

### P011–P020
Sumber resmi:
- `03_BOOKS/JILID-1/PAGE_REGISTER_P011-P020_FROZEN-v1.0.md`

Keputusan kunci:
- P011: `كَ لَ`
- P012: `مَ نَ`
- P013: `هَ وَ يَ`
- P014: awal/penanaman Kasrah.
- P015–P019: perluasan Kasrah sampai seluruh huruf tercakup.
- P020: checkpoint Fathah + Kasrah.
- Murojaah kumulatif sejak P001.

Status produksi:
- Generator P011–P020: MERGED TO MAIN.
- P014/P019/P020: audit visual lulus.
- KFGQPC Uthman Taha: EMBEDDED.

### P021–P030
Sumber resmi:
- `03_BOOKS/JILID-1/PAGE_REGISTER_P021-P030_FROZEN-v1.0.md`

Keputusan kunci:
- P021: awal Dhammah.
- P021–P027: Dhammah bertahap sampai seluruh huruf tercakup.
- P028: penguatan Dhammah.
- P029–P030: latihan kumulatif Fathah–Kasrah–Dhammah.
- Jadwal Tahfidz/Bi’ah Arabiyah/Akhlak tetap mengikuti nomor pertemuan.

Status produksi:
- Generator P021–P030: MERGED TO MAIN.
- Rasio halaman normal: 38 token aktif : 26 review (~59,4% : 40,6%).
- Meaningful-practice gate: AKTIF.
- P021/P027/P030: audit visual lulus.
- KFGQPC Uthman Taha: EMBEDDED.

### P031–P040
Sumber resmi:
- `03_BOOKS/JILID-1/PAGE_REGISTER_P031-P040_FROZEN-v1.0.md`

Keputusan kunci:
- P031–P039: penguatan/evaluatif kumulatif Fathah–Kasrah–Dhammah; tidak ada kompetensi baru.
- P040: checkpoint akhir Jilid 1.
- P040 memuat 29 identitas huruf tanpa harakat + nama Fathah/Kasrah/Dhammah.
- P040 tidak memperkenalkan sambung/mad/tanwin/sukun/tasydid.

Status produksi:
- Generator P031–P040: MERGED TO MAIN.
- P031/P039/P040: audit visual lulus.
- Checkpoint P040: audit visual lulus.
- KFGQPC Uthman Taha: EMBEDDED.

## Full-book audit P001–P040

Pipeline resmi:
- `.github/workflows/qurbata-j1-full-audit.yml`
- `production/vivliostyle/scripts/merge-j1-full-audit.mjs`
- npm target: `build:j1-full:pdf`

Hasil audit teknis terakhir:
- 40 halaman: **LULUS**.
- Empat blok dibangun ulang dari register frozen sebelum digabung: **LULUS**.
- Marker KFGQPC Uthman Taha setelah merge: **LULUS**.
- Transisi P010→P011: **LULUS VISUAL**.
- Transisi P020→P021: **LULUS VISUAL**.
- Transisi P030→P031: **LULUS VISUAL**.
- P040 checkpoint akhir: **LULUS VISUAL**.
- QR RIQA OS dan Tanggal–Nilai–TTD: tersedia pada seluruh halaman produksi.

## Status keseluruhan
- Repository structure: READY
- Master curriculum Jilid 1: FROZEN v1.0
- Cumulative murojaah rule: FROZEN v1.0
- P001–P010 register: FROZEN; pipeline MERGED TO MAIN
- P011–P020 register: FROZEN; pipeline MERGED TO MAIN
- P021–P030 register: FROZEN; pipeline MERGED TO MAIN
- P031–P040 register: FROZEN; pipeline MERGED TO MAIN
- Full-book P001–P040 audit pipeline: MERGED TO MAIN
- Full-book 40-page AUDIT PDF: BUILD SUCCESS
- Status penerbitan: **BELUM FINAL CETAK**. Perubahan selanjutnya wajib melalui revisi master/register yang terdokumentasi, bukan edit ad hoc pada PDF/generator.

## Sumber prioritas
1. Master curriculum frozen.
2. Page register frozen P001–P040.
3. Generator produksi yang diturunkan dari register.
4. PDF audit sebagai output verifikasi.
5. Draft/sumber lama hanya sebagai arsip recovery.

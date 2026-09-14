# QURBATA JILID 1 — MASTER CONTENT

Status: CONTROLLED RECOVERY / PARTIAL FREEZE

Dokumen ini menjadi tempat resmi konsolidasi isi Jilid 1 dan tunduk pada:
- `02_MASTER_SYSTEM/QURBATA_TARTIL_J1_MASTER_CURRICULUM_FROZEN-v1.0.md`
- `02_MASTER_SYSTEM/QURBATA-J1-CUMULATIVE-MUROJAAH-FROZEN-v1.0.md`

## Prinsip
- Tidak membuat ulang materi lama tanpa audit.
- Mengambil dari sumber QURBATA yang sudah pernah disusun.
- Jika sumber lama bertentangan dengan keputusan terbaru, keputusan master frozen yang berlaku.
- Setiap blok halaman diverifikasi sebelum FREEZE.
- Generator/PDF tidak boleh menjadi sumber kebijakan kurikulum.

## Struktur
- PAGE-001 sampai PAGE-040.

## Register yang sudah dibekukan

### P011–P020
Sumber resmi:
- `03_BOOKS/JILID-1/PAGE_REGISTER_P011-P020_FROZEN-v1.0.md`

Keputusan kunci:
- P011: `كَ لَ`
- P012: `مَ نَ`
- P013: `هَ وَ يَ`
- P014: **awal/penanaman Kasrah**.
- P015–P019: perluasan Kasrah bertahap hingga seluruh huruf tercakup.
- P020: **checkpoint khusus** Fathah + Kasrah.
- Murojaah wajib kumulatif sejak P001.

Status produksi:
- Generator P011–P020: TERSEDIA DI MAIN.
- Workflow audit PDF: TERSEDIA DI MAIN.
- KFGQPC Uthman Taha: EMBEDDED pada build audit yang lolos.
- P014/P019/P020: audit visual terakhir lulus.
- Output tetap berlabel AUDIT sampai gate final kurikulum untuk satu blok dinyatakan selesai.

### P021–P030
Sumber resmi:
- `03_BOOKS/JILID-1/PAGE_REGISTER_P021-P030_FROZEN-v1.0.md`

Keputusan kunci:
- P021: **awal Dhammah**, karena Kasrah sudah dituntaskan di P019 dan P020 adalah checkpoint.
- P021–P027: Dhammah bertahap sampai seluruh huruf tercakup.
- P028: penguatan Dhammah.
- P029–P030: latihan kumulatif Fathah–Kasrah–Dhammah.
- Jadwal Tahfidz/Bi’ah Arabiyah/Akhlak tetap mengikuti nomor pertemuan P021–P030 dan tidak ikut bergeser akibat recovery struktur Tartil.
- Murojaah tetap kumulatif sejak P001.

Status produksi:
- Generator P021–P030: TERSEDIA DI MAIN.
- Workflow audit PDF: TERSEDIA DI MAIN.
- Rasio latihan normal: 38 token aktif : 26 token review (~59,4% : 40,6%).
- Gate contoh 3 huruf bermakna/nyaris bermakna: AKTIF.
- KFGQPC Uthman Taha: EMBEDDED pada build audit yang lolos.
- P021/P027/P030: audit visual terakhir lulus.
- Grafem Hamzah/Alif pada P027: lolos audit visual.
- Output tetap berlabel AUDIT sampai gate final kurikulum blok dinyatakan selesai.

## Status produksi keseluruhan
- Repository structure: READY
- Master curriculum Jilid 1: FROZEN v1.0
- Cumulative murojaah rule: FROZEN v1.0
- P011–P020 page register: FROZEN v1.0
- P011–P020 production pipeline: MERGED TO MAIN
- P021–P030 page register: FROZEN v1.0
- P021–P030 production pipeline: MERGED TO MAIN
- P031–P040: MENUNGGU RECOVERY + FREEZE REGISTER

## Sumber prioritas
1. Master curriculum frozen.
2. Page register frozen.
3. QURBATA Jilid 1 final/draft lama sebagai bahan recovery.
4. Hasil koreksi dan keputusan pengembangan QURBATA yang sudah disahkan.
5. Dokumen foundation QURBATA.

## Catatan recovery penting
Sumber produksi lama tetap disimpan sebagai bukti historis/audit. Struktur lama tidak otomatis menjadi authority. Pada P011–P030 telah ditemukan pergeseran fase yang harus dikoreksi: Kasrah selesai lebih awal di master terbaru sehingga Dhammah dimajukan mulai P021. Produk baru wajib mengikuti register frozen terbaru.

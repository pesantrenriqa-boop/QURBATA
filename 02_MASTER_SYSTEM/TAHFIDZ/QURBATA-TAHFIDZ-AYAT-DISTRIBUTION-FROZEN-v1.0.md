# QURBATA TAHFIDZ — AYAT DISTRIBUTION FROZEN v1.0

**Document ID:** QTS-AYAT-DISTRIBUTION-FROZEN-001  
**Status:** FROZEN  
**Date:** 15 August 2026  
**Frozen from:** `QURBATA-TAHFIDZ-AYAT-DISTRIBUTION-v0.3-CORRECTED.md`

## Freeze Decision

Pembagian target tahfidz QURBATA Jilid 1–8 dinyatakan **FROZEN v1.0** sebagai baseline corpus dan distribusi 320 halaman.

Prinsip yang dikunci:

- total 8 jilid × 40 halaman = 320 halaman;
- Al-Fatihah menjadi corpus wajib khusus;
- jalur utama hafalan bergerak berurutan dari Juz 30 → Juz 29 → Juz 28 → Juz 27 → Juz 26;
- ayat pendek boleh digabung dalam satu halaman;
- ayat panjang/beban berat boleh dibagi beberapa halaman;
- pembagian beban meningkat bertahap dari J1 menuju J8;
- tidak boleh melompati ayat dalam jalur juz tanpa keputusan revisi corpus resmi.

## Frozen Coverage

Baseline frozen menghasilkan:

1. Al-Fatihah — lengkap sebagai corpus wajib khusus.
2. Juz 30 — lengkap.
3. Juz 29 — lengkap.
4. Juz 28 — lengkap.
5. Juz 27 — lengkap.
6. Juz 26 — berlanjut secara berurutan sampai QS Muhammad [47]:12.

**Endpoint frozen:** `QS Muhammad [47]:12`.

## Frozen Page Source

### Jilid 1–3
Gunakan mapping pada `QURBATA-TAHFIDZ-AYAT-DISTRIBUTION-WORKING-v0.1.md` untuk J1–J3.

### Jilid 4–7
Gunakan mapping pada `QURBATA-TAHFIDZ-AYAT-DISTRIBUTION-v0.2-REBALANCE.md` untuk J4–J7.

### Jilid 8
Gunakan mapping corrected pada `QURBATA-TAHFIDZ-AYAT-DISTRIBUTION-v0.3-CORRECTED.md`.

Urutan J8 yang dikunci berakhir:

- P023 Adh-Dhariyat 31–40
- P024 Adh-Dhariyat 41–50
- P025 Adh-Dhariyat 51–60
- P026 Adh-Dhariyat 1–10
- P027 Adh-Dhariyat 11–20
- P028 Adh-Dhariyat 21–30
- P029–P037 Al-Ahqaf 1–35
- P038 Muhammad 1–4
- P039 Muhammad 5–8
- P040 Muhammad 9–12

Catatan urutan mushaf/juz: Adh-Dhariyat 31–60 menutup Juz 27, sedangkan Adh-Dhariyat 1–30 adalah awal bagian Juz 26 dalam arah corpus hafalan QURBATA yang bergerak mundur antarsurah dari akhir Al-Qur'an. Karena itu perpindahan tersebut disengaja dan bukan gap ayat.

## Freeze Audit

`PAGE_COUNT = 320/320 PASS`

`MAJOR_LOAD_STRESS = CORRECTED`

`JUZ_30 = COMPLETE`

`JUZ_29 = COMPLETE`

`JUZ_28 = COMPLETE`

`JUZ_27 = COMPLETE`

`JUZ_26_ENDPOINT = MUHAMMAD_12`

`KNOWN_DUPLICATE_AYAT = NONE`

`KNOWN_SKIPPED_AYAT_WITHIN_FROZEN_CORPUS = NONE`

`FREEZE_STATUS = PASS`

## Change Control

Mulai v1.0, file ini adalah baseline resmi pembagian ayat QURBATA Tahfidz. Perubahan berikutnya tidak boleh diam-diam mengganti target halaman.

Jika nanti ditemukan beban halaman yang kurang sesuai ketika dipasang ke buku QURBATA nyata, buat versi revisi baru (`v1.1` atau lebih tinggi) dengan alasan perubahan dan halaman yang terdampak. Jangan menimpa keputusan frozen v1.0.

## Next

Tahap berikutnya adalah menurunkan baseline frozen ini menjadi data siap-produksi untuk setiap halaman QURBATA, sehingga nama surat dan nomor ayat dapat ditampilkan pada halaman buku tanpa mengubah corpus frozen.
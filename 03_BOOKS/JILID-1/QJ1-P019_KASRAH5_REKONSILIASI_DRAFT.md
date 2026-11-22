# QURBATA Jilid 1 — P019 Kasrah 5 (DRAF REKONSILIASI)

**Tanggal:** 22 November 2026. **Status:** DRAF PRODUKSI; BELUM FROZEN, BELUM SIAP CETAK.

## Sumber dan keputusan alur

- Alur produksi draf: P014 pengayaan Fathah → P015 Kasrah 1 → P016 Kasrah 2 → P017 Kasrah 3 → P018 Kasrah 4 → **P019 Kasrah 5**.
- Register resmi `03_BOOKS/JILID-1/PAGE_REGISTER_P011-P020_FROZEN-v1.0.md` **masih menetapkan P019 Kasrah 6**. Dokumen ini **tidak mengubah** FROZEN.
- Seluruh 24 latihan diambil dari keluaran deterministik generator resmi `production/vivliostyle/scripts/build-p011-p020-from-frozen.mjs` **spesifikasi P018 Kasrah 5**, blob `f3cc15a5b696231b57ded8e3bd173d0ec4b83b6e`, lalu diurutkan 16 kelompok tiga huruf sebelum 8 kelompok dua huruf; tidak menambah latihan karangan.

## 1. Tartil — Kasrah 5

**Kompetensi baru:** `عِ غِ فِ قِ`. **Review:** Kasrah 1–4 (`بِ تِ ثِ جِ حِ خِ دِ ذِ رِ زِ سِ شِ صِ ضِ طِ ظِ`) dan seluruh Fathah sebelumnya. Semua latihan huruf lepas tanpa Dhammah, sukun, mad, tanwin, tasydid, atau huruf sambung.

| Baris | Kolom 1 | Kolom 2 | Kolom 3 |
|---:|---|---|---|
| 1 | شَ عِ رَ | لَ عِ بَ | نَ عِ مَ |
| 2 | صَ غِ رَ | رَ غِ بَ | حَ فِ ظَ |
| 3 | فَ قِ هَ | بَ قِ يَ | قِ عِ هَ |
| 4 | غِ فِ وَ | قِ عِ يَ | غِ بِ تِ |
| 5 | فِ ثِ جِ | قِ حِ خِ | عِ دِ ذِ |
| 6 | غِ رِ زِ | عِ غِ | فِ قَ |
| 7 | قِ كَ | عِ غِ | فِ لَ |
| 8 | قِ مَ | عِ غِ | فِ نَ |

### Audit whitelist dan duplikasi

- **24/24 slot terisi**, **16 kelompok tiga huruf + 8 kelompok dua huruf**; total 64 token.
- **22/24 slot unik**. `عِ غِ` terdapat tiga kali, yaitu dua duplikasi; harus diganti dengan sumber yang sah atau disahkan melalui editorial.
- **0 token Kasrah prematur**: semua token sesuai Fathah kumulatif atau Kasrah sampai tahap 5. Audit ini hanya pemeriksaan kompetensi karakter, bukan persetujuan final kebahasaan atau visual.
- **Gate cetak BLOCKED** karena dua duplikasi, ketidaksesuaian pemetaan P019 dengan FROZEN, serta belum ada verifikasi layout dan kompetensi final.

## 2. Bahasa Arab — INTRODUCE (usulan maju dari P021)

**`أَغْلِقِ الْكِتَابَ`** — **Tutuplah buku.**

- **Asal:** `PAGE_REGISTER_P001-P040_INTEGRATION_FROZEN-v1.3.md`, P021 INTRODUCE (P022 REPEAT-1, P023 REPEAT-2).
- **Alasan pemajuan:** materi `اِفْتَحِ الْكِتَابَ` sudah diperkenalkan pada draf P016, REPEAT-1 pada P017, REPEAT-2 pada P018; P019 harus progresif.
- **Latihan nyata:** guru mengucapkan `أَغْلِقِ الْكِتَابَ`, santri menutup buku, lalu mengulang kalimat.
- **Status:** usulan pemetaan draf, bukan perubahan FROZEN. P020 dan P021 perlu direkonsiliasi agar tidak melompati atau menduplikasi tahapan resmi.

## 3. Akhlak — INTRODUCE (usulan maju dari P021)

**`أَدِّ الْأَمَانَةَ إِلَى مَنِ ائْتَمَنَكَ`** — **Tunaikanlah amanah kepada orang yang mempercayaimu.**

- **Asal:** `PAGE_REGISTER_P001-P040_INTEGRATION_FROZEN-v1.3.md`, P021–P023 INTRODUCE → REPEAT-2.
- **Alasan pemajuan:** `وَقُولُوا لِلنَّاسِ حُسْنًا` sudah dipakai P016–P018.
- **Pembiasaan:** santri mengembalikan barang pinjaman, menjaga titipan, dan melaksanakan tanggung jawab.
- **Status:** usulan pemetaan draf, bukan perubahan FROZEN.

## 4. Tahfidz — QS. Al-Masad ayat 2 (usulan)

**`مَا أَغْنَىٰ عَنْهُ مَالُهُ وَمَا كَسَبَ`** — **Tidaklah berguna baginya hartanya dan apa yang dia usahakan.**

- **Alur draf:** P016 Al-Ikhlas:3 (ditetapkan pengguna) → P017 Al-Ikhlas:4 (usulan) → P018 Al-Masad:1 (usulan) → **P019 Al-Masad:2 (usulan)**.
- **Asal ayat:** generator resmi versi lama mencantumkan **Al-Masad:2** untuk P017; penempatan di P019 merupakan usulan penyesuaian alur setelah ketetapan P016.
- Teks sumber generator tanpa tanda alif kecil: `مَا أَغْنَى عَنْهُ مَالُهُ وَمَا كَسَبَ`. Penulisan `أَغْنَىٰ` pada draf ini perlu audit font Utsmani dan konsistensi sebelum cetak.
- **Belum disahkan** sebagai revisi master Tahfidz FROZEN.

## Gate final dan tindak lanjut

1. Temukan dua latihan pengganti yang benar-benar bersumber untuk menghapus duplikasi `عِ غِ`; jangan mengarang.
2. Rekonsiliasi perubahan pemetaan Tartil P019 dan checkpoint P020 terhadap FROZEN.
3. Rekonsiliasi BA/Akhlak P019–P021 agar tidak melompati `اِقْرَأْ` dan `وَقُلْ رَبِّ زِدْنِي عِلْمًا` pada P020 resmi.
4. Verifikasi Tahfidz P017–P019 terhadap master, tipografi Utsmani, dan render final.
5. **Tidak mengubah** register FROZEN, generator produksi, atau page object yang sudah disahkan.

## Referensi repo

- `03_BOOKS/JILID-1/QJ1-P018_KASRAH4_REKONSILIASI_DRAFT.md`
- `03_BOOKS/JILID-1/PAGE_REGISTER_P011-P020_FROZEN-v1.0.md`
- `03_BOOKS/JILID-1/PAGE_REGISTER_P001-P040_INTEGRATION_FROZEN-v1.3.md`
- `03_BOOKS/JILID-1/AMENDMENT_TAHFIDZ_P016_2026-11-22.md`
- `production/vivliostyle/scripts/build-p011-p020-from-frozen.mjs`

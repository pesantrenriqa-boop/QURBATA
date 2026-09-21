# QURBATA JILID 1 — TARTIL CONTENT MASTER P001–P020

**Version:** v0.1  
**Status:** WORKING CONTENT MASTER — PDF PRODUCTION PAUSED  
**Effective:** 2026-09-21

## Authority
Dokumen ini adalah tahap kurasi isi sebelum produksi PDF. Urutan kompetensi Tartil tetap mengikuti Page Register frozen. Dokumen ini tidak mengubah urutan pengenalan huruf/harakat.

## Hard rules
1. Generator PDF tidak boleh menciptakan kelompok 3 huruf secara otomatis.
2. Setiap kelompok 3 huruf harus berstatus **WORD**: kata Arab yang sah dan bermakna dengan harakat yang tercetak.
3. Prioritas: Qurani → fusha sah → bentuk leksikal terverifikasi.
4. Kata tidak boleh memakai huruf/harakat/fitur yang belum legal pada halaman itu.
5. Tidak boleh memaksakan sukun, tasydid, tanwin, mad, sambung, atau harakat tahap berikutnya.
6. Jika stok kata legal sedikit, kata sah boleh diulang terkontrol; kelompok 2 huruf tetap boleh fonetik.
7. Detached **ه** wajib dua lubang pada tahap renderer.
8. Setiap kata harus mempunyai gloss Indonesia untuk audit internal.
9. P019 dan P020 wajib curated, bukan random/cycling.

## Register kompetensi dan kandidat WORD

| Page | Kompetensi baru | Kandidat WORD legal | Gloss audit | Status |
|---|---|---|---|---|
| P001 | بَ تَ ثَ | — | Belum dipaksakan; stok huruf belum memadai | HOLD |
| P002 | ءَ أَ | — | Belum dipaksakan | HOLD |
| P003 | جَ حَ خَ | بَحَثَ | mencari/meneliti | WORD |
| P004 | دَ ذَ رَ زَ | — | Kurasi lanjutan | REVIEW |
| P005 | سَ شَ | دَرَسَ | belajar/telah belajar | WORD |
| P006 | صَ ضَ | صَبَرَ ؛ ضَرَبَ ؛ حَصَدَ | bersabar; memukul; memanen | WORD |
| P007 | طَ ظَ | طَلَبَ ؛ نَظَرَ ؛ ظَهَرَ | mencari/meminta; melihat; tampak | WORD |
| P008 | عَ غَ | عَمَلَ ؛ عَلَمَ ؛ غَفَرَ | berbuat/bekerja; mengetahui/menandai (perlu audit bentuk); mengampuni | REVIEW |
| P009 | فَ قَ | فَتَحَ ؛ قَرَأَ ؛ فَرَحَ | membuka; membaca; bergembira | WORD |
| P010 | Evaluasi Fathah I | Kandidat sah P003–P009 | Review seluruh Fathah legal | CURATE |
| P011 | كَ لَ | كَتَبَ ؛ أَكَلَ ؛ مَلَكَ | menulis; makan; memiliki/menguasai | WORD |
| P012 | مَ نَ | مَنَعَ ؛ نَزَلَ ؛ عَمَلَ | mencegah; turun; bekerja | WORD |
| P013 | هَ وَ يَ | هَدَى* ؛ وَجَدَ | memberi petunjuk*; menemukan | REVIEW |
| P014 | Kasrah بِ تِ ثِ جِ | — | Kurasi kata campuran Fathah–Kasrah tanpa fitur ilegal | CURATE |
| P015 | حِ خِ دِ ذِ | — | Kurasi | CURATE |
| P016 | رِ زِ سِ شِ | — | Kurasi | CURATE |
| P017 | صِ ضِ طِ ظِ | — | Kurasi | CURATE |
| P018 | عِ غِ فِ قِ | — | Kurasi | CURATE |
| P019 | كِ لِ مِ نِ هِ وِ يِ ءِ إِ | — | Curated completion Kasrah | CURATE |
| P020 | Checkpoint Fathah + Kasrah | — | Curated checkpoint; bukan random | CURATE |

\* Kandidat yang memerlukan bentuk/fitur di luar whitelist halaman harus ditolak saat audit final. Entri REVIEW bukan izin produksi.

## Audit fields per final word
Setiap entri final wajib dicatat sebagai:
`PAGE | ARABIC | ROOT/LEMMA | GLOSS_ID | QURAN/FUSHA | LEGAL_FEATURES | VERIFIED`

## Production gate
`REGISTER PASS → WORD-BANK PASS → HARAKAT PASS → MEANING PASS → HA-TWO-HOLE PASS → CURATED PAGE PASS → PDF GENERATION`

**PDF P001–P020 tidak boleh dibangun ulang sebagai FINAL sebelum CONTENT MASTER ini berstatus FROZEN.**

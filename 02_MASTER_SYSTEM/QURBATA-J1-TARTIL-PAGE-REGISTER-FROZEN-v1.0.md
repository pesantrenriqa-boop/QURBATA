# QURBATA JILID 1 — TARTIL PAGE REGISTER

Status: **FROZEN v1.0**  
Effective: 2026-09-25  
Authority: `QURBATA_TARTIL_BOOK_COMPOSITION_RULES_FROZEN-v1.4.md` status v1.6.6

## Prinsip
- Register ini adalah sumber TARGET/REVIEW untuk generator Tartil Jilid 1.
- Generator dilarang menebak TARGET dari nomor halaman.
- `REGULAR` = 2 baris pertama EXACT-2 TARGET-only; 6 baris berikut EXACT-3 dan setiap kelompok memuat TARGET.
- `CHECKPOINT` = struktur khusus curated; tidak memakai fallback REGULAR.
- Semua bentuk tetap detached/tunggal.

## FASE FATHAH

| Page | Type | TARGET | REVIEW_ALLOWED |
|---|---|---|---|
| P001 | REGULAR-FOUNDATION | بَ تَ ثَ | — |
| P002 | REGULAR | ءَ أَ | بَ تَ ثَ |
| P003 | REGULAR | جَ حَ خَ | ءَ أَ بَ تَ ثَ |
| P004 | REGULAR | دَ ذَ رَ | ءَ أَ بَ تَ ثَ جَ حَ خَ |
| P005 | REGULAR | زَ سَ شَ | ءَ أَ بَ تَ ثَ جَ حَ خَ دَ ذَ رَ |
| P006 | REGULAR | صَ ضَ طَ | ءَ أَ بَ تَ ثَ جَ حَ خَ دَ ذَ رَ زَ سَ شَ |
| P007 | REGULAR | ظَ عَ غَ | seluruh Fathah P001–P006 |
| P008 | REGULAR | فَ قَ كَ | seluruh Fathah P001–P007 |
| P009 | REGULAR | لَ مَ نَ هَ وَ يَ | seluruh Fathah P001–P008 |
| P010 | CHECKPOINT-FATHAH | seluruh huruf Fathah legal | P001–P009 |

> P009 memiliki enam TARGET; dua baris penanaman harus dikurasi dari TARGET P009 dan tidak boleh memakai review.

## FASE KASRAH

Prinsip fase Kasrah: huruf TARGET adalah huruf ber-Kasrah pada halaman itu. REVIEW_ALLOWED mencakup seluruh Fathah yang sudah legal + Kasrah dari halaman sebelumnya.

| Page | Type | TARGET | REVIEW_ALLOWED |
|---|---|---|---|
| P011 | REGULAR | بِ تِ ثِ | seluruh Fathah |
| P012 | REGULAR | ءِ إِ | seluruh Fathah + Kasrah P011 |
| P013 | REGULAR | جِ حِ خِ | seluruh Fathah + Kasrah P011–P012 |
| P014 | REGULAR | دِ ذِ رِ | seluruh Fathah + Kasrah P011–P013 |
| P015 | REGULAR | زِ سِ شِ | seluruh Fathah + Kasrah P011–P014 |
| P016 | REGULAR | صِ ضِ طِ | seluruh Fathah + Kasrah P011–P015 |
| P017 | REGULAR | ظِ عِ غِ | seluruh Fathah + Kasrah P011–P016 |
| P018 | REGULAR | فِ قِ كِ | seluruh Fathah + Kasrah P011–P017 |
| P019 | REGULAR-CURATED | لِ مِ نِ هِ وِ يِ | seluruh Fathah + Kasrah P011–P018 |
| P020 | CHECKPOINT-FATHAH-KASRAH | seluruh Fathah + Kasrah legal | P001–P019 |

## FASE DHAMMAH

Prinsip fase Dhammah: huruf TARGET adalah huruf ber-Dhammah. REVIEW_ALLOWED mencakup seluruh Fathah + Kasrah legal dan Dhammah halaman sebelumnya.

| Page | Type | TARGET | REVIEW_ALLOWED |
|---|---|---|---|
| P021 | REGULAR | بُ تُ ثُ | seluruh Fathah + Kasrah |
| P022 | REGULAR | ءُ أُ | seluruh Fathah + Kasrah + Dhammah P021 |
| P023 | REGULAR | جُ حُ خُ | seluruh Fathah + Kasrah + Dhammah P021–P022 |
| P024 | REGULAR | دُ ذُ رُ | seluruh Fathah + Kasrah + Dhammah P021–P023 |
| P025 | REGULAR | زُ سُ شُ | seluruh Fathah + Kasrah + Dhammah P021–P024 |
| P026 | REGULAR | صُ ضُ طُ | seluruh Fathah + Kasrah + Dhammah P021–P025 |
| P027 | REGULAR | ظُ عُ غُ | seluruh Fathah + Kasrah + Dhammah P021–P026 |
| P028 | REGULAR | فُ قُ كُ | seluruh Fathah + Kasrah + Dhammah P021–P027 |
| P029 | REGULAR | لُ مُ نُ هُ وُ يُ | seluruh Fathah + Kasrah + Dhammah P021–P028 |
| P030 | CHECKPOINT-DHAMMAH | seluruh Fathah + Kasrah + Dhammah legal | P001–P029 |

## P031–P040 — HOLD / SPEC REQUIRED

P031–P040 **tidak boleh digenerasikan dari tebakan atau pool algoritmik** sampai kompetensi halaman-halaman ini diverifikasi terhadap master curriculum yang sah. Status sementara:

| Page | Type | TARGET | Status |
|---|---|---|---|
| P031 | HOLD | — | SPECIAL_PAGE_SPEC_MISSING |
| P032 | HOLD | — | SPECIAL_PAGE_SPEC_MISSING |
| P033 | HOLD | — | SPECIAL_PAGE_SPEC_MISSING |
| P034 | HOLD | — | SPECIAL_PAGE_SPEC_MISSING |
| P035 | HOLD | — | SPECIAL_PAGE_SPEC_MISSING |
| P036 | HOLD | — | SPECIAL_PAGE_SPEC_MISSING |
| P037 | HOLD | — | SPECIAL_PAGE_SPEC_MISSING |
| P038 | HOLD | — | SPECIAL_PAGE_SPEC_MISSING |
| P039 | HOLD | — | SPECIAL_PAGE_SPEC_MISSING |
| P040 | HOLD/CHECKPOINT | — | SPECIAL_PAGE_SPEC_MISSING |

## HARD GATES

1. `TARGET_MISSING` → FAIL.
2. REGULAR cell 1–6 bukan EXACT-2 → FAIL.
3. REGULAR cell 7–24 bukan EXACT-3 → FAIL.
4. REGULAR cell 1–6 mengandung non-TARGET → FAIL.
5. REGULAR cell 7–24 tidak mengandung minimal satu TARGET → FAIL.
6. Unsur di luar TARGET + REVIEW_ALLOWED → `FUTURE_COMPETENCY_FAIL`.
7. Kelompok 1 huruf di mana pun → `SINGLE_LETTER_GROUP_FAIL`.
8. Duplikasi kelompok → `DUPLICATE_GROUP_FAIL`.
9. Page berstatus HOLD → `SPECIAL_PAGE_SPEC_MISSING`; PDF P001–P040 tidak boleh dinyatakan FINAL.
10. Semua output tetap harus lolos `DETACHED-LETTER` dan `HA-GLYPH`.

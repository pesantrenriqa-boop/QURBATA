# QPS-001 — QURBATA Page Production Standard

**Status:** ACTIVE  
**Scope:** Semua halaman latihan Jilid 1–8.

## Struktur Dasar

- 1 halaman = 24 kotak contoh.
- 1 pertemuan = 1/2 atau 1 halaman.
- Halaman khusus/evaluasi boleh memakai struktur berbeda, tetapi wajib diberi `PAGE_TYPE`.

## Komposisi Baku

| Jenis kotak | Target awal |
|---|---:|
| NEW | 10 |
| REVIEW_IMMEDIATE | 7 |
| REVIEW_SPACED | 5 |
| REVIEW_GLOBAL | 2 |
| Total | 24 |

Komposisi dapat berubah maksimal ±2 kotak bila alasan pedagogis dicatat. Halaman tidak boleh 100% materi baru.

## Metadata Wajib Halaman

- `PAGE_ID`
- `VOLUME`
- `PAGE_NO`
- `PAGE_TYPE`
- `PRIMARY_COMPETENCY`
- `NEW_UNIT_IDS`
- `REVIEW_UNIT_IDS`
- `PREREQUISITES`
- `WHITELIST_FEATURES`
- `FORBIDDEN_FEATURES`
- `IQRO_PEDAGOGY_REFERENCE`
- `SOURCE_STATUS`
- `VALIDATION_STATUS`

## Metadata Wajib Kotak

- `BOX_ID`
- `EXAMPLE_ID`
- `TEXT_AR`
- `CONTENT_TYPE`
- `UNIT_ID`
- `REVIEW_TYPE`
- `SOURCE_TYPE`
- `SOURCE_REF`
- `DIFFICULTY`
- `ERROR_TARGET`
- `STATUS`

## Validator

Satu halaman lulus bila:

1. tepat 24 kotak;
2. minimal 3 kelas review hadir: immediate, spaced, global;
3. semua unsur teks berada pada whitelist;
4. tidak ada forbidden feature;
5. materi awal jilid tetap muncul melalui review;
6. materi pertengahan/akhir sebelumnya tetap terwakili;
7. tidak ada satu keluarga visual mendominasi berlebihan;
8. panjang contoh seimbang;
9. sumber teks dapat dilacak;
10. duplikasi hanya boleh bertujuan review.

## Review Debt

Setiap unit yang tidak muncul melebihi jarak review yang ditetapkan memperoleh `REVIEW_DEBT`. Unit dengan debt tertinggi diprioritaskan pada halaman berikutnya selama tidak melanggar progression.

## Hubungan Iqro'

Pola pengulangan awal–tengah–akhir, kenaikan bertahap, dan latihan kumulatif Iqro' dipakai sebagai rujukan pedagogis. Susunan 24 kotak, kode kompetensi, distribusi review, dan pemilihan akhir merupakan rancangan QURBATA.

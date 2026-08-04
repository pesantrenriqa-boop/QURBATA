# QURBATA Jilid 3 — Production Workboard

**Status:** ACTIVE  
**Branch:** `content/qurbata-jilid-1-8-production`

## Tujuan Jilid 3

Jilid 3 menjadi tahap penguasaan sukun per huruf target dan integrasi bertahap menuju kata serta frasa yang lebih alami. Materi tasydid dan hukum tajwid lanjut belum menjadi materi aktif kecuali sudah masuk whitelist resmi.

## Status Per Halaman

| Halaman | Sumber | Status recovery | Status audit | Status produksi |
|---|---|---|---|---|
| P001 | batch P001–P010 | FOUND | OPEN | NOT-READY |
| P002 | batch P001–P010 | FOUND | OPEN | NOT-READY |
| P003 | batch P001–P010 | FOUND | OPEN | NOT-READY |
| P004 | batch P001–P010 | FOUND | OPEN | NOT-READY |
| P005 | batch P001–P010 | FOUND | OPEN | NOT-READY |
| P006 | batch awal + versi lanjutan | CONFLICT | OPEN | NOT-READY |
| P007 | batch awal + versi lanjutan | CONFLICT | OPEN | NOT-READY |
| P008 | batch awal + versi lanjutan | CONFLICT | OPEN | NOT-READY |
| P009 | batch awal + versi lanjutan | CONFLICT | OPEN | NOT-READY |
| P010 | batch awal + versi lanjutan | CONFLICT | OPEN | NOT-READY |
| P011–P020 | batch P011–P020 | FOUND | OPEN | NOT-READY |
| P021–P030 | batch P021–P030 | FOUND | OPEN | NOT-READY |
| P031–P040 | batch P031–P040 | FOUND | OPEN | NOT-READY |

## Format Audit Setiap Halaman

Setiap halaman harus dicatat dengan struktur:

```text
PAGE_ID
COMPETENCY_ID
UNIT_ID
NEW_MATERIAL
REVIEW_SCOPE
TARGET_LETTERS
ALLOWED_PATTERNS
FORBIDDEN_PATTERNS
SPECIAL_PAGE_TYPE
BOX_01 ... BOX_24
SOURCE_IDS
DUPLICATION_CHECK
ACADEMIC_STATUS
```

## Whitelist Awal Jilid 3

- huruf dan harakat yang telah lulus Jilid 1–2;
- kata tiga sampai lima huruf sesuai tangga;
- mad fathah + alif;
- mad ya sukun;
- mad dhammah + wawu sukun;
- tanwin yang telah dikenalkan;
- sukun pada huruf target secara bertahap;
- frasa dua sampai tiga kata yang seluruh unsurnya telah dipelajari.

## Hold List

Contoh masuk `HOLD` apabila memuat:

- tasydid sebelum waktunya;
- hukum tajwid lanjut;
- bentuk kata yang melampaui tangga;
- terlalu banyak materi baru sekaligus;
- frasa ayat yang dipaksakan;
- sumber yang belum diverifikasi;
- pengulangan tanpa fungsi murojaah.

## Sprint Aktif

### Sprint QJ3-S01 — P001–P010

1. Pulihkan isi kotak P001–P005.
2. Bandingkan dua versi P006–P010.
3. Tetapkan sukun target per halaman.
4. Susun 24 kotak per halaman.
5. Tandai NEW dan REVIEW.
6. Jalankan pemeriksaan duplikasi internal Jilid 3 dan lintas Jilid 1–2.
7. Hubungkan ke kode kompetensi dan Unit Kompetensi.
8. Tetapkan status `CONTENT-READY` hanya setelah audit.

### Sprint QJ3-S02 — P011–P020

Dilaksanakan setelah QJ3-S01 lulus audit.

### Sprint QJ3-S03 — P021–P030

Dilaksanakan setelah QJ3-S02 lulus audit.

### Sprint QJ3-S04 — P031–P040

Dilaksanakan setelah QJ3-S03 lulus audit dan fungsi halaman 40 ditetapkan.

## Definition of Done Jilid 3

- 40 halaman tersedia;
- setiap halaman latihan memiliki 24 kotak;
- seluruh kotak berkode;
- seluruh halaman terhubung ke kompetensi dan Unit Kompetensi;
- tidak ada tasydid/tajwid lanjut yang lolos tanpa whitelist;
- halaman 20 dan 40 berfungsi sebagai halaman khusus;
- seluruh contoh memiliki status sumber;
- duplikasi terkontrol;
- jumlah contoh, kata, frasa, dan sumber dapat dihitung otomatis.

# QURBATA JILID 1 — ROLLING COVERAGE AUDIT P001–P013

Status: **AUDIT v0.1 — PRE-KASRAH GATE**

## Basis
Audit memakai master curated P001–P009 v0.3, checkpoint P010, dan P011–P013 v0.3 setelah MSL audit. Aturan lama tidak diubah.

## Gate utama
1. Kompetensi yang sudah diperkenalkan tidak boleh hilang terus-menerus dari review.
2. Setelah P002, `أَ` dan `ءَ` dihitung terpisah.
3. Pada P005–P009 keduanya wajib tetap masuk rotation.
4. P010 harus menguji seluruh 22 kompetensi P001–P009 secara seimbang.
5. P011–P013 harus tetap membawa review lama sambil mendominankan target baru.
6. Tidak ada future competency.
7. MSL tidak boleh menyebabkan target gate atau rolling coverage rusak.

## Audit khusus أَ / ءَ
| Page | أَ | ءَ | Result |
|---|---|---|---|
| P002 | hadir | hadir | PASS |
| P003 | hadir | hadir | PASS |
| P004 | hadir | hadir | PASS |
| P005 | hadir | hadir | PASS |
| P006 | hadir | hadir | PASS |
| P007 | hadir | hadir | PASS |
| P008 | hadir | hadir | PASS |
| P009 | hadir | hadir | PASS |
| P010 | 3× | 3× | PASS |
| P011 | hadir | hadir | PASS |
| P012 | hadir | hadir | PASS |
| P013 | أَ hadir | ءَ tidak muncul | WINDOW PASS |

Catatan P013: `ءَ` tidak muncul pada halaman ini, tetapi muncul pada P012 dan sebelumnya; ini tidak melanggar rolling-window rule. Pada fase berikutnya ia mendapat coverage debt dan harus diprioritaskan pada review legal awal Kasrah/Fathah campuran sesuai register.

## Family rolling audit
- P001 `ب ت ث`: terus muncul lintas P002–P013; PASS.
- P002 `ء أ`: sangat kuat P002–P012; P013 hanya أ; rolling PASS, debt untuk ء.
- P003 `ج ح خ`: muncul berulang sampai P013; PASS.
- P004 `د ذ ر ز`: muncul berulang sampai P013; PASS.
- P005 `س ش`: muncul berulang sampai P013; PASS.
- P006 `ص ض`: muncul berulang sampai P013; PASS.
- P007 `ط ظ`: muncul berulang sampai P013; PASS.
- P008 `ع غ`: muncul berulang sampai P013; PASS.
- P009 `ف ق`: muncul berulang sampai P013; PASS.
- P011 `ك ل`: muncul lagi P012 dan P013; PASS.
- P012 `م ن`: muncul P013; PASS.
- P013 `ه و ي`: target baru; baseline established.

## P010 checkpoint
P010 tetap menjadi anchor pemerataan: 22 kompetensi P001–P009 × tepat 3 kemunculan = 66 unit. Data checkpoint tidak diubah oleh MSL.

## Coverage debt entering P014
Prioritas review saat memasuki P014:
1. `ءَ` — debt tertinggi karena absen P013.
2. Huruf lama dengan frekuensi lebih rendah pada P011–P013 diprioritaskan setelah target Kasrah terpenuhi.
3. `أَ` tidak boleh dianggap mewakili `ءَ`.
4. Fathah review tidak boleh menggeser fokus target Kasrah P014.

## Meaningful Sequence impact
- P011 MSL target gate PASS.
- P012 sempat FAIL karena `عَبَدَ` tidak mengandung م/ن; sudah diperbaiki menjadi fonetik `مَ بَ دَ`.
- P013 MSL target gate PASS.
- Valid global USED meaningful words = 15, duplicate = 0.

## PRE-KASRAH DECISION
**P001–P013 = ROLLING COVERAGE PASS untuk melanjutkan penyusunan P014, dengan explicit coverage debt `ءَ` pada awal fase berikutnya.**

PASS ini hanya untuk data/kurikulum. Belum merupakan visual/render/PDF PASS.

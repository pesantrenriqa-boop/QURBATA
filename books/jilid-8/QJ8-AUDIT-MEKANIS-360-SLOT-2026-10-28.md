# QJ8 — Audit Mekanis 360 Kotak (28 Oktober 2026)

**Metode:** membaca langsung enam file prototipe pada branch default GitHub, mengekstrak tabel slot dan menghitung ID, teks Arab, referensi, serta duplikasi identik. Ini **bukan verifikasi mushaf atau tashih tajwid**.

## Hasil terukur
| Indikator | Hasil |
|---|---:|
| Baris slot terbaca | 360 |
| Slot-ID unik | 360 |
| ID ganda | 0 |
| Halaman terwakili | 40 |
| Halaman dengan jumlah slot ≠9 | 0 |
| Teks Arab unik (string persis) | 196 |
| Kotak mengulang teks yang identik | 164 |
| Jenis referensi tertulis unik | 34 |
| Referensi rentang/gabungan (perlu pemeriksaan) | 13 |
| Kotak diverifikasi mushaf | 0 |

## Duplikasi teks terbanyak (string identik)
| Teks | Kemunculan |
|---|---:|
| مَجْر۪ىٰهَا | 13 |
| عِوَجًا ۜ قَيِّمًا | 12 |
| ءَا۬عْجَمِيٌّ | 11 |
| لَا تَأْمَنَّا | 11 |
| مَنْ ۜ رَاقٍ | 10 |
| قَوَارِيرَا | 10 |
| مَرْقَدِنَا ۜ هَٰذَا | 9 |
| بَلْ ۜ رَانَ | 9 |
| ءَآلذَّكَرَيْنِ | 9 |
| ءَآلْـَٰٔنَ | 9 |
| سَلَٰسِلَا | 9 |
| عَادًا ٱلْأُولَىٰ | 8 |
| لَّٰكِنَّا | 8 |
| قَوَارِيرَ | 7 |
| ءَآللَّهُ | 7 |
| وَيَبْصُطُ | 5 |
| بِمُصَيْطِرٍ | 5 |
| الٓمٓ | 4 |

## Pemeriksaan spesifik
- QS 76:16: lafaz قَوَارِيرَ muncul **7** kali sebagai teks kotak, tetapi jumlah ini **bukan** jaminan seluruh rujukan benar.
- Lafaz قَوَارِيرَا muncul **10** kali; sebagian untuk QS 76:15.
- Referensi rentang atau gabungan harus dinormalisasi menjadi referensi ayat eksplisit untuk setiap kotak; tidak semua rentang berarti kesalahan (misalnya saktah 18:1–2).
- Pemeriksaan ini tidak bisa mengesahkan rasm, harakat, urutan lafaz dalam ayat, atau jalur Hafsh tanpa mushaf rujukan.

## Gate berikutnya
1. Tetapkan Source-ID mushaf Utsmani dan versi teks yang digunakan.
2. Bandingkan 360 transkripsi dengan ayat resmi menggunakan normalisasi Unicode yang **tidak menghilangkan** tanda bacaan penting.
3. Kelompokkan sasaran gharib, konteks, pengulangan, evaluasi; jangan menyebut 360 contoh gharib unik.
4. Pastikan keputusan akademik untuk konflik halaman P018/P028/P036/P038.
5. Isi reviewer dan Evidence-ID, kemudian baru ubah status cetak.

## Slot dengan rujukan rentang/gabungan
- P001-K07: 18:1–2 — عِوَجًا ۜ قَيِّمًا
- P005-K01: 18:1–2 — عِوَجًا ۜ قَيِّمًا
- P005-K05: 18:1–2 — عِوَجًا ۜ قَيِّمًا
- P005-K09: 18:1–2 — عِوَجًا ۜ قَيِّمًا
- P010-K01: 18:1–2 — عِوَجًا ۜ قَيِّمًا
- P023-K09: 10:51 / 10:91 — ءَآلْـَٰٔنَ
- P029-K01: 18:1–2 — عِوَجًا ۜ قَيِّمًا
- P031-K01: 18:1–2 — عِوَجًا ۜ قَيِّمًا
- P031-K05: 18:1–2 — عِوَجًا ۜ قَيِّمًا
- P031-K09: 18:1–2 — عِوَجًا ۜ قَيِّمًا
- P037-K04: 18:1–2 — عِوَجًا ۜ قَيِّمًا
- P037-K08: 18:1–2 — عِوَجًا ۜ قَيِّمًا
- P039-K01: 18:1–2 — عِوَجًا ۜ قَيِّمًا

# QJ3 P001–P010 — Audit V1

**Batch:** QJ3-BATCH-001-010  
**Status:** AUDITED-WITH-CORRECTIONS  
**Branch:** `content/qurbata-jilid-1-8-production`

## Hasil audit utama

1. Struktur 10 halaman × 24 kotak valid.
2. Semua halaman memiliki materi baru dan pengulangan.
3. Urutan mad alif → ya → wawu → campuran selaras dengan progression QURBATA.
4. P007–P008 sudah mengarah pada sukun per huruf target, bukan hukum tajwid.
5. Tidak ada tasydid pada materi cetak utama.
6. Beberapa item perlu klasifikasi sumber agar tidak dianggap semuanya berasal dari Al-Qur’an.
7. Ditemukan satu duplikasi dalam halaman yang sama pada P009: `يَسْمَعُ` muncul sebagai NEW dan REVIEW_IMMEDIATE.
8. Beberapa bentuk seperti `بَتَثَ`, `جَحَخَ`, `بَا`, `بِي`, `بُو`, `عَبْ`, dan `غَفْ` adalah latihan terkendali, bukan kata leksikal atau klaim teks Qur’ani.

## Klasifikasi sumber wajib

Setiap kotak kanonik wajib memakai salah satu nilai berikut:

- `QURAN_VERIFIED`: teks ditemukan dan diverifikasi langsung dari mushaf.
- `ARABIC_LEXICON`: kata Arab yang sah, tetapi tidak diklaim sebagai kutipan Qur’ani.
- `CONTROLLED_DRILL`: bentuk latihan buatan untuk kontras huruf, harakat, mad, atau sukun.
- `RECOVERY_SOURCE`: contoh hasil recovery yang masih menunggu klasifikasi akhir.

## Koreksi wajib sebelum kanonisasi

| Lokasi | Temuan | Keputusan |
|---|---|---|
| P009 K11 | `يَسْمَعُ` duplikat dalam halaman yang sama | Ganti dengan `يَفْتَحُ` sebagai review sukun ringan |
| P001 K18 | `بَتَثَ` bukan kata leksikal | Pertahankan sebagai `CONTROLLED_DRILL` |
| P002 K23 | `بَتَثَ` bukan kata leksikal | Pertahankan sebagai `CONTROLLED_DRILL` |
| P002 K24 | `جَحَخَ` bukan kata leksikal | Pertahankan sebagai `CONTROLLED_DRILL` |
| P003 K23–K24 | `بَا`, `تَا` | Tandai `CONTROLLED_DRILL` |
| P004 K23–K24 | `بِي`, `تِي` | Tandai `CONTROLLED_DRILL` |
| P005 K23–K24 | `بُو`, `تُو` | Tandai `CONTROLLED_DRILL` |
| P006 K23–K24 | rangkaian tiga mad | Tandai `CONTROLLED_DRILL` |
| P007 K23 | `أَبْ` | Pertahankan sebagai latihan sukun; bukan klaim ayat |
| P008 K23–K24 | `عَبْ`, `غَفْ` | Pertahankan sebagai `CONTROLLED_DRILL`; jangan diberi arti leksikal |
| P009 K23–K24 | pola `يَفْعَلُ`, `يَفْعِلُ` | Tandai `CONTROLLED_PATTERN`, bukan pembelajaran sharaf |

## Audit tingkat kesulitan

- P001–P002: sesuai sebagai jembatan dari Jilid 2.
- P003: sesuai untuk mad fathah + alif.
- P004: kata seperti `كَبِيرٌ`, `عَلِيمٌ`, `حَكِيمٌ`, `بَصِيرٌ`, `سَمِيعٌ`, `كَرِيمٌ` dapat dipakai, tetapi status tanwin harus selaras dengan prasyarat Jilid 2.
- P005: kata `يَقُولُ`, `يَكُونُ`, `وُجُوهٌ` lebih kompleks; tetap dipakai sebagai bagian akhir halaman setelah contoh pendek.
- P006: `مِيثَاقٌ` merupakan item paling berat; tetap ditempatkan sebagai item tingkat akhir halaman.
- P007–P008: bentuk mudhari’ berawalan `يـ` sah sebagai latihan panjang kata dan sukun, tanpa penjelasan sharaf.
- P009–P010: berfungsi sebagai integrasi, bukan pengenalan unsur baru besar.

## Audit review

Komposisi batch:

- materi baru/integrasi: 96/240 = 40%
- review langsung: 71/240 ≈ 29,6%
- review berjarak: 53/240 ≈ 22,1%
- review global: 20/240 ≈ 8,3%

Komposisi ini dinyatakan sesuai dengan standar target 40% baru dan 60% murojaah. Review hadir dari halaman awal sampai akhir blok.

## Gate tersisa

- verifikasi mushaf untuk semua item yang akan diberi status `QURAN_VERIFIED`;
- audit otomatis/semimanual terhadap seluruh kotak Jilid 1–2 untuk duplikasi lintas jilid;
- migrasi isi yang sudah dikoreksi ke `books/jilid-3/pages/QJ3-P001.md` sampai `QJ3-P010.md`;
- review akhir pemilik akademik sebelum `APPROVED`.

## Keputusan

Batch dapat lanjut ke tahap `CANONICAL-CANDIDATE` setelah koreksi P009 K11 dan penambahan klasifikasi sumber pada seluruh kotak.

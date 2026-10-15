# Patch rasio token J1 P011–P018 v0.1

Status: PROPOSAL REVISI TERKENDALI, belum diterapkan ke pilot, bukan FROZEN. Setiap substitusi mengganti satu token pada sel grid yang disebutkan, tidak mengubah jumlah baris atau kelompok. Hitung ulang setelah diterapkan.

## P011–P013: target 38/64 token baru (59,375%)

| Halaman | Sel grid | Token lama | Token pengganti | Alasan |
|---|---|---|---|---|
| P011 | B6 K1, token 1 | كَ | بَ | review P001 |
| P011 | B6 K2, token 1 | لَ | تَ | review P001 |
| P012 | B6 K1, token 1 | مَ | بَ | review P001 |
| P012 | B6 K2, token 1 | نَ | تَ | review P001 |
| P013 | B6 K1, token 1 | هَ | بَ | review P001 |
| P013 | B6 K2, token 1 | وَ | تَ | review P001 |

## P014–P018: target 40/66 token baru (60,61%)

| Halaman | Sel grid | Token lama | Token pengganti |
|---|---|---|---|
| P014 | B6 K1, token 1 | ءَ | بِ |
| P014 | B6 K2, token 1 | أَ | تِ |
| P014 | B6 K3, token 1 | خَ | ثِ |
| P014 | B7 K1, token 1 | رَ | جِ |
| P015 | B7 K1, token 1 | ءَ | حِ |
| P015 | B7 K2, token 1 | حَ | خِ |
| P015 | B7 K3, token 1 | أَ | دِ |
| P015 | B8 K1, token 1 | سَ | ذِ |
| P016 | B7 K1, token 2 | تَ | رِ |
| P016 | B7 K2, token 2 | أَ | زِ |
| P016 | B7 K3, token 2 | خَ | سِ |
| P016 | B8 K1, token 1 | جَ | شِ |
| P017 | B7 K2, token 3 | ثَ | صِ |
| P017 | B7 K3, token 1 | أَ | ضِ |
| P017 | B8 K1, token 1 | سِ | طِ |
| P017 | B8 K2, token 1 | تَ | ظِ |
| P018 | B7 K1, token 1 | وَ | عِ |
| P018 | B7 K2, token 1 | تِ | غِ |
| P018 | B7 K3, token 1 | أَ | فِ |
| P018 | B8 K1, token 1 | ذِ | قِ |

## QA wajib
- Cek setiap posisi dan token terhadap pilot sumber sebelum penerapan; jangan mengganti jika posisi telah berubah.
- Verifikasi keseimbangan sebaran huruf baru dan lama, bukan hanya persentase.
- Pastikan bentuk lepas, tidak ada kompetensi prematur dan penanaman dua baris tetap sesuai.
- Panel Bi'ah/Akhlak memakai FROZEN integrasi v1.3 dan Tahfidz memakai baseline distribusi FROZEN.
- Uji visual KFGQPC Uthman Taha, ha dua lubang, RTL A5, dan cetak.

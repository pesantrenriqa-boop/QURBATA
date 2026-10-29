# QJ8 — Spesifikasi Slot Kontekstual (Ayat Sebelum–Target–Sesudah)
Tanggal: 29 Oktober 2026. Status: **USULAN DESAIN / HOLD**, belum mengganti master maupun register lama.

## Ketentuan utama
**Satu slot latihan tidak boleh hanya berupa satu kata atau satu baris target.** Setiap slot sasaran harus menampilkan:
1. **Ayat sebelum** lokasi Gharib, lengkap bila tersedia (ayat n−1).
2. **Ayat target**, lengkap dengan nomor ayat dan penandaan visual pada lafaz Gharib.
3. **Ayat sesudah**, lengkap bila tersedia (ayat n+1).
4. Label kompetensi, surah/ayat, posisi target, serta instruksi guru untuk wasal, waqaf, dan ibtida.
5. **Kasus lintas batas ayat:** ayat target meliputi kedua ayat yang disambung (mis. Al-Kahfi 18:1–2); konteks luar meliputi ayat sebelum yang tersedia dan ayat setelah pasangan target. Jika target pada ayat pertama surah, jangan mengarang ayat 0 atau menyambungkan surah sebelumnya sebagai konteks otomatis.
6. Bila ayat sangat panjang, desain menggunakan **panel yang dapat berkembang** atau halaman lanjutan; jangan menghilangkan teks tanpa label 'kutipan parsial'. Untuk format A5, tidak perlu memaksa sembilan slot per halaman.
7. **Penanda warna tidak mengubah karakter rasm, harakat, atau tanda baca mushaf**; gunakan highlight/garis bawah visual yang terpisah dari teks.
8. Seluruh ayat sebelum/target/sesudah harus ditarik dari **satu edisi mushaf Hafs yang ditetapkan**, disertai Source-ID, Evidence-ID, nomor ayat, reviewer, dan status tashih. Dilarang merekonstruksi ayat penuh dari fragmen lama.

## Skema data baru (tanpa memodifikasi sumber lama)
| Field | Makna |
|---|---|
| Case-ID | Identitas satu kejadian Gharib autentik |
| Competency-ID | Satu kompetensi per halaman latihan |
| Surah, Target-Ayah-Start, Target-Ayah-End | Lokasi sasaran; mendukung lintas ayat |
| Before-Ayah-Ref / Before-Ayah-Text | Ayat sebelumnya (atau N/A di awal surah) |
| Target-Ayah-Ref / Target-Ayah-Text | Ayat target lengkap; bisa dua ayat bila lintas batas |
| After-Ayah-Ref / After-Ayah-Text | Ayat setelahnya |
| Target-Span | Posisi lafaz target dalam teks asli, tanpa mengubah rasm |
| Source-ID / Evidence-ID / Hafs-Route | Provenans dan jalur bacaan |
| Reading-Instruction | Talaqqi, wasal, waqaf, ibtida |
| Reviewer / QA-Status | Validasi ilmiah; default BELUM TASHIH |

## Pemetaan awal empat kasus Saktah
| Case-ID | Sebelum | Ayat target lengkap | Sesudah | Catatan |
|---|---|---|---|---|
| GH-SAK-01 | N/A (awal surah) | Al-Kahfi 18:1–2 | 18:3 | saktah pada batas 18:1–2 |
| GH-SAK-02 | Yasin 36:51 | Yasin 36:52 | 36:53 | saktah dalam 36:52 |
| GH-SAK-03 | Al-Qiyamah 75:26 | Al-Qiyamah 75:27 | 75:28 | saktah dalam 75:27 |
| GH-SAK-04 | Al-Muthaffifin 83:13 | Al-Muthaffifin 83:14 | 83:15 | saktah dalam 83:14 |

**Penting:** tabel ini baru pemetaan referensi. Teks Arab ayat lengkap **belum diimpor/ditashih**. Tidak ada klaim bahwa 4 slot baru telah terisi sesuai standar konteks.

## Tata letak A5 yang disarankan
- Judul: **Kompetensi Saktah** dan tujuan.
- **Satu kasus per panel besar**, dengan baris terpisah 'Sebelum', 'Target', 'Sesudah' yang tetap mempertahankan nomor ayat.
- Penanda visual target, teori Indonesia 1–2 kalimat, instruksi talaqqi.
- Empat kasus Saktah dapat tersebar pada 2–4 halaman fisik agar teks Utsmani cukup besar; **satu kompetensi dapat memiliki beberapa halaman fisik** tanpa berubah menjadi kompetensi baru.
- Jika satu kasus berisi ayat panjang, berikan halaman tambahan daripada memperkecil teks sampai tidak terbaca.

## Gate sebelum PDF baru
1. Periksa kesesuaian rujukan n−1, n, n+1 serta kasus lintas ayat.
2. Tarik ayat lengkap dari sumber mushaf otoritatif; cocokkan rasm dan tanda Gharib karakter demi karakter.
3. Tandai target tanpa mengubah teks sumber.
4. Tashih guru ahli dan catat Evidence-ID.
5. Rekonsiliasi dengan master J8 dan Decision-ID.
6. Hanya setelahnya buat PDF revisi; register lama 360 fragmen tetap arsip HOLD.

## Koreksi prinsip
**Satu halaman = satu kompetensi pedagogis** tidak sama dengan **satu halaman cetak = sembilan slot**. Jika ayat sebelum–target–sesudah lengkap, keterbacaan dan ketepatan bacaan didahulukan.

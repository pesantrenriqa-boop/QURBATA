# QURBATA Jilid 2 — Recovery Terintegrasi P021–P040

**Kode:** QJ2-REC-P021-P040  
**Status:** RECOVERED-SOURCE-REGISTERED / STAGED-BLOCKED  
**Tanggal recovery:** 1 Agustus 2026  
**Sumber baseline:** commit `67a42c40d796cbdcead4e98f5d03da370ac22406`  
**Jalur sumber lama:** `books/jilid-2/regenerated/`  
**Master:** `books/jilid-2/QJ2-MASTER-Struktur-40-Halaman.md`

Dokumen ini mengunci keberadaan dan klasifikasi sumber P021–P040. Status `STAGED-BLOCKED` dipertahankan. Dokumen ini bukan otorisasi cetak dan tidak menggantikan gate ahli, audit ortografi, render, audio, asesmen, safeguarding, Evidence-ID, dan Decision-ID.

## Register Halaman

| Halaman | Fokus Recovery | Status | Audit/Blocker |
|---|---|---|---|
| QJ2-P021 | Fathatain | STAGED-BLOCKED | AUD-QJ2-TAN-003; BLK-QJ2-ORTHO-001 |
| QJ2-P022 | Kasratain | STAGED-BLOCKED | AUD-QJ2-TAN-003; BLK-QJ2-ORTHO-001 |
| QJ2-P023 | Dhammatain | STAGED-BLOCKED | AUD-QJ2-TAN-003; BLK-QJ2-ORTHO-001 |
| QJ2-P024 | Integrasi tiga tanwin | STAGED-BLOCKED | AUD-QJ2-TAN-003; BLK-QJ2-ORTHO-001 |
| QJ2-P025 | Orientasi pendek–panjang | STAGED-BLOCKED | Objek khusus; materi dengar/tunjuk/tirukan |
| QJ2-P026 | Fathah pendek vs fathah + alif | STAGED-BLOCKED | AUD-QJ2-MAD-001 |
| QJ2-P027 | Alif mad pada tiga huruf | STAGED-BLOCKED | AUD-QJ2-MAD-001 |
| QJ2-P028 | Alif mad empat huruf dan pemutus | STAGED-BLOCKED | Objek khusus/transfer |
| QJ2-P029 | Transfer alif mad ke kata bermakna/Qurani | STAGED-BLOCKED | AUD-QJ2-MAD-001; Source-ID wajib |
| QJ2-P030 | Evaluasi alif mad dan kontras pendek | STAGED-BLOCKED | AUD-QJ2-MAD-001 |
| QJ2-P031 | Kasrah pendek vs kasrah + ya mad | STAGED-BLOCKED | AUD-QJ2-FINAL-001 |
| QJ2-P032 | Ya mad pada tiga huruf | STAGED-BLOCKED | AUD-QJ2-FINAL-001 |
| QJ2-P033 | Ya mad empat huruf dan transfer | STAGED-BLOCKED | AUD-QJ2-FINAL-001 |
| QJ2-P034 | Ya mad vs ya konsonan; murojaah alif | STAGED-BLOCKED | AUD-QJ2-FINAL-001 |
| QJ2-P035 | Dhammah pendek vs dhammah + waw mad | STAGED-BLOCKED | AUD-QJ2-FINAL-001 |
| QJ2-P036 | Waw mad pada tiga huruf | STAGED-BLOCKED | AUD-QJ2-FINAL-001 |
| QJ2-P037 | Waw mad empat huruf dan transfer | STAGED-BLOCKED | AUD-QJ2-FINAL-001 |
| QJ2-P038 | Waw mad vs waw konsonan; murojaah alif/ya | STAGED-BLOCKED | AUD-QJ2-FINAL-001 |
| QJ2-P039 | Integrasi tiga mad dan kontras pendek–panjang | STAGED-BLOCKED | AUD-QJ2-FINAL-001 |
| QJ2-P040 | Evaluasi akhir + Checkpoint Nama Huruf IV | STAGED-BLOCKED | AUD-QJ2-FINAL-001; panel lisan terpisah |

## Bukti Isi yang Ditemukan

Salah satu sumber staging nyata adalah QJ2-P031 pada commit `d82cbc440b49d91ad692e0ecff47420a934cc4b4`, dengan jalur:

`books/jilid-2/regenerated/QJ2-P031-Pendek-Panjang.md`

Contoh di dalamnya antara lain:

- `قَالَ`
- `قِيلَ`
- `نُورُ`
- `أَحَدٌ`
- `رَجُلٍ`
- `عَمَلًا`
- `بَاعَ`
- `فِيهِ`
- `كِتَابَ`
- `كَبِيرِ`
- `رَسُولُ`
- `شَجَرَةٌ`
- `بَقَرَةٍ`
- `حَسَنَةً`
- `عَذَابَ`
- `رَحِيمِ`
- `يَقُولُ`
- `صَدَقَةٌ`
- `حِسَابَ`
- `عَلِيمِ`
- `قُلُوبُ`
- `نَفَقَةٍ`
- `مَكَانَ`
- `سُجُودُ`

Contoh tersebut dibekukan sebagai data recovery, bukan sebagai materi final siap cetak.

## Aturan Integrasi

1. Isi sumber lama tetap berada di `books/jilid-2/regenerated/` sampai salinan recovery per halaman selesai dibuat.
2. Setiap file recovery berikutnya harus mencatat path dan commit asal.
3. Status `STAGED-BLOCKED` tidak boleh diubah hanya karena isi telah ditemukan.
4. Tanwin, mad, kata bermakna, kandidat Qurani, evaluasi, dan panel nama huruf harus tetap dipisahkan menurut fungsi.
5. Klaim kata atau frasa Qurani wajib mempunyai Source-ID dan verifikasi teks.
6. Tidak boleh membuat contoh baru untuk menggantikan isi staging yang belum diekstrak.

## Status

- Sumber P021–P040: **FOUND 20/20**.
- Register recovery terintegrasi: **COMPLETE 20/20**.
- Salinan isi penuh per halaman ke folder recovery resmi: **NEXT STEP**.
- Kesiapan cetak: **BLOCKED**.

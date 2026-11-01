# Protokol audit 114 surah — QURBATA Jilid 8

Sumber: QJ8-TRACKER-AUDIT-114-SURAH-2026-11-01.csv. **Semua baris adalah status awal administratif, bukan bukti penyisiran mushaf selesai.**

## Definisi status

- `NOT_REVIEWED`: belum ada entri di register untuk surah ini; **bukan** berarti nihil kasus Gharib.
- `INDEXED_NOT_VERIFIED`: sudah ada satu atau lebih indeks kasus; belum tentu seluruh ayat surah telah disisir.
- `REVIEWED_WITH_CASES`: hanya setelah seluruh ayat surah ditelusuri dan daftar kasus diverifikasi terhadap rujukan qiraat.
- `REVIEWED_NO_CASE`: hanya setelah penyisiran penuh dengan catatan sumber dan penanggung jawab; bukan nilai default.

## Catatan minimum sebelum mengubah status

Surah, rentang ayat yang diperiksa, identitas mushaf dan versi, sumber qiraat Hafs dan thariq, daftar ID kasus, kemungkinan overlap, pemeriksa, tanggal, dan keputusan. Jangan mencantumkan ayat buatan atau mengubah rasm.

## Aturan integritas

- Tidak boleh memaksa sembilan contoh per halaman.
- GH-012 adalah kelompok referensi, bukan satu kejadian.
- GH-021/GH-027/GH-029 harus diputuskan overlap sebelum jumlah kasus final.
- Empat saktah kanonik tetap empat; hā’ sakt tidak otomatis dihitung sebagai saktah.
- Semua kandidat HOLD sampai pemeriksaan ahli. Master lama 360 slot tetap utuh.

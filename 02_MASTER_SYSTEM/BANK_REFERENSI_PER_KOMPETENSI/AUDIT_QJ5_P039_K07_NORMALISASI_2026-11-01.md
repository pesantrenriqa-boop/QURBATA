# QJ5 P039/K07 — normalisasi lintas delapan register (2026-11-01)

Status: **NORMALIZED_PHRASE_NOT_FOUND / SHARED_WORD_FOUND / TASHIH_PENDING**.

## Metode
Membaca ulang seluruh delapan file `02_MASTER_SYSTEM/BANK_REFERENSI_PER_KOMPETENSI/REGISTER_24_KELOMPOK_JILID_{1..8}.md` pada branch `audit/j4-tashih-20261024`. Untuk pencarian, Unicode dinormalisasi NFKD, harakat Arab dan tanda Qurani rentang U+064B–065F, U+0670, U+06D6–06ED dibuang, tatwil dibuang, variasi alif diseragamkan, dan varian ya diseragamkan. Ini heuristik pencarian, bukan normalisasi rasm untuk pencetakan.

## Temuan
- Potongan lengkap target QS 39:69 `وَجِا۟ىٓءَ بِٱلنَّبِيِّـۧنَ وَٱلشُّهَدَآءِ` tidak ditemukan sebagai frasa lengkap dalam delapan register yang dibaca.
- Kata terkait `وَجِيءَ` muncul **empat kali** di register Jilid 5, masing-masing dalam potongan `وَجِيءَ يَوْمَئِذٍ بِجَهَنَّمَ` (QS Al-Fajr 89:23).
- Tidak ada temuan pada Jilid 1–4 dan 6–8 untuk pola kata dan frasa yang diuji.
- Dengan demikian, kandidat **tidak baru secara unsur kata**, tetapi berbeda sebagai konteks ayat dan potongan. Ini bukan alasan otomatis menggugurkan, namun perlu mempertimbangkan keragaman latihan.
- Klasifikasi mad wajib muttasil pada `وَجِا۟ىٓءَ` dan `ٱلشُّهَدَآءِ` tetap memerlukan tashih sumber dan guru.

## Keputusan
Jangan klaim bebas duplikasi total. K07 tetap kandidat penelitian dan register aktif QS 51:7 tetap tidak diubah. Nilai Sah P039 tetap 0/8. Audit berikutnya: cek rasm Utsmani dan potongan yang layak waqaf/ibtida, lalu persetujuan sebelum perubahan.

# QURBATA Jilid 1 — Audit cakupan evaluasi P010 dan P020

Status: QA cakupan token selesai, **belum print-ready**. Sumber P010: `QJ1_P010_GRID_EVALUASI_FATHAH_8x3_DRAF_v0.1.md`. Sumber P020: bagian C `QJ1_P019-P020_KASRAH_CHECKPOINT_8x3_v0.1.md`. Panel yang benar mengikuti `QJ1_P010_P020_EVALUASI_AUTHORITY_CORRECTED_v0.2.md`, bukan teks panel lama di pilot.

## P010 — Evaluasi Fathah
- Grid 8 baris × 3 kelompok; 66 token.
- 22 bentuk berbeda dan setiap bentuk muncul **tepat 3 kali**: بَ تَ ثَ ءَ أَ جَ حَ خَ دَ ذَ رَ زَ سَ شَ صَ ضَ طَ ظَ عَ غَ فَ قَ.
- **PASS cakupan dan pemerataan** untuk 22 bentuk yang telah dikenalkan P001–P009.
- Bi'ah اِسْتَمِعْ; Akhlak أَفْشُوا السَّلَامَ بَيْنَكُمْ; Tahfidz Al-Falaq 4.

## P020 — Evaluasi Fathah + Kasrah
- Grid bagian C: 8 baris × 3 kelompok; 72 token; 58 bentuk berbeda.
- 14 bentuk masing-masing muncul 2 kali: بَ تِ ثَ جِ حَ خِ دَ ذِ رَ زِ سَ شِ صَ ضِ.
- 44 bentuk lain masing-masing muncul 1 kali.
- Cakupan bentuk berbeda: **58 dari 58** (29 identitas × dua harakat, memperlakukan ءَ dan أَ sebagai dua bentuk grafis serta ءِ dan إِ sebagai pasangan Kasrah).
- **PASS cakupan; WARNING pemerataan**: 14 bentuk memiliki pengulangan, 44 hanya sekali. Tidak harus sama rata untuk checkpoint sampel, tetapi rubrik penilaian wajib mempertimbangkan ketimpangan frekuensi.
- Aktivitas 29 identitas tanpa harakat dan pengenalan nama Fathah/Kasrah adalah tugas terpisah, tidak dihitung dalam 72 token grid.
- Bi'ah اِقْرَأْ; Akhlak وَقُلْ رَبِّ زِدْنِي عِلْمًا; Tahfidz Al-Fatihah 6.

## Gate sebelum cetak
1. Pastikan keputusan rubrik P020: nilai per token atau per identitas bentuk, agar 14 bentuk berulang tidak berbobot lebih besar tanpa sengaja.
2. Tashih Al-Falaq 4 dan Al-Fatihah 6 dari mushaf otoritatif; verifikasi klasifikasi sumber Akhlak.
3. Audit visual A5 RTL, font KFGQPC Uthman Taha, hamzah/alif, ha dua lubang, ruang nilai/tanggal/paraf dan QR.
4. Jangan mengubah register FROZEN tanpa keputusan revisi eksplisit.

# QURBATA — Aturan Grid Adaptif Latihan Tartil Jilid 2–8 v1.0

**Keputusan desain:** mulai Jilid 2, jumlah kotak per baris mengikuti panjang dan jenis materi, bukan dipatok tiga kotak. Berlaku untuk desain Paged.js/A5; tidak mengubah Jilid 1 atau konten FROZEN.

## Tiga pola resmi
1. **3 kotak/baris:** huruf, suku kata, atau kata pendek.
2. **2 kotak/baris:** frasa pendek–sedang yang membutuhkan ruang baca lebih luas.
3. **1 kotak/baris:** frasa panjang, penggalan ayat panjang, atau ayat yang wajar dibaca sebagai satu baris penuh.

Ketiga pola **boleh dicampur pada halaman yang sama**. Keputusan dibuat **per baris latihan**, bukan per halaman. Kotak lebar satu baris harus benar-benar memiliki ruang penuh, bukan kotak 1/3 yang diperbesar fontnya. Frasa dan ayat tidak boleh dipotong secara sembarang untuk memenuhi grid.

## Kontrak layout untuk renderer
- `columns: 3 | 2 | 1` per exercise row; `items.length <= columns`.
- `content_type: letter | word | phrase | ayah_excerpt | full_ayah`.
- `source_ref` wajib untuk kata/frasa/ayat yang diklaim berasal dari Al-Qur'an; teks harus cocok dengan mushaf primer sebelum G1 PASS.
- RTL; font KFGQPC Uthman Taha untuk semua teks Arab; ukuran huruf dan tinggi baris mengikuti keterbacaan dan harakat.
- Jika teks terlalu panjang untuk satu baris A5, jangan mengecilkan huruf secara ekstrem: tandai `NEEDS_LAYOUT_REVIEW`, pecah menjadi baris teks yang sah **di dalam satu kotak lebar**, atau pindahkan ke latihan berikutnya melalui keputusan editorial.
- Boleh ada baris tiga kotak, diikuti dua kotak, lalu satu kotak dalam satu halaman.
- Pertahankan minimal lima aktivitas/latihan per halaman jika sesuai standar konten; jumlah kotak bukan pengganti jumlah latihan.
- Jangan mengubah target Tahfidz FROZEN atau nash hanya karena kebutuhan layout.

## Contoh data (struktur saja, bukan nash siap cetak)
```json
{
  "exercise_rows": [
    {"columns":3,"content_type":"word","items":["[kata pendek 1]","[kata pendek 2]","[kata pendek 3]"]},
    {"columns":2,"content_type":"phrase","items":["[frasa 1]","[frasa 2]"]},
    {"columns":1,"content_type":"ayah_excerpt","items":["[teks ayat panjang yang sudah ditashih]"],"source_ref":"[surah:ayat]"}
  ]
}
```

## Gate QA layout
- G1: sumber dan akurasi nash/tanda baca.
- G2: kelayakan instruksi Arab.
- G5: cek overflow A5, tinggi baris, posisi harakat, RTL, konsistensi variasi 3/2/1.
- Jangan menandai final tanpa bukti render dan pemeriksaan penashih.

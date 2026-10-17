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


## Addendum v1.1 — Pedagogi bertahap J2–J8 (keputusan 17 Oktober 2026)

**Aturan lebih spesifik ini mengungguli interpretasi bahwa semua latihan harus campuran 3/2/1.**

- **Penanaman kompetensi baru:** mulai dengan **2 atau 3 kotak per baris** berisi contoh pendek yang terfokus. Guru mencontohkan, santri menirukan, lalu membedakan fitur target.
- **Transisi:** 2 kotak untuk frasa/penggalan yang memperluas konteks; hanya dipakai bila mendukung kompetensi.
- **Latihan inti dan kelancaran:** **1 kotak penuh per baris** untuk frasa/ayat yang lebih panjang; utamakan kesinambungan bacaan, waqaf dan keterbacaan.
- **Jilid 6–8:** **seluruh baris latihan boleh 1 kotak penuh** apabila kompetensi yang diajarkan sudah layak dalam konteks ayat panjang. Jika hukum bacaan baru, berikan contoh pendek terarah pada bagian penanaman (dapat berupa 2–3 kotak), lalu latihan panjang 1 kotak.
- **Evaluasi:** 1 kotak per baris bila targetnya bacaan berkesinambungan; jangan menjadikan jumlah kotak sebagai indikator kompetensi.
- **Batasan:** 1 kotak adalah **lebar satu baris latihan**, bukan janji bahwa seluruh ayat selalu muat dalam satu baris tipografis. Ayat yang terlalu panjang dapat membungkus beberapa baris teks **di dalam kotak penuh** dengan penanganan waqaf yang benar.
- **Keputusan per baris berdasarkan:** kompetensi baru/lama, panjang nash, kompleksitas tajwid, kapasitas santri, dan keterbacaan A5.
- **Jangan mengubah urutan kompetensi FROZEN, Tahfidz FROZEN, atau mencomot potongan ayat tanpa tashih sumber.**

### Perbandingan metodologis
- **Ummi:** direct method, pengulangan, dan pembelajaran bertahap; menjadi inspirasi contoh langsung dan latihan berulang (https://ummifoundation.org/metode).
- **Tilawati:** urutan kompetensi berjilid, klasikal dan baca-simak serta evaluasi bertahap; menjadi inspirasi perpindahan dari penanaman ke bacaan praktik (https://tilawati.org/).
- **Iqro’ dan Bil Qolam:** dijadikan rujukan pembanding lanjutan setelah contoh halaman otoritatif diperiksa; **tidak diklaim** memiliki aturan jumlah kotak yang sama.

### QA tambahan
Setiap halaman harus menyimpan `phase: introduction | transition | fluency | evaluation`, `columns: 1|2|3`, `competency_id`, `quran_source_ref` bila menggunakan nash, serta `layout_review`. Untuk J6–J8, `columns:1` pada semua baris latihan adalah **valid**, bukan kegagalan variasi.

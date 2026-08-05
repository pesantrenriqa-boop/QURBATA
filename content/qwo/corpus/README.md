# QURBATA Verified Quran Corpus

## Master input

Nama file produksi:

```text
content/qwo/corpus/quran-uthmani.txt
```

Format yang diterima:

```text
surah|ayah|teks Utsmani
```

Contoh:

```text
1|1|بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
```

## Sumber

- Tanzil Quran Text
- Text type: Uthmani
- Version: 1.1
- Encoding: UTF-8

## Aturan integritas

1. Teks corpus tidak boleh diedit, dinormalisasi, atau dikoreksi secara manual.
2. Harakat, tanda waqaf, tanda kecil Utsmani, hamzah, alif washal, dan seluruh karakter harus dipertahankan.
3. Blok copyright Tanzil yang diawali `#` harus tetap berada dalam file.
4. File harus memiliki tepat 6.236 baris ayat valid.
5. Referensi pertama harus `1|1|...` dan referensi terakhir `114|6|...`.
6. Tidak boleh ada referensi surah-ayat yang berulang.
7. Seluruh data turunan wajib menyimpan `SourceRef`.

## Validasi

Jalankan:

```bash
python content/qwo/production/runtime/corpus_candidate_generator.py \
  --corpus content/qwo/corpus/quran-uthmani.txt
```

Keluaran hanya sah bila menampilkan:

```text
AYAH_ROWS=6236
```

Jika corpus tidak lengkap atau berubah, proses harus berhenti dan tidak menghasilkan kandidat produksi.

## Status

Corpus Tanzil telah diverifikasi tersedia di File Library pengguna. File Library dan repository GitHub adalah dua penyimpanan berbeda; file produksi harus hadir pada path di atas agar GitHub Actions dan pipeline repository dapat menjalankannya.

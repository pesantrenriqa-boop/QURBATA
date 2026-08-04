# QWO Pipeline Runtime V1

Tujuan tunggal runtime ini adalah menghasilkan sampai 2.500 kandidat QWO unik dari corpus Al-Qur'an tanpa mengulang objek kata.

## Input

File JSONL, satu token Al-Qur'an per baris:

```json
{"surah_number":2,"ayah_number":1,"token_index":1,"uthmani_token":"...","source_edition":"NAMA_EDISI_RESMI","verification_status":"SOURCE_VERIFIED"}
```

Field wajib:

- `surah_number`
- `ayah_number`
- `token_index`
- `uthmani_token`
- `source_edition`

Catatan penting:

- `uthmani_token` harus berasal dari sumber mushaf terverifikasi.
- Script tidak menyediakan atau mengarang teks Al-Qur'an.
- Bentuk Utsmani asli selalu dipertahankan.
- Kombinasi surah, ayat, dan indeks token harus unik.

## Menjalankan

```bash
python3 content/qwo/pipeline/runtime/qwo_pipeline.py \
  --input path/to/quran-token-corpus.jsonl \
  --output-dir content/qwo/pipeline/output/run-001 \
  --limit 2500
```

Tidak membutuhkan library eksternal.

## Output

- `TOKEN_OCCURRENCE.csv`
- `LEXEME_ENTRY.csv`
- `MASTER_QWO_CANDIDATES.csv`
- `PIPELINE_REPORT.json`

## Aturan V1

1. Satu `CanonicalKey` hanya menghasilkan satu objek kandidat.
2. Kompetensi boleh berulang melalui objek Al-Qur'an yang berbeda.
3. Objek kata yang sama tidak diulang sebagai kandidat lain.
4. Semua kandidat berhenti pada status `CANDIDATE`.
5. Tidak ada promosi otomatis menjadi `ACTIVE`.
6. Hasil dapat direproduksi dengan input dan versi script yang sama.

## Target launching

Runtime dianggap memenuhi kebutuhan produksi awal apabila corpus resmi menghasilkan minimal 2.500 bentuk unik yang lolos pemetaan kompetensi dasar. Setelah itu pekerjaan berpindah ke distribusi kandidat ke tangga Jilid 1–8 dan review pedagogis, bukan memperluas arsitektur.

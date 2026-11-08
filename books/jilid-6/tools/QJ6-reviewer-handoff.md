# QJ6 — Panduan serah-terima pemeriksaan ahli

**Status:** draf terkendali; bukan persetujuan cetak atau pengesahan mushaf.

## Berkas dari GitHub Actions

Unduh artefak `qj6-register-and-audit` dari workflow **QURBATA J6 Register Audit** pada commit yang akan diperiksa.

- `QJ6-committed-slots.csv`: register **asli** dari commit, bukan template kosong.
- `QJ6-review-queue.csv`: daftar slot tertahan beserta alasan dan sidik jari baris.
- `QJ6-review-worksheet.csv`: lembar keputusan kosong untuk pemeriksa.
- `QJ6-empty-slot-evidence.csv`: formulir pengumpulan bukti primer untuk 25 slot kosong; tidak berisi usulan ayat.
- `QJ6-committed-audit.json`: hasil audit register asli.
- `QJ6-review-artifact-sha256.txt`: checksum untuk kelima berkas di atas.
- `QJ6-slots.csv` dan `QJ6-audit.json`: **hanya scaffolding terisolasi untuk pengujian**, jangan dipakai sebagai register materi yang telah terisi.

## Verifikasi integritas

Di folder hasil ekstraksi artefak, jalankan:

```bash
sha256sum --check QJ6-review-artifact-sha256.txt
```

Seluruh entri harus berstatus `OK`. Jika gagal, unduh ulang dari run yang sama; jangan menggabungkan berkas dari run atau commit berbeda. Sidik jari `row_sha256` mengikat setiap keputusan dengan keseluruhan baris register asal.

## Urutan review

1. Dahulukan 25 slot kosong (P017, P018, P036), namun **jangan mengisi** tanpa sumber primer dan keputusan kurikulum.
2. Periksa secara langsung tanda waqaf MSI, terutama P017-S02/S04 dan P015-S01/S06 serta P016-S03.
3. Tinjau P022-S09 yang masih `RESEARCH`; lalu kesesuaian tajwid, kompetensi, dan prasyarat seluruh kandidat.
4. Pada lembar reviewer, isi `decision` hanya dengan `APPROVE`, `REVISE`, atau `REJECT`, serta nama, tanggal, edisi mushaf, bukti sumber, kaidah tajwid, dan bukti kesesuaian kurikulum. Keputusan adalah **usulan review**, bukan perubahan otomatis pada register.
5. Dari checkout commit yang sama, jalankan:
   ```bash
   python3 books/jilid-6/tools/qj6-review-queue.py --validate-worksheet QJ6-review-worksheet.csv
   ```
6. Untuk 25 slot kosong, lengkapi formulir bukti primer sesuai P017 (posisi tanda waqaf) atau P018/P036 (persetujuan unit hafalan). Periksa dengan:
   ```bash
   python3 books/jilid-6/tools/qj6-review-queue.py --validate-empty-evidence QJ6-empty-slot-evidence.csv
   ```
   Lulus validasi hanya membuktikan kelengkapan kolom, **bukan autentikasi ayat, edisi MSI, atau persetujuan kurikulum**.
7. Arsipkan keputusan dan bukti dengan Decision-ID. Perubahan register hanya melalui perubahan terpisah, pemeriksaan ahli, pengujian ulang, dan persetujuan eksplisit.

**Gate:** semua slot masih tertahan; `print_approved=false`. Lulus audit teknis tidak berarti lulus pentashihan atau siap cetak.

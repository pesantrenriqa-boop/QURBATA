# QJ6 — Matriks kerja pengisian 25 slot tersisa

Status: DRAF KANDIDAT / BELUM DISAHKAN. Dokumen ini **bukan register resmi**, bukan bukti primer, dan bukan izin cetak.

Baseline issue #22: 335/360 terisi; 25 EMPTY; 1 RESEARCH (P022-S09). `print_approved=false`.

| Halaman | Slot | Jenis kebutuhan | Data yang harus dikumpulkan sebelum pengisian resmi | Status |
|---|---|---|---|---|
| P017 | S01 | Tanda waqaf لا | Edisi MSI, surah:ayat, halaman, posisi glyph لا, bukti foto/rujukan, pemeriksa dan tanggal | MENUNGGU BUKTI |
| P017 | S03 | Tanda waqaf لا | Edisi MSI, surah:ayat, halaman, posisi glyph لا, bukti foto/rujukan, pemeriksa dan tanggal | MENUNGGU BUKTI |
| P017 | S05 | Tanda waqaf لا | Edisi MSI, surah:ayat, halaman, posisi glyph لا, bukti foto/rujukan, pemeriksa dan tanggal | MENUNGGU BUKTI |
| P017 | S06 | Tanda waqaf لا | Edisi MSI, surah:ayat, halaman, posisi glyph لا, bukti foto/rujukan, pemeriksa dan tanggal | MENUNGGU BUKTI |
| P017 | S07 | Tanda waqaf لا | Edisi MSI, surah:ayat, halaman, posisi glyph لا, bukti foto/rujukan, pemeriksa dan tanggal | MENUNGGU BUKTI |
| P017 | S08 | Tanda waqaf لا | Edisi MSI, surah:ayat, halaman, posisi glyph لا, bukti foto/rujukan, pemeriksa dan tanggal | MENUNGGU BUKTI |
| P017 | S09 | Tanda waqaf لا | Edisi MSI, surah:ayat, halaman, posisi glyph لا, bukti foto/rujukan, pemeriksa dan tanggal | MENUNGGU BUKTI |
| P018 | S01 | Hafalan awal | ID unit hafalan disahkan, surah:ayat, urutan, batas ayat, target, cek duplikasi, pemeriksa dan tanggal | MENUNGGU KEPUTUSAN |
| P018 | S02 | Hafalan awal | ID unit hafalan disahkan, surah:ayat, urutan, batas ayat, target, cek duplikasi, pemeriksa dan tanggal | MENUNGGU KEPUTUSAN |
| P018 | S03 | Hafalan awal | ID unit hafalan disahkan, surah:ayat, urutan, batas ayat, target, cek duplikasi, pemeriksa dan tanggal | MENUNGGU KEPUTUSAN |
| P018 | S04 | Hafalan awal | ID unit hafalan disahkan, surah:ayat, urutan, batas ayat, target, cek duplikasi, pemeriksa dan tanggal | MENUNGGU KEPUTUSAN |
| P018 | S05 | Hafalan awal | ID unit hafalan disahkan, surah:ayat, urutan, batas ayat, target, cek duplikasi, pemeriksa dan tanggal | MENUNGGU KEPUTUSAN |
| P018 | S06 | Hafalan awal | ID unit hafalan disahkan, surah:ayat, urutan, batas ayat, target, cek duplikasi, pemeriksa dan tanggal | MENUNGGU KEPUTUSAN |
| P018 | S07 | Hafalan awal | ID unit hafalan disahkan, surah:ayat, urutan, batas ayat, target, cek duplikasi, pemeriksa dan tanggal | MENUNGGU KEPUTUSAN |
| P018 | S08 | Hafalan awal | ID unit hafalan disahkan, surah:ayat, urutan, batas ayat, target, cek duplikasi, pemeriksa dan tanggal | MENUNGGU KEPUTUSAN |
| P018 | S09 | Hafalan awal | ID unit hafalan disahkan, surah:ayat, urutan, batas ayat, target, cek duplikasi, pemeriksa dan tanggal | MENUNGGU KEPUTUSAN |
| P036 | S01 | Hafalan lanjutan/murajaah | ID unit disahkan, surah:ayat, hubungan P018, porsi murajaah, cek duplikasi, pemeriksa dan tanggal | MENUNGGU KEPUTUSAN |
| P036 | S02 | Hafalan lanjutan/murajaah | ID unit disahkan, surah:ayat, hubungan P018, porsi murajaah, cek duplikasi, pemeriksa dan tanggal | MENUNGGU KEPUTUSAN |
| P036 | S03 | Hafalan lanjutan/murajaah | ID unit disahkan, surah:ayat, hubungan P018, porsi murajaah, cek duplikasi, pemeriksa dan tanggal | MENUNGGU KEPUTUSAN |
| P036 | S04 | Hafalan lanjutan/murajaah | ID unit disahkan, surah:ayat, hubungan P018, porsi murajaah, cek duplikasi, pemeriksa dan tanggal | MENUNGGU KEPUTUSAN |
| P036 | S05 | Hafalan lanjutan/murajaah | ID unit disahkan, surah:ayat, hubungan P018, porsi murajaah, cek duplikasi, pemeriksa dan tanggal | MENUNGGU KEPUTUSAN |
| P036 | S06 | Hafalan lanjutan/murajaah | ID unit disahkan, surah:ayat, hubungan P018, porsi murajaah, cek duplikasi, pemeriksa dan tanggal | MENUNGGU KEPUTUSAN |
| P036 | S07 | Hafalan lanjutan/murajaah | ID unit disahkan, surah:ayat, hubungan P018, porsi murajaah, cek duplikasi, pemeriksa dan tanggal | MENUNGGU KEPUTUSAN |
| P036 | S08 | Hafalan lanjutan/murajaah | ID unit disahkan, surah:ayat, hubungan P018, porsi murajaah, cek duplikasi, pemeriksa dan tanggal | MENUNGGU KEPUTUSAN |
| P036 | S09 | Hafalan lanjutan/murajaah | ID unit disahkan, surah:ayat, hubungan P018, porsi murajaah, cek duplikasi, pemeriksa dan tanggal | MENUNGGU KEPUTUSAN |

## Kasus tambahan

- P022-S09: RESEARCH, memerlukan keputusan pentashih QS 21:92 dan titik waqaf; **bukan** bagian dari 25 EMPTY.
- P017-S02/S04 dan P015-S01/S06 serta P016-S03: perlu kolasi tanda waqaf MSI.

## Prosedur untuk mengisi register asli

1. Unduh `QJ6-committed-slots.csv` dan `QJ6-empty-slot-evidence.csv` dari **run yang sama**; verifikasi checksum dan `row_sha256`.
2. Lengkapi bukti primer/keputusan ahli per slot; jangan menggunakan teks rekaan atau placeholder sebagai ayat.
3. Jalankan `qj6-review-queue.py --validate-empty-evidence`; lakukan pentashihan substantif terpisah.
4. Ubah register asli hanya untuk slot dengan keputusan yang tercatat; audit regresi, lalu minta otorisasi rilis independen.

Sumber: issues #22–#26 dan `books/jilid-6/tools/QJ6-reviewer-action-request.md`.

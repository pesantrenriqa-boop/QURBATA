# QURBATA Jilid 6 — Papan kerja cepat penyelesaian hold

**Status awal:** 360 slot, 335 terisi, 25 kosong (P017: 7; P018: 9; P036: 9); 1 slot P022-S09 berstatus RESEARCH. Semua slot masih release hold dan **belum disetujui untuk cetak**. Ini papan penugasan, bukan catatan bukti atau keputusan ahli.

## Jalur paralel (tanpa menunggu paket lain)

| Jalur | Ruang lingkup | Tindakan ahli yang diperlukan | Hasil yang harus diserahkan | Kriteria siap diproses |
| --- | --- | --- | --- | --- |
| A — MSI | P017 tujuh EMPTY; P017-S02/S04; P015-S01/S06; P016-S03 | Pentashih memeriksa mushaf MSI target dan posisi tanda waqaf secara langsung | Identitas edisi, surah/ayat, halaman, bukti tanda waqaf, keputusan bertanggal | Bukti primer dapat ditelusuri dan memenuhi prasyarat kompetensi |
| B — Kurikulum hafalan awal | P018 sembilan EMPTY | Penanggung jawab kurikulum menetapkan unit hafalan, urutan, target dan penilaian | Dokumen keputusan resmi + ID persetujuan per unit, ayat dan cek duplikasi | Unit disahkan dan sumber ayat dapat diperiksa |
| C — Kurikulum hafalan lanjutan | P036 sembilan EMPTY | Penanggung jawab kurikulum menetapkan progresi dan murajaah terkait P018 | Dokumen keputusan resmi + ID persetujuan, peta hubungan P018 | Urutan konsisten, tidak ada duplikasi yang tidak disengaja |
| D — Kasus khusus | P022-S09 RESEARCH | Pentashih dan ahli tajwid menilai teks QS 21:92 serta titik waqaf sesuai kompetensi | Keputusan tertulis dengan alasan, rujukan mushaf, aturan bacaan | Status RESEARCH diselesaikan lewat revisi register terpisah, bukan APPROVE langsung |

## Pelacakan GitHub langsung

- [Issue #22 — pusat koordinasi](https://github.com/pesantrenriqa-boop/QURBATA/issues/22)
- [Issue #23 — jalur A, pentashih MSI/waqaf](https://github.com/pesantrenriqa-boop/QURBATA/issues/23)
- [Issue #24 — jalur B, hafalan P018](https://github.com/pesantrenriqa-boop/QURBATA/issues/24)
- [Issue #25 — jalur C, hafalan P036](https://github.com/pesantrenriqa-boop/QURBATA/issues/25)
- [Issue #26 — jalur D, P022-S09 RESEARCH](https://github.com/pesantrenriqa-boop/QURBATA/issues/26)

Gunakan [template laporan bukti ahli](../../../.github/ISSUE_TEMPLATE/qj6-expert-evidence.md) saat menyerahkan hasil pemeriksaan. Template ini berada pada branch kerja; sampai tersedia pada default branch, salin isinya ke komentar issue yang relevan. **Issue yang dibuat tidak berarti reviewer telah ditugaskan atau bukti sudah diterima.**

## Prosedur satu putaran

1. **Bagi tugas A–D secara paralel.** Tidak perlu menunggu hasil jalur lain untuk mulai memeriksa bukti.
2. **Kunci versi sumber:** gunakan satu commit/run dan verifikasi checksum artefak. Simpan `row_sha256` tanpa perubahan.
3. **Isi berkas resmi:** `QJ6-empty-slot-evidence.csv` untuk 25 slot kosong; `QJ6-review-worksheet.csv` untuk keputusan pada slot terisi. Jangan mengisi teks ayat hasil tebakan.
4. **Periksa administrasi:** jalankan kedua validator. Bila ada kesalahan, kembalikan hanya baris bermasalah kepada reviewer, bukan seluruh paket.
5. **Periksa substansi:** pentashih/kurikulum mengecek bukti primer dan prasyarat; catat keputusan, tanggal, dan ID yang unik.
6. **Implementasi terkontrol:** ubah register hanya untuk slot dengan bukti yang telah disahkan, pada commit/PR terpisah; jalankan audit dan tes; pertahankan release hold yang belum terselesaikan.
7. **Rilis independen:** keputusan review atau CI hijau tidak otomatis berarti boleh cetak.

## Pelaporan progres yang tidak menyesatkan

Gunakan empat angka berbeda: (a) slot terisi, (b) bukti primer diterima, (c) slot telah disahkan ahli, (d) slot lolos gerbang cetak. **Jangan menyamakan angka (a) dengan (c) atau (d).**

| Indikator | Baseline terkonfirmasi | Target setelah bukti ahli |
| --- | ---: | --- |
| Slot terisi | 335/360 | Maksimum 360/360, hanya jika seluruh 25 usulan disahkan |
| Slot kosong | 25 | 0 jika semua keputusan dan sumber lengkap |
| P022-S09 RESEARCH | 1 | 0 setelah keputusan dan revisi yang sah |
| Izin cetak | Tidak | Hanya setelah otorisasi rilis independen |

## Penghalang yang tidak dapat diselesaikan oleh otomatisasi

**Belum ada bukti primer atau keputusan ahli baru yang diserahkan melalui papan kerja ini.** Tim teknis tidak boleh menciptakan contoh waqaf, memilih ayat hafalan atas nama kurikulum, mengesahkan tanda MSI, atau menaikkan flag verifikasi secara otomatis.

Dokumen pendamping: [permintaan tindakan reviewer](QJ6-reviewer-action-request.md), [panduan serah-terima](QJ6-reviewer-handoff.md), [checklist penerimaan](QJ6-reviewer-return-checklist.md).

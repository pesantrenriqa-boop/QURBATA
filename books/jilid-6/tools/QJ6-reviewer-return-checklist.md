# QJ6 — Checklist penerimaan hasil pemeriksaan ahli

**Tujuan:** memastikan hasil pentashih dapat diterima, diverifikasi, dan diaudit tanpa mengubah register secara otomatis. Dokumen ini bukan persetujuan materi atau cetak.

## Pemeriksaan penerimaan berkas

- [ ] Catat URL run GitHub Actions, commit SHA penuh, tanggal pengiriman, nama dan peran pengirim.
- [ ] Terima `QJ6-review-worksheet.csv` dan/atau `QJ6-empty-slot-evidence.csv` dari **satu** versi register; jangan menggabungkan hasil lintas commit.
- [ ] Cocokkan `QJ6-committed-slots.csv` dengan commit rujukan; verifikasi `QJ6-review-artifact-sha256.txt` menggunakan `sha256sum --check`.
- [ ] Pastikan `row_sha256` pada **setiap baris** `QJ6-empty-slot-evidence.csv` tidak diubah; formulir versi lama tanpa kolom tersebut harus diekspor ulang dari commit yang sesuai. Jangan memindahkan keputusan ke formulir baru tanpa pemeriksaan ulang sumbernya.
- [ ] Jalankan `python3 books/jilid-6/tools/qj6-review-queue.py --validate-worksheet <path>` untuk worksheet dan `--validate-empty-evidence <path>` untuk intake slot kosong.
- [ ] Pastikan setiap keputusan menyertakan identitas pentashih, tanggal, identitas edisi mushaf, bukti rujukan, kaidah tajwid, dan kecocokan kompetensi.
- [ ] Untuk `REVISE`/`REJECT`, periksa alasan pada `review_notes`. Untuk `RESEARCH` dan `EMPTY`, jangan memproses `APPROVE` langsung.
- [ ] Periksa **bukti primer secara manusiawi**: surah/ayat, bentuk dan lokasi tanda waqaf pada edisi target, kecocokan potongan ayat, serta batas materi jilid sebelumnya.
- [ ] Pastikan keputusan unit hafalan P018/P036 berasal dari penanggung jawab kurikulum yang berwenang, dengan ID dan tanggal keputusan.
- [ ] Catat setiap konflik bukti sebagai `NEEDS_CLARIFICATION` di log serah-terima; jangan mengubah CSV register untuk menyembunyikan konflik.
- [ ] Buat usulan perubahan register sebagai pull request/commit **terpisah**; jalankan seluruh audit dan regression tests sebelum penggabungan.
- [ ] Pertahankan `print_approved=false` hingga ada otorisasi rilis independen setelah semua hold ditutup.

## Jalur pengembalian tercepat

1. **Pentashih MSI:** unggah bukti ke [Issue #23](https://github.com/pesantrenriqa-boop/QURBATA/issues/23) untuk P017/P015/P016; kasus P022-S09 khusus ke [Issue #26](https://github.com/pesantrenriqa-boop/QURBATA/issues/26).
2. **Penanggung jawab hafalan:** unggah keputusan resmi P018 ke [Issue #24](https://github.com/pesantrenriqa-boop/QURBATA/issues/24), dan P036 ke [Issue #25](https://github.com/pesantrenriqa-boop/QURBATA/issues/25).
3. Gunakan [template laporan](../../../.github/ISSUE_TEMPLATE/qj6-expert-evidence.md) sebagai format komentar; sertakan tautan bukti primer dan nomor keputusan, bukan sekadar pernyataan sudah dicek.
4. Koordinator memperbarui [Issue #22](https://github.com/pesantrenriqa-boop/QURBATA/issues/22) hanya setelah berkas diterima dan diperiksa. Jika belum ada bukti, biarkan checklist tetap kosong.
5. Jangan menunggu keempat jalur selesai untuk memvalidasi **administrasi** satu paket yang sudah masuk; tetapi jangan melakukan persetujuan cetak secara parsial.

## Log serah-terima (isi oleh penerima)

| Kolom | Nilai |
| --- | --- |
| Tanggal penerimaan | BELUM DIISI |
| Nama/peran pengirim | BELUM DIISI |
| Nama/peran penerima | BELUM DIISI |
| Commit SHA dan run CI asal | BELUM DIISI |
| Paket W1/H1/H2/R1 | BELUM DIISI |
| Berkas dan checksum cocok | BELUM DIPERIKSA |
| Validator worksheet/intake | BELUM DIJALANKAN |
| Bukti primer telah diperiksa | BELUM DIPERIKSA |
| Konflik dan tindak lanjut | BELUM DIISI |
| Keputusan penerimaan administrasi | BELUM DIPUTUSKAN |

**Penting:** nilai `BELUM DIISI` adalah petunjuk dokumen ini, bukan nilai yang boleh dimasukkan ke kolom bukti CSV. Lulus checksum dan validator tidak membuktikan kebenaran teks mushaf, kaidah tajwid, atau persetujuan kurikulum.

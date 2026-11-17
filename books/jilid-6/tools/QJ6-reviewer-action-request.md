# QURBATA Jilid 6 — Permintaan tindakan pemeriksa (P017, P018, P036, P022)

**Status:** PERLU BUKTI PRIMER DAN KEPUTUSAN AHLI. Dokumen ini adalah permintaan kerja, **bukan hasil tashih**. Jangan mengubah teks mushaf, menandai verified, atau mengizinkan cetak berdasarkan dokumen ini.

## Paket kerja yang dapat dibagi ke pemeriksa

| Paket | Slot | Penanggung jawab yang diperlukan | Keputusan yang diminta | Bukti minimum | Keluaran |
| --- | --- | --- | --- | --- | --- |
| W1 — tanda waqaf لا | P017-S01, S03, S05–S09 (7 kosong); bandingkan P017-S02/S04 (terisi tetapi tanda belum terbukti) | Pentashih/tajwid yang dapat melihat mushaf MSI target | Identifikasi contoh dengan **tanda waqaf لا tersendiri**, bukan huruf لا sebagai kata; tentukan kecocokan kompetensi | Identitas edisi MSI, surah:ayat, halaman/tautan edisi, posisi tanda, dokumentasi rujukan, catatan prasyarat | Isian bukti untuk 7 slot kosong dan keputusan untuk S02/S04 |
| H1 — hafalan pertama | P018-S01–S09 (9 kosong) | Penanggung jawab kurikulum hafalan | Tetapkan unit hafalan resmi, urutan, target usia, batas ayat, dan kriteria penilaian | Dokumen kurikulum bertanggal, ID persetujuan unit, surah:ayat, pemeriksaan pengulangan | Keputusan unit hafalan dan isian bukti untuk 9 slot |
| H2 — hafalan lanjutan | P036-S01–S09 (9 kosong) | Penanggung jawab kurikulum hafalan | Tetapkan unit lanjutan dan porsi murajaah, pastikan progresi dari P018 | Dokumen kurikulum bertanggal, ID persetujuan, keterkaitan P018, surah:ayat | Keputusan unit dan isian bukti untuk 9 slot |
| R1 — riset bacaan | P022-S09 (1 RESEARCH) | Pentashih mushaf dan ahli tajwid | Tentukan ketepatan potongan QS 21:92 dan titik berhenti untuk kompetensi terkait | Bukti ayat edisi target, kaidah tajwid/waqaf, alasan keputusan, identitas pemeriksa | APPROVE/REVISE/REJECT **setelah** revisi status register yang terdokumentasi; tidak boleh approve RESEARCH langsung |

## Perhatian khusus tanda MSI

Selain P017, mohon kolasi langsung tanda waqaf pada P015-S01 (QS 6:36), P015-S06 (QS 10:65), dan P016-S03 (QS 61:7). Catat **posisi dan bentuk glyph yang terlihat pada edisi MSI**, bukan hasil pencarian teks digital atau perkiraan.

## Ketentuan isian formulir yang diperbarui

- Kolom `row_sha256` pada `QJ6-empty-slot-evidence.csv` adalah sidik jari **baris register asal** dan tidak boleh diubah. Formulir tanpa kolom ini berasal dari versi lama dan perlu diekspor ulang.
- Gunakan `decision_id` unik untuk setiap usulan slot. Jangan memakai ID yang sama untuk dua usulan berbeda.
- Untuk P017, isi `waqf_sign_position` berdasarkan tanda waqaf yang benar-benar terlihat di edisi MSI target; **jangan isi** `hafalan_unit_approval_id`.
- Untuk P018/P036, isi `hafalan_unit_approval_id` dari keputusan kurikulum resmi; **jangan isi** `waqf_sign_position`.
- Kolom yang masih kosong berarti **belum ada bukti**, bukan bukti persetujuan. Tidak perlu mengisi ayat rekaan untuk memenuhi jumlah slot.

## Instruksi pelaksanaan

1. Unduh satu artefak `qj6-register-and-audit` dari run GitHub Actions yang sama. Gunakan `QJ6-committed-slots.csv` sebagai sumber register, **bukan** `QJ6-slots.csv` scaffold pengujian.
2. Verifikasi `QJ6-review-artifact-sha256.txt` menggunakan `sha256sum --check QJ6-review-artifact-sha256.txt`.
3. Isi `QJ6-empty-slot-evidence.csv` untuk paket W1/H1/H2 dan `QJ6-review-worksheet.csv` untuk keputusan terhadap baris yang sudah terisi. Catat bukti, reviewer, tanggal, dan Decision-ID; jangan mengisi placeholder seperti `pending`.
4. Validasi format menggunakan `qj6-review-queue.py --validate-empty-evidence` dan `--validate-worksheet`. **Lulus validator hanya berarti format dan kelengkapan administratif**, bukan keaslian ayat atau kesesuaian kurikulum.
5. Serahkan berkas beserta salinan/rujukan bukti primer. Tim pengembang kemudian membuat **commit terpisah** untuk setiap perubahan register dan menjalankan audit ulang. Tidak ada persetujuan cetak otomatis.

## Pertanyaan keputusan yang belum dapat dijawab oleh perangkat lunak

- **W1:** Tanda لا yang tepat berada di mana pada halaman mushaf target? Apakah setiap contoh memenuhi prasyarat jilid ini?
- **H1:** Surah/ayat mana yang *sudah disahkan* sebagai hafalan pertama, dan apakah 9 slot memang diperlukan?
- **H2:** Bagian mana yang merupakan hafalan baru dan mana murajaah? Bagaimana hubungan dengan H1?
- **R1:** Apakah bentuk dan titik waqaf QS 21:92 sesuai target kompetensi? Jika tidak, apa revisi yang disahkan?

**Gerbang rilis:** 360 slot tetap dalam hold dan `print_approved=false` sampai bukti primer, pemeriksaan kompetensi, audit regresi, dan otorisasi cetak independen selesai.

# Sistem cepat pengisian dan audit QURBATA Jilid 6

**Status:** DRAFT TOOLING. Tidak mengubah master dan tidak mengklaim tashih otomatis.

## Arsitektur
- Sumber kompetensi: `books/jilid-6/QJ6-MASTER-Struktur-40-Halaman.md`.
- Satu register CSV, 360 baris, ID tetap QJ6-P001-S01 s.d. QJ6-P040-S09.
- Pengisian dilakukan batch 10 halaman; CSV adalah data kerja, master tetap pengendali.
- Status: EMPTY → CANDIDATE → SOURCE_CHECKED → COMPETENCY_CHECKED → REVIEW → APPROVED.
- **APPROVED bukan status final buku**; keputusan akhir tetap melalui review ahli dan governance.

## Jalankan
```bash
python3 books/jilid-6/tools/qj6_slots.py init --master books/jilid-6/QJ6-MASTER-Struktur-40-Halaman.md --csv books/jilid-6/tools/QJ6-slots.csv
python3 books/jilid-6/tools/qj6_slots.py audit --master books/jilid-6/QJ6-MASTER-Struktur-40-Halaman.md --csv books/jilid-6/tools/QJ6-slots.csv --report books/jilid-6/tools/QJ6-audit.json
```
Perintah init menolak menimpa CSV yang sudah ada. Audit menampilkan duplikat, slot hilang, ketidakcocokan halaman, sumber kosong, dan verifikasi yang belum lengkap.

## Gate audit
1. 360 ID unik dan 9 slot tiap halaman.
2. Teks Qurani harus dibandingkan dengan mushaf rujukan otoritatif secara manual; algoritme tidak mengesahkan rasm.
3. Source-ID, surah dan nomor ayat wajib.
4. Pemeriksaan kompetensi (termasuk materi prematur) wajib dilakukan ahli; flag `competency_verified=yes` bukan pengganti bukti.
5. Evaluasi P010/P020/P030/P040 tidak boleh mengenalkan materi baru.
6. P018/P028/P036/P038 mempertahankan fungsi integrasi sesuai master.
7. Tidak boleh mempublikasikan tanpa reviewer, Evidence-ID dan Decision-ID sesuai baseline.

## Strategi percepatan
Buat kandidat massal pada salinan CSV; gunakan audit otomatis tiap batch; lakukan tashih sumber dan kompetensi; hanya kandidat yang lolos masuk tahap review. Simpan perubahan via PR agar mudah dibandingkan dan di-rollback.

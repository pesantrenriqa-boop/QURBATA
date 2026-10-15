# QURBATA J1 — Proposal Change Control CC-001 untuk penanaman dua TARGET

**Status: PROPOSAL / BELUM DISETUJUI / FROZEN TIDAK DIUBAH.** Dokumen ini mengusulkan penyelesaian kontradiksi matematis antara 6 sel penanaman TARGET-only dan HARD GATE larangan duplikasi pada halaman dengan tepat 2 TARGET.

## Cakupan
P002 (ءَ أَ), P005 (سَ شَ), P006 (صَ ضَ), P007 (طَ ظَ), P008 (عَ غَ), P009 (فَ قَ), P011 (كَ لَ), P012 (مَ نَ). P001/P003/P004 tidak mendapat pengecualian. Semua halaman lain tetap mengikuti FROZEN.

## Bukti kontradiksi
Dua TARGET menghasilkan maksimal 2×2=4 pasangan berurutan berbeda jika pasangan AA/BB diperbolehkan; enam sel TARGET-only unik mustahil. Jika AA/BB dilarang, hanya dua pasangan unik. Maka persyaratan enam sel dan nol duplikasi tidak dapat berlaku serentak untuk n=2.

## Usulan keputusan operasional (opsi A)
1. Tetap 8×3 kelompok, baris 1–2 tepat enam sel EXACT-2 TARGET-only; baris 3–8 tepat 18 sel EXACT-3 dengan sekurang-kurangnya satu TARGET per sel dan hanya REVIEW_ALLOWED.
2. Khusus n=2, izinkan **dua pengulangan penanaman** yang tercatat (menggunakan keempat pola AA, AB, BA, BB); keenam sel menjadi 4 pola unik + 2 pengulangan. Kelompok latihan 18/18 wajib unik; tidak boleh menduplikasi sel penanaman.
3. TARGET tetap 60%±toleransi kurasi dari 66 token bila rasio ini diberlakukan; halaman foundation/checkpoint mengikuti aturan masing-masing. Jangan menganggap persentase sebagai bukti mutu pedagogis.
4. Tandai `EXCEPTION-APPROVED` hanya setelah persetujuan tertulis pemilik kurikulum; sebelum itu `EXCEPTION-PENDING` dan hard gate resmi tetap BLOCKED.
5. Jangan mengubah register FROZEN, generator, atau label siap cetak sebelum keputusan disahkan dan perubahan diimplementasikan dengan tes regresi.

## Alternatif keputusan (opsi B)
Pertahankan nol duplikasi dengan **mengubah bentuk penanaman** (misalnya memperbolehkan pasangan dengan REVIEW), tetapi ini bertentangan dengan TARGET-only dan membutuhkan revisi kurikulum lebih luas. Tidak direkomendasikan tanpa penilaian pedagogis.

## Formulir keputusan
- ID: QJ1-CC-001
- Pemilik keputusan: Pengarah Kurikulum QURBATA
- Keputusan: [ ] SETUJU opsi A  [ ] TOLAK  [ ] MINTA REVISI
- Tanggal keputusan: __________
- Alasan dan konsekuensi: __________
- Tanda tangan/otorisasi: __________

## Acceptance tests setelah persetujuan
- Delapan halaman n=2: 6 sel planting, tepat 4 pasangan unik dan 2 duplikasi terencana, 18 sel practice unik dan legal.
- P001/P003/P004: 6 pasangan planting unik tanpa pengecualian.
- Semua halaman: urutan TARGET FROZEN tetap, no future token, detached-letter, glyph, tashih, dan proof A5 RTL.

**Batas:** belum ada persetujuan yang tercatat. Ini dokumen permintaan keputusan, bukan keputusan yang telah berlaku.

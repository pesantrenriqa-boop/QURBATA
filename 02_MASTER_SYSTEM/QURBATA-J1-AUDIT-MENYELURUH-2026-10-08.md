# AUDIT MENYELURUH QURBATA JILID 1 — TEMUAN AWAL & GATE PRODUKSI
Tanggal: 2026-10-08
Branch: renderer/pagedjs-p001-prototype
STATUS: AUDIT IN PROGRESS — NOT PRINT READY

## CAKUPAN YANG TELAH DIVERIFIKASI
- Register P001–P040 tersedia dan P040 tercatat CHECKPOINT-FINAL.
- File dengan pola `02_MASTER_SYSTEM/QURBATA-J1-READING-PNNN-v0.1.md` berhasil diakses: P014–P040 (27 file).
- P001–P013 tidak ditemukan **pada pola path tersebut**; ini belum membuktikan kontennya tidak ada di repo. Lakukan penelusuran nama/path alternatif sebelum menandai sebagai hilang.
- P031–P038 serta P040 masing-masing memuat 24 baris soal bernomor dalam struktur yang diperiksa. P039 memuat 24 soal utama ditambah 6 langkah protokol bernomor; penghitung angka mentah tidak boleh dipakai sebagai group-count.
- P021–P028 menggunakan bagian instruksi bernomor sehingga penghitung mentah melebihi 24; wajib ekstraksi blok soal sebelum audit otomatis.

## TEMUAN DAN RISIKO
1. BLOCKER TRACEABILITY: lokasi dan versi otoritatif P001–P013 belum diverifikasi.
2. BLOCKER LEXICAL: audit MSL lintas halaman, bentuk leksikal, dan pengulangan kata belum diselesaikan. Perlu verifikasi semua klaim 'kata bermakna' dengan rujukan kamus Arab dan konteks morfologi.
3. BLOCKER PHONOLOGICAL: setiap item harus diverifikasi legalitas harakat menurut halaman pengenalan; jangan menganggap seluruh harakat legal secara retrospektif.
4. BLOCKER TYPOGRAPHY: rendering PDF, penggunaan KFGQPC Uthman Taha, posisi harakat, dua lubang ha, dan kesesuaian layout belum diuji.
5. CHECKPOINT P040: bagian tanpa harakat harus dinilai sebagai identifikasi huruf, bukan tebak vokal. Periksa kecocokan rubrik dan layout cetak.
6. SCORING P036–P039: skor 100 merupakan rancangan internal; validasi reliabilitas dan kejelasan deskriptor penilaian diperlukan.
7. VERSIONING: beberapa file P014–P028 memuat status v0.2/v0.4 meski nama file berakhir v0.1. Perlu harmonisasi metadata versi tanpa menghilangkan riwayat.
8. CROSS-PAGE DUPLICATES: deteksi pengulangan belum dituntaskan; setiap pengulangan harus diklasifikasikan review terencana atau duplikasi tak disengaja.

## TINDAKAN WAJIB SEBELUM FREEZE
- Temukan otoritas P001–P013 dan inventaris semua 40 halaman.
- Parse semua kelompok latihan dari blok otoritatif, bukan seluruh baris bernomor.
- Audit cakupan huruf dan harakat per halaman, termasuk batas kompetensi.
- Normalisasi grafem Arab (hamzah, alif, ta marbuta, harakat) untuk deteksi duplikasi, tanpa mengubah authority.
- Verifikasi makna/morfologi setiap item yang diklaim leksikal; tandai decoding-only untuk yang belum terverifikasi.
- Audit instruksi guru, tahfidz, akhlak, dan BA sesuai cakupan Jilid 1.
- Audit P020 dan P040: membaca dengan/tanpa harakat, nilai, tanggal, tanda tangan.
- Render PDF dan inspeksi visual semua halaman.
- Catat temuan per halaman: severity, evidence, fix, reviewer, status.

## KEPUTUSAN
HOLD PRINT FREEZE. Dokumen ini adalah catatan audit awal yang didasarkan pada pembacaan dan verifikasi akses berkas, bukan sertifikat bahwa seluruh 40 halaman sudah lolos audit substansi.


## AUDIT LANJUTAN — 2026-10-08: DEDUPLIKASI P029–P040
Metode: membaca langsung 12 berkas P029–P040, mengekstrak nomor soal 1–24, dan membandingkan rangkaian Arab setelah normalisasi spasi (harakat tetap dipertahankan).

HASIL:
- 12/12 berkas dapat dibaca.
- 288/288 butir bernomor 1–24 teridentifikasi (24 per halaman).
- 8 kemunculan ulang identik lintas halaman:
  1. P029:8 → P032:3 — `دِ ذُ رَ`
  2. P032:15 → P037:15 — `زُ رِ عَ`
  3. P036:19 → P039:13 — `تُ بِ عَ`
  4. P030:15 → P039:17 — `فُ تِ حَ`
  5. P029:1 → P040:1 — `بَ بِ بُ`
  6. P029:4 → P040:4 — `سَ سُ سِ`
  7. P029:15 → P040:16 — `سُ ئِ لَ`
  8. P030:14 → P040:18 — `وُ جِ دَ`

PENILAIAN:
- Pengulangan pada P040 mungkin sengaja sebagai tes retensi; pertahankan sementara sampai blueprint tes akhir dikonfirmasi.
- P039 diberi label simulasi final dan memuat 2 stimulus identik dari halaman sebelumnya. Tandai sebagai potensi paparan soal (MEDIUM) dan ganti bila menginginkan tes transfer belum pernah dilihat.
- P037:15 adalah reuse P032:15; mungkin retensi terencana.
- Klaim P040 bahwa C13–C18 seluruhnya 'REVIEW-REUSE' belum terbukti untuk keenam butir hanya dari data P029–P040: ditemukan bukti identik untuk C16 dan C18 saja pada rentang itu. Audit halaman lebih awal diperlukan.

CATATAN BATASAN:
- Ini audit kecocokan string, bukan verifikasi keabsahan kata Arab.
- P001–P013 masih belum ditemukan pada pola path yang diuji; pencarian GitHub pada default branch untuk nama P001/P013 tidak memberi hasil, namun bukan bukti tidak adanya berkas pada branch kerja.
- Tidak ada perubahan pada materi latihan dalam tahap ini.

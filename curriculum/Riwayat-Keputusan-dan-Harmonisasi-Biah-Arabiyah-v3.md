# Riwayat keputusan dan harmonisasi Bi’ah Arabiyah v3
26 November 2026. Catatan pengendalian atas arahan pemilik akademik agar seluruh aturan tersimpan sebagai acuan resmi. Branch main. Tunduk pada QURBATA-BASELINE; bukan pengganti REG-GOV atau Decision-ID formal. Status: catatan riwayat terkontrol; keputusan desain v3 disetujui, aktivasi materi belum.
## Riwayat
|Dokumen|Status|Perubahan|
|---|---|---|
|standards/Panduan-Sintaks-Pembelajaran-QURBATA-60-Menit-FROZEN.md|Riwayat desain|18 langkah 10–40–10|
|standards/Panduan-Sintaks-Pembelajaran-QURBATA-Jilid-1-8-FROZEN.md|FROZEN pedagogis v2|Diferensiasi jilid; struktur tetap|
|standards/Panduan-Biah-Arabiyah-QURBATA-Jilid-1-8-FROZEN-v3.md|FROZEN desain Arab|J1–2 instruksi/adab, J3 mulai mufradat sistematis; mengganti arah Arab v2 saja|
|curriculum/Register-Instruksi-Guru-dan-Akhlak-QJ1-QJ2-DRAFT.md|DRAFT|80 slot; J2 usulan|
|curriculum/Migrasi-Inventaris-Mufradat-Jilid-3-8-v3-DRAFT.md|DRAFT|45 entri, 100 baris lema; baseline 550 usulan|
|curriculum/Crosswalk-Arab-Hadis-Akhlak-QJ1-v3-DRAFT.md|DRAFT|40 kandidat, 0 approved|
|books/jilid-1/Panduan-Guru-QJ1-Bagian-01-P001-P010-DRAFT.md|Riwayat target Arab lama|Jangan gunakan sebagai target Arab v3|
|books/jilid-1/Panduan-Guru-QJ1-Bagian-01-P001-P010-v3-DRAFT.md|DRAFT revisi|10 tabel 60 menit; commit c9e9dad52fbb0770c2782c3000ce476424952703|
## Audit tema hadis
PROP-HAD-QJ1-001: HAD-000026 generalisasi/replace; HAD-000039 pertimbangkan J2/kanal guru; HAD-000032 pindah jika terlalu abstrak; HAD-000038 kanal guru/pindah dengan privasi; HAD-000033 bedakan dari HAD-000006 atau merge. Jangan paksa 40 intro baru; checkpoint review. HAD-000037 tidak selaras langsung dengan doa, perlu review usia. Tidak ada penggantian matan. P001 salam HAD-000007 dan P022 terima kasih HAD-000018 merupakan usulan resequence, bukan aktivasi. Jadwal MAP-HAD-QJ1-001 1/3/7/14, checkpoint P008/016/024/032/040 maksimum 8 prompt, harus dihitung ulang berdasarkan intro sah; alokasi lama 5 menit konflik dengan 2+2 menit v2/v3, uji durasi diperlukan. Tidak mengubah MAP atau PROP.
## Governance
Setiap revisi catat tanggal, sumber/path, versi, alasan, status, perubahan, dependency, bukti dan commit. Simpan sejarah melalui Git dan arsip sesuai baseline; jangan gunakan versi tergantikan untuk produksi. FROZEN desain bukan APPROVED materi. DEC-CUR-005 masih mengendalikan kandidat siklus lama sampai harmonisasi formal ACP/DEC-CUR; v3 tidak mengaktifkan teks atau gate. Perlu Decision-ID formal dan pembaruan indeks governance sebelum klaim acuan operasional penuh. Tidak menetapkan ID baru tanpa pemeriksaan register. Tahap berikutnya revisi P011–020, kemudian P021–040 setelah gate desain terkait.

## Log kelanjutan — 26 November 2026
- `books/jilid-1/Panduan-Guru-QJ1-Bagian-02-P011-P020-v3-DRAFT.md` — commit `ab17597791897380a3ba8491add4a846643d0936`. Revisi 10 tabel, 180 langkah, masing-masing 60 menit; target lisan mengikuti v3, kandidat hadis HOLD. Panduan lama P011–P020 dipertahankan sebagai riwayat, bukan target Arab terbaru.
- P018 tetap BLOCKED-CUR-HAF-002; P020 evaluasi respons tanpa model, panel nama huruf terpisah. Sumber Tartil diwarisi dari panduan sebelumnya, belum diperiksa ulang. Tidak ada aktivasi atau perubahan FROZEN.
- Progres revisi panduan J1: 20/40. Berikutnya P021–P030 setelah pemeriksaan gate desain dan sumber halaman. Decision-ID formal, harmonisasi register, validasi ahli dan uji durasi masih terbuka.


## Log P021–P030 — 26 November 2026
- Panduan `books/jilid-1/Panduan-Guru-QJ1-Bagian-03-P021-P030-v3-DRAFT.md`, commit `b00052c2843590f52982bbd79333e6f2c90fc9b1`. 10 tabel, 18 langkah dan 60 menit masing-masing; blob sumber dicatat.
- P028 alternatif desain praktik kumulatif v3, unit khusus tetap ditahan sampai harmonisasi DEC-CUR-005/gate. P030 evaluasi 24 fathah, 24 kasrah, 16 dhammah, 29 identitas; tidak mengklaim cakupan 74 padanan. Hadis HOLD; tidak mengubah FROZEN atau register induk. Audit token independen, validasi ahli dan Decision-ID masih terbuka.
- Progres 30/40 panduan DRAFT. Berikutnya P031–P040.


## Log P031–P040 — 26 November 2026
- `books/jilid-1/Panduan-Guru-QJ1-Bagian-04-P031-P040-v3-DRAFT.md`, commit `abc3d1cc97fdf3a8fb39cd69fbd52b757ffa4ed2`. 10 tabel, 18 langkah dan 60 menit masing-masing; blob sumber dicatat.
- P033 ءُ HOLD; P036 BLOCKED-CUR-HAF-002; P038 inti akhlak dengan target Arab kondisional. P040 konflik sumber §6 talqin sampel vs tes mandiri: usulan pisahkan tes dari latihan setelah tes, perlu keputusan formal. Panel nama huruf II terpisah; uji kelayakan waktu. Hadis HOLD, audit token dan validasi ahli terbuka.
- 40/40 panduan DRAFT tersusun, bukan FROZEN final. Berikutnya audit lintas empat bagian, harmonisasi dan pengesahan desain sesuai governance. Tidak mengubah FROZEN atau register induk.


## Log konsolidasi v3.1 — 26 November 2026
- Master `books/jilid-1/Master-Panduan-Guru-QJ1-v3.1-DRAFT.md`: commit awal `23c28c5cf61c791268ae225183b1b7462ae4ef47`; penandaan paparan `7040b5d5720188dfd24511c5291af83e53e2440b`. 40 tabel/720 langkah/2400 menit; 10–40–10 tiap sesi. 32 target reguler, 2 kondisional, 6 review/evaluasi. Jadwal recall N+1/2/4/8 asumsi satu halaman per sesi; hitung ulang jika tertunda.
- Audit literal awal 149 kecocokan instruksi sebelum intro reguler (dapat tumpang tindih); 159 baris instruksi diberi label paparan awal/kondisional. Bukan audit linguistik menyeluruh. Paparan bukan mastery. Dokumen bagian asli dipertahankan.
- Status DRAFT, bukan FROZEN final. Audit token, whitelist, LO/KO, validasi hadis/hafalan, harmonisasi unit khusus dan tes, Decision-ID dan uji waktu terbuka. Tidak mengubah FROZEN atau register induk.

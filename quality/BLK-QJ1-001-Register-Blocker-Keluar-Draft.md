# BLK-QJ1-001 — Register Blocker Keluar-Draft Jilid 1

**Register-ID:** BLK-QJ1-001  
**Status:** OPEN  
**Tanggal:** 28 Juli 2026  
**Cakupan:** PR #2 — Buku QURBATA Jilid 1

## 1. Blocker Materi dan Keilmuan

| Blocker-ID | Lokasi | Kebutuhan | Pemilik Keputusan | Status |
|---|---|---|---|---|
| BLOCKED-CUR-HAF-001 | QJ1-P018 | Teks Hafalan 1, sumber, batas potongan, model bacaan, Hafalan Object-ID, pengesah | Pemilik Akademik + ahli | OPEN |
| BLOCKED-CUR-ARB-001 | QJ1-P001–P040/P028 | Validasi ahli atas model bahasa dan AR-SEN-000082–000096, model pelafalan, batas literasi, keputusan gerbang, Arabic Learning Object-ID, serta otorisasi | Pemilik Akademik + ahli Bahasa Arab | OPEN — PRODUK SIAP REVIEW |
| BLOCKED-CUR-ARB-002 | Jilid 1–8 | Validasi ACP-QUR-001 dan pemetaan Stage-ID/AR-LEX/AR-GRM/AR-FUN/AR-ASM ke jilid dan halaman | Pemilik Akademik + panel ahli | OPEN |
| BLOCKED-CUR-HAF-002 | QJ1-P036 | Teks Hafalan 2, sumber, batas potongan, model bacaan, Hafalan Object-ID, pengesah | Pemilik Akademik + ahli | OPEN |
| BLOCKED-ORTHO-QJ1-001 | QJ1-P033 | Verifikasi fungsi, penulisan, dan penyajian ءُ dalam urutan Jilid 1 | Ahli Bahasa Arab/Qira’at | OPEN |

## 1A. Substatus Blocker Bahasa Arab

| Komponen | Bukti | Status |
|---|---|---|
| baseline kosa kata Jilid 1 | 45 entri aktual; 40 target terhitung; turunan tidak dihitung ulang | COMPLETE-DRAFT |
| master kalimat | 96 Sentence-ID unik; 0 duplikasi | COMPLETE-DRAFT |
| struktur/fungsi | AR-GRM dan AR-FUN-000001–000008 terdaftar | COMPLETE-DRAFT |
| pemetaan halaman | MAP-ARB-QJ1-001; P001–P040 | COMPLETE-DRAFT |
| panduan guru lima menit | GDE-ARB-QJ1-001; 40 halaman | COMPLETE-DRAFT |
| penanaman sumber ke halaman | 40/40 memiliki Sentence-ID/Text-ID dan status; 0 hilang/duplikat | COMPLETE-DRAFT |
| audit keterlacakan | AUD-ARB-QJ1-002 | COMPLETE-DRAFT |
| paket ahli 15 kalimat | REV-ARB-QJ1-002; 15/15 PRECHECK-PASS | READY-FOR-EXPERT |
| keputusan ahli kalimat | 15/15 keputusan dan Evidence-ID | NOT PROVIDED |
| validasi 81 kalimat terdahulu dan tiga teks | bukti ahli bahasa/pedagogi/syar‘i | NOT PROVIDED |
| model pelafalan/audio resmi | sumber, pengisi suara, review, hak penggunaan | NOT PROVIDED |
| batas audiens sumber halaman | 40/40 segmen berlabel GURU dan bukan teks baca peserta; larangan tampil sebelum whitelist/editorial/render | COMPLETE-DRAFT |
| whitelist literasi silang dan render peserta | audit bentuk Arab guru versus unsur baca setiap halaman pada produk render final | OPEN |
| gerbang siklus | P010, P020, P028 | 0/3 SIAP; GATE NOT RUN |
| safeguarding dan uji durasi kelas | bukti pelaksanaan dan tindak lanjut | NOT PROVIDED |
| otorisasi akademik dan Document Controller | keputusan, tanggal, audit trail | NOT PROVIDED |

COMPLETE-DRAFT berarti artefak telah tersedia dan terlacak, bukan telah divalidasi atau disahkan. Karena unsur NOT PROVIDED dan OPEN masih material, BLOCKED-CUR-ARB-001/002 tetap OPEN.

## 2. Usulan Penutupan yang Tersedia

[PROP-CUR-QJ1-001](https://github.com/pesantrenriqa-boop/QURBATA/blob/feature/qj1-master-structure/quality/PROP-CUR-QJ1-001-Usulan-Materi-Khusus.md) telah menyiapkan rekomendasi terkontrol:

- P018: Surah Al-Fatihah ayat 1–3;
- P028: rekomendasi tema lama superseded parsial; MAP-ARB-QJ1-001 kini menyediakan pemetaan pilot P001–P040 dan kandidat AR-CYC-000003/AR-TXT-000001, tetapi belum divalidasi;
- P036: Surah Al-Fatihah ayat 4–7 disertai murojaah ayat 1–3.

Proposal belum mengikat dan tidak mengubah status blocker. Pemilik Akademik harus memilih, lalu ahli terkait memverifikasi sumber, teks, vokalisasi, pelafalan, beban, serta kelayakannya.

## 3. Gate Penelaahan

| Gate-ID | Cakupan hasil pindai | Bukti yang Dibutuhkan | Status |
|---|---:|---|---|
| GATE-ACA-QJ1 | 39 halaman menunggu pemeriksa akademik | Nama, tanggal, temuan, keputusan, tanda persetujuan | OPEN |
| GATE-EDT-QJ1 | 39 halaman menunggu pemeriksa editorial | Koreksi bahasa, konsistensi istilah, layout source | OPEN |
| GATE-RND-QJ1 | 37 halaman memiliki gate render | Render font Arab, spasi tidak tersambung, diakritik terbaca | OPEN |
| GATE-ASM-QJ1 | 38 halaman memerlukan telaah asesmen | Rubrik, bukti, aturan keputusan, bentuk paralel | OPEN |
| GATE-SAFE-QJ1 | 40 halaman memerlukan safeguarding | Beban, bahasa rahmah, penghentian aman, non-stigmatisasi | OPEN |
| GATE-AUTH-QJ1 | 38 halaman menunggu pengesah | Identitas otoritas dan keputusan eksplisit | OPEN |

Jumlah berasal dari audit metadata otomatis dan harus dikonfirmasi Document Controller saat review.

## 4. Gate Makro Keluar-Draft

| No. | Gate Makro | Status |
|---:|---|---|
| 1 | Struktur 40 halaman lengkap | COMPLETE |
| 2 | Audit otomatis distribusi dan whitelist | COMPLETE |
| 3 | Keputusan materi khusus | OPEN |
| 4 | Review akademik/Arab/Qira’at | OPEN |
| 5 | Review editorial dan render | OPEN |
| 6 | Validasi asesmen dan safeguarding | OPEN |
| 7 | Otorisasi serta audit trail persetujuan | OPEN |
| 8 | Penutupan seluruh blocker | OPEN |

Kesiapan keluar-Draft berbasis gate saat ini: **2 dari 8 gate makro selesai (25%)**. Angka ini bukan persentase efektivitas buku atau persentase keseluruhan proyek QURBATA.

## 5. Urutan Tindak Lanjut

1. Pemilik Akademik menetapkan materi Hafalan 1 dan Hafalan 2 serta memastikan ruang lingkup review Bahasa Arab.
2. Ahli Bahasa Arab mengisi REV-ARB-QJ1-002, menilai 81 kalimat terdahulu dan tiga teks, lalu mencatat Evidence-ID.
3. Ahli memverifikasi ءُ, model pelafalan, batas literasi, dan kandidat leksikal; editorial/render membuktikan bahwa naskah guru tidak bocor menjadi bacaan peserta.
4. Pemeriksa akademik menelaah urutan, bentuk, harakat, makhraj, dan beban.
5. Editorial serta render memeriksa seluruh sumber halaman.
6. Tim asesmen dan safeguarding mengesahkan rubrik serta kontrol peserta.
7. Document Controller mencatat bukti, versi, penutupan blocker, dan otorisasi.
8. PR baru dapat dipertimbangkan keluar dari Draft.

## 6. Riwayat

| Versi | Tanggal | Ringkasan |
|---|---|---|
| 0.6.0-id | 28 Juli 2026 | Menetapkan batas audiens guru pada 40/40 sumber halaman; audit whitelist produk render tetap terbuka |
| 0.5.0-id | 28 Juli 2026 | Memecah blocker Bahasa Arab menjadi substatus selesai-draf versus bukti/validasi yang masih terbuka |
| 0.4.0-id | 28 Juli 2026 | Menautkan pemetaan pilot Bahasa Arab tanpa menutup blocker |
| 0.3.0-id | 28 Juli 2026 | Menambahkan blocker validasi dan pemetaan Arabic Competency Progression |
| 0.2.0-id | 28 Juli 2026 | Menautkan usulan materi khusus tanpa menutup blocker |
| 0.1.0-id | 28 Juli 2026 | Register blocker dan gate pertama setelah struktur 40/40 selesai |

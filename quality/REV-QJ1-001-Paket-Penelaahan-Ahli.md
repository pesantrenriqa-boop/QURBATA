# REV-QJ1-001 — Paket Penelaahan Ahli Buku QURBATA Jilid 1

**Review-ID:** REV-QJ1-001  
**Status:** MENUNGGU PENELAAHAN  
**Tanggal disiapkan:** 28 Juli 2026  
**Cakupan:** QJ1-P001–QJ1-P040 pada PR #2  
**Pengendali:** QC-000, CUR-QJ1-001, DEC-CUR-002, QJ1-MASTER  
**Bukti pendamping:** AUD-QJ1-001 dan BLK-QJ1-001

## 1. Aturan Penelaahan

1. Setiap keputusan harus mencantumkan nama, peran, tanggal, cakupan, temuan, dan keputusan.
2. Keputusan yang tersedia: `DISETUJUI`, `DISETUJUI DENGAN KOREKSI`, atau `DITOLAK`.
3. Satu temuan material menghasilkan tindak lanjut bernomor dan tidak boleh ditutup tanpa bukti.
4. Audit otomatis hanya membuktikan struktur, hitungan, distribusi, dan whitelist; audit itu bukan fatwa, tashih, atau validasi pedagogis.
5. PR tetap Draft sampai seluruh gate pada BLK-QJ1-001 ditutup.

## 2. Penelaahan Bahasa Arab/Qira’at

| Pemeriksaan | Bukti yang dicatat | Keputusan |
|---|---|---|
| Bentuk dan nama 29 identitas huruf | Daftar koreksi per halaman | MENUNGGU |
| Fathah, kasrah, dan dhammah | Koreksi bentuk, posisi, dan bunyi | MENUNGGU |
| `ءَ/ءِ/ءُ` dan `أَ/إِ/أُ` | Keputusan eksplisit atas fungsi dan penyajian | MENUNGGU |
| Makhraj dan pasangan huruf rawan | Catatan ahli dan model pelafalan | MENUNGGU |
| Bunyi pendek versus mad | Konfirmasi tidak ada pengenalan prematur | MENUNGGU |
| Kandidat tiga huruf dekat akar Qurani/Arab | Validasi bentuk, makna, dan batas klaim | MENUNGGU |
| Larangan bentuk sambung/materi prematur | Daftar pelanggaran atau pernyataan nihil | MENUNGGU |

### Keputusan wajib BLOCKED-ORTHO-QJ1-001

Ahli harus memilih salah satu:

- `PERTAHANKAN ءُ` dengan dasar keilmuan dan pedoman penyajian;
- `UBAH` dengan bentuk pengganti serta dampak ke seluruh halaman;
- `TUNDA` dengan batas cakupan dan rencana remediasi.

## 3. Penelaahan Akademik dan Kurikulum

| Pemeriksaan | Bukti yang dicatat | Keputusan |
|---|---|---|
| Urutan pengenalan huruf dan harakat | Catatan per fase/halaman | MENUNGGU |
| Murojaah kumulatif merata | Konfirmasi kesesuaian DEC-CUR-002 | MENUNGGU |
| Beban 24 tangga/64 token | Penilaian usia, durasi, dan kelelahan | MENUNGGU |
| Satu halaman per pertemuan | Kondisi remedial dan pengecualian | MENUNGGU |
| Outcome–LO–KO–asesmen | Temuan keterlacakan | MENUNGGU |
| Kandidat leksikal | Kesesuaian pedagogis tanpa memalsukan kata | MENUNGGU |
| Halaman khusus | Kesesuaian posisi P018, P028, P036, P038 | MENUNGGU |

## 4. Keputusan Materi Khusus

### QJ1-P018 — Hafalan 1

Wajib ditetapkan: teks, sumber, batas potongan, tujuan, model bacaan, Hafalan Object-ID, pemilik akademik, dan pengesah.

### QJ1-P028 — Bahasa Arab 1

Wajib ditetapkan: tema, tujuan komunikatif, mufradat, vokalisasi, makna, konteks, model pelafalan, Arabic Learning Object-ID, ahli Bahasa Arab, dan pengesah.

### QJ1-P036 — Hafalan 2

Wajib ditetapkan: teks, sumber, batas potongan, hubungan dengan Hafalan 1, model bacaan, Hafalan Object-ID, pemilik akademik, dan pengesah.

Keputusan atas ketiga materi harus mempunyai Decision-ID tersendiri dan tidak boleh diinferensikan dari persetujuan umum buku.

## 5. Penelaahan Editorial dan Render

| Pemeriksaan | Kriteria lulus | Keputusan |
|---|---|---|
| Istilah dan metadata | Konsisten pada 40 halaman | MENUNGGU |
| Font Arab dan diakritik | Terbaca pada ukuran cetak sasaran | MENUNGGU |
| Huruf terpisah | Tidak tersambung akibat shaping/render | MENUNGGU |
| Arah teks | RTL/LTR tidak mengubah urutan latihan | MENUNGGU |
| Nomor dan tangga | 24 tangga tampil lengkap dan berurutan | MENUNGGU |
| Cetak dan layar | Tidak ada clipping, fallback, atau glyph hilang | MENUNGGU |
| Aksesibilitas | Kontras, ukuran, dan instruksi memadai | MENUNGGU |

Bukti minimal: hasil render PDF/PNG pada lingkungan sasaran, daftar font, ukuran cetak, dan sampel pemeriksaan setiap halaman.

## 6. Asesmen dan Safeguarding

| Pemeriksaan | Kriteria lulus | Keputusan |
|---|---|---|
| Rubrik | Konstruk, indikator, dan pencatatan jelas | MENUNGGU |
| Ambang keputusan | Tidak ditetapkan tanpa dasar validasi | MENUNGGU |
| Bentuk paralel | Cakupan setara dan terdokumentasi | MENUNGGU |
| Remedial | Mengarah ke prasyarat penyebab kesalahan | MENUNGGU |
| Bahasa rahmah | Tidak mempermalukan atau memberi stigma | MENUNGGU |
| Beban peserta | Ada jeda dan penghentian aman | MENUNGGU |
| Data/bukti | Minimal, relevan, dan terlindungi | MENUNGGU |

## 7. Lembar Keputusan

| Peran | Nama | Cakupan | Keputusan | Tanggal | Bukti/Temuan |
|---|---|---|---|---|---|
| Ahli Bahasa Arab/Qira’at |  |  |  |  |  |
| Pemilik Akademik |  |  |  |  |  |
| Editor |  |  |  |  |  |
| Pemeriksa Render |  |  |  |  |  |
| Penelaah Asesmen |  |  |  |  |  |
| Penelaah Safeguarding |  |  |  |  |  |
| Document Controller |  |  |  |  |  |
| Otoritas Persetujuan |  |  |  |  |  |

## 8. Syarat Penutupan

Paket ini selesai hanya jika:

- seluruh baris keputusan terisi;
- seluruh koreksi sudah diterapkan dan diverifikasi ulang;
- tiga keputusan materi khusus mempunyai Decision-ID;
- BLOCKED-ORTHO-QJ1-001 ditutup dengan keputusan ahli;
- semua bukti ditautkan;
- BLK-QJ1-001 menunjukkan delapan gate makro COMPLETE;
- otoritas persetujuan secara eksplisit mengizinkan PR keluar dari Draft.

## 9. Riwayat

| Versi | Tanggal | Ringkasan |
|---|---|---|
| 0.1.0-id | 28 Juli 2026 | Paket penelaahan ahli pertama untuk QJ1-P001–P040 |

# QWO Production Status V1

Tanggal pembaruan: 4 Agustus 2026

## Hasil produksi
- Candidate pool A-001: 90 objek
- Candidate pool A-002: 120 objek
- Total kandidat competency-first: 210 objek
- Corpus surah-first: 0 objek aktif
- QWO aktif: 0 objek
- Status umum: CANDIDATE

## Cakupan kompetensi yang sudah diproduksi
- Sambungan tiga huruf
- Transisi huruf non-connector
- Hamzah qatha
- Alif maqshurah
- Sukun dasar
- Sukun ain dan ghain
- Sukun huruf tebal
- Tasydid
- Mad alif
- Mad ya
- Mad wawu
- Tanwin fathah
- Tanwin kasrah
- Tanwin dhammah
- Alif lam
- Ta marbuthah

## Gate validasi
1. Verifikasi kandidat terhadap teks mushaf.
2. Isi SourceRef surah:ayat.
3. Normalisasi bentuk Utsmani dan bentuk pencarian.
4. Audit TargetCompetency dan SecondaryCompetencies.
5. Tandai duplikasi bentuk dan keluarga morfologi.
6. Promosikan kandidat lolos menjadi SOURCE_VERIFIED.
7. Promosikan kandidat tervalidasi pedagogis menjadi ACTIVE.

## Target gelombang selanjutnya
- Naikkan total menjadi minimal 350 kandidat.
- Tambahkan keluarga visual huruf yang belum terwakili.
- Tambahkan pola mad dan sukun yang lebih beragam.
- Mulai verifikasi sumber untuk 100 kandidat prioritas tertinggi.
- Setelah minimal 100 QWO ACTIVE tersedia, mulai produksi QPO frasa dua kata.

## Catatan kualitas
Candidate pool adalah area produksi cepat, bukan data final generator. Kandidat yang bentuknya meragukan atau memerlukan verifikasi khusus tetap dipertahankan sebagai CANDIDATE dengan prioritas REVIEW dan tidak boleh digunakan oleh generator.
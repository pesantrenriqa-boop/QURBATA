# QWO Large Production Plan V1

## Tujuan
Mempercepat produksi MASTER_QWO secara besar tanpa mengulangi kesalahan pendekatan surah-first.

## Prinsip wajib
1. Produksi dimulai dari QCI/kompetensi.
2. Surah dan ayat hanya metadata sumber.
3. Candidate Pool tidak otomatis menjadi QWO aktif.
4. Aktivasi memerlukan validasi teks, sumber ayat, morfologi, dan dependency QCI.
5. Al-Fatihah tidak digunakan sebagai corpus awal default.

## Pipeline produksi
CANDIDATE -> SOURCE_VERIFIED -> QCI_MAPPED -> PEDAGOGY_REVIEWED -> ACTIVE

## Target batch
- Gelombang A: 100 kandidat dasar
- Gelombang B: 250 kandidat mad dan tanwin
- Gelombang C: 500 kandidat sukun, tasydid, dan struktur
- Gelombang D: 1.000 kandidat frasa-ready

## Aturan kelulusan
Objek hanya boleh berstatus ACTIVE apabila:
- ArabicWord terverifikasi;
- SourceRef terisi;
- TargetCompetency valid;
- RequiredCompetencies lengkap;
- tidak melampaui whitelist level;
- lolos pemeriksaan pedagogis.

## Mode produksi
Candidate pool boleh diproduksi cepat dalam jumlah besar. Aktivasi tetap dilakukan berlapis agar kesalahan tidak masuk generator.
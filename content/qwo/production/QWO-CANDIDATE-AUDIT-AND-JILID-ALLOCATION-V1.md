# QWO Candidate Audit and Jilid Allocation V1

Tanggal: 4 Agustus 2026
Status: CANDIDATE ALLOCATION — belum menjadi halaman final

## Hasil

- Corpus: 6.236 ayat.
- Token occurrence: 77.881.
- Lexeme unik: 18.818.
- Kandidat diaudit: 2.500 objek unik.
- Alokasi awal: 300 objek per Jilid 1–8.
- Cadangan: 100 objek.
- Pengulangan CanonicalKey: 0.
- Semua sumber dapat ditelusuri ke surah, ayat, dan token.

## Koreksi penting

Mapper V1 memakai pola `ُو` untuk mad wawu tanpa memastikan bahwa huruf waw tidak berharakat. Akibatnya kata seperti `هُوَ` dapat salah diberi label MAD_WAWU.

Mapper V2 memperbaiki aturan:
- mad wawu: dhammah diikuti waw yang tidak membawa harakat pendek, tanwin, atau tasydid;
- mad ya: kasrah diikuti ya yang tidak membawa harakat pendek, tanwin, atau tasydid;
- mad alif: fathah diikuti alif tanpa harakat pendek, atau alif khanjariyah yang eksplisit.

Contoh kontrol:
- `هُوَ` bukan MAD_WAWU;
- `فِيهِ` dapat menjadi MAD_YA;
- bentuk Utsmani asli tidak diubah.

## Prinsip alokasi

Alokasi memakai skor kesulitan teknis agar objek bergerak dari bentuk pendek dan sambungan dasar menuju kombinasi fitur yang lebih kompleks. Ini adalah pool bahan per jilid, bukan keputusan halaman final.

Setiap jilid memperoleh 300 objek berbeda. Kompetensi boleh berulang, tetapi objek `CanonicalKey` tidak berulang di seluruh delapan jilid.

## Gate berikutnya

1. Audit sampel per kompetensi.
2. Cocokkan pool dengan tangga materi resmi setiap jilid.
3. Pilih objek untuk setiap halaman.
4. Tandai `Consumed = TRUE` setelah objek ditempatkan.
5. Jangan menggunakan objek cadangan kecuali diperlukan untuk mengganti objek yang ditolak.

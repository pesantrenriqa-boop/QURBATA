# QJ1 — Register Sumber Recovery

**Status:** ACTIVE  
**Induk:** `books/RECOVERY-CONSOLIDATION-INDEX-JILID-1-3.md`

## Sumber Utama

- Master struktur dan isi sampai P040: commit `c820ca4c0504185bf5e63d7765089fbd7c4b4e2b`.
- Kontrol freeze: `books/jilid-1/QJ1-FREEZE.md`.
- Halaman kanonik: `books/jilid-1/pages/QJ1-P001.md` sampai `QJ1-P040.md`.
- Sumber pembanding recovery P001: `03_BOOKS/JILID-1/PAGE-001.md`.

## Status

| Rentang | Status | Tindakan |
|---|---|---|
| P001 | SOURCE-VERIFIED | Urutan 64 token cocok dengan sumber recovery dan telah dibentuk menjadi 24 tangga. Bersihkan rujukan aturan 60:40 yang sudah tidak berlaku. |
| P002 | SOURCE-VERIFIED-WITH-GATE | Versi 0.4.0-id pada commit `b43a8b2d1fc67f893bad2e7bd987850d70eaf514` memiliki 24 tangga, 64 token, whitelist ءَ أَ بَ تَ ثَ, dan pemerataan 12–13 token per identitas. Terminologi serta penyajian ءَ/أَ tetap menunggu verifikasi ahli. |
| P003 | SOURCE-CONFLICT | Kandidat pemerataan mutlak: `91ad43999a26f594c1134271c02b827e93c8cc8c`. Kandidat 60:40 yang lebih baru: `50929c460774677b5e9170f143ce0ce7b41b2771`. Jangan freeze sebelum kebijakan distribusi final diterapkan konsisten. |
| P004 | SOURCE-CONFLICT | Kandidat pemerataan mutlak: `2e43a5007167489ab95d1c4f6c9bc952266bf339`; kandidat 60:40: `a614a6f580216de9f3109770d595d629093a681d`. |
| P005 | SOURCE-CONFLICT | Kandidat pemerataan mutlak: `f28841bb4a6d030e26cbc8b635bf3ab244c5e5d3`; kandidat 60:40: `5e7830447b565cc5e90460a277d133b5accc59a5`. |
| P006 | SOURCE-CONFLICT | Kandidat pemerataan mutlak: `c53d05d95322c8a8323b60619e4b7963d251b622`; kandidat 60:40: `72bbda5baf58bfcf7fe0018f7fcf6c1d0e418211`. |
| P007 | SOURCE-CONFLICT | Kandidat pemerataan mutlak: `7f26989703cde92885f0a8912a1cec0963e6fa5a`; kandidat 60:40: `dd445dff273da1ce9e540d5d10f6ec3d8eb5e9af`. |
| P008 | SOURCE-CONFLICT | Kandidat pemerataan mutlak: `b07079871dcfb3eef4adc5d9a4cf5846b79d43be`; kandidat 60:40: `b81d940d52cf904c1a9726ebce2fecf79a675659`. |
| P009 | SOURCE-CONFLICT | Kandidat pemerataan mutlak: `0808c66741663bbd97b6b4c4050672067da59566`; kandidat 60:40: `7b1f9c7f354af22a232dd8548e5bb818c065d203`. |
| P010 | SOURCE-VERIFIED-ASSESSMENT-WITH-GATE | Evaluasi fathah 100% review. Kandidat pemerataan/evaluasi: `dc6274030f1170a925454c54272b41e72b30843a`; audit batch: `8bbc21dad83411a370aebf55075d3650df0d6ea6`. Tidak mengenalkan materi baru. |
| P011 | SOURCE-CONFLICT | Versi pemerataan mutlak ada pada `49001706739cad87be4d80e2eef62dd36f513e0c`; versi 60:40 diregenerasi pada `5a7829e17b3a1087e1969bf6e54013cf7023a33a` dan diperbaiki jumlah token/keunikan pada `a550d80b2332ec7af25f052c18f6fcb90a3f0906`. File kanonik main saat ini v0.5.1-id memakai 39 token baru dan 25 review; jangan freeze sebelum kebijakan distribusi final diputuskan. |
| P012–P013 | FOUND-POLICY-CONFLICT | Halaman akuisisi fathah keluarga Mim–Nun serta Ha–Waw–Ya. Audit harus membandingkan garis pemerataan kumulatif dengan regenerasi dominasi materi baru; whitelist hanya fathah dan huruf yang telah sah. |
| P014–P015 | FOUND-INTEGRATION-REVIEW | Halaman penguatan seluruh fathah dan otomatisasi, bukan akuisisi keluarga baru. Wajib 100% mengambil unsur sah P001–P013; tidak boleh memakai rasio materi baru 60:40 karena tidak ada materi huruf baru. |
| P016–P017 | FOUND-POLICY-CONFLICT | Awal kasrah dan keluarga tenggorokan. Perlu memisahkan token kasrah baru dari review fathah serta memastikan tidak ada dhammah, mad, tanwin, sukun, tasydid, atau teks melampaui whitelist. |
| P018 | FOUND-HAFALAN-CANDIDATE-BLOCKED | Unit Hafalan 1, kandidat Al-Fatihah ayat 1–3, berstatus `APPROVED-CANDIDATE-INACTIVE`. Aturan 24 tangga/token tidak berlaku. Belum boleh aktif sebelum validasi qiraah, rasm, tajwid, waqaf-ibtida’, pembagian potongan, model audio, asesmen, dan safeguarding. |
| P019 | FOUND-POLICY-CONFLICT | Halaman kasrah ujung lidah. Perlu audit distribusi kasrah baru versus review kasrah/fathah sebelumnya serta verifikasi whitelist. |
| P020 | FOUND-ASSESSMENT-WITH-GATE | Evaluasi fathah–kasrah dan checkpoint lisan nama huruf. Tidak boleh mengenalkan materi baca baru; panel nama huruf harus dipisahkan dari skor kemampuan membaca. |
| P021–P040 | FOUND-UNASSESSED | Verifikasi isi contoh satu per satu terhadap master, whitelist, progression, dan versi terakhir yang tidak superseded/invalid. |

## Catatan Audit P002

- Pola halaman: tangga 1–8 masing-masing dua huruf; tangga 9–24 masing-masing tiga huruf.
- Total: 64 token.
- Tidak ditemukan mad, tanwin, sukun, tasydid, bentuk sambung, atau rangkaian lebih dari tiga huruf dalam sumber latihan.
- Status `SOURCE-VERIFIED-WITH-GATE` bukan berarti siap cetak; render, makhraj, metadata ahli, dan safeguarding masih terbuka.

## Konflik Kebijakan P003–P009 dan P011

Halaman-halaman tersebut mempunyai dua garis sumber yang sama-sama pernah dinyatakan sah pada tahapnya:

1. versi pemerataan mutlak seluruh identitas yang sudah dipelajari sesuai DEC-CUR-002;
2. versi regenerasi berikutnya dengan 39 token materi baru dan 25 token review, sekitar 60:40.

Audit distribusi draf tidak otomatis menjadikan versi 60:40 sebagai sumber final. Keputusan proyek terbaru tentang murojaah kumulatif dan rasio halaman harus menjadi dasar tunggal sebelum freeze.

## Catatan P010

- P010 adalah evaluasi, bukan halaman akuisisi.
- Seluruh sampel berasal dari materi fathah P001–P009.
- Status audit lama: `PASS-DRAFT-ASSESSMENT`.
- Render, verifikasi ahli, rubrik keputusan, safeguarding, pilot, Evidence-ID, dan Decision-ID masih terbuka.

## Catatan Batch P011–P020

- P011–P013 menutup seluruh keluarga fathah.
- P014–P015 adalah penguatan dan otomatisasi; keduanya tidak memiliki materi huruf baru.
- P016–P017 dan P019 merupakan tahap kasrah.
- P018 adalah unit hafalan lisan, sehingga tidak boleh dipaksa mengikuti format 24 tangga latihan baca.
- P020 adalah evaluasi dua harakat plus checkpoint nama huruf lisan; kedua hasil harus dicatat terpisah.
- Segmen Bahasa Arab guru, hafalan, nama huruf, dan latihan baca harus tetap menjadi bidang data terpisah agar turunan buku/aplikasi tidak mencampur fungsi.

## Larangan

- Jangan membuat contoh baru untuk menggantikan isi recovery sebelum audit selesai.
- Jangan memakai file PDF/slide sebagai sumber mandiri.
- Jangan memilih versi hanya berdasarkan tanggal commit; status superseded, keputusan kurikulum, whitelist, dan konsistensi lintas halaman lebih tinggi prioritasnya.
- Jangan menyatakan Jilid 1 selesai recovery hanya berdasarkan keberadaan struktur 40 halaman.

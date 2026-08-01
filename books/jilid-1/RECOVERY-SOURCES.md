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
| P011–P040 | FOUND-UNASSESSED | Verifikasi isi contoh satu per satu terhadap master, whitelist, progression, dan versi terakhir yang tidak superseded/invalid. |

## Catatan Audit P002

- Pola halaman: tangga 1–8 masing-masing dua huruf; tangga 9–24 masing-masing tiga huruf.
- Total: 64 token.
- Tidak ditemukan mad, tanwin, sukun, tasydid, bentuk sambung, atau rangkaian lebih dari tiga huruf dalam sumber latihan.
- Status `SOURCE-VERIFIED-WITH-GATE` bukan berarti siap cetak; render, makhraj, metadata ahli, dan safeguarding masih terbuka.

## Konflik Kebijakan P003–P009

Setiap halaman P003–P009 mempunyai dua garis sumber yang sama-sama pernah dinyatakan sah pada tahapnya:

1. versi pemerataan mutlak seluruh identitas yang sudah dipelajari sesuai DEC-CUR-002;
2. versi regenerasi berikutnya dengan 39 token materi baru dan 25 token review, sekitar 60:40.

Audit `AUD-QJ1-CONTENT-002` menyatakan batch 60:40 lulus audit distribusi draf, tetapi audit tersebut juga menegaskan bahwa batch belum siap uji lapangan. Karena keputusan proyek berikutnya mengarah pada murojaah kumulatif 50:50, audit 60:40 tidak otomatis menjadikan versi tersebut sumber final.

## Catatan P010

- P010 adalah evaluasi, bukan halaman akuisisi.
- Seluruh sampel berasal dari materi fathah P001–P009.
- Status audit lama: `PASS-DRAFT-ASSESSMENT`.
- Render, verifikasi ahli, rubrik keputusan, safeguarding, pilot, Evidence-ID, dan Decision-ID masih terbuka.

## Larangan

- Jangan membuat contoh baru untuk menggantikan isi recovery sebelum audit selesai.
- Jangan memakai file PDF/slide sebagai sumber mandiri.
- Jangan memilih versi hanya berdasarkan tanggal commit; status superseded, keputusan kurikulum, whitelist, dan konsistensi lintas halaman lebih tinggi prioritasnya.
- Jangan menyatakan Jilid 1 selesai recovery hanya berdasarkan keberadaan struktur 40 halaman.

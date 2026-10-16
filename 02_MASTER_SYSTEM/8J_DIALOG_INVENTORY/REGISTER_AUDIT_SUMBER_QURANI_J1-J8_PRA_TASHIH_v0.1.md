# REGISTER AUDIT SUMBER QURANI J1–J8 — PRA-TASHIH v0.1

**STATUS: REGISTER KERJA, BELUM TASHIH MUSHAF.** Menindaklanjuti kebijakan `KEBIJAKAN_SUMBER_QURANI_KATA_FRASA_KALIMAT_J1-J8_v1.0.md`. Lingkup 8 jilid × 40 halaman = 320 halaman. Dokumen ini bukan bukti bahwa 320 halaman sudah diaudit satu per satu.

## Aturan penerimaan
- `LETTER_CARD`: huruf/harakat terisolasi, jelas diberi label peraga dan tidak diklaim kata Qurani.
- `WORD`: wajib bukti satu kata yang terdapat dalam ayat tertentu; rekam teks tepat sesuai mushaf.
- `PHRASE` / `SENTENCE`: wajib penggalan **berurutan** dalam ayat tertentu; catat posisi awal–akhir.
- `DIALOG`: Bahasa Arab interaktif buatan guru diperbolehkan **hanya** di jalur Bi'ah, tidak boleh disisipkan sebagai bacaan Tartil Qurani.
- `REJECT`: gabungan kata buatan, kata tanpa surah-ayat, atau bentuk imlai yang diklaim identik rasm Utsmani tanpa tashih.

## Daftar prioritas audit yang teridentifikasi
| Lokasi | Temuan dari paket sebelumnya | Tindakan | Status |
|---|---|---|---|
| J2 P001–P020 | Kartu bentuk huruf terisolasi dan fragmen sambung | Tetap sebagai peraga, jangan diberi label kata Qurani | ALLOWED-CARD / FONT-QA |
| J2 P021–P024 | Tanwin pada huruf tunggal | Peraga tanda saja; latihan kata harus diganti kata utuh Qurani yang ditashih | NEEDS-REPLACEMENT |
| J2 P025–P028 | Pasangan bunyi pendek–panjang buatan | Peraga fonetik sementara; grid kata harus dari Al-Qur'an | NEEDS-REPLACEMENT |
| J2 P029 | Kandidat قَالَ / كَانَ / مَالِكِ | Verifikasi mushaf primer, rasm, lokasi dan harakat; jangan cetak kandidat langsung | CANDIDATE-QURAN |
| J2 P030–P038 | Suku kata fonetik buatan untuk mad | Peraga bunyi saja; setiap kata utuh yang masuk grid harus Qurani | NEEDS-REPLACEMENT |
| J2 P039–P040 | Integrasi dan evaluasi dengan kartu | Butir evaluasi berbentuk kata/frasa wajib dari Al-Qur'an | NEEDS-REPLACEMENT |
| J1 dan J3–J8 | Ada inventaris dan draf terdahulu, belum diekstrak menjadi daftar setiap kata/frasa | Ekstraksi per halaman dan pencocokan mushaf | NOT-AUDITED |

## Skema baris evidence bank
`jilid | halaman | competence | unit_type | arabic_exact | surah | ayah | span_start | span_end | mushaf_edition | rasm_status | harakat_status | font_status | reviewer | verdict`

Verdict hanya `CARD-ONLY`, `CANDIDATE-QURAN`, `VERIFIED-QURAN`, atau `REJECT`. `VERIFIED-QURAN` memerlukan bukti edisi mushaf, lokasi dan tanda tangan tashih. Tidak boleh mengubah status hanya karena kata terlihat umum dalam Al-Qur'an.

## Gate lanjutan
1. Ekstraksi seluruh contoh kata/frasa dari materi J1–J8; hitung dan temukan yang tidak punya sumber.
2. Cocokkan setiap unit dengan mushaf rujukan dan simpan bukti surah, ayat, span.
3. Audit ortografi rasm, harakat, mad, tanda waqaf, font KFGQPC Uthman Taha.
4. Perbaiki contoh yang gagal, tanpa mengubah crosswalk Tahfidz FROZEN.
5. Luluskan halaman hanya setelah seluruh empat inventaris dan QA integrasi terpenuhi.

**Status aktual:** kebijakan diberlakukan, register awal dibuat; **0/320 halaman dinyatakan lulus audit sumber Qurani melalui register ini**.

QURBATA Jilid 1 — Revisi Leksikal Fathah P011–P015 v0.1
Status: DRAF REVIEW; Blueprint v1.0 FROZEN.

P011 كَ لَ
Dengan ك/ل, bank menjadi jauh lebih natural. Kandidat prioritas: كَ تَ بَ (كتب), أَ كَ لَ (أكل), شَ كَ رَ (شكر), خَ لَ قَ (خلق), جَ عَ لَ (جعل), دَ خَ لَ (دخل), سَ لَ كَ (سلك). Target ك/ل tetap dominan 39 token; pola aktual dipilih hanya jika membantu target.

P012 مَ نَ
Kandidat kuat: حَ مَ دَ (حمد), رَ حَ مَ (رحم), عَ مَ لَ (عمل), مَ لَ كَ (ملك), نَ صَ رَ (نصر), مَ نَ عَ (منع), نَ فَ عَ (نفع), أَ مَ نَ (أمن), سَ مَ عَ (سمع), جَ مَ عَ (جمع). P012 seharusnya mulai terasa sangat Arab/Qurani, tetapi م/ن tetap materi fokus.

P013 هَ وَ يَ
Alfabet fathah praktis lengkap. Kandidat: هَ دَ يَ (هدي), وَ عَ دَ (وعد), وَ جَ دَ (وجد), وَ هَ بَ (وهب), يَ سَ رَ (يسر), هَ لَ كَ (هلك), هَ جَ رَ (هجر), وَ قَ عَ (وقع). Kontrol khusus: وَ tetap pendek, bukan mad.

P014 INTEGRASI SELURUH FATHAH
Karena seluruh inventori tersedia, halaman ini menjadi titik utama 'rasa Arab/Qurani'. Rekomendasi 16 tangga tiga-huruf: حَ مَ دَ | رَ حَ مَ | ذَ كَ رَ | سَ جَ دَ | شَ كَ رَ | صَ بَ رَ | عَ بَ دَ | عَ مَ لَ | غَ فَ رَ | فَ تَ حَ | قَ رَ أَ | كَ تَ بَ | نَ صَ رَ | هَ دَ يَ | وَ عَ دَ | يَ سَ رَ. Delapan tangga dua-huruf tetap untuk kontras visual/makhraj dan pemerataan 29 identitas. Audit distribusi wajib sebelum mengganti master.

P015 OTOMATISASI FATHAH
Jangan mengulang urutan P014 seluruhnya. Gunakan campuran kata/pola Arab aktual + CONTROLLED baru untuk menguji transfer. Kandidat rotasi leksikal: خَ لَ قَ | جَ عَ لَ | دَ خَ لَ | أَ كَ لَ | سَ مَ عَ | جَ مَ عَ | مَ نَ عَ | نَ فَ عَ | وَ جَ دَ | وَ هَ بَ | وَ قَ عَ | هَ جَ رَ. Sisanya controlled, terutama keluarga huruf yang rawan tertukar.

CATATAN AKADEMIK
- Bentuk seperti حَ مَ دَ, ذَ كَ رَ, سَ جَ دَ, شَ كَ رَ, صَ بَ رَ, عَ بَ دَ, غَ فَ رَ, فَ تَ حَ, قَ رَ أَ, كَ تَ بَ, نَ صَ رَ dan lainnya harus melalui verifikasi morfologi/vokalisasi sebelum tag AR-WORD/QURAN final.
- 'Rasa Qurani' tidak berarti semua item harus diberi label ayat. Banyak item cukup AR-WORD/AR-ROOT meski akarnya sangat sering dalam Al-Qur'an.
- QURAN/HADITH hanya diberikan jika token benar-benar cocok dengan bentuk sumber yang tervalidasi.

GATE FASE FATHAH
1. P001–P015 selesai kurasi konseptual.
2. Berikutnya: audit token 64 per halaman dan rasio 39:25 untuk halaman akuisisi.
3. Validasi AR-WORD/QURAN/HADITH.
4. Baru terapkan daftar final ke master halaman dan data Vivliostyle.
5. Render sampel P001, P005, P010, P014, P015 untuk review visual sebelum masuk kasrah.

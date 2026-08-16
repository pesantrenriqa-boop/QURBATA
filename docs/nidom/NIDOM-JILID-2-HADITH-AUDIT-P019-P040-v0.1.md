# QURBATA NIDOM Jilid 2 — Hadith Content Audit P019–P040 v0.1

Status: PRE-FREEZE CONTENT AUDIT
Scope: P019–P040
Rule: tema boleh spiral/berulang; matan utama tidak boleh diulang monoton; setiap kutipan harus dilabeli bila hanya potongan dari hadits lebih panjang.

## P019–P020 — Checkpoint I
- Tidak perlu menambah hadits baru sebagai materi utama.
- Gunakan checkpoint kumulatif P001–P018.
- Bila hadits dikutip dalam soal, label: `potongan hadits yang telah dipelajari`.
- PASS pedagogi: evaluasi tanpa menambah beban hafalan baru.

## P021–P024 — Rahmah
- P021 `مَنْ لَا يَرْحَمْ لَا يُرْحَمْ` — gunakan sebagai matan ringkas tema rahmah.
- P022 `الرَّاحِمُونَ يَرْحَمُهُمُ الرَّحْمَنُ` — redaksi berbeda, tema sama.
- P023 `ارْحَمُوا مَنْ فِي الْأَرْضِ ...` — harus dipahami sebagai kelanjutan/segmen dari hadits rahmah; jangan memberi kesan sebagai riwayat terpisah bila sumbernya sama dengan P022.
- P024 `إِنَّمَا يَرْحَمُ اللَّهُ مِنْ عِبَادِهِ الرُّحَمَاءَ` — tema sama dengan sudut pandang berbeda.
- Kamus wajib mengikuti matan aktual per halaman.

## P025–P028 — Amanah & Tanggung Jawab
- P025 `أَدِّ الْأَمَانَةَ إِلَى مَنِ ائْتَمَنَكَ` — cocok untuk tindakan konkret menjaga amanah.
- P026 `وَإِذَا اؤْتُمِنَ خَانَ` — label wajib: `potongan hadits tanda-tanda kemunafikan`, bukan hadits mandiri.
- P027 `كُلُّكُمْ رَاعٍ وَكُلُّكُمْ مَسْئُولٌ عَنْ رَعِيَّتِهِ` — cocok untuk memperluas amanah menjadi tanggung jawab.
- P028 `آيَةُ الْمُنَافِقِ ثَلَاثٌ` — jika dipakai, hubungkan eksplisit dengan P026 dan jangan dijadikan ancaman moral yang terlalu berat bagi anak; fokus pada perilaku yang harus diperbaiki.

## P029–P032 — Hormat, Izin, Adab
- P029 hadits menyayangi yang muda/menghormati yang tua — cocok sebagai jangkar.
- P030 hadits memuliakan Muslim yang telah berusia — gunakan untuk perluasan adab menghormati.
- P031 `الْبِرُّ حُسْنُ الْخُلُقِ` — cocok sebagai generalisasi akhlak baik.
- P032 `خَيْرُكُمْ أَحْسَنُكُمْ أَخْلَاقًا` — cocok sebagai refleksi kualitas akhlak.
- Tugas harus konkret: mendengar sampai selesai, meminta izin, menjawab panggilan, menerima nasihat.

## P033–P035 — Menolong dengan Benar
- P033 `وَاللَّهُ فِي عَوْنِ الْعَبْدِ مَا كَانَ الْعَبْدُ فِي عَوْنِ أَخِيهِ` — VERIFIED sebagai bagian Sahih Muslim 2699a.
- Sumber canonical: Sahih Muslim 2699a; label PDF sebaiknya `HR. Muslim 2699a (potongan hadits)`.
- P034 dapat memakai segmen lain dari hadits yang sama: `مَنْ نَفَّسَ عَنْ مُؤْمِنٍ كُرْبَةً ...` tetapi harus dilabeli `potongan hadits` dan jangan dianggap riwayat baru.
- P035 sebaiknya menjadi misi/praktik menolong, tidak perlu memaksakan hadits ketiga bila tujuan halaman adalah transfer perilaku.
- Prinsip: bantuan yang benar menguatkan kebaikan, bukan membantu menyontek/berbuat salah.

## P036 — Quiz Akhir
- Tidak ada hadits baru.
- Delapan kompetensi: ramah/salam, lisan, sabar, jujur, rahmah, amanah, hormat, menolong benar.
- Soal campuran: identifikasi, pilihan tindakan, alasan sederhana.

## P037 — Penalaran Akhir
- Tidak ada hadits baru.
- Empat kasus lintas kompetensi.
- Format jawaban: `tindakan → alasan → akibat`.

## P038 — Stasiun Praktik
- Tidak ada hadits baru.
- Enam demonstrasi perilaku.
- Guru menilai performa, bukan kemampuan menghafal redaksi.

## P039 — Jejak Kebiasaan
- Tidak ada hadits baru.
- Rating tiga tingkat: mandiri / masih diingatkan / perlu latihan.
- Penilai: anak + guru + orang tua/wali.

## P040 — Rapor NIDOM Jilid 2
- Tidak ada hadits baru.
- Rekap delapan kompetensi + satu target kebiasaan menuju Jilid 3.
- Tidak menambah konsep baru pada halaman rapor.

## Audit decisions
1. P019–P020 dan P036–P040 tidak perlu hadits baru.
2. P023 harus dilabeli sebagai bagian/kelanjutan riwayat yang sama dengan P022 bila menggunakan Tirmidzi 1924.
3. P026 wajib berlabel potongan hadits tanda-tanda kemunafikan.
4. P028 harus disajikan secara pedagogis: evaluasi perilaku, bukan memberi label anak sebagai munafik.
5. P033 diverifikasi sebagai potongan Sahih Muslim 2699a.
6. P034 bila menggunakan `مَنْ نَفَّسَ عَنْ مُؤْمِنٍ كُرْبَةً` juga berasal dari Sahih Muslim 2699a dan wajib diberi label potongan hadits.
7. Kamus Arab–Indonesia harus dibangkitkan dari matan aktual halaman, bukan dictionary tema default.
8. FREEZE tetap BLOCKED sampai renderer menerapkan seluruh keputusan audit dan render ulang 40/40 PASS.

## Next gate
- Patch renderer labels/source + page-specific dictionary.
- Render P001–P040.
- Verify Uthman Taha, no overflow, no duplicate-main-hadith violation.
- Produce Drive review PDF.
- Freeze only after visual/content review.

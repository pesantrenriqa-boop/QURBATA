# QURBATA NIDOM — JILID 3 — HADITH AUDIT v0.1

Status: CORE ANCHORS AUDITED BEFORE RENDERER
Scope: P001–P040 production map

## Production rule
- Kompetensi boleh spiral 3–5 halaman; matan hadits utama tidak diulang monoton.
- Hadits hanya ditampilkan jika relevan dengan aktivitas halaman.
- Halaman kasus, praktik, checkpoint, refleksi, dan rapor tidak dipaksa memiliki hadits baru.
- Kamus arti per kata wajib mengikuti matan yang benar-benar tampil.
- Potongan hadits harus diberi label transparan sebagai potongan/redaksi dari riwayat yang lebih panjang.
- Arabic production font tetap Uthman Taha embedded.

## Audited anchors

### Haya / malu yang menjaga diri
1. الحَيَاءُ مِنَ الإِيمَانِ
   - Fungsi: jangkar inti bahwa haya merupakan bagian iman.
   - Source family: Sahih al-Bukhari / Sahih Muslim, bab al-haya.
   - Production: boleh dipakai P001 sebagai matan pendek tingkat Beginner 2.

2. الحَيَاءُ لَا يَأْتِي إِلَّا بِخَيْرٍ
   - Source: Sahih Muslim 37a; juga Sahih al-Bukhari 6117.
   - Meaning: haya tidak mendatangkan kecuali kebaikan.
   - Production: P002.

3. الحَيَاءُ كُلُّهُ خَيْرٌ
   - Source: Sahih Muslim 37b, riwayat Imran b. Husain.
   - Meaning: haya seluruhnya merupakan kebaikan.
   - Production: P003.

4. إِذَا لَمْ تَسْتَحِ فَاصْنَعْ مَا شِئْتَ
   - Source: Sahih al-Bukhari 6120; bagian dari redaksi lebih panjang tentang perkataan kenabian terdahulu.
   - Production: P022, wajib diberi penjelasan pedagogis: bukan izin berbuat sesuka hati, tetapi peringatan bahwa hilangnya haya membuka pintu perilaku buruk.

### Menahan marah / self-control
5. لَا تَغْضَبْ
   - Source: Sahih al-Bukhari 6116.
   - Production: P006; dapat ditampilkan sebagai jawaban Nabi yang sangat ringkas, dengan konteks bahwa nasihat itu diulang.

6. لَيْسَ الشَّدِيدُ بِالصُّرَعَةِ، إِنَّمَا الشَّدِيدُ الَّذِي يَمْلِكُ نَفْسَهُ عِنْدَ الْغَضَبِ
   - Source: Sahih al-Bukhari 6114; parallel in Sahih Muslim.
   - Meaning: kuat bukan sekadar mengalahkan orang lain, tetapi mampu menguasai diri ketika marah.
   - Production: P007.

### Rifq / lembut tanpa lemah
7. إِنَّ اللهَ رَفِيقٌ يُحِبُّ الرِّفْقَ
   - Source family: Sahih Muslim, bab fadl al-rifq.
   - Production: P012. Jika memakai potongan pendek ini, label sumber harus menyatakan potongan hadits.

8. مَنْ يُحْرَمِ الرِّفْقَ يُحْرَمِ الْخَيْرَ
   - Source: Sahih Muslim 2592a/2592b; varian 2592c juga tercatat.
   - Meaning: siapa yang terhalang dari kelembutan, terhalang dari kebaikan.
   - Production: P013.

9. إِنَّ الرِّفْقَ لَا يَكُونُ فِي شَيْءٍ إِلَّا زَانَهُ، وَلَا يُنْزَعُ مِنْ شَيْءٍ إِلَّا شَانَهُ
   - Source family: Sahih Muslim, bab fadl al-rifq.
   - Production: P014; audit nomor riwayat final kembali saat data renderer dikunci.

## Pages intentionally without forced new hadith
P004–P005, P008–P011, P015–P020, P021, P023–P040 dapat memakai kasus, kisah, dialog, role-play, misi, murojaah dalil sebelumnya, evaluasi, atau refleksi tanpa memaksakan matan baru.

## Renderer gates
- CORE_HADITH_SOURCE_AUDIT=PASS
- DUPLICATE_MAIN_HADITH_CONSECUTIVE=0
- FORCED_HADITH_ON_ASSESSMENT_PAGE=0
- DICTIONARY_MATCHES_VISIBLE_MATN=PASS
- AGE_EXPLANATION_FOR_B6120=REQUIRED
- FONT_UTHMAN=PASS
- OVERFLOW=0
- PAGE_COUNT=40

## Freeze policy
Jilid 3 tidak boleh berstatus FROZEN sampai renderer P001–P040 selesai, PDF master diperiksa, dan audit sumber/matan/terjemah/kamus pada teks yang benar-benar tercetak berstatus PASS.

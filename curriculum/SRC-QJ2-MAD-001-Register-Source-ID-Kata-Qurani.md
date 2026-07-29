# SRC-QJ2-MAD-001 — Register Source-ID Kata Qurani Blok Mad

**Status:** IN-PROGRESS — sumber resmi mulai diverifikasi  
**Tanggal:** 30 Juli 2026  
**Sumber utama:** Qur'an Kementerian Agama Republik Indonesia

## 1. Aturan

1. Label “Qurani” hanya diberikan apabila lafaz persis ditemukan pada sumber resmi.
2. Bentuk dasar yang hanya mirip akar katanya diberi status `ARABIC-VOCAB`, bukan kutipan Qurani.
3. Harakat akhir harus sesuai konteks ayat. Perubahan dari رَسُوْلًا menjadi رَسُوْلٌ bukan lagi kutipan lafaz persis meskipun leksimnya sama.
4. Tampilan mad ya dan waw mengikuti Mushaf Standar Indonesia: contoh رَحِيْمٌ dan غَفُوْرٌ dengan sukun eksplisit.
5. Potongan peserta tidak boleh memuat unsur tajwid yang belum menjadi prasyarat, walaupun kata sumbernya sah.

## 2. Entri terverifikasi awal

| Source-ID | Lafaz target | Surah:ayat | Bukti konteks | Status penggunaan |
|---|---|---|---|---|
| QID-050-027-QALA | قَالَ | Qaf 50:27 | قَالَ قَرِيْنُهٗ | EXACT-QURAN |
| QID-050-027-KANA | كَانَ | Qaf 50:27 | وَلٰكِنْ كَانَ | EXACT-QURAN |
| QID-012-077-MAKANAN | مَكَانًا | Yusuf 12:77 | شَرٌّ مَّكَانًا | EXACT-QURAN |
| QID-017-095-RASULAN | رَسُوْلًا | Al-Isra' 17:95 | مَلَكًا رَّسُوْلًا | EXACT-QURAN |
| QID-016-115-GHAFUR | غَفُوْرٌ | An-Nahl 16:115 | اِنَّ اللّٰهَ غَفُوْرٌ رَّحِيْمٌ | EXACT-QURAN |
| QID-016-115-RAHIM | رَحِيْمٌ | An-Nahl 16:115 | اِنَّ اللّٰهَ غَفُوْرٌ رَّحِيْمٌ | EXACT-QURAN |
| QID-024-011-ADHAB | عَذَابٌ | An-Nur 24:11 | لَهٗ عَذَابٌ عَظِيْمٌ | EXACT-QURAN |
| QID-024-011-AZHIM | عَظِيْمٌ | An-Nur 24:11 | لَهٗ عَذَابٌ عَظِيْمٌ | EXACT-QURAN |
| QID-009-110-ALIM | عَلِيْمٌ | At-Taubah 9:110 | وَاللّٰهُ عَلِيْمٌ حَكِيْمٌ | EXACT-QURAN |
| QID-009-110-HAKIM | حَكِيْمٌ | At-Taubah 9:110 | وَاللّٰهُ عَلِيْمٌ حَكِيْمٌ | EXACT-QURAN |
| QID-002-007-QULUB | قُلُوْبِهِمْ | Al-Baqarah 2:7 | خَتَمَ اللّٰهُ عَلٰى قُلُوْبِهِمْ | EXACT-QURAN; bentuk قُلُوْبٌ tetap vocabulary sampai ditemukan persis |
| QID-033-070-QAWLAN | قَوْلًا | Al-Ahzab 33:70 | وَقُوْلُوْا قَوْلًا سَدِيْدًا | EXACT-QURAN |
| QID-033-070-SADIDAN | سَدِيْدًا | Al-Ahzab 33:70 | قَوْلًا سَدِيْدًا | EXACT-QURAN |
| QID-002-195-SABIL | سَبِيْلِ | Al-Baqarah 2:195 | فِيْ سَبِيْلِ اللّٰهِ | EXACT-QURAN; bentuk سَبِيْلٌ belum diklaim persis |

## 3. Tautan sumber resmi

- Qaf 50:22–45: https://quran.kemenag.go.id/quran/per-ayat/surah/50?from=22&to=45
- Yusuf 12:76–111: https://quran.kemenag.go.id/quran/per-kata/surah/12?from=76&to=111
- Al-Isra' 17:82–111: https://quran.kemenag.go.id/quran/per-kata/surah/17?from=82&to=111
- An-Nahl 16:114–128: https://quran.kemenag.go.id/quran/per-ayat/surah/16?from=114&to=128
- An-Nur 24:11–64: https://quran.kemenag.go.id/quran/per-ayat/surah/24?from=11&to=64
- At-Taubah 9:103–129: https://quran.kemenag.go.id/quran/per-ayat/surah/9?from=103&to=129
- Al-Baqarah 2:3–286: https://quran.kemenag.go.id/quran/per-ayat/surah/2?from=3&to=286
- Al-Ahzab 33:37–73: https://quran.kemenag.go.id/quran/per-ayat/surah/33?from=37&to=73

## 4. Kandidat berikutnya untuk verifikasi

قِيلَ، دِيْنٌ، تِيْنٌ، طِيْنٌ، حِيْنٌ، فِيْلٌ، كَرِيْمٌ، يَتِيْمٌ، شَدِيْدٌ، قَرِيْبٌ، بَعِيْدٌ، نُوْرٌ، سُوْقٌ، رُوْحٌ، فَوْزٌ، دُوْنَ، نُجُوْمٌ، سُجُوْدٌ، حُدُوْدٌ، شُهُوْدٌ، دُخُوْلٌ، خُرُوْجٌ.

Entri di bagian ini tetap berstatus `PENDING-SOURCE-ID` dan tidak boleh diklaim sebagai lafaz Qurani persis sebelum diverifikasi.
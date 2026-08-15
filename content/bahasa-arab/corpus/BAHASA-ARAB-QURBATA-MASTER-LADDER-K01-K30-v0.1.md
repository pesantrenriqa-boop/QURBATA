# BAHASA ARAB QURBATA — MASTER LADDER K01–K30 v0.1

Status: **AUDIT CANDIDATE — belum FROZEN**

## Dasar
Dokumen ini dibangun ulang setelah audit menemukan bahwa draft Jilid 1–7 sebelumnya terlalu banyak memakai urutan intuitif. Ladder ini memisahkan **kompetensi linguistik baru** dari **murojaah/transfer**, menggunakan prerequisite eksplisit, dan harus diuji terhadap corpus Al-Qur'an sebelum freeze.

Prinsip tetap:
1. Contoh utama berasal dari corpus Al-Qur'an.
2. Contoh pada level K-n tidak boleh membutuhkan fitur gramatikal di atas K-n sebagai target analisis.
3. Materi QURBATA tetap komunikatif dan ringan; istilah nahwu dipakai sebagai metadata guru, bukan beban siswa pemula.
4. Kompetensi lama yang hanya berganti kosakata/subjek/waktu adalah REVIEW/TRANSFER, bukan kompetensi baru.
5. Distribusi ke Jilid 1–8 mengikuti ceiling TARTIL dan kesiapan baca-tulis.

## Ladder inti
| K | Kompetensi linguistik | Prasyarat | Target sederhana |
|---|---|---|---|
| K01 | Isim: mengenali kata benda/nama | — | mengenali unit makna nominal |
| K02 | Mufrad mudzakkar–muannats | K01 | membedakan bentuk tunggal dasar |
| K03 | Ma‘rifah–nakirah dasar | K01 | mengenali definiteness sederhana |
| K04 | Isim isyarah dekat: هذا / هذه | K01–K03 | menunjuk benda/orang |
| K05 | Dhamir munfashil dasar: أنا، أنت، هو، هي | K01 | mengenali pelaku nominal |
| K06 | Mubtada’ sederhana | K01–K05 | mengenali topik jumlah ismiyah |
| K07 | Khabar mufrad sederhana | K06 | membentuk jumlah ismiyah dua unsur |
| K08 | Kesesuaian gender pada jumlah ismiyah | K02,K06,K07 | هذا ... / هذه ... secara benar |
| K09 | Na‘t–man‘ut dasar | K02,K03,K07 | isim + sifat sederhana |
| K10 | Jar–majrur dasar | K01,K03 | في، على، من، إلى + isim |
| K11 | Khabar شبه جملة (jar–majrur) | K06,K10 | jumlah ismiyah dengan khabar lokasi |
| K12 | Idhafah dasar | K01,K03 | hubungan kepemilikan/relasi dua isim |
| K13 | Dhamir muttashil milkiyah | K05,K12 | كتابي، كتابك، كتابه |
| K14 | Isim istifham dasar: ما، من، أين | K04–K13 | pertanyaan identifikasi/lokasi |
| K15 | Hal/nafi nominal dasar: نعم، لا، ليس | K06–K14 | respons dan negasi nominal sederhana |
| K16 | Fi‘il madhi + fa‘il eksplisit/tersirat | K01,K05 | peristiwa lampau dasar |
| K17 | Dhamir pada fi‘il madhi | K05,K16 | فعلتُ، فعلتَ، فعلَ |
| K18 | Maf‘ul bih sederhana | K16,K17 | fi‘il + objek langsung |
| K19 | Fi‘il mudhari‘ + fa‘il | K16,K17 | aktivitas kini/kebiasaan |
| K20 | Dhamir pada fi‘il mudhari‘ | K05,K19 | أفعل، تفعل، يفعل |
| K21 | Nafi fi‘liyah dasar: لا / ما / لم | K16–K20 | negasi verba dasar |
| K22 | Istifham fi‘liyah: هل / ماذا / متى | K14,K16–K21 | pertanyaan aktivitas/waktu |
| K23 | Fi‘il amr dasar | K19,K20 | perintah langsung sederhana |
| K24 | Nahi dasar: لا + mudhari‘ majzum secara fungsional | K21,K23 | larangan sederhana |
| K25 | ‘Athaf dasar: و، ثم، فـ | K07,K16–K24 | menghubungkan unsur/kejadian |
| K26 | Zharf zaman/makan dasar | K10,K16–K25 | hari/waktu/tempat dalam kalimat |
| K27 | Kana dan saudara paling dasar | K06–K11 | perubahan jumlah ismiyah secara terbatas |
| K28 | Inna dan saudara paling dasar | K06–K11 | penegasan jumlah ismiyah secara terbatas |
| K29 | Silah/maushul dan sebab sederhana | K09,K16–K28 | الذي/التي, لأن secara terbatas |
| K30 | Integrasi wacana Qur'ani pendek | K01–K29 | 2–4 klausa dengan fitur yang sudah dikuasai |

## Catatan audit
- K01–K15 = fondasi nominal dan identifikasi.
- K16–K26 = fondasi verbal dan relasi waktu/tempat.
- K27–K30 = transformasi dan integrasi.
- Perubahan orang pertama → ketiga, sekarang → lampau → akan datang **tidak otomatis** menjadi kompetensi baru jika hanya substitusi bentuk; harus dipetakan sebagai transfer di dalam kompetensi morfologis yang sama.

Dokumen ini adalah rekonstruksi audit berdasarkan prinsip yang pernah disepakati (corpus Qur'an, prerequisite, competency ceiling). Master K01–K30 historis yang identik belum ditemukan di repo/library; karena itu versi ini tidak boleh disebut hasil pemulihan verbatim.
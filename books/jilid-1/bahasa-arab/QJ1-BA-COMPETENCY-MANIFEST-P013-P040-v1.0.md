# QURBATA Jilid 1 — Bahasa Arab Competency Manifest P013–P040

Status: AUTHORITATIVE SOURCE MANIFEST v1.0
Source: `BAHASA-ARAB-QURBATA-JILID-1-P001-P040-MASTER-LADDER-K01-K04-v3.1.pdf`
Scope: Bahasa Arab Jilid 1 P013–P040
Rule: paragraf/latihan turunan tidak boleh memperkenalkan kompetensi di atas halaman aktif. Evaluasi bersifat kumulatif dan tidak memperkenalkan kompetensi baru. Writing tetap dibatasi ceiling TARTIL halaman terkait.

## P013–P018 — K02

| Page | Level | Target | Fungsi |
|---|---|---|---|
| P013 | K02 • Bandingkan | `عَبْدٌ` / `نَفْسٌ` | dengar, pilih, tunjuk, ucapkan; membandingkan dua isim |
| P014 | K02 • Bandingkan | `قَوْمٌ` / `أُمَّةٌ` | memilah dua isim |
| P015 | K02 • Bandingkan | `مَاءٌ` / `جَنَّةٌ` | membedakan target secara lisan tanpa teori panjang |
| P016 | K02 • Pilih | `رَحْمَةٌ` | menentukan kelompok target |
| P017 | K02 • Pilih | `كِتَابٌ` | menentukan kelompok target |
| P018 | Latihan Kumulatif 3 | K01–K02 | tidak ada kompetensi baru |

## P019–P027 — K03

| Page | Level | Target | Fungsi |
|---|---|---|---|
| P019 | K03 • Nakirah | `كِتَابٌ` | mengenali bentuk umum tanpa `ال` |
| P020 | K03 • Ma'rifah | `الْكِتَابُ` | mengenali bentuk tertentu dengan `ال` |
| P021 | K03 • Bandingkan | `رَسُولٌ` / `الرَّسُولُ` | membedakan umum dan tertentu |
| P022 | K03 • Bandingkan | `رَحْمَةٌ` / `الرَّحْمَةُ` | membandingkan nakirah–ma'rifah |
| P023 | K03 • Bandingkan | `جَنَّةٌ` / `الْجَنَّةُ` | memilih bentuk sesuai stimulus |
| P024 | Latihan Kumulatif 4 | K01–K03 | tidak ada kompetensi baru |
| P025 | K03 • Ma'rifah | `الْقُرْآنُ` | mengenali isim tertentu |
| P026 | K03 • Ma'rifah | `الْأَرْضُ` | mengenali bentuk dengan `ال` |
| P027 | K03 • Ma'rifah | `السَّمَاءُ` | mengenali bentuk dengan `ال` |

## P028–P036 — K04

| Page | Level | Target | Fungsi |
|---|---|---|---|
| P028 | K04 • Isim Isyarah | `هٰذَا` | menunjuk mudzakkar dekat |
| P029 | K04 • Isim Isyarah | `هٰذِهِ` | menunjuk muannats dekat |
| P030 | Latihan Kumulatif 5 | K01–K04 | tidak ada kompetensi baru |
| P031 | K04 • Isim Isyarah | `ذٰلِكَ` | membedakan dekat dan jauh |
| P032 | K04 • Fragmen Qur'ani | `ذٰلِكَ الْكِتَابُ` | mengenali `ذٰلِكَ` + isim ma'rifah |
| P033 | K04 • Fragmen Qur'ani | `هٰذَا الْقُرْآنُ` | mengenali `هٰذَا` pada fragmen |
| P034 | K04 • Fragmen Qur'ani | `هٰذِهِ جَهَنَّمُ` | mengenali `هٰذِهِ` pada fragmen |
| P035 | K04 • Fragmen Qur'ani | `هٰذِهِ نَاقَةُ اللَّهِ` | target hanya isim isyarah; struktur lanjut belum diajarkan |
| P036 | Latihan Kumulatif 6 | K01–K04 | tidak ada kompetensi baru |

## P037–P040 — Integrasi Jilid 1

| Page | Level | Target | Fungsi |
|---|---|---|---|
| P037 | Integrasi K01–K04 | `هٰذَا` / `هٰذِهِ` / `ذٰلِكَ` | memilih kata tunjuk sesuai stimulus |
| P038 | Integrasi K01–K04 | `كِتَابٌ` / `الْكِتَابُ` | membedakan umum atau tertentu |
| P039 | Integrasi K01–K04 | `ذٰلِكَ الْكِتَابُ` / `هٰذَا الْقُرْآنُ` | menggabungkan target Jilid 1; tidak ada kompetensi baru |
| P040 | Evaluasi Akhir Jilid 1 | K01–K04 | evaluasi kumulatif; tidak ada kompetensi baru |

## Guard untuk generator paragraf

1. `ACTIVE_PAGE` menentukan ceiling kompetensi.
2. Kosakata/struktur baru hanya boleh berasal dari kompetensi halaman aktif.
3. Unsur murojaah boleh mengambil halaman sebelumnya, tetapi tidak boleh membawa fitur dari halaman sesudahnya.
4. Halaman evaluasi (`P018`, `P024`, `P030`, `P036`, `P040`) dilarang memperkenalkan kompetensi baru.
5. P035 secara eksplisit hanya menargetkan isim isyarah; struktur idhafah/struktur lanjut pada fragmen tidak dijadikan kompetensi aktif.
6. P037–P040 adalah integrasi/evaluasi K01–K04, bukan K05.
7. Bentuk tulisan harus tetap tunduk pada ceiling TARTIL Jilid 1; Bahasa Arab komunikatif tidak boleh memaksa fitur tulisan yang belum tersedia pada TARTIL.

## Production decision

Manifest ini menjadi sumber eksplisit untuk pekerjaan P013–P040 dan menutup gap sumber yang sebelumnya membuat generator paragraf berhenti di P012. Semua renderer/data paragraf berikutnya harus merujuk manifest ini sebelum produksi.
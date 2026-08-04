# QURBATA Quran Learning Object Schema — Whole Quran Model

**Status:** ACTIVE STANDARD  
**Scope:** seluruh Al-Qur'an 30 juz sebagai sumber materi QURBATA.  
**Pengendali urutan:** kompetensi dan prasyarat, bukan urutan juz atau surah.

## Prinsip inti

1. Seluruh 30 juz menjadi satu korpus sumber.
2. Objek dipilih berdasarkan kesesuaian kompetensi, prasyarat, tingkat kesulitan, dan nilai pedagogis.
3. Yang diulang adalah kompetensi dan Unit Kompetensi dengan contoh berbeda.
4. Generator dilarang memilih objek yang mengandung unsur belum diajarkan.
5. Target akhir Jilid 1–8 adalah kesiapan membaca seluruh Al-Qur'an, bukan satu juz tertentu.
6. Satu objek tidak boleh dipakai ulang dalam satu blok 10 halaman kecuali ada keputusan pedagogis tertulis.
7. Jilid 3 dan sesudahnya menggunakan kata utuh sebagai latihan reguler; dua huruf atau suku kata terpisah tidak boleh menjadi filler.

## Jenis objek

| Kode | Nama | Isi |
|---|---|---|
| `QWO` | QURBATA Word Object | satu kata Al-Qur'an |
| `QPO` | QURBATA Phrase Object | frasa 2–5 kata |
| `QAO` | QURBATA Ayah Object | potongan ayat atau ayat utuh |
| `QSO` | QURBATA Surah Object | satu surah utuh |

Urutan penggunaan umum:

```text
huruf → QWO → QPO → QAO → QSO → mushaf 30 juz
```

## Field identitas dan sumber

| Field | Fungsi |
|---|---|
| `ObjectId` | ID unik permanen |
| `ObjectType` | QWO / QPO / QAO / QSO |
| `ArabicTextNormalized` | teks Arab tervokalisasi untuk pencarian |
| `ArabicTextUthmani` | teks Utsmani untuk cetak dan tampilan mushaf |
| `SurahNumber` | nomor surah |
| `SurahName` | nama surah |
| `AyahStart` | ayat awal |
| `AyahEnd` | ayat akhir |
| `JuzNumber` | nomor juz sumber |
| `SourceStatus` | QURAN_VERIFIED / QURAN_CANDIDATE / HOLD |

## Field kompetensi

| Field | Fungsi |
|---|---|
| `TargetCompetencies` | kompetensi utama yang dilatih |
| `TargetUnits` | Unit Kompetensi utama |
| `RequiredCompetencies` | seluruh prasyarat membaca objek |
| `CumulativeCompetencies` | target + seluruh prasyarat |
| `IntroducesNewCompetency` | TRUE/FALSE |
| `ReviewCompetencies` | kompetensi lama yang tetap dilatih dengan contoh baru |
| `DependencyStatus` | COMPLETE / INCOMPLETE / HOLD |

## Field kelayakan dan skor

| Field | Fungsi |
|---|---|
| `AllowedFromVolume` | jilid minimum |
| `AllowedFromPage` | halaman minimum |
| `DifficultyScore` | skor kesulitan 1–100 |
| `PedagogicalScore` | mutu objek sebagai contoh pembelajaran 1–100 |
| `FrequencyInQuran` | frekuensi bentuk/lemma bila tersedia |
| `ReviewPriority` | prioritas sebagai contoh review kompetensi |
| `ReusePolicy` | UNIQUE_BLOCK_10 / REUSE_ALLOWED / HOLD |
| `Status` | ACTIVE / REVIEW / HOLD / DEPRECATED |

## Komponen DifficultyScore

- panjang objek;
- jumlah huruf;
- perubahan bentuk sambung;
- variasi harakat;
- mad;
- sukun;
- tanwin;
- tasydid;
- hamzah;
- alif-lam;
- tanda waqaf;
- kombinasi hukum bacaan;
- panjang frasa atau ayat.

## Komponen PedagogicalScore

- satu kompetensi utama terlihat jelas;
- sedikit unsur pengganggu;
- bentuk visual mudah dikenali;
- sesuai akumulasi kompetensi halaman;
- kaya variasi tetapi tidak meloncat;
- berguna untuk review kompetensi lama;
- relevan untuk transisi menuju mushaf;
- tidak bergantung pada pengulangan contoh yang sama.

## Feature flags bacaan

- `ContainsMadAlif`
- `ContainsMadYa`
- `ContainsMadWaw`
- `ContainsSukun`
- `ContainsTanwin`
- `ContainsShadda`
- `ContainsHamza`
- `ContainsAlifLam`
- `ContainsWaqfMark`
- `ContainsDisconnectedLetter`
- `WordCount`
- `LetterCount`

## Aturan kelayakan generator

Objek `O` boleh dipilih pada halaman `P` hanya jika:

```text
O.AllowedFromVolume <= P.Volume
O.AllowedFromPage <= P.Page
O.RequiredCompetencies ⊆ P.AvailableCompetencies
O.DependencyStatus = COMPLETE
O.Status = ACTIVE
O.SourceStatus = QURAN_VERIFIED
O.ReusePolicy tidak dilanggar
```

## Akumulasi kompetensi halaman

```text
AvailableCompetencies(Pn)
= semua kompetensi aktif sampai Pn-1
+ kompetensi baru Pn
```

Generator halaman harus memilih:

- objek berbeda yang melatih kompetensi baru;
- objek berbeda yang mengulang kompetensi sebelumnya;
- variasi dari seluruh 30 juz;
- distribusi tingkat kesulitan yang seimbang;
- tanpa mengulang contoh sebagai bentuk utama murojaah.

## Larangan

- Tidak boleh membatasi sumber hanya pada Juz 30, Al-Fatihah, atau urutan mushaf tertentu.
- Tidak boleh memilih objek hanya karena pendek, jika mengandung prasyarat yang belum aktif.
- Tidak boleh memberi label review pada objek yang sama hanya karena dipindahkan ke halaman lain.
- Tidak boleh memasukkan tasydid, hamzah, tanwin, sukun, mad, alif-lam, waqaf, atau kombinasi lanjut sebelum seluruh prasyaratnya aktif.
- Tidak boleh memberi status `QURAN_VERIFIED` tanpa rujukan surah dan ayat yang jelas.

# QURBATA Quranic Word Bank — Cumulative Competency Schema

**Status:** ACTIVE STANDARD  
**Tujuan:** memastikan setiap kata hanya muncul jika kompetensi baru dan seluruh kompetensi prasyaratnya telah tersedia pada halaman tersebut.

## Prinsip inti

1. Yang diulang adalah kompetensi dan Unit Kompetensi, bukan contoh yang sama.
2. Setiap kata membawa satu atau lebih `TargetCompetency`.
3. Setiap kata membawa seluruh `RequiredCompetencies` yang diperlukan untuk membacanya.
4. `CumulativeCompetencies` adalah gabungan kompetensi target dan seluruh prasyarat.
5. Generator hanya boleh memilih kata apabila semua `RequiredCompetencies` telah aktif sebelum atau pada halaman target.
6. Satu kata tidak boleh dipakai ulang dalam satu blok 10 halaman kecuali diberi keputusan pedagogis khusus.
7. Jilid 3 dan sesudahnya memakai kata utuh; bentuk dua huruf atau suku kata terpisah tidak digunakan sebagai filler.

## Field wajib

| Field | Fungsi |
|---|---|
| `WordId` | ID unik kata |
| `ArabicText` | teks Arab tervokalisasi |
| `Surah` | nama/nomor surah |
| `Ayah` | nomor ayat |
| `SourceStatus` | QURAN_VERIFIED / QURAN_CANDIDATE / HOLD |
| `TargetCompetencies` | kompetensi baru yang dilatih |
| `TargetUnits` | Unit Kompetensi baru |
| `RequiredCompetencies` | seluruh kompetensi prasyarat |
| `CumulativeCompetencies` | target + seluruh prasyarat |
| `AllowedFromVolume` | jilid minimum |
| `AllowedFromPage` | halaman minimum |
| `DifficultyScore` | skor kesulitan 1–100 |
| `WordLength` | jumlah huruf |
| `ContainsMadAlif` | ya/tidak |
| `ContainsMadYa` | ya/tidak |
| `ContainsMadWaw` | ya/tidak |
| `ContainsSukun` | ya/tidak |
| `ContainsTanwin` | ya/tidak |
| `ContainsShadda` | ya/tidak |
| `ContainsHamza` | ya/tidak |
| `ReviewWeight` | prioritas dipilih sebagai review kompetensi |
| `ReusePolicy` | UNIQUE_BLOCK_10 / REUSE_ALLOWED / HOLD |
| `Status` | ACTIVE / REVIEW / HOLD / DEPRECATED |

## Aturan kelayakan generator

Sebuah kata `W` boleh dipilih pada halaman `P` hanya jika:

```text
W.AllowedFromVolume <= P.Volume
W.AllowedFromPage <= P.Page
W.RequiredCompetencies ⊆ P.AvailableCompetencies
W.Status = ACTIVE
W.SourceStatus = QURAN_VERIFIED
W.ReusePolicy tidak dilanggar
```

## Akumulasi kompetensi halaman

```text
AvailableCompetencies(Pn)
= seluruh kompetensi yang sudah aktif sampai Pn-1
+ kompetensi baru Pn
```

Contoh review:

```text
Halaman baru: QT-U-014
Kompetensi tersedia: QT-U-001 s.d. QT-U-014

Generator memilih kata baru yang:
- melatih QT-U-014; atau
- mengulang salah satu QT-U-001 s.d. QT-U-013;
- tetapi tidak mengulang kata yang sudah dipakai dalam blok aktif.
```

## Larangan

- Tidak boleh memilih kata hanya karena cocok dengan satu kompetensi baru tetapi mengandung unsur yang belum diajarkan.
- Tidak boleh memberi label review pada kata yang sama hanya karena dipindahkan ke halaman lain.
- Tidak boleh memasukkan tasydid, hamzah, tanwin, sukun, mad, alif-lam, atau bentuk lanjut sebelum seluruh kompetensi prasyaratnya aktif.

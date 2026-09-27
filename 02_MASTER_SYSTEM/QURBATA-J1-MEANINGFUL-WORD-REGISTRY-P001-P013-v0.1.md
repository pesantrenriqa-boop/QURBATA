# QURBATA JILID 1 — MEANINGFUL WORD REGISTRY P001–P013

Status: **WORKING v0.2 — AUDITED / GLOBAL-NO-REPEAT**
Authority: `QURBATA-J1-MEANINGFUL-SEQUENCE-ADDENDUM-v0.1.md`.

## Prinsip
- Aturan lama tidak berubah.
- Kata bermakna hanya menggantikan slot EXACT-3 jika legal pada halaman tersebut.
- Tampilan tetap detached.
- Satu `source_word_key` hanya boleh dipakai sekali di seluruh Jilid 1.
- Kandidat tidak otomatis USED; status USED hanya setelah lolos target gate halaman.

## REGISTRY
| key | source_word | detached_display | arti ringkas | earliest legal | status / location |
|---|---|---|---|---:|---|
| كتب | كَتَبَ | كَ تَ بَ | telah menulis | P011 | USED P011/C07 |
| ترك | تَرَكَ | تَ رَ كَ | telah meninggalkan | P011 | USED P011/C08 |
| ركب | رَكَبَ | رَ كَ بَ | telah menaiki | P011 | USED P011/C09 |
| سكن | سَكَنَ | سَ كَ نَ | telah tinggal/diam | P012 | AVAILABLE |
| منع | مَنَعَ | مَ نَ عَ | telah mencegah | P012 | USED P012/C07 |
| نفع | نَفَعَ | نَ فَ عَ | telah memberi manfaat | P012 | USED P012/C08 |
| نزل | نَزَلَ | نَ زَ لَ | telah turun | P012 | USED P012/C09 |
| نصر | نَصَرَ | نَ صَ رَ | telah menolong | P012 | USED P012/C10 |
| نظر | نَظَرَ | نَ ظَ رَ | telah melihat/memandang | P012 | USED P012/C11 |
| عبد | عَبَدَ | عَ بَ دَ | telah menyembah | P012 | AVAILABLE — rejected P012 because no مَ/نَ target |
| وعد | وَعَدَ | وَ عَ دَ | telah berjanji | P013 | USED P013/C07 |
| وهب | وَهَبَ | وَ هَ بَ | telah memberi/menganugerahkan | P013 | USED P013/C08 |
| وجد | وَجَدَ | وَ جَ دَ | telah menemukan | P013 | USED P013/C09 |
| ولد | وَلَدَ | وَ لَ دَ | telah melahirkan | P013 | USED P013/C10 |
| وقع | وَقَعَ | وَ قَ عَ | telah terjadi/jatuh | P013 | USED P013/C11 |
| يسر | يَسَرَ | يَ سَ رَ | bentuk dari akar يسر; perlu verifikasi makna-konteks sebelum penggunaan | P013 | HOLD |
| هلك | هَلَكَ | هَ لَ كَ | telah binasa | P013 | USED P013/C12 |
| هجر | هَجَرَ | هَ جَ رَ | telah meninggalkan | P013 | USED P013/C13 |

## GLOBAL USED SET
`كتب`, `ترك`, `ركب`, `منع`, `نفع`, `نزل`, `نصر`, `نظر`, `وعد`, `وهب`, `وجد`, `ولد`, `وقع`, `هلك`, `هجر`

Total USED = **15**; duplicate = **0**.

## AVAILABLE / HOLD
- `سكن` AVAILABLE
- `عبد` AVAILABLE; tidak boleh digunakan kecuali target halaman kelak membuatnya legal.
- `يسر` HOLD sampai verifikasi bentuk/makna.

## QA RULE
Sebelum kandidat berubah menjadi USED, wajib PASS berurutan: legal letters/harakat → target presence → exact length → page duplicate → rolling coverage → global source uniqueness.

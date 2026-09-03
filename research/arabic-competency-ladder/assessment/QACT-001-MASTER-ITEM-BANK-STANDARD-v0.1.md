# QACT-001 — QURBATA Arabic Competency Test: Master Item-Bank Standard

**Status:** ACTIVE DEVELOPMENT
**Basis:** FROZEN K01–K65 architecture; Qur'anic evidence-gated competency ladder
**Purpose:** membangun alat uji kompetensi Bahasa Arab Qurani terstandar berbasis diagnosis kompetensi, bukan sekadar skor total.

## 1. Sasaran bank
- 65 kompetensi (K01–K65).
- Target awal: 20 butir tervalidasi per kompetensi = 1.300 butir.
- Setiap kompetensi harus mempunyai beberapa Qur'anic occurrences yang independen, variasi leksikal/morfologis/struktural, boundary/negative control, dan operasi peserta yang konsisten.
- Butir yang definisi kompetensinya belum ditemukan secara authoritative diberi status BLOCKED-DEFINITION dan **tidak boleh direka**.

## 2. Jenis paket
1. **Placement** — sampel lintas tangga untuk menemukan titik masuk.
2. **Diagnostic** — menguji profil K01–K65 dan dependency.
3. **Proficiency** — bentuk paralel terkalibrasi untuk pelaporan kemampuan.
4. **Competency verification** — fokus satu K dengan evidence lebih dalam.

## 3. Metadata wajib setiap item
`Item-ID | Competency-ID | Evidence-Ref | Target-Span | Operation | Format | Stem | Options | Key | Key-Rationale | Distractor-Rationale | Boundary | Difficulty | Dependency | Validation | Psychometric-Status`

## 4. Blueprint 20 butir per kompetensi
- 4 recognition/identification
- 4 discrimination/negative-control
- 4 structure-in-context
- 4 transfer ke occurrence Qurani lain
- 2 dependency-sensitive
- 2 integrative/high-discrimination

Distribusi dapat berubah setelah pilot/IRT; jumlah 20 adalah target bank awal, bukan panjang tes final.

## 5. Quality gate
DRAFT → LANGUAGE-REVIEW → QURAN-EVIDENCE-REVIEW → CONTENT-VALIDATED → PILOT → ITEM-ANALYSIS → CALIBRATED → OPERATIONAL.

## 6. Skoring
Pelaporan utama harus menghasilkan:
- skor total;
- mastery per K;
- confidence/evidence count;
- kompetensi terendah yang menjadi blocker;
- kompetensi berikut yang siap diuji;
- profil domain dan rekomendasi belajar.

Jangan menyatakan peserta menguasai kompetensi lanjutan jika dependency kritis di bawahnya belum mempunyai evidence memadai.

## 7. Psikometri
Sesudah pilot, simpan p-value/item difficulty, daya pembeda, distractor functioning, reliabilitas, DIF/fairness flag, dan parameter Rasch/IRT bila model memenuhi asumsi. Bentuk tes operasional harus memakai item yang telah lolos gate, bukan item DRAFT.

## 8. Kompetensi yang sudah mempunyai definisi eksplisit dalam audit E3
K04 preposition recognition; K09 preposition + overt noun; K10 verb + overt fa'il; K17 simple na'at–man'ut; K21 attached pronoun as direct object; K27 generic negation recognition (E3-candidate); K29 imperative recognition; K32 قد recognition; K35 ليس recognition; K36 لو recognition.

K11, K12, K13, K20, K23, K26, K28, K30, K33, K34, K37, K45, K65 tercatat sebagai candidate pool Wave 02 tetapi definisi lengkap harus dipulihkan sebelum produksi item.

## 9. Prinsip anti-fabrikasi
Nama/operasi K yang belum didukung dokumen authoritative tidak boleh diisi berdasarkan tebakan urutan nahwu. Recovery definisi K01–K65 adalah pekerjaan paralel dan menjadi gate produksi seluruh 1.300 butir.

# Evidence K30–K31 v0.1

**Status:** WORKING RESEARCH — NON-AUTHORITATIVE

## K30-CAND — Recognition Hamzah Istifham `أَ`

Target: mengenali hamzah istifham pada occurrence yang tervalidasi sebagai penanda pertanyaan.

Evidence rules:
- wajib occurrence-specific; surface alif/hamzah tidak otomatis K30;
- clitic segmentation harus dicatat;
- scope pertanyaan dan struktur clause sesudahnya tetap locked;
- contoh inti diprioritaskan dari konteks yang tidak membutuhkan kompetensi di atas K30.

Risks:
- ortografi/segmentasi dapat menyatu dengan token berikut;
- hamzah dapat muncul berdekatan dengan bentuk lain sehingga corpus tag/function validation wajib.

Judgement: **STRONG CANDIDATE**, tetapi lebih berat daripada `هَلْ` karena segmentasi.

## K31-CAND — Recognition Future Markers `سـ` / `سوف`

Target: mengenali penanda future pada fi'il mudhari' tanpa mengajarkan seluruh semantik temporal/aspektual.

Dependencies:
- K7 recognition fi'il mudhari'.

Evidence rules:
- `سوف` dapat diperlakukan sebagai token-level marker;
- prefixed `سـ` harus disegmentasi dari fi'il;
- subject, object, and clause structure of the host verb remain governed by prior K;
- semantic nuances beyond future marking remain locked.

Risks:
- prefixed `سـ` membutuhkan morphological segmentation lebih ketat;
- host verb dapat membawa suffix/object/other structures.

Judgement: **STRONG**, but evidence should separate `سوف` and prefixed `سـ` subtypes.

## Head-to-head K30 vs K31

K30 introduces a new interrogative surface marker with segmentation burden.
K31 reuses already-frozen mudhari' recognition and adds future marking.

Dependency-wise K31 may actually be slightly lighter because it builds directly on K7, while K30 requires function-specific hamzah tagging.

### Revised hypothesis

- K30-CAND — recognition future marker `سوف` first, then prefixed `سـ` as same K subtype if evidence clean;
- K31-CAND — recognition hamzah istifham `أَ`.

This is a **proposed swap** from the previous frontier and requires counterexample test before freeze.

## Next

1. counterexample test proposed K30/K31 swap;
2. if stable, freeze K30–K31;
3. then rescan next lightweight nodes before fa'il mustatir and silah maushul.
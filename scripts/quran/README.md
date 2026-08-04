# Whole-Quran QWO Importer

This pipeline replaces manual, tiny QWO seeds with a reproducible whole-mushaf import.

## Source requirements

Use a verified Quran text containing exactly 6,236 ayat, one ayah per line, in canonical mushaf order. The recommended source is Tanzil Uthmani text. Keep its text and license notice unchanged. The importer stores exact source tokens in `ArabicTextUthmani`; it does not rewrite the Quran text.

Tanzil usage requirements include attribution and preservation of its license notice. See:

- https://tanzil.net/download/
- https://tanzil.net/docs/text_license

## Run

```powershell
python scripts/quran/import_whole_quran_qwo.py `
  --input data/source/quran-uthmani.txt `
  --output content/qlo/generated/QWO-WHOLE-QURAN-CANDIDATES.csv
```

Expected output: tens of thousands of QWO occurrence records covering all 30 juz.

## Generated metadata

The importer produces:

- exact Uthmani token;
- normalized search form;
- surah, ayah, and word position;
- whole-Quran occurrence frequency;
- letter count;
- automatic feature tags: short vowels, mad, sukun, tanwin, shadda, hamza, alif-lam;
- initial target competency;
- required and cumulative competencies;
- difficulty and pedagogical scores;
- earliest candidate jilid;
- review priority and reuse policy.

## Important QA boundary

Generated records are `CANDIDATE`, not publication-ready. Automatic tagging accelerates production but does not replace:

1. verification against the exact source ayah;
2. competency audit by QURBATA curriculum reviewers;
3. progression audit against Jilid 1–8;
4. Uthmani rendering validation;
5. final `ACTIVE` approval.

## Why occurrence records

The same written word may appear in different ayat and contexts. Each occurrence receives a stable QWO ID and source reference. A later deduplication view can group normalized forms while preserving every Quranic occurrence.

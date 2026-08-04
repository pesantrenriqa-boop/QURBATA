# Whole-Quran QWO Importer

This pipeline replaces manual, tiny QWO seeds with a reproducible whole-mushaf import.

## Source requirements

Use a verified Quran text containing exactly 6,236 ayat, one ayah per line, in canonical mushaf order. The recommended source is Tanzil Uthmani text. Keep its text and license notice unchanged. The importer stores exact source tokens in `ArabicTextUthmani`; it does not rewrite the Quran text.

Tanzil usage requirements include attribution and preservation of its license notice. See:

- https://tanzil.net/download/
- https://tanzil.net/docs/text_license

## Generate QWO candidates

```powershell
python scripts/quran/import_whole_quran_qwo.py `
  --input data/source/quran-uthmani.txt `
  --output content/qlo/generated/QWO-WHOLE-QURAN-CANDIDATES.csv
```

Expected output: tens of thousands of QWO occurrence records covering all 30 juz.

Every generated object starts as:

- `Status=REVIEW`;
- `SourceStatus=QURAN_CANDIDATE`.

The importer is not permitted to grant `ACTIVE` or `QURAN_VERIFIED` automatically.

## Validate an existing QWO CSV

```powershell
python scripts/quran/import_whole_quran_qwo.py `
  --validate-csv content/qlo/generated/QWO-WHOLE-QURAN-CANDIDATES.csv
```

Validation fails when it finds:

- legacy or unknown competency codes;
- missing competency prerequisites;
- an object placed earlier than the official minimum jilid;
- invalid surah or ayah references;
- status values outside the official schema;
- an `ACTIVE` object whose source is not `QURAN_VERIFIED`.

## Canonical competency policy

Only `QT-UK-###` codes defined in `curriculum/tartil/QCF-001-TARTIL-COMPETENCY-FRAMEWORK.md` are valid for production.

Legacy `QT-U-*` labels are migration aliases only. Their mappings are recorded in:

`curriculum/tartil/QT-UNIT-CODE-ALIAS-REGISTRY.csv`

New generated data must never emit legacy labels.

## Generated metadata

The importer produces:

- exact Uthmani token;
- normalized search form;
- surah, ayah, and word position;
- whole-Quran occurrence frequency;
- letter count;
- automatic feature tags: short vowels, mad, sukun, differentiated tanwin, shadda, hamza, alif-lam, and alif maqsurah;
- canonical target competency;
- explicit required and cumulative competencies;
- difficulty and pedagogical scores;
- earliest candidate jilid controlled by the competency registry;
- review priority and reuse policy.

## Important QA boundary

Generated records are review candidates, not publication-ready. Automatic tagging accelerates production but does not replace:

1. verification against the exact source ayah;
2. competency audit by QURBATA curriculum reviewers;
3. progression audit against Jilid 1–8;
4. Uthmani rendering validation;
5. final `QURAN_VERIFIED` source approval;
6. final `ACTIVE` object approval.

The generator for book pages may select an object only when all of the following are true:

```text
Status = ACTIVE
SourceStatus = QURAN_VERIFIED
DependencyStatus = COMPLETE
AllowedFromJilid <= target jilid
RequiredCompetencies are already available
```

## Why occurrence records

The same written word may appear in different ayat and contexts. Each occurrence receives a stable QWO ID and source reference. A later deduplication view can group normalized forms while preserving every Quranic occurrence.

# QWO Competency-First Policy V1

## Status
ACTIVE — authoritative policy for all QURBATA Word Object production.

## Core rule
QWO must be selected, grouped, reviewed, and released by competency requirements, not by mushaf order, surah order, juz order, or verse sequence.

## Prohibited production patterns
The following approaches are not allowed as the governing production sequence:

- starting from Al-Fatihah and continuing by surah;
- starting from Al-Baqarah and continuing by mushaf order;
- using one surah as the default first QWO batch;
- assuming lower surah or ayah numbers mean lower learning difficulty;
- naming production batches in a way that implies mushaf sequence.

Source references remain mandatory metadata, but they do not determine instructional order.

## Required production flow

1. Resolve the target QCI competency.
2. Resolve all prerequisite competencies.
3. Search the Qur'an for candidate words matching that competency boundary.
4. Reject words that require any competency outside the allowed boundary.
5. Rank valid candidates by pedagogical value, frequency, visual diversity, review need, and suitability for the intended level.
6. Record surah, ayah, and token position only as source traceability.
7. Release the object only after source, competency, and pedagogical validation pass.

## Canonical grouping
Production sets must be competency-oriented, for example:

- `QWO-COMP-GRAPHEME-001`
- `QWO-COMP-FATHAH-001`
- `QWO-COMP-CONNECTION-3L-001`
- `QWO-COMP-MAD-ALIF-001`
- `QWO-COMP-TANWIN-FATH-001`

A single object may support multiple competencies, but it must have one explicit `TargetCompetency` and a complete `RequiredCompetencies` list.

## Generator rule
The generator must never ask which verse comes next. It must ask:

1. Which competency is being taught?
2. Which prerequisites are already permitted?
3. Which Qur'anic objects stay inside that competency boundary?
4. Which selection creates the best balance of new material and cumulative review?

## Al-Fatihah exclusion
Al-Fatihah must not be used as the default seed corpus or governing production order for MASTER_QWO. Any future use of Al-Fatihah content must result from normal competency matching, not from its position as the first surah.

## Migration rule
Any surah-first QWO batch must be deleted, quarantined, or rebuilt before it may become production data.

## Governance
Changes to this policy require an explicit documented decision. Convenience, frequency, or mushaf position alone cannot override competency-first sequencing.

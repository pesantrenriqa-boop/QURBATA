# QJ6 — Batch A review decisions and evidence ledger

Date: 2026-11-05. Scope: 30 source-flagged entries, across 14 pages. This is an **open review ledger**. It records outstanding decisions; it does not certify any Quranic text, MSI glyph, competency, or print approval.

## Triage groups

| Group | Entries | Pending decision | Gate |
| --- | ---: | --- | --- |
| P002–P011: emphatic letters and ra | 12 | Match phonetic target, exception rules, prerequisites, J1–J5 duplicates | Qualified tajwid reviewer |
| P015–P016: waqf signs | 11 | Direct MSI sign identity, exact position and intended teaching classification | Direct MSI edition collation |
| P022/P024/P031: end-waqf and long excerpts | 7 | Stopped pronunciation, intended stop point, long-verse pause plan | Qualified tajwid reviewer + MSI collation |
| **Total** | **30** | **All pending competency verification** | **No promotion** |

## Prioritized decision records

| Priority | Slot | Question to resolve | Evidence required | Decision |
| --- | --- | --- | --- | --- |
| Critical | P022-S09 | Is `فَٱعْبُدُونِ` appropriate for this specific verse-end waqf lesson? | Direct target-edition verse and qualified recitation explanation | PENDING / RESEARCH |
| High | P011-S05 | What is the exact ra rule for `قِرۡطَاسٖ` in the adopted recitation? | Named tajwid rule, reviewer, source page | PENDING |
| High | P008-S09 | Are multiple ra conditions acceptable in a tarqiq-I exercise? | Pedagogical target annotation and prerequisite review | PENDING |
| High | P015-S07 | Are both `ۛ` signs intended in one exercise? | MSI collation of both sign positions | PENDING |
| High | P017-S02, P017-S04 | Where is the standalone `لا` waqf sign in the target MSI edition? | Verse-specific direct MSI evidence | PENDING; not part of the 30 source-flagged batch |
| Medium | P024-S04 | Which of the two fathatan-alif words is the intended stopping point? | Teaching note and stopped-reading check | PENDING |
| Medium | P031-S07–S09 | Which pauses are intended for pacing and how do they map to MSI? | Marked pause plan and verse-level MSI comparison | PENDING |

## Evidence record template

For each reviewed slot, append a dated decision with:

- Slot ID and current CSV row fingerprint (to prevent approving stale text)
- Approved mushaf edition, surah:ayah, and exact sign/excerpt evidence
- Tajwid rule and exact target word/letter
- Curriculum prerequisite and Jilid 1–5 duplicate assessment
- Reviewer name, date, decision (APPROVE / REVISE / REJECT), and evidence link/page
- Independent print gate: **do not infer print approval from a review decision**

## Workflow

1. Review critical and high-priority decisions with direct primary evidence.
2. Record decisions in this ledger without silently rewriting Quranic text.
3. Change CSV verification fields only after a dated, evidence-backed review.
4. Re-run the register audit and regression suite; inspect `release_holds` before any print release.

No changes to `QJ6-slots.csv`, Quranic text, verification flags, or publication status.

# EVIDENCE MATURITY AUDIT — K01–K10 v1.0

**Status:** COMPLETED CONSERVATIVE AUDIT  
**Architecture:** K01–K65 FROZEN  
**Source:** `DRAFT-FROZEN-K01-K10-v1.0.md`  
**Rule:** no Qur'anic reference is invented during maturity audit; only evidence explicitly preserved in authoritative discovery artifacts is credited.

## Audit result

| K | Competency | Credited evidence in authoritative source | Maturity | Decision |
|---|---|---|---|---|
| K01 | simple isim recognition | competency definition preserved, but no explicit canonical verse anchor recorded in this source | E0 | anchor extraction/expansion required |
| K02 | `الـ` recognition | form definition preserved; no independent canonical verse anchor recorded | E0 | anchor required |
| K03 | simple nakirah/tanwin recognition | form definition preserved; no independent canonical verse anchor recorded | E0 | anchor required |
| K04 | frequent preposition recognition | explicit target forms `من، في، على، إلى، بـ، لـ`; no surah:ayah anchor attached to each | E0+ | forms confirmed; canonical cited anchor required |
| K05 | detached pronoun recognition | explicit forms `هو، هي، أنت، أنتم`; no surah:ayah anchor attached | E0+ | forms confirmed; canonical cited anchor required |
| K06 | simple perfect recognition | definition and exclusions preserved; no canonical verse anchor recorded | E0 | anchor required |
| K07 | simple imperfect recognition | definition and exclusions preserved; no canonical verse anchor recorded | E0 | anchor required |
| K08 | simple mubtada' + nominal khabar | `اللَّهُ الصَّمَدُ` — QS 112:2 | E1 | canonical anchor confirmed; expand clean bank |
| K09 | preposition + overt noun | clean types `فِي الْأَرْضِ`, `فِي السَّمَاوَاتِ`, `عَنِ النَّبَإِ`, `بِالْحَقِّ`, `مِنَ الْأَرْضِ`; source does not attach individual surah:ayah references here | E1- | multiple clean spans exist, but references must be normalized before E2 |
| K10 | verb + overt fa'il | clean types `جَاءَ الْحَقُّ`, `زَهَقَ الْبَاطِلُ`, `قَالَ مُوسَىٰ`, `يُرِيدُ اللَّهُ`; source does not attach individual surah:ayah references here | E1- | multiple clean spans exist, but references must be normalized before E2 |

## Interpretation

This audit deliberately lowers confidence compared with an informal global percentage. The frozen architecture is strong, but the **production evidence bank** is not yet uniformly mature because early discovery documents often preserved example spans without full normalized evidence metadata.

### Confirmed canonical anchor

K08:

> `اللَّهُ الصَّمَدُ` — QS 112:2

Target operation: identify overt nominal mubtada' `اللَّهُ` and overt nominal khabar `الصَّمَدُ` in a minimal nominal sentence.

Forbidden dependencies in core interpretation: PP khabar, idhafah, adjective relation, `إنّ`, `كان`, nested clause.

### K09 normalization queue

Existing clean spans to normalize with exact surah:ayah and target metadata:
- `فِي الْأَرْضِ`
- `فِي السَّمَاوَاتِ`
- `عَنِ النَّبَإِ`
- `بِالْحَقِّ`
- `مِنَ الْأَرْضِ`

### K10 normalization queue

Existing clean spans to normalize with exact surah:ayah and target metadata:
- `جَاءَ الْحَقُّ`
- `زَهَقَ الْبَاطِلُ`
- `قَالَ مُوسَىٰ`
- `يُرِيدُ اللَّهُ`

## Required next action

1. recover exact Qur'anic references for K09/K10 spans from authoritative corpus/evidence artifacts;
2. build explicit E1 anchors for K01–K07;
3. expand each K to several cumulative-clean occurrences;
4. record negative/premature examples;
5. promote only after metadata is complete.

## Progress implication

The previous `~55% evidence` figure was a planning estimate, not a per-K audited maturity score. This first formal audit shows why the evidence workstream must now be measured from committed audit records rather than intuition.

For K01–K10 specifically:
- architecture audited: 10/10;
- explicit fully referenced canonical anchor at E1+: 1/10 (K08);
- partial span banks awaiting reference normalization: 2/10 (K09–K10);
- recognition anchors requiring explicit extraction: 7/10.

**K01–K10 AUDIT: COMPLETE.**  
**NEXT: evidence-reference recovery and anchor build, then K11–K20 audit.**
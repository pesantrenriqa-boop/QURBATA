# EVIDENCE ANCHOR RECOVERY — K11–K20 v1.0

**Status:** CANONICAL E1 ANCHOR BATCH  
**Architecture:** K01–K65 FROZEN v1.0  
**Canonical definitions:** `CANONICAL-REGISTRY-K11-K20-v0.1.md`  
**Policy:** target span is kept as small as possible; the anchor validates the target operation and must not redefine the competency.

| K | Canonical target | Qur'anic anchor | Ref | Validation note |
|---|---|---|---|---|
| K11 | detached pronoun as mubtada' | `هُوَ الْعَلِيُّ` | 2:255 | `هو` is the overt detached-pronoun subject; `العلي` supplies the simple nominal predication target. The longer adjective continuation is outside the minimal target span. |
| K12 | jar–majrur as khabar | `لِلَّهِ الْحَمْدُ` | 45:36 | Minimal PP predicate `لله` with overt nominal subject `الحمد`; verse-initial `فـ` is excluded from the target span. |
| K13 | two overt nouns in idhafah | `رَسُولُ اللَّهِ` | 48:29 | Clean two-noun idhafah: `رسول` mudaf + `الله` mudaf ilayh. |
| K14 | overt nominal direct object | `وَرِثَ سُلَيْمَانُ دَاوُدَ` | 27:16 | Overt verb + overt fa'il `سليمان` + overt object `داود`; avoids hidden-subject dependence. |
| K15 | attached-pronoun segmentation | `رَبِّكَ` | 96:1 | Segment noun host `رب` + attached pronoun `ك`; no possessive-function mastery is required for the recognition operation itself. |
| K16 | validated conjunction recognition | `دَاوُدَ وَسُلَيْمَانَ` | 27:15 | Target is the overt coordinating `و`; construction-level coordination remains K19. |
| K17 | simple na'at–man'ut | `الصِّرَاطَ الْمُسْتَقِيمَ` | 1:6 | Clear two-token modified noun + adjective with visible agreement. |
| K18 | attached pronoun as mudaf ilayh | `عَبْدِهِ` | 17:1 | Noun host `عبد` + attached pronoun `ـه` in possessive/genitive relation. |
| K19 | coordination of two nominal units | `دَاوُدَ وَسُلَيْمَانَ` | 27:15 | Two overt proper nouns coordinated by validated `و`; target is the relation, not marker recognition alone. |
| K20 | preposition + attached pronoun | `لَهُ` | 2:255 | Direct preposition `لـ` + attached pronoun `ـه`; no intervening noun host. |

## Boundary controls

- K11 does not open PP/clausal khabar.
- K12 targets `لله الحمد`; the prefixed discourse `فـ` in the full verse is outside the anchor span.
- K13 is limited to two overt nouns; no three-member chain.
- K14 requires an overt object and uses an overt subject here specifically to avoid importing K41.
- K15 is segmentation only; functional assignment is deferred to K18/K20/K21.
- K16 recognizes the conjunction token; K19 interprets the coordination relation.
- K17 excludes adjective chains and nested dependencies.
- K18 distinguishes noun-host possession from verb-object and preposition-pronoun functions.
- K19 remains nominal coordination, not clause coordination K58.
- K20 requires direct preposition + pronoun, so `بإذنه` is not used as the canonical anchor because the pronoun attaches to `إذن`, not directly to the preposition.

## Promotion verdict

All K11–K20 now have an explicit canonical Qur'anic anchor with surah:ayah and minimal target span.

**K11–K20: promoted from E1- baseline to E1.**

Next: `EVIDENCE-ANCHOR-RECOVERY-K21-K25`, then recalculate the formal global evidence-maturity baseline.
# QURBATA NIDOM — JILID 1 — REVISION LOCK v1.1

Status: FROZEN FOR REBUILD

## Corrections

1. Batch v1.0 P012–P040 is NOT production-approved. It violated the agreed repetition architecture by assigning a new hadith/theme to nearly every page.
2. Arabic typography from P012 batch is NOT approved. Every Arabic string must render with the same verified KFGQPC Uthman Taha Naskh pipeline used by approved early pages. CSS declaration alone is insufficient; renderer must assert the actual loaded face before PDF export.
3. Jilid 1 assumes learner akhlak competency starts near ZERO. Therefore breadth is deliberately limited; repetition and habituation take priority over number of hadith.

## Core pedagogical rule

ONE HADITH / ONE CORE AKHLAK THEME spans 3–5 learning pages depending on difficulty. The same hadith may be repeated verbatim across the block. The activity changes while the moral anchor stays stable.

Progression inside one theme block:
- encounter / hear / imitate;
- recognize meaning and behavior;
- choose correct behavior in a simple situation;
- perform / habituate at school-home;
- retrieve / reflect / simple assessment where needed.

No requirement to introduce a new hadith on the next page.

## Jilid 1 design target

Target: approximately 7–8 core hadith themes across 40 pages, not 25–30 hadith. Use 4 pages as the normal block; 3 pages for very concrete themes and 5 pages for themes needing stronger habituation. Evaluation pages remain cumulative and should recycle all previous themes.

## Proposed 40-page architecture

- P001–P004 — SALAM: أَفْشُوا السَّلَامَ بَيْنَكُمْ
  Focus: hear/say salam → when to say → answer/practice → habituation check.
- P005–P008 — GOOD SPEECH: فَلْيَقُلْ خَيْرًا أَوْ لِيَصْمُتْ
  Focus: kind words → avoid hurtful words → choose speech in cases → home/school habit.
- P009–P010 — CUMULATIVE EVALUATION A
  Salam + good speech; objective, oral/practice, simple case, parent/teacher observation.
- P011–P014 — ANGER / SELF-CONTROL: إِنَّمَا الشَّدِيدُ الَّذِي يَمْلِكُ نَفْسَهُ عِنْدَ الْغَضَبِ
  Focus: recognize anger → pause/control → safe response → repeated habit.
- P015–P018 — HONESTY: إِنَّ الصِّدْقَ يَهْدِي إِلَى الْبِرِّ
  Focus: truth vs lie → admit mistakes → simple cases → repeated honesty habit.
- P019–P020 — CUMULATIVE EVALUATION B
  Retrieval and behavior transfer from P001–P018.
- P021–P024 — MERCY / CARE: مَنْ لَا يَرْحَمِ النَّاسَ لَا يَرْحَمْهُ اللَّهُ
  Focus: gentle behavior → helping/caring → younger/peer cases → home/school habit.
- P025–P028 — AMANAH: آيَةُ الْمُنَافِقِ ثَلَاثٌ ... وَإِذَا اؤْتُمِنَ خَانَ
  Focus: entrusted objects/tasks → borrowing/returning → simple cases → repeated habit.
- P029–P030 — CUMULATIVE EVALUATION C
  Mixed response selection, practice, short reasoning, observation.
- P031–P034 — RESPECT FOR PARENTS / ELDERS: theme anchored to a single verified hadith chosen before production.
  Focus: polite response → helping → listening → repeated home habit.
- P035–P36 — FINAL HABITUATION REVIEW
  Cross-theme practice stations; no new hadith.
- P037–P038 — FINAL JILID ASSESSMENT
  Knowledge + simple cases + direct practice; no new hadith.
- P039 — JEJAK KEBIASAANKU
  Learner + parent + teacher reflection.
- P040 — RAPOR NIDOM JILID 1
  Achievement summary and readiness for Jilid 2.

This gives 7 core theme blocks in Jilid 1 with deliberate repetition. If field use shows one block needs five encounters, reduce breadth rather than compress repetition.

## Typography gate

For every production render:
- bind Uthman Taha font asset before browser launch;
- wait for document.fonts.ready;
- assert document.fonts.check() using the exact Arabic sample;
- inspect computed fontFamily;
- fail the workflow if the Arabic node is not bound to KFGQPC Uthman Taha Naskh;
- no fallback-generated PDF is allowed into Drive production.

## Production consequence

The existing P001–P040 Print Master v1.0 is a DRAFT/REJECTED master and must not be treated as the final Jilid 1. Rebuild content blocks from P001 architecture while preserving the approved visual language (logo, B5 layout, low signatures, spiral review, restrained whitespace).
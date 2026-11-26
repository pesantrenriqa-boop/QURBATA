# Search strings v0.2 DRAFT
2026-11-26. Rancangan belum diuji pada antarmuka database asli.
A = ("Arabic language" OR "Arabic learning" OR "Arabic teaching" OR "Quranic Arabic" OR "Arabic vocabulary" OR "Arabic grammar" OR nahwu OR "bahasa Arab" OR "اللغة العربية")
B = (Quran OR "Qur'an" OR Quranic OR Koran OR Alquran OR "Al-Qur'an" OR القرآن)
C = (learn* OR teach* OR educat* OR pedagog* OR instruction* OR curriculum OR pembelajaran OR pengajaran OR تعليم OR تعلم)
Scopus: TITLE-ABS-KEY(A AND B AND C) AND PUBYEAR > 2015 AND PUBYEAR < 2027
WoS: TS=(A AND B AND C) AND PY=(2016-2026)
Replace A/B/C with full parenthesized expressions above before running.
ERIC: ("Arabic language" OR "Arabic vocabulary" OR "Arabic grammar" OR "Quranic Arabic") AND (Quran OR "Qur'an" OR Quranic OR Koran); use publication date 2016–2026, peer-reviewed filter if available; screen educational relevance manually.
DOAJ: run article searches separately: "Quranic Arabic" ; "Arabic language" Quran ; "Arabic vocabulary" Quran ; "bahasa Arab" Alquran ; "اللغة العربية" القرآن. Use year filters where supported, log exact interface behavior.
GARUDA: separate queries: pembelajaran bahasa Arab Al-Quran; bahasa Arab Alquran; kosakata bahasa Arab tahfidz; Quranic Arabic Corpus; nahwu Al-Quran.
Google Scholar: separate queries: "Arabic language learning" Quran; "Quranic Arabic" teaching; "Arabic vocabulary" Quran; "pembelajaran bahasa Arab" "Al-Qur'an"; "تعليم اللغة العربية" "القرآن الكريم". Proposed cap first 100 results per query sorted by relevance, log date and actual count; not exhaustive.
Do not use ecosystem as mandatory term. Additional focused queries: integrated curriculum, language environment, tahfiz, memorization, bi'ah arabiyah; validate against seed articles. Apply language and empirical criteria at screening rather than narrow database filters prematurely. Record exact expanded query, date, filters, export format, total retrieved and retained. Database syntax and access pending live testing.

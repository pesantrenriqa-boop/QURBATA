# Final Gate K11–K14 v1.0

**Status:** DRAFT-FROZEN — RESEARCH LAYER ONLY  
**Parent:** `STRESS-TEST-K11-K14-v0.1.md`, `EVIDENCE-BANK-K11-K14-v0.1.md`  
**Authority:** NON-AUTHORITATIVE; belum mengubah `REG-ARB-001` atau stage produksi.

## 1. Frozen Research Sequence

- **K11 — REL-PRON-MUBTADA** — dhamir munfashil sebagai mubtada' dalam jumlah ismiyyah sederhana
- **K12 — REL-KHABAR-PP** — khabar jar–majrur sederhana
- **K13 — REL-IDHAFAH-2N** — idhafah dua isim zhahir sederhana
- **K14 — REL-MAFUL-ZHAHIR** — maf'ul bih isim zhahir sederhana

## 2. Gate Result

Tidak ditemukan dependency reversal yang memaksa perubahan urutan.

### K11
Hard dependency: K5 + K8.  
Status: `DRAFT-FROZEN`.

### K12
Hard dependency: K8 + K9.  
Status: `DRAFT-FROZEN`.

### K13
Hard dependency: K1 dan exposure genitive melalui K9.  
Status: `DRAFT-FROZEN`.

### K14
Hard dependency: K10 + recognition isim.  
Status: `DRAFT-FROZEN WITH STRICT EVIDENCE FILTER`.

## 3. Cumulative Rule

Contoh K11 hanya boleh membutuhkan K1–K11.  
Contoh K12 hanya boleh membutuhkan K1–K12.  
Contoh K13 hanya boleh membutuhkan K1–K13.  
Contoh K14 hanya boleh membutuhkan K1–K14.

Setiap candidate yang membutuhkan kompetensi lebih tinggi tetap disimpan sebagai `PREMATURE`.

## 4. Scope Boundaries

K11 belum mencakup khabar jar–majrur, khabar jumlah, atau pronoun reference kompleks.  
K12 belum mencakup preposition + attached pronoun.  
K13 belum mencakup chain idhafah tiga unsur, mudhaf ilaih berupa attached pronoun, atau na'at pada unsur idhafah.  
K14 belum mencakup object pronoun, dua maf'ul, object clause, atau object yang membutuhkan struktur lebih tinggi.

## 5. Integration Guardrail

Freeze ini hanya research baseline. Mapping ke `REG-ARB-001` dan `AR-STG-*` menunggu freeze formal lintas layer dan review integrasi.

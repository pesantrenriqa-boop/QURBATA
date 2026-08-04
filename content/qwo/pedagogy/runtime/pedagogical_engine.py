#!/usr/bin/env python3
from __future__ import annotations
import csv, unicodedata
from dataclasses import dataclass
from pathlib import Path

SHORT = set("َُِ")
TANWIN = set("ًٌٍ")
SUKUN="ْ"; SHADDA="ّ"; DAGGER="ٰ"; MADDA="ٓ"
HAMZA_FORMS=set("ءأإؤئآ")
NON_CONNECTORS=set("ادذرزوأإآؤءٱى")

@dataclass
class Decision:
    passed: bool
    reasons: list[str]

def base_letters(text: str) -> list[str]:
    return [c for c in unicodedata.normalize("NFC", text) if unicodedata.category(c).startswith("L")]

def marks(text: str) -> set[str]:
    return {c for c in unicodedata.normalize("NFC", text) if unicodedata.category(c).startswith("M")}

def grapheme_clusters(text: str) -> list[str]:
    out=[]
    for c in unicodedata.normalize("NFC", text):
        if unicodedata.category(c).startswith("L"):
            out.append(c)
        elif unicodedata.category(c).startswith("M") and out:
            out[-1]+=c
    return out

def has_madd(text: str) -> bool:
    clusters=grapheme_clusters(text)
    for i,c in enumerate(clusters):
        b=c[0]; m=set(c[1:])
        prev=set(clusters[i-1][1:]) if i else set()
        if b=="ا" and ("َ" in prev or DAGGER in m): return True
        if b=="ي" and "ِ" in prev and not (m & (SHORT|TANWIN|{SHADDA})): return True
        if b=="و" and "ُ" in prev and not (m & (SHORT|TANWIN|{SHADDA})): return True
    return DAGGER in text or MADDA in text

def is_connected_pair(text: str) -> bool:
    letters=base_letters(text)
    if len(letters)!=2: return False
    return letters[0] not in NON_CONNECTORS

def has_nonconnector_transition(text: str) -> bool:
    letters=base_letters(text)
    return any(ch in NON_CONNECTORS for ch in letters[:-1])

def load_rules(path: str|Path):
    with open(path, encoding="utf-8", newline="") as f:
        return {r["CompetencyID"]:r for r in csv.DictReader(f)}

def validate(text: str, object_type: str, competency_id: str, rules) -> Decision:
    r=rules[competency_id]; reasons=[]
    if object_type not in r["AllowedObjectTypes"].split("|"): reasons.append("OBJECT_TYPE")
    letters=base_letters(text); ms=marks(text)
    if len(letters)>int(r["MaxBaseLetters"]): reasons.append("MAX_LENGTH")
    allowed=set(r["AllowedBaseLetters"])
    if any(ch not in allowed for ch in letters): reasons.append("LETTER_NOT_ALLOWED")
    allowed_marks=set(r["AllowedMarks"])
    forbidden=set(r["ForbiddenMarks"])
    if any(m not in allowed_marks for m in ms): reasons.append("MARK_NOT_ALLOWED")
    if ms & forbidden: reasons.append("FORBIDDEN_MARK")
    if r["AllowHamzaForms"]=="NO" and any(ch in HAMZA_FORMS for ch in letters): reasons.append("HAMZA_FORBIDDEN")
    if r["AllowMadd"]=="NO" and has_madd(text): reasons.append("MADD_FORBIDDEN")
    if r["AllowTanwin"]=="NO" and ms & TANWIN: reasons.append("TANWIN_FORBIDDEN")
    if r["AllowSukun"]=="NO" and SUKUN in ms: reasons.append("SUKUN_FORBIDDEN")
    if r["AllowShadda"]=="NO" and SHADDA in ms: reasons.append("SHADDA_FORBIDDEN")
    if r["AllowAlifLam"]=="NO" and "".join(letters).startswith(("ال","ٱل")): reasons.append("ALIF_LAM_FORBIDDEN")
    if r["AllowTaMarbuta"]=="NO" and "ة" in letters: reasons.append("TA_MARBUTA_FORBIDDEN")
    if r["AllowAlifMaqsura"]=="NO" and "ى" in letters: reasons.append("ALIF_MAQSURA_FORBIDDEN")
    rc=r["RequireConnected"]
    if rc=="YES" and not is_connected_pair(text): reasons.append("CONNECTED_REQUIRED")
    if rc=="NO" and is_connected_pair(text): reasons.append("CONNECTED_FORBIDDEN")
    rn=r["RequireNonConnector"]
    if rn=="YES" and not has_nonconnector_transition(text): reasons.append("NONCONNECTOR_REQUIRED")
    if rn=="NO" and has_nonconnector_transition(text): reasons.append("NONCONNECTOR_FORBIDDEN")
    return Decision(not reasons, reasons)

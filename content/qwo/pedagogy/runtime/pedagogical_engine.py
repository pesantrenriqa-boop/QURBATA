#!/usr/bin/env python3
from __future__ import annotations

import csv
import unicodedata
from dataclasses import dataclass
from pathlib import Path

SHORT = set("َُِ")
TANWIN = set("ًٌٍ")
SUKUN = "ْ"
SHADDA = "ّ"
DAGGER = "ٰ"
MADDA = "ٓ"
HAMZA_QATA = set("ءأإؤئآ")
HAMZA_WASL = "ٱ"
NON_CONNECTORS = set("ادذرزوأإآؤءٱى")
WAQF_SIGNS = set("ۖۗۚۛۜۙ")
QURAN_ANNOTATIONS = set("ۥۦۭۣ۟ۢۡ۠ۤ") | WAQF_SIGNS
BASE_ARABIC = set("ابتثجحخدذرزسشصضطظعغفقكلمنهويءأإؤئآٱىة")


@dataclass
class Decision:
    passed: bool
    reasons: list[str]


def normalize(text: str) -> str:
    return unicodedata.normalize("NFC", text)


def base_letters(text: str) -> list[str]:
    return [ch for ch in normalize(text) if ch in BASE_ARABIC]


def marks(text: str) -> set[str]:
    return {
        ch for ch in normalize(text)
        if unicodedata.category(ch).startswith("M") and ch not in QURAN_ANNOTATIONS
    }


def grapheme_clusters(text: str) -> list[str]:
    clusters: list[str] = []
    for ch in normalize(text):
        if ch in BASE_ARABIC:
            clusters.append(ch)
        elif unicodedata.category(ch).startswith("M") and clusters and ch not in QURAN_ANNOTATIONS:
            clusters[-1] += ch
    return clusters


def cluster_parts(cluster: str) -> tuple[str, set[str]]:
    return cluster[0], set(cluster[1:])


def has_mad_alif(text: str) -> bool:
    clusters = grapheme_clusters(text)
    for index, cluster in enumerate(clusters):
        base, cluster_marks = cluster_parts(cluster)
        previous_marks = set(clusters[index - 1][1:]) if index else set()
        if base == "ا" and FATHA in previous_marks:
            return True
        if DAGGER in cluster_marks:
            return True
    return DAGGER in text or MADDA in text


FATHA = "َ"
KASRA = "ِ"
DAMMA = "ُ"


def has_mad_ya(text: str) -> bool:
    clusters = grapheme_clusters(text)
    for index, cluster in enumerate(clusters):
        base, cluster_marks = cluster_parts(cluster)
        if base != "ي" or index == 0:
            continue
        previous_marks = set(clusters[index - 1][1:])
        if KASRA in previous_marks and not (cluster_marks & (SHORT | TANWIN | {SHADDA})):
            return True
    return False


def has_mad_waw(text: str) -> bool:
    clusters = grapheme_clusters(text)
    for index, cluster in enumerate(clusters):
        base, cluster_marks = cluster_parts(cluster)
        if base != "و" or index == 0:
            continue
        previous_marks = set(clusters[index - 1][1:])
        if DAMMA in previous_marks and not (cluster_marks & (SHORT | TANWIN | {SHADDA})):
            return True
    return False


def has_madd(text: str) -> bool:
    return has_mad_alif(text) or has_mad_ya(text) or has_mad_waw(text)


def is_connected_pair(text: str) -> bool:
    letters = base_letters(text)
    return len(letters) == 2 and letters[0] not in NON_CONNECTORS


def has_nonconnector_transition(text: str) -> bool:
    letters = base_letters(text)
    return any(ch in NON_CONNECTORS for ch in letters[:-1])


def starts_alif_lam(text: str) -> bool:
    letters = "".join(base_letters(text))
    return letters.startswith(("ال", "ٱل"))


def has_sukun_on(text: str, targets: set[str]) -> bool:
    for cluster in grapheme_clusters(text):
        base, cluster_marks = cluster_parts(cluster)
        if base in targets and SUKUN in cluster_marks:
            return True
    return False


def is_lafzul_jalalah(text: str) -> bool:
    letters = "".join(base_letters(text))
    return "الله" in letters or "ٱلله" in letters


def load_rules(path: str | Path) -> dict[str, dict[str, str]]:
    with open(path, encoding="utf-8", newline="") as handle:
        return {row["CompetencyID"]: row for row in csv.DictReader(handle)}


def require_target_feature(text: str, competency_id: str, reasons: list[str]) -> None:
    letters = base_letters(text)
    ms = marks(text)
    joined = "".join(letters)

    exact_lengths = {
        "C0001": 1, "C0002": 1, "C0003": 1, "C0004": 1,
        "C0005": 2, "C0006": 2, "C0007": 3, "C0012": 4,
    }
    if competency_id in exact_lengths and len(letters) != exact_lengths[competency_id]:
        reasons.append("TARGET_LENGTH")
    if competency_id == "C0013" and len(letters) < 5:
        reasons.append("TARGET_LENGTH")

    if competency_id == "C0002" and FATHA not in ms:
        reasons.append("FATHA_REQUIRED")
    if competency_id == "C0003" and KASRA not in ms:
        reasons.append("KASRA_REQUIRED")
    if competency_id == "C0004" and DAMMA not in ms:
        reasons.append("DAMMA_REQUIRED")
    if competency_id == "C0005" and not has_nonconnector_transition(text):
        reasons.append("NONCONNECTOR_REQUIRED")
    if competency_id == "C0006" and not is_connected_pair(text):
        reasons.append("CONNECTED_REQUIRED")
    if competency_id == "C0011" and not has_nonconnector_transition(text):
        reasons.append("NONCONNECTOR_REQUIRED")

    feature_requirements = {
        "C0014": (has_mad_alif(text), "MAD_ALIF_REQUIRED"),
        "C0015": (has_mad_ya(text), "MAD_YA_REQUIRED"),
        "C0016": (has_mad_waw(text), "MAD_WAW_REQUIRED"),
        "C0017": ("ً" in ms, "TANWIN_FATH_REQUIRED"),
        "C0018": ("ٍ" in ms, "TANWIN_KASR_REQUIRED"),
        "C0019": ("ٌ" in ms, "TANWIN_DAMM_REQUIRED"),
        "C0020": (SUKUN in ms, "SUKUN_REQUIRED"),
        "C0021": (has_sukun_on(text, HAMZA_QATA | {HAMZA_WASL}), "SUKUN_HAMZA_REQUIRED"),
        "C0022": (has_sukun_on(text, {"ع", "غ"}), "SUKUN_AIN_GHAIN_REQUIRED"),
        "C0023": (has_sukun_on(text, set("خصضغطقظ")), "SUKUN_EMPHATIC_REQUIRED"),
        "C0024": (SHADDA in ms, "SHADDA_REQUIRED"),
        "C0025": (starts_alif_lam(text), "ALIF_LAM_REQUIRED"),
        "C0026": ("ة" in letters, "TA_MARBUTA_REQUIRED"),
        "C0027": ("ى" in letters, "ALIF_MAQSURA_REQUIRED"),
        "C0028": (any(ch in HAMZA_QATA for ch in letters), "HAMZA_QATA_REQUIRED"),
        "C0029": (HAMZA_WASL in letters, "HAMZA_WASL_REQUIRED"),
        "C0030": (is_lafzul_jalalah(text), "LAFZ_JALALAH_REQUIRED"),
        "C0031": (is_lafzul_jalalah(text), "LAFZ_JALALAH_REQUIRED"),
        "C0032": (is_lafzul_jalalah(text) and not joined.startswith(("الله", "ٱلله")), "LAFZ_PREFIX_REQUIRED"),
    }
    condition = feature_requirements.get(competency_id)
    if condition and not condition[0]:
        reasons.append(condition[1])


def validate(text: str, object_type: str, competency_id: str, rules: dict[str, dict[str, str]]) -> Decision:
    if competency_id not in rules:
        return Decision(False, ["UNKNOWN_COMPETENCY"])

    rule = rules[competency_id]
    reasons: list[str] = []
    allowed_types = set(rule["AllowedObjectTypes"].split("|"))
    if object_type not in allowed_types:
        reasons.append("OBJECT_TYPE")

    letters = base_letters(text)
    ms = marks(text)
    if not letters:
        reasons.append("NO_ARABIC_BASE_LETTERS")
    if len(letters) > int(rule["MaxBaseLetters"]):
        reasons.append("MAX_LENGTH")

    allowed_letters = set(rule["AllowedBaseLetters"])
    if any(ch not in allowed_letters for ch in letters):
        reasons.append("LETTER_NOT_ALLOWED")

    allowed_marks = set(rule["AllowedMarks"])
    forbidden_marks = set(rule["ForbiddenMarks"])
    if any(mark not in allowed_marks for mark in ms):
        reasons.append("MARK_NOT_ALLOWED")
    if ms & forbidden_marks:
        reasons.append("FORBIDDEN_MARK")

    if rule["AllowHamzaForms"] == "NO" and any(ch in HAMZA_QATA | {HAMZA_WASL} for ch in letters):
        reasons.append("HAMZA_FORBIDDEN")
    if rule["AllowMadd"] == "NO" and has_madd(text):
        reasons.append("MADD_FORBIDDEN")
    if rule["AllowTanwin"] == "NO" and ms & TANWIN:
        reasons.append("TANWIN_FORBIDDEN")
    if rule["AllowSukun"] == "NO" and SUKUN in ms:
        reasons.append("SUKUN_FORBIDDEN")
    if rule["AllowShadda"] == "NO" and SHADDA in ms:
        reasons.append("SHADDA_FORBIDDEN")
    if rule["AllowAlifLam"] == "NO" and starts_alif_lam(text):
        reasons.append("ALIF_LAM_FORBIDDEN")
    if rule["AllowTaMarbuta"] == "NO" and "ة" in letters:
        reasons.append("TA_MARBUTA_FORBIDDEN")
    if rule["AllowAlifMaqsura"] == "NO" and "ى" in letters:
        reasons.append("ALIF_MAQSURA_FORBIDDEN")

    require_connected = rule["RequireConnected"]
    if require_connected == "YES" and not is_connected_pair(text):
        reasons.append("CONNECTED_REQUIRED")
    if require_connected == "NO" and is_connected_pair(text):
        reasons.append("CONNECTED_FORBIDDEN")

    require_nonconnector = rule["RequireNonConnector"]
    if require_nonconnector == "YES" and not has_nonconnector_transition(text):
        reasons.append("NONCONNECTOR_REQUIRED")
    if require_nonconnector == "NO" and has_nonconnector_transition(text):
        reasons.append("NONCONNECTOR_FORBIDDEN")

    require_target_feature(text, competency_id, reasons)
    return Decision(not reasons, sorted(set(reasons)))

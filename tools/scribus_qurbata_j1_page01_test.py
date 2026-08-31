# -*- coding: utf-8 -*-
import os
import csv

import scribus

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SOURCE_CSV = os.path.join(REPO_ROOT, "dist", "indesign-template-data", "QURBATA-INDESIGN-J1-4COL-8ROW-FULL-REFINED.csv")
COMP_TSV = os.path.join(REPO_ROOT, "dist", "indesign-template-data", "QURBATA-J1-40P-COMPETENCY.tsv")
OUTPUT_SLA = os.path.join(REPO_ROOT, "dist", "scribus", "QURBATA-J1-PAGE01-TEST-NATIVE.sla")

PAGE_W = 148.0
PAGE_H = 210.0
MARGIN = 13.0
GRID_Y = 55.0
GRID_W = PAGE_W - 2 * MARGIN
GRID_H = 120.0
GAP_X = 2.2
GAP_Y = 1.6
CELL_W = (GRID_W - 3 * GAP_X) / 4.0
CELL_H = (GRID_H - 7 * GAP_Y) / 8.0

FONT_LATIN_CANDIDATES = ["Arial", "Arial Regular", "Liberation Sans"]
FONT_ARABIC_CANDIDATES = [
    "KFGQPC Uthman Taha Naskh",
    "KFGQPC Uthman Taha Naskh Regular",
    "Amiri Quran",
    "Amiri"
]

def choose_font(candidates):
    fonts = set(scribus.getFontNames())
    for name in candidates:
        if name in fonts:
            return name
    return None

def load_page1():
    with open(SOURCE_CSV, "r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    page = next((r for r in rows if str(r.get("PageNumber", "")).strip() == "1"), None)
    if not page:
        raise RuntimeError("Page 1 data not found")

    with open(COMP_TSV, "r", encoding="utf-8-sig", newline="") as f:
        comps = list(csv.DictReader(f, delimiter="\t"))
    comp = next((r for r in comps if str(r.get("PageNumber", "")).strip() == "1"), None)
    if not comp:
        raise RuntimeError("Page 1 competency not found")

    cells = []
    for rr in range(1, 9):
        for cc in range(1, 5):
            key = "Row%02dCell%02d" % (rr, cc)
            value = str(page.get(key, "")).strip()
            if not value:
                raise RuntimeError("Empty Page-1 cell: %s" % key)
            cells.append(value)
    return page, comp, cells

def text_frame(x, y, w, h, text, font, size, name, align=scribus.ALIGN_CENTERED):
    frame = scribus.createText(x, y, w, h, name)
    scribus.insertText(text, 0, frame)
    if font:
        scribus.setFont(font, frame)
    scribus.setFontSize(size, frame)
    scribus.setTextAlignment(align, frame)
    try:
        scribus.setTextVerticalAlignment(scribus.ALIGNV_CENTERED, frame)
    except Exception:
        pass
    return frame

def grid_cell(x, y, w, h, text, font, name):
    frame = text_frame(x, y, w, h, text, font, 24, name, scribus.ALIGN_CENTERED)
    scribus.setLineColor("Black", frame)
    scribus.setLineWidth(0.7, frame)
    scribus.setFillColor("None", frame)
    return frame

def main():
    if not os.path.exists(SOURCE_CSV):
        raise RuntimeError("Source CSV not found: " + SOURCE_CSV)
    if not os.path.exists(COMP_TSV):
        raise RuntimeError("Competency TSV not found: " + COMP_TSV)

    page, comp, cells = load_page1()

    latin = choose_font(FONT_LATIN_CANDIDATES)
    arabic = choose_font(FONT_ARABIC_CANDIDATES)

    if not arabic:
        raise RuntimeError(
            "Arabic font not found in Scribus. Install/enable one of: " +
            ", ".join(FONT_ARABIC_CANDIDATES)
        )

    if scribus.haveDoc():
        scribus.closeDoc()

    ok = scribus.newDocument(
        (PAGE_W, PAGE_H),
        (MARGIN, MARGIN, 10.0, 10.0),
        scribus.PORTRAIT,
        1,
        scribus.UNIT_MILLIMETERS,
        scribus.NOFACINGPAGES,
        scribus.FIRSTPAGERIGHT,
        1
    )
    if not ok:
        raise RuntimeError("Scribus could not create the A5 document")

    text_frame(13, 11, 122, 8, "QURBATA JILID 1", latin, 9, "Header")
    text_frame(
        13, 27, 122, 7,
        "%s - %s" % (comp["CompetencyCode"], comp["CompetencyTitle"]),
        latin, 10, "CompetencyTitle"
    )
    text_frame(
        13, 35, 122, 12,
        "Target: " + comp["CompetencyTarget"],
        latin, 7.5, "CompetencyTarget"
    )

    i = 0
    for rr in range(8):
        for cc in range(4):
            x = MARGIN + cc * (CELL_W + GAP_X)
            y = GRID_Y + rr * (CELL_H + GAP_Y)
            grid_cell(x, y, CELL_W, CELL_H, cells[i], arabic, "R%dC%d" % (rr + 1, cc + 1))
            i += 1

    text_frame(13, 188, 35, 7, "QURBATA - JILID 1", latin, 7, "FooterLeft")
    text_frame(48, 188, 87, 7, "تَعَلَّمْ - اِعْمَلْ - عَلِّمْ", arabic, 8, "FooterCenter")

    out_dir = os.path.dirname(OUTPUT_SLA)
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    scribus.saveDocAs(OUTPUT_SLA)
    scribus.redrawAll()

    scribus.messageBox(
        "QURBATA Scribus",
        "Page 1 native test selesai.\n\n"
        "Cells: 32/32\n"
        "Competency: %s - %s\n"
        "Arabic font: %s\n\n"
        "Saved: %s" % (
            comp["CompetencyCode"],
            comp["CompetencyTitle"],
            arabic,
            OUTPUT_SLA
        ),
        scribus.ICON_INFORMATION,
        scribus.BUTTON_OK
    )

main()

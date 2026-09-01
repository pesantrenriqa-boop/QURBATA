# -*- coding: utf-8 -*-
import os
import csv
import scribus

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SOURCE_CSV = os.path.join(REPO_ROOT, "dist", "indesign-template-data", "QURBATA-INDESIGN-J1-4COL-8ROW-FULL-REFINED.csv")
COMP_TSV = os.path.join(REPO_ROOT, "dist", "indesign-template-data", "QURBATA-J1-40P-COMPETENCY.tsv")
SPECIAL_CSV = os.path.join(REPO_ROOT, "data", "indesign", "QURBATA-J1-SPECIAL-PAGES.csv")
SPECIAL_CONTENT_CSV = os.path.join(REPO_ROOT, "data", "indesign", "QURBATA-J1-SPECIAL-CONTENT.csv")
INTEGRATION_CSV = os.path.join(REPO_ROOT, "data", "indesign", "QURBATA-J1-40P-INTEGRATION-MASTER.csv")
OUTPUT_SLA = os.path.join(REPO_ROOT, "dist", "scribus", "QURBATA-JILID-1-PRODUCTION-40P.sla")

PAGE_W = 148.0
PAGE_H = 210.0
MARGIN = 13.0

HEADER_Y = 9.0
TITLE_Y = 22.0
TARGET_Y = 30.0
GRID_Y = 58.0
GRID_W = PAGE_W - 2 * MARGIN
GRID_H = 116.0
GAP_X = 2.2
GAP_Y = 1.6
CELL_W = (GRID_W - 3 * GAP_X) / 4.0
CELL_H = (GRID_H - 7 * GAP_Y) / 8.0

FOOTER_Y = 187.0

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

def load_csv(path, delimiter=","):
    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f, delimiter=delimiter))

def load_data():
    if not os.path.exists(SOURCE_CSV):
        raise RuntimeError("Source CSV not found: " + SOURCE_CSV)
    if not os.path.exists(COMP_TSV):
        raise RuntimeError("Competency TSV not found: " + COMP_TSV)
    if not os.path.exists(SPECIAL_CSV):
        raise RuntimeError("Special-page manifest not found: " + SPECIAL_CSV)

    tartil_rows = load_csv(SOURCE_CSV)
    comp_rows = load_csv(COMP_TSV, "\t")
    special_rows = load_csv(SPECIAL_CSV)
    if not os.path.exists(SPECIAL_CONTENT_CSV):
        raise RuntimeError("Special content master not found: " + SPECIAL_CONTENT_CSV)
    special_content_rows = load_csv(SPECIAL_CONTENT_CSV)
    if not os.path.exists(INTEGRATION_CSV):
        raise RuntimeError("Integration master not found: " + INTEGRATION_CSV)
    integration_rows = load_csv(INTEGRATION_CSV)

    tartil = {int(r["PageNumber"]): r for r in tartil_rows}
    comps = {int(r["PageNumber"]): r for r in comp_rows}
    specials = {int(r["PageNumber"]): r for r in special_rows}
    special_content = {int(r["PageNumber"]): r for r in special_content_rows}
    integration = {int(r["PageNumber"]): r for r in integration_rows}
    if len(integration) != 40:
        raise RuntimeError("Integration master must contain 40 rows; found %d" % len(integration))

    if len(comps) != 40:
        raise RuntimeError("Competency register must contain 40 rows; found %d" % len(comps))

    expected_tartil = [n for n in range(1, 41) if n not in specials]
    missing = [n for n in expected_tartil if n not in tartil]
    if missing:
        raise RuntimeError("Missing Tartil page data: " + ", ".join(map(str, missing)))

    return tartil, comps, specials, special_content, integration

def set_frame_text(frame, text, font, size, align=scribus.ALIGN_CENTERED):
    scribus.setText(text, frame)
    if font:
        scribus.setFont(font, frame)
    scribus.setFontSize(size, frame)
    scribus.setTextColor("Black", frame)
    scribus.setTextAlignment(align, frame)
    try:
        scribus.setTextVerticalAlignment(scribus.ALIGNV_CENTERED, frame)
    except Exception:
        pass

def text_frame(x, y, w, h, text, font, size, name, align=scribus.ALIGN_CENTERED, line_width=0.0):
    frame = scribus.createText(x, y, w, h, name)
    set_frame_text(frame, text, font, size, align)
    scribus.setFillColor("None", frame)
    scribus.setLineColor("Black", frame)
    scribus.setLineWidth(line_width, frame)
    return frame

def fit_text(frame, start_size, minimum=7.0, step=0.5):
    size = start_size
    scribus.setFontSize(size, frame)
    while scribus.textOverflows(frame) and size - step >= minimum:
        size -= step
        scribus.setFontSize(size, frame)
    return (not scribus.textOverflows(frame), size)

def create_page_shell(page_num, latin):
    text_frame(MARGIN, HEADER_Y, GRID_W, 7.0, "QURBATA JILID 1", latin, 8.5, "P%02d_Header" % page_num, line_width=0.7)
    text_frame(MARGIN, FOOTER_Y, 35.0, 7.0, "QURBATA - JILID 1", latin, 6.5, "P%02d_FooterLeft" % page_num, line_width=0.7)

def add_footer_arabic(page_num, arabic):
    frame = text_frame(48.0, FOOTER_Y, 87.0, 7.0, "تَعَلَّمْ - اِعْمَلْ - عَلِّمْ", arabic, 8.0, "P%02d_FooterArabic" % page_num, line_width=0.7)
    fit_text(frame, 8.0, 6.0, 0.5)

def add_competency(page_num, comp, latin):
    title = "%s - %s" % (comp["CompetencyCode"], comp["CompetencyTitle"])
    tf = text_frame(MARGIN, TITLE_Y, GRID_W, 7.0, title, latin, 9.5, "P%02d_CompetencyTitle" % page_num, line_width=0.7)
    fit_text(tf, 9.5, 7.5, 0.5)

    target = "Target: " + comp["CompetencyTarget"]
    tg = text_frame(MARGIN, TARGET_Y, GRID_W, 13.0, target, latin, 7.2, "P%02d_CompetencyTarget" % page_num, line_width=0.7)
    fit_text(tg, 7.2, 5.5, 0.4)

def add_integration_strip(page_num, integration, latin, arabic):
    # Compact per-meeting integration strip. Pending items remain visually blank;
    # workflow/status text is never printed in the learner book.
    x = MARGIN
    y = 43.5
    w = GRID_W
    h = 12.0
    col_w = w / 3.0

    items = [
        ("Tahfidz", integration.get("TahfidzText", "").strip(), integration.get("TahfidzRef", "").strip()),
        ("Bahasa Arab", integration.get("BahasaArabText", "").strip(), integration.get("BahasaArabMeaning", "").strip()),
        ("NIDOM", integration.get("NidomText", "").strip(), integration.get("NidomMeaning", "").strip()),
    ]

    for idx, item in enumerate(items):
        label, primary, secondary = item
        bx = x + idx * col_w
        text_frame(bx, y, col_w, 4.0, label, latin, 5.8, "P%02d_IntLabel%d" % (page_num, idx + 1), line_width=0.5)
        if primary:
            use_arabic = any("\u0600" <= ch <= "\u06ff" for ch in primary)
            pf = text_frame(bx, y + 4.0, col_w, 5.0, primary, arabic if use_arabic else latin, 8.0 if use_arabic else 6.2, "P%02d_IntPrimary%d" % (page_num, idx + 1), align=(scribus.ALIGN_RIGHT if use_arabic else scribus.ALIGN_CENTERED), line_width=0.5)
            if use_arabic:
                scribus.setTextDirection(scribus.DIRECTION_RTL, pf)
                scribus.setTextAlignment(scribus.ALIGN_RIGHT, pf)
            fit_text(pf, 8.0 if use_arabic else 6.2, 5.0, 0.5)
            if use_arabic:
                scribus.setTextDirection(scribus.DIRECTION_RTL, pf)
                scribus.setTextAlignment(scribus.ALIGN_RIGHT, pf)
        else:
            text_frame(bx, y + 4.0, col_w, 5.0, "", latin, 6.0, "P%02d_IntPrimary%d" % (page_num, idx + 1), line_width=0.5)
        if secondary:
            sf = text_frame(bx, y + 9.0, col_w, 3.0, secondary, latin, 4.8, "P%02d_IntSecondary%d" % (page_num, idx + 1), line_width=0.5)
            fit_text(sf, 4.8, 4.0, 0.4)


def add_tartil_grid(page_num, row, arabic):
    cells = []
    for rr in range(1, 9):
        for cc in range(1, 5):
            key = "Row%02dCell%02d" % (rr, cc)
            value = str(row.get(key, "")).strip()
            if not value:
                raise RuntimeError("Empty cell on page %d: %s" % (page_num, key))
            cells.append(value)

    i = 0
    for rr in range(8):
        for cc in range(4):
            x = MARGIN + cc * (CELL_W + GAP_X)
            y = GRID_Y + rr * (CELL_H + GAP_Y)
            name = "P%02d_R%dC%d" % (page_num, rr + 1, cc + 1)

            # Outer cell border is a rectangle, not a text frame.
            box = scribus.createRect(x, y, CELL_W, CELL_H, name + "_BOX")
            scribus.setFillColor("None", box)
            scribus.setLineColor("Black", box)
            scribus.setLineWidth(0.7, box)

            # Arabic content uses a separate, borderless text frame physically
            # anchored to the RIGHT side. Its width is deliberately compact so
            # even if Scribus falls back to left paragraph positioning, the text
            # itself still lives on the right side of the cell.
            inner_w = CELL_W * 0.78
            right_pad = 1.0
            inner_x = x + CELL_W - inner_w - right_pad
            frame = scribus.createText(inner_x, y, inner_w, CELL_H, name)
            scribus.setFillColor("None", frame)
            scribus.setLineColor("None", frame)
            scribus.setLineWidth(0.0, frame)
            scribus.setText(cells[i], frame)
            if arabic:
                scribus.setFont(arabic, frame)
            scribus.setFontSize(24.0, frame)
            scribus.setTextColor("Black", frame)
            try:
                scribus.setTextVerticalAlignment(scribus.ALIGNV_CENTERED, frame)
            except Exception:
                pass

            # Apply RTL/right alignment to the stored paragraph.
            scribus.selectText(0, scribus.getTextLength(frame), frame)
            scribus.setTextDirection(scribus.DIRECTION_RTL, frame)
            scribus.setTextAlignment(scribus.ALIGN_RIGHT, frame)
            ok, final_size = fit_text(frame, 24.0, 13.0, 0.5)
            scribus.selectText(0, scribus.getTextLength(frame), frame)
            scribus.setTextDirection(scribus.DIRECTION_RTL, frame)
            scribus.setTextAlignment(scribus.ALIGN_RIGHT, frame)

            if scribus.getTextLength(frame) <= 0:
                raise RuntimeError("Arabic text did not insert: " + name)
            if not ok:
                raise RuntimeError("Unresolved Tartil overflow: %s (%.1f pt)" % (name, final_size))
            i += 1

def add_special_page(page_num, spec, content, comp, latin, arabic):
    title = content.get("Title", "").strip() or comp["CompetencyTitle"]
    text_frame(MARGIN, 54.0, GRID_W, 15.0, title, latin, 16.0, "P%02d_SpecialTitle" % page_num, line_width=0.7)
    primary = content.get("PrimaryText", "").strip()
    secondary = content.get("SecondaryText", "").strip()
    instruction = content.get("Instruction", "").strip()
    if primary:
        use_arabic = any("\u0600" <= ch <= "\u06ff" for ch in primary)
        size = 22.0 if use_arabic else 13.0
        pf = text_frame(MARGIN + 8, 76.0, GRID_W - 16, 24.0, primary, arabic if use_arabic else latin, size, "P%02d_SpecialPrimary" % page_num, line_width=0.7)
        fit_text(pf, size, 11.0, 0.5)
    if secondary:
        sf = text_frame(MARGIN + 8, 104.0, GRID_W - 16, 12.0, secondary, latin, 9.5, "P%02d_SpecialSecondary" % page_num, line_width=0.7)
        fit_text(sf, 9.5, 7.0, 0.5)
    inf = text_frame(MARGIN + 8, 123.0, GRID_W - 16, 34.0, instruction, latin, 9.0, "P%02d_SpecialInstruction" % page_num, line_width=0.7)
    fit_text(inf, 9.0, 7.0, 0.5)
    add_footer_arabic(page_num, arabic)

def validate_document(tartil_pages):
    bad = []
    for page_num in tartil_pages:
        for rr in range(1, 9):
            for cc in range(1, 5):
                name = "P%02d_R%dC%d" % (page_num, rr, cc)
                try:
                    if scribus.getTextLength(name) <= 0 or scribus.textOverflows(name):
                        bad.append(name)
                except Exception:
                    bad.append(name)
    return bad

def hide_scribus_frame_edges_in_saved_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = f.read()
        data = data.replace('SHOWFRAME="1"', 'SHOWFRAME="0"', 1)
        with open(path, "w", encoding="utf-8") as f:
            f.write(data)
    except Exception:
        pass


def main():
    tartil, comps, specials, special_content, integration = load_data()

    latin = choose_font(FONT_LATIN_CANDIDATES)
    arabic = choose_font(FONT_ARABIC_CANDIDATES)
    if not latin:
        raise RuntimeError("Latin font not found: " + ", ".join(FONT_LATIN_CANDIDATES))
    if not arabic:
        raise RuntimeError("Arabic font not found: " + ", ".join(FONT_ARABIC_CANDIDATES))

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
        raise RuntimeError("Scribus could not create A5 document")

    try:
        scribus.setRedraw(False)
    except Exception:
        pass

    tartil_page_numbers = []

    try:
        for page_num in range(1, 41):
            if page_num > 1:
                scribus.newPage(-1)
                scribus.gotoPage(page_num)

            create_page_shell(page_num, latin)
            add_competency(page_num, comps[page_num], latin)
            add_integration_strip(page_num, integration[page_num], latin, arabic)

            if page_num in specials:
                if page_num not in special_content:
                    raise RuntimeError("Special content missing for page %d" % page_num)
                add_special_page(page_num, specials[page_num], special_content[page_num], comps[page_num], latin, arabic)
            else:
                add_tartil_grid(page_num, tartil[page_num], arabic)
                add_footer_arabic(page_num, arabic)
                tartil_page_numbers.append(page_num)

        bad = validate_document(tartil_page_numbers)
        if bad:
            raise RuntimeError("Final Tartil validation failed: " + ", ".join(bad[:20]))

        out_dir = os.path.dirname(OUTPUT_SLA)
        if not os.path.isdir(out_dir):
            os.makedirs(out_dir)

        scribus.saveDocAs(OUTPUT_SLA)

        # Hide Scribus editing-frame edges in the saved document. These are not
        # printable borders; turning them off keeps the Tartil grid visually clean.
        try:
            scribus.closeDoc()
            hide_scribus_frame_edges_in_saved_file(OUTPUT_SLA)
            scribus.openDoc(OUTPUT_SLA)
        except Exception:
            pass

    finally:
        try:
            scribus.setRedraw(True)
            scribus.redrawAll()
        except Exception:
            pass

    scribus.messageBox(
        "QURBATA Scribus",
        "Jilid 1 production selesai.\n\n"
        "Pages: 40\n"
        "Tartil pages: 36\n"
        "Special pages: 4\n"
        "Tartil cells: 1152/1152\n"
        "Arabic font: %s\n\n"
        "Saved: %s" % (arabic, OUTPUT_SLA),
        scribus.ICON_INFORMATION,
        scribus.BUTTON_OK
    )

main()

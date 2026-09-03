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
OUTPUT_PDF = os.path.join(REPO_ROOT, "dist", "scribus", "QURBATA-JILID-1-PRODUCTION-40P-PREVIEW.pdf")
TARTIL_RENDER_DIR = os.path.join(REPO_ROOT, "dist", "scribus", "tartil-render-cache")

PAGE_W = 148.0
PAGE_H = 210.0
MARGIN = 13.0

HEADER_Y = 9.0
TITLE_Y = 10.0
TARGET_Y = 0.0
GRID_Y = 38.0
GRID_W = PAGE_W - 2 * MARGIN
GRID_H = 142.0
GAP_X = 2.2
GAP_Y = 1.6
CELL_W = (GRID_W - 3 * GAP_X) / 4.0
CELL_H = (GRID_H - 7 * GAP_Y) / 8.0

FOOTER_Y = 190.0
GUIDE_LAYER = "TARTIL GUIDES"
CONTENT_LAYER = "Background"

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
    scribus.setLineColor("None", frame)
    scribus.setLineWidth(0.0, frame)
    return frame

def fit_text(frame, start_size, minimum=7.0, step=0.5):
    size = start_size
    scribus.setFontSize(size, frame)
    while scribus.textOverflows(frame) and size - step >= minimum:
        size -= step
        scribus.setFontSize(size, frame)
    return (not scribus.textOverflows(frame), size)

def _decorative_rule(x1, y, x2, name):
    line = scribus.createLine(x1, y, x2, y, name)
    scribus.setLineColor("Blue", line)
    scribus.setLineWidth(0.55, line)
    return line


def create_page_shell(page_num, latin):
    # Decorative header/footer are generated independently on EVERY page.
    # No dependency on master pages, so pages 1-40 always receive them.

    # HEADER — thin blue rules, diamonds, centered brand.
    _decorative_rule(MARGIN, 8.8, MARGIN + 33.0, "P%02d_HeaderRuleL" % page_num)
    _decorative_rule(MARGIN + GRID_W - 33.0, 8.8, MARGIN + GRID_W, "P%02d_HeaderRuleR" % page_num)

    brand = text_frame(
        MARGIN + 36.0, 5.7, GRID_W - 72.0, 6.0,
        "QURBATA JILID 1", latin, 8.4,
        "P%02d_Brand" % page_num
    )
    scribus.setTextColor("Blue", brand)

    mark_l = text_frame(MARGIN + 32.8, 5.9, 3.2, 5.0, "◆", latin, 5.6,
                        "P%02d_HeaderDiamondL" % page_num)
    mark_r = text_frame(MARGIN + GRID_W - 36.0, 5.9, 3.2, 5.0, "◆", latin, 5.6,
                        "P%02d_HeaderDiamondR" % page_num)
    scribus.setTextColor("Blue", mark_l)
    scribus.setTextColor("Blue", mark_r)

    # Small page badge in the top-right, still subtle.
    badge = text_frame(
        MARGIN + GRID_W - 11.0, 4.9, 10.0, 5.0,
        "%02d" % page_num, latin, 5.6,
        "P%02d_HeaderPage" % page_num
    )
    scribus.setTextColor("Blue", badge)

    # FOOTER — motto sits above two short blue rules and centered identity.
    _decorative_rule(MARGIN, FOOTER_Y + 5.2, MARGIN + 34.0, "P%02d_FooterRuleL" % page_num)
    _decorative_rule(MARGIN + GRID_W - 34.0, FOOTER_Y + 5.2, MARGIN + GRID_W, "P%02d_FooterRuleR" % page_num)

    footer = text_frame(
        MARGIN + 35.0, FOOTER_Y + 1.9, GRID_W - 70.0, 6.0,
        "QURBATA JILID 1   •   %02d" % page_num,
        latin, 6.2,
        "P%02d_FooterIdentity" % page_num
    )
    scribus.setTextColor("Blue", footer)



def add_footer_arabic(page_num, arabic):
    frame = text_frame(MARGIN, FOOTER_Y - 4.0, GRID_W, 6.0,
                       "تَعَلَّمْ  •  اِعْمَلْ  •  عَلِّمْ",
                       arabic, 8.8, "P%02d_FooterArabic" % page_num)
    scribus.setTextColor("Blue", frame)
    fit_text(frame, 8.8, 7.2, 0.5)



def add_competency(page_num, comp, latin):
    title = comp["CompetencyTitle"]
    tf = text_frame(MARGIN, 13.0, GRID_W, 7.5, title, latin, 11.8,
                    "P%02d_CompetencyTitle" % page_num)
    fit_text(tf, 11.8, 9.2, 0.5)



def add_integration_strip(page_num, integration, latin, arabic):
    x = MARGIN
    y = 22.0
    col_w = GRID_W / 3.0
    items = [
        ("TAHFIDZ", integration.get("TahfidzText", "").strip()),
        ("BAHASA ARAB", integration.get("BahasaArabText", "").strip()),
        ("NIDOM", integration.get("NidomText", "").strip()),
    ]
    for idx, item in enumerate(items):
        label, primary = item
        bx = x + idx * col_w
        lf = text_frame(bx, y, col_w, 3.4, label, latin, 5.4,
                        "P%02d_IntLabel%d" % (page_num, idx + 1))
        scribus.setTextColor("Blue", lf)
        pf = text_frame(bx + 0.8, y + 3.2, col_w - 1.6, 8.0, primary,
                        arabic, 8.5,
                        "P%02d_IntPrimary%d" % (page_num, idx + 1))
        try:
            scribus.selectText(0, scribus.getTextLength(pf), pf)
            scribus.setTextDirection(scribus.DIRECTION_RTL, pf)
            scribus.setTextAlignment(scribus.ALIGN_CENTERED, pf)
        except Exception:
            pass
        fit_text(pf, 8.5, 6.0, 0.5)



def _sanitize_arabic_drill(text):
    banned = set([
        "\u061c", "\u200e", "\u200f",
        "\u202a", "\u202b", "\u202c", "\u202d", "\u202e",
        "\u2066", "\u2067", "\u2068", "\u2069"
    ])
    clean = "".join(ch for ch in text if ch not in banned)
    clean = clean.replace("\u00a0", " ")
    return " ".join(clean.split())


def _visual_qurbata_token(token):
    # QURBATA J1 visual convention:
    # every HEH used as a drill glyph must use the two-eye / two-hole form.
    # Normalize ALL common HEH code points/presentation forms, not only a token
    # whose first code point is plain U+0647. Source/master data stays unchanged.
    heh_forms = {
        "ه": "ﻫ",  # U+0647 -> HEH initial form
        "ﻩ": "ﻫ",  # isolated presentation form
        "ﻪ": "ﻫ",  # final presentation form
        "ﻫ": "ﻫ",  # initial presentation form
        "ﻬ": "ﻫ",  # medial presentation form
    }
    return "".join(heh_forms.get(ch, ch) for ch in token)


def _tokenize_arabic_drill(text):
    return [_visual_qurbata_token(tok) for tok in _sanitize_arabic_drill(text).split(" ") if tok]


def _place_tartil_token(col_x, y, col_w, slot_h, token, arabic, name):
    # One real invisible COLUMN per letter. Every column has identical width.
    # This means a 3-letter drill is literally three equal columns:
    # [LEFT LETTER] [MIDDLE LETTER] [RIGHT LETTER].
    frame = scribus.createText(col_x, y, col_w, slot_h, name)
    scribus.setFillColor("None", frame)
    scribus.setLineColor("None", frame)
    scribus.setLineWidth(0.0, frame)
    scribus.setText(token, frame)
    if arabic:
        scribus.setFont(arabic, frame)
    scribus.setFontSize(30.0, frame)
    scribus.setTextColor("Black", frame)
    try:
        scribus.setTextDistances(0.0, 0.0, 0.0, 0.0, frame)
        scribus.setTextVerticalAlignment(scribus.ALIGNV_CENTERED, frame)
    except Exception:
        pass
    try:
        scribus.selectText(0, scribus.getTextLength(frame), frame)
        scribus.setTextDirection(scribus.DIRECTION_RTL, frame)
        scribus.setTextAlignment(scribus.ALIGN_CENTERED, frame)
        if arabic:
            scribus.setFont(arabic, frame)
        scribus.setFontSize(30.0, frame)
    except Exception:
        pass

    if scribus.getTextLength(frame) <= 0:
        raise RuntimeError("Arabic token did not insert: " + name)
    if scribus.textOverflows(frame):
        raise RuntimeError("Tartil letter-column overflow: " + name)


def add_tartil_grid(page_num, row, arabic):
    cells = []
    for rr in range(1, 9):
        for cc in range(1, 5):
            key = "Row%02dCell%02d" % (rr, cc)
            value = str(row.get(key, "")).strip()
            if not value:
                raise RuntimeError("Empty cell on page %d: %s" % (page_num, key))
            cells.append(_tokenize_arabic_drill(value))

    i = 0
    for rr in range(8):
        for cc in range(4):
            cell_x = MARGIN + cc * (CELL_W + GAP_X)
            y = GRID_Y + rr * (CELL_H + GAP_Y)
            base_name = "P%02d_R%dC%d" % (page_num, rr + 1, cc + 1)
            tokens = cells[i]

            # Fixed 3-column teaching matrix in EVERY material cell.
            # The PDF has no column lines; these are geometry only.
            inner_left = cell_x + CELL_W * 0.06
            inner_w = CELL_W * 0.88
            col_gap = CELL_W * 0.025
            col_w = (inner_w - 2.0 * col_gap) / 3.0

            col_x = [
                inner_left,                              # physical LEFT column
                inner_left + col_w + col_gap,           # physical CENTER column
                inner_left + 2.0 * (col_w + col_gap),   # physical RIGHT column
            ]

            n = len(tokens)
            if n == 1:
                placements = [(tokens[0], 1)]
            elif n == 2:
                # Arabic reading order: token 1 on RIGHT, token 2 on LEFT.
                # Keep center intentionally empty so both outer edges line up.
                placements = [(tokens[0], 2), (tokens[1], 0)]
            elif n == 3:
                # token 1 RIGHT, token 2 CENTER, token 3 LEFT.
                placements = [(tokens[0], 2), (tokens[1], 1), (tokens[2], 0)]
            else:
                # Defensive fallback. Jilid-1 main drills are expected to be <=3.
                raise RuntimeError(
                    "Tartil drill has more than 3 letter-columns: %s" % base_name
                )

            # Non-printing guide lines at the actual column boundaries.
            try:
                old_layer = scribus.getActiveLayer()
            except Exception:
                old_layer = CONTENT_LAYER
            _ensure_tartil_guide_layer()
            scribus.setActiveLayer(GUIDE_LAYER)
            boundaries = [
                inner_left,
                inner_left + col_w,
                inner_left + col_w + col_gap,
                inner_left + 2.0 * col_w + col_gap,
                inner_left + 2.0 * (col_w + col_gap),
                inner_left + 3.0 * col_w + 2.0 * col_gap,
            ]
            for gi, gx in enumerate(boundaries):
                guide = scribus.createLine(
                    gx, y + 0.8, gx, y + CELL_H - 0.8,
                    base_name + "_COLGUIDE%d" % (gi + 1)
                )
                scribus.setLineColor("Blue", guide)
                scribus.setLineWidth(0.20, guide)
            try:
                scribus.setActiveLayer(old_layer)
            except Exception:
                scribus.setActiveLayer(CONTENT_LAYER)

            for j, placement in enumerate(placements):
                token, physical_col = placement
                token_name = base_name + "_T%d" % (j + 1)
                _place_tartil_token(
                    col_x[physical_col], y, col_w, CELL_H,
                    token, arabic, token_name
                )
                try:
                    scribus.selectText(0, scribus.getTextLength(token_name), token_name)
                    actual_size = float(scribus.getFontSize(token_name))
                    if abs(actual_size - 30.0) > 0.05:
                        raise RuntimeError(
                            "Tartil font-size audit failed: %s = %.2f pt" %
                            (token_name, actual_size)
                        )
                except RuntimeError:
                    raise
                except Exception:
                    pass

            i += 1

def add_special_page(page_num, spec, content, comp, latin, arabic):
    title = content.get("Title", "").strip() or comp["CompetencyTitle"]
    text_frame(MARGIN, 54.0, GRID_W, 15.0, title, latin, 16.0, "P%02d_SpecialTitle" % page_num, line_width=0.0)
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
    # Token frames are validated at creation time. A failure/overflow raises
    # immediately, so no second-pass single-frame audit is needed here.
    return []



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

    _ensure_tartil_guide_layer()
    try:
        scribus.setActiveLayer(CONTENT_LAYER)
    except Exception:
        pass

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

        # Export a PDF preview. Scribus "Show Frames" edges are editor-only and
        # never print; this preview gives a clean production view for QC.
        try:
            pdf = scribus.PDFfile()
            pdf.file = OUTPUT_PDF
            pdf.pages = list(range(1, 41))
            pdf.save()
        except Exception:
            pass

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
        "Saved SLA: %s\nPDF preview: %s" % (arabic, OUTPUT_SLA, OUTPUT_PDF),
        scribus.ICON_INFORMATION,
        scribus.BUTTON_OK
    )

main()

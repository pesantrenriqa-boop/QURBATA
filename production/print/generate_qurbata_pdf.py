#!/usr/bin/env python3
"""Generate participant-facing QURBATA print PDFs from controlled Markdown pages."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

from pypdf import PdfReader
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A5
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph


TEACHER_SECTION = "## Segmen Bahasa Arab 5 Menit"
ARABIC_RE = re.compile(r"[\u0600-\u06ff]")
EXERCISE_RE = re.compile(
    r"^\|\s*(\d+)\s*\|\s*(QJ\d+-P\d+-(?:L|ASM\d+-I)\d+)\s*\|\s*(.*?)\s*\|$"
)


@dataclass(frozen=True)
class PrintPage:
    code: str
    title: str
    exercises: tuple[str, ...]
    advice: str
    status: str
    kind: str
    arabic_focus: str


SPECIAL_PAGE_CODES = {"QJ1-P018", "QJ1-P028", "QJ1-P036", "QJ1-P038"}
TRIM_PAGE = A5


def parse_page(path: Path) -> PrintPage:
    source = path.read_text(encoding="utf-8")
    participant_source = source.split(TEACHER_SECTION, 1)[0]
    heading = re.search(r"^#\s+(QJ\d+-P\d+)\s+—\s+(.+)$", participant_source, re.M)
    if not heading:
        raise ValueError(f"{path}: heading/code not found")

    status_match = re.search(r"^\*\*Status:\*\*\s*(.+?)\s*$", participant_source, re.M)
    advice_match = re.search(
        r"^##\s+\d+\.\s+Tema Akhlak\s*$.*?^>\s*(.+?)\s*$",
        participant_source,
        re.M | re.S,
    )
    arabic_focus_match = re.search(
        r"^-\s+\*\*Fokus lisan:\*\*\s*(.+?)\s*$",
        source,
        re.M,
    )
    exercises = []
    for line in participant_source.splitlines():
        match = EXERCISE_RE.match(line)
        if match:
            exercises.append(match.group(3).strip())

    code = heading.group(1)
    if len(exercises) not in (0, 24):
        raise ValueError(f"{path}: expected 24 exercises/samples, found {len(exercises)}")
    if not exercises and code not in SPECIAL_PAGE_CODES:
        raise ValueError(f"{path}: missing participant exercises on a non-special page")
    if any(not ARABIC_RE.search(item) for item in exercises):
        raise ValueError(f"{path}: a participant exercise has no Arabic character")

    return PrintPage(
        code=code,
        title=heading.group(2).strip(),
        exercises=tuple(exercises),
        advice=(advice_match.group(1).strip() if advice_match else ""),
        status=(status_match.group(1).strip() if status_match else "Draf"),
        kind=("exercise" if exercises else "special"),
        arabic_focus=(arabic_focus_match.group(1).strip() if arabic_focus_match else ""),
    )


def register_fonts(arabic_font: Path, ui_font: Path) -> None:
    if not arabic_font.exists():
        raise FileNotFoundError(f"Arabic font not found: {arabic_font}")
    if not ui_font.exists():
        raise FileNotFoundError(f"UI font not found: {ui_font}")
    pdfmetrics.registerFont(TTFont("QurbataArabic", str(arabic_font), shapable=True))
    pdfmetrics.registerFont(TTFont("QurbataUI", str(ui_font)))


def crop_marks(canvas: Canvas, trim_x: float, trim_y: float, trim_w: float, trim_h: float) -> None:
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor("#222222"))
    canvas.setLineWidth(0.25)
    gap, length = 1.2 * mm, 4 * mm
    for x, direction in ((trim_x, -1), (trim_x + trim_w, 1)):
        canvas.line(x + direction * gap, trim_y, x + direction * (gap + length), trim_y)
        canvas.line(
            x + direction * gap,
            trim_y + trim_h,
            x + direction * (gap + length),
            trim_y + trim_h,
        )
    for y, direction in ((trim_y, -1), (trim_y + trim_h, 1)):
        canvas.line(trim_x, y + direction * gap, trim_x, y + direction * (gap + length))
        canvas.line(
            trim_x + trim_w,
            y + direction * gap,
            trim_x + trim_w,
            y + direction * (gap + length),
        )
    canvas.restoreState()


def draw_cover(canvas: Canvas, bleed: float) -> None:
    trim_w, trim_h = TRIM_PAGE
    trim_x = trim_y = bleed
    green = colors.HexColor("#176B4D")
    dark_green = colors.HexColor("#0D4B37")
    orange = colors.HexColor("#E9852D")
    cream = colors.HexColor("#F8F4E8")

    canvas.setFillColor(cream)
    canvas.rect(0, 0, trim_w + 2 * bleed, trim_h + 2 * bleed, fill=1, stroke=0)
    crop_marks(canvas, trim_x, trim_y, trim_w, trim_h)
    canvas.setFillColor(green)
    canvas.rect(trim_x, trim_y, trim_w, trim_h, fill=1, stroke=0)
    canvas.setFillColor(dark_green)
    canvas.circle(trim_x + trim_w / 2, trim_y + trim_h * 0.72, 43 * mm, fill=1, stroke=0)
    canvas.setStrokeColor(orange)
    canvas.setLineWidth(2.2)
    canvas.circle(trim_x + trim_w / 2, trim_y + trim_h * 0.72, 35 * mm, fill=0, stroke=1)

    canvas.setFillColor(colors.white)
    canvas.setFont("QurbataUI", 8)
    canvas.drawCentredString(trim_x + trim_w / 2, trim_y + trim_h - 18 * mm, "SISTEM PEMBELAJARAN AL-QUR'AN TERINTEGRASI")
    canvas.setFont("QurbataUI", 27)
    canvas.drawCentredString(trim_x + trim_w / 2, trim_y + trim_h * 0.73, "QURBATA")
    canvas.setFillColor(orange)
    canvas.setFont("QurbataUI", 15)
    canvas.drawCentredString(trim_x + trim_w / 2, trim_y + trim_h * 0.63, "JILID 1")
    canvas.setFillColor(colors.white)
    canvas.setFont("QurbataUI", 9)
    canvas.drawCentredString(trim_x + trim_w / 2, trim_y + 52 * mm, "TAHSIN & TILAWAH  •  TAHFIDZ")
    canvas.drawCentredString(trim_x + trim_w / 2, trim_y + 45 * mm, "BAHASA ARAB  •  AKHLAK")
    canvas.setFont("QurbataUI", 7)
    canvas.drawCentredString(trim_x + trim_w / 2, trim_y + 24 * mm, "Disusun oleh Aris Liswanto")
    canvas.drawCentredString(trim_x + trim_w / 2, trim_y + 18 * mm, "RIQA Education Center")
    canvas.setFillColor(orange)
    canvas.roundRect(trim_x + 22 * mm, trim_y + 8 * mm, trim_w - 44 * mm, 3 * mm, 1.5 * mm, fill=1, stroke=0)


def draw_identity_page(canvas: Canvas, bleed: float) -> None:
    trim_w, trim_h = TRIM_PAGE
    trim_x = trim_y = bleed
    safe = 12 * mm
    x = trim_x + safe
    y = trim_y + safe
    w = trim_w - 2 * safe
    h = trim_h - 2 * safe
    green = colors.HexColor("#176B4D")
    orange = colors.HexColor("#E9852D")
    ink = colors.HexColor("#17231E")
    pale = colors.HexColor("#F3F8F5")

    canvas.setFillColor(colors.white)
    canvas.rect(0, 0, trim_w + 2 * bleed, trim_h + 2 * bleed, fill=1, stroke=0)
    crop_marks(canvas, trim_x, trim_y, trim_w, trim_h)
    canvas.setFillColor(green)
    canvas.roundRect(x, y + h - 27 * mm, w, 27 * mm, 4 * mm, fill=1, stroke=0)
    canvas.setFillColor(colors.white)
    canvas.setFont("QurbataUI", 18)
    canvas.drawString(x + 7 * mm, y + h - 12 * mm, "IDENTITAS PESERTA")
    canvas.setFont("QurbataUI", 7)
    canvas.drawString(x + 7 * mm, y + h - 20 * mm, "QURBATA Jilid 1 • Buku Peserta")
    canvas.setFillColor(orange)
    canvas.circle(x + w - 12 * mm, y + h - 13.5 * mm, 4 * mm, fill=1, stroke=0)

    fields = ("Nama lengkap", "Nomor peserta", "Lembaga / kelas", "Nama guru", "Tanggal mulai", "Tanggal selesai")
    cursor = y + h - 40 * mm
    canvas.setFont("QurbataUI", 7)
    for label in fields:
        canvas.setFillColor(pale)
        canvas.setStrokeColor(colors.HexColor("#B8D3C6"))
        canvas.roundRect(x, cursor - 21 * mm, w, 18 * mm, 2 * mm, fill=1, stroke=1)
        canvas.setFillColor(ink)
        canvas.drawString(x + 5 * mm, cursor - 7 * mm, label)
        canvas.setStrokeColor(colors.HexColor("#7AA58F"))
        canvas.line(x + 5 * mm, cursor - 15 * mm, x + w - 5 * mm, cursor - 15 * mm)
        cursor -= 23 * mm
    canvas.setFillColor(colors.HexColor("#68766F"))
    canvas.setFont("QurbataUI", 6.5)
    canvas.drawCentredString(x + w / 2, y + 2 * mm, "Simpan buku ini sebagai rekam belajar dan murojaah peserta.")


def draw_page(canvas: Canvas, page: PrintPage, bleed: float, page_number: int) -> None:
    trim_w, trim_h = TRIM_PAGE
    trim_x = trim_y = bleed
    safe = 7 * mm
    content_x = trim_x + safe
    content_y = trim_y + safe
    content_w = trim_w - 2 * safe
    content_h = trim_h - 2 * safe

    canvas.setFillColor(colors.white)
    canvas.rect(0, 0, trim_w + 2 * bleed, trim_h + 2 * bleed, fill=1, stroke=0)
    crop_marks(canvas, trim_x, trim_y, trim_w, trim_h)

    green = colors.HexColor("#176B4D")
    orange = colors.HexColor("#E9852D")
    ink = colors.HexColor("#17231E")
    pale = colors.HexColor("#F3F8F5")

    header_h = 19 * mm
    canvas.setFillColor(green)
    canvas.roundRect(content_x, content_y + content_h - header_h, content_w, header_h, 4 * mm, fill=1, stroke=0)
    canvas.setFillColor(colors.white)
    canvas.setFont("QurbataUI", 6.5)
    canvas.drawString(content_x + 4 * mm, content_y + content_h - 5.5 * mm, page.code)
    canvas.setFont("QurbataUI", 10)
    canvas.drawString(content_x + 4 * mm, content_y + content_h - 13 * mm, page.title[:48])
    canvas.setFillColor(orange)
    canvas.circle(content_x + content_w - 6 * mm, content_y + content_h - header_h / 2, 2.4 * mm, fill=1, stroke=0)

    footer_h = 43 * mm
    grid_top = content_y + content_h - header_h - 3 * mm
    grid_bottom = content_y + footer_h + 2.5 * mm
    grid_h = grid_top - grid_bottom
    gap = 1.5 * mm
    cols, rows = 3, 8
    cell_w = (content_w - (cols - 1) * gap) / cols
    cell_h = (grid_h - (rows - 1) * gap) / rows

    arabic_style = ParagraphStyle(
        "ArabicExercise",
        fontName="QurbataArabic",
        fontSize=16,
        leading=19,
        alignment=TA_CENTER,
        wordWrap="LTR",
        shaping=1,
        textColor=ink,
    )
    if page.kind == "exercise":
        for index, exercise in enumerate(page.exercises):
            row, logical_col = divmod(index, cols)
            col = cols - 1 - logical_col
            x = content_x + col * (cell_w + gap)
            y = grid_top - (row + 1) * cell_h - row * gap
            canvas.setFillColor(pale if row % 2 == 0 else colors.white)
            canvas.setStrokeColor(colors.HexColor("#B8D3C6"))
            canvas.setLineWidth(0.55)
            canvas.roundRect(x, y, cell_w, cell_h, 1.8 * mm, fill=1, stroke=1)
            # Render isolated tokens one by one. This avoids Unicode bidi
            # reordering across whitespace and guarantees that source token 1
            # is visually rightmost, followed by token 2 and token 3.
            tokens = exercise.split()
            token_gap = 2.2 * mm
            rendered = []
            for token in tokens:
                paragraph = Paragraph(token, arabic_style)
                pw, ph = paragraph.wrap(13 * mm, cell_h - 1.5 * mm)
                rendered.append((paragraph, pw, ph))
            total_w = sum(item[1] for item in rendered) + token_gap * (len(rendered) - 1)
            cursor_right = x + (cell_w + total_w) / 2
            for paragraph, pw, ph in rendered:
                cursor_right -= pw
                paragraph.drawOn(canvas, cursor_right, y + (cell_h - ph) / 2)
                cursor_right -= token_gap
    else:
        card_x = content_x + 9 * mm
        card_y = grid_bottom + 9 * mm
        card_w = content_w - 18 * mm
        card_h = grid_h - 18 * mm
        canvas.setFillColor(pale)
        canvas.setStrokeColor(colors.HexColor("#B8D3C6"))
        canvas.setLineWidth(0.8)
        canvas.roundRect(card_x, card_y, card_w, card_h, 5 * mm, fill=1, stroke=1)
        canvas.setFillColor(green)
        canvas.setFont("QurbataUI", 14)
        canvas.drawCentredString(card_x + card_w / 2, card_y + card_h * 0.62, "HALAMAN KHUSUS")
        canvas.setFillColor(orange)
        canvas.setFont("QurbataUI", 8.5)
        canvas.drawCentredString(card_x + card_w / 2, card_y + card_h * 0.47, "Materi peserta menunggu keputusan dan pengesahan")
        canvas.setFillColor(colors.HexColor("#68766F"))
        canvas.setFont("QurbataUI", 6.5)
        canvas.drawCentredString(card_x + card_w / 2, card_y + card_h * 0.34, page.status[:110])

    panel_y = content_y + 13 * mm
    panel_h = 25 * mm
    panel_gap = 2 * mm
    panel_w = (content_w - panel_gap) / 2
    canvas.setFillColor(pale)
    canvas.setStrokeColor(colors.HexColor("#B8D3C6"))
    canvas.roundRect(content_x, panel_y, panel_w, panel_h, 2 * mm, fill=1, stroke=1)
    canvas.roundRect(content_x + panel_w + panel_gap, panel_y, panel_w, panel_h, 2 * mm, fill=1, stroke=1)
    canvas.setFillColor(green)
    canvas.setFont("QurbataUI", 6.5)
    canvas.drawString(content_x + 3 * mm, panel_y + panel_h - 6 * mm, "BAHASA ARAB • 5 MENIT")
    canvas.drawString(content_x + panel_w + panel_gap + 3 * mm, panel_y + panel_h - 6 * mm, "TAHFIDZ • MUROJAAH")
    canvas.setFillColor(ink)
    canvas.setFont("QurbataUI", 5.4)
    if page.arabic_focus and not ARABIC_RE.search(page.arabic_focus):
        arabic_line = page.arabic_focus[:62]
    else:
        arabic_line = "Materi lisan guru • lihat panduan guru"
    canvas.drawString(content_x + 3 * mm, panel_y + panel_h - 13 * mm, arabic_line)
    canvas.drawString(content_x + 3 * mm, panel_y + panel_h - 19 * mm, "Tulisannya menunggu whitelist literasi.")
    canvas.drawString(content_x + panel_w + panel_gap + 3 * mm, panel_y + panel_h - 13 * mm, "Target mengikuti peta hafalan Jilid 1.")
    canvas.drawString(content_x + panel_w + panel_gap + 3 * mm, panel_y + panel_h - 19 * mm, "Status: menunggu mapping per halaman.")

    form_y = content_y + 5.5 * mm
    canvas.setFillColor(colors.white)
    canvas.setStrokeColor(colors.HexColor("#7AA58F"))
    canvas.roundRect(content_x, form_y, content_w, 6 * mm, 1.3 * mm, fill=1, stroke=1)
    canvas.setFillColor(ink)
    canvas.setFont("QurbataUI", 5.2)
    canvas.drawString(content_x + 2 * mm, form_y + 2.1 * mm, "Tanggal: __________")
    canvas.drawString(content_x + 35 * mm, form_y + 2.1 * mm, "Nilai: ______")
    canvas.drawString(content_x + 58 * mm, form_y + 2.1 * mm, "Lulus / Ulang")
    canvas.drawString(content_x + 87 * mm, form_y + 2.1 * mm, "Paraf/TTD Guru: ______")

    canvas.setFillColor(green)
    canvas.setFont("QurbataUI", 5.5)
    advice = page.advice or "Belajar dengan tenang, teliti, dan sungguh-sungguh."
    canvas.drawString(content_x, content_y + 1.4 * mm, advice[:92])
    canvas.setFillColor(colors.HexColor("#68766F"))
    canvas.setFont("QurbataUI", 5)
    canvas.drawRightString(content_x + content_w, content_y + 1.4 * mm, f"QURBATA • Jilid 1 • {page_number}")


def generate(input_dir: Path, output: Path, arabic_font: Path, ui_font: Path, bleed_mm: float) -> list[PrintPage]:
    paths = sorted(input_dir.glob("QJ1-P*.md"))
    if not paths:
        raise ValueError(f"No QJ1 page sources found in {input_dir}")
    pages = [parse_page(path) for path in paths]
    register_fonts(arabic_font, ui_font)
    bleed = bleed_mm * mm
    trim_w, trim_h = TRIM_PAGE
    output.parent.mkdir(parents=True, exist_ok=True)
    canvas = Canvas(str(output), pagesize=(trim_w + 2 * bleed, trim_h + 2 * bleed), pageCompression=1)
    canvas.setTitle("QURBATA Jilid 1 - Buku Peserta")
    canvas.setAuthor("QURBATA / RIQA")
    draw_cover(canvas, bleed)
    canvas.showPage()
    draw_identity_page(canvas, bleed)
    canvas.showPage()
    for page_number, page in enumerate(pages, 1):
        draw_page(canvas, page, bleed, page_number)
        canvas.showPage()
    canvas.save()
    return pages


def preflight(output: Path, pages: list[PrintPage], bleed_mm: float) -> None:
    reader = PdfReader(str(output))
    expected_count = len(pages) + 2
    if len(reader.pages) != expected_count:
        raise ValueError(f"PDF page count mismatch: {len(reader.pages)} != {expected_count}")
    expected_w = TRIM_PAGE[0] + 2 * bleed_mm * mm
    expected_h = TRIM_PAGE[1] + 2 * bleed_mm * mm
    for index, pdf_page in enumerate(reader.pages, 1):
        width = float(pdf_page.mediabox.width)
        height = float(pdf_page.mediabox.height)
        if abs(width - expected_w) > 0.5 or abs(height - expected_h) > 0.5:
            raise ValueError(f"Page {index}: unexpected media box {width} x {height}")
        text = pdf_page.extract_text() or ""
        forbidden = ("Audience materi Arab", "Fokus lisan", "Status sumber bahasa")
        leaked = [marker for marker in forbidden if marker in text]
        if leaked:
            raise ValueError(f"Page {index}: teacher-only content leaked: {leaked}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", type=Path, default=Path("books/jilid-1/pages"))
    parser.add_argument("--output", type=Path, default=Path("output/pdf/QURBATA-Jilid-1-Peserta-print.pdf"))
    parser.add_argument("--arabic-font", type=Path, default=Path("production/print/fonts/AmiriQuran.ttf"))
    parser.add_argument("--ui-font", type=Path, default=Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
    parser.add_argument("--bleed-mm", type=float, default=3.0)
    args = parser.parse_args()
    pages = generate(args.input_dir, args.output, args.arabic_font, args.ui_font, args.bleed_mm)
    preflight(args.output, pages, args.bleed_mm)
    print(f"PASS: {args.output} ({len(pages)} pages; participant edition; preflight complete)")


if __name__ == "__main__":
    main()

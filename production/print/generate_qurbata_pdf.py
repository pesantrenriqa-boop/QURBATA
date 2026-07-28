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
from reportlab.lib.pagesizes import A4, landscape
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
    exercises = []
    for line in participant_source.splitlines():
        match = EXERCISE_RE.match(line)
        if match:
            exercises.append(match.group(3).strip())

    if len(exercises) != 24:
        raise ValueError(f"{path}: expected 24 exercises/samples, found {len(exercises)}")
    if any(not ARABIC_RE.search(item) for item in exercises):
        raise ValueError(f"{path}: a participant exercise has no Arabic character")

    return PrintPage(
        code=heading.group(1),
        title=heading.group(2).strip(),
        exercises=tuple(exercises),
        advice=(advice_match.group(1).strip() if advice_match else ""),
        status=(status_match.group(1).strip() if status_match else "Draf"),
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


def draw_page(canvas: Canvas, page: PrintPage, bleed: float) -> None:
    trim_w, trim_h = landscape(A4)
    trim_x = trim_y = bleed
    safe = 12 * mm
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
    canvas.setFont("QurbataUI", 9)
    canvas.drawString(content_x + 6 * mm, content_y + content_h - 7.5 * mm, page.code)
    canvas.setFont("QurbataUI", 17)
    canvas.drawString(content_x + 6 * mm, content_y + content_h - 15 * mm, page.title)
    canvas.setFillColor(orange)
    canvas.circle(content_x + content_w - 8 * mm, content_y + content_h - header_h / 2, 3.2 * mm, fill=1, stroke=0)

    footer_h = 12 * mm
    grid_top = content_y + content_h - header_h - 5 * mm
    grid_bottom = content_y + footer_h + 4 * mm
    grid_h = grid_top - grid_bottom
    gap = 3 * mm
    cols, rows = 4, 6
    cell_w = (content_w - (cols - 1) * gap) / cols
    cell_h = (grid_h - (rows - 1) * gap) / rows

    arabic_style = ParagraphStyle(
        "ArabicExercise",
        fontName="QurbataArabic",
        fontSize=25,
        leading=31,
        alignment=TA_CENTER,
        wordWrap="LTR",
        shaping=1,
        textColor=ink,
    )
    for index, exercise in enumerate(page.exercises):
        row, logical_col = divmod(index, cols)
        col = cols - 1 - logical_col
        x = content_x + col * (cell_w + gap)
        y = grid_top - (row + 1) * cell_h - row * gap
        canvas.setFillColor(pale if row % 2 == 0 else colors.white)
        canvas.setStrokeColor(colors.HexColor("#B8D3C6"))
        canvas.setLineWidth(0.55)
        canvas.roundRect(x, y, cell_w, cell_h, 2.4 * mm, fill=1, stroke=1)
        # ReportLab's RTL line handling reverses whitespace-separated runs.
        # Reverse the source tokens once so the visual right-to-left order
        # remains identical to the controlled Markdown exercise.
        visual_exercise = " ".join(reversed(exercise.split()))
        paragraph = Paragraph(visual_exercise, arabic_style)
        pw, ph = paragraph.wrap(cell_w - 5 * mm, cell_h - 3 * mm)
        paragraph.drawOn(canvas, x + (cell_w - pw) / 2, y + (cell_h - ph) / 2)

    canvas.setFillColor(green)
    canvas.setFont("QurbataUI", 8.5)
    advice = page.advice or "Belajar dengan tenang, teliti, dan sungguh-sungguh."
    canvas.drawString(content_x, content_y + 3.5 * mm, advice[:150])
    canvas.setFillColor(colors.HexColor("#68766F"))
    canvas.setFont("QurbataUI", 7)
    canvas.drawRightString(content_x + content_w, content_y + 3.5 * mm, "QURBATA Jilid 1 • Draf terkendali")


def generate(input_dir: Path, output: Path, arabic_font: Path, ui_font: Path, bleed_mm: float) -> list[PrintPage]:
    paths = sorted(input_dir.glob("QJ1-P*.md"))
    if not paths:
        raise ValueError(f"No QJ1 page sources found in {input_dir}")
    pages = [parse_page(path) for path in paths]
    register_fonts(arabic_font, ui_font)
    bleed = bleed_mm * mm
    trim_w, trim_h = landscape(A4)
    output.parent.mkdir(parents=True, exist_ok=True)
    canvas = Canvas(str(output), pagesize=(trim_w + 2 * bleed, trim_h + 2 * bleed), pageCompression=1)
    canvas.setTitle("QURBATA Jilid 1 - Buku Peserta")
    canvas.setAuthor("QURBATA / RIQA")
    for page in pages:
        draw_page(canvas, page, bleed)
        canvas.showPage()
    canvas.save()
    return pages


def preflight(output: Path, pages: list[PrintPage], bleed_mm: float) -> None:
    reader = PdfReader(str(output))
    if len(reader.pages) != len(pages):
        raise ValueError(f"PDF page count mismatch: {len(reader.pages)} != {len(pages)}")
    expected_w = landscape(A4)[0] + 2 * bleed_mm * mm
    expected_h = landscape(A4)[1] + 2 * bleed_mm * mm
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
    parser.add_argument("--arabic-font", type=Path, default=Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
    parser.add_argument("--ui-font", type=Path, default=Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
    parser.add_argument("--bleed-mm", type=float, default=3.0)
    args = parser.parse_args()
    pages = generate(args.input_dir, args.output, args.arabic_font, args.ui_font, args.bleed_mm)
    preflight(args.output, pages, args.bleed_mm)
    print(f"PASS: {args.output} ({len(pages)} pages; participant edition; preflight complete)")


if __name__ == "__main__":
    main()

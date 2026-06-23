#!/usr/bin/env python3
"""
Cover letter PDF generator for Chris Stefan.

Usage:
  python generate_cover_letter.py \
    --body body.txt \
    --re "Job Title — Company" \
    --output output.pdf \
    [--salutation "Hi Name,"]

Body text format:
  - Separate paragraphs with blank lines.
  - Use **bold** for inline bold text.
  - Start bullet items with "• " (e.g. "• **Label:** Description.").
  - A standalone line ending in ":" (< 80 chars) becomes a bold section header.
  - Close with "Sincerely,\nChris Stefan" as its own paragraph block.
"""

import argparse
import re
from datetime import datetime

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Frame, Paragraph

# ── Font registration ──────────────────────────────────────────────────────────
FONT_DIR = "/usr/share/fonts/truetype/liberation"
pdfmetrics.registerFont(TTFont("LibSans",        f"{FONT_DIR}/LiberationSans-Regular.ttf"))
pdfmetrics.registerFont(TTFont("LibSans-Bold",   f"{FONT_DIR}/LiberationSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("LibSans-Italic", f"{FONT_DIR}/LiberationSans-Italic.ttf"))
pdfmetrics.registerFontFamily(
    "LibSans",
    normal="LibSans",
    bold="LibSans-Bold",
    italic="LibSans-Italic",
)

# ── Colors ─────────────────────────────────────────────────────────────────────
ACCENT = HexColor("#B55E2A")
BLACK  = HexColor("#1C1B18")
GRAY   = HexColor("#5A5750")

# ── Page dimensions ────────────────────────────────────────────────────────────
PAGE_W, PAGE_H = letter
MARGIN_L = 0.75 * inch
MARGIN_R = 0.75 * inch
MARGIN_T = 0.55 * inch
MARGIN_B = 0.65 * inch
CONTENT_W = PAGE_W - MARGIN_L - MARGIN_R

# ── Identity ───────────────────────────────────────────────────────────────────
NAME         = "Chris Stefan"
CONTACT_LINE = "chris.stefan@proton.me · +1 514.710.9601 · linkedin.com/in/chris-stefan · chrizefan.github.io/me"


# ── Text helpers ───────────────────────────────────────────────────────────────

def md_to_xml(text: str) -> str:
    """Convert **bold** markdown to ReportLab XML <b>bold</b> markup."""
    return re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", text)


# ── Paragraph styles ───────────────────────────────────────────────────────────

def _style(name, font="LibSans", size=9.2, leading=13, color=BLACK,
           space_after=7, space_before=0, left_indent=0, first_indent=0):
    return ParagraphStyle(
        name,
        fontName=font,
        fontSize=size,
        leading=leading,
        textColor=color,
        spaceAfter=space_after,
        spaceBefore=space_before,
        leftIndent=left_indent,
        firstLineIndent=first_indent,
    )

STYLE_BODY    = _style("body")
STYLE_BULLET  = _style("bullet", space_after=4, left_indent=11, first_indent=-11)
STYLE_SECTION = _style("section", font="LibSans-Bold", space_after=4, space_before=4)
STYLE_CLOSE   = _style("close",   space_before=6, space_after=2, leading=15)
STYLE_CLOSENM = _style("closenm", font="LibSans-Bold", space_after=0, leading=15)


def parse_body(body_text: str) -> list:
    """
    Parse body text into a list of Platypus flowables.

    Rules:
      - Blank lines separate blocks.
      - Lines starting with "• " are rendered as indented bullet items.
      - A single-line block ending in ":" (under 80 chars) → bold section header.
      - "Sincerely,\\nChris Stefan" → closing block.
      - Everything else → normal body paragraph.
      - **bold** is converted to <b>bold</b> XML markup everywhere.
    """
    flowables = []
    blocks = [b.strip() for b in body_text.strip().split("\n\n") if b.strip()]

    for block in blocks:
        # ── Closing ──────────────────────────────────────────────────────────
        if block.startswith("Sincerely"):
            lines = [l.strip() for l in block.split("\n") if l.strip()]
            for i, line in enumerate(lines):
                style = STYLE_CLOSENM if i > 0 else STYLE_CLOSE
                flowables.append(Paragraph(md_to_xml(line), style))

        # ── Bullet block ─────────────────────────────────────────────────────
        elif block.startswith("• "):
            for line in block.split("\n"):
                line = line.strip()
                if line.startswith("• "):
                    flowables.append(
                        Paragraph(f"• {md_to_xml(line[2:])}", STYLE_BULLET)
                    )
                elif line:
                    flowables.append(Paragraph(md_to_xml(line), STYLE_BODY))

        # ── Section header ───────────────────────────────────────────────────
        elif "\n" not in block and block.endswith(":") and len(block) < 80:
            flowables.append(Paragraph(md_to_xml(block), STYLE_SECTION))

        # ── Regular paragraph ────────────────────────────────────────────────
        else:
            flowables.append(Paragraph(md_to_xml(block), STYLE_BODY))

    return flowables


# ── PDF builder ────────────────────────────────────────────────────────────────

def build_pdf(body_text: str, re_line: str, salutation: str, output_path: str) -> str:
    """Render the complete cover letter to a PDF file."""

    c = canvas.Canvas(output_path, pagesize=letter)
    c.setTitle(f"Cover Letter — {re_line}")

    y = PAGE_H - MARGIN_T

    # Name ─────────────────────────────────────────────────────────────────────
    c.setFont("LibSans-Bold", 13)
    c.setFillColor(BLACK)
    c.drawString(MARGIN_L, y, NAME)
    y -= 14

    # Contact line ─────────────────────────────────────────────────────────────
    c.setFont("LibSans", 8)
    c.setFillColor(GRAY)
    c.drawString(MARGIN_L, y, CONTACT_LINE)
    y -= 10

    # HR divider (orange) ──────────────────────────────────────────────────────
    c.setStrokeColor(ACCENT)
    c.setLineWidth(0.8)
    c.line(MARGIN_L, y, PAGE_W - MARGIN_R, y)
    y -= 16

    # Date ─────────────────────────────────────────────────────────────────────
    c.setFont("LibSans", 9)
    c.setFillColor(BLACK)
    date_str = datetime.now().strftime("%B %d, %Y").replace(" 0", " ")
    c.drawString(MARGIN_L, y, date_str)
    y -= 20

    # Re: line — bold, orange ──────────────────────────────────────────────────
    c.setFont("LibSans-Bold", 9)
    c.setFillColor(ACCENT)
    c.drawString(MARGIN_L, y, f"Re: {re_line}")
    c.setFillColor(BLACK)
    y -= 20

    # Salutation — bold ────────────────────────────────────────────────────────
    c.setFont("LibSans-Bold", 9.2)
    c.setFillColor(BLACK)
    c.drawString(MARGIN_L, y, salutation)
    y -= 16

    # Body — Platypus frame (supports bullets + inline bold) ───────────────────
    frame_h = y - MARGIN_B
    frame = Frame(
        MARGIN_L, MARGIN_B,
        CONTENT_W, frame_h,
        leftPadding=0, rightPadding=0,
        topPadding=0, bottomPadding=0,
        showBoundary=0,
    )
    flowables = parse_body(body_text)
    frame.addFromList(flowables, c)

    c.save()
    return output_path


# ── CLI ────────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Generate Chris Stefan cover letter PDF")
    parser.add_argument("--body",       required=True, help="Path to body text file (.txt)")
    parser.add_argument("--re",         required=True, help="Re: line, e.g. 'Senior AI Engineer — Qonto'")
    parser.add_argument("--output",     required=True, help="Output PDF path")
    parser.add_argument("--salutation", default="Dear Hiring Team,",
                        help="Salutation line (e.g. 'Hi Name,' or 'Dear Hiring Team,')")
    args = parser.parse_args()

    with open(args.body) as f:
        body = f.read()

    out = build_pdf(body, args.re, args.salutation, args.output)
    print(f"PDF written to: {out}")


if __name__ == "__main__":
    main()

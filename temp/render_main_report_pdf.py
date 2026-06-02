from html import escape
from pathlib import Path
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    ListFlowable,
    ListItem,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


SRC = Path("outputs/deliverables/reports/main_report.md")
DST = Path("outputs/deliverables/reports/main_report.pdf")


def inline(text: str) -> str:
    text = escape(text)
    text = re.sub(
        r"`([^`]+)`",
        lambda m: f'<font name="Courier">{m.group(1)}</font>',
        text,
    )
    return text


def split_table_row(line: str) -> list[str]:
    parts = line.strip().strip("|").split("|")
    return [p.strip() for p in parts]


def is_separator(row: list[str]) -> bool:
    return all(re.fullmatch(r":?-{3,}:?", cell.strip()) for cell in row)


def build_table(lines: list[str], styles):
    rows = [split_table_row(line) for line in lines]
    rows = [row for row in rows if not is_separator(row)]
    if not rows:
        return []

    col_count = max(len(row) for row in rows)
    usable_width = 7.0 * inch
    col_width = usable_width / col_count
    data = []
    for row in rows:
        padded = row + [""] * (col_count - len(row))
        data.append([Paragraph(inline(cell), styles["TableCell"]) for cell in padded])

    table = Table(data, colWidths=[col_width] * col_count, repeatRows=1)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#EDEDED")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("GRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#BDBDBD")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    return [table, Spacer(1, 8)]


def make_styles():
    base = getSampleStyleSheet()
    styles = {
        "Title": ParagraphStyle(
            "Title",
            parent=base["Title"],
            fontName="Helvetica-Bold",
            fontSize=18,
            leading=22,
            alignment=TA_CENTER,
            spaceAfter=16,
        ),
        "H2": ParagraphStyle(
            "H2",
            parent=base["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=13,
            leading=16,
            spaceBefore=12,
            spaceAfter=6,
            keepWithNext=True,
        ),
        "Body": ParagraphStyle(
            "Body",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=9.5,
            leading=13,
            alignment=TA_LEFT,
            spaceAfter=6,
            splitLongWords=True,
            wordWrap="CJK",
        ),
        "Bullet": ParagraphStyle(
            "Bullet",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=9,
            leading=12,
            leftIndent=14,
            firstLineIndent=0,
            spaceAfter=3,
            splitLongWords=True,
            wordWrap="CJK",
        ),
        "TableCell": ParagraphStyle(
            "TableCell",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=7,
            leading=9,
            splitLongWords=True,
            wordWrap="CJK",
        ),
    }
    return styles


def parse_markdown(text: str):
    styles = make_styles()
    story = []
    lines = text.splitlines()
    i = 0

    while i < len(lines):
        line = lines[i].rstrip()

        if not line.strip():
            i += 1
            continue

        if line.startswith("# "):
            story.append(Paragraph(inline(line[2:].strip()), styles["Title"]))
            i += 1
            continue

        if line.startswith("## "):
            story.append(Paragraph(inline(line[3:].strip()), styles["H2"]))
            i += 1
            continue

        if line.startswith("|"):
            table_lines = []
            while i < len(lines) and lines[i].startswith("|"):
                table_lines.append(lines[i].rstrip())
                i += 1
            story.extend(build_table(table_lines, styles))
            continue

        if line.startswith("- "):
            items = []
            while i < len(lines) and lines[i].startswith("- "):
                text = lines[i][2:].strip()
                items.append(ListItem(Paragraph(inline(text), styles["Bullet"])))
                i += 1
            story.append(
                ListFlowable(
                    items,
                    bulletType="bullet",
                    start="circle",
                    leftIndent=12,
                    bulletFontSize=7,
                )
            )
            story.append(Spacer(1, 4))
            continue

        paragraph_lines = [line]
        i += 1
        while (
            i < len(lines)
            and lines[i].strip()
            and not lines[i].startswith("#")
            and not lines[i].startswith("|")
            and not lines[i].startswith("- ")
        ):
            paragraph_lines.append(lines[i].strip())
            i += 1
        story.append(Paragraph(inline(" ".join(paragraph_lines)), styles["Body"]))

    return story


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#666666"))
    canvas.drawCentredString(4.25 * inch, 0.45 * inch, f"Page {doc.page}")
    canvas.restoreState()


def main():
    text = SRC.read_text(encoding="utf-8")
    story = parse_markdown(text)
    doc = BaseDocTemplate(
        str(DST),
        pagesize=letter,
        leftMargin=0.7 * inch,
        rightMargin=0.7 * inch,
        topMargin=0.65 * inch,
        bottomMargin=0.65 * inch,
        title="HW01 Report",
        author="Khoi Minh Nguyen",
    )
    frame = Frame(
        doc.leftMargin,
        doc.bottomMargin,
        doc.width,
        doc.height,
        id="normal",
    )
    doc.addPageTemplates([PageTemplate(id="main", frames=[frame], onPage=footer)])
    doc.build(story)
    print(f"wrote {DST} ({DST.stat().st_size} bytes)")


if __name__ == "__main__":
    main()

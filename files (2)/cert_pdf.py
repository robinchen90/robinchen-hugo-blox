"""
cert_pdf.py — Generates a shareable PDF certificate from a signed cert JSON.

The PDF is the keepsake; the verification URL is the trust anchor. Every PDF
includes a QR code linking back to the verification page on robinchen.org,
so anyone holding the PDF can confirm authenticity by scanning it.

Design follows the dark/cream "Survived." aesthetic. Landscape letter size.
"""

import io
from pathlib import Path

from reportlab.lib.colors import HexColor, Color
from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
import qrcode


PAGE_W, PAGE_H = landscape(letter)

BG = HexColor("#0F1419")
INK = HexColor("#E8E5DC")
INK_MUTED = HexColor("#A39E91")
INK_DIM = HexColor("#8C8779")
INK_FAINT = HexColor("#6B675C")
RULE = HexColor("#2A2F36")


def _draw_qr(c: canvas.Canvas, data: str, x: float, y: float, size: float):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=2,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#E8E5DC", back_color="#0F1419")
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    from reportlab.lib.utils import ImageReader
    c.drawImage(ImageReader(buf), x, y, width=size, height=size, mask="auto")


def _wrap(text: str, width_chars: int):
    words = text.split()
    lines, line = [], ""
    for w in words:
        if len(line) + len(w) + 1 <= width_chars:
            line = (line + " " + w).strip()
        else:
            if line:
                lines.append(line)
            line = w
    if line:
        lines.append(line)
    return lines


def generate_pdf(cert: dict, output_path: Path) -> Path:
    """Generate a cert PDF from a signed certificate dict."""
    p = cert["payload"]
    c = canvas.Canvas(str(output_path), pagesize=landscape(letter))

    c.setFillColor(BG)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

    margin_x = 60
    margin_top = PAGE_H - 60

    c.setFillColor(INK_DIM)
    c.setFont("Helvetica", 9)
    c.drawString(margin_x, margin_top, "THE PROFESSOR'S LIST · A NOTE OF RECOGNITION")
    c.drawRightString(PAGE_W - margin_x, margin_top, "Robin Chen")

    c.setFillColor(INK)
    c.setFont("Times-Bold", 84)
    title_y = margin_top - 90
    c.drawString(margin_x, title_y, "Survived.")

    c.setFillColor(INK_MUTED)
    c.setFont("Helvetica", 12)
    c.drawString(margin_x, title_y - 28, f"{p['course']} · {p['semester']}")

    body_text = p.get("body_text") or (
        "Earned a place on this list through consistent presence, sustained effort, "
        "and the kind of command of the material that comes from actually doing the work."
    )

    c.setFillColor(HexColor("#C9C4B5"))
    c.setFont("Helvetica", 11)
    body_y = title_y - 65
    body_max_width = PAGE_W - 2 * margin_x - 200
    avg_char_width = 5.2
    chars_per_line = int(body_max_width / avg_char_width)
    lines = _wrap(body_text, chars_per_line)
    for i, line in enumerate(lines):
        c.drawString(margin_x, body_y - i * 16, line)

    rule_y = 130
    c.setStrokeColor(RULE)
    c.setLineWidth(0.5)
    c.line(margin_x, rule_y, PAGE_W - margin_x, rule_y)

    c.setFillColor(INK_DIM)
    c.setFont("Helvetica", 7.5)
    c.drawString(margin_x, rule_y - 18, "A NOTE ABOUT")

    c.setFillColor(INK)
    c.setFont("Times-Bold", 22)
    c.drawString(margin_x, rule_y - 44, p["issued_to"])

    c.setFillColor(INK_DIM)
    c.setFont("Helvetica", 9)
    c.drawString(margin_x, rule_y - 62, f"Reference {p['ref_id']} · {p['issued_date']}")
    c.drawString(margin_x, rule_y - 76, f"Verify at {p['verification_url']}")

    sig_x = 380
    c.setFillColor(INK)
    c.setFont("Times-Italic", 22)
    c.drawString(sig_x, rule_y - 30, "Robin Chen")
    c.setFillColor(INK_DIM)
    c.setFont("Helvetica", 7.5)
    c.drawString(sig_x, rule_y - 46, "ASSISTANT PROFESSOR OF ECONOMICS")
    c.drawString(sig_x, rule_y - 58, "ISSUED PERSONALLY · MAY BE VERIFIED BY ANYONE")

    qr_size = 80
    qr_x = PAGE_W - margin_x - qr_size
    qr_y = 25
    _draw_qr(c, p["verification_url"], qr_x, qr_y, qr_size)
    c.setFillColor(INK_FAINT)
    c.setFont("Helvetica", 7)
    c.drawRightString(qr_x - 8, qr_y + 36, "Scan to verify")
    c.drawRightString(qr_x - 8, qr_y + 24, "Or visit the URL above")

    c.setFillColor(INK_FAINT)
    c.setFont("Helvetica", 7)
    disclaimer = (
        "Personal recognition from Robin Chen as an individual scholar. "
        "Not an institutional credential. Does not replace or supplement any record issued by the University of Northern Iowa."
    )
    disclaimer_lines = _wrap(disclaimer, 110)
    for i, line in enumerate(disclaimer_lines):
        c.drawString(margin_x, 35 - i * 9, line)

    c.save()
    return output_path

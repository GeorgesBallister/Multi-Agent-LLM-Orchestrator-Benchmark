"""Build the evidence-based orchestration report as a print-ready PDF."""

from __future__ import annotations

import html
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import BaseDocTemplate, Frame, Flowable, PageBreak, Paragraph, Spacer, Table, TableStyle
from reportlab.platypus import PageTemplate

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "reports" / "Orquestração multiagente com evidências.md"
OUTPUT = ROOT / "report" / "Relatorio-Orquestracao-Multiagente-Evidencias-2026.pdf"
BLACK = colors.HexColor("#0E0E0E")
RED = colors.HexColor("#E31B23")
CYAN = colors.HexColor("#00BCE4")
PAPER = colors.HexColor("#F7F5EF")
GRAY = colors.HexColor("#4B4B4B")
# Editorial tokens sampled from the separate Portifolio-LAY design system.
LAY_BLACK = colors.HexColor("#000000")
BONE = colors.HexColor("#FAF5E9")
YELLOW = colors.HexColor("#FFF201")
BLOOD = colors.HexColor("#C21818")
RETRO_CYAN = colors.HexColor("#00FFFF")
MAGENTA = colors.HexColor("#FF3EB5")
PAGE_SIZE = landscape(A4)


def register_fonts():
    regular = Path(r"C:\Windows\Fonts\arial.ttf")
    bold = Path(r"C:\Windows\Fonts\arialbd.ttf")
    italic = Path(r"C:\Windows\Fonts\ariali.ttf")
    pdfmetrics.registerFont(TTFont("ReportSans", str(regular)))
    pdfmetrics.registerFont(TTFont("ReportSansBold", str(bold)))
    pdfmetrics.registerFont(TTFont("ReportSansItalic", str(italic if italic.exists() else regular)))
    return "ReportSans", "ReportSansBold", "ReportSansItalic"


REGULAR, BOLD, ITALIC = register_fonts()


def inline_markdown(text):
    value = html.escape(text.strip())
    value = re.sub(r"\[([^\]]+)\]\((https?://[^\s)]+)\)", r'<link href="\2" color="#006F88"><u>\1</u></link>', value)
    value = re.sub(r"`([^`]+)`", r'<font name="Courier">\1</font>', value)
    value = re.sub(r"\*\*([^*]+)\*\*", r'<b>\1</b>', value)
    value = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r'<i>\1</i>', value)
    return value.replace("—", "-")


def table_from_lines(lines, s):
    rows = []
    for line in lines:
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-{3,}:?", cell.replace(" ", "")) for cell in cells):
            continue
        style = s["table_header"] if not rows else s["table"]
        rows.append([Paragraph(inline_markdown(cell), style) for cell in cells])
    count = max(len(row) for row in rows)
    for row in rows:
        row.extend([Paragraph("", s["table"])] * (count - len(row)))
    usable = PAGE_SIZE[0] - 28 * mm
    weights = {3: [1.1, 1.35, 1.35], 4: [1, 1.15, 1.25, 1.25], 5: [1.1, 1.25, 1.15, 1.25, 1.25]}.get(count, [1] * count)
    widths = [usable * weight / sum(weights) for weight in weights]
    table = Table(rows, colWidths=widths, repeatRows=1, hAlign="LEFT")
    commands = [("BACKGROUND", (0, 0), (-1, 0), YELLOW), ("TEXTCOLOR", (0, 0), (-1, 0), LAY_BLACK),
                ("GRID", (0, 0), (-1, -1), 0.45, LAY_BLACK), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5)]
    for idx in range(1, len(rows)):
        if idx % 2 == 0:
            commands.append(("BACKGROUND", (0, idx), (-1, idx), PAPER))
    table.setStyle(TableStyle(commands))
    return table


class SectionBanner(Flowable):
    """High contrast chapter opener, with a numbered red block."""

    def __init__(self, title, number, width=178 * mm, height=18 * mm):
        super().__init__()
        self.title, self.number = title, number
        self.width, self.height = width, height

    def wrap(self, avail_width, avail_height):
        self.width = avail_width
        return self.width, self.height

    def draw(self):
        c = self.canv
        c.setFillColor(LAY_BLACK)
        c.rect(0, 0, self.width, self.height, fill=1, stroke=0)
        c.setFillColor(BLOOD)
        c.rect(0, 0, 17 * mm, self.height, fill=1, stroke=0)
        c.setFillColor(BONE)
        c.setFont(BOLD, 13)
        c.drawCentredString(8.5 * mm, self.height / 2 - 4, self.number)
        c.setFillColor(BONE)
        c.setFont(BOLD, 12)
        text = self.title.upper()
        while pdfmetrics.stringWidth(text, BOLD, 12) > self.width - 24 * mm and len(text) > 12:
            text = text[:-4] + "…"
        c.drawString(23 * mm, self.height / 2 - 4, text)


class RoutingMap(Flowable):
    """Editorial route map; roles are proposed and explicitly provisional."""

    def __init__(self, width=178 * mm, height=91 * mm):
        super().__init__()
        self.width, self.height = width, height

    def wrap(self, avail_width, avail_height):
        self.width = avail_width
        return self.width, self.height

    def draw(self):
        c = self.canv
        c.setFillColor(LAY_BLACK)
        c.rect(0, self.height - 16 * mm, self.width, 16 * mm, fill=1, stroke=0)
        c.setFillColor(YELLOW)
        c.setFont(BOLD, 10)
        c.drawString(5 * mm, self.height - 10.5 * mm, "UM PEDIDO → UM DONO → UM GATE HUMANO")
        columns = [
            ("01 / ROTINA", "SCRIPTS", "hash · conversão\nresize · fixtures", YELLOW),
            ("02 / BUILD", "CODEX", "tarefas delimitadas\nworktree · testes", RETRO_CYAN),
            ("03 / RISCO", "CLAUDE", "arquitetura\nrevisão crítica", MAGENTA),
            ("04 / VISUAL", "GEMINI", "crawl · multimodal\nQA em browser", BLOOD),
        ]
        gap = 3 * mm
        card_w = (self.width - gap * 3) / 4
        y = self.height - 53 * mm
        for i, (kicker, name, detail, accent) in enumerate(columns):
            x = i * (card_w + gap)
            c.setFillColor(BONE)
            c.setStrokeColor(LAY_BLACK)
            c.setLineWidth(1.2)
            c.rect(x, y, card_w, 33 * mm, fill=1, stroke=1)
            c.setFillColor(accent)
            c.rect(x, y + 28 * mm, card_w, 5 * mm, fill=1, stroke=0)
            c.setFillColor(GRAY)
            c.setFont(BOLD, 6.3)
            c.drawString(x + 2.5 * mm, y + 23.5 * mm, kicker)
            c.setFillColor(LAY_BLACK)
            c.setFont(BOLD, 11 if name != "SCRIPTS" else 8.6)
            c.drawString(x + 2.5 * mm, y + 15 * mm, name)
            c.setFont(REGULAR, 6.6)
            for line_no, line in enumerate(detail.split("\n")):
                c.drawString(x + 2.5 * mm, y + 8.8 * mm - line_no * 3.2 * mm, line)
        c.setFillColor(LAY_BLACK)
        c.rect(0, 8 * mm, self.width, 11 * mm, fill=1, stroke=0)
        c.setFillColor(YELLOW)
        c.setFont(BOLD, 8)
        c.drawCentredString(self.width / 2, 12 * mm, "HUMANO: CONTRATO · TESTES · DIFF · APROVAÇÃO")
        c.setFillColor(GRAY)
        c.setFont(ITALIC, 6.7)
        c.drawString(0, 2 * mm, "Papéis propostos para piloto; autenticações e cotas seguem separadas.")


class MixChart(Flowable):
    """Illustrative 100-task split; no money or quota percentage is inferred."""

    def __init__(self, width=178 * mm, height=49 * mm):
        super().__init__()
        self.width, self.height = width, height

    def wrap(self, avail_width, avail_height):
        self.width = avail_width
        return self.width, self.height

    def draw(self):
        c = self.canv
        c.setFillColor(BLOOD)
        c.rect(0, self.height - 11 * mm, self.width, 11 * mm, fill=1, stroke=0)
        c.setFillColor(colors.white)
        c.setFont(BOLD, 10)
        c.drawString(4 * mm, self.height - 7.3 * mm, "SIMULAÇÃO · MIX DE 100 TAREFAS / SEMANA")
        rows = [("Script local", 50, YELLOW), ("Codex", 30, RETRO_CYAN), ("Claude", 15, MAGENTA), ("Gemini", 5, BLOOD)]
        max_width = self.width - 35 * mm
        top = self.height - 17 * mm
        for i, (label, value, color) in enumerate(rows):
            y = top - i * 7.3 * mm
            c.setFillColor(LAY_BLACK)
            c.setFont(BOLD, 8)
            c.drawString(0, y, label)
            c.setFillColor(colors.HexColor("#DDD8CB"))
            c.rect(28 * mm, y - 1.2 * mm, max_width, 4.5 * mm, fill=1, stroke=0)
            c.setFillColor(color)
            c.rect(28 * mm, y - 1.2 * mm, max_width * value / 100, 4.5 * mm, fill=1, stroke=0)
            c.setFillColor(LAY_BLACK)
            c.setFont(BOLD, 8)
            c.drawRightString(self.width, y, f"{value}% · {value} tarefas")
        c.setFillColor(GRAY)
        c.setFont(ITALIC, 6.8)
        c.drawString(0, 1.5 * mm, "Proposta de alocação, não dado medido. Tarefa ≠ token; valide qualidade, cota e retrabalho no piloto.")


class TelemetryStrip(Flowable):
    def __init__(self, width=178 * mm, height=28 * mm):
        super().__init__()
        self.width, self.height = width, height

    def wrap(self, avail_width, avail_height):
        self.width = avail_width
        return self.width, self.height

    def draw(self):
        c = self.canv
        items = [("2.060", "CHAMADAS"), ("33", "SUBAGENTES"), ("313K", "CACHE LIDO / CHAMADA")]
        gap = 3 * mm
        w = (self.width - 2 * gap) / 3
        for i, (value, label) in enumerate(items):
            x = i * (w + gap)
            c.setFillColor(LAY_BLACK if i != 1 else BLOOD)
            c.rect(x, 0, w, self.height, fill=1, stroke=0)
            c.setFillColor(YELLOW if i != 1 else colors.white)
            c.setFont(BOLD, 18)
            c.drawString(x + 4 * mm, 12 * mm, value)
            c.setFillColor(BONE)
            c.setFont(BOLD, 6.3)
            c.drawString(x + 4 * mm, 5 * mm, label)


class TelemetryWindow(Flowable):
    def __init__(self, width=178 * mm, height=23 * mm):
        super().__init__()
        self.width, self.height = width, height

    def wrap(self, avail_width, avail_height):
        self.width = avail_width
        return self.width, self.height

    def draw(self):
        c = self.canv
        items = [("+24", "SUBAGENTES", YELLOW), ("+986", "CHAMADAS", RETRO_CYAN), ("+155,1M", "TOKENS DE CACHE LIDOS", MAGENTA)]
        gap = 2.5 * mm
        w = (self.width - 2 * gap) / 3
        c.setFillColor(LAY_BLACK)
        c.setFont(BOLD, 7)
        c.drawString(0, self.height - 4 * mm, "JANELA LOCAL · 07:55 → 12:57")
        for i, (value, label, accent) in enumerate(items):
            x = i * (w + gap)
            c.setFillColor(LAY_BLACK)
            c.rect(x, 0, w, self.height - 7 * mm, fill=1, stroke=0)
            c.setFillColor(accent)
            c.setFont(BOLD, 15)
            c.drawString(x + 3 * mm, 6.2 * mm, value)
            c.setFillColor(BONE)
            c.setFont(BOLD, 6.4)
            c.drawRightString(x + w - 3 * mm, 7 * mm, label)


def on_page(canvas, doc):
    canvas.saveState()
    width, height = doc.pagesize
    if doc.page == 1:
        canvas.setFillColor(LAY_BLACK)
        canvas.rect(0, 0, width, height, fill=1, stroke=0)
        canvas.setFillColor(YELLOW)
        canvas.rect(0, height - 11 * mm, width, 11 * mm, fill=1, stroke=0)
        canvas.setFillColor(BLOOD)
        canvas.rect(width - 18 * mm, 0, 18 * mm, height - 11 * mm, fill=1, stroke=0)
    else:
        canvas.setFillColor(BONE)
        canvas.rect(0, 0, width, height, fill=1, stroke=0)
        canvas.setFillColor(LAY_BLACK)
        canvas.rect(0, height - 4 * mm, width, 4 * mm, fill=1, stroke=0)
        canvas.setFillColor(BLOOD)
        canvas.rect(width - 5 * mm, 0, 5 * mm, height - 4 * mm, fill=1, stroke=0)
        canvas.setStrokeColor(BLOOD)
        canvas.setLineWidth(2.4)
        canvas.line(16 * mm, 13 * mm, 30 * mm, 13 * mm)
        canvas.setFont(REGULAR, 7.2)
        canvas.setFillColor(GRAY)
        canvas.drawString(33 * mm, 10.7 * mm, "LAY® / CADERNO DE PESQUISA · IA")
        canvas.drawRightString(width - 16 * mm, 10.7 * mm, f"{doc.page:02d}")
    canvas.restoreState()


def styles():
    base = getSampleStyleSheet()
    return {
        "cover_kicker": ParagraphStyle("cover_kicker", parent=base["Normal"], fontName=BOLD, fontSize=9.5, leading=13, textColor=YELLOW, alignment=TA_LEFT, spaceAfter=12),
        "cover_title": ParagraphStyle("cover_title", parent=base["Title"], fontName=BOLD, fontSize=43, leading=45, textColor=BONE, alignment=TA_LEFT, spaceAfter=14),
        "cover_subtitle": ParagraphStyle("cover_subtitle", parent=base["Normal"], fontName=REGULAR, fontSize=13, leading=18, textColor=BONE, spaceAfter=18),
        "meta": ParagraphStyle("meta", parent=base["Normal"], fontName=REGULAR, fontSize=8.6, leading=12, textColor=GRAY),
        "body": ParagraphStyle("body", parent=base["BodyText"], fontName=REGULAR, fontSize=10.7, leading=15, textColor=LAY_BLACK, leftIndent=10 * mm, rightIndent=42 * mm, spaceAfter=7),
        "callout": ParagraphStyle("callout", parent=base["BodyText"], fontName=BOLD, fontSize=11, leading=15, textColor=LAY_BLACK, leftIndent=10 * mm, rightIndent=42 * mm, spaceBefore=2, spaceAfter=9, borderColor=BLOOD, borderWidth=1.4, borderPadding=8, backColor=YELLOW),
        "h1": ParagraphStyle("h1", parent=base["Heading1"], fontName=BOLD, fontSize=18, leading=22, textColor=LAY_BLACK, spaceBefore=14, spaceAfter=8, keepWithNext=True),
        "h2": ParagraphStyle("h2", parent=base["Heading2"], fontName=BOLD, fontSize=13.5, leading=17, textColor=BLOOD, leftIndent=10 * mm, spaceBefore=13, spaceAfter=6, keepWithNext=True),
        "table": ParagraphStyle("table", parent=base["BodyText"], fontName=REGULAR, fontSize=8, leading=10, textColor=LAY_BLACK),
        "table_header": ParagraphStyle("table_header", parent=base["BodyText"], fontName=BOLD, fontSize=8, leading=10, textColor=LAY_BLACK),
        "bullet": ParagraphStyle("bullet", parent=base["BodyText"], fontName=REGULAR, fontSize=10.5, leading=14.5, leftIndent=14 * mm, rightIndent=42 * mm, firstLineIndent=-4 * mm, spaceAfter=5),
        "code": ParagraphStyle("code", parent=base["Code"], fontName="Courier", fontSize=7.1, leading=9, textColor=BONE, backColor=LAY_BLACK, borderPadding=8, spaceBefore=4, spaceAfter=8),
    }


class BarChart(Flowable):
    """Compact, labeled horizontal bars for one comparable benchmark only."""

    def __init__(self, title, subtitle, rows, max_value, unit, note, width=170 * mm, height=104):
        super().__init__()
        self.title = title
        self.subtitle = subtitle
        self.rows = rows
        self.max_value = max_value
        self.unit = unit
        self.note = note
        self.width = width
        self.height = height

    def wrap(self, avail_width, avail_height):
        self.width = avail_width
        return self.width, self.height

    def draw(self):
        c = self.canv
        c.setFillColor(BLACK)
        c.setFont(BOLD, 10)
        c.drawString(0, self.height - 12, self.title)
        c.setFillColor(GRAY)
        c.setFont(REGULAR, 7.4)
        c.drawString(0, self.height - 24, self.subtitle)
        label_w = 42 * mm
        value_w = 20 * mm
        bar_w = self.width - label_w - value_w - 3 * mm
        top = self.height - 39
        row_gap = 15
        for index, (label, value, color) in enumerate(self.rows):
            y = top - index * row_gap
            c.setFillColor(BLACK)
            c.setFont(REGULAR, 8)
            c.drawString(0, y, label)
            c.setFillColor(colors.HexColor("#E7E5DF"))
            c.rect(label_w, y - 1.5, bar_w, 8, fill=1, stroke=0)
            c.setFillColor(color)
            c.rect(label_w, y - 1.5, bar_w * value / self.max_value, 8, fill=1, stroke=0)
            c.setFillColor(BLACK)
            c.setFont(BOLD, 8)
            c.drawRightString(self.width, y, f"{value:g} {self.unit}")
        c.setFillColor(GRAY)
        c.setFont(ITALIC, 7.1)
        c.drawString(0, 4, self.note)


def benchmark_charts(s):
    blue = colors.HexColor("#087F9C")
    red = RED
    amber = colors.HexColor("#E49A1A")
    return [
        BarChart(
            "Código em tarefas agênticas",
            "Artificial Analysis Intelligence Index v5.0 · FrontierCode 2.0 · 31 out. 2026",
            [("Claude Opus 5.5 max", 46, red), ("GPT-6 Astra max", 42, blue),
             ("GPT-6.1 Sol Terra", 42, blue), ("Claude Sonnet 5.5", 42, amber)],
            50, "%",
            "46% contra 42% neste benchmark. A diferença não prevê sucesso em qualquer repositório.",
        ),
        BarChart(
            "Terminal e execução de ferramentas",
            "Artificial Analysis · Terminal-Bench-Science · snapshot de 31 out. 2026",
            [("GPT-6 Astra max", 63, blue), ("Claude Opus 5.5 max", 59, red)],
            70, "%",
            "Use como sinal para tarefas de terminal semelhantes; não compare com SWE-bench nem com uso geral.",
        ),
        BarChart(
            "Custo por tarefa na mesma bateria",
            "Artificial Analysis Intelligence Index v5.0 · USD por tarefa · mesma mistura de tarefas",
            [("Claude Opus 5.5 max", 10.04, red), ("GPT-6 Astra max", 6.24, blue),
             ("GPT-6 Sol max", 1.27, amber)],
            11, "USD",
            "O benchmark favorece Sol em custo observado; confirme qualidade e retrabalho no piloto do seu projeto.",
        ),
    ]


def story_from_markdown(source, s):
    story = [Spacer(1, 24 * mm), Paragraph("RELATÓRIO DE PESQUISA", s["cover_kicker"]),
             Paragraph("QUEM FAZ<br/>O QUÊ<br/>E A QUE CUSTO?", s["cover_title"]),
             Paragraph("Claude · Gemini / Antigravity · Codex<br/>Cotas, rankings, telemetria e uma rotina para gastar contexto com intenção.", s["cover_subtitle"]),
             Spacer(1, 7 * mm), Paragraph("LAY® / CADERNO DE PESQUISA\u2003·\u200331 OUT 2026", s["cover_kicker"]),
             Spacer(1, 7 * mm), Paragraph("DADOS DE BENCHMARK NÃO SÃO COTAS. RELATOS NÃO SÃO RANKINGS.\nEste relatório separa as evidências e mostra onde elas ajudam numa decisão diária.", s["cover_subtitle"]), PageBreak()]
    table_buffer = []
    in_code = False
    code_lines = []
    quote_buffer = []
    def flush_quote():
        nonlocal quote_buffer
        if quote_buffer:
            text = "<br/>".join(inline_markdown(item) for item in quote_buffer)
            story.append(Paragraph(text, s["callout"]))
            quote_buffer = []
    def flush_table():
        nonlocal table_buffer
        if table_buffer:
            story.extend([Spacer(1, 2 * mm), table_from_lines(table_buffer, s), Spacer(1, 4 * mm)])
            table_buffer = []
    for raw in source.splitlines():
        line = raw.rstrip()
        if line.strip().startswith("```"):
            if in_code:
                # The full textual workflow is preserved in Markdown; the PDF uses
                # the larger routing infographic and task matrix instead.
                code_lines.clear()
                in_code = False
            else:
                in_code = True
            continue
        if in_code:
            code_lines.append(line)
            continue
        if line.startswith("> "):
            quote_buffer.append(line[2:].strip())
            continue
        flush_quote()
        if line.startswith("|"):
            table_buffer.append(line)
            continue
        flush_table()
        if not line.strip() or line.startswith("# ") or line.strip() == "---":
            continue
        if line.startswith("## "):
            heading = line[3:]
            if any(heading.startswith(prefix) for prefix in ("1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.")):
                story.append(PageBreak())
            match = re.match(r"^(\d+)\.\s*(.*)$", heading)
            if match:
                number, title = match.groups()
                story.append(SectionBanner(title, number))
                story.append(Spacer(1, 4 * mm))
            else:
                title = heading
                story.append(Paragraph(inline_markdown(heading), s["h1"]))
            if heading.lower().startswith("sumário executivo"):
                story.extend([TelemetryStrip(), Spacer(1, 4 * mm)])
            if heading.startswith("1."):
                story.extend([TelemetryWindow(), Spacer(1, 2 * mm)])
            elif heading.startswith("2."):
                story.extend([
                    Paragraph("TRÊS TESTES · TRÊS PERGUNTAS DIFERENTES", s["h2"]),
                    Paragraph("Cada gráfico mantém a escala e o cenário da própria bateria. Use o resultado para escolher o que testar; não para ordenar todos os modelos de forma geral.", s["body"]),
                    *benchmark_charts(s),
                    Spacer(1, 4 * mm),
                    Paragraph("Leitura prática: experimente Opus para mudanças de código difíceis, Astra em tarefas de terminal e Sol em trabalho repetitivo sensível a custo. São candidatos para piloto. Não foi encontrado resultado comparável de Gemini/Antigravity nesses mesmos cenários; seu uso visual decorre das ferramentas do produto, sem score equivalente nesta pesquisa.", s["body"]),
                    Paragraph("Fonte: Artificial Analysis Intelligence Index v5.0 · snapshot de 31 out. 2026. Custo por tarefa pertence à bateria publicada, não à assinatura do leitor.", s["meta"]),
                ])
            elif heading.startswith("4."):
                story.extend([RoutingMap(), Spacer(1, 4 * mm)])
        elif line.startswith("### "):
            subheading = line[4:]
            if subheading.startswith("Matriz de Classes"):
                story.append(PageBreak())
            if subheading.startswith("[SIMULAÇÃO]"):
                story.append(PageBreak())
            story.append(Paragraph(inline_markdown(subheading), s["h2"]))
            if subheading.startswith("[SIMULAÇÃO]"):
                story.extend([MixChart(), Spacer(1, 4 * mm), Paragraph("O gráfico representa uma hipótese de distribuição para 100 tarefas por semana. Os percentuais não representam tokens, saldo de cota ou economia em dinheiro.", s["meta"]), Spacer(1, 3 * mm)])
        elif re.match(r"^\d+\.\s+", line):
            story.append(Paragraph(inline_markdown(line), s["bullet"]))
        elif re.match(r"^[-*] ", line):
            story.append(Paragraph("■ " + inline_markdown(line[2:]), s["bullet"]))
        else:
            story.append(Paragraph(inline_markdown(line), s["body"]))
    flush_table()
    flush_quote()
    return story


def build():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    document = BaseDocTemplate(str(OUTPUT), pagesize=PAGE_SIZE, leftMargin=14 * mm, rightMargin=14 * mm, topMargin=14 * mm, bottomMargin=17 * mm, title="Relatório Orquestração Multiagente Evidências 2026", author="LAY")
    frame = Frame(document.leftMargin, document.bottomMargin, document.width, document.height, id="body")
    document.addPageTemplates([PageTemplate(id="report", frames=[frame], onPage=on_page)])
    document.build(story_from_markdown(SOURCE.read_text(encoding="utf-8"), styles()))
    print(OUTPUT)


if __name__ == "__main__":
    build()

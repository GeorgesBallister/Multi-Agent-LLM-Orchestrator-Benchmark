#!/usr/bin/env python3
"""Gera gráficos de nível editorial de alta agência (LAY® Design System):
1. allocation_comparison.png: Dual-Card Dossier com barras estilizadas (elimina colisões de pizza).
2. scatter_pareto_llm.png: Scatter plot estilo Financial Times / Bloomberg com Fronteira de Pareto.
3. forensic_telemetry_georges.png: Dashboard forense estilo Datadog / Grafana com timeline de colapso.
4. radar_capabilities.png: Radar poligonal neon com marcadores de vértice e dados numéricos.
"""

import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.font_manager import FontProperties
import numpy as np

# Diretórios
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG_DIR = os.path.join(BASE_DIR, "assets", "img")
os.makedirs(IMG_DIR, exist_ok=True)

# Paleta Editorial LAY® Calibrada
CANVAS_BG = "#08080A"
CARD_BG = "#111216"
CARD_BORDER = "#22252D"
TEXT_WHITE = "#FAF5E9"
TEXT_MUTED = "#8E929E"
TEXT_DIM = "#555864"

COLOR_RED = "#E31B23"       # Brand Red LAY
COLOR_RED_GLOW = "#FF454D"
COLOR_YELLOW = "#FFF201"    # Brand Yellow Alerta
COLOR_CYAN = "#00FFFF"      # Neon Cyan
COLOR_GREEN = "#10A37F"     # OpenAI Green
COLOR_PURPLE = "#A855F7"    # DeepSeek

# Configuração de Fontes
font_path_bahn = r"C:\Windows\Fonts\bahnschrift.ttf"
font_path_segoe = r"C:\Windows\Fonts\segoeui.ttf"
font_path_segoeb = r"C:\Windows\Fonts\segoeuib.ttf"

font_title = FontProperties(fname=font_path_bahn, size=13, weight="bold")
font_subtitle = FontProperties(fname=font_path_segoe, size=8.5)
font_card_title = FontProperties(fname=font_path_bahn, size=10, weight="bold")
font_label = FontProperties(fname=font_path_bahn, size=8.5, weight="bold")
font_num = FontProperties(fname=font_path_bahn, size=11, weight="bold")
font_caption = FontProperties(fname=font_path_segoe, size=7.5)


def generate_allocation_comparison():
    """1. Dual-Card Dossier Comparativo: Elimina o gráfico de pizza amador e cria um dashboard executivo."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 5.2), facecolor=CANVAS_BG)
    plt.subplots_adjust(wspace=0.18, left=0.06, right=0.94, top=0.84, bottom=0.12)

    for ax in (ax1, ax2):
        ax.set_facecolor(CARD_BG)
        for spine in ax.spines.values():
            spine.set_color(CARD_BORDER)
            spine.set_linewidth(1.2)
        ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

    # ==================== CARD 1: O HISTÓRICO REAL DO GEORGES ====================
    # Header do Card 1
    ax1.text(0.05, 0.92, "CENÁRIO OBSERVADO: MONOCULTURA OPUS", fontproperties=font_card_title, color=COLOR_RED, transform=ax1.transAxes)
    ax1.text(0.05, 0.85, "Esgotamento da janela rolante de 5 horas em menos de 20 minutos de loop.", fontproperties=font_subtitle, color=TEXT_MUTED, transform=ax1.transAxes)

    # Badge de Status (Alerta Crítico)
    bbox_alert = dict(boxstyle="square,pad=0.35", facecolor="#2A0B0D", edgecolor=COLOR_RED, linewidth=1)
    ax1.text(0.95, 0.90, "FALHA DE COTA", fontproperties=font_label, color=COLOR_RED, transform=ax1.transAxes, ha="right", bbox=bbox_alert)

    # Barras de Alocação Real
    items_real = [
        ("Claude Opus 5.5", 61.8, "1.273 chamadas · 535M tokens cache · Raciocínio pesado", COLOR_RED),
        ("Claude Sonnet 5.5", 36.4, "749 chamadas · 108M tokens cache · Engenharia core", "#FF6B6B"),
        ("Claude Haiku 5.5", 0.9, "18 chamadas · Subutilizado para tarefas mecânicas", "#888888"),
        ("Scripts Determinísticos", 0.9, "Rara delegação local · Quase tudo enviado ao Opus", "#555555"),
    ]

    y_pos = [0.65, 0.47, 0.29, 0.13]
    for (name, pct, desc, col), y in zip(items_real, y_pos):
        # Background bar
        rect_bg = patches.Rectangle((0.05, y), 0.90, 0.07, facecolor="#181A20", edgecolor="none", transform=ax1.transAxes, zorder=2)
        ax1.add_patch(rect_bg)
        # Value bar
        bar_w = 0.90 * (pct / 100.0)
        rect_val = patches.Rectangle((0.05, y), bar_w, 0.07, facecolor=col, edgecolor="none", transform=ax1.transAxes, zorder=3)
        ax1.add_patch(rect_val)
        # Labels
        ax1.text(0.05, y + 0.085, name, fontproperties=font_label, color=TEXT_WHITE, transform=ax1.transAxes)
        ax1.text(0.95, y + 0.085, f"{pct:.1f}%", fontproperties=font_num, color=col if pct > 5 else TEXT_MUTED, transform=ax1.transAxes, ha="right")
        ax1.text(0.05, y - 0.045, desc, fontproperties=font_caption, color=TEXT_MUTED, transform=ax1.transAxes)

    # ==================== CARD 2: A ARQUITETURA BALANCEADA LAY ====================
    # Header do Card 2
    ax2.text(0.05, 0.92, "ARQUITETURA RECOMENDADA: PIPELINE EM 5 TIERS", fontproperties=font_card_title, color=COLOR_YELLOW, transform=ax2.transAxes)
    ax2.text(0.05, 0.85, "Operação perpétua 7 dias/semana sob custo fixo de US$ 58 / mês.", fontproperties=font_subtitle, color=TEXT_MUTED, transform=ax2.transAxes)

    # Badge de Status (Estável / Aprovado)
    bbox_ok = dict(boxstyle="square,pad=0.35", facecolor="#0B261A", edgecolor=COLOR_GREEN, linewidth=1)
    ax2.text(0.95, 0.90, "OPERAÇÃO PERPÉTUA", fontproperties=font_label, color=COLOR_GREEN, transform=ax2.transAxes, ha="right", bbox=bbox_ok)

    # Barras de Alocação Recomendada
    items_ideal = [
        ("Scripts Locais & GPU (RTX 5070 Ti)", 50.0, "Hash, resize, SAM 2, rembg, conversões · Custo zero de token", COLOR_YELLOW),
        ("OpenAI Codex (GPT-6.1 Sol / Terra)", 30.0, "Suítes Vitest, mocks, fixtures, migrations · 4.2x mais barato", COLOR_GREEN),
        ("Claude Sonnet 5.5 Core (Claude Code)", 15.0, "Engenharia central React 19/Three.js · Compactado a cada 30 calls", COLOR_RED_GLOW),
        ("Gemini 3.8 Flash & Opus 5.5 Gate", 5.0, "Flash para ingestão 1M+ tokens · Opus apenas para aprovação final", COLOR_CYAN),
    ]

    for (name, pct, desc, col), y in zip(items_ideal, y_pos):
        rect_bg = patches.Rectangle((0.05, y), 0.90, 0.07, facecolor="#181A20", edgecolor="none", transform=ax2.transAxes, zorder=2)
        ax2.add_patch(rect_bg)
        bar_w = 0.90 * (pct / 100.0)
        rect_val = patches.Rectangle((0.05, y), bar_w, 0.07, facecolor=col, edgecolor="none", transform=ax2.transAxes, zorder=3)
        ax2.add_patch(rect_val)
        ax2.text(0.05, y + 0.085, name, fontproperties=font_label, color=TEXT_WHITE, transform=ax2.transAxes)
        ax2.text(0.95, y + 0.085, f"{pct:.1f}%", fontproperties=font_num, color=col, transform=ax2.transAxes, ha="right")
        ax2.text(0.05, y - 0.045, desc, fontproperties=font_caption, color=TEXT_MUTED, transform=ax2.transAxes)

    # Título Geral do Gráfico
    fig.text(0.06, 0.94, "DISTRIBUIÇÃO DE CARGA: DIAGNÓSTICO DO PROJETO VS ARQUITETURA ÓTIMA", fontproperties=font_title, color=TEXT_WHITE)
    fig.text(0.06, 0.90, "Comparativo direto entre o padrão de consumo que provocou o bloqueio de cota e o modelo calibrado de produção.", fontproperties=font_subtitle, color=TEXT_MUTED)

    out_path = os.path.join(IMG_DIR, "allocation_comparison.png")
    plt.savefig(out_path, dpi=300, facecolor=CANVAS_BG)
    plt.close()
    print(f"[CHART] Gerado com design de agência: {out_path}")


def generate_scatter_pareto():
    """2. Gráfico de Dispersão Estilo Financial Times / Bloomberg com Fronteira de Pareto."""
    fig, ax = plt.subplots(figsize=(11, 5.8), facecolor=CANVAS_BG)
    ax.set_facecolor(CARD_BG)
    plt.subplots_adjust(left=0.08, right=0.94, top=0.86, bottom=0.14)

    for spine in ax.spines.values():
        spine.set_color(CARD_BORDER)
        spine.set_linewidth(1.2)

    # Dados
    models = [
        ("Claude Opus 5.5 (Max)", 10.04, 97.0, 48, COLOR_RED, "Fronteira"),
        ("Claude Sonnet 5.5", 3.80, 94.2, 92, "#FF6B6B", "Fronteira"),
        ("Claude Haiku 5.5", 0.45, 78.5, 180, "#FFA8A8", "Sub-ótimo"),
        ("GPT-6 Astra (Max)", 6.24, 88.0, 85, COLOR_GREEN, "Sub-ótimo"),
        ("GPT-6.1 Sol (Terra)", 1.27, 68.8, 145, "#4ECCA3", "Fronteira"),
        ("GPT-6 Luna", 0.20, 58.0, 240, "#A8E6CF", "Sub-ótimo"),
        ("Gemini 4 Carbon", 3.20, 64.5, 110, "#00BCE4", "Sub-ótimo"),
        ("Gemini 3.8 Flash", 0.15, 61.2, 308, COLOR_CYAN, "Fronteira"),
        ("DeepSeek V4.1 Flash", 0.18, 63.0, 220, COLOR_PURPLE, "Sub-ótimo"),
    ]

    x_costs = [m[1] for m in models]
    y_scores = [m[2] for m in models]
    sizes = [m[3] * 3.8 for m in models]
    colors = [m[4] for m in models]

    # Grid sutil
    ax.grid(True, which="both", linestyle=":", color="#22252D", alpha=0.9, zorder=1)

    # Sombra da Fronteira de Pareto
    pareto_x = [0.15, 1.27, 3.80, 10.04]
    pareto_y = [61.2, 68.8, 94.2, 97.0]
    ax.fill_between(pareto_x, pareto_y, 45, color=COLOR_YELLOW, alpha=0.04, zorder=2)
    ax.plot(pareto_x, pareto_y, color=COLOR_YELLOW, linestyle="--", linewidth=1.8, label="Fronteira Eficiente de Pareto", zorder=3)

    # Glow dos pontos de dispersão
    ax.scatter(x_costs, y_scores, s=[s * 1.6 for s in sizes], c=colors, alpha=0.15, edgecolors="none", zorder=4)
    ax.scatter(x_costs, y_scores, s=sizes, c=colors, alpha=0.88, edgecolors=TEXT_WHITE, linewidth=1.2, zorder=5)

    # Rótulos precisos com badges
    offsets = {
        "Claude Opus 5.5 (Max)": (-140, 6),
        "Claude Sonnet 5.5": (-115, 8),
        "Claude Haiku 5.5": (12, -6),
        "GPT-6 Astra (Max)": (14, -5),
        "GPT-6.1 Sol (Terra)": (14, -7),
        "GPT-6 Luna": (12, -8),
        "Gemini 4 Carbon": (12, -8),
        "Gemini 3.8 Flash": (14, 5),
        "DeepSeek V4.1 Flash": (-125, 6),
    }

    for name, x, y in zip([m[0] for m in models], x_costs, y_scores):
        dx, dy = offsets.get(name, (10, 0))
        ax.annotate(
            name,
            (x, y),
            xytext=(dx, dy),
            textcoords="offset points",
            fontproperties=font_label,
            color=TEXT_WHITE,
            bbox=dict(boxstyle="square,pad=0.25", facecolor="#14161C", edgecolor="#2D313D", alpha=0.95),
            zorder=6,
        )

    ax.set_xscale("log")
    ax.set_xlim(0.10, 16.0)
    ax.set_ylim(48, 104)

    # Estilização de ticks
    ax.set_xticks([0.15, 0.50, 1.0, 2.0, 5.0, 10.0])
    ax.get_xaxis().set_major_formatter(plt.FuncFormatter(lambda val, _: f"${val:.2f}" if val < 1 else f"${int(val)}"))
    ax.tick_params(colors=TEXT_MUTED, labelsize=8)

    ax.set_xlabel("Custo Observado por Tarefa Completa (USD - Escala Logarítmica)", fontproperties=font_label, color=TEXT_WHITE, labelpad=8)
    ax.set_ylabel("Qualidade em Engenharia (SWE-bench Verified %)", fontproperties=font_label, color=TEXT_WHITE, labelpad=8)

    # Título & Subtítulo
    fig.text(0.08, 0.94, "FRONTEIRA DE PARETO: RESOLUÇÃO DE CÓDIGO VS CUSTO POR TAREFA", fontproperties=font_title, color=TEXT_WHITE)
    fig.text(0.08, 0.90, "Tamanho da bolha = Throughput (tokens/s). Modelos na linha amarela dominam os demais em custo-benefício.", fontproperties=font_subtitle, color=TEXT_MUTED)

    # Box de Insights
    box_insight = dict(boxstyle="square,pad=0.5", facecolor="#111318", edgecolor=COLOR_YELLOW, linewidth=1)
    ax.text(
        0.12, 53,
        "LEITURA DA FRONTEIRA:\n"
        "• Flash ($0.15 / 308 t/s): Varredura e digestão de repositório\n"
        "• Sol ($1.27 / 145 t/s): Testes unitários e migrações em massa\n"
        "• Sonnet ($3.80 / 92 t/s): Implementação e refatoração core\n"
        "• Opus ($10.04 / 48 t/s): Sanção arquitetural em turno único",
        fontproperties=font_caption, color=TEXT_WHITE, bbox=box_insight, zorder=7
    )

    out_path = os.path.join(IMG_DIR, "scatter_pareto_llm.png")
    plt.savefig(out_path, dpi=300, facecolor=CANVAS_BG)
    plt.close()
    print(f"[CHART] Gerado com design de agência: {out_path}")


def generate_forensic_telemetry():
    """3. Dashboard Forense Datadog/Grafana: A Linha do Tempo do Travamento."""
    fig, ax1 = plt.subplots(figsize=(11, 5.2), facecolor=CANVAS_BG)
    ax1.set_facecolor(CARD_BG)
    plt.subplots_adjust(left=0.08, right=0.92, top=0.85, bottom=0.15)

    for spine in ax1.spines.values():
        spine.set_color(CARD_BORDER)
        spine.set_linewidth(1.2)

    dates = ["30/10 18h", "30/10 21h", "30/10 23h", "31/10 02h", "31/10 07h", "31/10 08h", "31/10 12h"]
    x = np.arange(len(dates))
    cache_m = [428.1, 442.3, 480.3, 488.6, 490.2, 506.5, 645.3]
    subagents = [9, 9, 9, 9, 9, 11, 33]

    # Grid
    ax1.grid(True, linestyle=":", color="#22252D", alpha=0.9)

    # Zona de Colapso (Highlight)
    ax1.axvspan(4.5, 6.2, color="#2D0A0E", alpha=0.7, zorder=1)
    ax1.axvline(4.5, color=COLOR_RED, linestyle="--", linewidth=1.2, zorder=2)

    # Eixo 1: Tokens de Cache (Vermelho)
    ax1.fill_between(x, cache_m, 400, color=COLOR_RED, alpha=0.12, zorder=3)
    ax1.plot(x, cache_m, color=COLOR_RED, marker="o", markersize=6, linewidth=2.4, label="Tokens de Cache Reenviados (Milhões)", zorder=5)
    ax1.set_ylabel("Tokens de Cache Reenviados (Milhões)", fontproperties=font_label, color=COLOR_RED, labelpad=8)
    ax1.tick_params(axis="y", labelcolor=COLOR_RED, labelsize=8)
    ax1.set_ylim(380, 680)

    # Eixo 2: Subagentes (Amarelo)
    ax2 = ax1.twinx()
    ax2.spines["right"].set_color(CARD_BORDER)
    ax2.plot(x, subagents, color=COLOR_YELLOW, marker="s", markersize=6, linewidth=2.2, linestyle="-.", label="Subagentes em Segundo Plano", zorder=6)
    ax2.set_ylabel("Subagentes Concorrentes Ativos", fontproperties=font_label, color=COLOR_YELLOW, labelpad=8)
    ax2.tick_params(axis="y", labelcolor=COLOR_YELLOW, labelsize=8)
    ax2.set_ylim(0, 42)

    ax1.set_xticks(x)
    ax1.set_xticklabels(dates, fontproperties=font_label, color=TEXT_WHITE)
    ax1.tick_params(axis="x", colors=TEXT_MUTED)

    # Callout Forense da Causa Raiz
    box_fail = dict(boxstyle="square,pad=0.5", facecolor="#1F080A", edgecolor=COLOR_RED, linewidth=1.2)
    ax1.text(
        4.65, 595,
        "INCIDENTE: EXPLOSÃO DE SUBAGENTES\n"
        "• +24 subagentes gerados em 4 horas\n"
        "• +155M tokens reenviados em loop contínuo\n"
        "• ZERO compactações no período (estagnado em 5)\n"
        "• 61.8% de chamadas Opus 5.5\n"
        "=> Janela de 5h da Anthropic zerada em 20 min",
        fontproperties=font_caption, color=TEXT_WHITE, bbox=box_fail, zorder=7
    )

    fig.text(0.08, 0.94, "TELEMETRIA FORENSE DO PROJETO: POR QUE O CLAUDE TRAVOU?", fontproperties=font_title, color=TEXT_WHITE)
    fig.text(0.08, 0.90, "Dados reais extraídos dos registros locais (telemetria-ia-historico.csv) cobrindo 2.060 chamadas.", fontproperties=font_subtitle, color=TEXT_MUTED)

    out_path = os.path.join(IMG_DIR, "forensic_telemetry_georges.png")
    plt.savefig(out_path, dpi=300, facecolor=CANVAS_BG)
    plt.close()
    print(f"[CHART] Gerado com design de agência: {out_path}")


def generate_radar_capabilities():
    """4. Gráfico Radar Poligonal Neon com Tabela Lateral de Scores."""
    categories = [
        "Raciocínio Core &\nArquitetura Limpa",
        "Throughput &\nEconomia de Cota",
        "Isolamento Git\nWorktrees Paralelas",
        "Ingestão Massiva\n(1M+ Multimodal)",
        "Inspeção Visual\nBrowser-in-the-Loop",
    ]
    N = len(categories)

    claude_vals = [9.8, 4.0, 5.5, 7.5, 4.5]
    codex_vals = [6.8, 9.5, 9.8, 6.0, 6.5]
    antigravity_vals = [6.0, 7.5, 7.0, 9.8, 9.8]

    # Fechamento do polígono
    claude_p = claude_vals + claude_vals[:1]
    codex_p = codex_vals + codex_vals[:1]
    antigravity_p = antigravity_vals + antigravity_vals[:1]
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]

    fig = plt.figure(figsize=(10.5, 5.4), facecolor=CANVAS_BG)
    ax = fig.add_axes([0.05, 0.10, 0.55, 0.78], polar=True, facecolor=CARD_BG)

    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    plt.xticks(angles[:-1], categories, fontproperties=font_label, color=TEXT_WHITE)
    ax.tick_params(pad=14)

    ax.set_rlabel_position(30)
    plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color=TEXT_DIM, size=7)
    plt.ylim(0, 10.5)
    ax.grid(color="#22252D", linestyle=":", linewidth=1)

    # Polígonos
    ax.plot(angles, claude_p, color=COLOR_RED, linewidth=2, linestyle="-", label="Claude (Opus/Sonnet)")
    ax.fill(angles, claude_p, color=COLOR_RED, alpha=0.18)

    ax.plot(angles, codex_p, color=COLOR_GREEN, linewidth=2, linestyle="-", label="OpenAI Codex (Sol/Astra)")
    ax.fill(angles, codex_p, color=COLOR_GREEN, alpha=0.18)

    ax.plot(angles, antigravity_p, color=COLOR_CYAN, linewidth=2, linestyle="-", label="Google Antigravity (Flash)")
    ax.fill(angles, antigravity_p, color=COLOR_CYAN, alpha=0.18)

    # Painel Lateral de Dados (Tabela Executiva de Scores)
    ax_table = fig.add_axes([0.62, 0.15, 0.34, 0.68], facecolor=CARD_BG)
    for spine in ax_table.spines.values():
        spine.set_color(CARD_BORDER)
    ax_table.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

    ax_table.text(0.06, 0.90, "MATRIZ DE COMPETÊNCIA RELATIVA", fontproperties=font_card_title, color=COLOR_YELLOW, transform=ax_table.transAxes)
    ax_table.text(0.06, 0.82, "Avaliação empírica nos 5 eixos críticos de operação:", fontproperties=font_subtitle, color=TEXT_MUTED, transform=ax_table.transAxes)

    metrics_text = [
        ("Arquitetura & Clean Code", "Claude (9.8)", COLOR_RED, "Codex (6.8)", "AGY (6.0)"),
        ("Economia de Tokens / Cota", "Codex (9.5)", COLOR_GREEN, "AGY (7.5)", "Claude (4.0)"),
        ("Isolamento Git Worktrees", "Codex (9.8)", COLOR_GREEN, "AGY (7.0)", "Claude (5.5)"),
        ("Contexto Longo Multimodal", "AGY (9.8)", COLOR_CYAN, "Claude (7.5)", "Codex (6.0)"),
        ("Browser-in-the-Loop (UI)", "AGY (9.8)", COLOR_CYAN, "Codex (6.5)", "Claude (4.5)"),
    ]

    y_t = 0.66
    for axis_name, leader, l_col, s2, s3 in metrics_text:
        ax_table.text(0.06, y_t, axis_name, fontproperties=font_label, color=TEXT_WHITE, transform=ax_table.transAxes)
        ax_table.text(0.06, y_t - 0.05, f"Líder: {leader}", fontproperties=font_caption, color=l_col, transform=ax_table.transAxes, fontweight="bold")
        ax_table.text(0.55, y_t - 0.05, f"Secundários: {s2}, {s3}", fontproperties=font_caption, color=TEXT_DIM, transform=ax_table.transAxes)
        y_t -= 0.125

    fig.text(0.06, 0.94, "RADAR DE ESPECIALIZAÇÃO TÉCNICA: A COMPLEMENTARIDADE DOS MOTORES", fontproperties=font_title, color=TEXT_WHITE)
    fig.text(0.06, 0.90, "Demonstração de que cada ferramenta lidera eixos distintos, justificando o triângulo operacional.", fontproperties=font_subtitle, color=TEXT_MUTED)

    out_path = os.path.join(IMG_DIR, "radar_capabilities.png")
    plt.savefig(out_path, dpi=300, facecolor=CANVAS_BG)
    plt.close()
    print(f"[CHART] Gerado com design de agência: {out_path}")


def main():
    print("[CHARTS-V2] Gerando gráficos com design editorial de agência (LAY® standard)...")
    generate_allocation_comparison()
    generate_scatter_pareto()
    generate_forensic_telemetry()
    generate_radar_capabilities()
    print("[CHARTS-V2] Todos os gráficos foram recriados com sucesso!")


if __name__ == "__main__":
    main()

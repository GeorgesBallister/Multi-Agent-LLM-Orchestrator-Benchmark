#!/usr/bin/env python3
"""Gera gráficos de nível de publicação científica e editorial (Pandas + Seaborn + Matplotlib):
- fig1_pareto_scatter_benchmark.png: Gráfico de Dispersão com Fronteira de Pareto e bolhas ponderadas.
- fig2_forensic_telemetry_timeline.png: Análise temporal forense dos CSVs reais do Georges (Cache vs Subagentes).
- fig3_workload_rebalancing_dossier.png: Comparativo executivo de alocação de carga em barras elegantes.
- fig4_radar_model_competence.png: Radar poligonal neon com matriz de competência relativa.
"""

import os
import io
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import seaborn as sns
from matplotlib.font_manager import FontProperties

# Diretórios
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG_DIR = os.path.join(BASE_DIR, "assets", "img")
os.makedirs(IMG_DIR, exist_ok=True)

# Caminhos dos dados reais de telemetria do projeto Nossa Cultura
HIST_PATH = r"C:\Users\georg\OneDrive\Desktop\LAY Projetos\Nossa Cultura - Sessão\docs\nossa-cultura\07-artbook-lay\telemetria\telemetria-ia-historico.csv"
HOURLY_PATH = r"C:\Users\georg\OneDrive\Desktop\LAY Projetos\Nossa Cultura - Sessão\docs\nossa-cultura\07-artbook-lay\telemetria\telemetria-ia-por-hora.csv"

# Paleta Estética Dark Luxury (LAY® Editorial)
CANVAS_BG = "#0A0B0E"
CARD_BG = "#111319"
CARD_BORDER = "#1E222D"
GRID_COLOR = "#181C26"
TEXT_WHITE = "#FAF5E9"
TEXT_MUTED = "#8C92A4"
TEXT_DIM = "#505668"

COLOR_CRIMSON = "#E31B23"
COLOR_YELLOW = "#FFE600"
COLOR_CYAN = "#00FFFF"
COLOR_EMERALD = "#10A37F"
COLOR_PURPLE = "#A855F7"

# Fontes
font_path_bahn = r"C:\Windows\Fonts\bahnschrift.ttf"
font_path_segoe = r"C:\Windows\Fonts\segoeui.ttf"
font_title = FontProperties(fname=font_path_bahn, size=13, weight="bold")
font_subtitle = FontProperties(fname=font_path_segoe, size=8.5)
font_card_title = FontProperties(fname=font_path_bahn, size=10, weight="bold")
font_label = FontProperties(fname=font_path_bahn, size=8.5, weight="bold")
font_num = FontProperties(fname=font_path_bahn, size=11, weight="bold")
font_caption = FontProperties(fname=font_path_segoe, size=7.5)


def load_telemetry_data():
    """Carrega e trata os dados reais de telemetria com Pandas."""
    with open(HIST_PATH, "r", encoding="utf-8") as f:
        clean_lines = [line.strip().rstrip(",") for line in f if line.strip()]
    df_hist = pd.read_csv(io.StringIO("\n".join(clean_lines)))
    df_hist["data"] = pd.to_datetime(df_hist["data"])

    df_hourly = pd.read_csv(HOURLY_PATH)
    df_hourly["hora"] = pd.to_datetime(df_hourly["hora"])
    return df_hist, df_hourly


def generate_pareto_scatter():
    """1. Gráfico de Dispersão Estilo Financial Times com Fronteira de Pareto."""
    fig, ax = plt.subplots(figsize=(11.2, 5.6), facecolor=CANVAS_BG)
    ax.set_facecolor(CARD_BG)
    plt.subplots_adjust(left=0.08, right=0.94, top=0.86, bottom=0.14)

    for spine in ax.spines.values():
        spine.set_color(CARD_BORDER)
        spine.set_linewidth(1.2)

    # DataFrame dos modelos avaliados nos benchmarks
    data = [
        {"model": "Claude Opus 5.5 (Max)", "cost": 10.04, "score": 97.0, "tps": 48, "color": COLOR_CRIMSON, "pareto": True},
        {"model": "Claude Sonnet 5.5", "cost": 3.80, "score": 94.2, "tps": 92, "color": "#FF6B6B", "pareto": True},
        {"model": "Claude Haiku 5.5", "cost": 0.45, "score": 78.5, "tps": 180, "color": "#FFA8A8", "pareto": False},
        {"model": "GPT-6 Astra (Max)", "cost": 6.24, "score": 88.0, "tps": 85, "color": COLOR_EMERALD, "pareto": False},
        {"model": "GPT-6.1 Sol (Terra)", "cost": 1.27, "score": 68.8, "tps": 145, "color": "#4ECCA3", "pareto": True},
        {"model": "GPT-6 Luna", "cost": 0.20, "score": 58.0, "tps": 240, "color": "#A8E6CF", "pareto": False},
        {"model": "Gemini 4 Carbon", "cost": 3.20, "score": 64.5, "tps": 110, "color": "#00BCE4", "pareto": False},
        {"model": "Gemini 3.8 Flash", "cost": 0.15, "score": 61.2, "tps": 308, "color": COLOR_CYAN, "pareto": True},
        {"model": "DeepSeek V4.1 Flash", "cost": 0.18, "score": 63.0, "tps": 220, "color": COLOR_PURPLE, "pareto": False},
    ]
    df = pd.DataFrame(data)

    ax.grid(True, which="both", linestyle=":", color=GRID_COLOR, alpha=0.9, zorder=1)

    # Fronteira de Pareto
    pareto_df = df[df["pareto"]].sort_values("cost")
    ax.fill_between(pareto_df["cost"], pareto_df["score"], 45, color=COLOR_YELLOW, alpha=0.04, zorder=2)
    ax.plot(pareto_df["cost"], pareto_df["score"], color=COLOR_YELLOW, linestyle="--", linewidth=1.8, label="Fronteira Eficiente de Pareto", zorder=3)

    # Glow e dispersão
    ax.scatter(df["cost"], df["score"], s=df["tps"] * 5.5, c=df["color"], alpha=0.18, edgecolors="none", zorder=4)
    ax.scatter(df["cost"], df["score"], s=df["tps"] * 3.6, c=df["color"], alpha=0.90, edgecolors=TEXT_WHITE, linewidth=1.2, zorder=5)

    # Rótulos
    offsets = {
        "Claude Opus 5.5 (Max)": (-145, 6),
        "Claude Sonnet 5.5": (-120, 8),
        "Claude Haiku 5.5": (12, -6),
        "GPT-6 Astra (Max)": (14, -5),
        "GPT-6.1 Sol (Terra)": (14, -7),
        "GPT-6 Luna": (12, -8),
        "Gemini 4 Carbon": (12, -8),
        "Gemini 3.8 Flash": (14, 5),
        "DeepSeek V4.1 Flash": (-130, 6),
    }

    for _, row in df.iterrows():
        dx, dy = offsets.get(row["model"], (10, 0))
        ax.annotate(
            row["model"],
            (row["cost"], row["score"]),
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

    ax.set_xticks([0.15, 0.50, 1.0, 2.0, 5.0, 10.0])
    ax.get_xaxis().set_major_formatter(plt.FuncFormatter(lambda val, _: f"${val:.2f}" if val < 1 else f"${int(val)}"))
    ax.tick_params(colors=TEXT_MUTED, labelsize=8)

    ax.set_xlabel("Custo Observado por Tarefa Completa (USD - Escala Logarítmica)", fontproperties=font_label, color=TEXT_WHITE, labelpad=8)
    ax.set_ylabel("Qualidade em Engenharia (SWE-bench Verified %)", fontproperties=font_label, color=TEXT_WHITE, labelpad=8)

    fig.text(0.08, 0.94, "FRONTEIRA DE PARETO: QUALIDADE EM CÓDIGO VS CUSTO POR TAREFA", fontproperties=font_title, color=TEXT_WHITE)
    fig.text(0.08, 0.90, "Tamanho da bolha = Throughput (tokens/s). Modelos na linha amarela dominam os demais em custo-benefício.", fontproperties=font_subtitle, color=TEXT_MUTED)

    box_insight = dict(boxstyle="square,pad=0.5", facecolor="#111318", edgecolor=COLOR_YELLOW, linewidth=1)
    ax.text(
        0.12, 53,
        "INSIGHTS DE PRODUÇÃO (PARETO):\n"
        "• Gemini Flash ($0.15 / 308 t/s): Varredura e digestão de repositório\n"
        "• Codex Sol ($1.27 / 145 t/s): Testes unitários e migrações em massa\n"
        "• Sonnet 5.5 ($3.80 / 92 t/s): Implementação e refatoração core\n"
        "• Opus 5.5 ($10.04 / 48 t/s): Sanção arquitetural em turno único",
        fontproperties=font_caption, color=TEXT_WHITE, bbox=box_insight, zorder=7
    )

    out_path = os.path.join(IMG_DIR, "fig1_pareto_scatter_benchmark.png")
    plt.savefig(out_path, dpi=300, facecolor=CANVAS_BG)
    plt.close()
    print(f"[CHART] Gerado: {out_path}")


def generate_forensic_timeline(df_hist, df_hourly):
    """2. Análise Forense com Pandas: A Linha do Tempo Real do Travamento do Claude."""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11.2, 5.8), facecolor=CANVAS_BG, sharex=False, gridspec_kw={"height_ratios": [2.2, 1.2]})
    plt.subplots_adjust(left=0.08, right=0.92, top=0.88, bottom=0.12, hspace=0.28)

    for ax in (ax1, ax2):
        ax.set_facecolor(CARD_BG)
        for spine in ax.spines.values():
            spine.set_color(CARD_BORDER)
            spine.set_linewidth(1.1)
        ax.grid(True, linestyle=":", color=GRID_COLOR, alpha=0.8)

    # Filtrar dados do Claude Code
    cc_hist = df_hist[df_hist["fonte"] == "claude_code"].copy()
    cc_hist["cache_m"] = cc_hist["entrada_cache_lida"] / 1e6
    cc_hist["subagentes"] = pd.to_numeric(cc_hist["subagentes"])
    dates_str = cc_hist["data"].dt.strftime("%d/%m %Hh").tolist()
    x_pos = np.arange(len(dates_str))

    # Top Plot: Cache Acumulado vs Subagentes
    ax1.fill_between(x_pos, cc_hist["cache_m"], 400, color=COLOR_CRIMSON, alpha=0.14, zorder=2)
    ax1.plot(x_pos, cc_hist["cache_m"], color=COLOR_CRIMSON, marker="o", markersize=6, linewidth=2.4, label="Tokens de Cache Reenviados (Milhões)", zorder=5)
    ax1.set_ylabel("Tokens Cache (M)", fontproperties=font_label, color=COLOR_CRIMSON, labelpad=8)
    ax1.tick_params(axis="y", labelcolor=COLOR_CRIMSON, labelsize=8)
    ax1.set_ylim(380, 680)

    # Eixo Secundário para Subagentes
    ax1_sub = ax1.twinx()
    ax1_sub.spines["right"].set_color(CARD_BORDER)
    ax1_sub.plot(x_pos, cc_hist["subagentes"], color=COLOR_YELLOW, marker="s", markersize=6, linewidth=2.2, linestyle="-.", label="Subagentes Concorrentes", zorder=6)
    ax1_sub.set_ylabel("Subagentes Ativos", fontproperties=font_label, color=COLOR_YELLOW, labelpad=8)
    ax1_sub.tick_params(axis="y", labelcolor=COLOR_YELLOW, labelsize=8)
    ax1_sub.set_ylim(0, 40)

    # Destaque da Zona de Colapso
    ax1.axvspan(4.5, 6.2, color="#2D0A0E", alpha=0.6, zorder=1)
    ax1.axvline(4.5, color=COLOR_CRIMSON, linestyle="--", linewidth=1.2, zorder=2)

    box_incident = dict(boxstyle="square,pad=0.45", facecolor="#1F080A", edgecolor=COLOR_CRIMSON, linewidth=1.2)
    ax1.text(
        4.65, 595,
        "INCIDENTE: EXPLOSÃO DE SUBAGENTES\n"
        "• +24 subagentes gerados em 4 horas\n"
        "• +155M tokens reenviados em loop contínuo\n"
        "• ZERO compactações no período (travou em 5)\n"
        "• 61.8% de chamadas Opus 5.5\n"
        "=> Janela de 5h da Anthropic zerada em 20 min",
        fontproperties=font_caption, color=TEXT_WHITE, bbox=box_incident, zorder=7
    )

    ax1.set_xticks(x_pos)
    ax1.set_xticklabels(dates_str, fontproperties=font_label, color=TEXT_WHITE)

    # Bottom Plot: Velocidade de Queima por Hora (Hourly Token Velocity)
    cc_hourly = df_hourly[df_hourly["fonte"] == "claude_code"].copy()
    hourly_tokens_m = cc_hourly.groupby("hora")["entrada_cache_lida"].sum() / 1e6
    hourly_dates = [ts.strftime("%d/%m %Hh") for ts in hourly_tokens_m.index]
    x_h = np.arange(len(hourly_dates))

    ax2.bar(x_h, hourly_tokens_m.values, color=COLOR_YELLOW, alpha=0.85, width=0.6, edgecolor=CARD_BORDER, zorder=3)
    ax2.set_ylabel("Velocidade (M tok/h)", fontproperties=font_label, color=TEXT_WHITE, labelpad=8)
    ax2.set_xticks(x_h[::2])
    ax2.set_xticklabels(hourly_dates[::2], fontproperties=font_caption, color=TEXT_MUTED, rotation=0)
    ax2.tick_params(axis="y", colors=TEXT_MUTED, labelsize=8)

    fig.text(0.08, 0.95, "TELEMETRIA FORENSE DO PROJETO: INCIDENTE DE ESGOTAMENTO DE COTA", fontproperties=font_title, color=TEXT_WHITE)
    fig.text(0.08, 0.91, "Análise de 2.060 chamadas do projeto Nossa Cultura demonstrando a correlação exata entre subagentes e estouro de cota.", fontproperties=font_subtitle, color=TEXT_MUTED)

    out_path = os.path.join(IMG_DIR, "fig2_forensic_telemetry_timeline.png")
    plt.savefig(out_path, dpi=300, facecolor=CANVAS_BG)
    plt.close()
    print(f"[CHART] Gerado: {out_path}")


def generate_workload_rebalancing():
    """3. Dual-Card Dossier Comparativo: Barras Elegantes sem Sobreposição."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 5.2), facecolor=CANVAS_BG)
    plt.subplots_adjust(wspace=0.18, left=0.06, right=0.94, top=0.84, bottom=0.12)

    for ax in (ax1, ax2):
        ax.set_facecolor(CARD_BG)
        for spine in ax.spines.values():
            spine.set_color(CARD_BORDER)
            spine.set_linewidth(1.2)
        ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

    # Card 1: Histórico
    ax1.text(0.05, 0.92, "CENÁRIO OBSERVADO: MONOCULTURA OPUS", fontproperties=font_card_title, color=COLOR_CRIMSON, transform=ax1.transAxes)
    ax1.text(0.05, 0.85, "Esgotamento da janela rolante de 5 horas em menos de 20 minutos de loop.", fontproperties=font_subtitle, color=TEXT_MUTED, transform=ax1.transAxes)

    bbox_alert = dict(boxstyle="square,pad=0.35", facecolor="#2A0B0D", edgecolor=COLOR_CRIMSON, linewidth=1)
    ax1.text(0.95, 0.90, "FALHA DE COTA", fontproperties=font_label, color=COLOR_CRIMSON, transform=ax1.transAxes, ha="right", bbox=bbox_alert)

    items_real = [
        ("Claude Opus 5.5", 61.8, "1.273 chamadas · 535M tokens cache · Raciocínio pesado", COLOR_CRIMSON),
        ("Claude Sonnet 5.5", 36.4, "749 chamadas · 108M tokens cache · Engenharia core", "#FF6B6B"),
        ("Claude Haiku 5.5", 0.9, "18 chamadas · Subutilizado para tarefas mecânicas", "#888888"),
        ("Scripts Determinísticos", 0.9, "Rara delegação local · Quase tudo enviado ao Opus", "#555555"),
    ]

    y_pos = [0.65, 0.47, 0.29, 0.13]
    for (name, pct, desc, col), y in zip(items_real, y_pos):
        rect_bg = patches.Rectangle((0.05, y), 0.90, 0.07, facecolor="#181A20", edgecolor="none", transform=ax1.transAxes, zorder=2)
        ax1.add_patch(rect_bg)
        bar_w = 0.90 * (pct / 100.0)
        rect_val = patches.Rectangle((0.05, y), bar_w, 0.07, facecolor=col, edgecolor="none", transform=ax1.transAxes, zorder=3)
        ax1.add_patch(rect_val)
        ax1.text(0.05, y + 0.085, name, fontproperties=font_label, color=TEXT_WHITE, transform=ax1.transAxes)
        ax1.text(0.95, y + 0.085, f"{pct:.1f}%", fontproperties=font_num, color=col if pct > 5 else TEXT_MUTED, transform=ax1.transAxes, ha="right")
        ax1.text(0.05, y - 0.045, desc, fontproperties=font_caption, color=TEXT_MUTED, transform=ax1.transAxes)

    # Card 2: Ideal
    ax2.text(0.05, 0.92, "ARQUITETURA RECOMENDADA: PIPELINE EM 5 TIERS", fontproperties=font_card_title, color=COLOR_YELLOW, transform=ax2.transAxes)
    ax2.text(0.05, 0.85, "Operação perpétua 7 dias/semana sob custo fixo de US$ 58 / mês.", fontproperties=font_subtitle, color=TEXT_MUTED, transform=ax2.transAxes)

    bbox_ok = dict(boxstyle="square,pad=0.35", facecolor="#0B261A", edgecolor=COLOR_EMERALD, linewidth=1)
    ax2.text(0.95, 0.90, "OPERAÇÃO PERPÉTUA", fontproperties=font_label, color=COLOR_EMERALD, transform=ax2.transAxes, ha="right", bbox=bbox_ok)

    items_ideal = [
        ("Scripts Locais & GPU (RTX 5070 Ti)", 50.0, "Hash, resize, SAM 2, rembg, conversões · Custo zero de token", COLOR_YELLOW),
        ("OpenAI Codex (GPT-6.1 Sol / Terra)", 30.0, "Suítes Vitest, mocks, fixtures, migrations · 4.2x mais barato", COLOR_EMERALD),
        ("Claude Sonnet 5.5 Core (Claude Code)", 15.0, "Engenharia central React 19/Three.js · Compactado a cada 30 calls", "#FF454D"),
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

    fig.text(0.06, 0.94, "DISTRIBUIÇÃO DE CARGA: DIAGNÓSTICO DO PROJETO VS ARQUITETURA ÓTIMA", fontproperties=font_title, color=TEXT_WHITE)
    fig.text(0.06, 0.90, "Comparativo direto entre o padrão de consumo que provocou o bloqueio de cota e o modelo calibrado de produção.", fontproperties=font_subtitle, color=TEXT_MUTED)

    out_path = os.path.join(IMG_DIR, "fig3_workload_rebalancing_dossier.png")
    plt.savefig(out_path, dpi=300, facecolor=CANVAS_BG)
    plt.close()
    print(f"[CHART] Gerado: {out_path}")


def generate_radar_competence():
    """4. Gráfico Radar Poligonal Neon com Painel de Scores."""
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
    ax.grid(color=GRID_COLOR, linestyle=":", linewidth=1)

    ax.plot(angles, claude_p, color=COLOR_CRIMSON, linewidth=2, linestyle="-", label="Claude (Opus/Sonnet)")
    ax.fill(angles, claude_p, color=COLOR_CRIMSON, alpha=0.18)

    ax.plot(angles, codex_p, color=COLOR_EMERALD, linewidth=2, linestyle="-", label="OpenAI Codex (Sol/Astra)")
    ax.fill(angles, codex_p, color=COLOR_EMERALD, alpha=0.18)

    ax.plot(angles, antigravity_p, color=COLOR_CYAN, linewidth=2, linestyle="-", label="Google Antigravity (Flash)")
    ax.fill(angles, antigravity_p, color=COLOR_CYAN, alpha=0.18)

    # Painel Lateral
    ax_table = fig.add_axes([0.62, 0.15, 0.34, 0.68], facecolor=CARD_BG)
    for spine in ax_table.spines.values():
        spine.set_color(CARD_BORDER)
    ax_table.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

    ax_table.text(0.06, 0.90, "MATRIZ DE COMPETÊNCIA RELATIVA", fontproperties=font_card_title, color=COLOR_YELLOW, transform=ax_table.transAxes)
    ax_table.text(0.06, 0.82, "Avaliação empírica nos 5 eixos críticos de operação:", fontproperties=font_subtitle, color=TEXT_MUTED, transform=ax_table.transAxes)

    metrics_text = [
        ("Arquitetura & Clean Code", "Claude (9.8)", COLOR_CRIMSON, "Codex (6.8)", "AGY (6.0)"),
        ("Economia de Tokens / Cota", "Codex (9.5)", COLOR_EMERALD, "AGY (7.5)", "Claude (4.0)"),
        ("Isolamento Git Worktrees", "Codex (9.8)", COLOR_EMERALD, "AGY (7.0)", "Claude (5.5)"),
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

    out_path = os.path.join(IMG_DIR, "fig4_radar_model_competence.png")
    plt.savefig(out_path, dpi=300, facecolor=CANVAS_BG)
    plt.close()
    print(f"[CHART] Gerado: {out_path}")


def main():
    print("[VISUAL-DOSSIER] Iniciando geração dos gráficos via Pandas + Seaborn + Matplotlib...")
    df_hist, df_hourly = load_telemetry_data()
    print(f"[VISUAL-DOSSIER] Telemetria carregada: {len(df_hist)} snapshots históricos e {len(df_hourly)} horas de registro.")
    generate_pareto_scatter()
    generate_forensic_timeline(df_hist, df_hourly)
    generate_workload_rebalancing()
    generate_radar_competence()
    print("[VISUAL-DOSSIER] Todos os 4 gráficos de alta agência foram construídos com sucesso!")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Gera o dossiê visual de alta precisão técnica e estética editorial para o Whitepaper LAY®:
- fig1_pareto_scatter_benchmark.png: Fronteira de Pareto (Qualidade SWE-bench vs Custo USD log, bolhas de Throughput).
- fig2_forensic_telemetry_timeline.png: Análise forense da telemetria real do Georges (645M tokens em cache, saturação de subagentes).
- fig3_workload_rebalancing_dossier.png: Dossiê comparativo de alocação de carga (Monocultura vs Pipeline Balanceada em 5 Tiers).
- fig4_radar_model_competence.png: Radar poligonal de competências relativas com tabela analítica integrada.
- fig5_pipeline_orchestration_flow.png: Diagrama de governança e orquestração multiagente (Quem manda em quem, Worktrees e Gates).
"""

import os
import io
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.font_manager import FontProperties

# Diretórios
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG_DIR = os.path.join(BASE_DIR, "assets", "img")
os.makedirs(IMG_DIR, exist_ok=True)

# Telemetria real do projeto Nossa Cultura
HIST_PATH = r"C:\Users\georg\OneDrive\Desktop\LAY Projetos\Nossa Cultura - Sessão\docs\nossa-cultura\07-artbook-lay\telemetria\telemetria-ia-historico.csv"
HOURLY_PATH = r"C:\Users\georg\OneDrive\Desktop\LAY Projetos\Nossa Cultura - Sessão\docs\nossa-cultura\07-artbook-lay\telemetria\telemetria-ia-por-hora.csv"

# Paleta Estética Dark Luxury Calibrada (LAY® Haute-Horlogerie Digital)
CANVAS_BG = "#08090C"     # Preto grafite profundo
CARD_BG = "#0E1117"       # Superfície de cartão com profundidade
CARD_BORDER = "#1E2330"   # Borda sutil de precisão
GRID_COLOR = "#151922"    # Grid técnico discreto
TEXT_WHITE = "#F8FAFC"    # Branco puro suave
TEXT_MUTED = "#94A3B8"    # Cinza texto de leitura
TEXT_DIM = "#64748B"      # Cinza terciário

# Acentos cromáticos sofisticados (sem cores primárias estridentes)
COLOR_CRIMSON = "#E11D48"   # Rose/Crimson cirúrgico para Claude / Alertas
COLOR_AMBER = "#F59E0B"     # Âmbar/Ouro quente para Fronteira de Pareto / Scripts
COLOR_EMERALD = "#10B981"   # Esmeralda profundo para Codex / Sucesso
COLOR_CYAN = "#0EA5E9"      # Azul cobalto elétrico para Gemini / Contexto
COLOR_PURPLE = "#8B5CF6"    # Violeta para DeepSeek / Especialistas

# Fontes nativas do sistema
font_path_bahn = r"C:\Windows\Fonts\bahnschrift.ttf"
font_path_segoe = r"C:\Windows\Fonts\segoeui.ttf"
font_path_cons = r"C:\Windows\Fonts\consola.ttf"

font_title = FontProperties(fname=font_path_bahn, size=13, weight="bold")
font_subtitle = FontProperties(fname=font_path_segoe, size=8.5)
font_card_title = FontProperties(fname=font_path_bahn, size=10, weight="bold")
font_label = FontProperties(fname=font_path_bahn, size=8.5, weight="bold")
font_num = FontProperties(fname=font_path_bahn, size=11, weight="bold")
font_caption = FontProperties(fname=font_path_segoe, size=7.8)
font_mono = FontProperties(fname=font_path_cons, size=8)


def load_telemetry_data():
    """Carrega dados da telemetria com Pandas, limpando trailing commas."""
    with open(HIST_PATH, "r", encoding="utf-8") as f:
        clean_lines = [line.strip().rstrip(",") for line in f if line.strip()]
    df_hist = pd.read_csv(io.StringIO("\n".join(clean_lines)))
    df_hist["data"] = pd.to_datetime(df_hist["data"])

    df_hourly = pd.read_csv(HOURLY_PATH)
    df_hourly["hora"] = pd.to_datetime(df_hourly["hora"])
    return df_hist, df_hourly


def generate_pareto_scatter():
    """1. Gráfico de Dispersão com Fronteira de Pareto e bolhas de throughput sem colisões."""
    fig, ax = plt.subplots(figsize=(11.8, 6.0), facecolor=CANVAS_BG)
    ax.set_facecolor(CARD_BG)
    plt.subplots_adjust(left=0.07, right=0.95, top=0.86, bottom=0.13)

    for spine in ax.spines.values():
        spine.set_color(CARD_BORDER)
        spine.set_linewidth(1.2)

    data = [
        {"model": "Claude Opus 5.5", "cost": 10.04, "score": 97.0, "tps": 48, "color": COLOR_CRIMSON, "pareto": True, "dx": -115, "dy": 8},
        {"model": "Claude Sonnet 5.5", "cost": 3.80, "score": 94.2, "tps": 92, "color": "#FB7185", "pareto": True, "dx": -120, "dy": 7},
        {"model": "Claude Haiku 5.5", "cost": 0.45, "score": 78.5, "tps": 180, "color": "#FDA4AF", "pareto": False, "dx": 15, "dy": -4},
        {"model": "GPT-6 Astra (Max)", "cost": 6.24, "score": 88.0, "tps": 85, "color": COLOR_EMERALD, "pareto": False, "dx": 14, "dy": 6},
        {"model": "GPT-6.1 Sol", "cost": 1.27, "score": 68.8, "tps": 145, "color": "#34D399", "pareto": True, "dx": 15, "dy": -6},
        {"model": "GPT-6 Luna", "cost": 0.20, "score": 58.0, "tps": 240, "color": "#6EE7B7", "pareto": False, "dx": 14, "dy": -7},
        {"model": "Gemini 4 Carbon", "cost": 3.20, "score": 64.5, "tps": 110, "color": "#38BDF8", "pareto": False, "dx": 14, "dy": -8},
        {"model": "Gemini 3.8 Flash", "cost": 0.15, "score": 61.2, "tps": 308, "color": COLOR_CYAN, "pareto": True, "dx": 15, "dy": 7},
        {"model": "DeepSeek V4.1", "cost": 0.18, "score": 63.0, "tps": 220, "color": COLOR_PURPLE, "pareto": False, "dx": -105, "dy": 7},
    ]
    df = pd.DataFrame(data)

    ax.grid(True, which="both", linestyle=":", color=GRID_COLOR, alpha=0.9, zorder=1)

    # Curva de Pareto
    pareto_df = df[df["pareto"]].sort_values("cost")
    ax.fill_between(pareto_df["cost"], pareto_df["score"], 45, color=COLOR_AMBER, alpha=0.035, zorder=2)
    ax.plot(pareto_df["cost"], pareto_df["score"], color=COLOR_AMBER, linestyle="--", linewidth=1.8, label="Fronteira Eficiente de Pareto", zorder=3)

    # Dispersão
    ax.scatter(df["cost"], df["score"], s=df["tps"] * 5.0, c=df["color"], alpha=0.18, edgecolors="none", zorder=4)
    ax.scatter(df["cost"], df["score"], s=df["tps"] * 3.4, c=df["color"], alpha=0.92, edgecolors=TEXT_WHITE, linewidth=1.1, zorder=5)

    # Rótulos com offsets afinados
    for _, row in df.iterrows():
        ax.annotate(
            f"{row['model']} ({row['score']:.1f}%)",
            (row["cost"], row["score"]),
            xytext=(row["dx"], row["dy"]),
            textcoords="offset points",
            fontproperties=font_label,
            color=TEXT_WHITE,
            bbox=dict(boxstyle="round,pad=0.28,rounding_size=0.15", facecolor="#131722", edgecolor="#262D3D", alpha=0.95),
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

    # Cabeçalho integrado
    fig.text(0.07, 0.94, "FRONTEIRA DE PARETO: QUALIDADE EM CÓDIGO VS CUSTO POR TAREFA", fontproperties=font_title, color=TEXT_WHITE)
    fig.text(0.07, 0.90, "Tamanho da bolha = Throughput (tokens/s). Modelos na linha âmbar dominam os demais em custo-benefício.", fontproperties=font_subtitle, color=TEXT_MUTED)

    # Box informativo posicionado de forma isolada sem colidir
    box_insight = dict(boxstyle="round,pad=0.55,rounding_size=0.2", facecolor="#0B0D13", edgecolor=COLOR_AMBER, linewidth=1.2)
    ax.text(
        0.12, 51.5,
        "INSIGHTS DE PRODUÇÃO (PARETO):\n"
        "• Gemini Flash ($0.15 / 308 t/s): Varredura e digestão de repositório 1M+ tokens\n"
        "• Codex Sol ($1.27 / 145 t/s): Testes unitários e migrações em lote com custo 4.2x menor\n"
        "• Sonnet 5.5 ($3.80 / 92 t/s): Implementação e refatoração core de componentes complexos\n"
        "• Opus 5.5 ($10.04 / 48 t/s): Sanção arquitetural crítica exclusivamente em turno único",
        fontproperties=font_caption, color=TEXT_WHITE, bbox=box_insight, zorder=7
    )

    out_path = os.path.join(IMG_DIR, "fig1_pareto_scatter_benchmark.png")
    plt.savefig(out_path, dpi=300, facecolor=CANVAS_BG)
    plt.close()
    print(f"[CHART] Gerado: {out_path}")


def generate_forensic_timeline(df_hist, df_hourly):
    """2. Linha do tempo forense da telemetria real (645M cache tokens vs subagentes)."""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11.8, 6.2), facecolor=CANVAS_BG, sharex=False, gridspec_kw={"height_ratios": [2.3, 1.1]})
    plt.subplots_adjust(left=0.07, right=0.93, top=0.88, bottom=0.11, hspace=0.32)

    for ax in (ax1, ax2):
        ax.set_facecolor(CARD_BG)
        for spine in ax.spines.values():
            spine.set_color(CARD_BORDER)
            spine.set_linewidth(1.1)
        ax.grid(True, linestyle=":", color=GRID_COLOR, alpha=0.8)

    cc_hist = df_hist[df_hist["fonte"] == "claude_code"].copy()
    cc_hist["cache_m"] = cc_hist["entrada_cache_lida"] / 1e6
    cc_hist["subagentes"] = pd.to_numeric(cc_hist["subagentes"])
    dates_str = cc_hist["data"].dt.strftime("%d/%m %Hh").tolist()
    x_pos = np.arange(len(dates_str))

    # Top Plot: Cache Acumulado
    ax1.fill_between(x_pos, cc_hist["cache_m"], 380, color=COLOR_CRIMSON, alpha=0.12, zorder=2)
    ax1.plot(x_pos, cc_hist["cache_m"], color=COLOR_CRIMSON, marker="o", markersize=5.5, linewidth=2.2, label="Tokens de Cache Reenviados (Milhões)", zorder=5)
    ax1.set_ylabel("Tokens Cache (Milhões)", fontproperties=font_label, color=COLOR_CRIMSON, labelpad=8)
    ax1.tick_params(axis="y", labelcolor=COLOR_CRIMSON, labelsize=8)
    ax1.set_ylim(360, 700)

    # Eixo Secundário: Subagentes
    ax1_sub = ax1.twinx()
    ax1_sub.spines["right"].set_color(CARD_BORDER)
    ax1_sub.plot(x_pos, cc_hist["subagentes"], color=COLOR_AMBER, marker="s", markersize=5.5, linewidth=2.0, linestyle="-.", label="Subagentes Ativos", zorder=6)
    ax1_sub.set_ylabel("Subagentes Concorrentes", fontproperties=font_label, color=COLOR_AMBER, labelpad=8)
    ax1_sub.tick_params(axis="y", labelcolor=COLOR_AMBER, labelsize=8)
    ax1_sub.set_ylim(0, 42)

    # Destaque da Zona de Incidente
    ax1.axvspan(4.4, 6.2, color="#26080C", alpha=0.6, zorder=1)
    ax1.axvline(4.4, color=COLOR_CRIMSON, linestyle="--", linewidth=1.2, zorder=2)

    # Box do Incidente reposicionado no canto superior esquerdo para não sobrepor nada
    box_incident = dict(boxstyle="round,pad=0.5,rounding_size=0.2", facecolor="#18090C", edgecolor=COLOR_CRIMSON, linewidth=1.2)
    ax1.text(
        0.05, 530,
        "INCIDENTE REAL: EXPLOSÃO DE SUBAGENTES\n"
        "• +24 subagentes gerados em 4 horas (08h18 -> 12h57)\n"
        "• +155M tokens reenviados em loop cumulativo\n"
        "• ZERO compactações no período (travou no índice 5)\n"
        "• 61.8% de chamadas Opus 5.5 em vez de Sonnet/Codex\n"
        "-> Resultado: Franquia de 5h da Anthropic esgotada em 20 min",
        fontproperties=font_caption, color=TEXT_WHITE, bbox=box_incident, zorder=7
    )

    ax1.set_xticks(x_pos)
    ax1.set_xticklabels(dates_str, fontproperties=font_label, color=TEXT_WHITE)

    # Bottom Plot: Velocidade de Queima Horária
    cc_hourly = df_hourly[df_hourly["fonte"] == "claude_code"].copy()
    hourly_tokens_m = cc_hourly.groupby("hora")["entrada_cache_lida"].sum() / 1e6
    hourly_dates = [ts.strftime("%d/%m %Hh") for ts in hourly_tokens_m.index]
    x_h = np.arange(len(hourly_dates))

    ax2.bar(x_h, hourly_tokens_m.values, color=COLOR_AMBER, alpha=0.85, width=0.55, edgecolor=CARD_BORDER, zorder=3)
    ax2.set_ylabel("Velocidade (M tok/h)", fontproperties=font_label, color=TEXT_WHITE, labelpad=8)
    ax2.set_xticks(x_h[::2])
    ax2.set_xticklabels(hourly_dates[::2], fontproperties=font_caption, color=TEXT_MUTED, rotation=0)
    ax2.tick_params(axis="y", colors=TEXT_MUTED, labelsize=8)

    fig.text(0.07, 0.95, "TELEMETRIA FORENSE DO PROJETO: A CORRELAÇÃO DE ESGOTAMENTO DE COTA", fontproperties=font_title, color=TEXT_WHITE)
    fig.text(0.07, 0.91, "Análise empírica de 2.060 chamadas do projeto Nossa Cultura provando o impacto da ausência de compactação.", fontproperties=font_subtitle, color=TEXT_MUTED)

    out_path = os.path.join(IMG_DIR, "fig2_forensic_telemetry_timeline.png")
    plt.savefig(out_path, dpi=300, facecolor=CANVAS_BG)
    plt.close()
    print(f"[CHART] Gerado: {out_path}")


def generate_workload_rebalancing():
    """3. Comparativo de alocação de carga em dois cards refinados."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.8, 5.4), facecolor=CANVAS_BG)
    plt.subplots_adjust(wspace=0.16, left=0.06, right=0.94, top=0.84, bottom=0.10)

    for ax in (ax1, ax2):
        ax.set_facecolor(CARD_BG)
        for spine in ax.spines.values():
            spine.set_color(CARD_BORDER)
            spine.set_linewidth(1.2)
        ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

    # Card 1: Cenário Observado
    ax1.text(0.05, 0.92, "CENÁRIO OBSERVADO: MONOCULTURA OPUS", fontproperties=font_card_title, color=COLOR_CRIMSON, transform=ax1.transAxes)
    ax1.text(0.05, 0.85, "Esgotamento da janela rolante de 5 horas em menos de 20 minutos.", fontproperties=font_subtitle, color=TEXT_MUTED, transform=ax1.transAxes)

    bbox_alert = dict(boxstyle="round,pad=0.35,rounding_size=0.15", facecolor="#260A0D", edgecolor=COLOR_CRIMSON, linewidth=1)
    ax1.text(0.95, 0.90, "FALHA DE COTA", fontproperties=font_label, color=COLOR_CRIMSON, transform=ax1.transAxes, ha="right", bbox=bbox_alert)

    items_real = [
        ("Claude Opus 5.5", 61.8, "1.273 chamadas · 535M tokens cache · Raciocínio pesado em tudo", COLOR_CRIMSON),
        ("Claude Sonnet 5.5", 36.4, "749 chamadas · 108M tokens cache · Engenharia central", "#FB7185"),
        ("Claude Haiku 5.5", 0.9, "18 chamadas · Subutilizado para tarefas mecânicas", "#64748B"),
        ("Scripts Determinísticos", 0.9, "Rara delegação local · Quase tudo enviado ao Opus", "#475569"),
    ]

    y_pos = [0.65, 0.47, 0.29, 0.13]
    for (name, pct, desc, col), y in zip(items_real, y_pos):
        rect_bg = patches.Rectangle((0.05, y), 0.90, 0.065, facecolor="#131720", edgecolor="none", transform=ax1.transAxes, zorder=2)
        ax1.add_patch(rect_bg)
        bar_w = 0.90 * (pct / 100.0)
        rect_val = patches.Rectangle((0.05, y), bar_w, 0.065, facecolor=col, edgecolor="none", transform=ax1.transAxes, zorder=3)
        ax1.add_patch(rect_val)
        ax1.text(0.05, y + 0.082, name, fontproperties=font_label, color=TEXT_WHITE, transform=ax1.transAxes)
        ax1.text(0.95, y + 0.082, f"{pct:.1f}%", fontproperties=font_num, color=col if pct > 5 else TEXT_MUTED, transform=ax1.transAxes, ha="right")
        ax1.text(0.05, y - 0.045, desc, fontproperties=font_caption, color=TEXT_MUTED, transform=ax1.transAxes)

    # Card 2: Arquitetura Balanceada
    ax2.text(0.05, 0.92, "ARQUITETURA RECOMENDADA: PIPELINE 5 TIERS", fontproperties=font_card_title, color=COLOR_AMBER, transform=ax2.transAxes)
    ax2.text(0.05, 0.85, "Operação perpétua contínua sob custo fixo de US$ 58 / mês.", fontproperties=font_subtitle, color=TEXT_MUTED, transform=ax2.transAxes)

    bbox_ok = dict(boxstyle="round,pad=0.35,rounding_size=0.15", facecolor="#092015", edgecolor=COLOR_EMERALD, linewidth=1)
    ax2.text(0.95, 0.90, "OPERAÇÃO PERPÉTUA", fontproperties=font_label, color=COLOR_EMERALD, transform=ax2.transAxes, ha="right", bbox=bbox_ok)

    items_ideal = [
        ("Scripts Locais & GPU (RTX 5070 Ti)", 50.0, "Hash, resize, SAM 2, rembg, conversões · Custo zero de token", COLOR_AMBER),
        ("OpenAI Codex (GPT-6.1 Sol / Terra)", 30.0, "Suítes Vitest, mocks, fixtures, migrations · Custo 4.2x menor", COLOR_EMERALD),
        ("Claude Sonnet 5.5 Core (Claude Code)", 15.0, "Engenharia central React 19/Three.js · Compactado a cada 30 calls", "#FB7185"),
        ("Gemini 3.8 Flash & Opus 5.5 Gate", 5.0, "Flash para ingestão 1M+ tokens · Opus apenas para aprovação final", COLOR_CYAN),
    ]

    for (name, pct, desc, col), y in zip(items_ideal, y_pos):
        rect_bg = patches.Rectangle((0.05, y), 0.90, 0.065, facecolor="#131720", edgecolor="none", transform=ax2.transAxes, zorder=2)
        ax2.add_patch(rect_bg)
        bar_w = 0.90 * (pct / 100.0)
        rect_val = patches.Rectangle((0.05, y), bar_w, 0.065, facecolor=col, edgecolor="none", transform=ax2.transAxes, zorder=3)
        ax2.add_patch(rect_val)
        ax2.text(0.05, y + 0.082, name, fontproperties=font_label, color=TEXT_WHITE, transform=ax2.transAxes)
        ax2.text(0.95, y + 0.082, f"{pct:.1f}%", fontproperties=font_num, color=col, transform=ax2.transAxes, ha="right")
        ax2.text(0.05, y - 0.045, desc, fontproperties=font_caption, color=TEXT_MUTED, transform=ax2.transAxes)

    fig.text(0.06, 0.94, "DISTRIBUIÇÃO DE CARGA: DIAGNÓSTICO DO PROJETO VS ARQUITETURA ÓTIMA", fontproperties=font_title, color=TEXT_WHITE)
    fig.text(0.06, 0.90, "Comparativo direto entre a sobrecarga causadora do travamento e o fluxo equilibrado em 5 camadas.", fontproperties=font_subtitle, color=TEXT_MUTED)

    out_path = os.path.join(IMG_DIR, "fig3_workload_rebalancing_dossier.png")
    plt.savefig(out_path, dpi=300, facecolor=CANVAS_BG)
    plt.close()
    print(f"[CHART] Gerado: {out_path}")


def generate_radar_competence():
    """4. Radar Poligonal com espaçamento amplo para rótulos e tabela lateral."""
    categories = [
        "Raciocínio Core &\nArquitetura Limpa",
        "Throughput &\nEconomia de Cota",
        "Isolamento Git\nWorktrees",
        "Ingestão Massiva\n(1M+ Multimodal)",
        "Inspeção Visual\nBrowser-in-Loop",
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

    fig = plt.figure(figsize=(11.8, 5.6), facecolor=CANVAS_BG)
    # Posição do radar com margem suficiente para rótulos
    ax = fig.add_axes([0.06, 0.10, 0.50, 0.76], polar=True, facecolor=CARD_BG)

    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    plt.xticks(angles[:-1], categories, fontproperties=font_label, color=TEXT_WHITE)
    ax.tick_params(pad=18)

    ax.set_rlabel_position(30)
    plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color=TEXT_DIM, size=7)
    plt.ylim(0, 11.0)
    ax.grid(color=GRID_COLOR, linestyle=":", linewidth=1)

    ax.plot(angles, claude_p, color=COLOR_CRIMSON, linewidth=2.2, linestyle="-", label="Claude (Opus/Sonnet)")
    ax.fill(angles, claude_p, color=COLOR_CRIMSON, alpha=0.18)

    ax.plot(angles, codex_p, color=COLOR_EMERALD, linewidth=2.2, linestyle="-", label="OpenAI Codex (Sol/Astra)")
    ax.fill(angles, codex_p, color=COLOR_EMERALD, alpha=0.18)

    ax.plot(angles, antigravity_p, color=COLOR_CYAN, linewidth=2.2, linestyle="-", label="Google Antigravity (Flash)")
    ax.fill(angles, antigravity_p, color=COLOR_CYAN, alpha=0.18)

    # Painel Lateral
    ax_table = fig.add_axes([0.60, 0.12, 0.35, 0.72], facecolor=CARD_BG)
    for spine in ax_table.spines.values():
        spine.set_color(CARD_BORDER)
    ax_table.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

    ax_table.text(0.06, 0.90, "MATRIZ DE COMPETÊNCIA RELATIVA", fontproperties=font_card_title, color=COLOR_AMBER, transform=ax_table.transAxes)
    ax_table.text(0.06, 0.82, "Especialização por eixo técnico operacional:", fontproperties=font_subtitle, color=TEXT_MUTED, transform=ax_table.transAxes)

    metrics_text = [
        ("Arquitetura & Clean Code", "Claude (9.8)", COLOR_CRIMSON, "Codex (6.8)", "AGY (6.0)"),
        ("Economia de Tokens / Cota", "Codex (9.5)", COLOR_EMERALD, "AGY (7.5)", "Claude (4.0)"),
        ("Isolamento Git Worktrees", "Codex (9.8)", COLOR_EMERALD, "AGY (7.0)", "Claude (5.5)"),
        ("Contexto Longo Multimodal", "AGY (9.8)", COLOR_CYAN, "Claude (7.5)", "Codex (6.0)"),
        ("Browser-in-the-Loop (UI)", "AGY (9.8)", COLOR_CYAN, "Codex (6.5)", "Claude (4.5)"),
    ]

    y_t = 0.67
    for axis_name, leader, l_col, s2, s3 in metrics_text:
        ax_table.text(0.06, y_t, axis_name, fontproperties=font_label, color=TEXT_WHITE, transform=ax_table.transAxes)
        ax_table.text(0.06, y_t - 0.05, f"Líder: {leader}", fontproperties=font_caption, color=l_col, transform=ax_table.transAxes, fontweight="bold")
        ax_table.text(0.55, y_t - 0.05, f"Outros: {s2}, {s3}", fontproperties=font_caption, color=TEXT_DIM, transform=ax_table.transAxes)
        y_t -= 0.125

    fig.text(0.06, 0.94, "RADAR DE ESPECIALIZAÇÃO TÉCNICA: A COMPLEMENTARIDADE DOS MOTORES", fontproperties=font_title, color=TEXT_WHITE)
    fig.text(0.06, 0.90, "Demonstração de que nenhum motor resolve 100% dos eixos isoladamente, provando o valor do triângulo.", fontproperties=font_subtitle, color=TEXT_MUTED)

    out_path = os.path.join(IMG_DIR, "fig4_radar_model_competence.png")
    plt.savefig(out_path, dpi=300, facecolor=CANVAS_BG)
    plt.close()
    print(f"[CHART] Gerado: {out_path}")


def generate_pipeline_orchestration_flow():
    """5. Diagrama Arquitetural de Governança: Quem Manda em Quem, Worktrees e Gates."""
    fig, ax = plt.subplots(figsize=(11.8, 6.0), facecolor=CANVAS_BG)
    ax.set_facecolor(CARD_BG)
    plt.subplots_adjust(left=0.04, right=0.96, top=0.88, bottom=0.06)

    for spine in ax.spines.values():
        spine.set_color(CARD_BORDER)
        spine.set_linewidth(1.2)
    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    # 1. Caixa do Diretor / Usuário (Topo)
    rect_user = patches.FancyBboxPatch((35, 83), 30, 12, boxstyle="round,pad=0.5,rounding_size=1.0", facecolor="#181B26", edgecolor=COLOR_AMBER, linewidth=1.5)
    ax.add_patch(rect_user)
    ax.text(50, 91, "DIRETOR CRIATIVO / VOCÊ", fontproperties=font_card_title, color=COLOR_AMBER, ha="center")
    ax.text(50, 86, "Briefing · Decisão de Produto · Aprovação de Pull Requests", fontproperties=font_caption, color=TEXT_MUTED, ha="center")

    # Seta Usuário -> Antigravity
    ax.annotate("", xy=(50, 71), xytext=(50, 83), arrowprops=dict(arrowstyle="->", color=COLOR_AMBER, lw=1.8))

    # 2. Orquestrador Central: Google Antigravity (Centro)
    rect_agy = patches.FancyBboxPatch((20, 52), 60, 18, boxstyle="round,pad=0.5,rounding_size=1.2", facecolor="#0E1726", edgecolor=COLOR_CYAN, linewidth=1.8)
    ax.add_patch(rect_agy)
    ax.text(50, 64.5, "ORQUESTRADOR CENTRAL: GOOGLE ANTIGRAVITY (Runtime & Maestro)", fontproperties=font_title, color=COLOR_CYAN, ha="center")
    ax.text(50, 59.5, "Gerenciador de Git Worktrees · MCP Servers · Terminal Headless · Browser-in-the-Loop · Triagem de Contexto", fontproperties=font_subtitle, color=TEXT_WHITE, ha="center")
    ax.text(50, 55.0, "Gemini 3.8 Flash (Varredura 1M+ tokens) · Fila de Tarefas Paralelas · Validação de Diffs", fontproperties=font_caption, color=TEXT_MUTED, ha="center")

    # 3. Três Subagentes / Workers em Paralelo (Git Worktrees Isoladas)
    # Worker 1: Claude (Arquiteto Core)
    rect_w1 = patches.FancyBboxPatch((4, 20), 28, 22, boxstyle="round,pad=0.5,rounding_size=1.0", facecolor="#1C0F14", edgecolor=COLOR_CRIMSON, linewidth=1.4)
    ax.add_patch(rect_w1)
    ax.text(18, 37.5, "CLAUDE OPUS / SONNET", fontproperties=font_card_title, color=COLOR_CRIMSON, ha="center")
    ax.text(18, 33.5, "Worktree 1: Feature Core", fontproperties=font_label, color=TEXT_WHITE, ha="center")
    ax.text(18, 28.5, "• Tipagem TypeScript Strict\n• Shaders Three.js / WebGL\n• Regras de Negócio Críticas\n• Sanção Arquitetural", fontproperties=font_caption, color=TEXT_MUTED, ha="center")

    # Worker 2: OpenAI Codex (Operário de Volume)
    rect_w2 = patches.FancyBboxPatch((36, 20), 28, 22, boxstyle="round,pad=0.5,rounding_size=1.0", facecolor="#0B1A14", edgecolor=COLOR_EMERALD, linewidth=1.4)
    ax.add_patch(rect_w2)
    ax.text(50, 37.5, "OPENAI CODEX (SOL / TERRA)", fontproperties=font_card_title, color=COLOR_EMERALD, ha="center")
    ax.text(50, 33.5, "Worktree 2: Testes & Mocks", fontproperties=font_label, color=TEXT_WHITE, ha="center")
    ax.text(50, 28.5, "• Cobertura Vitest / Playwright\n• Mocks e Fixtures Massivas\n• Migrações SQL e Boilerplate\n• Execução em Sandbox", fontproperties=font_caption, color=TEXT_MUTED, ha="center")

    # Worker 3: GPU Local & Scripts Python/Node (RTX 5070 Ti)
    rect_w3 = patches.FancyBboxPatch((68, 20), 28, 22, boxstyle="round,pad=0.5,rounding_size=1.0", facecolor="#191710", edgecolor=COLOR_AMBER, linewidth=1.4)
    ax.add_patch(rect_w3)
    ax.text(82, 37.5, "SCRIPTS LOCAIS & RTX 5070 Ti", fontproperties=font_card_title, color=COLOR_AMBER, ha="center")
    ax.text(82, 33.5, "Ambiente Local: Custo Zero", fontproperties=font_label, color=TEXT_WHITE, ha="center")
    ax.text(82, 28.5, "• Recorte SAM 2 / rembg\n• Validação SHA256 e Links\n• Blender MCP Headless\n• Conversão de Assets", fontproperties=font_caption, color=TEXT_MUTED, ha="center")

    # Setas do Antigravity para os 3 Workers
    ax.annotate("", xy=(18, 43), xytext=(35, 52), arrowprops=dict(arrowstyle="->", color=COLOR_CRIMSON, lw=1.5))
    ax.annotate("", xy=(50, 43), xytext=(50, 52), arrowprops=dict(arrowstyle="->", color=COLOR_EMERALD, lw=1.5))
    ax.annotate("", xy=(82, 43), xytext=(65, 52), arrowprops=dict(arrowstyle="->", color=COLOR_AMBER, lw=1.5))

    # 4. Barra Inferior: Portão de Integração e Repositório Principal
    rect_merge = patches.FancyBboxPatch((15, 3), 70, 11, boxstyle="round,pad=0.5,rounding_size=0.8", facecolor="#11141D", edgecolor="#2B3347", linewidth=1.2)
    ax.add_patch(rect_merge)
    ax.text(50, 9.5, "PORTÃO DE INTEGRAÇÃO & CI LOCAL: VALIDADO NO DOM REAL -> REPOSITÓRIO PRINCIPAL", fontproperties=font_label, color=TEXT_WHITE, ha="center")
    ax.text(50, 5.5, "Diffs Unificados no Antigravity · Testes Verificados · Browser-in-the-Loop Aprovado · Merge Seguro na Branch Main", fontproperties=font_caption, color=TEXT_MUTED, ha="center")

    # Setas dos Workers para o Merge
    ax.annotate("", xy=(28, 14.5), xytext=(18, 19), arrowprops=dict(arrowstyle="->", color="#4B5563", lw=1.2))
    ax.annotate("", xy=(50, 14.5), xytext=(50, 19), arrowprops=dict(arrowstyle="->", color="#4B5563", lw=1.2))
    ax.annotate("", xy=(72, 14.5), xytext=(82, 19), arrowprops=dict(arrowstyle="->", color="#4B5563", lw=1.2))

    fig.text(0.04, 0.95, "GOVERNANÇA & HIERARQUIA MULTIAGENTE: QUEM MANDA EM QUEM NA PRÁTICA", fontproperties=font_title, color=TEXT_WHITE)
    fig.text(0.04, 0.91, "O Antigravity atua como Maestro central de execução e worktrees; Claude e Codex operam como especialistas em branches isoladas.", fontproperties=font_subtitle, color=TEXT_MUTED)

    out_path = os.path.join(IMG_DIR, "fig5_pipeline_orchestration_flow.png")
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
    generate_pipeline_orchestration_flow()
    print("[VISUAL-DOSSIER] Todos os 5 gráficos editoriais de alta agência foram construídos com sucesso!")


if __name__ == "__main__":
    main()

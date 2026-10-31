#!/usr/bin/env python3
"""Gera os gráficos de alta resolução para o relatório estratégico LAY:
1. Gráfico de Dispersão (Scatter Plot / Bubble Chart) com Fronteira de Pareto.
2. Análise Forense da Telemetria Real do Georges (Explosão de Tokens vs Subagentes).
3. Comparativo de Alocação de Carga (Monocultura Opus vs Pipeline Balanceado).
4. Gráfico Radar de Capacidades das 3 Plataformas.
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Diretórios
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG_DIR = os.path.join(BASE_DIR, "assets", "img")
os.makedirs(IMG_DIR, exist_ok=True)

# Paleta Editorial LAY
BG_COLOR = "#0E0E0E"
TEXT_COLOR = "#FAF5E9"
ACCENT_RED = "#E31B23"
ACCENT_YELLOW = "#FFF201"
ACCENT_CYAN = "#00FFFF"
ACCENT_GREEN = "#10A37F"
ACCENT_GRAY = "#888888"
CARD_BG = "#1A1A1A"
GRID_COLOR = "#2A2A2A"

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["text.color"] = TEXT_COLOR
plt.rcParams["axes.labelcolor"] = TEXT_COLOR
plt.rcParams["xtick.color"] = TEXT_COLOR
plt.rcParams["ytick.color"] = TEXT_COLOR


def generate_scatter_pareto():
    """1. Gráfico de Dispersão: Qualidade (SWE-bench / Intelligence) vs Custo/Consumo de Cota."""
    fig, ax = plt.subplots(figsize=(10, 6), facecolor=BG_COLOR)
    ax.set_facecolor(CARD_BG)

    # Dados dos modelos: (Nome, Custo por tarefa USD, Score SWE-bench/Código %, Throughput tok/s, Família)
    models = [
        ("Claude Opus 5.5 (Max)", 10.04, 97.0, 48, "#E31B23"),
        ("Claude Sonnet 5.5", 3.80, 94.2, 92, "#FF6B6B"),
        ("Claude Haiku 5.5", 0.45, 78.5, 180, "#FFA8A8"),
        ("GPT-6 Astra (Max)", 6.24, 88.0, 85, "#10A37F"),
        ("GPT-6.1 Sol (Terra)", 1.27, 68.8, 145, "#4ECCA3"),
        ("GPT-6 Luna", 0.20, 58.0, 240, "#A8E6CF"),
        ("Gemini 4 Carbon", 3.20, 64.5, 110, "#00BCE4"),
        ("Gemini 3.8 Flash", 0.15, 61.2, 308, "#00FFFF"),
        ("DeepSeek V4.1 Flash", 0.18, 63.0, 220, "#9B5DE5"),
    ]

    names = [m[0] for m in models]
    x_costs = [m[1] for m in models]
    y_scores = [m[2] for m in models]
    sizes = [m[3] * 4 for m in models]
    colors = [m[4] for m in models]

    # Scatter plot
    scatter = ax.scatter(x_costs, y_scores, s=sizes, c=colors, alpha=0.85, edgecolors="#FAF5E9", linewidth=1.5, zorder=5)

    # Rótulos dos modelos
    offsets = {
        "Claude Opus 5.5 (Max)": (-15, -18),
        "Claude Sonnet 5.5": (-20, 12),
        "Claude Haiku 5.5": (12, -8),
        "GPT-6 Astra (Max)": (12, -5),
        "GPT-6.1 Sol (Terra)": (14, -5),
        "GPT-6 Luna": (12, -10),
        "Gemini 4 Carbon": (12, -10),
        "Gemini 3.8 Flash": (12, 5),
        "DeepSeek V4.1 Flash": (-25, 12),
    }

    for name, x, y in zip(names, x_costs, y_scores):
        dx, dy = offsets.get(name, (10, 0))
        ax.annotate(
            name,
            (x, y),
            xytext=(dx, dy),
            textcoords="offset points",
            fontsize=8.5,
            fontweight="bold",
            color="#FAF5E9",
            bbox=dict(boxstyle="round,pad=0.2", facecolor="#111111", edgecolor="#333333", alpha=0.85),
            zorder=6,
        )

    # Curva da Fronteira de Pareto: Flash -> Sol -> Sonnet -> Opus
    pareto_x = [0.15, 1.27, 3.80, 10.04]
    pareto_y = [61.2, 68.8, 94.2, 97.0]
    ax.plot(pareto_x, pareto_y, color=ACCENT_YELLOW, linestyle="--", linewidth=2, label="Fronteira Eficiente de Pareto", zorder=4)

    # Área de destaque: Zona Ideal de Trabalho
    ax.fill_between(pareto_x, pareto_y, 50, color=ACCENT_YELLOW, alpha=0.06, zorder=2)

    ax.set_title("FRONTEIRA DE PARETO: QUALIDADE EM CÓDIGO VS CUSTO POR TAREFA", fontsize=12, fontweight="bold", pad=15, color=ACCENT_YELLOW)
    ax.set_xlabel("Custo Observado por Tarefa Complexa (USD - Escala Logarítmica)", fontsize=9.5, labelpad=10)
    ax.set_ylabel("Qualidade / Resolução de Repositório (SWE-bench Verified %)", fontsize=9.5, labelpad=10)
    ax.set_xscale("log")
    ax.set_xlim(0.10, 16.0)
    ax.set_ylim(50, 103)
    ax.grid(True, which="both", linestyle=":", color=GRID_COLOR, alpha=0.7)

    # Legenda explicativa
    ax.text(
        0.12,
        96,
        "Tamanho da bolha = Throughput (tokens/s)\nModelos na linha amarela formam o mix de ouro:\nGemini Flash (Carga) -> Codex Sol (Volume) -> Sonnet/Opus (Core)",
        fontsize=8,
        bbox=dict(boxstyle="square,pad=0.6", facecolor="#0E0E0E", edgecolor=ACCENT_YELLOW, alpha=0.9),
    )

    ax.legend(loc="lower right", facecolor="#111111", edgecolor="#444444", fontsize=8.5)
    plt.tight_layout()
    out_path = os.path.join(IMG_DIR, "scatter_pareto_llm.png")
    plt.savefig(out_path, dpi=300, facecolor=BG_COLOR)
    plt.close()
    print(f"[CHART] Gerado: {out_path}")


def generate_forensic_telemetry():
    """2. Gráfico Forense da Telemetria Real do Georges: O Colapso das 5 Horas."""
    fig, ax1 = plt.subplots(figsize=(10, 5.5), facecolor=BG_COLOR)
    ax1.set_facecolor(CARD_BG)

    # Timestamps reais de telemetria-ia-historico.csv
    dates = [
        "30/10 18h",
        "30/10 21h",
        "30/10 23h",
        "31/10 02h",
        "31/10 07h",
        "31/10 08h",
        "31/10 12h",
    ]
    x_indices = np.arange(len(dates))

    # Métricas reais de Claude Code
    cache_read_m = [428.1, 442.3, 480.3, 488.6, 490.2, 506.5, 645.3]  # Milhões de tokens
    subagents = [9, 9, 9, 9, 9, 11, 33]  # Subagentes disparados
    calls = [826, 900, 1014, 1062, 1074, 1179, 2060]  # Chamadas acumuladas
    compactations = [2, 3, 4, 4, 5, 5, 5]  # Compactações acumuladas

    # Eixo 1: Tokens de Cache Lidos (Área / Linha Vermelha)
    color_cache = ACCENT_RED
    ax1.set_xlabel("Linha do Tempo das Sessões do Projeto (30/10 a 31/10/2026)", fontsize=9.5, labelpad=10)
    ax1.set_ylabel("Tokens de Cache Reenviados (Milhões de Tokens)", color=color_cache, fontsize=9.5, labelpad=10)
    line1 = ax1.plot(x_indices, cache_read_m, color=color_cache, marker="o", linewidth=2.5, label="Tokens de Cache Lidos (M)")
    ax1.fill_between(x_indices, cache_read_m, 400, color=color_cache, alpha=0.15)
    ax1.tick_params(axis="y", labelcolor=color_cache)
    ax1.set_ylim(350, 700)

    # Eixo 2: Subagentes Concorrentes (Linha Amarela)
    ax2 = ax1.twinx()
    color_sub = ACCENT_YELLOW
    ax2.set_ylabel("Subagentes Concorrentes Criados", color=color_sub, fontsize=9.5, labelpad=10)
    line2 = ax2.plot(x_indices, subagents, color=color_sub, marker="s", linewidth=2.5, linestyle="-.", label="Subagentes Ativos")
    ax2.tick_params(axis="y", labelcolor=color_sub)
    ax2.set_ylim(0, 40)

    ax1.set_xticks(x_indices)
    ax1.set_xticklabels(dates, fontsize=8.5)
    ax1.grid(True, linestyle=":", color=GRID_COLOR, alpha=0.7)

    # Destaque da Zona do Colapso
    ax1.axvspan(4.5, 6.2, color=ACCENT_RED, alpha=0.22, zorder=1)
    ax1.text(
        4.6,
        610,
        "ZONA DO COLAPSO (08h às 12h)\n• +24 subagentes criados em 4 horas\n• +155M tokens reenviados em loop\n• ZERO compactações (travou em 5)\n=> Cota de 5h esgotada em 20 min!",
        fontsize=8,
        color="#FFFFFF",
        bbox=dict(boxstyle="square,pad=0.5", facecolor="#B00000", edgecolor=ACCENT_YELLOW, alpha=0.9),
    )

    plt.title("ANÁLISE FORENSE DO PROJETO DO GEORGES: A CAUSA DO TRAVAMENTO DO CLAUDE", fontsize=11, fontweight="bold", pad=15, color=ACCENT_RED)
    plt.tight_layout()
    out_path = os.path.join(IMG_DIR, "forensic_telemetry_georges.png")
    plt.savefig(out_path, dpi=300, facecolor=BG_COLOR)
    plt.close()
    print(f"[CHART] Gerado: {out_path}")


def generate_allocation_comparison():
    """3. Comparativo de Alocação de Trabalho: Como Estava vs Como Deve Ser."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5), facecolor=BG_COLOR)

    # Cores
    c_opus = "#E31B23"
    c_sonnet = "#FF6B6B"
    c_codex = "#10A37F"
    c_flash = "#00FFFF"
    c_scripts = "#FFF201"

    # Gráfico 1: Como o Georges Operou
    labels1 = ["Claude Opus 5.5\n(61.8%)", "Claude Sonnet 5.5\n(36.4%)", "Haiku\n(0.9%)", "Scripts / Codex\n(0.9%)"]
    sizes1 = [61.8, 36.4, 0.9, 0.9]
    colors1 = [c_opus, c_sonnet, "#FFA8A8", c_scripts]

    wedges1, texts1, autotexts1 = ax1.pie(
        sizes1,
        labels=labels1,
        autopct="%1.1f%%",
        startangle=140,
        colors=colors1,
        textprops=dict(color="#FAF5E9", fontsize=8),
        wedgeprops=dict(edgecolor=BG_COLOR, width=0.6),
    )
    for at in autotexts1:
        at.set_fontsize(7.5)
        at.set_color("#000000")
        at.set_weight("bold")
    ax1.set_title("COMO O PROJETO OPEROU\n(Monocultura Opus -> Quebra em 20 min)", fontsize=9.5, fontweight="bold", color=ACCENT_RED, pad=12)

    # Gráfico 2: Alocação Estratégica Balanceada
    labels2 = ["Scripts Locais\n(50%)", "Codex / Sol\n(30%)", "Sonnet 5.5 Core\n(15%)", "Flash & Opus Gate\n(5%)"]
    sizes2 = [50, 30, 15, 5]
    colors2 = [c_scripts, c_codex, c_sonnet, c_flash]

    wedges2, texts2, autotexts2 = ax2.pie(
        sizes2,
        labels=labels2,
        autopct="%1.1f%%",
        startangle=140,
        colors=colors2,
        textprops=dict(color="#FAF5E9", fontsize=8),
        wedgeprops=dict(edgecolor=BG_COLOR, width=0.6),
    )
    for at in autotexts2:
        at.set_fontsize(7.5)
        at.set_color("#000000")
        at.set_weight("bold")
    ax2.set_title("ALOCAÇÃO RECOMENDADA\n(Multi-Agente Balanceado -> Custo Fixo $58)", fontsize=9.5, fontweight="bold", color=ACCENT_YELLOW, pad=12)

    plt.tight_layout()
    out_path = os.path.join(IMG_DIR, "allocation_comparison.png")
    plt.savefig(out_path, dpi=300, facecolor=BG_COLOR)
    plt.close()
    print(f"[CHART] Gerado: {out_path}")


def generate_radar_capabilities():
    """4. Gráfico Radar: Especialização Comparativa entre Claude, Codex e Antigravity."""
    categories = [
        "Arquitetura &\nRaciocínio Limpo",
        "Volume Braçal &\nEconomia de Cota",
        "Isolamento Worktrees\nParalelas",
        "Mega-Contexto &\nMultimodalidade",
        "Browser Visual &\nInspeção de UI",
    ]
    N = len(categories)

    # Valores (escala 1 a 10)
    claude_vals = [9.8, 4.0, 5.5, 7.5, 4.5]
    codex_vals = [6.8, 9.5, 9.8, 6.0, 6.5]
    antigravity_vals = [6.0, 7.5, 7.0, 9.8, 9.8]

    # Repete o primeiro valor para fechar o polígono
    claude_vals += claude_vals[:1]
    codex_vals += codex_vals[:1]
    antigravity_vals += antigravity_vals[:1]

    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(7.5, 6), subplot_kw=dict(polar=True), facecolor=BG_COLOR)
    ax.set_facecolor(CARD_BG)

    # Ajusta ângulo do início
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)

    # Rótulos dos eixos
    plt.xticks(angles[:-1], categories, color="#FAF5E9", size=8.5, fontweight="bold")

    # Linhas radiais
    ax.set_rlabel_position(0)
    plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="#666666", size=7)
    plt.ylim(0, 10.5)

    # Plota polígonos
    ax.plot(angles, claude_vals, linewidth=2, linestyle="solid", color="#E31B23", label="Claude (Opus/Sonnet)")
    ax.fill(angles, claude_vals, color="#E31B23", alpha=0.2)

    ax.plot(angles, codex_vals, linewidth=2, linestyle="solid", color="#10A37F", label="OpenAI Codex (Sol/Astra)")
    ax.fill(angles, codex_vals, color="#10A37F", alpha=0.2)

    ax.plot(angles, antigravity_vals, linewidth=2, linestyle="solid", color="#00FFFF", label="Google Antigravity (Flash)")
    ax.fill(angles, antigravity_vals, color="#00FFFF", alpha=0.2)

    plt.title("RADAR DE ESPECIALIZAÇÃO: ONDE CADA FERRAMENTA BRILHA", size=11, color=ACCENT_YELLOW, weight="bold", pad=20)
    plt.legend(loc="upper right", bbox_to_anchor=(1.25, 1.1), facecolor="#111111", edgecolor="#444444", fontsize=8)

    plt.tight_layout()
    out_path = os.path.join(IMG_DIR, "radar_capabilities.png")
    plt.savefig(out_path, dpi=300, facecolor=BG_COLOR)
    plt.close()
    print(f"[CHART] Gerado: {out_path}")


def main():
    print("[CHARTS] Iniciando geração dos gráficos estatísticos e forenses...")
    generate_scatter_pareto()
    generate_forensic_telemetry()
    generate_allocation_comparison()
    generate_radar_capabilities()
    print("[CHARTS] Todos os 4 gráficos gerados com sucesso em assets/img/")


if __name__ == "__main__":
    main()

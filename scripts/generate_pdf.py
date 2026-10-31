#!/usr/bin/env python3
"""Compila o relatório HTML v2 em PDF de alta resolução usando Chrome ou Edge headless."""
import os
import subprocess
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML_PATH = os.path.join(BASE_DIR, "report", "report-template-v2.html")
PDF_PATH = os.path.join(BASE_DIR, "report", "Relatorio-Estrategico-Orquestracao-Multi-Agente-IA.pdf")

CHROME_PATHS = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]


def find_browser():
    for p in CHROME_PATHS:
        if os.path.exists(p):
            return p
    return None


def main():
    browser = find_browser()
    if not browser:
        print("Erro: Nenhum navegador Chromium (Chrome ou Edge) encontrado no sistema.", file=sys.stderr)
        sys.exit(1)

    print(f"[PDF-COMPILER] Navegador detectado: {browser}")
    print(f"[PDF-COMPILER] Lendo HTML: {HTML_PATH}")
    print(f"[PDF-COMPILER] Gerando PDF: {PDF_PATH}")

    cmd = [
        browser,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={PDF_PATH}",
        HTML_PATH,
    ]

    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(PDF_PATH) and os.path.getsize(PDF_PATH) > 1000:
        size_kb = os.path.getsize(PDF_PATH) / 1024
        print(f"[PDF-COMPILER] Sucesso! PDF gerado: {size_kb:.1f} KB")
    else:
        print("[PDF-COMPILER] Falha na compilação do PDF:", res.stderr, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

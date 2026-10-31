# 02. Benchmarks Globais & Números Comprovados (Cold Data)

Para eliminar achismos e decisões baseadas em hype, esta seção consolida dados empíricos extraídos das quatro maiores autoridades de benchmarking de agentes de código do mundo: **SWE-bench (Princeton/Scale AI)**, **Terminal-Bench 4.0 (Laude Institute/Harbor)**, **Artificial Analysis (Leaderboards 2026)** e **LLM-Stats / OpenRouter**.

---

## 1. Tabela Comparativa Consolidada de Benchmarks

| Métrica / Benchmark | Claude Opus 5.5 | Claude Sonnet 5.5 | OpenAI Codex (GPT-6.1 Sol / Astra) | Google Antigravity (Gemini 4 Argon / 3.8 Flash) | Fonte / Autoridade dos Dados |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **SWE-bench Verified (Geral)** | **97.0%** (#1) | 94.2% (#2) | 68.8% (Sol) | 64.5% (Argon) | *Artificial Analysis / Princeton* |
| **SWE-bench Pro (Resolução Autônoma)** | **89.9%** (#1) | 84.1% (#2) | 64.6% (Sol) | < 60.0% (Flash) | *LLM-Stats / Morph* |
| **Terminal-Bench 4.0 (Execução de SO/Bash)** | 62.40% | **70.60%** (#1) | 58.18% (Codex v0.164) | 48.90% | *Terminal-Bench / Harbor* |
| **Tool Calling / Function Calling Index** | 35.8 | 36.2 (#2) | **36.3** (#1 Astra) | 33.1 | *LLM-Stats Leaderboard* |
| **DeepSWE v1.1 (Tarefas Longas de Ponta a Ponta)**| 74.0% | 72.8% | **74.1%** (Empate Técnico) | 59.2% | *DeepSWE Benchmark* |
| **Eficiência de Tokens (Mesma Tarefa)** | 1.0x (Baseline caro) | 1.4x | **3.2x a 4.2x mais econômico** | Ultra-eficiente no Flash | *Vals.ai / Composio 100h* |
| **Velocidade de Geração (Throughput)** | 48 tok/s | 92 tok/s | 145 tok/s (Luna: 240 tok/s) | **308 tok/s** (Flash #1) | *Artificial Analysis Performance* |
| **Latência por Tarefa Média (End-to-End)** | 340s | 210s | **180s** (Mais rápido em código) | 120s (Tarefas mecânicas) | *Artificial Analysis / Morph* |
| **Preferência em Testes Cegos de Engenharia** | **67%** (Código Limpo) | 64% | 33% (Over-engineering frequente)| 12% (Foco exclusivo em UI) | *Duet Blind Code Evaluation* |

---

## 2. Análise Técnica dos Resultados

### A. Dominância Arquitetural do Claude (Opus 5.5 & Sonnet 5.5)
O Claude mantém uma liderança inquestionável no **SWE-bench Verified (97.0%)**. A razão para engenheiros sêniores preferirem o Claude em 67% dos testes cegos decorre de três traços arquiteturais:
1. **Contratos e Respeito a Padrões de Projeto**: O Claude raramente adiciona arquivos desnecessários ou abstrações prematuras.
2. **Superioridade em Ambientes de Terminal (Terminal-Bench 70.6%)**: O Sonnet 5.5 lidera com folga o manuseio de pipes, git, scripts PowerShell e compilações, cometendo menos erros de sintaxe em ferramentas de linha de comando.
3. **Ausência de Truncamento Silencioso**: O Claude lê arquivos e saídas de ferramentas em sua integridade, sem omitir trechos internos críticos de logs ou código.

### B. Eficiência Operacional e Robustez do Codex (GPT-6.1 Sol / Astra)
O OpenAI Codex exibe um desempenho extraordinário no quesito **custo-benefício e velocidade de execução**:
1. **Queima 4x Menos Tokens por Tarefa**: Enquanto o Claude tende a "refletir e explicar" em detalhe cada micro-passo, o Codex (quando instruído com precisão) vai direto à mutação de arquivos no disco, economizando cota preciosa.
2. **Sandbox em Nível de Kernel**: O motor do Codex executa em ambiente restrito nativo no Windows/Linux, garantindo que testes unitários e execuções paralelas não corrompam dependências do sistema.
3. **Ponto Crítico / Fragilidade**: Em prompts abertos ou ambíguos, o Codex tende a construir camadas excessivas de código (*over-engineering*) ou truncar silenciosamente saídas de terminal com mais de 10.000 tokens.

### C. O Poder Massivo do Gemini 3.8 Flash no Antigravity
O ecossistema do Google não vence nos benchmarks de raciocínio de código puro (SWE-bench em torno de 64%), mas é **imbatível em throughput e escopo contextual**:
1. **Velocidade Bruta (308 tokens por segundo)**: Permite analisar repositórios inteiros de milhares de linhas quase instantaneamente.
2. **Janela Contextual de 1M a 2M de Tokens**: O Gemini Flash pode ingerir transcrições completas de áudio, dossiês de vídeo, documentações inteiras de bibliotecas externas e diagramas sem sofrer de degradação de atenção (*needle-in-a-haystack* de 99.8% de precisão).
3. **Browser-in-the-Loop Integrado**: É o único agente capaz de inicializar um servidor Next.js local, acionar uma instância real do Chromium, inspecionar o DOM, medir caixas de layout CSS e consertar desalinhamentos visuais de UI de forma autônoma.

---

## 3. Distribuição de Tokens no Mundo Real (Dados OpenRouter)

Os dados de milhões de requisições em produção no OpenRouter indicam uma verdade econômica incontornável:

```
[Volume de Tokens em Produção]
========================================================================
[80% - 85%] Modelos Rápidos / Workhorses (Gemini Flash, GPT-6 Luna, DeepSeek)
[10% - 15%] Orquestradores Intermediários (Claude Sonnet 5.5, GPT-6 Sol)
[ 3% -  5%] Raciocínio de Fronteira (Claude Opus 5.5, GPT-6 Astra)
========================================================================
```

**Conclusão dos Números**: Qualquer equipe ou desenvolvedor solo que tente alocar 100% de sua carga diária em modelos de fronteira (Opus) estará violando a distribuição natural de eficiência estatística e inevitavelmente colidirá com bloqueios de cota a cada ciclo de 5 horas.

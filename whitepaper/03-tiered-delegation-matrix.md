# 03. Matriz de Delegação Estratégica em 5 Níveis (Tiering Matrix)

Para eliminar o desperdício de cota sem comprometer a qualidade do código entregue, o sistema adota uma segmentação rígida de tarefas em 5 Tiers operacionais, balanceando **Dificuldade Cognitiva**, **Consumo de Tokens** e **Custo de Latência**.

---

## 1. Visão Geral da Pirâmide de Execução

```
                    ▲
                   / \
      TIER 1      /   \      Claude Opus 5.5 (Single-Turn Gate)
                 /     \     [Raciocínio Puro, Shaders, Arquitetura]
                /───────\
    TIER 2     /         \    Claude Sonnet 5.5 (Claude Code)
              /           \   [Engenharia Core, React, Three.js, GSAP]
             /─────────────\
   TIER 3   /               \  OpenAI Codex (GPT-6.1 Sol / Terra)
           /                 \ [Testes Unitários, Boilerplate, Migrations, Mocks]
          /───────────────────\
  TIER 4 /                     \ Google Gemini 3.8 Flash (Antigravity CLI)
        /                       \[Ingestão Massiva, Regex, Inventários, Multimodal]
       /─────────────────────────\
TIER 5/                           \ Local RTX 5070 Ti + Browser-in-the-Loop
     /─────────────────────────────\[ComfyUI, SAM 2, Rembg, DOM Pixel Inspection]
```

---

## 2. Detalhamento por Tier Operacional

### TIER 1: Raciocínio Profundo & Arbitragem Arquitetural (Critical Reasoning)
* **Modelo Responsável**: **Claude Opus 5.5** (Anthropic).
* **Nível de Dificuldade**: Máximo (Cognição de Fronteira).
* **Taxa de Queima de Cota**: Altíssima (1 chamada de Opus consome o equivalente a 4-5 chamadas de Sonnet).
* **Escopo de Atuação**:
  * Definição de contratos de tipagem globais e arquitetura de pastas.
  * Formulação de shaders GLSL matemáticos complexos (Three.js/R3F).
  * Red-teaming de lógica de segurança, autorização e consistência transacional.
  * Veredito final de aprovação de Rodadas (Gates de Aceite).
* **Regra de Ouro**: **Chamada em Turno Único (Single-Turn)**. O Opus jamais lê arquivos pelo terminal em loop interativo; ele recebe o diff consolidado com o prompt de auditoria e responde com a aprovação ou lista de ajustes.

---

### TIER 2: Engenharia Central & Implementação de Código (Core Engineering)
* **Modelo Responsável**: **Claude Sonnet 5.5** (Claude Code CLI / Desktop).
* **Nível de Dificuldade**: Alto a Médio-Alto.
* **Taxa de Queima de Cota**: Balanceada (Ótimo ponto de equilíbrio entre raciocínio e throughput).
* **Escopo de Atuação**:
  * Escrita de componentes React 19 / Next.js 16 em TypeScript strict.
  * Implementação de animações GSAP sincronizadas com Lenis Scroll e Three.js.
  * Refatoração estrutural de múltiplos arquivos conectados.
  * Resolução de bugs complexos identificados em relatórios de erro.
* **Regra de Ouro**: **Compactação a cada 30 tool calls** via `/compact` e encerramento de sessão ao concluir a feature.

---

### TIER 3: Volume de Código, Testes & Boilerplate (High-Volume Generation)
* **Modelo Responsável**: **OpenAI Codex CLI (`codex exec`)** com **GPT-6.1 Sol / Terra**.
* **Nível de Dificuldade**: Médio a Baixo-Médio.
* **Taxa de Queima de Cota**: Extremamente Econômica (4x mais eficiente que Claude; franquia farta no ChatGPT Plus).
* **Escopo de Atuação**:
  * Geração completa de suítes de testes unitários (Vitest / Jest / Playwright).
  * Criação de dados de mock, fixtures, seeders de banco de dados e esquemas de validação Zod.
  * Conversão de interfaces legadas e migrações SQL/Prisma/Drizzle.
  * Revisão cruzada de código procurando *null-pointers* e regressões de tipagem.
* **Regra de Ouro**: Execução não-interativa em Git Worktrees separadas com `--ask-for-approval never`.

---

### TIER 4: Contexto Gigante, Extração & Rotinas Mecânicas (Mass Context Ingestion)
* **Modelo Responsável**: **Google Gemini 3.8 Flash** (Google Antigravity CLI `agy`).
* **Nível de Dificuldade**: Baixo (Tarefas mecânicas de alta velocidade).
* **Taxa de Queima de Cota**: Custo irrisório / Quase zero contra limites de mensagens.
* **Escopo de Atuação**:
  * Ingestão de repositórios gigantes (milhares de arquivos de uma só vez).
  * Mapeamento de grafos de dependência e indexação de arquivos via Graphify.
  * Análise de dossiês de áudio, stems musicais e extração de metadados de vídeo.
  * Renomeação em lote, buscas regex pesadas e organização de diretórios.
* **Regra de Ouro**: O Gemini Flash digere gigabytes de informação e cospe um **JSON ou Markdown enxuto (2k tokens)** para consumo imediato do Sonnet.

---

### TIER 5: Validação Visual em Navegador & Computação Local na GPU
* **Modelo Responsável**: **Google Antigravity 2.0 (Browser Agent)** + **RTX 5070 Ti Local (16GB VRAM)**.
* **Nível de Dificuldade**: Físico / Sensorial / Pixel-Perfect.
* **Taxa de Queima de Cota**: Zero (Processamento local na GPU) ou cota visual nativa do Antigravity.
* **Escopo de Atuação**:
  * **Browser-in-the-Loop**: O Antigravity abre o Chromium, renderiza a página a 375px (mobile) e 1920px (desktop), detecta botões sobrepostos e reporta anomalias visuais.
  * **Recorte de Sprites & Assets**: Execução de scripts locais com `rembg` e **SAM 2 (Segment Anything 2)** para extração pixel-perfect com canal Alpha limpo.
  * **Renderização 3D Offline**: Automação de cenas no Blender 5.2.3 LTS via **Blender MCP**.
* **Regra de Ouro**: **Nunca delegar recorte de imagem para LLMs de nuvem**. Modelos de difusão de nuvem alucinam bordas e destroem traços vetoriais; a RTX 5070 Ti local resolve com precisão determinística.

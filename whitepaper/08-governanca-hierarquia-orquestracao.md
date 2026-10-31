# 08. Governança, Hierarquia de Comando e Orquestração Multiagente na Prática

> **Autoridade Técnica:** Loud, Angry & Young® (LAY®)  
> **Status:** Especificação de Engenharia & Padrão de Produção  
> **Data de Atualização:** 31 de Outubro de 2026  

---

## 1. A Cadeia de Comando: Quem Manda em Quem?

Em sistemas autônomos multiagente, o caos surge quando modelos de diferentes capacidades tentam liderar simultaneamente a mesma árvore de arquivos. Para garantir previsibilidade, aderência arquitetural e custo zero de retrabalho, o ecossistema estabelece uma **hierarquia estrita e unidirecional de governança**:

```
                                    ┌────────────────────────┐
                                    │    DIRETOR CRIATIVO    │
                                    │      (Você / Dev)      │
                                    └───────────┬────────────┘
                                                │ Define escopo e aprova PRs
                                                ▼
                                    ┌────────────────────────┐
                                    │  ORQUESTRADOR CENTRAL  │
                                    │   Google Antigravity   │
                                    │   (Runtime & Maestro)  │
                                    └───────────┬────────────┘
                                                │
                 ┌──────────────────────────────┼──────────────────────────────┐
                 │ Distribui Worktree 1         │ Distribui Worktree 2         │ Aciona Scripts
                 ▼                              ▼                              ▼
      ┌────────────────────┐         ┌────────────────────┐         ┌────────────────────┐
      │  ENGENHEIRO CORE   │         │ OPERÁRIO DE VOLUME │         │ EXECUÇÃO MECÂNICA  │
      │  Claude Sonnet 5.5 │         │  OpenAI Codex Sol  │         │ Scripts & RTX 5070 │
      │  (Arquiteto Chefe) │         │  (Testes e Mocks)  │         │ (Custo Zero Token) │
      └──────────┬─────────┘         └──────────┬─────────┘         └──────────┬─────────┘
                 │                              │                              │
                 └──────────────────────────────┼──────────────────────────────┘
                                                │ Diffs unificados e testes verdes
                                                ▼
                                    ┌────────────────────────┐
                                    │   PORTÃO DE SANÇÃO     │
                                    │   Claude Opus 5.5      │
                                    │  (Single-Turn Gate)    │
                                    └───────────┬────────────┘
                                                │ Aprovação final
                                                ▼
                                    ┌────────────────────────┐
                                    │ REPOSITÓRIO PRINCIPAL  │
                                    │      (Branch Main)     │
                                    └────────────────────────┘
```

---

### 1.1. Papéis e Responsabilidades Estritas

| Nível Hierárquico | Componente / Modelo | Autoridade Máxima | O Que PODE Fazer | O Que NÃO PODE Fazer |
| :--- | :--- | :--- | :--- | :--- |
| **Nível 0: Direção** | **Usuário (Dev / Criativo)** | Soberania de Produto | Definir requisitos, priorizar sprints, revisar artefatos visuais, aprovar merge final. | Escrever código repetitivo à mão ou gastar horas em depuração mecânica. |
| **Nível 1: Maestro** | **Google Antigravity** | Soberania de Runtime | Gerenciar Git Worktrees, acionar MCP servers, executar terminal headless, inspecionar DOM real via Chromium, balancear filas de tarefas. | Alterar decisões de arquitetura core sem aprovação do Arquiteto. |
| **Nível 2: Arquiteto** | **Claude Sonnet 5.5** | Soberania de Código Core | Escrever componentes complexos, refatorar regras de negócio, manter contratos de tipos, otimizar shaders Three.js/WebGL. | Ficar preso em loops gerando 50 mocks de teste ou lendo logs gigantescos de terminal. |
| **Nível 3: Operário** | **OpenAI Codex (Sol)** | Soberania de Suíte de Testes | Gerar testes unitários Vitest, mocks, fixtures, scripts de migração SQL, boilerplate em massa, executar testes até o verde. | Mudar a arquitetura do componente ou remover testes existentes para forçar aprovação. |
| **Nível 4: Scanner** | **Gemini 3.8 Flash** | Soberania de Ingestão | Ler diretórios inteiros (1M+ tokens), construir grafos de dependência, fazer triagem de contexto, escanear CVEs e conformidade de assets. | Tomar decisões de refatoração profunda de código crítico. |
| **Nível 5: Máquina** | **Scripts Python/RTX 5070 Ti** | Soberania Determinística | Recortes de imagem (SAM 2/rembg), automação Blender MCP, hash SHA256, checagem de links e formatação Prettier/ESLint. | Consumir qualquer token de IA para cálculos ou transformações matemáticas puras. |

---

## 2. Gestão de Tarefas por Tiers (A Matriz Operacional em 5 Níveis)

Toda tarefa enviada ao sistema é classificada deterministicamente em um dos 5 Tiers antes de qualquer arquivo ser tocado:

### **Tier 0: Determinístico & Aceleração Local (Custo $0.00)**
- **Critério**: Tarefa possui algoritmo exato sem ambiguidade.
- **Exemplos**: Conversão de imagens PNG para WebP, corte por transparência, geração de hashes, validação de URLs, linting, formatação de código.
- **Executor**: Python 3.14 local + NVIDIA GeForce RTX 5070 Ti (CUDA/OptiX).
- **Consumo de Tokens de IA**: **Zero**.

### **Tier 1: Mega-Contexto & Triagem (Custo ~$0.15 / tarefa)**
- **Critério**: Ingestão bruta de volume maior que 100.000 tokens ou varredura de diretórios inteiros.
- **Exemplos**: Análise de documentações de 500 páginas, leitura completa da pasta `src/` para gerar grafo de dependências, diagnóstico de erros em dumps de logs de 50.000 linhas.
- **Executor**: Google Gemini 3.8 Flash via Antigravity / `agy`.
- **Throughput**: ~308 tokens por segundo.

### **Tier 2: Suítes de Testes & Boilerplate em Massa (Custo ~$1.27 / tarefa)**
- **Critério**: Geração de código de suporte volumoso, repetitivo e verificável por asserções binárias.
- **Exemplos**: Criação de 40 testes unitários Vitest, mocks para API do Three.js, scripts de seed de banco de dados, DTOs e esquemas Zod.
- **Executor**: OpenAI Codex (GPT-6.1 Sol / Terra) via sandbox CLI (`codex exec`).
- **Comportamento**: Execução autônoma em loop restrito de arquivos (*run-until-green*).

### **Tier 3: Engenharia Central & Refatoração (Custo ~$3.80 / tarefa)**
- **Critério**: Raciocínio multi-arquivo, abstração de componentes React 19, shaders WebGL complexos, sincronização de scroll GSAP e integridade de tipos.
- **Exemplos**: Construção da transição do tubarão em Three.js, refatoração de gerenciamento de estado complexo, arquitetura de componentes compostos.
- **Executor**: Claude Sonnet 5.5 via Claude Code ou Antigravity.
- **Protocolo de Segurança**: Compactação forçada de contexto a cada 30 turns.

### **Tier 4: Sanção Arquitetural Crítica (Custo ~$10.04 / decisão)**
- **Critério**: Decisão estrutural irreversível, auditoria de segurança de alto risco ou aprovação final de release candidate antes do deploy.
- **Exemplos**: Revisão de segurança de autenticação, validação de shaders de produção para evitar vazamento de memória GPU, sanção de PRs complexos.
- **Executor**: Claude Opus 5.5 (Modo Thinking).
- **Regra Inegociável**: **Exclusivamente em turno único (Single-Turn)**. Proibido colocar Opus em loop interativo.

---

## 3. Isolamento por Git Worktrees: Operação Paralela Sem Conflitos

O segredo para rodar múltiplos agentes simultaneamente sem corromper o repositório é o **Git Worktrees**:

```powershell
# Criação de worktrees isoladas a partir da branch principal
git worktree add ../worktree-core-feature -b feat/culture-core
git worktree add ../worktree-test-suite -b test/culture-vitest

# Agente Claude Sonnet trabalha em worktree-core-feature
claude -p "Implement core shader logic" --dir ../worktree-core-feature

# Em paralelo, Agente Codex trabalha em worktree-test-suite
codex exec --cd ../worktree-test-suite "Create Vitest mocks"

# Após conclusão, o Antigravity unifica e valida no DOM real
git merge test/culture-vitest
git merge feat/culture-core
```

Cada agente possui seu próprio diretório de trabalho físico e seu próprio histórico atômico do Git. Conflitos de edição concorrente são reduzidos a zero.

---

## 4. O Circuito de Segurança (Circuit Breaker Anti-Crash)

Para impedir repetições do incidente documentado na telemetria (onde o Claude Code consumiu a cota de 5 horas em menos de 20 minutos):

1. **Limitador de Subagentes Concorrentes**: O Orquestrador bloqueia o spawn de novos subagentes quando houver mais de 3 instâncias ativas simultâneas.
2. **Monitor de Cache Cumulativo**: Se a soma de tokens lidos em cache ultrapassar 40 milhões em uma única sessão sem uma compactação intermediária, a sessão é pausada e uma rotina de resumo (`/compact`) é injetada compulsoriamente.
3. **Escalonamento por Falhas**: Se um agente falhar em resolver um bug após 3 tentativas consecutivas, o loop é interrompido imediatamente e o relatório de erro é escalado para o nível superior, evitando queima inútil de tokens.

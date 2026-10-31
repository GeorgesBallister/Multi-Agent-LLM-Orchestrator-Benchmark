# 04. Análise Comparativa de Desktop Apps & Harnesses (Workflow Sem IDE)

Para desenvolvedores, designers e diretores criativos que **não querem escrever código manualmente em uma IDE tradicional** e operam puramente como diretores/arquitetos (apenas pensando, revisando e direcionando a IA), a escolha da janela de trabalho gráfica (o *Harness*) é decisiva.

---

## 1. O Triângulo de Aplicativos Desktop Nativos no Windows

```
┌────────────────────────────────────────────────────────────────────────┐
│                          PAINEL DE CONTROLE                            │
├─────────────────────┬──────────────────────────┬───────────────────────┤
│  Claude Desktop App │    Codex Desktop App     │  Antigravity 2.0 App  │
│    (Anthropic)      │         (OpenAI)         │       (Google)        │
├─────────────────────┼──────────────────────────┼───────────────────────┤
│ • Melhor Cérebro    │ • Melhor Mission Control │ • Olhos & Navegador   │
│ • Sem truncamento   │ • Git Worktrees visuais  │ • Browser-in-the-loop │
│ • 1 milhão de tokens│ • Sandbox no kernel      │ • Multimodal nativo   │
│ • Sem filas visuais │ • Trunca logs grandes    │ • Perde estado longo  │
└─────────────────────┴──────────────────────────┴───────────────────────┘
```

---

## 2. Diagnóstico Detalhado por Aplicativo

### A. OpenAI Codex Desktop App (O Melhor Painel Visual de Múltiplas Filas)
O Codex Desktop App foi desenhado especificamente para o paradigma de **gerenciamento de filas assíncronas**. Não é um chat conversacional comum; assemelha-se a um painel de centro de comando (*Mission Control*).

* **Pontos Fortes**:
  1. **Git Worktrees Nativas com 1 Clique**: Você pode despachar 4 tarefas em paralelo (ex.: "criar testes para o módulo A", "gerar mocks para o módulo B", "refatorar estilos CSS do módulo C"). O app cria automaticamente branches isoladas no disco, roda os agentes sem conflitos de merge e exibe os diffs lado a lado para aprovação humana com um clique.
  2. **Sandbox no Kernel do Windows**: Não requer WSL nem contêineres Docker pesados. Roda em sandbox seguro do sistema operacional via PowerShell nativo.
  3. **Visual Feedback Browser**: Possui um navegador interno onde você pode apontar o mouse na tela da sua aplicação, deixar uma anotação em um elemento visual e o agente altera o código correspondente.
* **Ponto Fraco Fatal**:
  * **Truncamento Silencioso**: Quando uma ferramenta MCP ou comando de terminal retorna saídas muito extensas (>10k tokens), o Codex trunca o meio da mensagem (`[...truncated...]`), perdendo detalhes arquiteturais silenciosamente.

---

### B. Claude Desktop App (Aba Code) — O Cérebro Incomparável
O Claude Desktop (versão v2.1.300+) unificou três modos: **Chat**, **Cowork** (manipulação de arquivos locais e navegador) e **Code** (o Claude Code rodando em interface gráfica sem necessidade de Node.js instalado).

* **Pontos Fortes**:
  1. **Integridade de Raciocínio (Zero Truncamento)**: O Claude é a única ferramenta do mercado que garante leitura 100% integral de arquivos imensos e logs de sistema, sem cortes arbitrários.
  2. **Sistema de Hooks Cirúrgicos**: Permite interceptar tool calls através de hooks (`PreToolUse`, `PostToolUse`, `PreCompact`) configurados no `settings.json`, impedindo ações destrutivas no disco.
  3. **Auto-Memory e Persistência**: Mantém notas contextuais entre sessões sem poluir o histórico de conversação ativo.
* **Pontos Fracos na GUI**:
  1. **Sessão Única Linear**: Não possui interface visual nativa para disparar 5 branches em Git Worktrees concorrentes em abas separadas na tela.
  2. **Ausência de Trava Automática de Subagentes**: Se o usuário permitir que o Claude abra *Agent Teams* livremente, o app instancia múltiplos subprocessos e consome a franquia do plano Pro em poucos minutos.

---

### C. Google Antigravity 2.0 Desktop (O Especialista Visual com "Olhos")
O Antigravity 2.0 Desktop converteu o ambiente clássico em um **Parallel Agent Manager** com suporte multimodal nativo.

* **Pontos Fortes**:
  1. **Browser-in-the-Loop Real**: Enquanto o usuário formula o próximo prompt, o agente do Antigravity inicializa o servidor de desenvolvimento, abre uma janela do Chromium, testa cliques, formulários e renderização de canvas WebGL, capturando screenshots automáticos.
  2. **Ingestão Direta de Assets Multimodais**: Permite arrastar pastas de áudios (stems), folhas de sprites e vídeos de referência para dentro do painel, interpretando tudo em um único prompt de 1M de tokens.
* **Pontos Fracos**:
  1. **Degradação em Raciocínio Profundo**: Em refatorações arquiteturais extensas (acima de 10 arquivos interdependentes), o modelo nativo tende a esquecer imports ou criar inconsistências contratuais de tipagem.

---

## 3. As Ferramentas Open-Source da Comunidade (Kanban de Agentes)

Para os desenvolvedores do Reddit que rejeitam IDEs e não querem alternar manualmente entre 3 janelas separadas no Windows, duas soluções *open-source (licença MIT)* destacam-se:

### 1. **Nimbalyst**
* **Conceito**: Um painel visual em formato Kanban feito especificamente para orquestrar agentes do Claude Code e OpenAI Codex na mesma tela.
* **Funcionamento**: Permite criar cartões de tarefas. Você arrasta o cartão para a coluna "Em Execução" e seleciona se a tarefa roda no Claude ou no Codex. O Nimbalyst instancia o Git Worktree em segundo plano, executa o CLI correspondente via headless e exibe os diffs prontos para merge na coluna "Revisão".

### 2. **Superset**
* **Conceito**: Interface leve em Rust/Tauri que expõe uma barra lateral unificada para terminais de agentes autônomos.
* **Destaque**: Possui medidor visual de consumo de cota em tempo real para Anthropic e OpenAI, pausando automaticamente novos subagentes quando a cota atinge 80% do limite da janela rolante.

---

## 4. O Veredito de Setup para o Georges

Para manter o fluxo mais fluido, sem atrito e com o máximo de poder visual:

1. **Janela Principal de Comando**: **Claude Desktop (Aba Code)** ou **Antigravity Desktop** como terminal de concepção.
2. **Execução de Fila Paralela**: Quando houver 5 tarefas repetitivas (ex.: testes, scripts, mocks), abrir o **Codex Desktop App**, criar as 4 threads em Worktree e aprovar tudo de uma vez.
3. **Auditoria Final**: O Antigravity sobrevoa o resultado no navegador real para garantir que nenhum pixel ficou fora do lugar.

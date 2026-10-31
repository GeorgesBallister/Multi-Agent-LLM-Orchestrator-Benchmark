# Evidências reposicionam a orquestração multiagente

**Publicação Técnica LAY · Edição Baseada em Evidências · 31 de outubro de 2026**

---

## Sumário Executivo: A Decisão Baseada em Dados

**Decisão executiva.** Para o fluxo de desenvolvimento sem IDE analisado neste estudo, não há respaldo técnico ou empírico para declarar Claude, Codex ou Antigravity um vencedor universal. A hipótese operacional a testar adota superfícies separadas com papéis calibrados:
1. **Codex Desktop** opera como painel humano de filas, worktrees paralelas e revisão de diffs;
2. **Claude Code / Desktop** assume o planejamento arquitetural, especificações formais e revisão crítica de alto risco em baixo volume de requisições;
3. **Antigravity / Gemini** executa tarefas que demandam contexto multimodal, navegação web, crawl e verificação visual no browser quando necessárias;
4. **Scripts determinísticos locais** assumem operações mecânicas previsíveis (hash, recorte, conversão, validação geométrica e empacotamento), reduzindo o uso de LLM em trabalho que não exige julgamento generativo.

Essa separação reconhece que **MCP conecta ferramentas, mas não transfere cotas nem unifica assinaturas**. A telemetria local oferece uma explicação compatível com o esgotamento rápido da cota do Claude no caso estudado: **2.060 chamadas, 33 subagentes e média de 313 mil tokens de cache lidos por chamada**, com crescimento de 155 milhões de tokens de cache em cerca de cinco horas. Ela não revela a fórmula da cota do fornecedor.

> **Escopo e método.** Pesquisa consolidada em 31 de outubro de 2026. Separa documentação oficial, benchmarks com metodologia, experimentos independentes com artefatos e relatos comunitários (qualitativos, sem validade estatística). Preços/cotas vêm dos fabricantes; desempenho vem do benchmark primário. A telemetria é um estudo de caso local, não uma amostra de mercado; o rascunho histórico do Argon permanece como hipótese, não como fonte factual.

---

## 1. O Limite Caiu Porque o Contexto se Multiplicou

O esgotamento de cotas em agentes autônomos pode acompanhar a multiplicação do contexto em pipelines paralelos. No retrato de telemetria local de 31/10/2026, o Claude Code registrou:
- **1 sessão principal** e **33 subagentes**;
- **2.060 chamadas** ao modelo;
- **645.363.759 tokens de cache lidos** e **11.060.887 tokens de cache escritos**;
- **2.803.653 tokens de saída** e **851.360 tokens de raciocínio**.

Esses valores representam uma média descritiva de **313.283 tokens de cache lidos por chamada**. Entre 07:55 e 12:57, o ambiente instanciou 24 novos subagentes e realizou 986 chamadas adicionais; o cache lido expandiu em **155.138.357 tokens** sem nenhum evento de compactação registrado nesse intervalo. O modelo identificado como `claude-opus-5-5` respondeu por 61,8% das chamadas e 83,0% de todo o cache lido. Esses dados revelam uma operação que reapresentou um contexto maciço centenas de vezes em paralelo.

A documentação oficial da Anthropic detalha o mecanismo: cada turno de agente incorpora histórico, arquivos lidos, instruções do projeto (`CLAUDE.md`), saídas de ferramentas e o prompt do usuário. Os limites são compartilhados entre Claude na web, Claude Desktop e Claude Code. A orientação oficial recomenda:
- Abrir contextos novos para tarefas não relacionadas;
- Executar `/compact` periodicamente durante sessões longas;
- Usar `/clear` rigorosamente ao concluir cada tarefa;
- Monitorar o volume por meio de `/context`;
- Referenciar arquivos por caminhos em vez de colar conteúdos integrais no prompt;
- Manter regras de projeto concisas e modulares ([Anthropic, uso e limites do Claude Code](https://support.claude.com/en/articles/14552983-models-usage-and-limits-in-claude-code); [Anthropic, limites de uso](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work)).

A telemetria do Antigravity confirmou que a migração de fornecedor não elimina o gargalo: registrou 253 conversas, 7.065 chamadas e 443.261.118 tokens de cache lidos. O log documentou o evento real **“Individual quota reached”** com suspensão temporária do lote e gravação de flag de pausa. Nenhum plano de consumidor é infinito.

| Sinal Observado na Telemetria | Diagnóstico Seguro | Ação Operacional Recomendada |
|---|---|---|
| Média de 313 mil tokens de cache lidos por chamada | Contexto acumulado e reenviado continuamente | Encerrar a unidade em handover e iniciar sessão nova com `/clear` |
| 24 subagentes criados em 5 horas | Paralelismo sem isolamento multiplicou o contexto ativo | Limitar concorrência a 1 orquestrador e até 2 workers de alta capacidade |
| 986 chamadas sem nova compactação | Execução em loop contínuo sem redução de estado | Compactar dentro da tarefa; nunca tratar compactação como sessão infinita |
| Evento de cota atingida no Antigravity | Limite dinâmico presente em todos os fornecedores | Interromper despacho via flag de pausa; processar etapas mecânicas em script local |

*Hipótese comunitária sob monitoramento:* Relatos de usuários indicam que reabrir sessões após conclusão de subagentes pode provocar regravação volumosa de cache (243 mil a 399 mil tokens em casos reportados). Trata-se de hipótese qualitativa que deve ser aferida no ambiente de teste antes de ser classificada como bug oficial ([relato de cache no Claude Code](https://www.reddit.com/r/ClaudeAI/comments/1whvqcl/quota_draining_claude_code_rebills_a_finished/)).

---

## 2. Rankings Comparam Tarefas e Não Aplicativos

Comparações técnicas exigem alinhamento de escopo, dataset e infraestrutura:
- **SWE-bench** afere resolução de issues reais sob um scaffold de agente padronizado (o subconjunto Verified possui 500 instâncias auditadas por humanos, enquanto o harness Bash Only isola o agente);
- **Terminal-Bench 4.0** avalia execução estrita em terminal (66 tarefas, até 500 passos, média de 3 repetições sob infraestrutura controlada);
- **Artificial Analysis** unifica avaliações de código, ciência e raciocínio com métricas de custo e latência;
- **LLM Stats** calcula ratings relativos com estimativa de incerteza estatística;
- **OpenRouter Rankings** expõe volume público de tráfego de seu marketplace, indicando adoção na plataforma, mas não qualidade técnica ([metodologia Artificial Analysis](https://artificialanalysis.ai/methodology/intelligence-benchmarking); [metodologia LLM Stats](https://llm-stats.com/research); [OpenRouter Rankings](https://openrouter.ai/rankings)).

### Evidências da Bateria Artificial Analysis (Snapshot de 31/10/2026)

Na metodologia v5.0 da Artificial Analysis, observou-se:
1. **FrontierCode 2.0 (tarefas agênticas complexas de código):**
   - Claude Opus 5.5 (esforço max): **46%**
   - GPT-6 Astra (esforço max): **42%**
   - GPT-6.1 Sol Terra: **42%**
   - Claude Sonnet 5.5: **42%**
   *(Diferença estreita de 4 pontos percentuais; orienta hipótese de piloto, sem comprovar superioridade universal).*
2. **Terminal-Bench-Science (execução autônoma de ferramentas em terminal):**
   - GPT-6 Astra (esforço max): **63%**
   - Claude Opus 5.5 (esforço max): **59%**
3. **Custo por Tarefa Observado na Mesma Bateria:**
   - Claude Opus 5.5 max: **US$ 10,04**
   - GPT-6 Astra max: **US$ 6,24**
   - GPT-6 Sol max: **US$ 1,27**

No leaderboard ao vivo capturado em 31/10/2026, Gemini 4 Carbon High marcou índice 59, Opus 5.5 max 58 e Astra max 57. Dias antes, a publicação inicial mostrava ordem distinta. A alternância comprova que esforço de raciocínio, versão e data alteram rankings dinâmicos.

Para geração e edição de imagens, o leaderboard de preferência humana cega da Artificial Analysis registrou GPT Image 2.5 Sunburst max em primeiro lugar na geração (Elo 1222±10, 13.014 amostras) e na edição (Elo 1199±11, 18.250 amostras), com Nano Banana 2.1 em 4º na geração (Elo 1176±12) e na faixa de 4º a 7º na edição (Elo 1151±13) ([geração](https://artificialanalysis.ai/image/leaderboard/text-to-image); [edição](https://artificialanalysis.ai/image/leaderboard/editing)).

| Pergunta Técnica | Evidência Apropriada | Conclusão Permitida | Conclusão Proibida |
|---|---|---|---|
| Qual modelo resolve issues sob scaffold fixo? | SWE-bench com mesmo agente e versão | Comparar modelos dentro daquele protocolo exato | Afirmar que "o modelo resolve 90% de qualquer software" |
| Qual configuração teve maior taxa no terminal? | Terminal-Bench com repetições e esforço documentados | Selecionar candidato prioritário para teste local | Comparar pontuação de terminal com SWE-bench |
| Qual modelo lidera preferência visual cega? | Leaderboard cego de imagem datado | Escolher ponto de partida para geração de assets | Presumir precisão de alpha ou conformidade de UI |
| O que indica o tráfego do OpenRouter? | Dados de requisições e tokens do marketplace | Entender demanda relativa daquela plataforma | Declarar mix ideal universal ou qualidade de modelo |
| Qual o valor de testes do Reddit? | Post com logs, código e ambiente reproduzíveis | Mapear hipóteses e modos de falha reais | Tratar relatos isolados como consenso estatístico |

---

## 3. Assinaturas, Aplicativos e CLIs Não se Fundem

Os três provedores disponibilizam clientes oficiais para operação sem IDE, mantendo contas, cobrança e cotas estritamente isoladas:
- **Claude Code**: integrado à assinatura Pro/Max no terminal e na aba Code do Claude Desktop;
- **Codex**: disponível como aplicativo de desktop (Windows, macOS, Linux), CLI e web para planos ChatGPT;
- **Antigravity 2.0**: aplicativo autônomo e CLI `agy` com suporte nativo a subagentes, Skills, MCP e automação de navegador ([Claude Code no plano](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan); [Codex e plano ChatGPT](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan); [Antigravity 2.0](https://antigravity.google/product/antigravity-2/)).

### A Regra de Isolamento de Cotas e MCP
O protocolo MCP (*Model Context Protocol*) interliga ferramentas e servidores de contexto; **ele não transfere privilégios nem cotas de um provedor para outro**. Se o Claude Code for executado com `ANTHROPIC_API_KEY` preenchida no ambiente, as requisições serão faturadas por token na API comercial, desconsiderando a assinatura Pro. O mesmo se aplica ao excedente do Antigravity quando configurado para "Always" e a ferramentas externas ([Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code/cli-usage); [OpenAI, Sign in with ChatGPT](https://help.openai.com/en/articles/20001542-using-your-chatgpt-plan-in-other-apps-and-sites); [Google One, Antigravity](https://support.google.com/googleone/answer/14534406)).

| Superfície Operacional | Papel Recomendado | Capacidade Verificada | Limite Inegociável |
|---|---|---|---|
| **Codex Desktop** | Painel humano de filas, worktrees, branches e aprovação de diffs | Gerenciamento de múltiplos agentes e worktrees paralelas | Não herda cotas de terceiros; exige revisão humana pré-merge |
| **Claude Desktop / Code** | Arquitetura, contratos, revisão crítica e raciocínio profundo | Suporte a subagentes, MCP e worktrees documentados | Cota dinâmica Pro de 5h compartilhada entre web, app e CLI |
| **Antigravity / `agy`** | Contexto multimodal alargado, navegação web e QA visual | Orquestração com browser, Skills, MCP e keyring nativo | Cotas temporais e semanais; bloqueio dinâmico por fornecedor |
| **Scripts Locais & GPU** | Hash, resize, conversão, validação de arquivos e testes | Execução determinística, custo zero de token, reprodutibilidade | Não realizam julgamento semântico ou direção de arte |

---

## 4. Arquitetura de Encaminhamento e Rotina Diária

A orquestração proposta substitui a busca por um "modelo vencedor" por encaminhamento de tarefa: primeiro scripts para trabalho determinístico; Codex para implementação delimitada após piloto; Claude para decisões arquiteturais e revisão crítica; Gemini/Antigravity para pesquisa, multimodalidade e QA visual quando essas capacidades forem necessárias. O dono humano fecha cada tarefa com contrato, evidência e aprovação. Os papéis são uma hipótese calibrável, sem cota compartilhada entre fornecedores.

### Rotina Diária para Conter Contexto e Cota

1. **Comece pela tarefa, não pelo modelo:** escreva objetivo, arquivos permitidos, commit de origem, entrada, saída e teste de aceite. Consulte o medidor de cada fornecedor separadamente.
2. **Tire o trabalho mecânico do caminho:** rode primeiro scripts locais para hash, resize, conversão, fixtures e outras operações determinísticas.
3. **Use Claude em pontos de decisão:** peça um plano focado para arquitetura ou risco; implemente em uma unidade delimitada e feche a sessão com resumo. Em tarefas distintas, use contexto novo e `/clear`; em tarefa longa, consulte `/context` e compacte com `/compact`.
4. **Encaminhe a execução uma vez:** Codex para implementação modular após piloto; Gemini/Antigravity para pesquisa/crawl ou QA visual que use browser. Evite mandar o mesmo prompt para os três sem uma pergunta de comparação definida.
5. **Feche com evidência:** execute testes, revise o diff e salve um handoff curto com arquivos, resultados, medidores antes/depois e próxima ação. Ao atingir aviso de quota, pare novos despachos daquele serviço.

Esse ciclo busca reduzir releituras de contexto e chamadas redundantes. Não há dado neste estudo que permita prometer uma porcentagem de economia ou prever a cota restante.

### Matriz de Classes de Trabalho e Políticas de Risco

| Classe de Trabalho | Dono da Decisão | Executor Inicial | Verificação Obrigatória | Política de Custo e Risco |
|---|---|---|---|---|
| **Arquitetura, shaders core, contratos e licenças** | Agente de alta capacidade + Humano | Claude Opus ou GPT Astra (após piloto) | Revisão independente, testes e typecheck estrito | 1 agente por decisão; sem paralelismo no mesmo contrato |
| **Implementação React/R3F/GSAP e módulos** | Orquestrador fixa contrato e interfaces | Worker em worktree isolado (Codex) | Suíte de testes unitários e teste de integração | Paralelizar somente módulos com arquivos disjuntos |
| **Vitest, mocks, fixtures e scripts repetitivos** | Especificação aprovada pelo orquestrador | Codex ou worker rápido após piloto | Suíte executada com cobertura útil comprovada | Lote delimitado; medir retrabalho antes de escalar |
| **Playwright, inspeção DOM, WebGL e QA por pixel** | Orquestrador avalia evidência capturada | Antigravity / runner de browser | Screenshots, console limpo e diff visual | Agente visual executa; aprovação final permanece humana |
| **Geração de assets visuais ou sonoros** | Direção de arte e referência recortada | GPT Image Sunburst ou Nano Banana 2.1 | Alpha, silhueta e prancha comparativa lado a lado | 1 asset por prompt; não gerar colagens compostas |
| **Processamento determinístico de arquivos** | Script validado | GPU e CPU locais | Checksum SHA-256, contagem e integridade | Custo zero de token; vedado uso de LLM para lógica fixa |
| **Gate final de integração e merge** | Responsável humano | Um integrador isolado por vez | Testes verdes, diff revisado e build de produção | Proibido uso de flags que desativem aprovação humana |

---

## 5. Decomposição Estruturada de Custos

O custo operacional real de uma infraestrutura multiagente não é fixo. Ele deve ser decomposto formalmente em quatro camadas:
$$\text{Custo Operacional Total} = \text{Assinaturas Fixas} + \text{Impostos e Câmbio} + \text{API Variável} + \text{Computação Local}$$

### 1. Assinaturas Fixas Oficiais
- **Claude Pro**: **US$ 20/mês** nos Estados Unidos (ou US$ 17/mês no plano anual pago antecipadamente) ([Claude Pricing](https://claude.com/pricing));
- **ChatGPT Plus**: **US$ 20/mês** nos Estados Unidos ([Codex Pricing](https://learn.chatgpt.com/docs/pricing));
- **Google AI Pro**: Valor varia conforme o país e a modalidade da conta Google ([Antigravity Pricing](https://antigravity.google/pricing); [Google One Help](https://support.google.com/googleone/answer/14534406)).

### 2. Impostos e Câmbio
O total em reais depende do câmbio efetivo, do emissor do cartão e de tributos que apareçam na fatura. Como o estudo não dispõe das faturas nem da cotação aplicada, não converte os preços em dólar para reais.

### 3. Consumo de API Variável
Ocorre quando chaves como `ANTHROPIC_API_KEY` ou `OPENAI_API_KEY` são ativadas em CLIs, quando ferramentas MCP utilizam endpoints pagos ou quando o controle de excedente do Antigravity é configurado como "Always".

### 4. Computação Local
Consumo de hardware da estação de trabalho (GPU dedicada e CPU em tarefas de build, renderização, conversão de assets e testes E2E locais), energia elétrica e banda. A telemetria local registrou 0,57 hora de GPU/CPU no pipeline analisado, sem potência média nem tarifa; não permite calcular custo de energia.

### [SIMULAÇÃO] Cenário Modelado de Roteamento em Regime Piloto
*Aviso Mandatório: A simulação a seguir é um modelo conceitual de engenharia para distribuição de carga. NÃO constitui previsão de fatura, garantia financeira ou medição de faturamento real.*

**Premissas da Simulação:**
- Projeto executa volume representativo de 100 tarefas semanais de engenharia;
- Chaves de API e excedentes pagos desligados; sem assumir custo variável adicional.

| Destino ilustrativo | Participação | Tarefas do cenário |
|---|---:|---:|
| Script local | 50% | 50 |
| Codex | 30% | 30 |
| Claude | 15% | 15 |
| Gemini / Antigravity | 5% | 5 |

**Leitura da simulação:**
O mix 50/30/15/5 é um ponto de partida, não medição de desempenho, cota ou fatura. Só um piloto pode comparar consumo, qualidade e retrabalho; não há base para prometer economia ou eliminação de saturação.

---

## 6. O Piloto que Transforma Hipótese em Engenharia

Antes de adotar qualquer modelo como padrão ou alterar contratações, o protocolo estabelece a execução de um piloto controlado:
1. **Corpus**: 20 a 50 tarefas fechadas extraídas do próprio repositório, abrangendo testes unitários, refactors modulares, fluxos de terminal e páginas de UI;
2. **Condições**: Mesmo commit de origem, mesma especificação de requisitos, mesmo tempo limite e isolamento em worktrees;
3. **Métrica Central**: **Taxa de tarefas aceitas por real e por hora**, acompanhada pelo índice de retrabalho humano e defeitos em produção.

| Resultado do Piloto | Decisão de Engenharia | Próxima Ação Prática |
|---|---|---|
| Worker rápido passa testes com mínimo retrabalho | Ampliar carga nessa classe de tarefa | Medir por mais uma semana mantendo auditoria cega |
| Modelo de fronteira reduz horas de revisão crítica | Reservar estritamente para contratos e gates | Manter concorrência em 1 worker e monitorar cota |
| Testes visuais identificam regressões não cobertas | Tornar etapa no browser obrigatória | Automatizar capturas de tela sem dispensar aprovação |
| Contexto cresce sem elevação no índice de aceite | Interromper sessão e isolar o escopo | Gerar artefato de handover, rodar `/clear` e reiniciar |
| Fornecedor atinge limite dinâmico de 5 horas | Suspender novos despachos ao fornecedor | Redirecionar trabalho para scripts locais determinísticos |

---

## 7. Síntese Executiva

> Em engenharia de software agêntica, a pergunta crítica não é qual modelo "vence" benchmarks, mas qual arranjo entrega trabalho aceito com menos retrabalho e dentro de limites observáveis. A telemetria local mostra contexto e paralelismo altos no caso analisado; a documentação é compatível com esses fatores, mas não prova uma relação causal nem permite prever cotas. O uso proposto distribui decisão, execução, QA visual e operações determinísticas por necessidade. O piloto deve confirmar ou refutar essa hipótese antes de aumentar a carga de qualquer ferramenta.

---

## 8. Bibliografia Anotada

1. **Anthropic.** [Claude Pricing](https://claude.com/pricing). Preços-base, planos e limites gerais de modelos. Acesso em 31 out. 2026.
2. **Anthropic.** [How do usage and length limits work?](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work). Janela dinâmica de 5 horas e limite semanal. Acesso em 31 out. 2026.
3. **Anthropic.** [Models, usage, and limits in Claude Code](https://support.claude.com/en/articles/14552983-models-usage-and-limits-in-claude-code). Boas práticas de contexto, `/clear`, `/compact`, `/context` e alocação de modelos. Acesso em 31 out. 2026.
4. **Anthropic.** [Use Claude Code with your Pro or Max plan](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan). Regras de autenticação por assinatura e separação de faturamento de API. Acesso em 31 out. 2026.
5. **Anthropic.** [Claude Code CLI usage](https://docs.anthropic.com/en/docs/claude-code/cli-usage). Interface oficial de automação por terminal e flags. Acesso em 31 out. 2026.
6. **OpenAI.** [Introducing the Codex app](https://openai.com/index/introducing-the-codex-app/). Centro de comando para múltiplos agentes paralelos e worktrees. Acesso em 31 out. 2026.
7. **OpenAI.** [Using Codex with your ChatGPT plan](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan). Escopo da assinatura ChatGPT, interfaces e distinção de API. Acesso em 31 out. 2026.
8. **OpenAI.** [Codex Pricing](https://learn.chatgpt.com/docs/pricing). Faixas estimadas de tarefas por modelo e limites de consumo. Acesso em 31 out. 2026.
9. **OpenAI.** [Using your ChatGPT plan in other apps and sites](https://help.openai.com/en/articles/20001542-using-your-chatgpt-plan-in-other-apps-and-sites). Políticas de uso de conta fora dos clientes proprietários. Acesso em 31 out. 2026.
10. **Google.** [Antigravity 2.0](https://antigravity.google/product/antigravity-2/), [Pricing](https://antigravity.google/pricing) e [Choose a model](https://antigravity.google/docs/models). Recursos autônomos, modelos suportados e regras de quota. Acesso em 31 out. 2026.
11. **Google.** [Antigravity CLI](https://github.com/google-antigravity/antigravity-cli) e [Google One Help: Antigravity](https://support.google.com/googleone/answer/14534406). Login por chaveiro de sistema, pooling de créditos e controle de excedente. Acesso em 31 out. 2026.
12. **Google.** [Aviso sobre ferramentas de terceiros](https://github.com/google-gemini/gemini-cli/discussions/20632). Diretrizes oficiais contra o uso de proxies não homologados. Acesso em 31 out. 2026.
13. **SWE-bench.** [Página oficial](https://www.swebench.com/). Metodologia de avaliação de software, dataset Verified e ambiente padronizado. Acesso em 31 out. 2026.
14. **Artificial Analysis.** [Metodologia de inteligência](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Intelligence Index v5.0](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5/) e [leaderboard](https://artificialanalysis.ai/leaderboards/models). Snapshots de FrontierCode 2.0, Terminal-Bench e custo por tarefa. Acesso em 31 out. 2026.
15. **LLM Stats.** [Research](https://llm-stats.com/research) e [leaderboard](https://llm-stats.com/leaderboards/llm-leaderboard). Ratings relativos e modelos estatísticos de incerteza. Acesso em 31 out. 2026.
16. **OpenRouter.** [Rankings](https://openrouter.ai/rankings). Tráfego e demanda pública de marketplace. Acesso em 31 out. 2026.
17. **Artificial Analysis.** [Metodologia de imagem](https://artificialanalysis.ai/methodology/image), [geração](https://artificialanalysis.ai/image/leaderboard/text-to-image) e [edição](https://artificialanalysis.ai/image/leaderboard/editing). Leaderboard de preferência humana cega em geração e edição de imagens. Acesso em 31 out. 2026.
18. **Reddit e repositórios de experimentos.** [Opus para planejar e Codex para executar](https://www.reddit.com/r/ClaudeAI/comments/1sdk2sj/i_benchmarked_plan_with_opus_execute_with_codex/); [seis projetos Codex vs Claude](https://www.reddit.com/r/codex/comments/1tbkmc3/codex_vs_claude_code_i_ran_a_6project_benchmark/); [repositório do experimento](https://github.com/AdrielRod/codex-vs-claude-code). Relatos de engenharia independentes. Acesso em 31 out. 2026.
19. **Relatos de comunidade.** [Quotas Codex](https://www.reddit.com/r/codex/comments/1w9up47/what_on_earth_happened_to_usage_limits/), [comparativo dos três aplicativos](https://www.reddit.com/r/codex/comments/1s1btfx/codex_vs_claude_code_vs_antigravity_whats_your/) e [cache no Claude](https://www.reddit.com/r/ClaudeAI/comments/1whvqcl/quota_draining_claude_code_rebills_a_finished/). Evidências qualitativas de modos de falha. Acesso em 31 out. 2026.
20. **Nimbalyst e Paradev.** [Nimbalyst](https://github.com/Nimbalyst/nimbalyst); [Paradev](https://github.com/ParadevAI/Paradev); [mudança de nome](https://paradev.com/blog/a-new-name); [instalação Paradev](https://docs.paradev.com/install). Licenciamento, arquitetura e limites de compatibilidade. Acesso em 31 out. 2026.
21. **Evidência local auditada.** Snapshot de telemetria de 31 out. 2026 (`telemetria-ia-ultima.json`, `telemetria-ia-historico.csv`); logs do pipeline R06 e transcrições de sessão. Dados restritos ao estudo de caso local.

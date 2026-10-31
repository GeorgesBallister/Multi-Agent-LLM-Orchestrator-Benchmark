# Produtos, cotas e restrições oficiais para orquestração multiagente

Pesquisa concluída em 31 de outubro de 2026 (America/São_Paulo). Salvo quando indicada outra data, todas as páginas foram consultadas nessa data. Este documento usa apenas fontes primárias dos fabricantes para afirmar capacidades, preços, cotas e regras de autenticação. Resultados de Reddit, vídeos, blogs independentes e benchmarks de terceiros pertencem a outra camada da pesquisa e não são tratados aqui como fatos oficiais.

## Qual é o estado atual dos três produtos comparados?

### Takeaway

Claude Code, Codex e Antigravity são hoje agentes de desenvolvimento utilizáveis fora de um IDE tradicional. Os três têm uma interface oficial de linha de comando. Codex e Antigravity também se apresentam oficialmente como aplicativos autônomos de orquestração; Claude oferece Claude Code tanto no terminal quanto na aba Code do aplicativo Claude Desktop. A descrição antiga do Antigravity como apenas um IDE derivado de VS Code está desatualizada.

### Cited Findings

- A Anthropic inclui Claude Code no plano Pro e documenta seu uso na aba Code do Claude Desktop, no terminal e em IDEs suportados ([Claude Help Center, “Use Claude Code with your Pro or Max plan”](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan)).
- A OpenAI descreve o Codex app como um “command center” para múltiplos agentes, com tarefas paralelas e worktrees integradas; a versão para Windows foi anunciada em 4 de março de 2026 ([OpenAI, “Introducing the Codex app”](https://openai.com/index/introducing-the-codex-app/)).
- A OpenAI documenta Codex em aplicativo, CLI, IDE, web e iOS dentro dos planos ChatGPT elegíveis ([OpenAI Help Center, “Using Codex with your ChatGPT plan”](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan)).
- O Antigravity 2.0 é apresentado pelo Google como aplicativo autônomo para Windows, macOS e Linux, com múltiplos agentes paralelos, subagentes, Skills, MCP e hooks; o produto também oferece CLI e extensões para IDEs ([Google, Antigravity 2.0](https://antigravity.google/product/antigravity-2/); [Google Antigravity Docs, “Choose a model”](https://antigravity.google/docs/models)).
- O repositório oficial da CLI `agy` afirma que app e CLI compartilham o mesmo motor central de agente e as mesmas configurações, com autenticação por Google Sign-In e armazenamento de credenciais no keyring do sistema ([Google, repositório oficial `google-antigravity/antigravity-cli`](https://github.com/google-antigravity/antigravity-cli)).
- O Google encerrou a autenticação de consumidor na antiga Gemini CLI e orientou usuários individuais a migrarem para a Antigravity CLI em 18 de junho de 2026 ([Google Developers, depreciação do Gemini Code Assist for individuals](https://developers.google.com/gemini-code-assist/docs/deprecations/code-assist-individuals); [anúncio oficial no repositório Gemini CLI](https://github.com/google-gemini/gemini-cli/discussions/27274)).

### Inferences

- Para um fluxo “sem IDE”, não é necessário escolher o produto apenas pela existência de CLI: todos os três atendem esse requisito. A decisão deve ser guiada por cotas, ergonomia de orquestração, necessidade de navegador/computer use e tolerância a limites dinâmicos.
- A existência de extensões de IDE no Antigravity não transforma o IDE em requisito; app e CLI são superfícies oficiais independentes.

### Gaps

- As fontes oficiais não oferecem um benchmark neutro, reproduzível e idêntico entre os três produtos. Qualquer ranking de “melhor orquestrador” exige testes externos ou um protocolo próprio.
- As interfaces mudam rapidamente. A seleção efetivamente exibida na conta e o comando de status/uso de cada produto permanecem a fonte operacional mais confiável para aquela conta.

## Quais planos, preços e mecânicas de cota são oficialmente publicados?

### Takeaway

Claude Pro e ChatGPT Plus custam oficialmente US$ 20/mês nos Estados Unidos. O preço brasileiro do Google AI Pro deve ser conferido na conta/localidade; não há base suficiente nas páginas globais consultadas para fixar “R$ 99” como preço universal. Nos três ecossistemas, cotas são dinâmicas. Anthropic, OpenAI e Google usam janelas de cinco horas e semanais em pelo menos parte dos planos, porém só a OpenAI fornece atualmente faixas estimadas de mensagens/tarefas por modelo para Codex. Nenhum número desse tipo é uma garantia contratual.

### Cited Findings

| Produto/plano | Preço oficial publicado | Mecânica oficial de cota | O que não é prometido |
|---|---:|---|---|
| Claude Pro | US$ 20/mês ou US$ 17/mês no anual, cobrado US$ 200 antecipadamente | Limite de 5 horas e limite semanal; Pro = 1×. O uso é compartilhado entre Claude, Claude Desktop e Claude Code. | Quantidade fixa de mensagens. O consumo varia por modelo, tamanho do contexto, arquivos, recursos e esforço. ([Claude Pricing](https://claude.com/pricing); [Claude Help, limites](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work)) |
| Claude Max | US$ 100/mês | 5× o Pro em cada janela de 5 horas e na semana; prioridade em tráfego alto. | “Uso ilimitado”. ([Claude Pricing](https://claude.com/pricing)) |
| Claude Ultra | US$ 200/mês | Sem limite de 5 horas para contas verificadas; 10× o Pro por semana. | Semana ilimitada. ([Claude Pricing](https://claude.com/pricing)) |
| ChatGPT Plus / Codex | US$ 20/mês nos EUA | Uma janela de 5 horas e uma cota semanal compartilhadas pelo trabalho local e em nuvem; o consumo varia conforme modelo, local de execução, contexto, raciocínio e ferramentas. | Um número fixo ou “nunca atinge o limite”. ([Codex Pricing](https://learn.chatgpt.com/docs/pricing); [OpenAI Help, resets](https://help.openai.com/en/articles/20001498-how-resets-work-in-codex)) |
| ChatGPT Pro / Codex | A partir de US$ 100/mês | Três níveis de uso; sessões mais longas. Os valores exatos dependem do nível escolhido. | “Ilimitado” fora das salvaguardas e do nível contratado. ([ChatGPT Pricing](https://chatgpt.com/pricing/); [Codex Pricing](https://learn.chatgpt.com/docs/pricing)) |
| Antigravity Free | US$ 0 | Limites básicos semanais; a tela de uso do produto mostra saldo semanal e de 5 horas. | Quantidade pública fixa de prompts ou sessões. ([Antigravity Pricing](https://antigravity.google/pricing); [Antigravity Docs, modelos e uso](https://antigravity.google/docs/models)) |
| Google AI Pro / Antigravity | Preço varia por país e conta | Limites maiores que o Free, mais um pool flexível de créditos de IA; a capacidade não é garantida. | “5–6 sessões pesadas” ou outro total fixo. ([Antigravity Pricing](https://antigravity.google/pricing); [Google One Help, Antigravity](https://support.google.com/googleone/answer/14534406)) |
| Google AI Ultra / Antigravity | Preço varia por país e conta | Limites maiores que o Pro e pool maior de créditos. | Quantidade pública fixa de tarefas. ([Antigravity Pricing](https://antigravity.google/pricing); [Google One Help, Antigravity](https://support.google.com/googleone/answer/14534406)) |

- No Claude, a primeira mensagem inicia a janela; ela é restaurada integralmente cinco horas depois. O limite semanal restaura em horário fixo específico da conta ([Claude Help, “How do usage and length limits work?”](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work)).
- A página atual de preços do Codex oferece apenas estimativas, não garantias, para tarefas locais por janela de cinco horas no Plus: GPT-6 Astra, 5–45; GPT-6.1 Sol, 15–160; GPT-6.1 Terra, 35–285; GPT-6 Sol, 15–150; GPT-6 Luna, 350–3.000. Trabalho local e em nuvem compartilha a cota, e limites semanais podem se aplicar ([OpenAI, Codex Pricing](https://learn.chatgpt.com/docs/pricing)).
- A OpenAI permite que usuários Plus/Pro elegíveis comprem créditos ou resets adicionais; um reset instantâneo restaura as janelas de cinco horas e semanal e reinicia o calendário semanal ([OpenAI Help, créditos no Codex](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan); [OpenAI Help, paid resets](https://help.openai.com/en/articles/20001507-paid-weekly-work-and-codex-rate-limit-resets)).
- O Google informa que as cotas básicas são temporais e dependem do nível; quando habilitado, o excedente do Antigravity usa créditos de IA a preços padrão de API. O usuário pode configurar o excedente como “Never” ou “Always” ([Google One Help, Antigravity e créditos](https://support.google.com/googleone/answer/14534406)).
- A Anthropic permite ativar créditos de uso após a cota do plano; se uma chave de API estiver configurada para o Claude Code, o consumo é cobrado como API em vez de usar a assinatura ([Claude Help, usage credits](https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans); [Claude Help, Claude Code no plano](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan)).

### Inferences

- “US$ 20/mês” descreve apenas o preço-base de Claude Pro e ChatGPT Plus. Impostos, conversão, cobrança local, créditos adicionais e API podem alterar o gasto real.
- Uma comparação honesta de valor precisa registrar o modelo utilizado, o tamanho inicial e final do contexto, o número de tool calls e as duas barras de cota. Contar apenas prompts mistura tarefas muito diferentes.
- A alegação “Antigravity reseta a cada 5 horas” é hoje parcialmente correta, mas incompleta: a documentação atual também mostra limite semanal. Não há respaldo oficial para converter isso em um número fixo de sessões.

### Gaps

- O Google não publica nas páginas consultadas um total de prompts/tokens por nível do Antigravity. “Mais” e “ainda mais” são descrições relativas.
- A OpenAI publica intervalos estimados para Codex, mas não uma fórmula de conversão de tokens para tarefas. A Anthropic não publica um contador fixo de mensagens para o Pro atual.
- O preço local exato do Google AI Pro/Ultra e promoções dependem de país, conta, tributos e momento da contratação; deve ser capturado na tela oficial da conta usada no teste.

## Quais modelos estão realmente disponíveis hoje?

### Takeaway

Os nomes recentes encontrados na conversa — Claude Opus/Sonnet 5.5, família GPT-6 e Nano Banana 2/2.1 — existem oficialmente. Isso não valida automaticamente os rankings ou resultados atribuídos a eles. A lista efetiva de modelos pode depender de plano, região e rollout; o seletor ou comando de modelo da própria conta prevalece.

### Cited Findings

- A tabela de preços da Anthropic lista Opus, Sonnet e Haiku nos planos Pro, Max e Ultra, com janela de contexto de até 1 milhão de tokens variando por modelo ([Claude Pricing](https://claude.com/pricing)).
- A documentação atual do Claude Code enumera Haiku 5.5, Sonnet 5.5, Opus 5.5 e Fable 5.1, entre outros, e orienta usar `/model` como fonte de verdade da disponibilidade na conta ([Claude Help, “Claude Code model configuration”](https://support.claude.com/en/articles/11940350-claude-code-model-configuration)).
- A Anthropic anunciou Opus 5.5 em 22 de setembro de 2026, Sonnet 5.5 em 28 de setembro e Haiku 5.5 em 7 de outubro; a página oficial também registra Fable 5.1 ([Anthropic, “Models”](https://www.anthropic.com/news/models)).
- A OpenAI lista atualmente GPT-6.1 Sol, GPT-6 Astra, GPT-6.1 Terra, GPT-6 Sol e GPT-6 Luna entre os modelos de Codex/ChatGPT, com acesso variando por plano ([OpenAI, Codex Pricing](https://learn.chatgpt.com/docs/pricing); [ChatGPT Pricing](https://chatgpt.com/pricing/)).
- O seletor oficial do Antigravity lista Gemini 4 Argon, Gemini 3.8/3.7/3.6 Flash, Gemini 3.1 Pro, Claude Sonnet 5.5, Claude Opus 5.5, Claude Sonnet 4.6, Claude Opus 4.6 e GPT-OSS 120B; a disponibilidade depende do plano ([Google Antigravity Docs, “Choose a model”](https://antigravity.google/docs/models)).
- O Google identifica Nano Banana 2 como Gemini 3.1 Flash Image e o descreveu em 26 de fevereiro de 2026; a documentação atual também apresenta Nano Banana 2.1 como a opção eficiente mais recente para geração/edição de imagens ([Google Developers Blog, Nano Banana 2](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-nano-banana-2/); [Gemini API, Nano Banana 2.1](https://ai.google.dev/gemini-api/docs/models/gemini-nano-banana-2.1)).
- A OpenAI anunciou GPT Image 2.5 Sunburst e Flare em 8 de setembro de 2026, disponíveis em ChatGPT, Work e Codex; Sunburst prioriza precisão/edição e Flare velocidade ([OpenAI, “Introducing ChatGPT Images 2.5”](https://openai.com/index/introducing-chatgpt-images-2-5/)).

### Inferences

- “GPT-OSS 120B” no Antigravity não equivale a acesso a GPT-6/Codex nem transfere direitos de uma assinatura ChatGPT. É um modelo distinto oferecido pelo Google dentro do Antigravity.
- Um nome de modelo verdadeiro não torna verdadeiro um número de benchmark associado a ele. Modelo, variante, data, configuração de raciocínio, ferramentas e conjunto de testes precisam coincidir.

### Gaps

- Não foi encontrada fonte oficial que confirme “Opus 5.5 tornou-se silenciosamente o padrão do Claude Code Pro na versão 2.1.280”. A documentação manda consultar `/model`; a alegação de padrão/versão deve ser removida ou demonstrada por captura e changelog oficiais.
- A janela “até 1M” não significa que todo plano, modelo, ferramenta e conversa sempre usem 1M, nem que a saída nunca seja truncada. O limite de saída é uma propriedade separada.
- Rankings como “GPT Image 2.5 é nº 1 no Artificial Analysis” não são afirmações do fabricante e exigem fonte e data do benchmark de terceiro.

## Quais recursos de orquestração são oficialmente suportados?

### Takeaway

Codex e Antigravity têm o conjunto oficial mais explícito para orquestração visual de vários agentes: subagentes, tarefas paralelas, worktrees, navegador e aplicativo autônomo. Claude Code oferece subagentes, MCP e execução paralela com worktrees, mas sua assinatura Pro compartilha uma cota sensível ao contexto com o chat/desktop. “Suporta” significa que há documentação oficial do recurso, não que ele esteja disponível em toda conta, região ou plano.

### Cited Findings

| Recurso | Claude / Claude Code | OpenAI Codex / ChatGPT | Google Antigravity |
|---|---|---|---|
| Subagentes | Sim, agentes especializados com contexto e permissões próprios ([Claude Code, subagents](https://docs.anthropic.com/en/docs/claude-code/sub-agents)) | Sim, no app/CLI e na matriz oficial do Codex ([Codex Pricing](https://learn.chatgpt.com/docs/pricing); [Codex app](https://openai.com/index/introducing-the-codex-app/)) | Sim, subagentes dinâmicos e customizáveis ([Antigravity 2.0](https://antigravity.google/product/antigravity-2/); [Antigravity Docs, custom subagents](https://antigravity.google/docs/subagents)) |
| Worktrees / isolamento Git | Documenta sessões paralelas com Git worktrees ([Claude Code, common workflows](https://docs.anthropic.com/en/docs/claude-code/common-workflows)) | Worktrees integradas no app ([Codex app](https://openai.com/index/introducing-the-codex-app/)) | Worktrees nativas por projeto ([Antigravity Features](https://antigravity.google/docs/features)) |
| MCP / conectores | MCP em Claude Code e Claude Desktop ([Anthropic MCP](https://docs.anthropic.com/en/docs/mcp)) | MCP configurável na CLI/IDE, com configuração compartilhada ([OpenAI Developers, MCP](https://developers.openai.com/learn/docs-mcp)) | MCP, Skills, plugins e hooks oficiais ([Antigravity 2.0](https://antigravity.google/product/antigravity-2/); [Antigravity Docs, MCP](https://antigravity.google/docs/mcp)) |
| Navegador / computer use | Claude em Chrome faz parte do Pro; computer use programático também existe na API, mas é superfície/billing separado ([Claude Pricing](https://claude.com/pricing); [Anthropic API, computer use](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/computer-use-tool)) | App inclui navegador/computer use e pode trabalhar com imagens ([OpenAI, “Codex for almost everything”](https://openai.com/index/codex-for-almost-everything/)) | `/browser` cria subagente com contexto isolado, Chrome/DevTools, screenshots e gravações ([Antigravity Docs, browser](https://antigravity.google/docs/commands/browser)) |
| Geração/edição de imagem | Não foi localizado gerador nativo equivalente documentado para Claude Code; integrações externas são possíveis via ferramentas/MCP | GPT Image 2.5 está disponível no Codex e ChatGPT ([OpenAI, Images 2.5](https://openai.com/index/introducing-chatgpt-images-2-5/)) | Nano Banana existe no ecossistema Gemini, mas não foi demonstrado nas fontes consultadas como ferramenta nativa garantida de toda sessão Antigravity ([Gemini API, Nano Banana 2.1](https://ai.google.dev/gemini-api/docs/models/gemini-nano-banana-2.1)) |
| Compactação/contexto | `/compact`, `/clear`, `/context` e gerenciamento automático em alguns fluxos ([Claude Help, model usage and limits](https://support.claude.com/en/articles/14552983-models-usage-and-limits-in-claude-code)) | A plataforma Agents oferece compactação; o app gerencia contexto de tarefas, mas a mecânica exata do produto pode mudar ([OpenAI Developers, Agents API](https://developers.openai.com/api/docs/guides/agents-api/overview)) | `/context` detalha tokens e checkpoints; a CLI compacta turnos antigos automaticamente em resumos de checkpoint ([Antigravity CLI, `/context`](https://antigravity.google/docs/cli/commands/context/)) |
| Automação agendada | Claude permite handoff/agendamento nos planos pagos ([Claude Pricing](https://claude.com/pricing)) | Codex oferece trabalho agendado ([OpenAI, Codex for almost everything](https://openai.com/index/codex-for-almost-everything/)) | `/schedule` e scheduled tasks ([Antigravity Features](https://antigravity.google/docs/features)) |

### Inferences

- Para coordenação visual de muitas tarefas simultâneas, Codex e Antigravity oferecem evidência oficial mais direta. Para delegação especializada dentro de uma sessão de código, os três têm mecanismos documentados.
- A capacidade de abrir um navegador não garante desempenho autônomo idêntico. Perfil, isolamento, permissões, gravações e aprovação de ações diferem.
- MCP é um protocolo de ferramentas, não um mecanismo de unificação de assinaturas. O servidor chamado pode ter sua própria autenticação e cobrança.

### Gaps

- Não há fonte primária comparando confiabilidade, número máximo prático de agentes paralelos, conflitos de merge ou qualidade do supervisor sob a mesma carga.
- “Context compaction” não é exposto de modo uniforme. Claude oferece compactação explícita; Antigravity documenta compactação automática em checkpoints; a mecânica interna do app Codex pode mudar. Isso não prova qualidade ou custo equivalentes.
- A geração de imagem no ecossistema Google e a disponibilidade do Nano Banana não provam, por si só, uma ferramenta de geração visual embutida em toda sessão do Antigravity.

## Uma assinatura de consumidor pode ser usada por CLI ou chamada de outro aplicativo?

### Takeaway

Sim, quando a própria fabricante oferece login da assinatura na CLI oficial: Claude Code, Codex CLI e `agy` são os caminhos corretos. Um orquestrador pode tecnicamente iniciar essas CLIs como processos, mas cada CLI conserva sua autenticação, cota e termos. Isso não autoriza transformar a assinatura em endpoint de API, compartilhar credenciais ou usar proxy não oficial. Chamadas por chave de API são cobradas separadamente, salvo créditos explicitamente incluídos no plano.

### Cited Findings

- O Claude Code permite login com conta Claude Pro/Max e também login separado de console/API; se `ANTHROPIC_API_KEY` estiver configurada, a execução usa faturamento de API, não a cota da assinatura ([Claude Code, getting started](https://docs.anthropic.com/en/docs/claude-code/getting-started); [Claude Help, usar com Pro/Max](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan)).
- A CLI do Claude expõe modo não interativo `claude -p`, seleção de modelo, limites de turnos, JSON e configuração MCP, permitindo automação sem converter a assinatura em API ([Claude Code, CLI usage](https://docs.anthropic.com/en/docs/claude-code/cli-usage)).
- A Codex CLI aceita “Sign in with ChatGPT”; o consumo conta na franquia do plano. A OpenAI diferencia isso do uso por chave de API, que segue tarifas padrão de API ([OpenAI Help, Codex no plano ChatGPT](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan); [OpenAI, Codex Pricing](https://learn.chatgpt.com/docs/pricing)).
- A OpenAI só estende a assinatura ChatGPT a aplicativos/sites participantes que implementem oficialmente “Sign in with ChatGPT”; um aplicativo arbitrário não herda automaticamente a assinatura ([OpenAI Help, “Using your ChatGPT plan in other apps and sites”](https://help.openai.com/en/articles/20001542-using-your-chatgpt-plan-in-other-apps-and-sites)).
- A Agents API da OpenAI é um produto de API separado, com cobrança e controles próprios, ainda que ofereça subagentes, sandboxes, MCP e compactação ([OpenAI Developers, Agents API](https://developers.openai.com/api/docs/guides/agents-api/overview)).
- A Antigravity CLI oficial autentica com Google Sign-In e usa keyring do sistema; esse é o caminho oficial de automação em terminal para a assinatura Google ([repositório oficial Antigravity CLI](https://github.com/google-antigravity/antigravity-cli)).
- A equipe do Google advertiu que ferramentas de terceiros e proxies que acessassem recursos/cotas do Antigravity podiam acionar bloqueios de conta; a orientação foi usar clientes oficiais ([Google Gemini CLI, comunicado oficial sobre ferramentas de terceiros](https://github.com/google-gemini/gemini-cli/discussions/20632)).
- O Google trata excedente por créditos de IA/preço de API, controlável por configuração; a assinatura não converte todo acesso programático em uso incluso ([Google One Help, Antigravity](https://support.google.com/googleone/answer/14534406)).

### Inferences

- Um fluxo tecnicamente defensável é: o orquestrador executa `claude -p`, `codex exec` ou `agy` instalados oficialmente; cada processo usa seu próprio login e exibe seu próprio status. Isso é diferente de capturar tokens, simular endpoints ou rotear requisições por proxy.
- “Antigravity chama Claude Code” pode ser descrito como automação de shell, não como integração comercial nativa. A cota consumida continua sendo a da conta Claude autenticada na CLI.
- MCP pode chamar uma ferramenta que, por sua vez, usa API; nesse caso, a cobrança segue as credenciais da ferramenta. Não existe “cota MCP” que transforme API em assinatura de consumidor.
- A conclusão jurídica depende dos termos vigentes, país e implementação. As fontes sustentam a separação técnica/comercial, não um parecer jurídico abrangente.

### Gaps

- Não foi localizada autorização oficial de Anthropic, OpenAI ou Google para expor uma CLI autenticada como serviço multiusuário ou proxy. Esse desenho deve ser tratado como fora do escopo de uma assinatura individual.
- A possibilidade técnica de iniciar um processo não assegura estabilidade de automação, suporte do fabricante ou permissão para contornar rate limits.
- Termos de serviço e políticas podem mudar; uma implantação pública/comercial exige revisão dos termos atuais por fornecedor.

## Por que a cota do Claude pode acabar tão rápido e qual é a orientação oficial?

### Takeaway

Claude Code reenvia a conversa inteira e o contexto do projeto a cada turno. Sessões longas, arquivos grandes, `CLAUDE.md` extenso, uso de Opus/Fable, research/web e múltiplas ferramentas aceleram o consumo. O comportamento é esperado pela mecânica publicada, não evidência automática de erro de faturamento. A recomendação oficial é separar tarefas, limpar/compactar contexto, referenciar arquivos e escolher o modelo adequado.

### Cited Findings

- Cada turno do Claude Code inclui a conversa acumulada, contexto do projeto como `CLAUDE.md` e arquivos lidos, além do novo prompt; por isso sessões longas crescem mais rápido ([Claude Help, “Models, usage, and limits in Claude Code”](https://support.claude.com/en/articles/14552983-models-usage-and-limits-in-claude-code)).
- A Anthropic recomenda `/clear` entre tarefas não relacionadas, `/compact` no meio de tarefas longas, `/context` para inspecionar a ocupação, referências a arquivos em vez de colagem e `CLAUDE.md` com cerca de 200 linhas ou menos ([Claude Help, “Models, usage, and limits in Claude Code”](https://support.claude.com/en/articles/14552983-models-usage-and-limits-in-claude-code)).
- A orientação oficial é usar Opus para raciocínio profundo, Sonnet para a maior parte da programação e Haiku para tarefas rápidas/mecânicas; a própria Anthropic sugere “planejar com Opus, executar com Sonnet” e documenta `opusplan` ([Claude Help, “Models, usage, and limits in Claude Code”](https://support.claude.com/en/articles/14552983-models-usage-and-limits-in-claude-code)).
- Mensagens longas, arquivos grandes, conversas extensas, pesquisa/web, modelo escolhido e Artifacts afetam o uso ([Claude Help, “Usage limit best practices”](https://support.claude.com/en/articles/9797557-usage-limit-best-practices)).
- Os limites de cinco horas e semanais são compartilhados por Claude web, Claude Desktop e Claude Code, portanto atividade em outra superfície reduz a franquia restante ([Claude Help, limites](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work); [Claude Help, Claude Code no plano](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan)).
- O Claude oferece gerenciamento automático de contexto com sumarização em certos fluxos de execução de código, mas isso não elimina o custo de conversas longas ([Claude Help, limites e contexto](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work)).

### Inferences

- A percepção de “poucos prompts” pode coexistir com alto consumo se cada prompt carregar uma sessão grande, vários arquivos e muitos tool calls.
- Subagentes e paralelismo podem multiplicar a atividade útil e também o consumo. Devem ser avaliados por tarefa concluída, não por mensagem visível ao usuário.
- Para investigar uma drenagem anormal, o teste mínimo deve iniciar em `/clear`, registrar `/context`, modelo, horário do início da janela, ferramentas usadas e status antes/depois.

### Gaps

- A Anthropic não publica uma fórmula para transformar tokens/tool calls em percentual da cota Pro. Não é possível auditar um caso individual apenas com o número de prompts.
- Sem logs de `/usage`, `/context`, modelo e horários, não é possível distinguir sessão pesada, compartilhamento entre superfícies, excedente pago ou anomalia da conta.

## Quais alegações da conversa e do whitepaper resistem à auditoria oficial?

### Takeaway

A arquitetura geral — usar um app como hub e chamar CLIs oficiais separadamente — é tecnicamente plausível. O material, porém, mistura recursos reais com limites exatos não publicados, rankings de terceiros sem ficha de teste e generalizações como “nunca trunca”, “nunca bate limite” e “sem surpresas de API”. Essas frases não devem entrar no relatório como fatos.

### Cited Findings

| Alegação encontrada | Veredito | Base oficial / correção necessária |
|---|---|---|
| “Antigravity pode ser o hub principal sem IDE.” | Confirmada, com ressalva | App e CLI autônomos são oficiais; a superioridade como hub é uma conclusão de teste, não fato do fabricante ([Antigravity 2.0](https://antigravity.google/product/antigravity-2/); [Antigravity CLI](https://github.com/google-antigravity/antigravity-cli)). |
| “Antigravity é um IDE baseado em VS Code.” | Desatualizada/incompleta | O produto atual oferece app, CLI e extensões para vários IDEs ([Antigravity Docs](https://antigravity.google/docs/models)). |
| “Antigravity tem Claude Opus/Sonnet e GPT-OSS 120B.” | Confirmada para a lista atual, acesso varia | O seletor oficial lista esses modelos por plano ([Antigravity Models](https://antigravity.google/docs/models)). |
| “Antigravity reseta a cada 5 horas.” | Parcial | A UI documentada mostra limite de 5 horas e semanal; quantidades são dinâmicas/não publicadas ([Antigravity Models](https://antigravity.google/docs/models); [Antigravity Pricing](https://antigravity.google/pricing)). |
| “O Pro rende 5–6 sessões pesadas.” | Não verificável oficialmente | Google não publica esse total; precisa de log experimental com conta, modelo, contexto e data. |
| “Claude Pro dá 45 mensagens” ou “10–40 prompts de Claude Code”. | Desatualizada como regra atual | As páginas atuais descrevem limites dinâmicos de 5 horas e semanais; não prometem contagem fixa ([Claude Pricing](https://claude.com/pricing); [Claude Help, limites](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work)). |
| “Claude Opus 5.5 é padrão silencioso no Pro/versão 2.1.280.” | Não verificada | A documentação manda usar `/model` como fonte de verdade; nenhuma fonte oficial consultada confirma esse padrão ([Claude model configuration](https://support.claude.com/en/articles/11940350-claude-code-model-configuration)). |
| “Claude nunca trunca até 1M.” | Falsa como generalização | “Até 1M” varia por modelo; contexto, saída, ferramentas e cotas são limites distintos ([Claude Pricing](https://claude.com/pricing); [Claude context window](https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans)). |
| “Codex Plus entrega 15–150 GPT-6 Sol ou até 3.000 Luna a cada 5h.” | Essencialmente correta, mas é estimativa | A faixa atual é 15–150 para GPT-6 Sol e 350–3.000 para Luna; GPT-6.1 Sol é 15–160. O uso real varia e há cota semanal ([Codex Pricing](https://learn.chatgpt.com/docs/pricing)). |
| “Codex nunca atinge o limite.” | Falsa/não sustentada | A OpenAI documenta janelas de 5 horas, semanais, créditos e resets pagos ([OpenAI Help, resets](https://help.openai.com/en/articles/20001498-how-resets-work-in-codex); [paid resets](https://help.openai.com/en/articles/20001507-paid-weekly-work-and-codex-rate-limit-resets)). |
| “MCP permite gastar a assinatura de outro fornecedor.” | Falsa | MCP conecta ferramentas; a cobrança depende da autenticação da CLI/servidor. API permanece separada ([Anthropic MCP](https://docs.anthropic.com/en/docs/mcp); [OpenAI MCP](https://developers.openai.com/learn/docs-mcp)). |
| “Antigravity pode chamar `claude -p` e `codex exec`.” | Tecnicamente plausível, não integração nativa comprovada | As duas CLIs têm modos oficiais de automação e login próprio; o launcher não transfere a assinatura ([Claude CLI](https://docs.anthropic.com/en/docs/claude-code/cli-usage); [OpenAI, Codex como plataforma](https://developers.openai.com/blog/codex-as-a-platform); [Codex com ChatGPT](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan)). |
| “Uso de proxy/bridge preserva a cota Google.” | Arriscada/contrariada | O Google alertou que ferramentas/proxies de terceiros para recursos Antigravity podem causar bloqueios ([comunicado oficial](https://github.com/google-gemini/gemini-cli/discussions/20632)). |
| “O fluxo é 100% por assinatura, sem surpresa de API.” | Falsa como garantia | Os três ecossistemas têm API/overage/créditos separados ou opcionais; variáveis de ambiente e toggles podem mudar a fonte de cobrança ([Claude Code no plano](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan); [Codex Pricing](https://learn.chatgpt.com/docs/pricing); [Google One Help](https://support.google.com/googleone/answer/14534406)). |
| “GPT Image 2.5 e Nano Banana 2/2.1 existem.” | Confirmada | Os nomes/produtos são oficiais ([OpenAI Images 2.5](https://openai.com/index/introducing-chatgpt-images-2-5/); [Google Nano Banana 2](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-nano-banana-2/); [Nano Banana 2.1](https://ai.google.dev/gemini-api/docs/models/gemini-nano-banana-2.1)). |
| “GPT Image 2.5 é nº 1 no Artificial Analysis.” | Fora do escopo oficial / requer fonte externa | A OpenAI confirma o produto, não esse ranking ([OpenAI Images 2.5](https://openai.com/index/introducing-chatgpt-images-2-5/)). |
| “SWE-bench 97%, 89,9%; Terminal-Bench 70,6%; tool-calling 36,3%; 4× mais eficiente.” | Não verificável com as fontes primárias reunidas | Números precisam de URL do leaderboard/paper, data, variante, metodologia, pass@k, ferramentas e reprodução. Não devem ser atribuídos ao plano/app sem isso. |
| “Consenso do Reddit confirma o ranking.” | Evidência anedótica, não fato oficial | Deve ser apresentado como amostra qualitativa com método de coleta, período e vieses; não valida capacidade oficial. |
| “Alocação ideal 80/15/5 entre produtos.” | Hipótese de planejamento | Não existe recomendação oficial equivalente; precisa de teste de carga/custo do caso de uso. |
| “Nimbalyst/Superset provam o melhor fluxo.” | Não auditada nesta camada | São alegações sobre terceiros e exigem fontes originais/casos reproduzíveis, não documentação de fabricante. |

### Inferences

- O relatório final deve separar três níveis: (1) capacidade oficial documentada; (2) teste reproduzível próprio; (3) opinião/relato de comunidade. O whitepaper atual cruza esses níveis sem rotulagem suficiente.
- A recomendação “Antigravity como hub” pode permanecer como hipótese ou resultado de experimento próprio, desde que não seja apresentada como conclusão oficial ou universal.
- Rankings sem data se deterioram rapidamente; a versão do modelo, tier de raciocínio, harness e ferramentas devem acompanhar todo número.

### Gaps

- Esta nota não valida benchmarks de terceiros, posts do Reddit, vídeos ou casos de uso de Nimbalyst/Superset. Esses itens precisam de trilha de pesquisa separada.
- Não foram fornecidos logs brutos dos testes mencionados na conversa; portanto, resultados de truncamento, sessões e taxa de sucesso não são reproduzíveis aqui.
- Uma alegação marcada “não verificada” não é necessariamente falsa; significa que não há sustentação primária suficiente para publicá-la como fato.

## Qual configuração é defensável para o fluxo sem IDE e sem cobrança acidental?

### Takeaway

A configuração mais segura é manter os três clientes oficiais separados e deixar um deles apenas coordenar processos: Antigravity app/`agy`, Codex app/CLI com “Sign in with ChatGPT” e Claude Code com login Claude. Desabilite excedente/créditos quando o objetivo for custo estritamente fixo, remova chaves de API do ambiente das CLIs de assinatura e registre o status de uso antes/depois dos testes. A escolha do hub deve ser decidida pelo experimento, não por uma promessa de fabricante.

### Cited Findings

- Claude Code pode usar assinatura ou API conforme a autenticação/configuração, e o comando `/model` mostra a oferta disponível ([Claude Help, Claude Code no plano](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan); [Claude model configuration](https://support.claude.com/en/articles/11940350-claude-code-model-configuration)).
- Codex mostra consumo pelo dashboard e pelo comando `/status`; a carga varia com modelo, execução, contexto, raciocínio, velocidade e ferramentas ([OpenAI Help, Codex no plano](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan)).
- O Google permite definir excedente como “Never” para evitar consumo automático de créditos adicionais ([Google One Help, Antigravity](https://support.google.com/googleone/answer/14534406)).
- O uso de clientes oficiais evita o padrão de proxy de terceiros explicitamente associado pelo Google a risco de bloqueio ([Google, comunicado sobre ferramentas de terceiros](https://github.com/google-gemini/gemini-cli/discussions/20632)).

### Inferences

- Protocolo mínimo recomendado para o benchmark: nova sessão/contexto; mesmo repositório/commit; prompt idêntico; mesmo limite de tempo; modelo e esforço registrados; logs de tool calls; captura das barras de 5 horas e semanais; verificação por testes; revisão cega da saída.
- Para reduzir custo de Claude: planejar em Opus apenas quando necessário, executar em Sonnet, usar Haiku para mecânica, limpar entre tarefas e compactar antes de a sessão crescer demais.
- Para tarefas paralelas: worktrees por agente e integração final em uma branch separada reduzem colisões. O ganho precisa ser comparado ao consumo adicional de agentes simultâneos.
- Um controle “sem API” deve auditar variáveis como `ANTHROPIC_API_KEY` e `OPENAI_API_KEY`, toggles de excedente e plugins/MCPs que possuam chaves próprias, sem registrar os valores secretos.

### Gaps

- Nenhuma fonte oficial garante custo mensal totalmente fixo se overage/créditos estiverem habilitados ou se ferramentas externas possuírem suas próprias chaves.
- A decisão final do hub ainda precisa dos resultados do benchmark próprio e da camada de evidências externas; esta nota estabelece apenas o piso factual oficial.

## Qual é a bibliografia primária usada nesta nota?

### Takeaway

A bibliografia abaixo é o conjunto mínimo de páginas primárias que sustenta a auditoria. Páginas de ajuda e pricing são vivas; para publicação, recomenda-se arquivar PDF/captura com data de acesso e repetir a checagem imediatamente antes de postar no LinkedIn.

### Cited Findings

| Organização | Documento oficial | Data publicada/atualizada quando exibida | Acesso |
|---|---|---:|---:|
| Anthropic | [Claude Pricing](https://claude.com/pricing) | página viva | 2026-10-31 |
| Anthropic | [How do usage and length limits work?](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work) | página viva | 2026-10-31 |
| Anthropic | [Use Claude Code with your Pro or Max plan](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan) | página viva | 2026-10-31 |
| Anthropic | [Models, usage, and limits in Claude Code](https://support.claude.com/en/articles/14552983-models-usage-and-limits-in-claude-code) | página viva | 2026-10-31 |
| Anthropic | [Claude Code model configuration](https://support.claude.com/en/articles/11940350-claude-code-model-configuration) | página viva | 2026-10-31 |
| Anthropic | [Usage limit best practices](https://support.claude.com/en/articles/9797557-usage-limit-best-practices) | página viva | 2026-10-31 |
| Anthropic | [Claude Code CLI usage](https://docs.anthropic.com/en/docs/claude-code/cli-usage) | página viva | 2026-10-31 |
| Anthropic | [Model Context Protocol](https://docs.anthropic.com/en/docs/mcp) | página viva | 2026-10-31 |
| OpenAI | [Codex Pricing](https://learn.chatgpt.com/docs/pricing) | página viva | 2026-10-31 |
| OpenAI | [ChatGPT Pricing](https://chatgpt.com/pricing/) | página viva | 2026-10-31 |
| OpenAI | [Using Codex with your ChatGPT plan](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan) | página viva | 2026-10-31 |
| OpenAI | [How resets work in Codex](https://help.openai.com/en/articles/20001498-how-resets-work-in-codex) | página viva | 2026-10-31 |
| OpenAI | [Using your ChatGPT plan in other apps and sites](https://help.openai.com/en/articles/20001542-using-your-chatgpt-plan-in-other-apps-and-sites) | página viva | 2026-10-31 |
| OpenAI | [Introducing the Codex app](https://openai.com/index/introducing-the-codex-app/) | 2026-02-02; atualização Windows 2026-03-04 | 2026-10-31 |
| OpenAI | [Codex for almost everything](https://openai.com/index/codex-for-almost-everything/) | página de anúncio | 2026-10-31 |
| OpenAI | [Codex as a platform: build on the open agent harness](https://developers.openai.com/blog/codex-as-a-platform) | 2026 | 2026-10-31 |
| OpenAI | [Introducing ChatGPT Images 2.5](https://openai.com/index/introducing-chatgpt-images-2-5/) | 2026-09-08 | 2026-10-31 |
| Google | [Antigravity Pricing](https://antigravity.google/pricing) | página viva | 2026-10-31 |
| Google | [Antigravity 2.0](https://antigravity.google/product/antigravity-2/) | página viva | 2026-10-31 |
| Google | [Antigravity Docs: Choose a model](https://antigravity.google/docs/models) | página viva | 2026-10-31 |
| Google | [Antigravity Features](https://antigravity.google/docs/features) | página viva | 2026-10-31 |
| Google | [Antigravity browser](https://antigravity.google/docs/commands/browser) | página viva | 2026-10-31 |
| Google | [Antigravity CLI](https://github.com/google-antigravity/antigravity-cli) | repositório vivo | 2026-10-31 |
| Google | [Google One Help: Antigravity](https://support.google.com/googleone/answer/14534406) | página viva | 2026-10-31 |
| Google | [Depreciação do Gemini Code Assist for individuals](https://developers.google.com/gemini-code-assist/docs/deprecations/code-assist-individuals) | 2026 | 2026-10-31 |
| Google | [Nano Banana 2](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-nano-banana-2/) | 2026-02-26 | 2026-10-31 |
| Google | [Nano Banana 2.1](https://ai.google.dev/gemini-api/docs/models/gemini-nano-banana-2.1) | página viva | 2026-10-31 |

### Inferences

- Como pricing e limites são documentos vivos, a data de acesso faz parte da evidência. Uma publicação posterior deve dizer “situação em 31/10/2026” e não sugerir permanência.
- Para afirmações de desempenho, esta bibliografia precisa ser complementada por papers/leaderboards originais e logs próprios; documentação de fabricante não substitui benchmark.

### Gaps

- Algumas páginas vivas não exibem claramente data de atualização. Nesses casos, a data de acesso é o único marcador temporal confiável disponível.
- A preservação de versões arquivadas não foi executada nesta nota; é recomendada antes da publicação final.

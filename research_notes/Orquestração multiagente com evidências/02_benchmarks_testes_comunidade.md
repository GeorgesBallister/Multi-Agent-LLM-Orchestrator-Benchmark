# Benchmarks, testes independentes e evidência de comunidade

Recorte temporal: fontes verificadas em **31 de outubro de 2026**. Esta nota compara Claude/Claude Code, OpenAI Codex/ChatGPT e Google Antigravity/Gemini sem misturar quatro classes de evidência: benchmark primário reproduzível, agregador/ranking, experimento independente com artefatos e relato anedótico de comunidade. Números de snapshots dinâmicos devem ser republicados com a data de captura.

## Como interpretar rankings sem produzir uma falsa tabela universal

### Takeaway

Não existe um placar único que responda qual aplicativo é “melhor” para programação agêntica. SWE-bench mede resolução de issues sob um *scaffold*; Terminal-Bench mede tarefas executadas em terminal; LLM Stats agrega evidências heterogêneas; Artificial Analysis roda avaliações com configuração própria; OpenRouter mede tráfego, não qualidade. A comparação defensável preserva versão, *harness*, esforço de raciocínio, número de tarefas, repetições, custo e data.

### Cited Findings

**Hierarquia usada nesta pesquisa**

1. **Nível A — benchmark primário com tarefas e métrica publicadas.** O [SWE-bench oficial](https://www.swebench.com/) informa 2.294 instâncias de issues reais em 12 repositórios Python no conjunto original e 500 instâncias revisadas por humanos no SWE-bench Verified. Na visualização “Bash Only”, todos os modelos usam o mesmo ambiente mini-SWE-agent, e o resultado é percentual de instâncias resolvidas. Isso é evidência comparável **dentro daquela configuração**, não um atributo permanente do modelo.
2. **Nível B — laboratório/agregador com metodologia declarada.** A [metodologia v5.0 da Artificial Analysis](https://artificialanalysis.ai/methodology/intelligence-benchmarking) combina nove avaliações e quatro categorias ponderadas igualmente — Knowledge Work, Coding, Science e General —, mas também alerta que implementações distintas podem não ser diretamente comparáveis. O [LLM Stats Research v3.1](https://llm-stats.com/research) usa ratings relativos com incerteza, combina avaliação independente e evidência externa e diz explicitamente que observações ausentes não equivalem a falha.
3. **Nível C — experimento independente auditável.** Um teste de usuário sobe de valor quando publica prompts, versões, repositório, worktrees, testes executáveis, custos e resultados brutos. Ainda assim, poucas tarefas de um ou dois repositórios não sustentam generalização para toda engenharia de software.
4. **Nível D — relato de comunidade.** Reddit, YouTube e blogs ajudam a descobrir modos de falha, bugs de quota e workflows. Sem protocolo, logs e replicação, são evidência qualitativa, não estimativa de incidência nem “consenso”.

**O que cada ranking mede**

| Fonte | Unidade real | Pode sustentar | Não pode sustentar |
|---|---|---|---|
| [SWE-bench](https://www.swebench.com/) | Issues resolvidas sob dataset e agente especificados | Comparação dentro da mesma variante/harness | “Modelo X resolve 97% de qualquer trabalho de software” |
| [Artificial Analysis Intelligence](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | Índice composto e subavaliações sob sua infraestrutura | Relação qualidade/custo e desempenho por avaliação na data | Comparar um score de Terminal-Bench com um score SWE-bench como se fossem a mesma escala |
| [LLM Stats](https://llm-stats.com/research) | Rating relativo conservador/TrueSkill sobre evidências heterogêneas | Triangulação ampla com incerteza | Interpretar 60,2 como 60,2% de acerto ou garantia de um app específico |
| [OpenRouter Rankings](https://openrouter.ai/rankings) | Tokens de prompt + conclusão do tráfego público, em buckets diários | Popularidade/uso dentro do marketplace OpenRouter | Qualidade, número de usuários, receita ou proporção ideal de roteamento |

O [OpenRouter explica no próprio ranking](https://openrouter.ai/rankings) que requisições privadas são excluídas e que “top models” usa volume de tokens, enquanto *market share* usa contagem de requisições. Modelos mais verbosos e tokenizadores distintos podem, portanto, aparecer maiores sem atender mais pessoas nem produzir melhor software.

### Inferences

- Uma tabela publicável deve ter colunas de **fonte, versão, data, modelo exato, esforço, scaffold, tarefas, repetições, métrica e custo**. Se uma dessas informações faltar, a incerteza precisa aparecer na legenda.
- Scores agregados servem melhor como triagem. A decisão operacional deve ser confirmada com um conjunto privado de tarefas do próprio repositório, porque os aplicativos adicionam ferramentas, compaction, permissões e coordenação que o benchmark de modelo pode não medir.
- OpenRouter é uma fonte adequada para falar de demanda relativa no seu próprio ecossistema; não é base para afirmar um split de produção universal, como “80% Claude, 15% Codex, 5% Gemini”.

### Gaps

- A página dinâmica do OpenRouter não oferece, no recorte consultado, um snapshot imutável com hash do dataset. Para publicação, deve-se arquivar data, filtros e captura.
- LLM Stats não publica todos os detalhes operacionais internos da avaliação; o próprio site informa essa limitação. O rating é útil para triangulação, não para reprodução integral.
- Não foi localizado um benchmark primário que compare, de ponta a ponta e sob o mesmo protocolo, **os aplicativos** Claude Code, Codex e Antigravity com suas configurações atuais, quotas de assinatura e recursos de orquestração.

## O que os benchmarks atuais mostram sobre código, terminal, tarefas longas, imagem, latência e tokens

### Takeaway

No snapshot de 31/10/2026, Claude Opus 5.5, GPT-6 Astra e Gemini 4 Carbon ocupam o mesmo pelotão de fronteira em agregadores, com mudanças de liderança de poucos pontos conforme modelo novo, esforço e avaliação. Claude lidera FrontierCode 2.0 no recorte publicado; GPT-6 Astra lidera Terminal-Bench-Science; Gemini Carbon lidera o índice ao vivo capturado. Isso não forma uma ordem total. O achado mais estável é que esforço e custo mudam muito o resultado, e que tarefas agênticas longas consomem a maioria dos tokens da avaliação.

### Cited Findings

**Engenharia de software e terminal**

- Na [metodologia Artificial Analysis](https://artificialanalysis.ai/methodology/intelligence-benchmarking), Terminal-Bench 4.0 tem 66 tarefas, roda com mini-swe-agent, permite até 500 passos, mantém o transcript completo sem compaction e calcula pass@1 pela média de três repetições; cada tarefa só passa se todos os testes passarem. Isso mede execução em terminal sob um agente específico, não a interface de assinatura do Claude Code, Codex ou Antigravity.
- O [FrontierCode 2.0](https://artificialanalysis.ai/methodology/intelligence-benchmarking) usa 132 tarefas privadas, três tentativas por tarefa, testes ocultos/rubricas e até 500 turnos. No artigo de lançamento do [Intelligence Index v5.0](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5/), Claude Opus 5.5 no esforço máximo marcou 46%, enquanto GPT-6 Astra, GPT-6.1 Sol Terra e Claude Sonnet 5.5 ficaram em 42%. A diferença é interna a esse protocolo e snapshot.
- Terminal-Bench-Science tem 70 tarefas e três repetições, também com critério estrito de todos os testes passarem, segundo a [mesma metodologia](https://artificialanalysis.ai/methodology/intelligence-benchmarking). No [artigo v5.0](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5/), GPT-6 Astra marcou 63%, Claude Opus 5.5 59% e GPT-6.1 Sol 58%.
- O histórico oficial do [Terminal-Bench](https://www.tbench.ai/news) lista versões 2.0, 2.1, 3.0 e 4.0, com mudanças no benchmark. Uma [atualização de integridade](https://www.tbench.ai/news/leaderboard-integrity-update) documenta problemas de *reward hacking* e alterações de política. Logo, “Terminal-Bench” sem versão, data e harness é uma citação incompleta.

**Agregadores e volatilidade do snapshot**

- No [leaderboard ao vivo da Artificial Analysis](https://artificialanalysis.ai/leaderboards/models), capturado em 31/10/2026, Gemini 4 Carbon High aparecia com Intelligence Index 59, Claude Opus 5.5 max com 58, Claude Opus 5.5 xhigh com 57 e GPT-6 Astra max com 57. O [artigo oficial v5.0](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5/) publicado poucos dias antes ainda descrevia Opus 5.5 em primeiro, com 58, seguido de Astra 57 e Sol 55. A mudança mostra por que ranking dinâmico precisa de data.
- No [LLM Stats Benchmarks](https://llm-stats.com/benchmarks), verificado em 31/10/2026, o composite geral conservador mostrava Claude Opus 5.5 em 60,2, Gemini 4 Carbon em 59,0, Claude Sonnet 5.5 em 57,9, GPT-6 Astra em 57,5, Gemini 4 Argon em 54,4 e GPT-6.1 Sol em 53,3. Conforme a [metodologia](https://llm-stats.com/research), esses valores são ratings relativos com incerteza, não percentuais de acerto.
- O [leaderboard detalhado do LLM Stats](https://llm-stats.com/leaderboards/llm-leaderboard) separa categorias; por exemplo, no snapshot consultado, Opus 5.5 tinha 60,2 geral, 58,8 em reasoning e 50,9 em coding; Sonnet 5.5 tinha 57,9 geral, 56,2 em reasoning, 48,5 em coding e 36,2 em tools. O valor “36,2/36,3 em tools” é uma pontuação composta de categoria do site, não “36,3% de tool calling correto”.

**Custo e eficiência de tokens**

- No [artigo v5.0 da Artificial Analysis](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5/), Opus 5.5 max custou US$ 10,04 por tarefa do índice, Astra max US$ 6,24 e Sol max US$ 1,27; Sol ficou quatro pontos atrás de Opus por cerca de um oitavo do custo. Esses custos pertencem à mistura de tarefas e preços daquele teste, não a qualquer projeto real.
- O mesmo [artigo](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5/) relata aumento da mediana de tokens de saída por tarefa de 35 mil para 59 mil na atualização. Avaliações agênticas receberam 55% do peso do índice, mas responderam por aproximadamente 90% dos tokens de saída. Isso sustenta que qualidade agêntica de fronteira pode ser intensiva em tokens; não sustenta uma razão universal “Claude é 3,2× mais eficiente”.
- A configuração de esforço altera simultaneamente score, latência e custo no [leaderboard da Artificial Analysis](https://artificialanalysis.ai/leaderboards/models). Portanto, comparar “max” de um modelo com “low/default” de outro sem explicitar isso é metodologicamente fraco.

**Imagem e multimodal**

- A [metodologia de imagem da Artificial Analysis](https://artificialanalysis.ai/methodology/image) usa preferência humana cega em pares, estima Elo por Bradley–Terry, renova prompts mensalmente, gera uma imagem por prompt em configuração padrão e normaliza para 1024×1024. O resultado mede preferência visual agregada, não fidelidade de edição de um asset específico nem capacidade de implementar UI.
- No snapshot de 31/10/2026 do [leaderboard text-to-image](https://artificialanalysis.ai/image/leaderboard/text-to-image), GPT Image 2.5 Sunburst max aparecia em primeiro com Elo 1222±10 e 13.014 amostras; Nano Banana 2.1 aparecia em quarto, com faixa de rank 3–6, Elo 1176±12 e 6.210 amostras. No [leaderboard de edição](https://artificialanalysis.ai/image/leaderboard/editing), Sunburst estava em primeiro com 1199±11 e 18.250 amostras, e Nano Banana 2.1 na faixa 4–7 com 1151±13 e 6.868 amostras.
- Esses rankings de imagem não avaliam o produto Antigravity nem o fluxo completo de assets. Eles apenas situam modelos de geração/edição sob preferência humana cega.

**Latência**

- Artificial Analysis publica medidas de velocidade e latência junto aos modelos no [leaderboard ao vivo](https://artificialanalysis.ai/leaderboards/models), mas esses valores variam por provedor, endpoint, esforço e data. Atribuir “308 tokens/s” ou um tempo de primeira resposta a um modelo sem registrar endpoint e snapshot não é reproduzível.

### Inferences

- O melhor modelo de software no FrontierCode não é automaticamente o melhor para ciência em terminal, imagem ou custo. A seleção deve ser multidimensional.
- Para longos horizontes, uma métrica operacional melhor que “score bruto” é **tarefas aceitas por real e por hora**, incluindo falhas, correções humanas e consumo de quota. Nenhuma das fontes agregadas mede tudo isso para os três aplicativos.
- A proximidade entre modelos no topo e a volatilidade do snapshot favorecem um roteador por tarefa e um benchmark privado recorrente, em vez de uma hierarquia fixa do tipo “Claude > Codex > Gemini”.

### Gaps

- Não foi encontrada, nas fontes primárias consultadas, confirmação para SWE-bench Verified de 97% para Opus 5.5, 94,2% para Sonnet, 68,8% para Codex e 64,5% para Gemini sob o mesmo harness.
- Não foi encontrada uma fonte primária suficiente para os números “SWE-bench Pro 89,9/84,1/64,6”, “Terminal-Bench 4.0 70,6 para Sonnet”, “DeepSWE v1.1” como benchmark comparativo central, “eficiência 3,2–4,2×” ou “preferência cega de engenharia 67%” apresentados no rascunho Argon.
- Não há medido aqui um benchmark comum de contexto longo real, uso de browser e coordenação multiagente para os três aplicativos. Janelas nominais de contexto não medem retenção útil após compaction.

## O que os testes independentes publicados por usuários realmente acrescentam

### Takeaway

Os melhores testes comunitários localizados publicam tarefas, worktrees ou repositórios e executam testes reais. Eles sugerem que o resultado depende do tamanho da tarefa, handoff entre modelos, disciplina de validação e repositório. Nenhum tem amostra representativa suficiente para declarar vencedor universal. Seu maior valor é fornecer protocolos que podem ser reproduzidos no repositório do leitor.

### Cited Findings

| Experimento | Protocolo e resultado reportado | Força | Limite |
|---|---|---|---|
| [Plan with Opus, Execute with Codex](https://www.reddit.com/r/ClaudeAI/comments/1sdk2sj/i_benchmarked_plan_with_opus_execute_with_codex/) | Três tarefas reais em worktrees isoladas: 80 LOC custaram US$0,33 com Opus e US$0,53 no híbrido; 400 LOC, US$0,68 vs US$0,74; 1.060 LOC, US$0,86 vs US$0,78. O autor estimou crossover em ~600 LOC e identificou cache reads/saída copiada ao contexto como custo relevante. | Números por tarefa, isolamento e custos expostos. | n=3; linhas de código não são medida universal de complexidade; a fronteira de 600 LOC não deve ser generalizada. |
| [Codex vs Claude Code, seis projetos](https://www.reddit.com/r/codex/comments/1tbkmc3/codex_vs_claude_code_i_ran_a_6project_benchmark/) e [repositório público](https://github.com/AdrielRod/codex-vs-claude-code) | Três rodadas; cada modelo propôs desafios, implementou, fez auto/cross-review; houve testes de runtime e revisão humana. Codex venceu as rodadas 1 e 2, Claude a 3. | Artefatos e testes podem ser auditados; avalia comportamento de construir/testar/revisar. | Seis projetos bespoke; modelos também participam da definição/revisão; o placar 2×1 não estima taxa populacional. |
| [Benchmark em produção Rails](https://www.reddit.com/r/ClaudeAI/comments/1qxr7vs/gpt53_codex_vs_opus_46_we_benchmarked_both_on_our/) | O autor descreve evals derivados de PRs reais com graders múltiplos; reporta aproximadamente 0,70 de qualidade por menos de US$1/ticket para Codex e ~0,61 por cerca de US$5/ticket para Opus. | Tarefas derivadas de trabalho real e tentativa de medir custo/qualidade. | Dataset, rubrica e infraestrutura são específicos; números do autor não equivalem a benchmark independente revisado. |
| [56 tarefas reais em dois projetos OSS](https://www.reddit.com/r/ClaudeCode/comments/1t0xrad/gpt55_vs_gpt54_vs_opus_47_on_56_real_coding_tasks/) | Tarefas foram derivadas de commits aceitos e rodadas com os agentes nativos e configurações padrão. | Amostra maior e ground truth de commits reais. | Dois repositórios; troca simultaneamente modelo e harness, portanto não isola o efeito do modelo. |

O teste híbrido de três tarefas também evidencia custo de coordenação: plano, stdout e revisão adicionam contexto. Esse é um mecanismo plausível e mensurável no próprio log; ele não prova que handoff seja sempre pior ou melhor.

Para YouTube e blogs, o critério mínimo de citação deve ser: prompt completo, versão/data, estado inicial idêntico, repositório ou fixture, wall-clock, tokens/custo, testes automáticos, falhas incluídas e artefatos brutos. Nenhum vídeo ou blog adicional localizado superou os experimentos acima em transparência suficiente para receber peso quantitativo.

### Inferences

- O crossover econômico entre um agente único e uma dupla planejador→executor depende mais de volume de contexto, cache e número de turnos que de linhas de código isoladamente.
- Worktrees são uma boa unidade experimental: permitem iniciar candidatos da mesma base, executar testes e comparar diffs. Ainda é preciso controlar dependências, portas, bancos e arquivos externos.
- O protocolo recomendado para o projeto é selecionar 20–50 tarefas fechadas e estratificadas (bug, feature, refactor, browser/UI, imagem, terminal), rodar pelo menos três repetições por combinação app/modelo e registrar aceitação humana cega, testes, wall-clock, tokens, custo e quota consumida.

### Gaps

- Os posts não fornecem uma distribuição representativa de organizações, linguagens e tamanhos de repositório.
- Os experimentos em interfaces de assinatura raramente expõem tokens reais e preço marginal, porque o produto mostra percentuais de quota em vez de billing por chamada.
- Não foi achado teste independente, com repositório e protocolo equivalente, incluindo Antigravity ao lado de Claude Code e Codex nas mesmas tarefas.

## O que Reddit e relatos de campo dizem sobre quotas, subagentes, sessões longas e escolha de aplicativo

### Takeaway

Reddit não mostra consenso; mostra uma distribuição de experiências incompatíveis. Há relatos de consumo abrupto tanto em Claude Code quanto em Codex, além de experiências positivas e negativas com Antigravity. O relato mais tecnicamente útil identifica um possível *cache miss* ao retomar subagente finalizado e inclui contagens de tokens e razão `messages_changed`. Mesmo esse caso continua sendo uma observação de usuário, dependente de versão, até replicação/acknowledgement oficial.

### Cited Findings

**Quota e paralelismo no Claude Code**

- Em [“Quota draining? Claude Code re-bills a finished sub-agent’s whole context”](https://www.reddit.com/r/ClaudeAI/comments/1whvqcl/quota_draining_claude_code_rebills_a_finished/), publicado aproximadamente um mês antes do recorte, o autor inspecionou transcripts e afirma que a primeira mensagem após dois subagentes terminarem reescreveu 243 mil e 399 mil tokens no cache e leu apenas cerca de 16 mil; mensagens enquanto os agentes ainda rodavam teriam custado 2–4 mil tokens. O log teria marcado `messages_changed`; o autor informou ter enviado o caso à Anthropic. Isso é uma hipótese de bug com mecanismo verificável, não prova de que todo subagente multiplica consumo dessa forma.
- O mesmo relato cita Claude Code 2.1.269/2.1.273 no contexto da investigação. Qualquer reprodução precisa fixar versão, janela de cache, momento da mensagem e status do subagente.

**Quota no Codex — reclamações e contraexemplos**

- Em [“What on earth happened to usage limits?”](https://www.reddit.com/r/codex/comments/1w9up47/what_on_earth_happened_to_usage_limits/), um usuário relata que duas tarefas simples consumiram a janela de cinco horas em 10–15 minutos; as respostas misturam experiências distintas e hipóteses de bug/variação de conta.
- Em [“5 hour limits are back for Plus users”](https://www.reddit.com/r/codex/comments/1vy3yhu/5_hour_limits_are_back_for_plus_users/), os relatos também divergem. Um comentário compara o mesmo prompt/repo e diz ter usado 40% em Opus contra 78% em Sol em cerca de 38/35 minutos; não há protocolo ou logs suficientes para tratar essa razão como benchmark.
- Em [“Codex on ChatGPT Plus burned 75% of 5h in 20 mins”](https://www.reddit.com/r/codex/comments/1sgzy01/codex_on_chatgpt_plus_burned_75_of_5h_in_20_mins/), o autor atribui 75% de uma janela a um refactor de 20 minutos. Em sentido oposto, um relato de 25/10/2026, [“Codex usage is horrible compared to Claude Code”](https://www.reddit.com/r/ClaudeCode/comments/1xey6r4/codex_usage_is_horrible_compared_to_claude_code/), afirma que 25 tarefas em Claude consumiram cerca de 20% da janela de cinco horas, enquanto uma tentativa Codex falhou e consumiu 30–35% da quota semanal. Os dois são anedotas e impedem a narrativa simplista de que um produto sempre tem quota superior.

**Antigravity, confiabilidade e escolha do app**

- Na discussão [“Codex vs Claude Code vs Antigravity”](https://www.reddit.com/r/codex/comments/1s1btfx/codex_vs_claude_code_vs_antigravity_whats_your/), aberta cerca de sete meses antes do recorte, o autor descreve Claude como forte mas caro/limitado, Codex como mais autônomo e Antigravity como inconsistente. Comentários variam: alguns preferem planejar com Claude e executar com Codex; outros usam Gemini apenas para perguntas; há também relatos de Antigravity resolvendo problemas que os demais não resolveram. A thread demonstra heterogeneidade, não ranking.
- Em [relato de migração de Claude/Codex para Antigravity](https://www.reddit.com/r/google_antigravity/comments/1s337wg/experience_coming_from_claude_and_codex/), o autor elogia contexto de monorepo, mas relata regressões em 14 de 15 branches testadas. Sem estado inicial, testes e logs, o número descreve a experiência daquele usuário.
- O [megathread de comparação do r/codex](https://www.reddit.com/r/codex/comments/1x3k1li/codex_comparison_megathread/) trata explicitamente comparações como dependentes da tarefa e incentiva avaliação no próprio repositório.

**Sessões longas, IDE e worktrees**

- A evidência comunitária mais consistente é processual: contextos longos acumulam stdout/cache, handoffs perdem informação e worktrees ajudam a isolar implementações. O [teste Opus→Codex](https://www.reddit.com/r/ClaudeAI/comments/1sdk2sj/i_benchmarked_plan_with_opus_execute_with_codex/) quantifica um caso de stdout inflando custo; o [benchmark de seis projetos](https://www.reddit.com/r/codex/comments/1tbkmc3/codex_vs_claude_code_i_ran_a_6project_benchmark/) publica implementações e runtime tests; as ferramentas Nimbalyst e Paradev usam worktrees como mecanismo de isolamento, conforme seus repositórios oficiais.
- Não foi localizada evidência quantitativa suficiente de que um fluxo “sem IDE” seja superior. O que aparece são preferências por terminal, interfaces visuais ou browser, geralmente confundidas com modelo, tarefa e familiaridade do usuário.

O renderer público do Reddit não expôs de forma estável score e total de comentários para todas as páginas; esses números foram omitidos em vez de estimados. Idade relativa e data só são registradas quando visíveis.

### Inferences

- O consumo de quota parece ser uma função de modelo/esforço, tamanho do contexto, cache, paralelismo, frequência de tool calls, compaction e política de produto. Comparar apenas minutos de parede produz conclusões instáveis.
- Um teste de quotas deve capturar percentuais antes/depois, timestamps, versão do CLI, modelo/esforço, tamanho do repo, número de subagentes, tokens/cache quando disponíveis, tool calls, compactions e resultado aceito. Sem isso, “acabou em 20 minutos” é sinal de investigação, não taxa.
- Paralelismo aumenta throughput potencial, mas também multiplica contextos e conflitos. Worktree isola arquivos e branches; não isola automaticamente processos, portas, containers, credenciais ou bancos.

### Gaps

- Não foram obtidos logs de billing oficiais que confirmem o suposto bug de retomada de subagentes do Claude Code em todas as versões.
- As quotas dos planos são dinâmicas e podem depender de conta, região, modelo e promoção. Esta nota não converte relatos em número oficial garantido.
- Não foi localizada a origem auditável do alegado teste Medium de “um milhão de tokens” citado no rascunho. Ele não deve ser publicado como fato.
- A busca não sustenta frases como “Reddit concorda”. Os contraexemplos são numerosos e relevantes.

## Superset/Paradev e Nimbalyst: existência, licença, Windows e relevância

### Takeaway

As duas ferramentas existem e são relevantes para orquestração visual de agentes em worktrees, mas não são equivalentes. Nimbalyst se apresenta como gratuito, MIT e multiplataforma, incluindo Windows. Superset mudou de nome para Paradev em 26/10/2026, usa Elastic License 2.0, prioriza macOS, oferece Linux x64 experimental e não suporta Windows. Portanto, a descrição Argon de “Superset MIT para Windows” está errada/desatualizada.

### Cited Findings

| Critério | Nimbalyst | Superset → Paradev |
|---|---|---|
| Existência/manutenção | Repositório público ativo: [Nimbalyst/nimbalyst](https://github.com/Nimbalyst/nimbalyst). | Repositório público ativo: [ParadevAI/Paradev](https://github.com/ParadevAI/Paradev); o [anúncio oficial](https://paradev.com/blog/a-new-name) informa a mudança de nome em 26/10/2026. |
| Licença | O projeto declara [MIT](https://github.com/Nimbalyst/nimbalyst). | O repositório usa [Elastic License 2.0](https://github.com/ParadevAI/Paradev), uma licença *source-available*, não MIT/OSI. |
| Sistemas | O README declara app desktop para macOS, Windows e Linux no [repositório oficial](https://github.com/Nimbalyst/nimbalyst). | A [documentação de instalação](https://docs.paradev.com/install) prioriza macOS, marca Linux x64 como experimental e informa que Windows não está disponível/planejado. |
| Agentes | Claude Code, Codex e OpenCode; Copilot/OpenCode em estágios indicados no [README](https://github.com/Nimbalyst/nimbalyst). | Suporta agentes CLI, incluindo Claude Code e Codex, conforme [visão geral](https://docs.paradev.com/overview) e [documentação Codex](https://docs.paradev.com/agents/codex). |
| Isolamento | Sessões paralelas com worktree, Kanban, diff review, git e artefatos em arquivos, conforme [README](https://github.com/Nimbalyst/nimbalyst). | Cada agente pode rodar em worktree separado, com comparação de diffs, conforme [documentação](https://docs.paradev.com/overview). |

Nimbalyst é pertinente ao uso em Windows e ao workflow visual sem depender de uma IDE tradicional. Paradev é pertinente como referência de UX/orquestração, mas não como recomendação local para Windows no estado atual.

A [documentação Paradev para Codex](https://docs.paradev.com/agents/codex) informa que o agente pode usar assinatura ChatGPT ou API key e que, por padrão, o app executa Codex com flags que desabilitam approval/sandbox, salvo alteração do usuário. Isso é um risco operacional: worktree limita conflitos de Git, mas permissão ampla ainda pode afetar arquivos externos, rede e serviços acessíveis.

### Inferences

- Nimbalyst e Paradev resolvem a camada de **coordenação/observabilidade**, não provam superioridade dos modelos executados dentro delas.
- Para um ambiente Windows, Nimbalyst é o candidato verificável entre os dois. Paradev exigiria macOS ou Linux experimental; WSL não deve ser presumido como suporte oficial.
- Antes de paralelizar 10 ou 100 agentes, deve-se testar isolamento de portas, banco, containers, credenciais, processos e caches. Worktree sozinho só resolve a árvore Git.

### Gaps

- A declaração de compatibilidade e as capacidades são majoritariamente auto-relatadas pelos projetos. Não foi executado nesta pesquisa um teste de instalação independente em Windows.
- Não há benchmark independente que mostre ganho líquido de produtividade de Nimbalyst ou Paradev depois de contabilizar merge, revisão, conflitos e consumo de quota.
- A manutenção pode mudar rapidamente. Recomenda-se registrar release/tag/commit antes da publicação final.

## Auditoria das afirmações herdadas da conversa Argon e dos rascunhos

### Takeaway

O material Argon mistura fontes reais com números sem trilha verificável e transforma relatos em regras universais. As correções abaixo preservam o que pode ser sustentado e removem precisão falsa. A conclusão publicável é: os modelos de fronteira estão próximos e alternam liderança por tarefa; custo/quota dependem de workflow; comunidade oferece hipóteses e protocolos, não consenso.

### Cited Findings

| Afirmação herdada | Veredito | Correção sustentada |
|---|---|---|
| “SWE-bench Verified: Opus 5.5 97%, Sonnet 94,2%, Codex 68,8%, Gemini 64,5%; fonte Princeton/Artificial Analysis.” | **Não verificada e provavelmente mistura harnesses/snapshots.** | O [SWE-bench](https://www.swebench.com/) permite comparar entradas dentro da mesma variante e scaffold; qualquer placar precisa linkar a linha/modelo/harness/data exatos. Os quatro números não foram confirmados juntos. |
| “SWE-bench Pro 89,9/84,1/64,6.” | **Não verificada.** | Manter apenas com fonte primária, versão, métrica e agente. Não foi localizada essa combinação nas fontes consultadas. |
| “Terminal-Bench 4.0: Sonnet 70,6 e ranking fechado.” | **Não verificada como tabela atual.** | Terminal-Bench 4.0 na [Artificial Analysis](https://artificialanalysis.ai/methodology/intelligence-benchmarking) tem 66 tarefas, três repetições e mini-swe-agent. Citar o resultado direto do snapshot, não transportar valor entre versões. |
| “Tool Calling Index 36,3.” | **Rótulo enganoso.** | O [LLM Stats leaderboard](https://llm-stats.com/leaderboards/llm-leaderboard) possui score de categoria *tools* em uma escala composta. Não deve ser apresentado como 36,3% de chamadas corretas. |
| “DeepSWE v1.1 prova o ranking geral.” | **Fonte/metodologia insuficiente.** | Um benchmark só sustenta sua tarefa, versão e harness. Não foi encontrada base para usá-lo como ranking geral dos aplicativos. |
| “Claude é 3,2–4,2× mais eficiente em tokens.” | **Não sustentada.** | O [artigo v5.0](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5/) mostra grandes diferenças de custo por configuração e que tarefas agênticas consomem ~90% da saída, mas não estabelece essa razão universal. |
| “308 tokens/s” e latências exatas como propriedade fixa do modelo. | **Snapshot incompleto.** | Velocidade depende de endpoint, provedor, esforço e data; registrar esses campos usando o [leaderboard Artificial Analysis](https://artificialanalysis.ai/leaderboards/models). |
| “Preferência cega de engenharia: 67%.” | **Não verificada.** | Preferência visual cega tem metodologia clara em [Artificial Analysis Image](https://artificialanalysis.ai/methodology/image); não foi achado protocolo equivalente para esse “67%” de engenharia. |
| “Claude nunca trunca; Codex trunca >10k por causa do kernel sandbox.” | **Absolutismo sem evidência.** | Truncamento depende de CLI, ferramenta, limites de output e versão. Sandbox e truncamento são mecanismos diferentes; medir com logs na versão testada. |
| “Gemini/Antigravity é o único com browser e 1–2M de contexto.” | **Não demonstrada e mistura modelo com app.** | Diferenciar janela nominal do modelo, contexto utilizável, compaction e ferramentas do aplicativo. Não foi localizado teste comum que prove exclusividade. |
| “OpenRouter indica distribuição de produção 80–85%/10–15%/3–5%.” | **Inferência inválida.** | [OpenRouter Rankings](https://openrouter.ai/rankings) mede tokens no tráfego público da plataforma, não qualidade, usuários ou mix ideal. |
| “Reddit chegou a um consenso.” | **Falso enquadramento.** | As threads [comparativa](https://www.reddit.com/r/codex/comments/1s1btfx/codex_vs_claude_code_vs_antigravity_whats_your/) e de [quotas Codex](https://www.reddit.com/r/codex/comments/1w9up47/what_on_earth_happened_to_usage_limits/) contêm relatos conflitantes; devem ser descritas como anedotas. |
| “Teste Medium de 1 milhão de tokens comprovou X.” | **Fonte não identificada.** | Remover até obter URL, autor, data, prompts, logs e protocolo. |
| “Superset e Nimbalyst são MIT, Windows e equivalentes.” | **Falso/desatualizado.** | [Nimbalyst](https://github.com/Nimbalyst/nimbalyst) declara MIT e Windows. [Superset virou Paradev](https://paradev.com/blog/a-new-name), usa [Elastic License 2.0](https://github.com/ParadevAI/Paradev) e sua [instalação](https://docs.paradev.com/install) não suporta Windows. |

**Bibliografia operacional, por finalidade**

- Benchmark de issues: [SWE-bench oficial](https://www.swebench.com/).
- Metodologia e resultados de inteligência/código/terminal: [Artificial Analysis Methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking), [Index v5.0](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5/) e [leaderboard ao vivo](https://artificialanalysis.ai/leaderboards/models).
- Integridade/versões de terminal: [Terminal-Bench News](https://www.tbench.ai/news) e [Leaderboard Integrity Update](https://www.tbench.ai/news/leaderboard-integrity-update).
- Agregação com incerteza: [LLM Stats Research](https://llm-stats.com/research), [Benchmarks](https://llm-stats.com/benchmarks) e [Leaderboard](https://llm-stats.com/leaderboards/llm-leaderboard).
- Tráfego de marketplace: [OpenRouter Rankings](https://openrouter.ai/rankings).
- Imagem: [Artificial Analysis Image Methodology](https://artificialanalysis.ai/methodology/image), [Text-to-Image](https://artificialanalysis.ai/image/leaderboard/text-to-image) e [Image Editing](https://artificialanalysis.ai/image/leaderboard/editing).
- Experimentos de comunidade auditáveis: [Opus→Codex em worktrees](https://www.reddit.com/r/ClaudeAI/comments/1sdk2sj/i_benchmarked_plan_with_opus_execute_with_codex/), [seis projetos e cross-review](https://www.reddit.com/r/codex/comments/1tbkmc3/codex_vs_claude_code_i_ran_a_6project_benchmark/), [repositório dos seis projetos](https://github.com/AdrielRod/codex-vs-claude-code), [Rails/PR eval](https://www.reddit.com/r/ClaudeAI/comments/1qxr7vs/gpt53_codex_vs_opus_46_we_benchmarked_both_on_our/) e [56 tarefas reais](https://www.reddit.com/r/ClaudeCode/comments/1t0xrad/gpt55_vs_gpt54_vs_opus_47_on_56_real_coding_tasks/).
- Relatos de quota/campo: [cache-resume no Claude](https://www.reddit.com/r/ClaudeAI/comments/1whvqcl/quota_draining_claude_code_rebills_a_finished/), [limites Codex 1](https://www.reddit.com/r/codex/comments/1w9up47/what_on_earth_happened_to_usage_limits/), [limites Codex 2](https://www.reddit.com/r/codex/comments/1vy3yhu/5_hour_limits_are_back_for_plus_users/), [comparativo dos três apps](https://www.reddit.com/r/codex/comments/1s1btfx/codex_vs_claude_code_vs_antigravity_whats_your/) e [relato Antigravity](https://www.reddit.com/r/google_antigravity/comments/1s337wg/experience_coming_from_claude_and_codex/).
- Orquestradores: [Nimbalyst](https://github.com/Nimbalyst/nimbalyst), [Paradev](https://github.com/ParadevAI/Paradev), [documentação Paradev](https://docs.paradev.com/overview), [instalação](https://docs.paradev.com/install) e [Codex no Paradev](https://docs.paradev.com/agents/codex).

### Inferences

- O relatório final deve substituir rankings absolutos por uma matriz de decisão: qualidade por classe de tarefa, custo por tarefa aceita, tempo, quota, robustez, integração e risco de permissão.
- A recomendação mais defensável é **Claude/Opus ou GPT/Astra para tarefas de alta dificuldade conforme teste privado; modelos mais baratos para mecânica; Gemini/Antigravity quando suas ferramentas/contexto forem vantajosos e validados; cross-review em mudanças de risco**. Isso é estratégia de avaliação, não ranking fixo.
- Para LinkedIn, publicar a hierarquia de evidência e os limites aumenta credibilidade. Relatos dramáticos de quota podem ser citados como casos, acompanhados de contraexemplos e sem linguagem de prevalência.

### Gaps

- Antes do PDF final, reabrir os leaderboards dinâmicos, registrar captura, filtros e modelos exatos; uma atualização pode mudar a ordem em dias.
- Falta o benchmark privado, de ponta a ponta, com os três aplicativos e o mesmo corpus de tarefas. Essa é a principal etapa necessária para transformar a pesquisa em recomendação operacional forte.
- Afirmações de quota devem ser revalidadas em documentação oficial na data de publicação; não usar percentuais de Reddit como termos do plano.

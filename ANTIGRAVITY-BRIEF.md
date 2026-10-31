# Brief para Antigravity — redesign editorial do relatório

## Objetivo

Gerar uma publicação visual em PDF que apresente os resultados da pesquisa em formato legível para LinkedIn e A4. A peça é independente do projeto “Nossa Cultura”; não alterar nenhum arquivo do site Portifolio-LAY ou do projeto Nossa Cultura.

## Arquivos de trabalho autorizados

- `reports/Orquestração multiagente com evidências.md` — conteúdo e fontes canônicos.
- `scripts/build_evidence_report.py` — compositor do PDF.
- `README.md` — índice do material e escopo.
- `ANTIGRAVITY-BRIEF.md` — este handoff.
- `report/Relatorio-Orquestracao-Multiagente-Evidencias-2026.pdf` — saída gerada.

Não editar as notas de pesquisa sem motivo documentado. Não modificar arquivos fora do repositório de pesquisa. Não fazer commit, push nem publicar o PDF em serviços externos.

## Direção visual LAY

Tomar como referência os tokens em `Portifolio-LAY/src/styles/tokens.css` e as famílias tipográficas declaradas em `src/app/fonts.ts`, sem copiar componentes, arquivos de marca ou fontes para este repositório. O documento inteiro usa página A4 em orientação paisagem e composição editorial de livro, com páginas de abertura, spreads de dados e seções de leitura contínua.

- Cores: preto `#000000`, bone white `#FAF5E9`, amarelo `#FFF201`, vermelho `#C21818`, ciano `#00FFFF`, magenta `#FF3EB5`.
- Referências tipográficas: JoTa Urban para display; Ubuntu para texto; JetBrains Mono para métricas; Silkscreen para acentos pontuais. Se não for possível embutir uma fonte no PDF, use uma substituta instalada e legível.
- Composição: editorial urbana/brutalista, contraste alto, títulos grandes, números destacados, filetes e blocos geométricos. Evitar aparência de artigo acadêmico genérico, cartões SaaS, sombras suaves e gradientes decorativos.
- Leitura: corpo confortável em A4 paisagem; gráficos simples, com unidades, fonte e nota metodológica visíveis. Considerar leitura na tela do celular sem depender de texto minúsculo.

## Narrativa e gráficos esperados

1. Capa de impacto com título, tema, autoria institucional LAY e data editorial `31 out. 2026`.
2. Sumário executivo com o achado de telemetria local: 2.060 chamadas, 33 subagentes e média de 313.283 tokens de cache lidos por chamada. Sinalizar que isso é um caso local e não revela a fórmula da cota comercial.
3. Evidência de ranking em gráficos independentes para FrontierCode 2.0, Terminal-Bench-Science e custo/tarefa. Manter modelo, esforço, unidade, data, fonte e limite de interpretação. Não pôr métricas de benchmarks diferentes na mesma escala.
4. Mapa de encaminhamento diário: scripts locais para tarefas determinísticas; Codex para trabalho delimitado após piloto; Claude para arquitetura e revisão de alto risco com contexto enxuto; Gemini/Antigravity para pesquisa, multimodalidade e QA visual quando necessários; gate final humano.
5. Custo em camadas: assinaturas fixas em USD, câmbio/tributos dependentes da fatura, API variável e energia/compute local. Exibir Google AI Pro como preço por país/conta, sem inventar preço local.
6. Se apresentar o mix de 50% scripts, 30% Codex, 15% Claude e 5% Gemini, identificá-lo como **SIMULAÇÃO de alocação de 100 tarefas/semana**. Não chamar percentuais de tokens, economia ou uso observado. Não prever a fatura, cota ou redução de cache.
7. Fechamento com plano de piloto: tarefas equivalentes, commit inicial comum, limites iguais, testes, retrabalho, tempo e medidores de cota.
8. Bibliografia anotada e clicável, incluindo benchmarks, documentação oficial, experimentos independentes, relatos do Reddit explicitamente qualitativos e telemetria local marcada como não pública.

## Restrições de evidência

- A pesquisa foi consolidada em `31/10/2026`; preços e rankings são snapshots, sujeitos a mudança.
- Valores de Artificial Analysis (Opus max US$ 10,04; GPT-6 Astra max US$ 6,24; GPT-6 Sol max US$ 1,27 por tarefa) pertencem à configuração e mistura daquela bateria. Não são preços de assinatura nem cobrança desta conta.
- Claude Pro e ChatGPT Plus: US$ 20/mês nos EUA no recorte da pesquisa. Google AI Pro: conferir o preço da região e da conta, sem inferir valor brasileiro.
- Cotas dinâmicas não têm conversão pública e auditável para tokens por tarefa. Não prometer “economia de X%” nem “fim da saturação”.
- Separar documentação oficial, benchmark/metodologia, experimento independente, relato comunitário e observação do projeto local.
- Não alegar resultado de Gemini/Antigravity em testes que não incluíram essa superfície sob condição comparável.
- Não calcular reais sem faturas, câmbio aplicado e tributos comprovados; não calcular custo de energia sem potência média medida e tarifa.

## Critérios de aceite e revisão visual

- PDF existe no caminho de saída e pode ser aberto por um leitor padrão.
- Capa e páginas internas têm contraste visual coerente e hierarquia clara.
- Nenhum gráfico está sem rótulos, unidade, fonte ou data; barras não induzem comparações entre testes incompatíveis.
- Texto, tabelas e links não estão cortados, sobrepostos ou ilegíveis; não há página vazia involuntária.
- A bibliografia continua acessível por hyperlinks no PDF.
- Conferir `pdfinfo`, número de páginas e anotações/links; renderizar capa, página de gráficos, página de custos e última página para inspeção visual.
- Atualizar README para descrever precisamente gráficos e limites, sem promover um modelo como vencedor universal.

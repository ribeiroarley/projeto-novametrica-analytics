# NovaMétrica: Diagnóstico de Rentabilidade, Risco de Supply Chain e Eficiência Promocional

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## 1. O Desafio de Negócio (Problem Statement)

A NovaMétrica opera como uma rede varejista multirregional com modelo de distribuição omnichannel (Lojas Físicas, E-commerce próprio e Marketplace). Ao final do primeiro quadrimestre de 2026, a diretoria executiva deparou-se com sinais contraditórios: embora o faturamento global permanecesse robusto, o fluxo de caixa e a rentabilidade líquida exibiam vulnerabilidades operacionais ocultas.

Três gargalos centrais foram submetidos à auditoria analítica:

1. **Compressão de Margem Financeira por Ações Promocionais:** Suspeita de que as campanhas de desconto agressivo, notadamente a Semana do Consumidor, estavam canibalizando margem bruta sem entregar ganho real de elasticidade-preço ou expansão de volume de transações.
2. **Desequilíbrio Crítico de Inventário e Risco de Ruptura:** Risco iminente de desabastecimento nos SKUs de maior giro comercial em paralelo ao aprisionamento de capital de giro em mercadorias de baixo giro estagnadas em centros de distribuição.
3. **Atribuição Indevida de Custos e Fricção Logística:** Crença interna de que os atrasos de transporte e cumprimento de prazo de entrega eram o vetor primário das devoluções de mercadorias e da queda nos índices de satisfação dos clientes.

---

## 2. Metodologia de Investigação e Governança Epistêmica

Para substituir percepções subjetivas por evidências auditáveis, o diagnóstico adotou um pipeline formal de engenharia e análise de dados operado via ambiente virtual isolado (`.venv`), garantindo reprodutibilidade matemática através de rotinas versionadas em `07_scripts_exploratorios/`.

A integridade analítica apoia-se em um framework de governança epistêmica estrito, categorizando cada conclusão em quatro graus de sustentação factual:

- **[CONFIRMADO]:** Fato empírico extraído e recalculado a partir das bases primárias saneadas (724 pedidos faturados e conciliados, totalizando R$ 374.588,22 em receita líquida).
- **[PROVÁVEL]:** Inferência baseada em padrões estatísticos consistentes e convergência de indicadores, sem atribuição isolada de causalidade.
- **[HIPÓTESE REJEITADA]:** Conjectura de negócio refutada formalmente pelos testes de hipótese e correlações lineares.
- **[DADO AUSENTE]:** Lacuna cadastral ou operacional na esteira de dados que impede diagnóstico causal conclusivo de produto.

---

## 3. As 3 Hipóteses Auditadas: Diagnóstico Quantitativo (The Findings)

### Hipótese 1: A "Semana do Consumidor" Destruiu Margem sem Alavancar Volume?

- **Veredito:** `[CONFIRMADO]`
- **Evidências:** 
  - Enquanto as vendas regulares ("Sem Campanha") sustentaram margem bruta média de **43,97%** com desconto médio controlado de **4,34%**, a campanha *Semana do Consumidor* registrou desconto médio de **17,95%** (rente ao teto estatutário de 18,0%).
  - A margem bruta da campanha despencou para **34,99%**, representando uma destruição líquida de **8,98 pontos percentuais** de rentabilidade (-20,4% relativo vs. vendas regulares).
- **Impacto no Negócio:**
  - A concessão do teto de desconto atraiu apenas **29 pedidos**, gerando R$ 11.136,43 de receita líquida. 
  - Conclui-se que não houve ganho de escala compensatório: a campanha meramente transferiu valor da companhia para clientes que teriam adquirido a preços normais.

| Iniciativa Comercial | Volume (Pedidos) | Receita Líquida (R$) | Margem Bruta (R$) | Desconto Médio (%) | Margem Bruta (%) | Desvio vs. Regular |
|:---|---:|---:|---:|---:|---:|---:|
| Vendas Regulares (Sem Campanha) | 545 | R$ 289.543,17 | R$ 127.318,17 | 4,34% | 43,97% | Referência |
| Frete Turbo | 52 | R$ 26.018,17 | R$ 10.523,17 | 8,49% | 40,45% | -3,52 p.p. |
| Liquida Verão | 62 | R$ 29.609,60 | R$ 11.766,60 | 13,02% | 39,74% | -4,23 p.p. |
| Páscoa Digital | 36 | R$ 18.280,85 | R$ 7.326,85 | 11,80% | 40,08% | -3,89 p.p. |
| **Semana do Consumidor** | **29** | **R$ 11.136,43** | **R$ 3.896,43** | **17,95%** | **34,99%** | **-8,98 p.p.** |

---

### Hipótese 2: O Atraso Logístico é a Causa Raiz das Devoluções e Queda de Avaliação?

- **Veredito:** `[HIPÓTESE REJEITADA]`
- **Evidências:**
  - Os pedidos devolvidos registraram prazo médio de entrega de **4,85 dias** (mediana 5,0 dias; desvio padrão 2,03 dias), enquanto os pedidos não devolvidos tiveram média de **5,33 dias** (mediana 5,0 dias; desvio padrão 2,01 dias).
  - Os pedidos devolvidos chegaram **0,48 dias mais rápido** aos destinatários do que as compras retidas.
  - O coeficiente de correlação linear de Pearson entre Prazo de Entrega e Nota de Avaliação do Cliente foi de **r = +0,0732**, comprovando ausência de relação estatística entre atraso de frete e insatisfação.
- **Causa Real:**
  - A avaliação média despencou entre os clientes com devolução (**3,56 estrelas vs. 4,02 estrelas** em pedidos regulares), comprovando frustração de consumo decorrente de vício do produto, expectativas desalinhadas na vitrine virtual ou erro de expedição.
- **Vulnerabilidade Detectada:**
  - `[DADO AUSENTE]`: A ausência cadastral da variável `Motivo_Devolucao` no fluxo reverso impede identificar se o defeito é fabril ou de especificação de catálogo. A operação de transporte está isenta de culpa.

| Grupo de Pedidos | Volume | Prazo Médio (dias) | Mediana (dias) | Desvio Padrão | Nota Média (1-5) | Avaliações Válidas |
|:---|---:|---:|---:|---:|---:|---:|
| Pedidos Não Devolvidos | 667 | 5,33 | 5,0 | 2,01 | 4,02 | 581 |
| Pedidos Devolvidos | 27 | 4,85 | 5,0 | 2,03 | 3,56 | 25 |

---

### Hipótese 3: Há Risco Iminente de Ruptura em SKUs Estratégicos?

- **Veredito:** `[CONFIRMADO - ALERTA CRÍTICO]`
- **Evidências:**
  - Três produtos prioritários de alto giro encontram-se em patamar de desabastecimento iminente, com saldo físico de **5 unidades por SKU**, contra a meta operacional mínima de segurança estabelecida em **12 unidades**.
  - O consumo diário histórico (run rate em 120 dias) atesta esgotamento total em cerca de 10 dias corridos.
- **Exposição Financeira:**
  - A demanda conjunta dos três itens gera **R$ 669,69/dia** em vendas líquidas.
  - A ausência de reposição imediata acarretará perda projetada de **R$ 20.090,72** no faturamento do mês subsequente (maio de 2026).
  - Em contrapartida, foram identificados itens com mais de 25 dias sem venda e saldo de 40 unidades (`ES-001`, `SP-002`, `PT-002`), acumulando **~R$ 35.000,00 de capital de giro estagnado**.

| SKU | Produto | Categoria | Estoque Atual | Estoque Mínimo | Run Rate Diário | Cobertura Restante | Faturamento em Risco / Dia | Perda Projetada (30 dias) |
|:---|:---|:---|---:|---:|---:|---:|---:|---:|
| EL-001 | Smartwatch Move | Eletrônicos | 5 un | 12 un | 0,467 un/dia | 10,7 dias | R$ 307,79 | R$ 9.233,84 |
| CA-003 | Aspirador Compact | Casa | 5 un | 12 un | 0,458 un/dia | 10,9 dias | R$ 217,97 | R$ 6.539,07 |
| MO-002 | Jaqueta Corta-Vento | Moda | 5 un | 12 un | 0,483 un/dia | 10,3 dias | R$ 143,93 | R$ 4.317,81 |
| **CONSOLIDADO** | **Top 3 Críticos** | **Multicategoria** | **15 un** | **36 un** | **1,408 un/dia** | **~10,6 dias** | **R$ 669,69** | **R$ 20.090,72** |

---

## 4. Matriz de Decisão e Soluções Estratégicas (Action Plan)

A priorização executiva foi modelada sob o método Esforço × Impacto, gerando quatro iniciativas deliberadas para o C-Level:

| ID | Classificação na Matriz | Iniciativa Estratégica | Impacto Estimado | Prazo de Execução | Área Responsável | Status de Aprovação |
|:---:|:---|:---|:---|:---:|:---|:---:|
| **ACT-01** | **Quick Win** (Alto Impacto, Baixo Esforço) | Emissão emergencial de Pedido de Compra (PO) de reposição de 30 unidades por SKU para `EL-001`, `CA-003` e `MO-002`. | Evita perda imediata de R$ 20.090,72/mês por ruptura e restabelece 60 dias de cobertura. | Imediato (7 dias) | Suprimentos & Operações | Aprovado |
| **ACT-02** | **Projeto Estratégico** (Alto Impacto, Médio Esforço) | Redesenho da política da *Semana do Consumidor*: trava de desconto máximo em 12% para itens individuais e permissão de 18% restrita a combos com margem bruta > 50%. | Recuperação estimada de 5 a 7 p.p. de margem bruta em ciclos promocionais (~R$ 15.000,00 por evento). | Curto Prazo (30 dias) | Diretoria Comercial & Pricing | Aprovado |
| **ACT-03** | **Melhoria Contínua** (Médio Impacto, Baixo Esforço) | Implementação obrigatória do campo estruturado `Motivo_Devolucao` no fluxo reverso do SAC e no portal de devoluções online. | Elimina lacuna crítica de dados, viabiliza correções de ficha técnica de produto e reduz custos de devolução. | Curto Prazo (30 dias) | Atendimento & SAC | Aprovado |
| **ACT-04** | **Otimização de Capital** (Médio Impacto, Baixo Esforço) | Campanha promocional de queima de estoque parado ("Outlet NovaMétrica") para itens com cobertura superior a 90 dias (`ES-001`, `SP-002`, `PT-002`). | Desmobilização de ~R$ 35.000,00 em capital de giro estagnado, liberando espaço físico e caixa operacional. | Médio Prazo (90 dias) | Gerência Comercial & Pricing | Aprovado |

---

## 5. Arquitetura da Solução e Rastreabilidade

O repositório está estruturado por propósito funcional, segregando dados brutos, artefatos analíticos e entregáveis de decisão:

```text
projeto-nova-metrica-analytics/
├── .antigravity/                            # Regras de governança operacional e parâmetros da CLI
├── GEMINI_CONTEXT.md                       # Diretrizes consolidadas e regras de negócio para IA
├── GEMINI.md                               # Ponto de entrada de regras globais do workspace
├── 01_ingestao_dados_brutos/               # Camada Raw: transações e dados de inventário de partida
├── 02_planejamento_e_operacoes/            # Diretrizes corporativas e atas de alinhamento
├── 03_conectores_e_comunicacoes/           # Fontes não estruturadas de canais corporativos simulados
├── 04_governanca_e_contexto/               # Conhecimento persistente e glossário de regras de negócio
├── 05_analytics_e_artifacts/               # Camada tratada: vendas_novametrica_clean.csv e regras JSON
├── 06_entregaveis_estrategicos/            # Entregáveis executivos:
│   ├── deck_executivo_diretoria.md         # Apresentação executiva em 5 atos (<= 40 palavras/slide)
│   ├── matriz_esforco_impacto_priorizacao.xlsx # Planilha corporativa formatada com as ações priorizadas
│   └── relatorio_diagnostico_final_novametrica.md # Relatório executivo completo em 6 blocos
├── 07_scripts_exploratorios/               # Módulo oficial de esteiras e evidências algorítmicas:
│   ├── 01_pipeline_eda_novametrica.py      # Pipeline automatizado de ingestão, saneamento e cálculo de hipóteses
│   └── 02_atualizar_matriz_priorizacao.py  # Script de atualização e estilização da matriz de priorização
├── skills_e_templates/                     # Skill especializada em entregáveis executivos
├── requirements.txt                        # Especificação de dependências da esteira de dados
└── LICENSE                                 # Licença aberta MIT do repositório
```

### Rastreabilidade Analítica e Auditoria
Todos os números, conclusões e tabelas apresentados neste estudo de caso são 100% auditáveis e reprodutíveis:
- **Base Transacional Saneada:** O dataset [`05_analytics_e_artifacts/vendas_novametrica_clean.csv`](05_analytics_e_artifacts/vendas_novametrica_clean.csv) consolida os tratamentos de tipagem temporal, enriquecimento e correção cadastral de canais.
- **Esteira de Cálculo e EDA:** O pipeline [`07_scripts_exploratorios/01_pipeline_eda_novametrica.py`](07_scripts_exploratorios/01_pipeline_eda_novametrica.py) processa as 724 transações e a posição de inventário dos 20 SKUs, calculando os testes de hipótese e gerando o output executivo.
- **Modelagem de Priorização:** O script [`07_scripts_exploratorios/02_atualizar_matriz_priorizacao.py`](07_scripts_exploratorios/02_atualizar_matriz_priorizacao.py) formaliza as quatro ações homologadas na planilha [`06_entregaveis_estrategicos/matriz_esforco_impacto_priorizacao.xlsx`](06_entregaveis_estrategicos/matriz_esforco_impacto_priorizacao.xlsx).

---

## 6. Licença
Distribuído sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

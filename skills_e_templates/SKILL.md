---
name: entregaveis-executivos-novametrica
description: >-
  Skill especializada para o ecossistema Antigravity CLI e modelos Gemini na transformação de análises
  de dados da NovaMétrica em entregáveis executivos padronizados e estratégicos para diretoria e gestores.
  Acione esta Skill SEMPRE que o usuário solicitar: relatórios executivos, apresentações de resultados (decks),
  memos gerenciais, sínteses de inteligência analítica, diagnósticos de KPIs (vendas, margem, estoque e logística)
  ou materiais para tomada de decisão no ambiente NovaMétrica. Garante rigor na separação estrita entre
  [CONFIRMADO] (fatos quantificados), [PROVÁVEL] (interpretações fundamentadas) e [HIPÓTESE] (hipóteses a validar),
  com diretrizes nativas para o agente Gemini no Antigravity.
---

# Entregáveis Executivos NovaMétrica (Antigravity CLI + Gemini)

Skill especializada em transformar dados analíticos, transacionais e operacionais da **NovaMétrica** em comunicações executivas padronizadas, precisas e orientadas à tomada de decisão de alto nível, operando nativamente no ecossistema **Antigravity CLI** potencializado por modelos **Gemini**.

---

## 🎯 Objetivo e Princípios Operacionais

Garantir que todo artefato ou análise gerada para lideranças e diretoria da NovaMétrica mantenha:
1. **Linguagem de Negócio Direta:** Sem prolixidade técnica desnecessária, focando em impacto em receita, margem e giro.
2. **Separação Epistêmica Rigorosa:** Diferenciação inequívoca entre dados brutos auditados, correlações prováveis e hipóteses estratégicas.
3. **Recomendações Acionáveis e Sustentadas:** Cada recomendação deve possuir evidência numérica, estimativa de impacto financeiro/operacional e responsável direto.
4. **Governança Nativa no Antigravity:** Integração com o pipeline de dados Python (`.venv`), execução reprodutível e geração de artifacts limpos no diretório de trabalho.

---

## ⚡ Quando Acionar Esta Skill

A ativação ocorre automaticamente no Antigravity CLI com Gemini mediante os seguintes gatilhos e solicitações:

| Gatilho Explícito | Exemplos de Solicitação |
|---|---|
| **Relatório Executivo** | "gere um relatório para a diretoria", "elabore um relatório executivo de vendas" |
| **Documento Gerencial / Memo** | "prepare um memo gerencial consolidado", "visão consolidada de KPIs" |
| **Apresentação de Resultados (Deck)** | "monte a estrutura de um deck executivo", "slides para a reunião de diretoria" |
| **Resumo Executivo para C-Level** | "resumo de insights para o CEO/CFO", "o que levar para a reunião de comitê" |
| **Material de Tomada de Decisão** | "material de suporte para decisão de pricing", "análise de corte de descontos" |
| **Diagnóstico de Hipóteses** | "resolva as 3 hipóteses de negócio", "diagnóstico de risco de ruptura e margem" |

---

## 🛡️ Regra Pétrea de Governança Epistêmica

A NovaMétrica adota governança analítica estrita. É terminantemente proibido misturar dados empíricos com suposições sem o devido marcador:

| Marcador | Definição Operacional | Exemplo NovaMétrica |
|---|---|---|
| `[CONFIRMADO]` | Fato auditado diretamente nas bases transacionais ou planilhas de inventário. | `[CONFIRMADO] A margem bruta média da base saneada é de 42,93%, com receita líquida de R$ 374.588,22.` |
| `[PROVÁVEL]` | Padrão consistente ou correlação observada, sem prova de causalidade definitiva. | `[PROVÁVEL] O desconto médio de 17,95% na Semana do Consumidor é o principal causador da compressão da margem percentual para 34,99%.` |
| `[HIPÓTESE]` | Explicação plausível de negócio, demandando validação empírica ou novos testes. | `[HIPÓTESE] O aumento de devoluções pode estar atrelado à incompatibilidade de expectativas no canal online, e não a atrasos logísticos.` |
| `[DADO AUSENTE]` | Métrica ou dimensão indispensável não catalogada nas fontes atuais. | `[DADO AUSENTE] Motivo categorizado de devolução de produto não registrado no CSV transacional.` |
| `[INCONSISTÊNCIA]`| Violação de regra de negócio corporativa ou desvio de integridade referencial. | `[INCONSISTÊNCIA] Existência da grafia 'Ecommerce' em vez do padrão corporativo 'E-commerce'.` |

> ⚠️ **Regra Prática:** Se não há um número específico nos dados que comprove a declaração, classifique-a imediatamente como `[PROVÁVEL]` ou `[HIPÓTESE]`.

---

## 📐 Estruturas Padrão de Entregáveis

### 1. Relatório Executivo (Estrutura Obrigatória em 6 Blocos)

```markdown
1. SUMÁRIO EXECUTIVO (máx. 5 linhas)
   → O que ocorreu, principal KPI numérico, risco crítico e principal recomendação.

2. CONTEXTO E LIMITAÇÕES
   → Recorte temporal, fontes saneadas (ex: vendas_novametrica_clean.csv), filtros aplicados e lacunas.

3. FATOS OBSERVADOS [CONFIRMADO]
   → Tabelas e bullets objetivos com números, unidades monetárias e períodos.

4. INTERPRETAÇÕES SUSTENTADAS
   → Análise analítica sinalizada estritamente com [CONFIRMADO], [PROVÁVEL] ou [HIPÓTESE].

5. RISCOS E ALERTAS OPERACIONAIS
   → Indicadores violando limites do JSON de governança (Margem < 32%, Devolução > 5%, Desconto > 18%, Ruptura).

6. PLANO DE AÇÃO E RECOMENDAÇÕES PRIORIZADAS
   → Formato obrigatório para cada recomendação:
     • [AÇÃO]: Descrição clara e mandatória.
     • [EVIDÊNCIA]: Dado numérico auditado de sustentação.
     • [IMPACTO ESTIMADO]: Ganho financeiro, retenção de margem ou mitigação de risco.
     • [RESPONSÁVEL SUGERIDO]: Área de negócio (Comercial, Operações, Marketing, Pricing).
```

### 2. Deck Executivo de Apresentação (Narrativa em 5 Atos)

```text
ATO 1 — O CENÁRIO: Abertura executiva, volume transacionado e número de ouro do período.
ATO 2 — O QUE ESTÁ FUNCIONANDO: Alavancas de receita, categorias resilientes e margem saudável.
ATO 3 — PONTOS DE ATENÇÃO: Descontos excessivos, risco iminente de ruptura de estoque e devoluções.
ATO 4 — INTERPRETAÇÕES E DIAGNÓSTICO: Hipóteses validadas vs. rejeitadas com marcadores epistêmicos.
ATO 5 — PRÓXIMOS PASSOS: Recomendações priorizadas na matriz impacto vs. esforço com responsáveis.
```

---

## ⚙️ Diretrizes para Agentes Gemini no Antigravity CLI

1. **Uso do Ambiente Python:** Toda manipulação de dados deve ser executada através do interpretador local do projeto (`.\.venv\Scripts\python.exe`), garantindo reprodutibilidade do pandas e openpyxl.
2. **Persistência de Dados Tratados:** Resultados consolidados devem ser gravados em `05_analytics_e_artifacts/` seguindo UTF-8 com BOM e delimitador adequado.
3. **Artifacts e Relatórios:** Quando gerar relatórios extensos ou tabelas de cruzamento, apresente sumários executivos no terminal e gere artifacts Markdown no diretório oficial de artifacts para inspeção da diretoria.
4. **Alinhamento com Metas Corporativas (JSON de Governança):**
   - Margem Bruta Mínima: **32,0%**
   - Teto Máximo de Desconto: **18,0%**
   - Taxa Máxima de Devolução: **5,0%**
   - Cobertura Crítica de Estoque: **< 15 dias**

---

## 📚 Documentos de Referência Disponíveis

- [Glossário de Métricas](references/glossario_novametrica.md): Dicionário de termos financeiros e operacionais da NovaMétrica.
- [Template de Deck](references/template_deck.md): Estrutura em 5 atos para apresentações executivas.
- [Template de Relatório](references/template_relatorio.md): Modelo pré-estruturado em 6 blocos com marcadores de certeza.

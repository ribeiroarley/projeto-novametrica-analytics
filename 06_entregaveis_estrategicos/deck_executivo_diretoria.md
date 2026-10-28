# Apresentação Executiva: Caso NovaMétrica (Diretoria Executiva)

**Período:** 1º Quadrimestre de 2026 (Jan–Abr)  
**Governança:** Antigravity CLI + Gemini Developer Guidelines  
**Base Analítica:** `vendas_novametrica_clean.csv` (724 pedidos) & `raw_posicao_inventario_skus.xlsx` (20 SKUs)  

---

## SLIDE 1 — ATO 1: O CENÁRIO
**Título:** Desempenho Consolidado do Quadrimestre

> Número de destaque:  
> **R$ 374.588,22** — Receita líquida faturada no período (jan–abr/2026).

- 724 pedidos auditados e integrados com sucesso.
- Margem bruta consolidada robusta de **42,93%** (R$ 160.824,62).
- Ticket médio realizado de **R$ 517,39**.

*(Fontes: vendas_novametrica_clean.csv | 01_pipeline_eda_novametrica.py)*

---

## SLIDE 2 — ATO 2: O QUE ESTÁ FUNCIONANDO
**Título:** Resiliência Comercial das Operações Regulares

> Número de destaque:  
> **43,97%** — Margem bruta média das vendas regulares sem campanha.

- ✅ **Vendas Regulares:** Geraram **R$ 289,5k** (77,3% da receita líquida total).
- ✅ **Disciplina de Pricing:** Desconto médio de apenas **4,34%** fora de promoções.
- ✅ **Canais Equilibrados:** E-commerce e Lojas Físicas mantêm margem saudável acima de 40%.

*(Fontes: vendas_novametrica_clean.csv | config_limiares_e_alertas_kpis.json)*

---

## SLIDE 3 — ATO 3: PONTOS DE ATENÇÃO
**Título:** Três Alertas Críticos que Exigem Decisão

- ⚠️ **Queima de Margem na Semana do Consumidor:** Queda de **8,98 p.p.** de margem (34,99%) com desconto agressivo de **17,95%** sem escala (apenas 29 pedidos).
- ⚠️ **Ruptura Iminente de Estoque:** SKUs `EL-001`, `CA-003` e `MO-002` com estoque para **~10,6 dias** e **R$ 20.090,72/mês** expostos.
- ⚠️ **Logística Isenta de Devoluções:** Pedidos devolvidos chegaram **0,48 dias mais rápido** que os normais (r = +0,0732); falha reside no produto.

*(Fontes: vendas_novametrica_clean.csv | raw_posicao_inventario_skus.xlsx)*

---

## SLIDE 4 — ATO 4: A INTERPRETAÇÃO
**Título:** Diagnóstico Estratégico Integrado

| Grau de Certeza | Afirmação Analítica |
|:---|:---|
| `[CONFIRMADO]` | Logística de frete é eficiente (4,85d em devoluções); atrasos não causam devoluções. |
| `[PROVÁVEL]` | Descontos isolados de até 18% destroem valor sem alavancar elasticidade de demanda. |
| `[HIPÓTESE]` | Devoluções decorrem de discrepância de expectativa ou falhas de especificações de catálogo. |

> **Diretriz Executiva:** Concentrar governança imediata em compras e pricing, preservando a esteira operacional logística.

---

## SLIDE 5 — ATO 5: PRÓXIMOS PASSOS
**Título:** Quatro Decisões Imediatas do C-Level

1. **Reposição Emergencial (7 dias):** Emitir PO de 30 un para `EL-001`, `CA-003` e `MO-002` com fornecedores homologados.
2. **Nova Trava de Desconto (30 dias):** Teto de 12% na Semana do Consumidor ou condicionamento de 18% a bundles de alta margem.
3. **Auditoria de Devoluções (30 dias):** Implementar campo obrigatório `Motivo_Devolucao` no checkout/SAC.
4. **Desmobilização de Capital (90 dias):** Promoção de queima para itens de baixo giro (`ES-001`, `SP-002`, `PT-002`).

*(Alinhamento: Matriz Esforço × Impacto | Gerências Comercial, Suprimentos e SAC)*

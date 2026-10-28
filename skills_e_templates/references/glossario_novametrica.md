# Glossário NovaMétrica — Termos e Definições Padrão

> Use este glossário para garantir consistência de linguagem em todos os entregáveis executivos.
> Sempre que um termo aparecer em análise ou relatório, verificar a definição padrão aqui.

---

## Métricas Financeiras

| Termo | Definição NovaMétrica | Campo no CSV |
|---|---|---|
| **Receita Bruta** | Valor total antes de descontos | `Receita_Bruta` |
| **Valor do Desconto** | Valor monetário do desconto aplicado | `Valor_Desconto` |
| **Receita Líquida** | Receita Bruta menos Valor do Desconto | `Receita_Liquida` |
| **Custo Total** | Custo direto associado ao pedido | `Custo_Total` |
| **Margem Bruta** | Receita Líquida menos Custo Total | `Margem_Bruta` |
| **Desconto %** | Percentual de desconto sobre Receita Bruta | `Desconto_Perc` |

---

## Dimensões de Análise

| Dimensão | Valores Possíveis | Campo no CSV |
|---|---|---|
| **Canal** | E-commerce, Loja Física, Marketplace, etc. | `Canal` |
| **Região** | Norte, Nordeste, Centro-Oeste, Sudeste, Sul | `Regiao` |
| **Categoria** | [[Categorias dos produtos]] | `Categoria` |
| **Campanha** | Nome da campanha promocional | `Campanha` |
| **Origem da Campanha** | Canal de mídia da campanha | `Origem_Campanha` |
| **Forma de Pagamento** | Cartão, Boleto, Pix, etc. | `Forma_Pagamento` |

---

## Status de Pedidos

| Status | Significado para Análise |
|---|---|
| **Entregue** | Pedido concluído — incluir em receita |
| **Cancelado** | Não gera receita — excluir de métricas financeiras |
| **Devolvido** | Campo `Devolvido = Sim` — excluir da receita líquida final |
| **Em trânsito** | Receita ainda não confirmada — tratar com cautela |

> ⚠️ **Regra crítica:** Sempre filtrar pedidos com `Status_Pedido = Cancelado` e
> `Devolvido = Sim` antes de calcular qualquer métrica de receita ou margem.

---

## Indicadores Operacionais

| Indicador | Definição | Campo |
|---|---|---|
| **Prazo de Entrega** | Dias entre pedido e entrega | `Prazo_Entrega_Dias` |
| **Taxa de Devolução** | % de pedidos devolvidos sobre total | Calculado: `Devolvido / Total` |
| **Avaliação Média** | Nota média do cliente (1–5) | `Avaliacao_Cliente` |

---

## Termos de Negócio

| Termo | Definição no Contexto NovaMétrica |
|---|---|
| **Ruptura de estoque** | SKU com estoque zero ou abaixo do ponto de pedido |
| **Excesso de estoque** | SKU com cobertura acima de 90 dias sem giro |
| **Política comercial** | Regras de desconto máximo por categoria/canal |
| **Campanha eficiente** | Campanha com receita atribuída superior ao custo estimado |
| **Margem saudável** | Margem bruta acima de 30% (referência interna NovaMétrica) |
| **SKU** | Unidade de manutenção de estoque — código único de produto |

---

## Sinalizadores de Certeza (Padrão da Skill)

| Sinalizador | Quando usar |
|---|---|
| `[CONFIRMADO]` | Evidência direta e quantificável nos dados disponíveis |
| `[PROVÁVEL]` | Padrão consistente nos dados, mas sem confirmação causal |
| `[HIPÓTESE]` | Raciocínio plausível, sem evidência confirmada nos dados |
| `[DADO AUSENTE]` | Informação necessária não disponível nas bases atuais |
| `[INCONSISTÊNCIA]` | Campo com valores contraditórios ou fora do padrão esperado |

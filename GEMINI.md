# Diretrizes Globais do Projeto NovaMétrica (Antigravity CLI + Gemini)

Consulte [`GEMINI_CONTEXT.md`](GEMINI_CONTEXT.md) e [`.antigravity/rules.json`](.antigravity/rules.json) para os detalhes operacionais completos.

---

## 🚨 REGRAS PÉTREAS MANDATÓRIAS:
1. **Regra de Isolamento Virtual:** Toda e qualquer execução de código, auditoria ou análise estatística DEVE ser feita exclusivamente utilizando o interpretador do ambiente virtual isolado: `.\.venv\Scripts\python.exe`. O uso do Python global é estritamente proibido.
2. **Regra de Evidência e Rastreabilidade Analítica (Proibição de Scripts na Raiz):** Nenhum script Python (`.py`), notebook (`.ipynb`) ou código de profiling deve ser salvo solto na raiz. Todo script de exploração, checagem, saneamento ou teste de hipótese DEVE ser obrigatoriamente versionado e salvo dentro da pasta `07_scripts_exploratorios/` como evidência documental de pesquisa.

---

## Regras Operacionais de Governança:
1. **Governança Epistêmica:** Aplique rigorosamente a separação entre `[CONFIRMADO]`, `[PROVÁVEL]`, `[HIPÓTESE]`, `[DADO AUSENTE]` e `[INCONSISTÊNCIA]`.
2. **Limiares de KPI da NovaMétrica:**
   - Margem Bruta Mínima: 32,0%
   - Teto Máximo de Desconto: 18,0%
   - Taxa Máxima de Devolução: 5,0%
   - Cobertura de Estoque de Segurança: > 15 dias
3. **Camada de Analytics:** Use sempre a base limpa [`05_analytics_e_artifacts/vendas_novametrica_clean.csv`](05_analytics_e_artifacts/vendas_novametrica_clean.csv) gerada pelo pipeline [`07_scripts_exploratorios/01_pipeline_eda_novametrica.py`](07_scripts_exploratorios/01_pipeline_eda_novametrica.py).
4. **Recomendações Executivas:** Estruture sempre com `[AÇÃO]`, `[EVIDÊNCIA]`, `[IMPACTO ESTIMADO]` e `[RESPONSÁVEL SUGERIDO]`.

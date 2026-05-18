# Fase F1 — Papers Academicos e Referencias

**Status**: PENDENTE
**Dependencias**: Nenhuma
**Bloqueia**: F3, F4, F5

---

## Objetivo

Pesquisar, resumir e catalogar os papers academicos sobre modelos de regressao ML.

---

## Arquivo de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/regression-ml/papers.md`

---

## Papers a Cobrir

| # | Paper | Autores | Ano | Foco |
|---|-------|---------|-----|------|
| 1 | Random Forests | Breiman | 2001 | Random Forest para regressao |
| 2 | Greedy Function Approximation: A Gradient Boosting Machine | Friedman | 2001 | GBM original |
| 3 | XGBoost: A Scalable Tree Boosting System | Chen, Guestrin | 2016 | XGBoost para regressao |
| 4 | A Tutorial on Support Vector Regression | Smola, Scholkopf | 2004 | SVR fundamentos e kernels |
| 5 | LightGBM: A Highly Efficient Gradient Boosting Decision Tree | Ke, Meng et al. | 2017 | LightGBM para grandes datasets |
| 6 | A Unified Approach to Interpreting Model Predictions (SHAP) | Lundberg, Lee | 2017 | SHAP values |
| 7 | The Elements of Statistical Learning (Cap. 9, 10, 15) | Hastie, Tibshirani, Friedman | 2009 | Referencia completa de metodos tree-based |

---

## Formato do Arquivo de Saida

```markdown
---
slug: regression-ml-papers
name: "Academic Papers & References — Regression ML Models"
domain: regression-ml
type: reference-guide
status: draft
tags: [regression-ml, papers, academic, xgboost, random-forest, svr, shap, gradient-boosting]
---

# Academic Papers & References — Regression ML Models

## 1. Breiman (2001) — Random Forests

### Summary
[3-5 paragrafos]

### Relevance to Model Validation
[Como se aplica]

### Key Takeaways
- [pontos]

### Citation
[APA format]

---
```

---

## Etapas de Implementacao

### Etapa 1: Pesquisar cada paper na web
### Etapa 2: Redigir resumos, relevancia, takeaways, citacao APA
### Etapa 3: Montar papers.md com frontmatter YAML
### Etapa 4: Verificacao

```bash
ls -la /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/regression-ml/papers.md
grep -c "^## " /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/regression-ml/papers.md
```

---

## Criterios de Aceite

- [x] Arquivo `papers.md` criado no destino correto
- [x] Frontmatter YAML valido com slug, name, domain, type, status, tags
- [x] Todos os 7 papers cobertos com resumo, relevancia, takeaways e citacao
- [x] Cada resumo tem pelo menos 3 paragrafos
- [x] Cada paper tem pelo menos 3 key takeaways
- [x] Citacoes em formato APA
- [x] Conteudo buscado na web (nao inventado)

---

## Ferramentas Necessarias

- **WebSearch**, **WebFetch**, **Write**

---

**End of Specification**

# Fase F1 — Papers Academicos e Referencias

**Status**: PENDENTE
**Dependencias**: Nenhuma
**Bloqueia**: F3, F4, F5

---

## Objetivo

Pesquisar, resumir e catalogar os papers academicos sobre modelos de classificacao.

---

## Arquivo de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/classification/papers.md`

---

## Papers a Cobrir

| # | Paper | Autores | Ano | Foco |
|---|-------|---------|-----|------|
| 1 | Random Forests | Breiman | 2001 | Fundamento de Random Forests |
| 2 | XGBoost: A Scalable Tree Boosting System | Chen, Guestrin | 2016 | XGBoost e gradient boosting |
| 3 | A Unified Approach to Interpreting Model Predictions (SHAP) | Lundberg, Lee | 2017 | SHAP values para interpretabilidade |
| 4 | LightGBM: A Highly Efficient Gradient Boosting Decision Tree | Ke, Meng, Finley et al. | 2017 | LightGBM para grandes datasets |
| 5 | Support-Vector Networks | Cortes, Vapnik | 1995 | SVM para classificacao |
| 6 | Fairness and Abstraction in Sociotechnical Systems | Selbst, Boyd, Friedler et al. | 2019 | Fairness em ML |
| 7 | "Why Should I Trust You?" Explaining the Predictions of Any Classifier (LIME) | Ribeiro, Singh, Guestrin | 2016 | LIME para interpretabilidade local |

---

## Formato do Arquivo de Saida

```markdown
---
slug: classification-papers
name: "Academic Papers & References — Classification Models"
domain: classification
type: reference-guide
status: draft
tags: [classification, papers, academic, random-forest, xgboost, shap, fairness]
---

# Academic Papers & References — Classification Models

## 1. Breiman (2001) — Random Forests

### Summary
[3-5 paragrafos]

### Relevance to Model Validation
[Como se aplica]

### Key Takeaways
- [ponto 1]
- [ponto 2]
- [ponto 3]

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
ls -la /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/classification/papers.md
grep -c "^## " /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/classification/papers.md
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

# Fase F1 — Papers Academicos e Referencias

**Status**: PENDENTE
**Dependencias**: Nenhuma
**Bloqueia**: F3, F4, F5

---

## Objetivo

Pesquisar, resumir e catalogar os papers academicos sobre metodos ensemble.

---

## Arquivo de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/ensemble/papers.md`

---

## Papers a Cobrir

| # | Paper | Autores | Ano | Foco |
|---|-------|---------|-----|------|
| 1 | Bagging Predictors | Breiman | 1996 | Fundamento de bagging |
| 2 | A Decision-Theoretic Generalization of On-Line Learning and an Application to Boosting | Freund, Schapire | 1997 | AdaBoost original |
| 3 | Stacked Generalization | Wolpert | 1992 | Stacking como meta-aprendizado |
| 4 | Random Forests | Breiman | 2001 | RF como ensemble de arvores |
| 5 | Greedy Function Approximation: A Gradient Boosting Machine | Friedman | 2001 | GBM framework |
| 6 | An Empirical Comparison of Voting Classification Algorithms | Opitz, Maclin | 1999 | Comparacao de metodos ensemble |
| 7 | Ensemble Methods: Foundations and Algorithms | Zhou | 2012 | Livro-texto de ensembles |

---

## Formato do Arquivo de Saida

```markdown
---
slug: ensemble-papers
name: "Academic Papers & References — Ensemble Models"
domain: ensemble
type: reference-guide
status: draft
tags: [ensemble, papers, academic, bagging, boosting, stacking, random-forest]
---

# Academic Papers & References — Ensemble Models

## 1. Breiman (1996) — Bagging Predictors

### Summary
[3-5 paragrafos]

### Relevance to Model Validation
[Como se aplica]

### Key Takeaways
- [pontos]

### Citation
[APA format]
```

---

## Etapas de Implementacao

### Etapa 1: Pesquisar cada paper na web
### Etapa 2: Redigir resumos, relevancia, takeaways, citacao APA
### Etapa 3: Montar papers.md com frontmatter YAML
### Etapa 4: Verificacao

```bash
ls -la /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/ensemble/papers.md
grep -c "^## " /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/ensemble/papers.md
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

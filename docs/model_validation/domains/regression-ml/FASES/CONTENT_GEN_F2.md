# Fase F2 — Noticias e Artigos

**Status**: CONCLUIDO
**Dependencias**: Nenhuma
**Bloqueia**: Nenhuma

---

## Objetivo

Pesquisar e redigir artigos sobre regressao ML, seguindo o template news.

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/news/`

## Template: `/home/guhaase/projetos/ModelRiskLab/mrl-content-files/templates/news.md`

---

## Artigos a Gerar

| # | Titulo Sugerido | Tipo | Slug |
|---|-----------------|------|------|
| 1 | Tree-Based Regression: From Decision Trees to XGBoost | Tutorial | tree-based-regression-decision-trees-xgboost |
| 2 | SVR vs Tree-Based Models: When to Use What for Regression | Comparacao | svr-vs-tree-based-models-regression |
| 3 | Feature Importance in Regression: Permutation vs SHAP | Tecnica | feature-importance-regression-permutation-shap |
| 4 | Residual Analysis for ML Regression Models | Tutorial | residual-analysis-ml-regression-models |
| 5 | Quantile Regression with Gradient Boosting | Tecnica | quantile-regression-gradient-boosting |
| 6 | Overfitting in Regression Trees: Detection and Prevention | Pitfalls | overfitting-regression-trees-detection-prevention |
| 7 | ML Regression in Real Estate Valuation: A Case Study | Case study | ml-regression-real-estate-valuation-case-study |

---

## Formato: seguir template `news.md`

Salvar como: `2026-03-16_<slug>.md`

Cada artigo: minimo 800 palavras, Key Takeaways, References, tags incluem "regression-ml".

---

## Etapas de Implementacao

### Etapa 1: Pesquisa — buscar conteudo atualizado para cada topico
### Etapa 2: Redacao — minimo 800 palavras, codigo Python quando aplicavel
### Etapa 3: Salvamento — salvar no diretorio de destino
### Etapa 4: Verificacao

```bash
ls -la /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/news/2026-03-16_*{tree-based,svr,feature-importance,residual,quantile,overfitting,real-estate}*.md
```

---

## Criterios de Aceite

- [x] 7 artigos criados no diretorio de destino
- [x] Todos seguem o template news.md com frontmatter YAML valido
- [x] Cada artigo tem no minimo 800 palavras
- [x] Cada artigo tem secao de Key Takeaways
- [x] Cada artigo tem secao de References
- [x] Conteudo baseado em pesquisa web (nao inventado)
- [x] Tags incluem "regression-ml" em todos os artigos

---

## Ferramentas Necessarias

- **WebSearch**, **WebFetch**, **Write**

---

**End of Specification**

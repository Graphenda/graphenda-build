# Fase F2 — Noticias e Artigos

**Status**: CONCLUIDO
**Dependencias**: Nenhuma
**Bloqueia**: Nenhuma

---

## Objetivo

Pesquisar e redigir artigos sobre modelos de classificacao, seguindo o template news.

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/news/`

## Template: `/home/guhaase/projetos/ModelRiskLab/mrl-content-files/templates/news.md`

---

## Artigos a Gerar

| # | Titulo Sugerido | Tipo | Slug |
|---|-----------------|------|------|
| 1 | Random Forest vs XGBoost: When to Use Which | Comparacao | random-forest-vs-xgboost-when-to-use |
| 2 | Understanding AUC-ROC and Precision-Recall Curves | Tutorial | understanding-auc-roc-precision-recall |
| 3 | SHAP Values Explained: A Practical Guide | Tutorial | shap-values-explained-practical-guide |
| 4 | Dealing with Imbalanced Classes in Classification | Tecnica | dealing-imbalanced-classes-classification |
| 5 | Fairness in Machine Learning: A Practical Perspective | Regulatorio | fairness-machine-learning-practical-perspective |
| 6 | Hyperparameter Tuning: Grid Search, Random Search, and Bayesian Optimization | Tutorial | hyperparameter-tuning-grid-random-bayesian |
| 7 | Model Validation for Classification in Banking Under SR 11-7 | Regulatorio | model-validation-classification-banking-sr-11-7 |

---

## Formato: seguir template `news.md`

Salvar como: `2026-03-16_<slug>.md`

Cada artigo: minimo 800 palavras, Key Takeaways, References, tags incluem "classification".

---

## Etapas de Implementacao

### Etapa 1: Pesquisa — buscar conteudo atualizado para cada topico
### Etapa 2: Redacao — minimo 800 palavras, codigo Python quando aplicavel
### Etapa 3: Salvamento — salvar no diretorio de destino
### Etapa 4: Verificacao

```bash
ls -la /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/news/2026-03-16_*{random-forest,auc-roc,shap,imbalanced,fairness,hyperparameter,classification}*.md
```

---

## Criterios de Aceite

- [x] 7 artigos criados no diretorio de destino
- [x] Todos seguem o template news.md com frontmatter YAML valido
- [x] Cada artigo tem no minimo 800 palavras
- [x] Cada artigo tem secao de Key Takeaways
- [x] Cada artigo tem secao de References
- [x] Conteudo baseado em pesquisa web (nao inventado)
- [x] Tags incluem "classification" em todos os artigos

---

## Ferramentas Necessarias

- **WebSearch**, **WebFetch**, **Write**

---

**End of Specification**

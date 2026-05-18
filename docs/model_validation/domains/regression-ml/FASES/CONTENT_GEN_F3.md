# Fase F3 — Guias Explicativos

**Status**: COMPLETO
**Dependencias**: F1 (para referencias dos papers)
**Bloqueia**: F4, F5

---

## Objetivo

Criar 5 guias explicativos completos sobre modelos de regressao ML.

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/regression-ml/`

---

## Guias a Gerar

### 1. overview.md — Visao Geral de Regressao ML

**Conteudo obrigatorio:**
- Regressao ML vs regressao estatistica: quando usar cada uma
- Trade-off entre interpretabilidade e performance preditiva
- Categorias: tree-based, kernel-based, instance-based
- Quando ML supera modelos lineares: nao-linearidades, interacoes
- Pipeline tipico: feature engineering, treino, validacao, deploy

**Pesquisa web:** buscar aplicacoes recentes, comparacoes ML vs estatistica em industria

### 2. models.md — Tipos de Modelos de Regressao ML

**Conteudo obrigatorio:**
- Decision Tree Regressor: CART, criterios de split (MSE, MAE)
- Random Forest Regressor: bagging, OOB score, feature importance
- Gradient Boosting Regressor: learning rate, profundidade, shrinkage
- XGBoost Regressor: regularizacao L1/L2, column subsampling
- LightGBM Regressor: leaf-wise growth, histogram binning
- CatBoost Regressor: ordered boosting, symmetric trees
- SVR: kernels (RBF, linear, poly), epsilon-insensitive loss
- KNN Regressor: distancias, ponderacao, escolha de K

**Pesquisa web:** buscar benchmarks, comparacoes em competicoes Kaggle

### 3. validation.md — Validacao de Modelos de Regressao ML

**Conteudo obrigatorio:**
- Cross-validation para regressao (k-fold, repeated k-fold)
- Analise de residuos: patterns, heteroscedasticidade, outliers
- Residuos vs preditos, residuos vs features
- Learning curves: deteccao de overfitting/underfitting
- Comparacao de modelos via metricas out-of-sample
- SHAP para validacao de relacoes esperadas
- Analise de extrapolacao: previsao fora do range de treino

**Pesquisa web:** buscar melhores praticas, limitacoes de tree-based em extrapolacao

### 4. metrics.md — Metricas de Regressao ML

**Conteudo obrigatorio:**
- RMSE: penaliza erros grandes
- MAE: metrica robusta a outliers
- MAPE: erro percentual (cuidado com zeros)
- R² e Adjusted R²: explicacao de variancia
- Quantile loss: para regressao quantilica
- Huber loss: combinacao de MSE e MAE
- Relative metrics: comparacao com baseline (naive, media)

**Pesquisa web:** buscar debates sobre metricas, quando usar cada uma

### 5. pitfalls.md — Armadilhas e Erros Comuns

**Conteudo obrigatorio:**
- Nao fazer analise de residuos em modelos ML
- Ignorar extrapolacao (tree-based models sao flat fora do range)
- Feature leakage no pipeline de feature engineering
- Overfitting com arvores muito profundas
- Confiar apenas em feature importance de impureza (biased para alta cardinalidade)
- Nao escalar features para SVR e KNN
- Ignorar heteroscedasticidade nos residuos

**Pesquisa web:** buscar case studies de falhas (Zillow Offers, etc.)

---

## Formato de Cada Guia

```markdown
---
slug: regression-ml-<nome>
name: "<Titulo do Guia>"
domain: regression-ml
type: guide
difficulty: intermediate
status: draft
tags: [regression-ml, <tags-especificas>]
references:
  - title: "<titulo>"
    authors: "<autores>"
    year: <ano>
    type: paper
---
```

Cada guia: minimo 1500 palavras, formulas LaTeX, tabelas comparativas, referencias da F1.

---

## Etapas de Implementacao

### Etapa 1: Ler papers.md (F1) e spec do dominio
### Etapa 2: Pesquisa complementar na web
### Etapa 3: Redacao dos 5 guias
### Etapa 4: Verificacao

```bash
ls -la /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/regression-ml/
wc -l /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/regression-ml/*.md
```

---

## Criterios de Aceite

- [x] 5 guias criados: overview.md, models.md, validation.md, metrics.md, pitfalls.md
- [x] Alem dos 5 guias, papers.md da F1 tambem presente no diretorio
- [x] Todos com frontmatter YAML valido (slug, name, domain, type, difficulty, status, tags)
- [x] Cada guia com minimo de 1500 palavras
- [x] Formulas LaTeX incluidas onde necessario (MSE, MAE, Huber, quantile loss)
- [x] Referencias cruzadas aos papers da F1
- [x] Conteudo baseado em pesquisa web
- [x] Tom tecnico e adequado para profissionais de model validation

---

## Ferramentas Necessarias

- **Read**, **WebSearch**, **WebFetch**, **Write**

---

**End of Specification**

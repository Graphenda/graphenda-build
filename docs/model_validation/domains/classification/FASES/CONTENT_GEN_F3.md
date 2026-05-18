# Fase F3 — Guias Explicativos

**Status**: COMPLETO
**Dependencias**: F1 (para referencias dos papers)
**Bloqueia**: F4, F5

---

## Objetivo

Criar 5 guias explicativos completos sobre modelos de classificacao.

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/classification/`

---

## Guias a Gerar

### 1. overview.md — Visao Geral de Modelos de Classificacao

**Conteudo obrigatorio:**
- O que sao modelos de classificacao e suas categorias
- Classificacao binaria vs multiclasse vs multilabel
- Trade-off entre interpretabilidade e performance
- Discriminacao vs calibracao: conceitos distintos
- Quando usar modelos simples vs complexos
- Fairness e etica em modelos de classificacao

**Pesquisa web:** buscar tendencias recentes, regulacao de ML em bancos, EU AI Act

### 2. models.md — Tipos de Modelos de Classificacao

**Conteudo obrigatorio:**
- Decision Tree: CART, criterios de split (Gini, entropia)
- Random Forest: bagging de arvores, feature importance
- XGBoost: gradient boosting, regularizacao, hiperparametros-chave
- LightGBM: histogram-based, categorical features nativas
- CatBoost: ordered boosting, tratamento de categoricas
- SVM: kernel trick, margens, hiperparametros C e gamma
- K-Nearest Neighbors: distancias, escolha de K
- Naive Bayes: Gaussian, Multinomial, Bernoulli

**Pesquisa web:** buscar benchmarks recentes, comparacoes em competicoes (Kaggle)

### 3. validation.md — Validacao de Modelos de Classificacao

**Conteudo obrigatorio:**
- Estrategias de split: holdout, k-fold, stratified k-fold
- Curva ROC e selecao de threshold
- Curva Precision-Recall para classes desbalanceadas
- Matriz de confusao e metricas derivadas
- Calibracao: Platt scaling, isotonic regression
- SHAP e LIME para explicabilidade
- Fairness metrics: demographic parity, equalized odds
- Population Stability Index (PSI) para monitoramento

**Pesquisa web:** buscar melhores praticas SR 11-7, EU AI Act, frameworks de fairness

### 4. metrics.md — Metricas de Classificacao

**Conteudo obrigatorio:**
- AUC-ROC: interpretacao e limitacoes
- AUC-PR: melhor para classes desbalanceadas
- Accuracy, Precision, Recall, F1-Score
- Log-loss (cross-entropy)
- Cohen's Kappa: concordancia ajustada por chance
- Matthews Correlation Coefficient (MCC)
- KS statistic: separacao de distribuicoes
- Gini coefficient: 2*AUC - 1

**Pesquisa web:** buscar debates sobre metricas, quando usar cada uma

### 5. pitfalls.md — Armadilhas e Erros Comuns

**Conteudo obrigatorio:**
- Usar accuracy com classes desbalanceadas
- Nao calibrar probabilidades antes de usar como scores
- Data leakage durante feature engineering
- Overfitting por nao usar cross-validation
- Ignorar fairness e bias sistematico
- Feature importance instavel entre runs (RF)
- Nao monitorar concept drift em producao

**Pesquisa web:** buscar case studies reais (Apple Card bias, Zillow, etc.)

---

## Formato de Cada Guia

```markdown
---
slug: classification-<nome>
name: "<Titulo do Guia>"
domain: classification
type: guide
difficulty: intermediate
status: draft
tags: [classification, <tags-especificas>]
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
ls -la /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/classification/
wc -l /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/classification/*.md
```

---

## Criterios de Aceite

- [x] 5 guias criados: overview.md, models.md, validation.md, metrics.md, pitfalls.md
- [x] Alem dos 5 guias, papers.md da F1 tambem presente no diretorio
- [x] Todos com frontmatter YAML valido (slug, name, domain, type, difficulty, status, tags)
- [x] Cada guia com minimo de 1500 palavras
- [x] Formulas LaTeX incluidas onde necessario (Gini, entropy, cross-entropy)
- [x] Referencias cruzadas aos papers da F1
- [x] Conteudo baseado em pesquisa web
- [x] Tom tecnico e adequado para profissionais de model validation

---

## Ferramentas Necessarias

- **Read**, **WebSearch**, **WebFetch**, **Write**

---

**End of Specification**

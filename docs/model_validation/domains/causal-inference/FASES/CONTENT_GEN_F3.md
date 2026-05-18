# Fase F3 — Guias Explicativos

**Status**: COMPLETO
**Dependencias**: F1
**Bloqueia**: F4, F5

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/causal-inference/`

---

## Guias a Gerar

### 1. overview.md
- O que e inferencia causal e por que difere de correlacao
- Framework de resultados potenciais (Rubin) vs DAGs (Pearl)
- SUTVA e assignment mechanism
- Quando usar: politicas publicas, marketing, medicina, credito
- Hierarquia de evidencia: RCT > quasi-experimental > observacional
- Relacao entre causal inference e model validation

### 2. models.md
- Difference-in-Differences (DiD): parallel trends, staggered adoption
- Regression Discontinuity Design (RDD): sharp vs fuzzy
- Instrumental Variables (IV): relevance, exclusion, 2SLS
- Propensity Score: matching, weighting (IPW), stratification
- Causal Forests (Athey-Imbens): efeitos heterogeneos
- Double Machine Learning (DML): Chernozhukov et al.
- Synthetic Control Method: para estudos com poucas unidades tratadas
- DAGs e do-calculus: identificacao causal via grafos

### 3. validation.md
- Checklist de validacao para modelos de inferencia causal
- Validacao de premissas por metodo:
  - DiD: teste de parallel trends pre-tratamento
  - RDD: continuidade de covariaveis no cutoff, bandwidth selection
  - IV: teste de instrumento fraco (F > 10), exclusion restriction
  - PSM: balanceamento pos-matching (standardized differences)
- Analise de sensibilidade: Rosenbaum bounds, E-value
- Placebo tests: tratamento falso em periodo/grupo errado
- Robustez a especificacao: variar controles, janelas, bandwidths
- Validacao cruzada para causal forests (honest estimation)

### 4. metrics.md
- ATE (Average Treatment Effect): efeito medio
- ATT (Average Treatment Effect on the Treated): efeito nos tratados
- CATE (Conditional Average Treatment Effect): efeito heterogeneo
- Standardized Mean Difference (SMD): balanceamento pos-matching
- First-stage F-statistic: forca do instrumento (IV)
- Bandwidth selection metrics (RDD): MSE-optimal, coverage
- E-value: robustez a confounding nao observado
- RMSE de previsao de efeitos heterogeneos (causal forests)

### 5. pitfalls.md
- Confundir correlacao com causalidade (o erro mais comum)
- DiD com parallel trends violados e nao testados
- Propensity score matching com covariaveis pos-tratamento
- Instrumento fraco que amplifica bias em vez de corrigi-lo
- RDD com manipulacao do running variable no cutoff
- Ignorar analise de sensibilidade a confounders nao observados
- Over-matching: balancear em variaveis mediators
- Nao reportar incerteza nos efeitos estimados

---

## Formato: `slug: causal-inference-<nome>`, `domain: causal-inference`, `type: guide`

Cada guia: minimo 1500 palavras, formulas LaTeX (ATE, ATT, DiD estimator, propensity score, E-value), referencias da F1.

---

## Criterios de Aceite

- [x] 5 guias criados: overview.md, models.md, validation.md, metrics.md, pitfalls.md
- [x] papers.md da F1 tambem presente
- [x] Todos com frontmatter YAML valido
- [x] Cada guia com minimo de 1500 palavras
- [x] Formulas LaTeX incluidas (ATE, DiD estimator, propensity score, E-value)
- [x] Referencias cruzadas aos papers da F1
- [x] Conteudo baseado em pesquisa web

---

**End of Specification**

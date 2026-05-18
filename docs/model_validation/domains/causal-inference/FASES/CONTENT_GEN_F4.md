# Fase F4 — Codigo de Exemplo

**Status**: COMPLETO
**Dependencias**: F3
**Bloqueia**: F5

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/causal-inference/`

---

## Arquivos a Gerar

### Modeling (5 arquivos)

#### 1. modeling/did_analysis.py
- Difference-in-Differences com statsmodels e linearmodels
- Teste de parallel trends pre-tratamento
- Event study plot (leads and lags)
- DiD com multiplos periodos (staggered)
- Dataset: LaLonde NSW

#### 2. modeling/rdd_analysis.py
- Regression Discontinuity com rdrobust
- Bandwidth selection (MSE-optimal)
- Visualizacao: scatter com fit local ao redor do cutoff
- Testes de falsificacao: continuidade de covariaveis
- Dataset: LaLonde NSW

#### 3. modeling/propensity_score.py
- Propensity score estimation com regressao logistica e GBM
- Matching (nearest neighbor, caliper)
- IPW (Inverse Probability Weighting)
- Balanceamento: SMD antes e depois do matching
- Dataset: LaLonde NSW

#### 4. modeling/causal_forest.py
- Causal Forest com econml (EconML da Microsoft)
- Honest estimation com splitting
- CATE estimation e feature importance
- Visualizacao de efeitos heterogeneos
- Dataset: LaLonde NSW

#### 5. modeling/double_ml.py
- Double Machine Learning com econml
- Nuisance functions com XGBoost
- Cross-fitting procedure
- Comparacao com OLS e IPW
- Dataset: LaLonde NSW

### Validation (2 arquivos)

#### 6. validation/sensitivity_analysis.py
- E-value calculation para resultados observacionais
- Rosenbaum bounds para matched studies
- Contour plot: bias vs efeito causal
- Maddala test para overidentification (IV)
- Dataset: LaLonde NSW

#### 7. validation/placebo_tests.py
- Placebo treatment no periodo pre-tratamento
- Placebo outcome em variavel nao afetada
- Permutation test de assignment
- Falsification tests para RDD
- Dataset: LaLonde NSW

### Visualization (1 arquivo)

#### 8. visualization/causal_plots.py
- Event study plot (DiD com leads/lags)
- RDD scatter com fit local e cutoff
- Love plot: SMD antes e depois do matching
- CATE distribution (histogram de efeitos heterogeneos)
- Sensitivity contour plot (E-value)
- DAG visualization com graphviz
- Parallel trends test plot
- Dataset: LaLonde NSW

---

## Formato: cada script com docstring, main(), RANDOM_STATE = 42

---

## Criterios de Aceite

- [x] 8 scripts Python criados nas subpastas corretas
- [x] modeling/did_analysis.py — DiD com parallel trends test e event study
- [x] modeling/rdd_analysis.py — RDD com bandwidth selection e falsification tests
- [x] modeling/propensity_score.py — PSM com logistic + GBM, matching + IPW
- [x] modeling/causal_forest.py — Causal Forest com econml, CATE e feature importance
- [x] modeling/double_ml.py — DML com econml e XGBoost nuisance functions
- [x] validation/sensitivity_analysis.py — E-value, Rosenbaum bounds, contour plot
- [x] validation/placebo_tests.py — Placebo treatment, placebo outcome, permutation
- [x] visualization/causal_plots.py — Event study, RDD, Love plot, CATE, DAG
- [x] Todos passam verificacao de sintaxe Python
- [x] Todos tem docstring, funcoes organizadas e main()
- [x] Stack: econml + dowhy + statsmodels, LaLonde NSW como dataset principal

---

## Bibliotecas Utilizadas

| Biblioteca | Versao Minima | Uso |
|------------|---------------|-----|
| econml | >= 0.14 | Causal Forest, DML, CATE estimation |
| dowhy | >= 0.10 | Framework end-to-end de inferencia causal |
| statsmodels | >= 0.14 | OLS, IV (2SLS), DiD classico |
| linearmodels | >= 5.0 | IV, panel, DiD avancado |
| scikit-learn | >= 1.3 | Logistic regression, GBM, metricas |
| xgboost | >= 1.7 | Nuisance functions para DML |
| matplotlib | >= 3.7 | Visualizacoes |
| seaborn | >= 0.12 | Visualizacoes |
| graphviz | >= 0.20 | DAG visualization |

---

**End of Specification**

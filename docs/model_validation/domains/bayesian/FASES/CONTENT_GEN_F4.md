# Fase F4 — Codigo de Exemplo

**Status**: COMPLETO
**Dependencias**: F3
**Bloqueia**: F5

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/bayesian/`

---

## Arquivos a Gerar

### Modeling (5 arquivos)

#### 1. modeling/bayesian_regression.py
- Regressao linear bayesiana com PyMC
- Definicao de priors (Normal, Student-t, Cauchy)
- Inferencia via NUTS sampler
- Posterior summary e intervalos de credibilidade
- Dataset: sintetico ou California Housing (sklearn)

#### 2. modeling/hierarchical_model.py
- Modelo hierarquico com PyMC
- Varying intercepts e slopes por grupo
- Partial pooling vs no pooling vs complete pooling
- Shrinkage bayesiano
- Dataset: Radon (PyMC examples)

#### 3. modeling/gaussian_process.py
- GP regression com scikit-learn GaussianProcessRegressor
- Kernels: RBF, Matern, combinacoes
- Otimizacao de hiperparametros do kernel
- Predicao com intervalos de incerteza
- Dataset: sintetico 1D

#### 4. modeling/bayesian_classification.py
- Regressao logistica bayesiana com PyMC
- Posterior dos coeficientes e odds ratios
- Comparacao com logistica frequentista
- Predicao probabilistica com incerteza
- Dataset: Iris (sklearn) ou sintetico binario

#### 5. modeling/bsts_timeseries.py
- Bayesian Structural Time Series com PyMC
- Componentes: trend, sazonalidade
- Previsao com intervalos de credibilidade
- Comparacao com ARIMA frequentista
- Dataset: AirPassengers ou sintetico

### Validation (2 arquivos)

#### 6. validation/mcmc_diagnostics.py
- Trace plots para convergencia visual com ArviZ
- R-hat e ESS automatizados (az.summary)
- Autocorrelacao das cadeias
- Rank plots e divergence diagnostics
- BFMI check
- Dataset: modelo da F4.1 ou F4.2

#### 7. validation/model_comparison_bayesian.py
- LOO-CV com ArviZ (az.loo)
- WAIC com ArviZ (az.waic)
- Comparacao de modelos via elpd_diff (az.compare)
- Posterior predictive checks (az.plot_ppc)
- Prior predictive checks
- Dataset: modelos da F4.1 e F4.2

### Visualization (1 arquivo)

#### 8. visualization/bayesian_plots.py
- Trace plots e posterior distributions (az.plot_trace)
- Forest plot de coeficientes com HDI (az.plot_forest)
- Posterior predictive check plots (az.plot_ppc)
- GP mean + uncertainty bands
- Pair plot de posteriors (az.plot_pair)
- LOO-PIT plot para calibracao (az.plot_loo_pit)
- Dataset: modelos anteriores

---

## Formato: cada script com docstring, main(), RANDOM_STATE = 42

---

## Criterios de Aceite

- [x] 8 scripts Python criados nas subpastas corretas
- [x] modeling/bayesian_regression.py — Regressao bayesiana com PyMC e NUTS
- [x] modeling/hierarchical_model.py — Modelo hierarquico com partial pooling
- [x] modeling/gaussian_process.py — GP com kernels e uncertainty bands
- [x] modeling/bayesian_classification.py — Logistica bayesiana com PyMC
- [x] modeling/bsts_timeseries.py — BSTS com trend e sazonalidade
- [x] validation/mcmc_diagnostics.py — R-hat, ESS, trace, divergences com ArviZ
- [x] validation/model_comparison_bayesian.py — LOO-CV, WAIC, PPC com ArviZ
- [x] visualization/bayesian_plots.py — Trace, forest, PPC, GP bands, pair, LOO-PIT
- [x] Todos os scripts passam verificacao de sintaxe Python
- [x] Todos os scripts tem docstring, funcoes organizadas e main()
- [x] Codigo usa PyMC + ArviZ como stack principal

---

## Bibliotecas Utilizadas

| Biblioteca | Versao Minima | Uso |
|------------|---------------|-----|
| numpy | >= 1.24 | Arrays |
| pandas | >= 2.0 | DataFrames |
| pymc | >= 5.0 | Modelagem bayesiana, NUTS, priors |
| arviz | >= 0.16 | Diagnosticos, LOO-CV, WAIC, visualizacoes |
| scikit-learn | >= 1.3 | GaussianProcessRegressor, datasets |
| matplotlib | >= 3.7 | Visualizacoes |
| seaborn | >= 0.12 | Visualizacoes estatisticas |

---

## Ferramentas Necessarias

- **Read**, **WebSearch**, **Write**

---

**End of Specification**

# Fase F3 — Guias Explicativos

**Status**: PENDENTE
**Dependencias**: F1
**Bloqueia**: F4, F5

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/bayesian/`

---

## Guias a Gerar

### 1. overview.md
- O que e inferencia bayesiana e como difere da frequentista
- Teorema de Bayes: prior, likelihood, posterior, evidence
- Vantagens: incerteza quantificada, priors informativos, regularizacao natural
- Quando usar modelos bayesianos vs frequentistas
- Programacao probabilistica: conceito e ferramentas

### 2. models.md
- Regressao Bayesiana: linear com priors nos coeficientes
- Modelos Hierarquicos (Multilevel): priors parcialmente pooled
- Gaussian Processes: prior sobre funcoes, kernels, hiperparametros
- Modelos de Mistura Bayesianos: Dirichlet Process
- Bayesian Neural Networks: incerteza em redes neurais
- BSTS: Bayesian Structural Time Series
- Regressao logistica bayesiana

### 3. validation.md
- Diagnosticos de MCMC: trace plots, R-hat, ESS
- Geweke diagnostic e teste de convergencia
- Autocorrelacao nas cadeias
- Prior predictive check
- Posterior predictive check
- LOO-CV com PSIS
- WAIC
- Calibracao de intervalos de credibilidade

### 4. metrics.md
- LOO-CV (elpd_loo)
- WAIC
- Bayes Factor
- R-hat (potential scale reduction)
- ESS (effective sample size)
- BFMI
- Posterior intervals: credibilidade vs confianca
- Pareto k diagnostic

### 5. pitfalls.md
- Priors nao informativos que sao informativos sem querer
- Nao verificar convergencia de MCMC
- ESS muito baixo
- Posterior multimodal com sampler inadequado
- Confundir intervalo de credibilidade com confianca
- Overfitting em modelos bayesianos complexos
- Nao fazer posterior predictive checks
- Ignorar Pareto k warnings no LOO-CV

---

## Formato: frontmatter com `slug: bayesian-<nome>`, `domain: bayesian`, `type: guide`

Cada guia: minimo 1500 palavras, formulas LaTeX (Bayes theorem, posterior, MCMC), tabelas comparativas, referencias da F1.

---

## Criterios de Aceite

- [x] 5 guias criados: overview.md, models.md, validation.md, metrics.md, pitfalls.md
- [x] Alem dos 5 guias, papers.md da F1 tambem presente no diretorio
- [x] Todos com frontmatter YAML valido
- [x] Cada guia com minimo de 1500 palavras
- [x] Formulas LaTeX incluidas onde necessario (Bayes theorem, posterior, GP kernel)
- [x] Referencias cruzadas aos papers da F1
- [x] Conteudo baseado em pesquisa web
- [x] Tom tecnico e adequado para profissionais de model validation

---

## Ferramentas Necessarias

- **Read**, **WebSearch**, **WebFetch**, **Write**

---

**End of Specification**

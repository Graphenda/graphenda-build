# Fase F5 — Templates e Exemplos de Relatorio de Validacao

**Status**: COMPLETO
**Dependencias**: F3 (guias), F4 (codigo)
**Bloqueia**: Nenhuma (fase final)

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/report-templates/bayesian/`

---

## Arquivos a Gerar

### 1. template.md

```markdown
---
slug: bayesian-validation-report-template
name: "Validation Report Template — Bayesian Models"
domain: bayesian
type: report-template
status: draft
tags: [bayesian, validation-report, template, mcmc, pymc, hierarchical]
---

# Model Validation Report — Bayesian Models

## 1. Executive Summary

## 2. Model Description
### 2.1 Model Type (Bayesian Regression / Hierarchical / GP / BSTS)
### 2.2 Purpose and Use Case
### 2.3 Model Structure (priors, likelihood, hierarchical levels)
### 2.4 Parameters and Hyperparameters

## 3. Data
### 3.1 Data Source and Period
### 3.2 Data Quality Assessment
### 3.3 Feature Engineering
### 3.4 Group Structure (if hierarchical)

## 4. Prior Specification
### 4.1 Prior Choices and Justification
### 4.2 Prior Predictive Check Results
### 4.3 Sensitivity of Priors (weakly vs strongly informative)

## 5. Inference
### 5.1 Sampler Configuration (NUTS, chains, warmup, draws)
### 5.2 Computational Cost

## 6. MCMC Diagnostics
### 6.1 Convergence (R-hat for all parameters)
### 6.2 Effective Sample Size (ESS bulk and tail)
### 6.3 Trace Plots
### 6.4 Divergences and Tree Depth
### 6.5 BFMI (Bayesian Fraction of Missing Information)
### 6.6 Autocorrelation

## 7. Model Validation
### 7.1 Posterior Predictive Checks
### 7.2 LOO-CV (elpd_loo, Pareto k diagnostics)
### 7.3 WAIC
### 7.4 Calibration of Credible Intervals
### 7.5 Comparison with Alternative Models (elpd_diff)

## 8. Results
### 8.1 Posterior Summary (mean, median, HDI)
### 8.2 Key Parameters Interpretation
### 8.3 Predictions with Uncertainty

## 9. Sensitivity Analysis
### 9.1 Sensitivity to Prior Specification
### 9.2 Sensitivity to Sampler Configuration
### 9.3 Sensitivity to Data Subset
### 9.4 Sensitivity to Model Structure

## 10. Limitations and Risks
### 10.1 Known Limitations
### 10.2 Computational Constraints
### 10.3 Model Risk Assessment
### 10.4 Monitoring Recommendations

## 11. Conclusion and Recommendations
### 11.1 Overall Assessment
### 11.2 Conditions for Approval
### 11.3 Recommended Re-estimation Frequency

## Appendices
### A. Full Posterior Summary Table
### B. Trace Plots for All Parameters
### C. Prior vs Posterior Comparison
### D. LOO-CV Detailed Results (Pareto k)
### E. Code and Reproducibility
### F. Data Dictionary
```

### 2. example.md — Exemplo Completo

Preencher com:
- **Cenario**: Modelo hierarquico de niveis de radon por condado
- **Modelo**: Hierarchical varying-intercept com PyMC (partial pooling)
- **Dados**: Radon dataset (919 obs, 85 condados)
- **Incluir**: prior predictive check, MCMC diagnostics (R-hat, ESS, traces), posterior predictive check, LOO-CV, shrinkage plot, prior sensitivity
- **Tom**: relatorio real para comite de validacao

---

## Criterios de Aceite

- [x] template.md criado com todas as 11 secoes principais + appendices
- [x] template.md tem instrucoes/placeholders claros em cada secao
- [x] template.md cobre prior specification, MCMC diagnostics e model validation (especificos bayesianos)
- [x] template.md inclui secoes para LOO-CV, PPC e prior sensitivity
- [x] example.md preenchido com cenario Radon (modelo hierarquico)
- [x] example.md tem MCMC diagnostics (R-hat, ESS, trace plots)
- [x] example.md tem prior predictive check e posterior predictive check
- [x] example.md tem LOO-CV com Pareto k diagnostics
- [x] example.md tem prior sensitivity analysis
- [x] example.md tem conclusao e recomendacoes realistas
- [x] Ambos os arquivos tem frontmatter YAML valido
- [x] Conteudo baseado em pesquisa web

---

## Ferramentas Necessarias

- **Read**, **WebSearch**, **WebFetch**, **Write**

---

**End of Specification**

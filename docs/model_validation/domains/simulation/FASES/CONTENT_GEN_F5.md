# Fase F5 — Templates e Exemplos de Relatorio de Validacao

**Status**: CONCLUIDO
**Dependencias**: F3, F4
**Bloqueia**: Nenhuma

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/report-templates/simulation/`

---

### 1. template.md

```markdown
---
slug: simulation-validation-report-template
name: "Validation Report Template — Simulation Models"
domain: simulation
type: report-template
status: draft
tags: [simulation, validation-report, template, monte-carlo, var, cvar, stress-testing, backtesting, sobol]
---

# Model Validation Report — Simulation Models

## 1. Executive Summary

## 2. Simulation Type and Objective
### 2.1 Model Type (Monte Carlo / ABM / DES / System Dynamics)
### 2.2 Purpose and Use Case
### 2.3 Scope and Limitations

## 3. Input Distributions
### 3.1 Variables and Sources
### 3.2 Distribution Fitting (parametric / empirical)
### 3.3 Correlation Structure (copulas, Cholesky)
### 3.4 Data Quality Assessment

## 4. Calibration
### 4.1 Parameter Estimation Method
### 4.2 Historical Reproduction
### 4.3 Goodness-of-Fit Tests (KS, AD, chi-squared)
### 4.4 Calibration Error Metrics

## 5. Convergence
### 5.1 Number of Simulations and Justification
### 5.2 Monte Carlo Standard Error
### 5.3 Convergence Plots (cumulative mean, CI bands)
### 5.4 Variance Reduction Techniques Applied

## 6. Results — VaR and CVaR
### 6.1 VaR at Confidence Levels (95%, 99%, 99.5%)
### 6.2 CVaR / Expected Shortfall
### 6.3 Confidence Intervals for Risk Measures
### 6.4 Distribution of Simulated P&L
### 6.5 Comparison with Analytical/Historical Methods

## 7. Backtesting
### 7.1 Kupiec Test (Proportion of Failures)
### 7.2 Christoffersen Test (Conditional Coverage)
### 7.3 Traffic Light System (Basel)
### 7.4 Rolling VaR vs Realized Losses Plot
### 7.5 Backtest Period and Sample Size

## 8. Sensitivity Analysis
### 8.1 Sobol Indices (First-Order and Total-Order)
### 8.2 Most Critical Inputs
### 8.3 Tornado Diagram
### 8.4 Scenario Sensitivity

## 9. Compliance — Basel / CCAR
### 9.1 Regulatory Scenarios Applied
### 9.2 Stress Test Results
### 9.3 Capital Impact Assessment
### 9.4 Documentation of Assumptions and Limitations

## 10. Operational
### 10.1 Computation Time and Resources
### 10.2 Reproducibility (random seed, versioning)
### 10.3 Model Update Frequency

## 11. Conclusion and Recommendations
### 11.1 Overall Assessment
### 11.2 Conditions for Deployment
### 11.3 Recommended Review Frequency
### 11.4 Identified Risks and Mitigations

## Appendices
### A. Full Metric Tables
### B. Convergence and Distribution Plots
### C. Backtesting Detailed Results
### D. Sensitivity Analysis Detailed Results
### E. Stress Test Scenario Definitions
### F. Code and Reproducibility
### G. Data Dictionary
```

### 2. example.md — Exemplo Completo

Preencher com:
- **Cenario**: Monte Carlo para VaR de portfolio de acoes
- **Portfolio**: 5 acoes (AAPL, MSFT, JPM, GS, XOM) com pesos iguais
- **Dados**: Fama-French / yfinance como fonte de retornos
- **Simulacao**: 100,000 cenarios com distribuicao normal e t-Student
- **Incluir**: calibracao de distribuicoes, convergencia MC, VaR 95%/99%, CVaR, backtesting com Kupiec e Christoffersen, analise de sensibilidade Sobol, stress testing com cenarios historicos (2008, COVID)
- **Tom**: relatorio real para comite de validacao

---

## Criterios de Aceite

- [x] template.md criado com 11 secoes + appendices
- [x] template.md cobre simulation type, input distributions, calibration, convergence
- [x] template.md inclui VaR/CVaR results, backtesting Kupiec/Christoffersen
- [x] template.md inclui sensitivity analysis com Sobol indices
- [x] template.md inclui compliance Basel/CCAR
- [x] example.md preenchido com MC VaR para portfolio de acoes
- [x] example.md tem calibracao de distribuicoes e convergencia MC
- [x] example.md tem backtesting com Kupiec e Christoffersen
- [x] example.md tem analise de sensibilidade Sobol
- [x] example.md tem stress testing com cenarios historicos
- [x] example.md tem conclusao e recomendacoes realistas
- [x] Ambos tem frontmatter YAML valido
- [x] Conteudo baseado em pesquisa web

---

**End of Specification**

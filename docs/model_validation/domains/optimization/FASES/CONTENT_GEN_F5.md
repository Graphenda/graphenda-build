# Fase F5 — Templates e Exemplos de Relatorio de Validacao

**Status**: COMPLETO
**Dependencias**: F3, F4
**Bloqueia**: Nenhuma

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/report-templates/optimization/`

---

### 1. template.md

```markdown
---
slug: optimization-validation-report-template
name: "Validation Report Template — Optimization Models"
domain: optimization
type: report-template
status: draft
tags: [optimization, validation-report, template, linear-programming, mip, sensitivity-analysis, shadow-prices, feasibility]
---

# Model Validation Report — Optimization Models

## 1. Executive Summary

## 2. Model Description
### 2.1 Model Type (LP / MIP / QP / NLP / Metaheuristic)
### 2.2 Purpose and Use Case
### 2.3 Decision Variables
### 2.4 Key Hyperparameters and Solver Settings

## 3. Mathematical Formulation
### 3.1 Objective Function
### 3.2 Constraints
### 3.3 Variable Bounds and Types
### 3.4 Formulation Completeness Review

## 4. Solution
### 4.1 Optimal Objective Value
### 4.2 Optimality Gap (for MIP)
### 4.3 Solution Time
### 4.4 Decision Variable Values
### 4.5 Comparison with Baselines (heuristic, equal-weight, manual)

## 5. Feasibility
### 5.1 Constraint Satisfaction Verification
### 5.2 Binding vs Slack Constraints
### 5.3 Variable Bounds Compliance
### 5.4 Infeasibility Diagnosis (if applicable)

## 6. Sensitivity Analysis and Shadow Prices
### 6.1 Shadow Prices of Key Constraints
### 6.2 Reduced Costs of Decision Variables
### 6.3 Objective Coefficient Ranges
### 6.4 RHS Ranges of Validity
### 6.5 Tornado Diagram of Parameter Sensitivity

## 7. Stress Testing
### 7.1 Extreme Scenarios Definition
### 7.2 Solution Robustness Under Perturbation
### 7.3 Infeasibility Under Stress
### 7.4 Objective Value Degradation

## 8. Operational Validation
### 8.1 Solution Implementability
### 8.2 Computational Time vs Execution Frequency
### 8.3 Scalability Assessment
### 8.4 Integration with Downstream Systems

## 9. Limitations and Risks
### 9.1 Known Limitations
### 9.2 Model Risk Assessment
### 9.3 Parameter Uncertainty Impact
### 9.4 Monitoring Recommendations

## 10. Conclusion and Recommendations
### 10.1 Overall Assessment
### 10.2 Conditions for Deployment
### 10.3 Recommended Review Frequency

## Appendices
### A. Full Solution Output
### B. Sensitivity Analysis Tables
### C. Stress Test Detailed Results
### D. Solver Log and Configuration
### E. Code and Reproducibility
### F. Data Dictionary
```

### 2. example.md — Exemplo Completo

Preencher com:
- **Cenario**: Otimizacao de mix de producao com restricoes de capacidade (LP)
- **Formulacao**: 4 produtos, 3 recursos, maximizar lucro
- **Solucao**: Valores otimos, shadow prices das restricoes
- **Sensitivity**: Analise completa com ranges de validade, tornado diagram
- **Stress Testing**: Variacao de demanda e capacidade em cenarios extremos
- **Operacional**: Tempo de solucao vs frequencia de replanejamento
- **Tom**: relatorio real para comite de validacao

---

## Criterios de Aceite

- [x] template.md criado com 10 secoes + appendices
- [x] template.md cobre formulation, solution, feasibility, sensitivity/shadow prices
- [x] template.md inclui stress testing e operational validation
- [x] template.md inclui sensitivity analysis com shadow prices e reduced costs
- [x] template.md inclui feasibility check com binding/slack
- [x] example.md preenchido com production mix LP
- [x] example.md tem formulacao matematica completa
- [x] example.md tem analise de sensibilidade com shadow prices
- [x] example.md tem stress testing com cenarios extremos
- [x] example.md tem conclusao e recomendacoes realistas
- [x] Ambos tem frontmatter YAML valido
- [x] Conteudo baseado em pesquisa web

---

**End of Specification**

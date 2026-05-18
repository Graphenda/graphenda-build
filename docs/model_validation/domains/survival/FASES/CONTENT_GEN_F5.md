# Fase F5 — Templates e Exemplos de Relatorio de Validacao

**Status**: CONCLUIDO
**Dependencias**: F3 (guias), F4 (codigo)
**Bloqueia**: Nenhuma (fase final)

---

## Objetivo

Criar um template reutilizavel de relatorio de validacao para modelos de sobrevivencia
e um exemplo completo preenchido com dados reais.

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/report-templates/survival/`

---

## Arquivos a Gerar

### 1. template.md — Template de Relatorio de Validacao

```markdown
---
slug: survival-validation-report-template
name: "Validation Report Template — Survival Models"
domain: survival
type: report-template
status: draft
tags: [survival, validation-report, template, sr-11-7, cox-ph, kaplan-meier]
---

# Model Validation Report — Survival Models

## 1. Executive Summary

## 2. Model Description
### 2.1 Model Type (KM / Cox PH / AFT / Competing Risks)
### 2.2 Event of Interest and Censoring Definition
### 2.3 Input Variables (Covariates)
### 2.4 Time Variable and Follow-up Period

## 3. Data
### 3.1 Data Source and Period
### 3.2 Censoring Assessment (% censored, censoring distribution)
### 3.3 Event Distribution (time-to-event histogram)
### 3.4 Data Quality and Missing Values
### 3.5 Train/Test Split (temporal or random)

## 4. Exploratory Analysis
### 4.1 Kaplan-Meier Curves by Key Groups
### 4.2 Event Rate Over Time
### 4.3 Distribution of Follow-up Times

## 5. Methodology
### 5.1 Model Selection Rationale
### 5.2 Variable Selection
### 5.3 Handling of Censoring
### 5.4 Treatment of Time-Varying Covariates (if applicable)

## 6. Diagnostics
### 6.1 Proportional Hazards Assumption
#### 6.1.1 Schoenfeld Residuals Test
#### 6.1.2 Log-Log Plot
#### 6.1.3 Remediation (if violated)
### 6.2 Residual Analysis
#### 6.2.1 Martingale Residuals
#### 6.2.2 Deviance Residuals
### 6.3 Influence Analysis (dfbeta)
### 6.4 Goodness of Fit

## 7. Performance
### 7.1 Discrimination
#### 7.1.1 C-statistic (Harrell's Concordance Index)
#### 7.1.2 Time-Dependent AUC
### 7.2 Calibration
#### 7.2.1 Predicted vs Observed Survival Curves
#### 7.2.2 Brier Score (Integrated)
### 7.3 Model Comparison (if multiple models)
### 7.4 Out-of-Sample Performance

## 8. Sensitivity Analysis
### 8.1 Sensitivity to Censoring Assumptions
### 8.2 Sensitivity to Variable Inclusion/Exclusion
### 8.3 Sensitivity to Follow-up Window
### 8.4 Competing Risks Assessment (if applicable)

## 9. Limitations and Risks
### 9.1 Known Limitations
### 9.2 Model Risk Assessment
### 9.3 Monitoring Recommendations

## 10. Conclusion and Recommendations
### 10.1 Overall Assessment
### 10.2 Conditions for Approval
### 10.3 Recommended Monitoring Frequency

## Appendices
### A. Detailed Statistical Tables (hazard ratios, CIs, p-values)
### B. Diagnostic Plots (KM, Schoenfeld, calibration)
### C. Kaplan-Meier Curves by Subgroup
### D. Code and Reproducibility
### E. Data Dictionary
```

### 2. example.md — Exemplo Completo com Dados Reais

Preencher o template com:
- **Cenario**: Modelo Cox PH para sobrevivencia de pacientes com cancer de pulmao
- **Modelo**: Cox PH com teste de PH e hazard ratios
- **Dados**: Lung Cancer dataset (lifelines, 228 obs)
- **Incluir**: hazard ratios, C-statistic, Schoenfeld test, calibracao, KM curves
- **Tom**: relatorio real para comite de validacao

---

## Etapas de Implementacao

### Etapa 1: Pesquisar templates de validation reports para modelos de sobrevivencia
### Etapa 2: Criar template.md com estrutura completa
### Etapa 3: Preencher example.md com lung cancer dataset
### Etapa 4: Verificacao

```bash
ls -la /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/report-templates/survival/
grep -c "^## " /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/report-templates/survival/template.md
wc -l /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/report-templates/survival/example.md
```

---

## Criterios de Aceite

- [x] template.md criado com todas as 10 secoes principais + appendices
- [x] template.md tem instrucoes/placeholders claros em cada secao
- [x] template.md referencia requisitos regulatorios (SR 11-7)
- [x] template.md cobre particularidades de sobrevivencia (censura, PH assumption, C-statistic)
- [x] example.md preenchido com cenario Lung Cancer (Cox PH)
- [x] example.md tem hazard ratios com CIs e p-values
- [x] example.md tem C-statistic e time-dependent AUC
- [x] example.md tem teste de Schoenfeld para PH assumption
- [x] example.md tem calibracao (predicted vs observed)
- [x] example.md tem conclusao e recomendacoes realistas
- [x] Ambos os arquivos tem frontmatter YAML valido
- [x] Conteudo regulatorio baseado em pesquisa web

---

## Ferramentas Necessarias

- **Read**, **WebSearch**, **WebFetch**, **Write**

---

**End of Specification**

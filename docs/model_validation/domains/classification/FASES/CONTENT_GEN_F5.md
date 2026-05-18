# Fase F5 — Templates e Exemplos de Relatorio de Validacao

**Status**: CONCLUIDO
**Dependencias**: F3 (guias), F4 (codigo)
**Bloqueia**: Nenhuma (fase final)

---

## Objetivo

Criar um template reutilizavel de relatorio de validacao para modelos de classificacao
e um exemplo completo preenchido com dados reais.

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/report-templates/classification/`

---

## Arquivos a Gerar

### 1. template.md — Template de Relatorio de Validacao

```markdown
---
slug: classification-validation-report-template
name: "Validation Report Template — Classification Models"
domain: classification
type: report-template
status: draft
tags: [classification, validation-report, template, sr-11-7, xgboost, fairness]
---

# Model Validation Report — Classification Models

## 1. Executive Summary

## 2. Model Description
### 2.1 Model Type (RF / XGBoost / LightGBM / SVM / Ensemble)
### 2.2 Model Purpose and Use Case
### 2.3 Input Variables (Features)
### 2.4 Target Variable and Positive Class Definition
### 2.5 Model Complexity and Interpretability Tier

## 3. Data
### 3.1 Data Source and Period
### 3.2 Data Quality Assessment
### 3.3 Class Distribution (imbalance ratio)
### 3.4 Feature Engineering and Transformations
### 3.5 Train/Test/Validation Split Strategy

## 4. Methodology
### 4.1 Model Selection Rationale
### 4.2 Feature Selection
### 4.3 Hyperparameter Tuning Strategy
### 4.4 Handling of Class Imbalance (SMOTE, class weights, etc.)
### 4.5 Cross-Validation Strategy

## 5. Performance — Discrimination
### 5.1 AUC-ROC (with bootstrap CI)
### 5.2 AUC-PR (Precision-Recall)
### 5.3 Gini Coefficient
### 5.4 KS Statistic
### 5.5 Metrics at Chosen Threshold
#### 5.5.1 Threshold Selection Rationale
#### 5.5.2 Confusion Matrix
#### 5.5.3 Precision, Recall, F1-Score
#### 5.5.4 Specificity and NPV

## 6. Performance — Calibration
### 6.1 Calibration Plot (Reliability Diagram)
### 6.2 Brier Score
### 6.3 Log-Loss
### 6.4 Calibration Method (if applied: Platt, Isotonic)

## 7. Interpretability
### 7.1 Feature Importance (impurity / permutation / SHAP)
### 7.2 SHAP Summary Plot
### 7.3 SHAP Dependence Plots (top features)
### 7.4 Partial Dependence Plots
### 7.5 LIME (individual predictions, if applicable)

## 8. Fairness Assessment
### 8.1 Protected Attributes Identified
### 8.2 Demographic Parity
### 8.3 Equalized Odds
### 8.4 Disparate Impact Ratio
### 8.5 Mitigation Actions (if needed)

## 9. Stability and Monitoring
### 9.1 Cross-Validation Variance
### 9.2 Population Stability Index (PSI)
### 9.3 Characteristic Stability Index (CSI)
### 9.4 Feature Drift Assessment
### 9.5 Concept Drift Detection Strategy

## 10. Sensitivity Analysis
### 10.1 Sensitivity to Feature Inclusion/Exclusion
### 10.2 Sensitivity to Threshold Selection
### 10.3 Sensitivity to Hyperparameters
### 10.4 Sensitivity to Training Data Period

## 11. Limitations and Risks
### 11.1 Known Limitations
### 11.2 Model Risk Assessment (materiality)
### 11.3 Monitoring Recommendations

## 12. Conclusion and Recommendations
### 12.1 Overall Assessment
### 12.2 Conditions for Approval
### 12.3 Recommended Monitoring Frequency

## Appendices
### A. Detailed Hyperparameters
### B. Full Feature Importance Table
### C. SHAP Plots for All Features
### D. Fairness Metrics by Subgroup
### E. Code and Reproducibility
### F. Data Dictionary
```

### 2. example.md — Exemplo Completo com Dados Reais

Preencher o template com:
- **Cenario**: Modelo XGBoost para deteccao de fraude
- **Modelo**: XGBoost com tuning, SHAP, calibracao
- **Dados**: Credit Card Fraud dataset (Kaggle, 284K obs, altamente desbalanceado)
- **Incluir**: AUC-ROC, AUC-PR, KS, SHAP summary, calibration plot, fairness (se aplicavel), PSI
- **Tom**: relatorio real para comite de validacao

---

## Etapas de Implementacao

### Etapa 1: Pesquisar templates de validation reports para modelos de ML/classificacao
### Etapa 2: Criar template.md com estrutura completa (12 secoes + appendices)
### Etapa 3: Preencher example.md com Credit Card Fraud + XGBoost
### Etapa 4: Verificacao

```bash
ls -la /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/report-templates/classification/
grep -c "^## " /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/report-templates/classification/template.md
wc -l /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/report-templates/classification/example.md
```

---

## Criterios de Aceite

- [x] template.md criado com todas as 12 secoes principais + appendices
- [x] template.md tem instrucoes/placeholders claros em cada secao
- [x] template.md referencia requisitos regulatorios (SR 11-7, EU AI Act)
- [x] template.md cobre discriminacao, calibracao, interpretabilidade, fairness e estabilidade
- [x] example.md preenchido com cenario Credit Card Fraud (XGBoost)
- [x] example.md tem metricas de discriminacao (AUC-ROC, AUC-PR, KS, Gini)
- [x] example.md tem metricas de calibracao (Brier Score, calibration plot)
- [x] example.md tem SHAP analysis (summary + top features)
- [x] example.md tem fairness assessment (ou justificativa de N/A)
- [x] example.md tem PSI e estabilidade
- [x] example.md tem conclusao e recomendacoes realistas
- [x] Ambos os arquivos tem frontmatter YAML valido
- [x] Conteudo regulatorio baseado em pesquisa web

---

## Ferramentas Necessarias

- **Read**, **WebSearch**, **WebFetch**, **Write**

---

**End of Specification**

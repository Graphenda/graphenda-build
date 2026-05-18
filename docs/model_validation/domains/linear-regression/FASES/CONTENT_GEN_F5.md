# Fase F5 — Templates e Exemplos de Relatorio de Validacao

**Status**: CONCLUIDO
**Dependencias**: F3 (guias), F4 (codigo)
**Bloqueia**: Nenhuma (fase final)

---

## Objetivo

Criar um template reutilizavel de relatorio de validacao para modelos de regressao
linear e um exemplo completo preenchido com dados sinteticos, seguindo as melhores
praticas de model risk management (SR 11-7, SS1/23, ECB Guide).

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/report-templates/linear-regression/`

---

## Arquivos a Gerar

### 1. template.md — Template de Relatorio de Validacao

Estrutura obrigatoria do template:

```markdown
---
slug: linear-regression-validation-report-template
name: "Validation Report Template — Linear Regression"
domain: linear-regression
type: report-template
status: draft
tags: [linear-regression, validation-report, template, sr-11-7]
---

# Model Validation Report — Linear Regression

## 1. Executive Summary
[Placeholder com instrucoes do que incluir]

## 2. Model Description
### 2.1 Model Type and Purpose
### 2.2 Input Variables (Features)
### 2.3 Target Variable
### 2.4 Model Specification

## 3. Data
### 3.1 Data Source and Period
### 3.2 Data Quality Assessment
### 3.3 Data Treatments and Transformations
### 3.4 Train/Test Split

## 4. Methodology
### 4.1 Estimation Method
### 4.2 Variable Selection
### 4.3 Hyperparameter Tuning (if applicable)

## 5. Assumption Diagnostics
### 5.1 Linearity (Residuals vs Fitted)
### 5.2 Normality of Residuals (Q-Q Plot, Shapiro-Wilk)
### 5.3 Homoscedasticity (Breusch-Pagan)
### 5.4 Independence (Durbin-Watson)
### 5.5 Multicollinearity (VIF)
### 5.6 Influential Observations (Cook's Distance)

## 6. Performance Metrics
### 6.1 In-Sample Metrics (R², Adj R², RMSE, MAE)
### 6.2 Out-of-Sample Metrics
### 6.3 Cross-Validation Results
### 6.4 Model Comparison (if applicable)

## 7. Sensitivity Analysis
### 7.1 Coefficient Stability
### 7.2 Feature Importance
### 7.3 Stress Testing

## 8. Limitations and Risks
### 8.1 Known Limitations
### 8.2 Model Risk Assessment
### 8.3 Monitoring Recommendations

## 9. Conclusion and Recommendations
### 9.1 Overall Assessment
### 9.2 Conditions for Approval
### 9.3 Recommended Monitoring Frequency

## Appendices
### A. Detailed Statistical Tables
### B. Diagnostic Plots
### C. Code and Reproducibility
### D. Data Dictionary
```

### 2. example.md — Exemplo Completo com Dados Sinteticos

Preencher o template acima com:
- **Cenario**: Modelo de precificacao de imoveis (California Housing)
- **Modelo**: OLS com selecao de variaveis via Lasso
- **Dados**: California Housing dataset (sklearn)
- **Incluir**: resultados numericos reais (calcular ou buscar), graficos descritos em texto, tabelas com metricas
- **Tom**: como se fosse um relatorio real entregue a um comite de validacao

---

## Etapas de Implementacao

### Etapa 1: Pesquisa de Frameworks

- Buscar na web templates de validation reports usados em bancos
- Buscar requisitos do SR 11-7 para documentacao de modelos
- Buscar exemplos de relatorios da industria

### Etapa 2: Criacao do Template

- Criar `template.md` com a estrutura completa
- Incluir instrucoes/placeholders em cada secao
- Adicionar notas sobre o que reguladores esperam ver

### Etapa 3: Preenchimento do Exemplo

- Criar `example.md` preenchendo o template
- Usar resultados do California Housing dataset
- Incluir metricas numericas realistas
- Descrever graficos de diagnostico (referenciando scripts da F4)
- Escrever conclusoes e recomendacoes como em relatorio real

### Etapa 4: Verificacao

```bash
# Verificar que ambos os arquivos existem
ls -la /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/report-templates/linear-regression/

# Verificar frontmatter
head -12 /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/report-templates/linear-regression/template.md
head -12 /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/report-templates/linear-regression/example.md

# Verificar secoes do template (deve ter 9 secoes principais)
grep -c "^## " /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/report-templates/linear-regression/template.md

# Verificar tamanho do exemplo (deve ser substancial)
wc -l /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/report-templates/linear-regression/example.md
```

---

## Criterios de Aceite

- [x] template.md criado com todas as 9 secoes principais + appendices
- [x] template.md tem instrucoes/placeholders claros em cada secao
- [x] template.md referencia requisitos regulatorios (SR 11-7)
- [x] example.md preenchido com cenario California Housing
- [x] example.md tem metricas numericas (R², RMSE, MAE, VIF, p-values)
- [x] example.md tem descricao de graficos de diagnostico
- [x] example.md tem conclusao e recomendacoes realistas
- [x] Ambos os arquivos tem frontmatter YAML valido
- [x] Conteudo regulatorio baseado em pesquisa web

---

## Ferramentas Necessarias

- **Read**: para ler guias (F3) e scripts (F4)
- **WebSearch**: para buscar templates e requisitos regulatorios
- **WebFetch**: para acessar documentos regulatorios
- **Write**: para criar template e exemplo

---

**End of Specification**

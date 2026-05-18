# Fase F5 — Templates e Exemplos de Relatorio de Validacao

**Status**: CONCLUIDO
**Dependencias**: F3 (guias), F4 (codigo)
**Bloqueia**: Nenhuma (fase final)

---

## Objetivo

Criar um template reutilizavel de relatorio de validacao para modelos de dados
em painel e um exemplo completo preenchido com dados reais, seguindo as melhores
praticas de model risk management (SR 11-7, SS1/23, ECB Guide).

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/report-templates/panel-data/`

---

## Arquivos a Gerar

### 1. template.md — Template de Relatorio de Validacao

Estrutura obrigatoria do template:

```markdown
---
slug: panel-data-validation-report-template
name: "Validation Report Template — Panel Data Models"
domain: panel-data
type: report-template
status: draft
tags: [panel-data, validation-report, template, sr-11-7]
---

# Model Validation Report — Panel Data

## 1. Executive Summary
[Placeholder com instrucoes do que incluir]

## 2. Model Description
### 2.1 Model Type (FE / RE / GMM) and Purpose
### 2.2 Panel Structure (N entities x T periods)
### 2.3 Input Variables (Features)
### 2.4 Target Variable
### 2.5 Model Specification

## 3. Data
### 3.1 Data Source and Period
### 3.2 Panel Balancedness Assessment
### 3.3 Data Quality (missing values, attrition)
### 3.4 Data Treatments and Transformations
### 3.5 Train/Test Split Strategy for Panels

## 4. Methodology
### 4.1 Estimation Method (FE / RE / GMM)
### 4.2 Variable Selection
### 4.3 Instrument Selection (if GMM)
### 4.4 Standard Error Specification (clustered, HAC)

## 5. Specification Tests
### 5.1 Hausman Test (FE vs RE)
### 5.2 F-test for Fixed Effects (FE vs Pooled OLS)
### 5.3 Breusch-Pagan LM Test (RE vs Pooled OLS)
### 5.4 Sargan/Hansen Test (if GMM — instrument validity)
### 5.5 AR(1)/AR(2) Tests (if GMM — serial correlation)

## 6. Diagnostics
### 6.1 Serial Correlation (Wooldridge Test)
### 6.2 Heteroscedasticity
### 6.3 Cross-Sectional Dependence (Pesaran CD)
### 6.4 Panel Unit Root Tests (if applicable)
### 6.5 Influential Entities

## 7. Performance Metrics
### 7.1 R² Within, Between, and Overall
### 7.2 In-Sample Metrics (RMSE, MAE)
### 7.3 Out-of-Sample Metrics
### 7.4 Model Comparison Table (FE vs RE vs Pooled)

## 8. Sensitivity Analysis
### 8.1 Coefficient Stability Across Specifications
### 8.2 Robustness to Alternative Standard Errors
### 8.3 Subsample Analysis (by entity group or time period)
### 8.4 Instrument Sensitivity (if GMM)

## 9. Limitations and Risks
### 9.1 Known Limitations
### 9.2 Model Risk Assessment
### 9.3 Monitoring Recommendations

## 10. Conclusion and Recommendations
### 10.1 Overall Assessment
### 10.2 Conditions for Approval
### 10.3 Recommended Monitoring Frequency

## Appendices
### A. Detailed Statistical Tables
### B. Diagnostic Plots
### C. Entity-Level Fixed Effects
### D. Code and Reproducibility
### E. Data Dictionary
```

### 2. example.md — Exemplo Completo com Dados Reais

Preencher o template acima com:
- **Cenario**: Modelo de determinantes do investimento corporativo (Grunfeld dataset)
- **Modelo**: Fixed Effects com teste de Hausman justificando a escolha
- **Dados**: Grunfeld Investment (10 firmas x 20 anos, statsmodels)
- **Incluir**: resultados numericos reais, testes de especificacao completos, tabelas com metricas
- **Tom**: como se fosse um relatorio real entregue a um comite de validacao

---

## Etapas de Implementacao

### Etapa 1: Pesquisa de Frameworks

- Buscar na web templates de validation reports para modelos de painel
- Buscar requisitos do SR 11-7 para documentacao de modelos econometricos
- Buscar exemplos de relatorios da industria bancaria

### Etapa 2: Criacao do Template

- Criar `template.md` com a estrutura completa
- Incluir instrucoes/placeholders em cada secao
- Adicionar notas sobre o que reguladores esperam ver em paineis
- Destacar particularidades de painel (Hausman, instrument tests, R² within/between)

### Etapa 3: Preenchimento do Exemplo

- Criar `example.md` preenchendo o template
- Usar resultados do Grunfeld dataset
- Incluir metricas numericas realistas (rodar codigo da F4 ou buscar resultados)
- Incluir resultados dos testes de especificacao (Hausman, F-test, BP LM)
- Descrever graficos de diagnostico (referenciando scripts da F4)
- Escrever conclusoes e recomendacoes como em relatorio real

### Etapa 4: Verificacao

```bash
# Verificar que ambos os arquivos existem
ls -la /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/report-templates/panel-data/

# Verificar frontmatter
head -12 /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/report-templates/panel-data/template.md
head -12 /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/report-templates/panel-data/example.md

# Verificar secoes do template (deve ter 10 secoes principais)
grep -c "^## " /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/report-templates/panel-data/template.md

# Verificar tamanho do exemplo (deve ser substancial)
wc -l /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/report-templates/panel-data/example.md
```

---

## Criterios de Aceite

- [x] template.md criado com todas as 10 secoes principais + appendices
- [x] template.md tem instrucoes/placeholders claros em cada secao
- [x] template.md referencia requisitos regulatorios (SR 11-7)
- [x] template.md cobre particularidades de painel (Hausman, instruments, R² within/between)
- [x] example.md preenchido com cenario Grunfeld Investment
- [x] example.md tem resultados de testes de especificacao (Hausman, F-test, BP LM)
- [x] example.md tem metricas numericas (R² within/between/overall, RMSE, p-values)
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

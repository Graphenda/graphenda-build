# Fase F5 — Templates e Exemplos de Relatorio de Validacao

**Status**: CONCLUIDO
**Dependencias**: F3 (guias), F4 (codigo)
**Bloqueia**: Nenhuma (fase final)

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/report-templates/nlp-classical/`

---

## Arquivos a Gerar

### 1. template.md

```markdown
---
slug: nlp-classical-validation-report-template
name: "Validation Report Template — NLP Classical"
domain: nlp-classical
type: report-template
status: draft
tags: [nlp, classical, validation-report, template, tfidf, lda, ner, sentiment]
---

# Model Validation Report — NLP Classical

## 1. Executive Summary

## 2. Model Description
### 2.1 Task (Classification / NER / Topic Modeling / Sentiment)
### 2.2 Text Representation (TF-IDF, BoW, n-grams)
### 2.3 Algorithm (NB, SVM, LDA, CRF)
### 2.4 Key Hyperparameters

## 3. Data
### 3.1 Data Source, Volume, and Language
### 3.2 Class Distribution (if classification)
### 3.3 Data Quality (noise, duplicates, labeling quality)
### 3.4 Train/Test Split

## 4. Text Preprocessing
### 4.1 Pipeline Description (tokenization, stopwords, stemming/lemmatization)
### 4.2 Impact Assessment of Each Step
### 4.3 Vocabulary Size and Coverage
### 4.4 OOV (Out-of-Vocabulary) Analysis

## 5. Text Representation
### 5.1 Method (TF-IDF, BoW) and Configuration
### 5.2 Feature Dimensionality
### 5.3 n-gram Range Selection

## 6. Performance
### 6.1 Overall Metrics (Accuracy, F1-macro, F1-weighted)
### 6.2 Per-Class Metrics (Precision, Recall, F1)
### 6.3 Confusion Matrix Analysis
### 6.4 Comparison with Baselines
### 6.5 Topic Coherence (if topic modeling)
### 6.6 Entity-Level F1 (if NER)

## 7. Error Analysis
### 7.1 Most Common Error Categories
### 7.2 Examples of Critical Errors
### 7.3 Ambiguous Cases
### 7.4 Feature Importance (top terms per class)

## 8. Robustness
### 8.1 Linguistic Variations (typos, slang, regional)
### 8.2 Domain Shift (texts from different sources)
### 8.3 Temporal Drift (language evolution)
### 8.4 Sensitivity to Preprocessing Choices

## 9. Limitations and Risks
### 9.1 Known Limitations (vocabulary, OOV)
### 9.2 Model Risk Assessment
### 9.3 Monitoring Recommendations

## 10. Conclusion and Recommendations
### 10.1 Overall Assessment
### 10.2 Conditions for Approval
### 10.3 Recommended Retraining Frequency

## Appendices
### A. Full Preprocessing Pipeline
### B. Vocabulary Statistics
### C. Per-Class Detailed Metrics
### D. Error Examples
### E. Code and Reproducibility
### F. Data Dictionary
```

### 2. example.md — Exemplo Completo

Preencher com:
- **Cenario**: Classificacao de reclamacoes de clientes por categoria
- **Modelo**: TF-IDF + SVM com grid search
- **Dados**: 20 Newsgroups (sklearn) como proxy
- **Incluir**: preprocessing impact analysis, per-class metrics, confusion matrix, error analysis, top features per class, robustness assessment
- **Tom**: relatorio real para comite de validacao

---

## Criterios de Aceite

- [x] template.md criado com todas as 10 secoes principais + appendices
- [x] template.md tem instrucoes/placeholders claros em cada secao
- [x] template.md cobre preprocessing, text representation, error analysis, robustness (especificos NLP)
- [x] template.md inclui secao para OOV analysis e linguistic variations
- [x] example.md preenchido com cenario classificacao de reclamacoes (TF-IDF + SVM)
- [x] example.md tem preprocessing impact assessment
- [x] example.md tem per-class metrics e confusion matrix
- [x] example.md tem error analysis com exemplos
- [x] example.md tem top features per class (TF-IDF terms)
- [x] example.md tem conclusao e recomendacoes realistas
- [x] Ambos os arquivos tem frontmatter YAML valido
- [x] Conteudo baseado em pesquisa web

---

## Ferramentas Necessarias

- **Read**, **WebSearch**, **WebFetch**, **Write**

---

**End of Specification**

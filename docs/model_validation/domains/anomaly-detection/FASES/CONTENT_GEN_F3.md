# Fase F3 — Guias Explicativos

**Status**: COMPLETO
**Dependencias**: F1
**Bloqueia**: F4, F5

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/anomaly-detection/`

---

## Guias a Gerar

### 1. overview.md
- O que e deteccao de anomalias: conceitos e taxonomia
- Anomalias pontuais, contextuais e coletivas
- Aplicacoes: fraude, AML, ciberseguranca, manufatura
- Extreme imbalance como desafio fundamental (0.1%–1% positivos)
- Abordagens: supervisionada vs semi-supervisionada vs nao-supervisionada
- Desafios regulatorios: explicabilidade, compliance AML/BSA
- Metricas de negocio vs metricas tecnicas

### 2. models.md
- Isolation Forest: isolamento por particionamento aleatorio
- Local Outlier Factor (LOF): anomalia baseada em densidade local
- One-Class SVM: fronteira de decisao no espaco de features
- Autoencoders para deteccao de anomalias: reconstruction error
- XGBoost cost-sensitive: escala de pesos para classe minoritaria
- Ensemble de detectores: combinacao de multiplos algoritmos
- SMOTE e variantes: oversampling sintetico para treino
- Deep learning: variational autoencoders, LSTM para series temporais
- Trade-offs: interpretabilidade vs performance em contexto regulatorio

### 3. validation.md
- Checklist de validacao para modelos de anomaly detection
- Temporal validation: treino no passado, teste no futuro (nunca split aleatorio)
- Walk-forward validation para dados de fraude
- Stratified splits preservando proporcao de anomalias
- Validacao out-of-time (OOT) e out-of-sample (OOS)
- Estabilidade temporal: PSI (Population Stability Index)
- Cross-validation adaptada para dados desbalanceados
- Testes de robustez: adversarial samples, concept drift
- Validacao de threshold: operating point selection

### 4. metrics.md
- AUC-PR (Precision-Recall): metrica principal para dados desbalanceados
- AUC-ROC: limitacoes com extreme imbalance
- Precision@k e Recall@k: metricas de ranking
- F1-Score, F2-Score: trade-off precision vs recall
- Cost-based metrics: custo esperado por decisao
- Alert rate e false positive rate operacional
- Lift e gain charts
- PSI: estabilidade da distribuicao de scores
- KS statistic: separacao entre classes
- Metricas de negocio: fraude capturada ($), custo de investigacao, ROI

### 5. pitfalls.md
- Split aleatorio em dados temporais (data leakage)
- Usar AUC-ROC como metrica principal com extreme imbalance
- Alert fatigue: muitos falsos positivos degradam operacao
- Ignorar custo assimetrico (falso negativo >>> falso positivo)
- Treinar com SMOTE e avaliar com dados sinteticos
- Nao fazer validacao temporal (walk-forward)
- Otimizar threshold sem considerar custo operacional
- Ignorar concept drift e sazonalidade em fraude
- Nao monitorar PSI em producao
- Compliance: modelos nao explicaveis para reguladores AML

---

## Formato: `slug: anomaly-detection-<nome>`, `domain: anomaly-detection`, `type: guide`

Cada guia: minimo 1500 palavras, formulas LaTeX (Isolation Forest anomaly score, AUC-PR, cost matrix, PSI), referencias da F1.

---

## Criterios de Aceite

- [x] 5 guias criados: overview.md, models.md, validation.md, metrics.md, pitfalls.md
- [x] papers.md da F1 tambem presente
- [x] Todos com frontmatter YAML valido
- [x] Cada guia com minimo de 1500 palavras
- [x] Formulas LaTeX incluidas (anomaly score, AUC-PR, cost matrix, PSI)
- [x] Referencias cruzadas aos papers da F1
- [x] Conteudo baseado em pesquisa web

---

**End of Specification**

# Fase F4 — Codigo de Exemplo

**Status**: COMPLETO
**Dependencias**: F3
**Bloqueia**: F5

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/anomaly-detection/`

---

## Arquivos a Gerar

### Modeling (5 arquivos)

#### 1. modeling/isolation_forest.py
- Isolation Forest com sklearn
- Tuning de n_estimators, contamination, max_samples
- Anomaly score distribution
- Feature importance via permutation
- Comparacao com baselines (random, threshold)
- Dataset: Credit Card Fraud (Kaggle)

#### 2. modeling/autoencoder_anomaly.py
- Autoencoder para deteccao de anomalias com PyTorch
- Reconstruction error como anomaly score
- Arquitetura: encoder-decoder com bottleneck
- Threshold selection via percentil
- Comparacao com Isolation Forest
- Dataset: Credit Card Fraud (Kaggle)

#### 3. modeling/cost_sensitive_xgboost.py
- XGBoost com scale_pos_weight para desbalanceamento
- Cost matrix: custo de FP vs FN
- Threshold optimization baseado em custo
- Comparacao: cost-sensitive vs standard
- Expected cost per decision
- Dataset: Credit Card Fraud (Kaggle)

#### 4. modeling/ensemble_detectors.py
- Ensemble de detectores: IF + LOF + One-Class SVM
- Voting: majority, average score, stacking
- Comparacao individual vs ensemble
- Calibracao de scores entre detectores
- pyod para pipeline unificado
- Dataset: Credit Card Fraud (Kaggle)

#### 5. modeling/smote_pipeline.py
- SMOTE, BorderlineSMOTE, ADASYN com imbalanced-learn
- Pipeline: SMOTE + classificador (XGBoost, Random Forest)
- Comparacao: com vs sem oversampling
- Avaliacao com dados originais (nunca com dados sinteticos)
- Cross-validation com imblearn Pipeline
- Dataset: Credit Card Fraud (Kaggle)

### Validation (3 arquivos)

#### 6. validation/temporal_validation.py
- Walk-forward temporal validation
- Split por timestamp: treino passado, teste futuro
- Comparacao: temporal split vs random split (mostra data leakage)
- PSI entre periodos (Population Stability Index)
- KS statistic por periodo
- Metricas por janela temporal
- Dataset: Credit Card Fraud (Kaggle)

#### 7. validation/cost_analysis.py
- Cost matrix completa: FP cost (investigacao), FN cost (fraude nao detectada)
- Expected cost por threshold
- Optimal threshold via cost minimization
- ROI do modelo vs baseline
- Sensitivity analysis: variando custos
- Break-even analysis
- Dataset: Credit Card Fraud (Kaggle)

#### 8. validation/alert_fatigue_analysis.py
- Alert rate por threshold
- Precision at different alert volumes
- Workload analysis: alerts por analista por dia
- Precision@k para operacao
- Trade-off: fraude capturada vs volume de alertas
- Simulacao de capacidade operacional
- Dataset: Credit Card Fraud (Kaggle)

### Visualization (1 arquivo)

#### 9. visualization/anomaly_plots.py
- Precision-Recall curve com AUC-PR
- ROC curve com AUC-ROC (e discussao de limitacao)
- Score distribution: anomalias vs normais
- Cost curve: custo esperado vs threshold
- PSI por periodo temporal (bar chart)
- Alert volume vs precision trade-off
- Confusion matrix heatmap por threshold
- Lift chart e cumulative gain
- Dataset: Credit Card Fraud (Kaggle)

---

## Formato: cada script com docstring, main(), RANDOM_STATE = 42

---

## Criterios de Aceite

- [x] 9 scripts Python criados nas subpastas corretas
- [x] modeling/isolation_forest.py — Isolation Forest com sklearn, tuning, feature importance
- [x] modeling/autoencoder_anomaly.py — Autoencoder PyTorch, reconstruction error
- [x] modeling/cost_sensitive_xgboost.py — XGBoost cost-sensitive, threshold optimization
- [x] modeling/ensemble_detectors.py — Ensemble IF+LOF+OCSVM com pyod
- [x] modeling/smote_pipeline.py — SMOTE/BorderlineSMOTE/ADASYN com imbalanced-learn
- [x] validation/temporal_validation.py — Walk-forward, PSI, KS, temporal vs random split
- [x] validation/cost_analysis.py — Cost matrix, optimal threshold, ROI, break-even
- [x] validation/alert_fatigue_analysis.py — Alert rate, precision@k, workload analysis
- [x] visualization/anomaly_plots.py — PR curve, ROC, score dist, cost curve, PSI, lift
- [x] Todos passam verificacao de sintaxe Python
- [x] Todos tem docstring, funcoes organizadas e main()
- [x] Stack: sklearn + pyod + imbalanced-learn + xgboost + torch + Credit Card Fraud dataset

---

## Bibliotecas Utilizadas

| Biblioteca | Versao Minima | Uso |
|------------|---------------|-----|
| scikit-learn | >= 1.3 | Isolation Forest, One-Class SVM, metricas, preprocessing |
| pyod | >= 1.1 | Ensemble de detectores, LOF, pipeline unificada |
| imbalanced-learn | >= 0.11 | SMOTE, BorderlineSMOTE, ADASYN, Pipeline |
| xgboost | >= 2.0 | Cost-sensitive classification |
| torch | >= 2.0 | Autoencoder customizado |
| matplotlib | >= 3.7 | Visualizacoes |
| seaborn | >= 0.12 | Visualizacoes |
| pandas | >= 2.0 | Manipulacao de dados |
| numpy | >= 1.24 | Computacao numerica |

---

**End of Specification**

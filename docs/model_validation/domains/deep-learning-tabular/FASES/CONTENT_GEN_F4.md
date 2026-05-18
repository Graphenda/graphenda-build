# Fase F4 — Codigo de Exemplo

**Status**: CONCLUIDO
**Dependencias**: F3
**Bloqueia**: F5

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/deep-learning-tabular/`

---

## Arquivos a Gerar

### Modeling (4 arquivos)

#### 1. modeling/mlp_tabular.py
- MLP com PyTorch para dados tabulares
- Entity embeddings para categoricas, normalizacao de numericas
- Batch normalization, dropout, early stopping
- Comparacao com XGBoost no mesmo dataset
- Dataset: Adult Income (UCI) ou California Housing (sklearn)

#### 2. modeling/tabnet_training.py
- Treino de TabNet com pytorch-tabnet
- Configuracao de sparse attention
- Visualizacao de feature importance via attention masks
- Grid search de hiperparametros principais
- Dataset: Adult Income (UCI)

#### 3. modeling/ft_transformer.py
- Implementacao de FT-Transformer (rtdl ou customizado)
- Tokenizacao de features numericas e categoricas
- Self-attention com positional encoding adaptado
- Avaliacao e comparacao com baselines
- Dataset: Adult Income (UCI)

#### 4. modeling/baseline_comparison.py
- Pipeline: MLP vs TabNet vs FT-Transformer vs XGBoost vs LightGBM
- Mesma validacao cruzada para todos
- Teste estatistico de significancia (Wilcoxon)
- Tabela resumo de resultados (metricas + tempo)
- Dataset: Adult Income (UCI)

### Validation (2 arquivos)

#### 5. validation/convergence_analysis.py
- Learning curves (train vs validation loss)
- Deteccao de overfitting
- Analise de sensibilidade ao learning rate
- Variancia entre multiplos runs com seeds diferentes
- Dataset: modelo da F4.1 ou F4.2

#### 6. validation/interpretability_comparison.py
- SHAP values para modelos de DL tabulares
- Comparacao de feature importance: attention vs SHAP vs permutation
- Consistency check entre metodos
- Dataset: modelos treinados nas F4.1-F4.3

### Visualization (1 arquivo)

#### 7. visualization/tabular_dl_plots.py
- Learning curves e convergencia
- Heatmap de attention weights (TabNet)
- Comparacao de performance entre modelos (bar chart com CI)
- Feature importance comparativa entre arquiteturas
- Calibration plot para probabilidades
- Dataset: modelos anteriores

---

## Formato: cada script com docstring, main(), RANDOM_STATE = 42

---

## Criterios de Aceite

- [x] 7 scripts Python criados nas subpastas corretas
- [x] modeling/mlp_tabular.py — MLP com entity embeddings e comparacao XGBoost
- [x] modeling/tabnet_training.py — TabNet com attention masks e feature importance
- [x] modeling/ft_transformer.py — FT-Transformer com tokenizacao
- [x] modeling/baseline_comparison.py — Pipeline comparativo com teste estatistico
- [x] validation/convergence_analysis.py — Learning curves, overfitting, seed variance
- [x] validation/interpretability_comparison.py — SHAP vs attention vs permutation
- [x] visualization/tabular_dl_plots.py — Learning curves, attention heatmap, comparison, calibration
- [x] Todos os scripts passam verificacao de sintaxe Python
- [x] Todos os scripts tem docstring, funcoes organizadas e main()
- [x] Codigo usa PyTorch + pytorch-tabnet como stack principal

---

## Bibliotecas Utilizadas

| Biblioteca | Versao Minima | Uso |
|------------|---------------|-----|
| torch | >= 2.0 | MLP, FT-Transformer |
| pytorch-tabnet | >= 4.0 | TabNet |
| xgboost | >= 2.0 | Baseline |
| lightgbm | >= 4.0 | Baseline |
| scikit-learn | >= 1.3 | Preprocessing, metricas, CV |
| shap | >= 0.43 | Interpretabilidade |
| optuna | >= 3.0 | Tuning |
| matplotlib | >= 3.7 | Visualizacoes |
| seaborn | >= 0.12 | Visualizacoes |

---

## Ferramentas Necessarias

- **Read**, **WebSearch**, **Write**

---

**End of Specification**

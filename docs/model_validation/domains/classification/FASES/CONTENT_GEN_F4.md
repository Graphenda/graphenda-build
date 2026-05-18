# Fase F4 — Codigo de Exemplo

**Status**: CONCLUIDO
**Dependencias**: F3 (para contexto dos guias)
**Bloqueia**: F5

---

## Objetivo

Criar exemplos de codigo Python completos e funcionais para modelos de classificacao.

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/classification/`

---

## Arquivos a Gerar

### Modeling (5 arquivos)

#### 1. modeling/random_forest_classifier.py
- Treinamento de Random Forest com sklearn
- Tuning de hiperparametros (n_estimators, max_depth, min_samples)
- Feature importance (impurity-based e permutation)
- OOB score como estimativa de erro
- Dataset: Breast Cancer Wisconsin (sklearn)

#### 2. modeling/xgboost_classifier.py
- Treinamento de XGBoost com xgboost e sklearn API
- Tuning com GridSearchCV ou Optuna
- Early stopping com validation set
- SHAP values para interpretabilidade
- Dataset: Breast Cancer Wisconsin (sklearn)

#### 3. modeling/lightgbm_catboost.py
- LightGBM com tuning de hiperparametros
- CatBoost com categorical features nativas
- Comparacao de performance entre os tres boosting frameworks
- Feature importance com SHAP
- Dataset: Adult Income (UCI) ou sintetico com categoricas

#### 4. modeling/svm_classifier.py
- SVM com kernel RBF e linear
- Scaling de features (StandardScaler, MinMaxScaler)
- Tuning de C e gamma com GridSearchCV
- Comparacao de kernels
- Dataset: Breast Cancer Wisconsin (sklearn)

#### 5. modeling/ensemble_comparison.py
- Pipeline completo comparando RF, XGBoost, LightGBM, SVM
- Cross-validation estratificada
- Ranking de modelos por multiplas metricas (AUC, F1, Log-loss)
- Analise de trade-offs (tempo de treino vs performance)
- Dataset: Breast Cancer Wisconsin (sklearn)

### Validation (2 arquivos)

#### 6. validation/classification_metrics.py
- Curva ROC e AUC com intervalo de confianca (bootstrap)
- Curva Precision-Recall
- Matriz de confusao com heatmap
- KS statistic e curva
- Selecao otima de threshold (Youden's J, F1-max)
- Calibration plot e Brier Score
- Dataset: modelo treinado na F4.2

#### 7. validation/fairness_analysis.py
- Metricas de fairness por grupo protegido
- Demographic parity e equalized odds
- Disparate impact ratio
- Mitigacao de bias com reweighting (fairlearn)
- Dataset: Adult Income (UCI) com atributo protegido (sex, race)

### Visualization (1 arquivo)

#### 8. visualization/classification_plots.py
- ROC e Precision-Recall curves (multiplos modelos)
- SHAP summary plot e dependence plots
- Confusion matrix heatmap
- Feature importance bar chart (RF vs XGBoost vs SHAP)
- Calibration plot (reliability diagram)
- KS plot com separacao de distribuicoes
- Learning curves (train vs validation)
- Dataset: modelos treinados nos scripts anteriores

---

## Formato de Cada Script

```python
"""
<Titulo do Script>
==================

<Descricao breve — 2-3 linhas>

Domain: Classification Models
Category: <modeling|validation|visualization>
Dependencies: <lista de pacotes>

Usage:
    python <nome_do_script>.py
"""

# --- Imports ---
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# --- Configuration ---
RANDOM_STATE = 42

# --- Functions ---
def main():
    """Main execution."""
    pass

if __name__ == "__main__":
    main()
```

---

## Etapas de Implementacao

### Etapa 1: Ler guias da F3 e spec do dominio
### Etapa 2: Pesquisar APIs (sklearn, xgboost, lightgbm, catboost, shap, fairlearn)
### Etapa 3: Desenvolver os 8 scripts
### Etapa 4: Verificacao

```bash
find /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/classification/ -name "*.py" | sort

for f in $(find /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/classification/ -name "*.py"); do
    echo "=== $(basename $f) ==="
    python3 -c "import ast; ast.parse(open('$f').read()); print('Syntax OK')"
done
```

---

## Criterios de Aceite

- [x] 8 scripts Python criados nas subpastas corretas
- [x] modeling/random_forest_classifier.py — RF com tuning e feature importance
- [x] modeling/xgboost_classifier.py — XGBoost com early stopping e SHAP
- [x] modeling/lightgbm_catboost.py — LightGBM + CatBoost com comparacao
- [x] modeling/svm_classifier.py — SVM com kernels e tuning
- [x] modeling/ensemble_comparison.py — Pipeline comparando todos os modelos
- [x] validation/classification_metrics.py — ROC, PR, KS, confusion, calibration
- [x] validation/fairness_analysis.py — Fairness metrics com fairlearn
- [x] visualization/classification_plots.py — Todos os plots de classificacao
- [x] Todos os scripts passam verificacao de sintaxe Python
- [x] Todos os scripts tem docstring, funcoes organizadas e main()
- [x] Codigo usa datasets acessiveis (sklearn ou sinteticos)

---

## Bibliotecas Utilizadas

| Biblioteca | Versao Minima | Uso |
|------------|---------------|-----|
| numpy | >= 1.24 | Arrays e operacoes numericas |
| pandas | >= 2.0 | DataFrames |
| scikit-learn | >= 1.3 | RF, SVM, KNN, metricas, CV, pipelines |
| xgboost | >= 2.0 | XGBoost classifier |
| lightgbm | >= 4.0 | LightGBM classifier |
| catboost | >= 1.2 | CatBoost classifier |
| shap | >= 0.43 | SHAP values e visualizacoes |
| fairlearn | >= 0.9 | Metricas de fairness |
| matplotlib | >= 3.7 | Visualizacoes |
| seaborn | >= 0.12 | Visualizacoes estatisticas |

---

## Ferramentas Necessarias

- **Read**, **WebSearch**, **Write**

---

**End of Specification**

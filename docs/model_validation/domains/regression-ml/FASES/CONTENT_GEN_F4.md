# Fase F4 — Codigo de Exemplo

**Status**: CONCLUIDO
**Dependencias**: F3 (para contexto dos guias)
**Bloqueia**: F5

---

## Objetivo

Criar exemplos de codigo Python completos e funcionais para modelos de regressao ML.

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/regression-ml/`

---

## Arquivos a Gerar

### Modeling (4 arquivos)

#### 1. modeling/tree_regressors.py
- Decision Tree, Random Forest e Gradient Boosting com sklearn
- Tuning de hiperparametros com cross-validation
- Feature importance (impurity-based e permutation)
- Partial dependence plots
- Dataset: California Housing (sklearn)

#### 2. modeling/xgboost_lightgbm_regression.py
- XGBoost e LightGBM para regressao
- Tuning com Optuna ou GridSearchCV
- Early stopping com validation set
- SHAP summary e dependence plots
- Dataset: California Housing (sklearn)

#### 3. modeling/svr_knn.py
- SVR com kernels RBF e linear
- KNN Regressor com distancia ponderada
- Pipeline com StandardScaler
- Comparacao com tree-based models
- Dataset: California Housing (sklearn)

#### 4. modeling/quantile_regression_ml.py
- Quantile regression com GradientBoostingRegressor (sklearn)
- Intervalos de previsao com quantis 0.05, 0.5, 0.95
- Comparacao com regressao pontual
- Visualizacao dos intervalos
- Dataset: California Housing (sklearn)

### Validation (2 arquivos)

#### 5. validation/residual_analysis_ml.py
- Residuos vs preditos para detectar padrao
- Residuos vs cada feature
- Distribuicao de residuos (histograma, Q-Q)
- Deteccao de heteroscedasticidade visual
- Learning curves (train size vs error)
- Dataset: modelo treinado na F4.2

#### 6. validation/model_comparison.py
- Pipeline de comparacao: DT, RF, XGBoost, LightGBM, SVR
- Cross-validation com multiplas metricas (RMSE, MAE, R²)
- Ranking de modelos com intervalos de confianca
- Teste de Diebold-Mariano para significancia
- Analise de tempo de treino vs performance
- Dataset: California Housing (sklearn)

### Visualization (1 arquivo)

#### 7. visualization/regression_ml_plots.py
- Predicted vs Actual scatter
- Residual plots por modelo
- Feature importance comparison (SHAP vs permutation)
- Partial dependence plots (1D e 2D)
- Learning curves
- Quantile regression bands
- Dataset: modelos treinados nos scripts anteriores

---

## Formato de Cada Script

```python
"""
<Titulo do Script>
==================

<Descricao breve — 2-3 linhas>

Domain: Regression ML Models
Category: <modeling|validation|visualization>
Dependencies: <lista de pacotes>

Usage:
    python <nome_do_script>.py
"""

# --- Imports ---
import numpy as np
import pandas as pd

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
### Etapa 2: Pesquisar APIs (sklearn, xgboost, lightgbm, shap, optuna)
### Etapa 3: Desenvolver os 7 scripts
### Etapa 4: Verificacao

```bash
find /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/regression-ml/ -name "*.py" | sort

for f in $(find /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/regression-ml/ -name "*.py"); do
    echo "=== $(basename $f) ==="
    python3 -c "import ast; ast.parse(open('$f').read()); print('Syntax OK')"
done
```

---

## Criterios de Aceite

- [x] 7 scripts Python criados nas subpastas corretas
- [x] modeling/tree_regressors.py — DT, RF, GBR com tuning e feature importance
- [x] modeling/xgboost_lightgbm_regression.py — XGBoost + LightGBM com SHAP
- [x] modeling/svr_knn.py — SVR + KNN com pipeline e scaling
- [x] modeling/quantile_regression_ml.py — Quantile regression com intervalos
- [x] validation/residual_analysis_ml.py — Residuos, Q-Q, learning curves
- [x] validation/model_comparison.py — Pipeline comparativo com Diebold-Mariano
- [x] visualization/regression_ml_plots.py — Predicted vs actual, PDP, SHAP, quantile bands
- [x] Todos os scripts passam verificacao de sintaxe Python
- [x] Todos os scripts tem docstring, funcoes organizadas e main()
- [x] Codigo usa datasets acessiveis (sklearn California Housing)

---

## Bibliotecas Utilizadas

| Biblioteca | Versao Minima | Uso |
|------------|---------------|-----|
| numpy | >= 1.24 | Arrays e operacoes numericas |
| pandas | >= 2.0 | DataFrames |
| scikit-learn | >= 1.3 | RF, GBR, SVR, KNN, metricas, CV, pipelines |
| xgboost | >= 2.0 | XGBoost regressor |
| lightgbm | >= 4.0 | LightGBM regressor |
| shap | >= 0.43 | SHAP values e visualizacoes |
| optuna | >= 3.0 | Otimizacao bayesiana |
| matplotlib | >= 3.7 | Visualizacoes |
| seaborn | >= 0.12 | Visualizacoes estatisticas |

---

## Ferramentas Necessarias

- **Read**, **WebSearch**, **Write**

---

**End of Specification**

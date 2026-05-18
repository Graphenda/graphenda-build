# Fase F4 — Codigo de Exemplo

**Status**: CONCLUIDO
**Dependencias**: F3 (para contexto dos guias)
**Bloqueia**: F5

---

## Objetivo

Criar exemplos de codigo Python completos e funcionais para metodos ensemble.

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/ensemble/`

---

## Arquivos a Gerar

### Modeling (4 arquivos)

#### 1. modeling/bagging_random_subspace.py
- BaggingClassifier e BaggingRegressor com sklearn
- Comparacao com Random Forest
- Efeito do numero de estimadores na performance
- Random subspace method (feature bagging)
- Dataset: Breast Cancer Wisconsin (sklearn)

#### 2. modeling/boosting_comparison.py
- AdaBoost vs GradientBoosting vs XGBoost vs LightGBM
- Tuning de learning rate e numero de estimadores
- Curva de performance vs complexidade
- Analise de overfitting com early stopping
- Dataset: Breast Cancer Wisconsin (sklearn)

#### 3. modeling/stacking_blending.py
- StackingClassifier e StackingRegressor com sklearn
- Definicao de base learners e meta-learner
- Blending manual com holdout
- Cross-validated stacking para evitar leakage
- Dataset: Breast Cancer Wisconsin (sklearn)

#### 4. modeling/voting_ensemble.py
- VotingClassifier (hard e soft) com sklearn
- Ponderacao otima de votos
- Combinacao de modelos heterogeneos (RF + LR + SVM)
- Comparacao com stacking
- Dataset: Breast Cancer Wisconsin (sklearn)

### Validation (2 arquivos)

#### 5. validation/ensemble_diversity.py
- Metricas de diversidade entre modelos base
- Q-statistic e correlation entre previsoes
- Contribuicao marginal de cada componente
- Ablation study: performance ao remover modelos
- Dataset: ensemble treinado na F4.3

#### 6. validation/oob_analysis.py
- OOB score para Random Forest e BaggingClassifier
- Comparacao OOB vs cross-validation
- OOB feature importance
- Convergencia do OOB error com numero de arvores
- Dataset: Breast Cancer Wisconsin (sklearn)

### Visualization (1 arquivo)

#### 7. visualization/ensemble_plots.py
- Performance vs numero de estimadores (bagging e boosting)
- Diversidade heatmap entre modelos base
- Comparacao de modelos: ensemble vs individuais
- Decision boundaries de ensembles vs modelos individuais (2D)
- Contribuicao de cada base learner no stacking
- Dataset: sintetico 2D para decision boundaries + Breast Cancer

---

## Formato de Cada Script

```python
"""
<Titulo do Script>
==================

<Descricao breve — 2-3 linhas>

Domain: Ensemble Models
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
### Etapa 2: Pesquisar APIs (sklearn ensemble, xgboost, lightgbm)
### Etapa 3: Desenvolver os 7 scripts
### Etapa 4: Verificacao

```bash
find /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/ensemble/ -name "*.py" | sort

for f in $(find /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/ensemble/ -name "*.py"); do
    echo "=== $(basename $f) ==="
    python3 -c "import ast; ast.parse(open('$f').read()); print('Syntax OK')"
done
```

---

## Criterios de Aceite

- [x] 7 scripts Python criados nas subpastas corretas
- [x] modeling/bagging_random_subspace.py — Bagging vs RF vs random subspace
- [x] modeling/boosting_comparison.py — AdaBoost vs GBR vs XGBoost vs LightGBM
- [x] modeling/stacking_blending.py — Stacking com sklearn + blending manual
- [x] modeling/voting_ensemble.py — VotingClassifier hard/soft com ponderacao
- [x] validation/ensemble_diversity.py — Q-statistic, correlation, ablation study
- [x] validation/oob_analysis.py — OOB score, comparacao com CV, convergencia
- [x] visualization/ensemble_plots.py — Performance curves, diversity heatmap, decision boundaries
- [x] Todos os scripts passam verificacao de sintaxe Python
- [x] Todos os scripts tem docstring, funcoes organizadas e main()
- [x] Codigo usa datasets acessiveis (sklearn Breast Cancer ou sinteticos)

---

## Bibliotecas Utilizadas

| Biblioteca | Versao Minima | Uso |
|------------|---------------|-----|
| numpy | >= 1.24 | Arrays e operacoes numericas |
| pandas | >= 2.0 | DataFrames |
| scikit-learn | >= 1.3 | Bagging, Voting, Stacking, RF, GBR, AdaBoost |
| xgboost | >= 2.0 | XGBoost |
| lightgbm | >= 4.0 | LightGBM |
| matplotlib | >= 3.7 | Visualizacoes |
| seaborn | >= 0.12 | Visualizacoes estatisticas |

---

## Ferramentas Necessarias

- **Read**, **WebSearch**, **Write**

---

**End of Specification**

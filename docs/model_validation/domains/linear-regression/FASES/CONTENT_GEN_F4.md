# Fase F4 — Codigo de Exemplo

**Status**: CONCLUIDO
**Dependencias**: F3 (para contexto dos guias)
**Bloqueia**: F5

---

## Objetivo

Criar exemplos de codigo Python completos e funcionais para regressao linear,
cobrindo modelagem, validacao e visualizacao. Cada script deve ser autocontido,
bem documentado e pronto para execucao.

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/linear-regression/`

---

## Arquivos a Gerar

### Modeling (3 arquivos)

#### 1. modeling/ols_complete.py
- Exemplo completo de OLS com statsmodels
- Leitura de dados (California Housing do sklearn)
- EDA basico
- Fit do modelo, interpretacao do summary
- Intervalos de confianca dos coeficientes
- Predicoes com intervalos

#### 2. modeling/regularization_comparison.py
- Comparacao Ridge vs Lasso vs ElasticNet
- Grid search de hiperparametros com cross-validation
- Curva de regularization path
- Selecao de features pelo Lasso
- Tabela comparativa de resultados

#### 3. modeling/robust_regression.py
- Deteccao de outliers (Cook's distance, leverage)
- OLS vs M-estimator vs LTS
- Comparacao de coeficientes e residuos
- Visualizacao do impacto dos outliers

### Validation (2 arquivos)

#### 4. validation/diagnostics_complete.py
- Residuos vs fitted plot
- Q-Q plot dos residuos
- Scale-location plot
- Leverage vs residuos (Cook's distance)
- Teste Breusch-Pagan (heteroscedasticidade)
- Teste Durbin-Watson (autocorrelacao)
- VIF (multicolinearidade)
- Teste Shapiro-Wilk (normalidade)

#### 5. validation/cross_validation.py
- K-fold cross-validation
- Comparacao de metricas entre folds (R², RMSE, MAE)
- Selecao de modelo via CV
- Learning curves
- Visualizacao dos resultados

### Visualization (1 arquivo)

#### 6. visualization/regression_plots.py
- Scatter com linha de regressao e IC
- Residual plots (4-panel diagnostic)
- Partial regression plots
- Cook's distance plot
- VIF heatmap
- Regularization path plot
- Prediction interval plot

---

## Formato de Cada Script

```python
"""
<Titulo do Script>
==================

<Descricao breve — 2-3 linhas>

Domain: Linear Regression
Category: <modeling|validation|visualization>
Dependencies: <lista de pacotes>

Usage:
    python <nome_do_script>.py
"""

# --- Imports ---
import numpy as np
import pandas as pd
# ... (imports relevantes)

# --- Configuration ---
RANDOM_STATE = 42
# ... (constantes)

# --- Functions ---
def main():
    """Main execution."""
    # [codigo organizado em funcoes]
    pass

if __name__ == "__main__":
    main()
```

---

## Etapas de Implementacao

### Etapa 1: Leitura de Contexto

- Ler os guias da F3 para alinhar conteudo dos scripts com os guias
- Ler a spec do dominio para garantir cobertura

### Etapa 2: Pesquisa de Melhores Praticas

- Buscar na web exemplos de referencia (statsmodels docs, sklearn docs)
- Verificar APIs atualizadas das bibliotecas

### Etapa 3: Desenvolvimento dos Scripts

Para cada script:
- Escrever codigo funcional e testavel
- Usar datasets do sklearn (California Housing, ou gerar sinteticos)
- Adicionar docstrings e comentarios explicativos
- Organizar com funcoes e main()
- Garantir que roda sem erros com dependencias padrao

### Etapa 4: Verificacao

```bash
# Verificar que todos os 6 scripts existem
find /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/linear-regression/ -name "*.py" | sort

# Verificar sintaxe Python
for f in $(find /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/linear-regression/ -name "*.py"); do
    echo "=== $(basename $f) ==="
    python3 -c "import ast; ast.parse(open('$f').read()); print('Syntax OK')"
done

# Verificar que cada script tem docstring e main
for f in $(find /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/linear-regression/ -name "*.py"); do
    echo "=== $(basename $f) ==="
    grep -c 'def main' "$f"
    grep -c '"""' "$f"
done
```

---

## Criterios de Aceite

- [x] 6 scripts Python criados nas subpastas corretas
- [x] modeling/ols_complete.py — OLS completo com statsmodels
- [x] modeling/regularization_comparison.py — Ridge vs Lasso vs ElasticNet
- [x] modeling/robust_regression.py — Regressao robusta vs OLS
- [x] validation/diagnostics_complete.py — Suite completa de diagnosticos
- [x] validation/cross_validation.py — K-fold CV com comparacao de modelos
- [x] visualization/regression_plots.py — Todos os plots de diagnostico
- [x] Todos os scripts passam verificacao de sintaxe Python
- [x] Todos os scripts tem docstring, funcoes organizadas e main()
- [x] Codigo usa datasets acessiveis (sklearn ou sinteticos)

---

## Bibliotecas Utilizadas

| Biblioteca | Versao Minima | Uso |
|------------|---------------|-----|
| numpy | >= 1.24 | Arrays e operacoes numericas |
| pandas | >= 2.0 | DataFrames e manipulacao de dados |
| statsmodels | >= 0.14 | OLS, WLS, diagnosticos, testes |
| scikit-learn | >= 1.3 | Ridge, Lasso, ElasticNet, CV, datasets |
| matplotlib | >= 3.7 | Visualizacoes |
| seaborn | >= 0.12 | Visualizacoes estatisticas |
| scipy | >= 1.11 | Testes estatisticos |

---

## Ferramentas Necessarias

- **Read**: para ler guias da F3
- **WebSearch**: para verificar APIs atualizadas
- **Write**: para criar cada script

---

**End of Specification**

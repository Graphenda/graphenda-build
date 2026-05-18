# Fase F4 — Codigo de Exemplo

**Status**: CONCLUIDO
**Dependencias**: F3 (para contexto dos guias)
**Bloqueia**: F5

---

## Objetivo

Criar exemplos de codigo Python completos e funcionais para modelos de sobrevivencia.

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/survival/`

---

## Arquivos a Gerar

### Modeling (4 arquivos)

#### 1. modeling/kaplan_meier.py
- Estimador KM com lifelines
- Curvas de sobrevivencia por grupo
- Teste de log-rank para comparacao
- Mediana de sobrevivencia e intervalos de confianca
- Dataset: Lung Cancer (lifelines)

#### 2. modeling/cox_ph.py
- Modelo Cox PH com lifelines
- Interpretacao de hazard ratios
- Cox com covariaveis time-varying
- Selecao de variaveis com penalizacao (Lasso-Cox)
- Dataset: Rossi Recidivism (lifelines)

#### 3. modeling/aft_parametric.py
- Modelos AFT: Weibull, Log-Normal, Log-Logistic
- Comparacao de distribuicoes parametricas
- Interpretacao de acceleration factors
- Selecao de melhor distribuicao via AIC
- Dataset: Lung Cancer (lifelines)

#### 4. modeling/competing_risks.py
- Modelo Fine-Gray para riscos competitivos
- Incidencia cumulativa por causa
- Comparacao com cause-specific Cox
- Dataset: sintetico com eventos competitivos

### Validation (2 arquivos)

#### 5. validation/ph_assumption_test.py
- Schoenfeld residuals e teste de PH
- Log-log plot para cada covariavel
- Estratificacao como solucao para violacao de PH
- Time-varying coefficients como alternativa
- Dataset: Rossi Recidivism (lifelines)

#### 6. validation/concordance_calibration.py
- Calculo do C-statistic com lifelines
- Time-dependent AUC com scikit-survival
- Calibracao: predicted vs observed survival curves
- Brier Score integrado
- Dataset: Lung Cancer (lifelines)

### Visualization (1 arquivo)

#### 7. visualization/survival_plots.py
- Curvas Kaplan-Meier com bandas de confianca
- Forest plot de hazard ratios
- Schoenfeld residuals plot
- Calibracao visual (predicted vs observed)
- Funcao de hazard estimada
- Dataset: Lung Cancer + Rossi

---

## Formato de Cada Script

```python
"""
<Titulo do Script>
==================

<Descricao breve — 2-3 linhas>

Domain: Survival Models
Category: <modeling|validation|visualization>
Dependencies: <lista de pacotes>

Usage:
    python <nome_do_script>.py
"""

# --- Imports ---
import numpy as np
import pandas as pd
from lifelines import ...

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
### Etapa 2: Pesquisar APIs (lifelines, scikit-survival)
### Etapa 3: Desenvolver os 7 scripts
### Etapa 4: Verificacao

```bash
find /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/survival/ -name "*.py" | sort

for f in $(find /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/survival/ -name "*.py"); do
    echo "=== $(basename $f) ==="
    python3 -c "import ast; ast.parse(open('$f').read()); print('Syntax OK')"
done
```

---

## Criterios de Aceite

- [x] 7 scripts Python criados nas subpastas corretas
- [x] modeling/kaplan_meier.py — KM com log-rank e mediana de sobrevivencia
- [x] modeling/cox_ph.py — Cox PH com hazard ratios e Lasso-Cox
- [x] modeling/aft_parametric.py — AFT Weibull, Log-Normal, Log-Logistic com AIC
- [x] modeling/competing_risks.py — Fine-Gray e cause-specific Cox
- [x] validation/ph_assumption_test.py — Schoenfeld, log-log plot, estratificacao
- [x] validation/concordance_calibration.py — C-statistic, td-AUC, Brier Score
- [x] visualization/survival_plots.py — KM curves, forest plot, Schoenfeld, calibracao
- [x] Todos os scripts passam verificacao de sintaxe Python
- [x] Todos os scripts tem docstring, funcoes organizadas e main()
- [x] Codigo usa datasets acessiveis (lifelines ou sinteticos)

---

## Bibliotecas Utilizadas

| Biblioteca | Versao Minima | Uso |
|------------|---------------|-----|
| numpy | >= 1.24 | Arrays e operacoes numericas |
| pandas | >= 2.0 | DataFrames |
| lifelines | >= 0.27 | KM, Cox PH, AFT, diagnosticos |
| scikit-survival | >= 0.22 | C-index, Brier Score, td-AUC |
| matplotlib | >= 3.7 | Visualizacoes |
| seaborn | >= 0.12 | Visualizacoes estatisticas |
| scipy | >= 1.11 | Distribuicoes parametricas |

---

## Ferramentas Necessarias

- **Read**, **WebSearch**, **Write**

---

**End of Specification**

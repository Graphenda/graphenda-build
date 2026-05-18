# Fase F4 — Codigo de Exemplo

**Status**: CONCLUIDO
**Dependencias**: F3 (para contexto dos guias)
**Bloqueia**: F5

---

## Objetivo

Criar exemplos de codigo Python completos e funcionais para modelos de series
temporais, cobrindo modelagem, validacao e visualizacao. Cada script deve ser
autocontido, bem documentado e pronto para execucao.

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/time-series/`

---

## Arquivos a Gerar

### Modeling (4 arquivos)

#### 1. modeling/arima_complete.py
- Identificacao de ordem via ACF/PACF e auto_arima (pmdarima)
- Estimacao ARIMA e SARIMA com statsmodels
- Forecasting com intervalos de confianca
- Comparacao com modelo naive como baseline
- Dataset: AirPassengers (statsmodels)

#### 2. modeling/garch_volatility.py
- Estimacao GARCH(1,1) com arch library
- Variantes EGARCH e GJR-GARCH
- Previsao de volatilidade condicional
- Aplicacao a retornos financeiros
- Dataset: S&P 500 returns (sintetico ou yfinance)

#### 3. modeling/var_system.py
- Estimacao VAR multivariado com statsmodels
- Selecao de lag order via criterios de informacao
- Funcoes impulso-resposta e decomposicao de variancia
- Teste de causalidade de Granger
- Dataset: macroeconomico sintetico ou statsmodels

#### 4. modeling/cointegration_vecm.py
- Teste de Johansen para cointegracao
- Estimacao de VECM
- Relacao de longo prazo e ajuste de curto prazo
- Dataset: pares de series cointegradas (sintetico)

### Validation (2 arquivos)

#### 5. validation/stationarity_tests.py
- Teste ADF (Augmented Dickey-Fuller)
- Teste KPSS
- Teste Phillips-Perron
- Diferenciacoes e transformacoes para estacionariedade
- Visualizacao de rolling mean e rolling std
- Dataset: AirPassengers e retornos financeiros

#### 6. validation/residual_diagnostics_ts.py
- Ljung-Box test para autocorrelacao residual
- Teste ARCH nos residuos
- Q-Q plot dos residuos
- ACF dos residuos padronizados
- Dataset: residuos de modelo ARIMA ajustado

### Visualization (1 arquivo)

#### 7. visualization/ts_plots.py
- Decomposicao de series temporais (trend, seasonal, residual)
- ACF e PACF plots
- Forecast vs realizado com bandas de confianca
- Impulso-resposta de modelos VAR
- Volatilidade condicional estimada (GARCH)
- Dataset: AirPassengers + retornos financeiros

---

## Formato de Cada Script

```python
"""
<Titulo do Script>
==================

<Descricao breve — 2-3 linhas>

Domain: Time Series Models
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

# --- Data Loading ---
def load_data():
    """Load dataset."""
    # ...

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

### Etapa 2: Pesquisa de APIs

- Buscar na web documentacao atualizada do statsmodels (SARIMAX, VAR, VECM)
- Verificar API da library arch (GARCH)
- Verificar API do pmdarima (auto_arima)
- Verificar disponibilidade dos datasets

### Etapa 3: Desenvolvimento dos Scripts

Para cada script:
- Escrever codigo funcional e testavel
- Usar datasets acessiveis (statsmodels, sinteticos)
- Adicionar docstrings e comentarios explicativos
- Organizar com funcoes e main()
- Garantir que roda sem erros com dependencias padrao

### Etapa 4: Verificacao

```bash
# Verificar que todos os 7 scripts existem
find /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/time-series/ -name "*.py" | sort

# Verificar sintaxe Python
for f in $(find /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/time-series/ -name "*.py"); do
    echo "=== $(basename $f) ==="
    python3 -c "import ast; ast.parse(open('$f').read()); print('Syntax OK')"
done

# Verificar que cada script tem docstring e main
for f in $(find /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/time-series/ -name "*.py"); do
    echo "=== $(basename $f) ==="
    grep -c 'def main' "$f"
    grep -c '"""' "$f"
done
```

---

## Criterios de Aceite

- [x] 7 scripts Python criados nas subpastas corretas
- [x] modeling/arima_complete.py — ARIMA/SARIMA com auto_arima e forecasting
- [x] modeling/garch_volatility.py — GARCH(1,1), EGARCH, GJR-GARCH
- [x] modeling/var_system.py — VAR com impulso-resposta e Granger
- [x] modeling/cointegration_vecm.py — Johansen + VECM
- [x] validation/stationarity_tests.py — ADF, KPSS, Phillips-Perron
- [x] validation/residual_diagnostics_ts.py — Ljung-Box, ARCH test, Q-Q plot
- [x] visualization/ts_plots.py — Decomposicao, ACF/PACF, forecast, IRF, volatilidade
- [x] Todos os scripts passam verificacao de sintaxe Python
- [x] Todos os scripts tem docstring, funcoes organizadas e main()
- [x] Codigo usa datasets acessiveis (statsmodels ou sinteticos)

---

## Bibliotecas Utilizadas

| Biblioteca | Versao Minima | Uso |
|------------|---------------|-----|
| numpy | >= 1.24 | Arrays e operacoes numericas |
| pandas | >= 2.0 | DataFrames e series temporais |
| statsmodels | >= 0.14 | ARIMA, SARIMAX, VAR, VECM, testes, ACF/PACF |
| arch | >= 6.0 | GARCH, EGARCH, GJR-GARCH, testes ARCH |
| pmdarima | >= 2.0 | auto_arima, selecao automatica de ordem |
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

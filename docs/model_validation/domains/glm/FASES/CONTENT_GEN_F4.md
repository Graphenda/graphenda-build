# Fase F4 — Codigo de Exemplo

**Status**: PENDENTE
**Dependencias**: F3 (para contexto dos guias)
**Bloqueia**: F5

---

## Objetivo

Criar exemplos de codigo Python completos e funcionais para Generalized Linear Models,
cobrindo modelagem, validacao e visualizacao. Cada script deve ser autocontido,
bem documentado e pronto para execucao.

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/glm/`

---

## Arquivos a Gerar

### Modeling (4 arquivos)

#### 1. modeling/logistic_regression.py
- Regressao logistica binaria com statsmodels e sklearn
- Interpretacao de coeficientes como odds ratios
- Curva ROC e selecao de threshold
- Logistica multinomial para multiplas classes
- Dataset: German Credit Data (UCI) ou sintetico

#### 2. modeling/poisson_negbin.py
- Regressao Poisson com statsmodels
- Deteccao de sobredispersao (Pearson chi² / df)
- Negative Binomial como alternativa
- Zero-Inflated Poisson com statsmodels
- Dataset: Bike Sharing (UCI) ou sintetico de contagens

#### 3. modeling/gamma_tweedie.py
- Regressao Gamma para dados de custo/sinistro
- Regressao Tweedie para dados com zeros e valores positivos
- Comparacao de link functions (log, inverse, identity)
- Dataset: Insurance Claims ou sintetico

#### 4. modeling/gam_splines.py
- GAM com pyGAM: splines para relacoes nao-lineares
- Selecao automatica de smoothing parameters
- Partial dependence plots
- Comparacao GAM vs GLM
- Dataset: German Credit ou sintetico

### Validation (2 arquivos)

#### 5. validation/calibration_analysis.py
- Teste de Hosmer-Lemeshow implementado passo a passo
- Curva de calibracao (reliability diagram)
- Brier Score e decomposicao
- Comparacao de calibracao entre modelos
- Dataset: modelo logistico ajustado na F4.1

#### 6. validation/deviance_diagnostics.py
- Deviance residuals vs fitted
- Pearson residuals e analise de sobredispersao
- Influence diagnostics (Cook's distance, leverage)
- Analise de deviance (modelo nulo vs modelo completo)
- Dataset: modelo GLM ajustado na F4.1 ou F4.2

### Visualization (1 arquivo)

#### 7. visualization/glm_plots.py
- Curva ROC e Precision-Recall
- Calibration plot (reliability diagram)
- Partial effects plots para cada variavel
- Residuos de deviance e Pearson
- Distribuicao predita vs observada
- Dataset: modelos ajustados nos scripts anteriores

---

## Formato de Cada Script

```python
"""
<Titulo do Script>
==================

<Descricao breve — 2-3 linhas>

Domain: Generalized Linear Models
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

- Buscar na web documentacao atualizada do statsmodels (GLM, families)
- Verificar API do sklearn (LogisticRegression, metrics)
- Verificar API do pyGAM
- Verificar disponibilidade dos datasets

### Etapa 3: Desenvolvimento dos Scripts

Para cada script:
- Escrever codigo funcional e testavel
- Usar datasets acessiveis (sklearn, statsmodels, sinteticos)
- Adicionar docstrings e comentarios explicativos
- Organizar com funcoes e main()
- Garantir que roda sem erros com dependencias padrao

### Etapa 4: Verificacao

```bash
find /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/glm/ -name "*.py" | sort

for f in $(find /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/glm/ -name "*.py"); do
    echo "=== $(basename $f) ==="
    python3 -c "import ast; ast.parse(open('$f').read()); print('Syntax OK')"
done

for f in $(find /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/glm/ -name "*.py"); do
    echo "=== $(basename $f) ==="
    grep -c 'def main' "$f"
    grep -c '"""' "$f"
done
```

---

## Criterios de Aceite

- [x] 7 scripts Python criados nas subpastas corretas
- [x] modeling/logistic_regression.py — Logistica binaria e multinomial com odds ratios
- [x] modeling/poisson_negbin.py — Poisson, NB e Zero-Inflated com sobredispersao
- [x] modeling/gamma_tweedie.py — Gamma e Tweedie para custos/sinistros
- [x] modeling/gam_splines.py — GAM com pyGAM e partial dependence
- [x] validation/calibration_analysis.py — Hosmer-Lemeshow, calibration plot, Brier Score
- [x] validation/deviance_diagnostics.py — Deviance/Pearson residuals, influence, ANOVA
- [x] visualization/glm_plots.py — ROC, PR, calibration, partial effects, residuos
- [x] Todos os scripts passam verificacao de sintaxe Python
- [x] Todos os scripts tem docstring, funcoes organizadas e main()
- [x] Codigo usa datasets acessiveis (sklearn, statsmodels ou sinteticos)

---

## Bibliotecas Utilizadas

| Biblioteca | Versao Minima | Uso |
|------------|---------------|-----|
| numpy | >= 1.24 | Arrays e operacoes numericas |
| pandas | >= 2.0 | DataFrames e manipulacao de dados |
| statsmodels | >= 0.14 | GLM (todas as familias), testes, diagnosticos |
| scikit-learn | >= 1.3 | LogisticRegression, metricas, CV, datasets |
| pyGAM | >= 0.9 | Generalized Additive Models |
| matplotlib | >= 3.7 | Visualizacoes |
| seaborn | >= 0.12 | Visualizacoes estatisticas |
| scipy | >= 1.11 | Distribuicoes e testes estatisticos |

---

## Ferramentas Necessarias

- **Read**: para ler guias da F3
- **WebSearch**: para verificar APIs atualizadas
- **Write**: para criar cada script

---

**End of Specification**

# Fase F4 — Codigo de Exemplo

**Status**: CONCLUIDO
**Dependencias**: F3 (para contexto dos guias)
**Bloqueia**: F5

---

## Objetivo

Criar exemplos de codigo Python completos e funcionais para modelos de dados
em painel, cobrindo modelagem, validacao e visualizacao. Cada script deve ser
autocontido, bem documentado e pronto para execucao.

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/panel-data/`

---

## Arquivos a Gerar

### Modeling (4 arquivos)

#### 1. modeling/fixed_effects.py
- Estimacao de Fixed Effects com linearmodels
- Inclusao de efeitos fixos de entidade e tempo
- Interpretacao dos coeficientes e efeitos fixos estimados
- Comparacao com dummies manuais via statsmodels
- Dataset: Grunfeld Investment (statsmodels)

#### 2. modeling/random_effects.py
- Estimacao de Random Effects com linearmodels
- Comparacao GLS vs OLS
- Estimacao da variancia dos efeitos aleatorios
- Dataset: Grunfeld Investment (statsmodels)

#### 3. modeling/arellano_bond_gmm.py
- Estimacao de painel dinamico com GMM
- Escolha e validacao de instrumentos
- Teste de Sargan/Hansen e testes AR(1)/AR(2)
- Comparacao Difference GMM vs System GMM
- Dataset: Grunfeld ou sintetico com lag da dependente

#### 4. modeling/pooled_ols_comparison.py
- Pooled OLS como benchmark
- Comparacao com FE, RE e First-Difference
- Demonstracao do vies por ignorar heterogeneidade
- Tabela comparativa de coeficientes e metricas
- Dataset: Grunfeld Investment (statsmodels)

### Validation (2 arquivos)

#### 5. validation/hausman_test.py
- Implementacao do teste de Hausman passo a passo
- Teste automatizado via linearmodels
- Interpretacao do resultado e decisao FE vs RE
- Testes complementares (Breusch-Pagan LM, F-test)
- Dataset: Grunfeld Investment (statsmodels)

#### 6. validation/panel_diagnostics.py
- Teste de Wooldridge para autocorrelacao serial
- Teste de heteroscedasticidade em painel
- Teste de dependencia cross-sectional (Pesaran CD)
- Teste de raiz unitaria em painel (LLC, IPS)
- Dataset: Grunfeld Investment (statsmodels)

### Visualization (1 arquivo)

#### 7. visualization/panel_plots.py
- Grafico de efeitos fixos estimados por entidade
- Comparacao de coeficientes entre modelos (FE vs RE vs OLS)
- Residuos por entidade e ao longo do tempo
- Heterogeneidade visual entre unidades do painel
- Dataset: Grunfeld Investment (statsmodels)

---

## Formato de Cada Script

```python
"""
<Titulo do Script>
==================

<Descricao breve — 2-3 linhas>

Domain: Panel Data Models
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
def load_grunfeld():
    """Load Grunfeld Investment dataset."""
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

- Buscar na web documentacao atualizada do linearmodels
- Verificar API do statsmodels para dados de painel
- Verificar disponibilidade do dataset Grunfeld

### Etapa 3: Desenvolvimento dos Scripts

Para cada script:
- Escrever codigo funcional e testavel
- Usar dataset Grunfeld (statsmodels) como dataset principal
- Adicionar docstrings e comentarios explicativos
- Organizar com funcoes e main()
- Garantir que roda sem erros com dependencias padrao

### Etapa 4: Verificacao

```bash
# Verificar que todos os 7 scripts existem
find /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/panel-data/ -name "*.py" | sort

# Verificar sintaxe Python
for f in $(find /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/panel-data/ -name "*.py"); do
    echo "=== $(basename $f) ==="
    python3 -c "import ast; ast.parse(open('$f').read()); print('Syntax OK')"
done

# Verificar que cada script tem docstring e main
for f in $(find /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/panel-data/ -name "*.py"); do
    echo "=== $(basename $f) ==="
    grep -c 'def main' "$f"
    grep -c '"""' "$f"
done
```

---

## Criterios de Aceite

- [x] 7 scripts Python criados nas subpastas corretas
- [x] modeling/fixed_effects.py — FE com linearmodels e dummies manuais
- [x] modeling/random_effects.py — RE com GLS e comparacao com OLS
- [x] modeling/arellano_bond_gmm.py — GMM dinamico com testes de instrumentos
- [x] modeling/pooled_ols_comparison.py — Pooled OLS vs FE vs RE vs FD
- [x] validation/hausman_test.py — Hausman passo a passo e automatizado
- [x] validation/panel_diagnostics.py — Suite de testes diagnosticos para painel
- [x] visualization/panel_plots.py — Plots de efeitos fixos, coeficientes e residuos
- [x] Todos os scripts passam verificacao de sintaxe Python
- [x] Todos os scripts tem docstring, funcoes organizadas e main()
- [x] Codigo usa dataset Grunfeld (statsmodels) ou sintetico acessivel

---

## Bibliotecas Utilizadas

| Biblioteca | Versao Minima | Uso |
|------------|---------------|-----|
| numpy | >= 1.24 | Arrays e operacoes numericas |
| pandas | >= 2.0 | DataFrames e MultiIndex para paineis |
| linearmodels | >= 5.0 | FE, RE, Between, FD, IV, GMM para paineis |
| statsmodels | >= 0.14 | Pooled OLS, datasets, testes |
| pyfixest | >= 0.15 | Fixed effects rapido (opcional) |
| matplotlib | >= 3.7 | Visualizacoes |
| seaborn | >= 0.12 | Visualizacoes estatisticas |
| scipy | >= 1.11 | Testes estatisticos |

---

## Ferramentas Necessarias

- **Read**: para ler guias da F3
- **WebSearch**: para verificar APIs atualizadas (linearmodels, pyfixest)
- **Write**: para criar cada script

---

**End of Specification**

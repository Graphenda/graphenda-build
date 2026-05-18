# Fase F4 — Codigo de Exemplo

**Status**: COMPLETO
**Dependencias**: F3
**Bloqueia**: F5

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/simulation/`

---

## Arquivos a Gerar

### Modeling (5 arquivos)

#### 1. modeling/monte_carlo_var.py
- Monte Carlo para VaR e CVaR de portfolio
- Simulacao de retornos com distribuicao normal e t-Student
- Comparacao: VaR historico vs parametrico vs Monte Carlo
- Intervalos de confianca do VaR
- Dataset: Fama-French / yfinance

#### 2. modeling/monte_carlo_pricing.py
- Pricing de opcoes europeias com Monte Carlo
- Black-Scholes como benchmark analitico
- Variance reduction: antithetic variates e control variates
- Convergencia: preco vs numero de simulacoes
- Dataset: parametros sinteticos de opcoes

#### 3. modeling/agent_based_model.py
- ABM simples com Mesa (Python)
- Agentes com regras de decisao
- Emergencia de comportamento macro
- Visualizacao da dinamica do sistema
- Stack: mesa

#### 4. modeling/stress_testing.py
- Framework de stress testing para portfolio
- Cenarios historicos: crise de 2008, COVID-2020
- Cenarios hipoteticos: choque de juros, credito
- Reverse stress test: qual cenario gera perda de X%
- Dataset: Fama-French / yfinance

#### 5. modeling/latin_hypercube.py
- Latin Hypercube Sampling com scipy
- Comparacao com random sampling e grid
- Eficiencia de cobertura do espaco de parametros
- Aplicacao em analise de sensibilidade
- Stack: scipy.stats.qmc

### Validation (3 arquivos)

#### 6. validation/convergence_analysis.py
- Analise de convergencia de Monte Carlo
- Erro vs numero de simulacoes (log-log plot)
- Determinacao do N minimo para precisao desejada
- Comparacao de variance reduction techniques
- Stack: numpy/scipy

#### 7. validation/var_backtesting.py
- Kupiec test (Proportion of Failures)
- Christoffersen test (independencia + cobertura condicional)
- Traffic light system (Basel)
- Rolling VaR vs perdas realizadas
- Stack: arch + scipy

#### 8. validation/sensitivity_sobol.py
- Analise de sensibilidade global com Sobol indices
- First-order e total-order effects
- Identificacao dos inputs mais criticos
- Visualizacao com tornado e pie charts
- Stack: SALib

### Visualization (1 arquivo)

#### 9. visualization/simulation_plots.py
- Distribuicao de perdas com VaR e CVaR marcados
- Convergencia de Monte Carlo (media cumulativa)
- Fan chart: cenarios ao longo do tempo
- Stress test heatmap (cenario vs portfolio loss)
- Backtest plot: VaR vs perdas realizadas (timeline)
- Sobol indices bar chart
- ABM: grid visualization dos agentes ao longo do tempo

---

## Formato: cada script com docstring, main(), RANDOM_STATE = 42

---

## Criterios de Aceite

- [x] 9 scripts Python criados nas subpastas corretas
- [x] modeling/monte_carlo_var.py — MC VaR/CVaR com normal e t-Student
- [x] modeling/monte_carlo_pricing.py — Pricing de opcoes com variance reduction
- [x] modeling/agent_based_model.py — ABM com Mesa
- [x] modeling/stress_testing.py — Framework de stress testing
- [x] modeling/latin_hypercube.py — LHS com scipy
- [x] validation/convergence_analysis.py — Convergencia MC
- [x] validation/var_backtesting.py — Kupiec + Christoffersen
- [x] validation/sensitivity_sobol.py — Sobol indices com SALib
- [x] visualization/simulation_plots.py — VaR dist, convergence, fan chart, heatmap, backtest, Sobol
- [x] Todos passam verificacao de sintaxe Python
- [x] Todos tem docstring, funcoes organizadas e main()
- [x] Stack: numpy/scipy + mesa + SALib + arch

---

## Bibliotecas Utilizadas

| Biblioteca | Versao Minima | Uso |
|------------|---------------|-----|
| numpy | >= 1.24 | Amostragem, arrays, operacoes numericas |
| scipy | >= 1.11 | Distribuicoes, LHS, testes estatisticos |
| mesa | >= 2.0 | Agent-Based Modeling |
| SALib | >= 1.4 | Analise de sensibilidade (Sobol, Morris) |
| arch | >= 6.0 | Modelos de volatilidade (GARCH), VaR backtesting |
| matplotlib | >= 3.7 | Visualizacoes |
| seaborn | >= 0.12 | Visualizacoes |
| yfinance | >= 0.2 | Download de precos de ativos |
| pandas | >= 2.0 | Manipulacao de dados |

---

**End of Specification**

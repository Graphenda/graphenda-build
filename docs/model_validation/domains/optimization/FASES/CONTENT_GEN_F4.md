# Fase F4 — Codigo de Exemplo

**Status**: COMPLETA
**Dependencias**: F3
**Bloqueia**: F5

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/optimization/`

---

## Arquivos a Gerar

### Modeling (5 arquivos)

#### 1. modeling/linear_programming.py
- LP com PuLP e scipy.optimize.linprog
- Formulacao: variaveis de decisao, funcao objetivo, restricoes
- Interpretacao da solucao dual (shadow prices)
- Exemplo: mix de producao com recursos limitados

#### 2. modeling/mip_scheduling.py
- MIP com PuLP para scheduling
- Variaveis binarias para decisoes on/off
- Restricoes de capacidade, precedencia, janela temporal
- Analise do optimality gap

#### 3. modeling/portfolio_optimization.py
- Otimizacao de portfolio (Markowitz) com cvxpy
- Mean-variance optimization com restricoes
- Efficient frontier
- Comparacao com portfolio equal-weight

#### 4. modeling/metaheuristic_ga.py
- Algoritmo genetico com DEAP
- Operadores: selecao, crossover, mutacao
- Convergencia ao longo das geracoes
- Comparacao com solucao exata (quando possivel)

#### 5. modeling/multi_objective.py
- Otimizacao multi-objetivo com NSGA-II (pymoo)
- Pareto front visualization
- Trade-off analysis entre objetivos
- Selecao de solucao no Pareto front

### Validation (2 arquivos)

#### 6. validation/sensitivity_analysis.py
- Analise de sensibilidade parametrica para LP/MIP
- Variacao de coeficientes da funcao objetivo
- Variacao de RHS das restricoes
- Shadow prices e ranges de validade
- Tornado diagram de sensibilidade

#### 7. validation/feasibility_check.py
- Verificacao automatica de restricoes na solucao
- Deteccao de restricoes binding vs slack
- Infeasibility diagnosis: quais restricoes conflitam
- Relaxation analysis para modelos infeasible

### Visualization (1 arquivo)

#### 8. visualization/optimization_plots.py
- Efficient frontier (portfolio optimization)
- Pareto front (multi-objective)
- Convergencia de metaheuristicas (fitness vs geracao)
- Tornado diagram de sensibilidade
- Gap de otimalidade ao longo do tempo de solucao
- Gantt chart para problemas de scheduling

---

## Formato: cada script com docstring, main(), RANDOM_STATE = 42

---

## Criterios de Aceite

- [x] 8 scripts Python criados nas subpastas corretas
- [x] modeling/linear_programming.py — LP com PuLP + scipy, shadow prices
- [x] modeling/mip_scheduling.py — MIP scheduling com variaveis binarias
- [x] modeling/portfolio_optimization.py — Markowitz com cvxpy, efficient frontier
- [x] modeling/metaheuristic_ga.py — GA com DEAP, convergencia
- [x] modeling/multi_objective.py — NSGA-II com pymoo, Pareto front
- [x] validation/sensitivity_analysis.py — Sensibilidade parametrica, tornado diagram
- [x] validation/feasibility_check.py — Feasibility, binding/slack, infeasibility diagnosis
- [x] visualization/optimization_plots.py — Efficient frontier, Pareto, convergencia, Gantt
- [x] Todos passam verificacao de sintaxe Python
- [x] Todos tem docstring, funcoes organizadas e main()
- [x] Stack: pulp + cvxpy + pymoo + deap

---

## Bibliotecas Utilizadas

| Biblioteca | Versao Minima | Uso |
|------------|---------------|-----|
| pulp | >= 2.7 | LP e MIP com interface simples |
| cvxpy | >= 1.3 | Otimizacao convexa (QP, SOCP) |
| pymoo | >= 0.6 | Otimizacao multi-objetivo (NSGA-II) |
| deap | >= 1.4 | Algoritmos evolutivos e geneticos |
| scipy | >= 1.11 | LP (linprog), NLP (minimize) |
| numpy | >= 1.24 | Operacoes numericas |
| matplotlib | >= 3.7 | Visualizacoes |
| seaborn | >= 0.12 | Visualizacoes |

---

**End of Specification**

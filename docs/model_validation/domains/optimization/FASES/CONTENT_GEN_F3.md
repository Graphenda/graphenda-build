# Fase F3 — Guias Explicativos

**Status**: CONCLUIDO
**Dependencias**: F1
**Bloqueia**: F4, F5

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/optimization/`

---

## Guias a Gerar

### 1. overview.md
- O que sao modelos de otimizacao e como diferem de modelos preditivos
- Tipos: programacao linear (LP), programacao inteira mista (MIP), nao-linear (NLP)
- Metaheuristicas: GA, SA, PSO, ACO
- Aplicacoes: supply chain, portfolio, scheduling, pricing, logistica
- Diferenca entre otimizacao e machine learning: feasibility vs prediction

### 2. models.md
- Programacao Linear (LP): simplex, dual, formulacao padrao
- Programacao Inteira Mista (MIP): branch-and-bound, cutting planes
- Programacao Quadratica (QP): portfolio optimization (Markowitz)
- Programacao Nao-Linear (NLP): metodos de gradiente, restricoes
- Algoritmos Geneticos (GA): populacao, crossover, mutacao, selecao
- Simulated Annealing (SA): cooling schedule, aceitacao de solucoes piores
- Particle Swarm Optimization (PSO): enxame, velocidade, posicao
- Multi-objective optimization: Pareto front, NSGA-II

### 3. validation.md
- Checklist de validacao para modelos de otimizacao
- Feasibility check: todas as restricoes sao satisfeitas?
- Optimality check: gap de otimalidade (MIP gap) aceitavel?
- Analise de sensibilidade: shadow prices, reduced costs
- Variacao de parametros: como a solucao muda com inputs
- Validacao de restricoes: completas, corretas, consistentes
- Benchmarking: comparar com solucoes conhecidas ou heuristicas
- Stress testing: comportamento em cenarios extremos
- Tempo computacional: solucao em tempo aceitavel para operacao

### 4. metrics.md
- Valor da funcao objetivo (minimizacao ou maximizacao)
- Optimality gap: diferenca entre bound e incumbent (MIP)
- Feasibility: numero de restricoes violadas
- Tempo de solucao: tempo ate convergencia
- Shadow prices: valor marginal de relaxar restricoes
- Reduced costs: custo de incluir variaveis fora da base
- Pareto optimality: dominancia em multi-objetivo
- Robustez: variacao da solucao em cenarios perturbados
- Analise de sensibilidade como metrica de confianca

### 5. pitfalls.md
- Formular restricoes incorretas ou incompletas
- Ignorar a qualidade da solucao (aceitar gap muito alto)
- Nao fazer analise de sensibilidade dos parametros
- Otimizar funcao objetivo errada (proxy ruim do objetivo real)
- Metaheuristicas sem convergencia verificada
- Nao validar feasibility da solucao implementada
- Ignorar tempo computacional em contexto operacional
- Over-constraining: modelo infeasible por restricoes excessivas

---

## Formato: `slug: optimization-<nome>`, `domain: optimization`, `type: guide`

Cada guia: minimo 1500 palavras, formulas LaTeX (LP standard form, simplex, Markowitz, NSGA-II crowding distance), referencias da F1.

---

## Criterios de Aceite

- [x] 5 guias criados: overview.md, models.md, validation.md, metrics.md, pitfalls.md
- [x] papers.md da F1 tambem presente
- [x] Todos com frontmatter YAML valido
- [x] Cada guia com minimo de 1500 palavras
- [x] Formulas LaTeX incluidas (LP form, Markowitz, shadow prices)
- [x] Referencias cruzadas aos papers da F1
- [x] Conteudo baseado em pesquisa web

---

**End of Specification**

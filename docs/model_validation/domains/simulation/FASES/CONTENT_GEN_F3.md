# Fase F3 — Guias Explicativos

**Status**: CONCLUIDA
**Dependencias**: F1
**Bloqueia**: F4, F5

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/simulation/`

---

## Guias a Gerar

### 1. overview.md
- O que sao modelos de simulacao e quando usa-los
- Tipos: Monte Carlo, agent-based (ABM), discrete event simulation (DES), system dynamics
- Aplicacoes em financas: VaR, CVaR, pricing de derivativos, stress testing
- Aplicacoes gerais: epidemiologia, logistica, planejamento urbano
- Contexto regulatorio: Basel stress testing, CCAR, DFAST
- Diferenca entre simulacao e modelos analiticos

### 2. models.md
- Monte Carlo basico: amostragem de distribuicoes, lei dos grandes numeros
- Monte Carlo para VaR e CVaR: simulacao historica vs parametrica
- Variance reduction: antithetic variates, control variates, importance sampling
- Latin Hypercube Sampling (LHS): cobertura eficiente do espaco
- Agent-Based Models: agentes, regras, emergencia
- Discrete Event Simulation (DES): filas, processos, recursos
- System Dynamics: stocks, flows, feedback loops
- Stress testing: cenarios historicos, hipoteticos, reverse stress test

### 3. validation.md
- Checklist de validacao para modelos de simulacao
- Verificacao: o codigo implementa corretamente a logica? (code review, unit tests)
- Calibracao: os parametros reproduzem dados historicos?
- Convergencia: quantas simulacoes sao necessarias? (erro de Monte Carlo)
- Backtesting de VaR: Kupiec test, Christoffersen test
- Validacao de distribuicoes de input: fit estatistico, testes de aderencia
- Analise de sensibilidade: quais inputs mais impactam outputs
- Validacao de ABM: emergencia reproduzivel, pattern-oriented modeling
- Stress testing regulatorio: aderencia a cenarios do regulador (Basel, CCAR)

### 4. metrics.md
- VaR (Value at Risk): percentil da distribuicao de perdas
- CVaR / Expected Shortfall: media das perdas alem do VaR
- Erro de Monte Carlo: desvio padrao / sqrt(N)
- Convergence rate: como o erro diminui com N
- Kupiec test (POF): frequencia de violacoes de VaR
- Christoffersen test: independencia e cobertura condicional
- Backtest p-values: adequacao do modelo de risco
- Calibration error: diferenca entre simulado e historico
- Sensitivity indices: Sobol indices para analise de sensibilidade global

### 5. pitfalls.md
- Numero insuficiente de simulacoes (resultado nao convergiu)
- Distribuicoes de input mal especificadas (garbage in, garbage out)
- Ignorar correlacoes entre variaveis de input
- VaR sem backtesting adequado
- Stress testing com cenarios insuficientemente severos
- Nao validar premissas de distribuicao (caudas pesadas vs normal)
- ABM com excesso de parametros sem calibracao
- Pseudo-random numbers sem seed reproduzivel

---

## Formato: `slug: simulation-<nome>`, `domain: simulation`, `type: guide`

Cada guia: minimo 1500 palavras, formulas LaTeX (VaR, CVaR, MC error, Sobol indices, Kupiec LR), referencias da F1.

---

## Criterios de Aceite

- [x] 5 guias criados: overview.md, models.md, validation.md, metrics.md, pitfalls.md
- [x] papers.md da F1 tambem presente
- [x] Todos com frontmatter YAML valido
- [x] Cada guia com minimo de 1500 palavras
- [x] Formulas LaTeX incluidas (VaR, CVaR, MC error, Kupiec LR, Sobol)
- [x] Referencias cruzadas aos papers da F1
- [x] Conteudo baseado em pesquisa web

---

**End of Specification**

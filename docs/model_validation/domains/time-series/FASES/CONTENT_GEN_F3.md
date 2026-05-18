# Fase F3 — Guias Explicativos

**Status**: CONCLUIDO
**Dependencias**: F1 (para referencias dos papers)
**Bloqueia**: F4, F5

---

## Objetivo

Criar 5 guias explicativos completos sobre series temporais, cobrindo desde
a visao geral ate armadilhas comuns. Cada guia deve ser autocontido, tecnico
e util para profissionais de model validation.

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/time-series/`

---

## Guias a Gerar

### 1. overview.md — Visao Geral de Series Temporais

**Conteudo obrigatorio:**
- O que sao series temporais e suas propriedades fundamentais
- Estacionariedade: definicao, importancia e tipos (fraca vs forte)
- Componentes: tendencia, sazonalidade, ciclo, ruido
- Decomposicao aditiva vs multiplicativa
- Quando usar modelos classicos vs machine learning

**Pesquisa web:** buscar aplicacoes recentes em financas, risk management, forecasting

### 2. models.md — Tipos de Modelos de Series Temporais

**Conteudo obrigatorio:**
- AR, MA, ARMA, ARIMA: formulacao e identificacao
- SARIMA: extensao sazonal do ARIMA
- GARCH e variantes (EGARCH, GJR-GARCH): modelagem de volatilidade
- VAR: sistemas multivariados, funcoes impulso-resposta
- VECM: modelos com correcao de erro para series cointegradas
- Exponential Smoothing (ETS): Holt-Winters
- Prophet: decomposicao aditiva com sazonalidade flexivel

**Pesquisa web:** buscar comparacoes praticas, benchmarks recentes (M5 competition)

### 3. validation.md — Validacao de Modelos de Series Temporais

**Conteudo obrigatorio:**
- Testes de estacionariedade (ADF, KPSS, Phillips-Perron)
- Analise de ACF e PACF para identificacao de ordens
- Diagnostico de residuos: Ljung-Box, normalidade
- Testes ARCH para heteroscedasticidade condicional
- Teste de Johansen para cointegracao
- Teste de Granger para causalidade
- Backtesting com janela deslizante (rolling window)

**Pesquisa web:** buscar melhores praticas de validacao, frameworks regulatorios para forecasting

### 4. metrics.md — Metricas de Forecasting e Testes

**Conteudo obrigatorio:**
- MAE, RMSE, MAPE, sMAPE: metricas de acuracia de previsao
- MASE (Mean Absolute Scaled Error): metrica escalada
- AIC, BIC: selecao de ordem do modelo
- Diebold-Mariano test: comparacao de forecasts
- Log-likelihood para modelos GARCH
- Theil's U: comparacao com naive forecast

**Pesquisa web:** buscar debates recentes sobre metricas (MAPE vs sMAPE), melhores praticas

### 5. pitfalls.md — Armadilhas e Erros Comuns

**Conteudo obrigatorio:**
- Aplicar modelos em series nao estacionarias
- Ignorar sazonalidade na modelagem
- Overfitting por excesso de parametros (ARIMA de ordem alta)
- Confundir correlacao temporal com causalidade
- Nao fazer split temporal correto (data leakage)
- Ignorar quebras estruturais
- Usar metricas inadequadas (MAPE com zeros)

**Pesquisa web:** buscar case studies de falhas em forecasting, exemplos da industria

---

## Formato de Cada Guia

```markdown
---
slug: time-series-<nome>
name: "<Titulo do Guia>"
domain: time-series
type: guide
difficulty: intermediate
status: draft
tags: [time-series, <tags-especificas>]
references:
  - title: "<titulo>"
    authors: "<autores>"
    year: <ano>
    type: paper
---

# <Titulo>

## Introducao
[Contexto e motivacao — 2-3 paragrafos]

## [Secoes do conteudo]
[Conteudo tecnico com formulas LaTeX quando necessario]

### [Subsecoes]
[Detalhes, exemplos, tabelas comparativas]

## Summary
[Resumo em 3-5 bullet points]

## References
[Lista de referencias usadas]
```

---

## Etapas de Implementacao

### Etapa 1: Leitura de Referencias

- Ler o arquivo `papers.md` gerado na F1 (se disponivel)
- Ler a especificacao completa: `/home/guhaase/projetos/Graphenda/build/docs/model_validation/domains/03-time-series.md`

### Etapa 2: Pesquisa Complementar

Para cada guia:
- Buscar na web conteudo complementar aos papers
- Buscar exemplos praticos da industria financeira (volatilidade, VaR, forecasting)
- Buscar melhores praticas de model validation para series temporais

### Etapa 3: Redacao dos Guias

Para cada guia:
- Redigir com minimo de 1500 palavras
- Incluir formulas LaTeX para conceitos matematicos (ARIMA, GARCH, ACF)
- Incluir tabelas comparativas quando aplicavel (ARIMA vs GARCH vs VAR)
- Referenciar papers da F1
- Tom tecnico mas didatico

### Etapa 4: Salvamento e Verificacao

```bash
# Verificar que todos os 5 guias existem
ls -la /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/time-series/

# Verificar frontmatter de cada um
for f in /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/time-series/*.md; do
    echo "=== $(basename $f) ==="
    head -15 "$f"
    echo ""
done

# Verificar tamanho minimo (pelo menos 80 linhas cada)
wc -l /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/time-series/*.md
```

---

## Criterios de Aceite

- [x] 5 guias criados: overview.md, models.md, validation.md, metrics.md, pitfalls.md
- [x] Alem dos 5 guias, papers.md da F1 tambem presente no diretorio
- [x] Todos com frontmatter YAML valido (slug, name, domain, type, difficulty, status, tags)
- [x] Cada guia com minimo de 1500 palavras
- [x] Formulas LaTeX incluidas onde necessario
- [x] Referencias cruzadas aos papers da F1
- [x] Conteudo baseado em pesquisa web
- [x] Tom tecnico e adequado para profissionais de model validation

---

## Ferramentas Necessarias

- **Read**: para ler papers.md (F1) e a spec do dominio
- **WebSearch**: para pesquisa complementar
- **WebFetch**: para acessar fontes especificas
- **Write**: para criar cada guia

---

**End of Specification**

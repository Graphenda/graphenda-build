# Fase F1 — Papers Academicos e Referencias

**Status**: CONCLUIDO
**Dependencias**: Nenhuma
**Bloqueia**: F3, F4, F5

---

## Objetivo

Pesquisar, resumir e catalogar os papers academicos e livros de referencia
sobre series temporais listados na especificacao do dominio, gerando um
arquivo consolidado de referencias para o ModelRiskLab.

---

## Arquivo de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/time-series/papers.md`

---

## Especificacao de Conteudo

Para cada paper/livro listado abaixo, busque na web e produza:

1. **Resumo** (3-5 paragrafos): contribuicao principal, metodologia, impacto na area
2. **Relevancia para Model Validation**: como o paper se aplica a validacao de modelos
3. **Key Takeaways**: 3-5 pontos principais
4. **Citacao formatada**: formato APA

### Papers a Cobrir

| # | Paper | Autores | Ano | Foco |
|---|-------|---------|-----|------|
| 1 | Time Series Analysis: Forecasting and Control | Box, Jenkins | 1970 | Fundamento ARIMA e metodologia Box-Jenkins |
| 2 | Autoregressive Conditional Heteroscedasticity with Estimates of the Variance of UK Inflation | Engle | 1982 | Modelo ARCH original |
| 3 | Generalized Autoregressive Conditional Heteroskedasticity | Bollerslev | 1986 | Extensao GARCH |
| 4 | Estimation and Hypothesis Testing of Cointegration Vectors in Gaussian VAR Models | Johansen | 1991 | Cointegracao e VECM |
| 5 | Co-integration and Error Correction: Representation, Estimation, and Testing | Engle, Granger | 1987 | Cointegracao de Engle-Granger |
| 6 | Vector Autoregressions | Sims | 1980 | Modelo VAR e impulso-resposta |
| 7 | Testing for a Unit Root in Time Series Regression | Dickey, Fuller | 1979 | Teste ADF de raiz unitaria |

---

## Formato do Arquivo de Saida

```markdown
---
slug: time-series-papers
name: "Academic Papers & References — Time Series Models"
domain: time-series
type: reference-guide
status: draft
tags: [time-series, papers, academic, references, econometrics, forecasting]
---

# Academic Papers & References — Time Series Models

## 1. Box & Jenkins (1970) — ARIMA and the Box-Jenkins Methodology

### Summary
[3-5 paragrafos]

### Relevance to Model Validation
[Como se aplica]

### Key Takeaways
- [ponto 1]
- [ponto 2]
- [ponto 3]

### Citation
[APA format]

---

## 2. [Proximo paper...]
[...]
```

---

## Etapas de Implementacao

### Etapa 1: Pesquisa de Papers

Para cada um dos 7 papers/livros listados:
- Busque na web informacoes sobre o paper (abstract, contribuicoes, citacoes)
- Busque contexto sobre a relevancia para model risk management e forecasting
- Registre as informacoes encontradas

### Etapa 2: Redacao dos Resumos

Para cada paper, redija:
- Resumo academico (3-5 paragrafos)
- Secao de relevancia para validacao de modelos
- Key takeaways (3-5 bullet points)
- Citacao APA

### Etapa 3: Montagem do Arquivo

- Monte o arquivo `papers.md` no formato especificado
- Inclua frontmatter YAML valido
- Garanta que todos os 7 papers estao cobertos

### Etapa 4: Verificacao

```bash
# Verificar que o arquivo existe
ls -la /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/time-series/papers.md

# Verificar frontmatter YAML
head -10 /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/time-series/papers.md

# Verificar que todos os 7 papers estao presentes
grep -c "^## " /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/time-series/papers.md
```

---

## Criterios de Aceite

- [x] Arquivo `papers.md` criado no destino correto
- [x] Frontmatter YAML valido com slug, name, domain, type, status, tags
- [x] Todos os 7 papers cobertos com resumo, relevancia, takeaways e citacao
- [x] Cada resumo tem pelo menos 3 paragrafos
- [x] Cada paper tem pelo menos 3 key takeaways
- [x] Citacoes em formato APA
- [x] Conteudo buscado na web (nao inventado)

---

## Ferramentas Necessarias

- **WebSearch**: para buscar informacoes sobre cada paper
- **WebFetch**: para acessar paginas com detalhes dos papers
- **Write**: para criar o arquivo final

---

**End of Specification**

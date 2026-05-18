# Fase F1 — Papers Academicos e Referencias

**Status**: CONCLUIDO
**Dependencias**: Nenhuma
**Bloqueia**: F3, F4, F5

---

## Objetivo

Pesquisar, resumir e catalogar os papers academicos e livros de referencia
sobre regressao linear listados na especificacao do dominio, gerando um
arquivo consolidado de referencias para o ModelRiskLab.

---

## Arquivo de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/linear-regression/papers.md`

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
| 1 | Regression Diagnostics: Identifying Influential Data and Sources of Collinearity | Belsley, Kuh, Welsch | 1980 | Diagnosticos classicos |
| 2 | Ridge Regression: Biased Estimation for Nonorthogonal Problems | Hoerl, Kennard | 1970 | Regularizacao L2 |
| 3 | Regression Shrinkage and Selection via the Lasso | Tibshirani | 1996 | Lasso (L1) |
| 4 | Regularization and Variable Selection via the Elastic Net | Zou, Hastie | 2005 | Elastic Net |
| 5 | Robust Regression and Outlier Detection | Rousseeuw, Leroy | 1987 | Regressao robusta |
| 6 | An Introduction to Statistical Learning (Cap. 3, 6) | James, Witten, Hastie, Tibshirani | 2013 | Referencia didatica |
| 7 | Applied Linear Statistical Models | Kutner, Nachtsheim, Neter, Li | 2004 | Diagnosticos completos |

---

## Formato do Arquivo de Saida

```markdown
---
slug: linear-regression-papers
name: "Academic Papers & References — Linear Regression"
domain: linear-regression
type: reference-guide
status: draft
tags: [linear-regression, papers, academic, references]
---

# Academic Papers & References — Linear Regression

## 1. Regression Diagnostics (Belsley, Kuh & Welsch, 1980)

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
- Busque contexto sobre a relevancia do paper para model risk management
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
ls -la /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/linear-regression/papers.md

# Verificar frontmatter YAML (deve ter slug, name, domain, type, status, tags)
head -10 /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/linear-regression/papers.md

# Verificar que todos os 7 papers estao presentes
grep -c "^## " /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/linear-regression/papers.md
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

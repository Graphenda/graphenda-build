# Fase F1 — Papers Academicos e Referencias

**Status**: PENDENTE
**Dependencias**: Nenhuma
**Bloqueia**: F3, F4, F5

---

## Objetivo

Pesquisar, resumir e catalogar os papers academicos e livros de referencia
sobre Generalized Linear Models listados na especificacao do dominio, gerando um
arquivo consolidado de referencias para o ModelRiskLab.

---

## Arquivo de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/glm/papers.md`

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
| 1 | Generalized Linear Models | McCullagh, Nelder | 1989 | Referencia fundamental de GLMs |
| 2 | Applied Logistic Regression | Hosmer, Lemeshow | 2000 | Logistica aplicada e teste de calibracao |
| 3 | An Introduction to Generalized Linear Models | Dobson, Barnett | 2008 | Texto didatico moderno |
| 4 | Regression Models for Count Data in R | Zeileis, Kleiber, Jackman | 2008 | Poisson, NB e zero-inflated |
| 5 | The Statistical Analysis of Failure Time Data | Kalbfleisch, Prentice | 2002 | GLMs para dados de sobrevivencia |
| 6 | Generalized Additive Models | Hastie, Tibshirani | 1990 | Extensao nao-parametrica dos GLMs |
| 7 | Maximum Likelihood Estimation for the Negative Binomial Distribution | Lawless | 1987 | NB como alternativa a Poisson |

---

## Formato do Arquivo de Saida

```markdown
---
slug: glm-papers
name: "Academic Papers & References — Generalized Linear Models"
domain: glm
type: reference-guide
status: draft
tags: [glm, papers, academic, references, logistic-regression, poisson, credit-scoring]
---

# Academic Papers & References — Generalized Linear Models

## 1. McCullagh & Nelder (1989) — Generalized Linear Models

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
- Busque contexto sobre a relevancia para model risk management, credit scoring e seguros
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
ls -la /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/glm/papers.md
head -10 /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/glm/papers.md
grep -c "^## " /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/glm/papers.md
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

# Fase F1 — Papers Academicos e Referencias

**Status**: PENDENTE
**Dependencias**: Nenhuma
**Bloqueia**: F3, F4, F5

---

## Objetivo

Pesquisar, resumir e catalogar os papers academicos e livros de referencia
sobre analise de sobrevivencia listados na especificacao do dominio.

---

## Arquivo de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/survival/papers.md`

---

## Papers a Cobrir

| # | Paper | Autores | Ano | Foco |
|---|-------|---------|-----|------|
| 1 | Regression Models and Life-Tables | Cox | 1972 | Cox PH (riscos proporcionais) |
| 2 | Nonparametric Estimation from Incomplete Observations | Kaplan, Meier | 1958 | Estimador Kaplan-Meier |
| 3 | Evaluating the Yield of Medical Tests | Harrell, Califf, Pryor, Lee, Rosati | 1982 | C-statistic (concordance index) |
| 4 | The Statistical Analysis of Failure Time Data | Kalbfleisch, Prentice | 2002 | Referencia completa de sobrevivencia |
| 5 | Regression Modeling Strategies | Harrell | 2015 | Validacao e calibracao de modelos Cox |
| 6 | Modelling Survival Data in Medical Research | Collett | 2015 | Texto aplicado de sobrevivencia |
| 7 | A Class of K-Sample Tests for Comparing the Cumulative Incidence of a Competing Risk | Gray | 1988 | Riscos competitivos |

---

## Formato do Arquivo de Saida

```markdown
---
slug: survival-papers
name: "Academic Papers & References — Survival Models"
domain: survival
type: reference-guide
status: draft
tags: [survival, papers, academic, references, cox-ph, kaplan-meier, competing-risks]
---

# Academic Papers & References — Survival Models

## 1. Cox (1972) — Regression Models and Life-Tables

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
```

---

## Etapas de Implementacao

### Etapa 1: Pesquisa de Papers
Para cada um dos 7 papers: buscar na web abstract, contribuicoes, citacoes, relevancia para MRM.

### Etapa 2: Redacao dos Resumos
Para cada paper: resumo (3-5 paragrafos), relevancia, key takeaways (3-5), citacao APA.

### Etapa 3: Montagem do Arquivo
Montar `papers.md` com frontmatter YAML valido e todos os 7 papers.

### Etapa 4: Verificacao
```bash
ls -la /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/survival/papers.md
head -10 /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/survival/papers.md
grep -c "^## " /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/survival/papers.md
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

- **WebSearch**, **WebFetch**, **Write**

---

**End of Specification**

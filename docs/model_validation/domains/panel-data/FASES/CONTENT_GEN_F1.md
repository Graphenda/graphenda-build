# Fase F1 — Papers Academicos e Referencias

**Status**: PENDENTE
**Dependencias**: Nenhuma
**Bloqueia**: F3, F4, F5

---

## Objetivo

Pesquisar, resumir e catalogar os papers academicos e livros de referencia
sobre dados em painel listados na especificacao do dominio, gerando um
arquivo consolidado de referencias para o ModelRiskLab.

---

## Arquivo de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/panel-data/papers.md`

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
| 1 | Some Tests of Specification for Panel Data: Monte Carlo Evidence and an Application to Employment Equations | Arellano, Bond | 1991 | GMM para paineis dinamicos |
| 2 | Specification Tests in Econometrics | Hausman | 1978 | Teste Hausman (FE vs RE) |
| 3 | Econometric Analysis of Cross Section and Panel Data | Wooldridge | 2010 | Referencia completa de paineis |
| 4 | Initial Conditions and Moment Restrictions in Dynamic Panel Data Models | Blundell, Bond | 1998 | System GMM |
| 5 | Panel Data Econometrics | Baltagi | 2005 | Manual classico de paineis |
| 6 | Fixed Effects, Random Effects and Hausman's Test | Clark, Linzer | 2015 | Revisao moderna do Hausman |
| 7 | Estimation and Inference in Short Panel Vector Autoregressions with Unit Roots and Cointegration | Binder, Hsiao, Pesaran | 2005 | PVAR e cointegracao em painel |

---

## Formato do Arquivo de Saida

```markdown
---
slug: panel-data-papers
name: "Academic Papers & References — Panel Data Models"
domain: panel-data
type: reference-guide
status: draft
tags: [panel-data, papers, academic, references, econometrics]
---

# Academic Papers & References — Panel Data Models

## 1. Arellano & Bond (1991) — GMM for Dynamic Panels

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
- Busque contexto sobre a relevancia para model risk management e econometria aplicada
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
ls -la /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/panel-data/papers.md

# Verificar frontmatter YAML
head -10 /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/panel-data/papers.md

# Verificar que todos os 7 papers estao presentes
grep -c "^## " /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/panel-data/papers.md
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

# Fase F2 — Noticias e Artigos

**Status**: CONCLUIDO
**Dependencias**: Nenhuma
**Bloqueia**: Nenhuma (conteudo independente)

---

## Objetivo

Pesquisar e redigir artigos no formato de noticias/tutoriais sobre GLMs,
cobrindo os topicos listados na especificacao do dominio. Cada artigo deve ser
independente e seguir o template de news do mrl-content-files.

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/news/`

---

## Template de Referencia

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/templates/news.md`

---

## Artigos a Gerar

| # | Titulo Sugerido | Tipo | Slug |
|---|-----------------|------|------|
| 1 | Understanding Logistic Regression from Scratch | Tutorial | understanding-logistic-regression-scratch |
| 2 | Poisson Regression: When Counts Matter | Tutorial | poisson-regression-when-counts-matter |
| 3 | Link Functions in GLMs Explained Intuitively | Tutorial | link-functions-glms-explained-intuitively |
| 4 | Hosmer-Lemeshow Test: Assessing Model Calibration | Tecnica | hosmer-lemeshow-test-model-calibration |
| 5 | Overdispersion in Count Models: Detection and Solutions | Pitfalls | overdispersion-count-models-detection-solutions |
| 6 | GLMs in Insurance Pricing: Industry Best Practices | Case study | glms-insurance-pricing-best-practices |
| 7 | Logistic Regression in Credit Scoring Under SR 11-7 | Regulatorio | logistic-regression-credit-scoring-sr-11-7 |

---

## Formato de Cada Arquivo

Seguir o template `news.md`:

```markdown
---
slug: <slug-do-artigo>
title: "<titulo>"
subtitle: "<subtitulo breve>"
category: model-validation
tags: [glm, <tags-especificas>]
isFeatured: false
isEditorial: false
status: draft
publishedAt: 2026-03-16
sourceUrl: null
---

## [Secao principal]

[Conteudo do artigo — minimo 800 palavras]

### [Subsecoes]

[Detalhes tecnicos, exemplos, codigo quando relevante]

## Key Takeaways

- [ponto 1]
- [ponto 2]
- [ponto 3]

## References

- [referencia 1]
- [referencia 2]
```

---

## Etapas de Implementacao

### Etapa 1: Pesquisa de Conteudo

Para cada um dos 7 artigos:
- Busque na web conteudo atualizado e relevante sobre o topico
- Identifique fontes confiaveis (papers, blogs tecnicos, documentacao regulatoria)
- Colete exemplos praticos e dados

### Etapa 2: Redacao dos Artigos

Para cada artigo:
- Redija com minimo de 800 palavras
- Inclua exemplos praticos (credit scoring, seguros, contagens)
- Inclua snippets de codigo Python quando aplicavel (statsmodels, sklearn)
- Mantenha tom tecnico mas acessivel
- Adicione referencias ao final

### Etapa 3: Salvamento dos Arquivos

Salvar cada artigo como:
`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/news/2026-03-16_<slug>.md`

### Etapa 4: Verificacao

```bash
ls -la /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/news/2026-03-16_*{logistic,poisson,link-function,hosmer,overdispersion,glm,credit-scoring}*.md

for f in /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/news/2026-03-16_*{logistic,poisson,link-function,hosmer,overdispersion,glm,credit-scoring}*.md; do
    echo "=== $(basename $f) ==="
    head -12 "$f"
    echo ""
done

wc -l /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/news/2026-03-16_*{logistic,poisson,link-function,hosmer,overdispersion,glm,credit-scoring}*.md
```

---

## Criterios de Aceite

- [x] 7 artigos criados no diretorio de destino
- [x] Todos seguem o template news.md com frontmatter YAML valido
- [x] Cada artigo tem no minimo 800 palavras
- [x] Cada artigo tem secao de Key Takeaways
- [x] Cada artigo tem secao de References
- [x] Conteudo baseado em pesquisa web (nao inventado)
- [x] Tags incluem "glm" em todos os artigos

---

## Ferramentas Necessarias

- **WebSearch**: para buscar conteudo atualizado sobre cada topico
- **WebFetch**: para acessar fontes especificas
- **Write**: para criar cada arquivo de artigo

---

**End of Specification**

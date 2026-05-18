# Fase F2 — Noticias e Artigos

**Status**: COMPLETO
**Dependencias**: Nenhuma
**Bloqueia**: Nenhuma (conteudo independente)

---

## Objetivo

Pesquisar e redigir artigos no formato de noticias/tutoriais sobre regressao linear,
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
| 1 | Assumptions of Linear Regression: A Complete Checklist | Tutorial | assumptions-linear-regression-checklist |
| 2 | When Linear Regression Fails: Real-World Case Studies | Case study | when-linear-regression-fails-case-studies |
| 3 | OLS vs Ridge vs Lasso: A Practical Comparison for Model Validators | Comparacao | ols-ridge-lasso-practical-comparison |
| 4 | Multicollinearity: Detection and Remedies in Practice | Tutorial | multicollinearity-detection-remedies |
| 5 | Model Validation for Linear Models Under SR 11-7 | Regulatorio | model-validation-linear-models-sr-11-7 |
| 6 | Why Your R-Squared Might Be Lying to You | Pitfalls | r-squared-might-be-lying |
| 7 | Robust Regression: When Outliers Break Your Model | Tecnica | robust-regression-outliers-break-model |

---

## Formato de Cada Arquivo

Seguir o template `news.md`:

```markdown
---
slug: <slug-do-artigo>
title: "<titulo>"
subtitle: "<subtitulo breve>"
category: model-validation
tags: [linear-regression, <tags-especificas>]
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
- Identifique fontes confiaveis (papers, blogs tecnicos, documentacao)
- Colete exemplos praticos e dados

### Etapa 2: Redacao dos Artigos

Para cada artigo:
- Redija com minimo de 800 palavras
- Inclua exemplos praticos
- Inclua snippets de codigo Python quando aplicavel
- Mantenha tom tecnico mas acessivel
- Adicione referencias ao final

### Etapa 3: Salvamento dos Arquivos

Salvar cada artigo como:
`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/news/2026-03-16_<slug>.md`

### Etapa 4: Verificacao

```bash
# Verificar que todos os 7 artigos existem
ls -la /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/news/2026-03-16_*

# Verificar frontmatter de cada um
for f in /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/news/2026-03-16_*.md; do
    echo "=== $(basename $f) ==="
    head -12 "$f"
    echo ""
done

# Verificar tamanho minimo (pelo menos 50 linhas cada)
wc -l /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/news/2026-03-16_*.md
```

---

## Criterios de Aceite

- [x] 7 artigos criados no diretorio de destino
- [x] Todos seguem o template news.md com frontmatter YAML valido
- [x] Cada artigo tem no minimo 800 palavras
- [x] Cada artigo tem secao de Key Takeaways
- [x] Cada artigo tem secao de References
- [x] Conteudo baseado em pesquisa web (nao inventado)
- [x] Tags incluem "linear-regression" em todos os artigos

---

## Ferramentas Necessarias

- **WebSearch**: para buscar conteudo atualizado sobre cada topico
- **WebFetch**: para acessar fontes especificas
- **Write**: para criar cada arquivo de artigo

---

**End of Specification**

# Fase F2 — Noticias e Artigos

**Status**: CONCLUIDO
**Dependencias**: Nenhuma
**Bloqueia**: Nenhuma (conteudo independente)

---

## Objetivo

Pesquisar e redigir artigos no formato de noticias/tutoriais sobre dados em painel,
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
| 1 | Fixed Effects vs Random Effects: When to Use Which | Tutorial | fixed-effects-vs-random-effects-guide |
| 2 | A Practical Guide to Panel Data Regression in Python | Tutorial | practical-guide-panel-data-python |
| 3 | Arellano-Bond GMM Estimation Explained | Tecnica | arellano-bond-gmm-estimation-explained |
| 4 | Common Pitfalls in Panel Data Analysis | Pitfalls | common-pitfalls-panel-data-analysis |
| 5 | Panel Data Models in Credit Risk: Regulatory Perspectives | Regulatorio | panel-data-credit-risk-regulatory |
| 6 | Hausman Test: Interpretation and Limitations | Tutorial | hausman-test-interpretation-limitations |
| 7 | Dynamic Panel Bias: The Nickell Problem | Tecnica | dynamic-panel-bias-nickell-problem |

---

## Formato de Cada Arquivo

Seguir o template `news.md`:

```markdown
---
slug: <slug-do-artigo>
title: "<titulo>"
subtitle: "<subtitulo breve>"
category: model-validation
tags: [panel-data, <tags-especificas>]
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
- Inclua snippets de codigo Python quando aplicavel (linearmodels, statsmodels)
- Mantenha tom tecnico mas acessivel
- Adicione referencias ao final

### Etapa 3: Salvamento dos Arquivos

Salvar cada artigo como:
`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/news/2026-03-16_<slug>.md`

### Etapa 4: Verificacao

```bash
# Verificar que todos os 7 artigos existem
ls -la /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/news/2026-03-16_*panel*
ls -la /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/news/2026-03-16_*fixed*
ls -la /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/news/2026-03-16_*hausman*
ls -la /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/news/2026-03-16_*arellano*
ls -la /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/news/2026-03-16_*nickell*

# Verificar frontmatter de cada um
for f in /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/news/2026-03-16_*{panel,fixed,hausman,arellano,nickell,gmm,dynamic}*.md; do
    echo "=== $(basename $f) ==="
    head -12 "$f"
    echo ""
done

# Verificar tamanho minimo (pelo menos 50 linhas cada)
wc -l /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/news/2026-03-16_*{panel,fixed,hausman,arellano,nickell}*.md
```

---

## Criterios de Aceite

- [x] 7 artigos criados no diretorio de destino
- [x] Todos seguem o template news.md com frontmatter YAML valido
- [x] Cada artigo tem no minimo 800 palavras
- [x] Cada artigo tem secao de Key Takeaways
- [x] Cada artigo tem secao de References
- [x] Conteudo baseado em pesquisa web (nao inventado)
- [x] Tags incluem "panel-data" em todos os artigos

---

## Ferramentas Necessarias

- **WebSearch**: para buscar conteudo atualizado sobre cada topico
- **WebFetch**: para acessar fontes especificas
- **Write**: para criar cada arquivo de artigo

---

**End of Specification**

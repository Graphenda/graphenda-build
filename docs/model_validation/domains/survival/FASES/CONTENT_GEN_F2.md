# Fase F2 — Noticias e Artigos

**Status**: CONCLUIDO
**Dependencias**: Nenhuma
**Bloqueia**: Nenhuma

---

## Objetivo

Pesquisar e redigir artigos sobre analise de sobrevivencia, seguindo o template news.

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/news/`

## Template: `/home/guhaase/projetos/ModelRiskLab/mrl-content-files/templates/news.md`

---

## Artigos a Gerar

| # | Titulo Sugerido | Tipo | Slug |
|---|-----------------|------|------|
| 1 | Survival Analysis in Python: A Complete Guide | Tutorial | survival-analysis-python-complete-guide |
| 2 | Cox Proportional Hazards: Assumptions and Diagnostics | Tutorial | cox-proportional-hazards-assumptions-diagnostics |
| 3 | Kaplan-Meier Curves Explained Simply | Tutorial | kaplan-meier-curves-explained-simply |
| 4 | C-statistic vs AUC: Concordance in Survival Models | Tecnica | c-statistic-vs-auc-concordance-survival |
| 5 | Survival Models in Credit Risk: Time-to-Default | Case study | survival-models-credit-risk-time-to-default |
| 6 | Competing Risks: When Events Compete for Attention | Tecnica | competing-risks-events-compete-attention |
| 7 | Testing the Proportional Hazards Assumption | Pitfalls | testing-proportional-hazards-assumption |

---

## Formato: seguir template `news.md`

Salvar como: `2026-03-16_<slug>.md`

Cada artigo: minimo 800 palavras, Key Takeaways, References, tags incluem "survival".

---

## Etapas de Implementacao

### Etapa 1: Pesquisa — buscar conteudo atualizado para cada topico
### Etapa 2: Redacao — minimo 800 palavras, codigo Python quando aplicavel (lifelines)
### Etapa 3: Salvamento — salvar no diretorio de destino
### Etapa 4: Verificacao

```bash
ls -la /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/news/2026-03-16_*survival*.md
ls -la /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/news/2026-03-16_*cox*.md
ls -la /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/news/2026-03-16_*kaplan*.md
ls -la /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/news/2026-03-16_*competing*.md
```

---

## Criterios de Aceite

- [x] 7 artigos criados no diretorio de destino
- [x] Todos seguem o template news.md com frontmatter YAML valido
- [x] Cada artigo tem no minimo 800 palavras
- [x] Cada artigo tem secao de Key Takeaways
- [x] Cada artigo tem secao de References
- [x] Conteudo baseado em pesquisa web (nao inventado)
- [x] Tags incluem "survival" em todos os artigos

---

## Ferramentas Necessarias

- **WebSearch**, **WebFetch**, **Write**

---

**End of Specification**

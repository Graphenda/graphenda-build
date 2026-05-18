# Fase F3 — Guias Explicativos

**Status**: COMPLETO
**Dependencias**: F1
**Bloqueia**: F4, F5

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/recommender/`

---

## Guias a Gerar

### 1. overview.md
- Sistemas de recomendacao e ubiquidade
- Tipos: collaborative filtering, content-based, hibrido
- Feedback explicito vs implicito
- Desafios: cold start, escalabilidade, diversidade vs relevancia
- Metricas de negocio vs metricas de ranking

### 2. models.md
- CF baseado em usuario e item
- Matrix Factorization: SVD, ALS, NMF
- BPR: ranking para feedback implicito
- NCF: GMF + MLP
- Wide & Deep: crossed features + embeddings
- Autoencoders para CF
- Content-based com TF-IDF e embeddings
- Hibridos: CF + content
- GRU4Rec para sessoes

### 3. validation.md
- Checklist para sistemas de recomendacao
- Split temporal: treino no passado, avaliacao no futuro
- Leave-one-out vs hold-out temporal
- Offline vs online (A/B testing)
- Cold start: avaliacao separada
- Diversidade e cobertura de catalogo
- Fairness: exposicao equilibrada
- Popularity bias analysis

### 4. metrics.md
- Precision@k e Recall@k
- NDCG: graded relevance
- MAP: ranking binario
- MRR: posicao do primeiro acerto
- Hit Rate@k
- Coverage: catalogo recomendado
- Diversity: dissimilaridade media
- Novelty: itens incomuns
- Metricas de negocio: CTR, conversion, revenue

### 5. pitfalls.md
- Metricas offline sem A/B
- Popularity bias
- Cold start nao tratado
- Split aleatorio (data leakage temporal)
- Otimizar accuracy ignorando diversidade
- Feedback loop
- Nao monitorar coverage e fairness

---

## Formato: `slug: recommender-<nome>`, `domain: recommender`, `type: guide`

Cada guia: minimo 1500 palavras, formulas LaTeX (MF objective, NDCG, BPR), referencias da F1.

---

## Criterios de Aceite

- [x] 5 guias criados: overview.md, models.md, validation.md, metrics.md, pitfalls.md
- [x] papers.md da F1 tambem presente
- [x] Todos com frontmatter YAML valido
- [x] Cada guia com minimo de 1500 palavras
- [x] Formulas LaTeX incluidas (MF, NDCG, BPR loss)
- [x] Referencias cruzadas aos papers da F1
- [x] Conteudo baseado em pesquisa web

---

**End of Specification**

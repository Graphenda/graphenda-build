# Fase F4 — Codigo de Exemplo

**Status**: COMPLETO
**Dependencias**: F3
**Bloqueia**: F5

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/recommender/`

---

## Arquivos a Gerar

### Modeling (4 arquivos)

#### 1. modeling/matrix_factorization.py
- SVD e ALS com surprise e implicit
- Tuning de fatores e regularizacao
- Precision@k e NDCG
- Comparacao SVD vs ALS para feedback implicito
- Dataset: MovieLens 100K (surprise)

#### 2. modeling/neural_collaborative_filtering.py
- NCF com PyTorch: GMF + MLP
- Embedding de usuarios e itens
- Negative sampling para feedback implicito
- Metricas de ranking
- Dataset: MovieLens 100K

#### 3. modeling/content_based.py
- Content-based com TF-IDF de descricoes
- Embeddings de itens com sentence-transformers
- Similaridade coseno
- Hibrido: CF scores + content similarity
- Dataset: MovieLens 100K + metadados

#### 4. modeling/wide_and_deep.py
- Wide & Deep com Keras
- Crossed features + embeddings
- Feedback implicito
- Comparacao com NCF e MF
- Dataset: MovieLens 100K

### Validation (2 arquivos)

#### 5. validation/offline_evaluation.py
- Pipeline de avaliacao offline completo
- Temporal split com hold-out
- Leave-one-out evaluation
- Precision@k, Recall@k, NDCG, MRR, Hit Rate
- Comparacao entre modelos com CI
- Dataset: MovieLens 100K

#### 6. validation/coverage_fairness.py
- Catalog coverage: % de itens recomendados
- Popularity bias: distribuicao de recomendacoes
- Gini coefficient de exposicao
- Fairness entre grupos de usuarios
- Dataset: modelos treinados nas F4.1-F4.4

### Visualization (1 arquivo)

#### 7. visualization/recommender_plots.py
- Precision@k e NDCG vs k (line chart comparativo)
- Popularidade vs frequencia de recomendacao (scatter)
- Coverage heatmap por categoria
- Distribuicao de ratings preditos vs reais
- Long tail analysis
- Dataset: modelos anteriores

---

## Formato: cada script com docstring, main(), RANDOM_STATE = 42

---

## Criterios de Aceite

- [x] 7 scripts Python criados nas subpastas corretas
- [x] modeling/matrix_factorization.py — SVD + ALS com surprise/implicit
- [x] modeling/neural_collaborative_filtering.py — NCF GMF+MLP com PyTorch
- [x] modeling/content_based.py — TF-IDF + sentence embeddings + hibrido
- [x] modeling/wide_and_deep.py — Wide & Deep com Keras
- [x] validation/offline_evaluation.py — Pipeline temporal split completo
- [x] validation/coverage_fairness.py — Coverage, popularity bias, Gini
- [x] visualization/recommender_plots.py — Precision@k, NDCG, long tail, coverage
- [x] Todos passam verificacao de sintaxe Python
- [x] Todos tem docstring, funcoes organizadas e main()
- [x] Stack: surprise + implicit + torch + MovieLens 100K

---

## Bibliotecas Utilizadas

| Biblioteca | Versao Minima | Uso |
|------------|---------------|-----|
| surprise | >= 1.1 | SVD, KNN collaborative filtering |
| implicit | >= 0.7 | ALS, BPR para feedback implicito |
| torch | >= 2.0 | NCF customizado |
| tensorflow | >= 2.13 | Wide & Deep (Keras) |
| sentence-transformers | >= 2.2 | Content embeddings |
| scikit-learn | >= 1.3 | TF-IDF, metricas |
| matplotlib | >= 3.7 | Visualizacoes |
| seaborn | >= 0.12 | Visualizacoes |

---

**End of Specification**

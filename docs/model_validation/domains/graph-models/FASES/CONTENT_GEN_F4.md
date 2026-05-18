# Fase F4 — Codigo de Exemplo

**Status**: COMPLETO
**Dependencias**: F3
**Bloqueia**: F5

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/graph-models/`

---

## Arquivos a Gerar

### Modeling (4 arquivos)

#### 1. modeling/gcn_node_classification.py
- GCN com PyTorch Geometric para node classification
- Preparacao do grafo: features, edges, labels
- Treino com masked split (transductive)
- Avaliacao em nos de teste
- Dataset: Cora (PyG)

#### 2. modeling/graphsage_inductive.py
- GraphSAGE com PyTorch Geometric
- Neighbor sampling para escalabilidade
- Inductive learning: generalizar para novos nos
- Mini-batch training com NeighborLoader
- Dataset: Cora (PyG)

#### 3. modeling/knowledge_graph_embeddings.py
- TransE, DistMult, ComplEx com PyKEEN
- Treino em knowledge graph
- Link prediction com filtered ranking
- Visualizacao de embeddings de entidades
- Dataset: FB15k-237 (PyKEEN)

#### 4. modeling/node2vec_embeddings.py
- Node2Vec com random walks
- Tunning de p e q (BFS vs DFS)
- Clustering e visualizacao de comunidades
- Comparacao com GCN embeddings
- Dataset: Cora (PyG)

### Validation (2 arquivos)

#### 5. validation/graph_model_eval.py
- Split correto para link prediction (temporal ou random)
- Negative sampling strategies
- Avaliacao: MRR, Hits@k, AUC-ROC
- Comparacao com baselines: Jaccard, Adamic-Adar, Common Neighbors
- Dataset: Cora (PyG)

#### 6. validation/over_smoothing_analysis.py
- Performance vs numero de camadas GCN
- MADGap: distancia media entre classes por camada
- Comparacao de tecnicas de mitigacao (DropEdge, residual connections)
- Visualizacao da homogeneizacao de embeddings
- Dataset: Cora (PyG)

### Visualization (1 arquivo)

#### 7. visualization/graph_plots.py
- Visualizacao de grafo com node colors por classe/score
- Embeddings de nos em 2D (t-SNE/UMAP)
- Performance vs profundidade (over-smoothing)
- Knowledge graph subgraph visualization
- MRR e Hits@k comparativo entre modelos
- Attention weights do GAT sobre o grafo
- Dataset: Cora (PyG) + resultados dos modelos anteriores

---

## Formato: cada script com docstring, main(), RANDOM_STATE = 42

---

## Criterios de Aceite

- [x] 7 scripts Python criados nas subpastas corretas
- [x] modeling/gcn_node_classification.py — GCN transductive com PyG no Cora
- [x] modeling/graphsage_inductive.py — GraphSAGE com NeighborLoader no Cora
- [x] modeling/knowledge_graph_embeddings.py — TransE/DistMult/ComplEx com PyKEEN
- [x] modeling/node2vec_embeddings.py — Node2Vec com random walks no Cora
- [x] validation/graph_model_eval.py — Link prediction eval com MRR, Hits@k
- [x] validation/over_smoothing_analysis.py — Performance vs depth + MADGap
- [x] visualization/graph_plots.py — Graph viz, t-SNE embeddings, over-smoothing plots
- [x] Todos passam verificacao de sintaxe Python
- [x] Todos tem docstring, funcoes organizadas e main()
- [x] Stack: torch-geometric + pykeen + networkx, Cora (PyG) como dataset principal

---

## Bibliotecas Utilizadas

| Biblioteca | Versao Minima | Uso |
|------------|---------------|-----|
| torch-geometric | >= 2.4 | GCN, GraphSAGE, GAT, datasets, NeighborLoader |
| pykeen | >= 1.10 | TransE, DistMult, ComplEx para KG embeddings |
| networkx | >= 3.1 | Analise classica de grafos, visualizacao |
| node2vec | >= 0.4 | Node embeddings via random walks |
| torch | >= 2.0 | Backend de GNNs |
| scikit-learn | >= 1.3 | Metricas, t-SNE, clustering |
| matplotlib | >= 3.7 | Visualizacoes |
| seaborn | >= 0.12 | Visualizacoes |

---

**End of Specification**

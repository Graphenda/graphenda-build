# Fase F3 — Guias Explicativos

**Status**: COMPLETO
**Dependencias**: F1
**Bloqueia**: F4, F5

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/graph-models/`

---

## Guias a Gerar

### 1. overview.md
- O que sao modelos baseados em grafos e quando usa-los
- Tipos de grafos: homogeneos, heterogeneos, knowledge graphs
- Tarefas: node classification, link prediction, graph classification
- Aplicacoes: redes sociais, fraude, drug discovery, knowledge graphs
- Graph neural networks vs graph embeddings vs metodos classicos

### 2. models.md
- GCN: convolucionais em grafos, message passing
- GraphSAGE: amostragem de vizinhos, inducao para novos nos
- GAT: attention mechanism em grafos
- TransE, DistMult, ComplEx: embeddings de knowledge graphs
- Node2Vec: random walks para node embeddings
- Over-smoothing: problema de profundidade em GNNs
- Transductive vs inductive: diferenca fundamental de settings
- Homofilia vs heterofilia: quando grafos ajudam

### 3. validation.md
- Checklist de validacao para modelos de grafos
- Split correto: transductive vs inductive setting
- Evitar data leakage em link prediction (edges no teste nao podem influenciar treino)
- Analise de over-smoothing: performance vs profundidade
- Sensibilidade ao numero de vizinhos amostrados (GraphSAGE)
- Comparacao com baselines nao-grafos (features tabulares)
- Validacao de knowledge graph embeddings: filtered vs raw ranking
- Robustez a perturbacoes na estrutura do grafo
- Analise de homofilia vs heterofilia do grafo

### 4. metrics.md
- Node classification: accuracy, F1, AUC-ROC
- Link prediction: MRR, Hits@k (1, 3, 10), AUC-ROC
- Graph classification: accuracy, F1
- Knowledge graph: MRR, Hits@1, Hits@10 (filtered setting)
- Embedding quality: clustering coefficient preservation
- Over-smoothing: MADGap (Mean Average Distance Gap)
- Computational: tempo de treino, memoria, escalabilidade

### 5. pitfalls.md
- Data leakage em link prediction (usar edges de teste no grafo de treino)
- Over-smoothing: GCNs profundas perdem informacao discriminativa
- Ignorar baselines sem estrutura de grafo
- Assumir que grafos sempre ajudam (depende da homofilia)
- Nao considerar escalabilidade para grafos grandes
- Knowledge graph embeddings avaliados sem filtered setting
- Ignorar a qualidade e completude do grafo de entrada

---

## Formato: `slug: graph-models-<nome>`, `domain: graph-models`, `type: guide`

Cada guia: minimo 1500 palavras, formulas LaTeX (GCN propagation rule, message passing, TransE scoring, MADGap), referencias da F1.

---

## Criterios de Aceite

- [x] 5 guias criados: overview.md, models.md, validation.md, metrics.md, pitfalls.md
- [x] papers.md da F1 tambem presente
- [x] Todos com frontmatter YAML valido
- [x] Cada guia com minimo de 1500 palavras
- [x] Formulas LaTeX incluidas (GCN propagation, message passing, TransE, MADGap)
- [x] Referencias cruzadas aos papers da F1
- [x] Conteudo baseado em pesquisa web

---

**End of Specification**

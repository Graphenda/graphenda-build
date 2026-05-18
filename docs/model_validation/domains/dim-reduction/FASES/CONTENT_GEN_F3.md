# Fase F3 — Guias Explicativos

**Status**: COMPLETO
**Dependencias**: F1
**Bloqueia**: F4, F5

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/dim-reduction/`

---

## Guias a Gerar

### 1. overview.md
- O que e reducao de dimensionalidade e por que e importante
- Maldicao da dimensionalidade: efeitos em distancias e modelos
- Reducao linear vs nao-linear
- Aplicacoes: visualizacao, pre-processamento, compressao, denoising
- Quando usar reducao vs feature selection

### 2. models.md
- PCA: decomposicao em componentes principais, variancia explicada
- Kernel PCA: extensao nao-linear com kernels (RBF, poly)
- Truncated SVD: para matrizes esparsas (texto, NLP)
- t-SNE: neighbor embedding, perplexity, aplicacao em visualizacao
- UMAP: preserva estrutura global e local, mais rapido que t-SNE
- Isomap: geodesic distances, manifold learning
- Autoencoders: reducao nao-linear via redes neurais
- Factor Analysis: modelo latente com ruido
- ICA: componentes independentes, separacao de sinais

### 3. validation.md
- Variancia explicada acumulada (PCA): scree plot
- Reconstruction error: qualidade da representacao reduzida
- Trustworthiness e continuity (t-SNE, UMAP)
- Preservacao de vizinhancos: k-NN accuracy no espaco reduzido
- Estabilidade de embeddings: sensibilidade a hiperparametros
- Validacao downstream: performance de modelo com features reduzidas
- Comparacao de metodos em mesma tarefa

### 4. metrics.md
- Explained variance ratio (PCA): proporcao e acumulada
- Reconstruction error (MSE entre original e reconstruido)
- Trustworthiness score: vizinhos falsos no embedding
- Continuity score: vizinhos perdidos no embedding
- Silhouette score no espaco reduzido (se ha clusters)
- Downstream task performance: acuracia/RMSE com features reduzidas
- Stress (MDS): distorcao de distancias

### 5. pitfalls.md
- Interpretar eixos de t-SNE/UMAP como significativos (nao sao)
- Nao escalar features antes de PCA
- Escolher numero de componentes arbitrariamente
- Usar t-SNE para mais do que visualizacao
- Interpretar distancias globais em t-SNE (somente locais confiaveis)
- Sensibilidade de t-SNE e UMAP a hiperparametros
- Aplicar PCA a dados com relacoes nao-lineares fortes

---

## Formato: frontmatter com `slug: dim-reduction-<nome>`, `domain: dim-reduction`, `type: guide`

Cada guia: minimo 1500 palavras, formulas LaTeX, tabelas comparativas, referencias da F1.

---

## Criterios de Aceite

- [x] 5 guias criados: overview.md, models.md, validation.md, metrics.md, pitfalls.md
- [x] Alem dos 5 guias, papers.md da F1 tambem presente no diretorio
- [x] Todos com frontmatter YAML valido
- [x] Cada guia com minimo de 1500 palavras
- [x] Formulas LaTeX incluidas onde necessario (PCA eigendecomposition, KL divergence)
- [x] Referencias cruzadas aos papers da F1
- [x] Conteudo baseado em pesquisa web
- [x] Tom tecnico e adequado para profissionais de model validation

---

## Ferramentas Necessarias

- **Read**, **WebSearch**, **WebFetch**, **Write**

---

**End of Specification**

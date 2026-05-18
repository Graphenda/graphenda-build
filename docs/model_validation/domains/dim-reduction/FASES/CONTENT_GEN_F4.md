# Fase F4 — Codigo de Exemplo

**Status**: CONCLUIDO
**Dependencias**: F3
**Bloqueia**: F5

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/dim-reduction/`

---

## Arquivos a Gerar

### Modeling (4 arquivos)

#### 1. modeling/pca_complete.py
- PCA com sklearn: fit, transform, inverse_transform
- Scree plot e variancia explicada acumulada
- Biplot: scores + loadings
- Escolha automatica de numero de componentes (95% variancia)
- Dataset: MNIST digits (sklearn) ou Iris

#### 2. modeling/tsne_umap.py
- t-SNE com sklearn: efeito de perplexity
- UMAP com umap-learn: n_neighbors e min_dist
- Comparacao visual dos dois metodos
- Coloracao por labels para validacao visual
- Dataset: MNIST digits (sklearn)

#### 3. modeling/kernel_pca_isomap.py
- Kernel PCA com kernels RBF e poly
- Isomap para dados com estrutura de manifold
- Comparacao em datasets nao-lineares (Swiss roll)
- Tuning de hiperparametros
- Dataset: Swiss roll (sklearn make_swiss_roll)

#### 4. modeling/autoencoder_reduction.py
- Autoencoder simples com PyTorch ou Keras
- Encoder para reducao, decoder para reconstrucao
- Variational Autoencoder (VAE) basico
- Comparacao com PCA em termos de reconstruction error
- Dataset: MNIST digits

### Validation (2 arquivos)

#### 5. validation/reconstruction_analysis.py
- Reconstruction error por numero de componentes
- Comparacao PCA vs Kernel PCA vs Autoencoder
- Trustworthiness e continuity para t-SNE e UMAP
- Downstream task: classificacao com features reduzidas vs originais
- Dataset: MNIST digits (sklearn)

#### 6. validation/embedding_stability.py
- Sensibilidade de t-SNE a perplexity (grid de valores)
- Sensibilidade de UMAP a n_neighbors e min_dist
- Reproducibilidade: multiplas execucoes com random seeds
- Procrustes analysis para comparacao de embeddings
- Dataset: MNIST digits (sklearn)

### Visualization (1 arquivo)

#### 7. visualization/dim_reduction_plots.py
- Scree plot e variancia acumulada (PCA)
- Biplot com loadings e scores
- t-SNE e UMAP side-by-side coloridos por label
- Swiss roll 3D vs embeddings 2D
- Reconstruction vs original (imagens)
- Grid de t-SNE com diferentes perplexities
- Dataset: MNIST + Swiss roll

---

## Formato: cada script com docstring, main(), RANDOM_STATE = 42

---

## Criterios de Aceite

- [x] 7 scripts Python criados nas subpastas corretas
- [x] modeling/pca_complete.py — PCA com scree plot, biplot, auto-components
- [x] modeling/tsne_umap.py — t-SNE + UMAP com comparacao visual
- [x] modeling/kernel_pca_isomap.py — Kernel PCA + Isomap com Swiss roll
- [x] modeling/autoencoder_reduction.py — AE e VAE com comparacao vs PCA
- [x] validation/reconstruction_analysis.py — Reconstruction error, trustworthiness, downstream
- [x] validation/embedding_stability.py — Sensibilidade a hiperparametros, Procrustes
- [x] visualization/dim_reduction_plots.py — Scree, biplot, t-SNE/UMAP, Swiss roll, reconstruction
- [x] Todos os scripts passam verificacao de sintaxe Python
- [x] Todos os scripts tem docstring, funcoes organizadas e main()
- [x] Codigo usa datasets acessiveis (sklearn digits, make_swiss_roll)

---

## Bibliotecas Utilizadas

| Biblioteca | Versao Minima | Uso |
|------------|---------------|-----|
| numpy | >= 1.24 | Arrays |
| pandas | >= 2.0 | DataFrames |
| scikit-learn | >= 1.3 | PCA, Kernel PCA, t-SNE, Isomap, Truncated SVD, metrics |
| umap-learn | >= 0.5 | UMAP |
| torch | >= 2.0 | Autoencoders (opcional: tensorflow/keras) |
| matplotlib | >= 3.7 | Visualizacoes |
| seaborn | >= 0.12 | Visualizacoes estatisticas |

---

## Ferramentas Necessarias

- **Read**, **WebSearch**, **Write**

---

**End of Specification**

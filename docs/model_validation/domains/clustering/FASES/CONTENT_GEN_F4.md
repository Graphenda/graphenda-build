# Fase F4 — Codigo de Exemplo

**Status**: CONCLUIDO
**Dependencias**: F3 (para contexto dos guias)
**Bloqueia**: F5

---

## Objetivo

Criar exemplos de codigo Python completos e funcionais para modelos de clustering.

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/clustering/`

---

## Arquivos a Gerar

### Modeling (4 arquivos)

#### 1. modeling/kmeans_complete.py
- K-Means com sklearn: inicializacao, convergencia
- K-Means++ e Mini-Batch K-Means
- Elbow method e silhouette para escolha de K
- Analise de centroids e perfil dos clusters
- Dataset: Mall Customers (Kaggle) ou Iris (sklearn)

#### 2. modeling/dbscan_optics.py
- DBSCAN com sklearn: escolha de eps e min_samples
- k-distance plot para determinar eps
- OPTICS com reachability plot
- Comparacao DBSCAN vs OPTICS
- Dataset: sintetico (moons, circles) + Iris

#### 3. modeling/gmm_clustering.py
- Gaussian Mixture Models com sklearn
- Selecao de K via BIC e AIC
- Tipos de covariancia: full, tied, diag, spherical
- Soft clustering: probabilidades de pertencimento
- Dataset: Iris (sklearn) ou Wine

#### 4. modeling/hierarchical_spectral.py
- Agglomerative Clustering com diferentes linkages
- Dendrograma e corte
- Spectral Clustering para clusters nao-convexos
- Comparacao em datasets sinteticos (moons, circles)
- Dataset: sintetico + Wine (sklearn)

### Validation (2 arquivos)

#### 5. validation/cluster_evaluation.py
- Silhouette score global e por cluster
- Davies-Bouldin e Calinski-Harabasz indices
- Gap statistic implementado
- Estabilidade via bootstrap (jaccard similarity entre runs)
- Dataset: Mall Customers ou Iris

#### 6. validation/cluster_profiling.py
- Descricao estatistica de cada cluster (media, mediana, distribuicao)
- Teste de significancia de diferencas entre clusters
- Importancia de features para separacao de clusters
- Cluster size distribution e outlier analysis
- Dataset: Mall Customers ou Wholesale Customers

### Visualization (1 arquivo)

#### 7. visualization/clustering_plots.py
- Scatter 2D com clusters coloridos (PCA se necessario)
- Silhouette plot por cluster
- Elbow plot com inertia
- Dendrograma para hierarchical clustering
- Radar chart / spider plot por cluster
- Heatmap de centroids
- Dataset: Mall Customers + sinteticos

---

## Formato de Cada Script

```python
"""
<Titulo do Script>
==================

<Descricao breve — 2-3 linhas>

Domain: Clustering Models
Category: <modeling|validation|visualization>
Dependencies: <lista de pacotes>

Usage:
    python <nome_do_script>.py
"""

# --- Imports ---
import numpy as np
import pandas as pd

# --- Configuration ---
RANDOM_STATE = 42

# --- Functions ---
def main():
    """Main execution."""
    pass

if __name__ == "__main__":
    main()
```

---

## Etapas de Implementacao

### Etapa 1: Ler guias da F3 e spec do dominio
### Etapa 2: Pesquisar APIs (sklearn cluster, hdbscan, yellowbrick)
### Etapa 3: Desenvolver os 7 scripts
### Etapa 4: Verificacao

```bash
find /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/clustering/ -name "*.py" | sort

for f in $(find /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/clustering/ -name "*.py"); do
    echo "=== $(basename $f) ==="
    python3 -c "import ast; ast.parse(open('$f').read()); print('Syntax OK')"
done
```

---

## Criterios de Aceite

- [x] 7 scripts Python criados nas subpastas corretas
- [x] modeling/kmeans_complete.py — K-Means com elbow, silhouette e centroid profiling
- [x] modeling/dbscan_optics.py — DBSCAN + OPTICS com k-distance e reachability
- [x] modeling/gmm_clustering.py — GMM com BIC/AIC e soft clustering
- [x] modeling/hierarchical_spectral.py — Agglomerative + Spectral com dendrograma
- [x] validation/cluster_evaluation.py — Silhouette, DB, CH, gap statistic, estabilidade
- [x] validation/cluster_profiling.py — Descricao estatistica, testes, feature importance
- [x] visualization/clustering_plots.py — Scatter, silhouette plot, elbow, dendrograma, radar, heatmap
- [x] Todos os scripts passam verificacao de sintaxe Python
- [x] Todos os scripts tem docstring, funcoes organizadas e main()
- [x] Codigo usa datasets acessiveis (sklearn, sinteticos ou CSV simples)

---

## Bibliotecas Utilizadas

| Biblioteca | Versao Minima | Uso |
|------------|---------------|-----|
| numpy | >= 1.24 | Arrays e operacoes numericas |
| pandas | >= 2.0 | DataFrames |
| scikit-learn | >= 1.3 | K-Means, DBSCAN, GMM, Agglomerative, Spectral, metricas |
| scipy | >= 1.11 | Hierarchical clustering, dendrogramas |
| matplotlib | >= 3.7 | Visualizacoes |
| seaborn | >= 0.12 | Visualizacoes estatisticas |

---

## Ferramentas Necessarias

- **Read**, **WebSearch**, **Write**

---

**End of Specification**

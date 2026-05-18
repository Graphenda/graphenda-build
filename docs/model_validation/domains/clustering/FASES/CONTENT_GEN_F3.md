# Fase F3 — Guias Explicativos

**Status**: PENDENTE
**Dependencias**: F1 (para referencias dos papers)
**Bloqueia**: F4, F5

---

## Objetivo

Criar 5 guias explicativos completos sobre modelos de clustering.

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/clustering/`

---

## Guias a Gerar

### 1. overview.md — Visao Geral de Clustering

**Conteudo obrigatorio:**
- O que e clustering e aprendizado nao supervisionado
- Tipos de clustering: particional, hierarquico, baseado em densidade, probabilistico
- Aplicacoes: segmentacao de clientes, anomaly detection, agrupamento de documentos
- Desafios: escolha do numero de clusters, validacao sem ground truth
- Quando usar clustering vs classificacao semi-supervisionada

**Pesquisa web:** buscar aplicacoes recentes em bancos, marketing, risk segmentation

### 2. models.md — Tipos de Modelos de Clustering

**Conteudo obrigatorio:**
- K-Means: algoritmo de Lloyd, inicializacao K-Means++, Mini-Batch K-Means
- K-Medoids (PAM): robusto a outliers
- DBSCAN: density-based, eps e min_samples, pontos de ruido
- OPTICS: extensao hierarquica do DBSCAN
- Gaussian Mixture Models (GMM): soft clustering, EM algorithm
- Hierarchical Clustering: aglomerativo (linkage: single, complete, Ward), dendrograma
- Mean Shift: kernel-based, sem necessidade de K
- Spectral Clustering: baseado em grafos, para clusters nao-convexos

**Pesquisa web:** buscar comparacoes praticas, quando usar cada algoritmo

### 3. validation.md — Validacao de Clustering

**Conteudo obrigatorio:**
- Silhouette score: interpretacao e por cluster
- Elbow method: inertia vs numero de clusters
- Gap statistic: comparacao com distribuicao de referencia
- Davies-Bouldin index: razao de dispersao
- Calinski-Harabasz index: razao de variancia entre/dentro
- Estabilidade de clusters: bootstrap e perturbacao
- Validacao externa (quando ha labels): ARI, NMI, V-measure
- Profiling de clusters: descricao estatistica de cada grupo

**Pesquisa web:** buscar melhores praticas de validacao, gap statistic implementacao

### 4. metrics.md — Metricas de Clustering

**Conteudo obrigatorio:**
- Silhouette score: [-1, 1], interpretacao
- Inertia (within-cluster sum of squares)
- Davies-Bouldin index: quanto menor, melhor
- Calinski-Harabasz: quanto maior, melhor
- Adjusted Rand Index (ARI): comparacao com ground truth
- Normalized Mutual Information (NMI)
- BIC para GMM: selecao de K e tipo de covariancia
- Dunn index: razao de distancias inter/intra-cluster

**Pesquisa web:** buscar guias de interpretacao, comparacao de metricas internas vs externas

### 5. pitfalls.md — Armadilhas e Erros Comuns

**Conteudo obrigatorio:**
- Escolher K arbitrariamente sem criterio
- Nao escalar features antes do clustering
- K-Means com clusters nao-esfericos ou de tamanhos diferentes
- Interpretar clusters como verdades absolutas
- Ignorar outliers que distorcem centroids
- Nao validar estabilidade dos clusters
- Usar metricas internas sem considerar o proposito do negocio

**Pesquisa web:** buscar case studies de falhas em segmentacao

---

## Formato de Cada Guia

```markdown
---
slug: clustering-<nome>
name: "<Titulo do Guia>"
domain: clustering
type: guide
difficulty: intermediate
status: draft
tags: [clustering, <tags-especificas>]
references:
  - title: "<titulo>"
    authors: "<autores>"
    year: <ano>
    type: paper
---
```

Cada guia: minimo 1500 palavras, formulas LaTeX, tabelas comparativas, referencias da F1.

---

## Etapas de Implementacao

### Etapa 1: Ler papers.md (F1) e spec do dominio
### Etapa 2: Pesquisa complementar na web
### Etapa 3: Redacao dos 5 guias
### Etapa 4: Verificacao

```bash
ls -la /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/clustering/
wc -l /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/clustering/*.md
```

---

## Criterios de Aceite

- [x] 5 guias criados: overview.md, models.md, validation.md, metrics.md, pitfalls.md
- [x] Alem dos 5 guias, papers.md da F1 tambem presente no diretorio
- [x] Todos com frontmatter YAML valido (slug, name, domain, type, difficulty, status, tags)
- [x] Cada guia com minimo de 1500 palavras
- [x] Formulas LaTeX incluidas onde necessario (silhouette, inertia, BIC)
- [x] Referencias cruzadas aos papers da F1
- [x] Conteudo baseado em pesquisa web
- [x] Tom tecnico e adequado para profissionais de model validation

---

## Ferramentas Necessarias

- **Read**, **WebSearch**, **WebFetch**, **Write**

---

**End of Specification**

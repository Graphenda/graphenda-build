# Fase F3 — Guias Explicativos

**Status**: PENDENTE
**Dependencias**: F1 (para referencias dos papers)
**Bloqueia**: F4, F5

---

## Objetivo

Criar 5 guias explicativos completos sobre metodos ensemble.

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/ensemble/`

---

## Guias a Gerar

### 1. overview.md — Visao Geral de Metodos Ensemble

**Conteudo obrigatorio:**
- O que sao metodos ensemble e por que funcionam
- Bias-variance tradeoff e como ensembles ajudam
- Categorias: bagging, boosting, stacking, voting
- Condicao de diversidade: por que modelos devem ser diferentes
- Teorema de Condorcet e sabedoria das multidoes
- Quando ensembles valem a complexidade adicional

**Pesquisa web:** buscar aplicacoes recentes, competicoes Kaggle, uso em bancos

### 2. models.md — Tipos de Metodos Ensemble

**Conteudo obrigatorio:**
- Bagging: bootstrap aggregating, reducao de variancia
- Random Forest: bagging + random subspace
- AdaBoost: boosting adaptativo, peso de amostras
- Gradient Boosting: otimizacao funcional via gradiente
- XGBoost, LightGBM, CatBoost: implementacoes modernas
- Stacking: meta-learner sobre base learners
- Voting: hard voting vs soft voting (media ponderada)
- Blending: stacking simplificado com holdout

**Pesquisa web:** buscar comparacoes, evolucao historica dos metodos

### 3. validation.md — Validacao de Ensembles

**Conteudo obrigatorio:**
- OOB error para modelos baseados em bagging
- Diversidade do ensemble: Q-statistic, correlation, kappa
- Contribuicao marginal de cada modelo base
- Cross-validation para ensembles (cuidados com data leakage no stacking)
- Curvas de learning: performance vs numero de estimadores
- Comparacao ensemble vs melhor modelo individual
- Ablation study: remover componentes e medir impacto

**Pesquisa web:** buscar melhores praticas, armadilhas de validacao em stacking

### 4. metrics.md — Metricas para Ensembles

**Conteudo obrigatorio:**
- OOB score: estimativa sem necessidade de holdout
- Metricas de diversidade: disagreement measure, Q-statistic
- Melhoria relativa sobre melhor modelo base
- Log-loss e Brier Score para ensembles probabilisticos
- Metricas especificas do problema (AUC, RMSE, etc.)
- Custo computacional: tempo de treino e inferencia

**Pesquisa web:** buscar metricas de diversidade, literatura sobre ensemble selection

### 5. pitfalls.md — Armadilhas e Erros Comuns

**Conteudo obrigatorio:**
- Stacking com data leakage (treinar meta-learner nos mesmos dados)
- Ensemble de modelos correlacionados (sem diversidade)
- Overfitting por excesso de complexidade no stacking
- Custo computacional nao justificado pelo ganho
- Dificuldade de interpretacao e explicabilidade
- Nao usar OOB quando disponivel (bagging)
- Blending com holdout pequeno: estimativa instavel

**Pesquisa web:** buscar case studies de falhas, exemplos de over-engineering

---

## Formato de Cada Guia

```markdown
---
slug: ensemble-<nome>
name: "<Titulo do Guia>"
domain: ensemble
type: guide
difficulty: intermediate
status: draft
tags: [ensemble, <tags-especificas>]
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
ls -la /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/ensemble/
wc -l /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/ensemble/*.md
```

---

## Criterios de Aceite

- [x] 5 guias criados: overview.md, models.md, validation.md, metrics.md, pitfalls.md
- [x] Alem dos 5 guias, papers.md da F1 tambem presente no diretorio
- [x] Todos com frontmatter YAML valido (slug, name, domain, type, difficulty, status, tags)
- [x] Cada guia com minimo de 1500 palavras
- [x] Formulas LaTeX incluidas onde necessario (bias-variance decomposition, bagging formula)
- [x] Referencias cruzadas aos papers da F1
- [x] Conteudo baseado em pesquisa web
- [x] Tom tecnico e adequado para profissionais de model validation

---

## Ferramentas Necessarias

- **Read**, **WebSearch**, **WebFetch**, **Write**

---

**End of Specification**

# Fase F3 — Guias Explicativos

**Status**: CONCLUIDO
**Dependencias**: F1
**Bloqueia**: F4, F5

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/deep-learning-tabular/`

---

## Guias a Gerar

### 1. overview.md
- O que e deep learning para dados tabulares e por que e desafiador
- Panorama: MLP, TabNet, FT-Transformer, NODE, SAINT
- Quando DL supera arvores (muitos dados, features de alta cardinalidade)
- Quando arvores ainda vencem (poucos dados, features numericas simples)
- Trade-off entre interpretabilidade, custo computacional e performance

### 2. models.md
- MLP classico: arquitetura, batch normalization, dropout
- TabNet: sparse attention, feature selection interpretavel
- FT-Transformer: tokenizacao de features + self-attention
- NODE: arvores diferenciaveis com gradient descent
- SAINT: inter-sample attention e pre-treino contrastivo
- Entity embeddings para variaveis categoricas
- Comparacao de arquiteturas: complexidade, tempo, performance

### 3. validation.md
- Checklist de validacao para redes neurais em dados tabulares
- Comparacao obrigatoria com baseline de arvores (XGBoost/LightGBM)
- Validacao de convergencia: learning curves, early stopping
- Sensibilidade a hiperparametros (lr, profundidade, dropout)
- Reproducibilidade: seeds, inicializacao, variancia entre runs
- Feature importance via attention weights vs SHAP
- Validacao out-of-time e out-of-distribution

### 4. metrics.md
- Metricas de regressao: RMSE, MAE, R² vs baselines
- Metricas de classificacao: AUC-ROC, log-loss, F1
- Comparacao estatistica: teste de Wilcoxon entre modelos
- Tempo de inferencia e custo computacional como metrica
- Calibracao de probabilidades (reliability diagram)
- Feature importance stability

### 5. pitfalls.md
- Usar DL quando arvores bastam (overengineering)
- Nao comparar com baselines simples
- Tuning insuficiente de hiperparametros
- Ignorar variancia entre runs
- Confiar em attention weights como explicacao causal
- Dados insuficientes para a complexidade do modelo
- Nao normalizar features numericas adequadamente

---

## Formato: frontmatter com `slug: deep-learning-tabular-<nome>`, `domain: deep-learning-tabular`, `type: guide`

Cada guia: minimo 1500 palavras, formulas LaTeX, tabelas comparativas, referencias da F1.

---

## Criterios de Aceite

- [x] 5 guias criados: overview.md, models.md, validation.md, metrics.md, pitfalls.md
- [x] Alem dos 5 guias, papers.md da F1 tambem presente no diretorio
- [x] Todos com frontmatter YAML valido
- [x] Cada guia com minimo de 1500 palavras
- [x] Formulas LaTeX incluidas (attention, cross-entropy, entity embeddings)
- [x] Referencias cruzadas aos papers da F1
- [x] Conteudo baseado em pesquisa web
- [x] Tom tecnico e adequado para profissionais de model validation

---

## Ferramentas Necessarias

- **Read**, **WebSearch**, **WebFetch**, **Write**

---

**End of Specification**

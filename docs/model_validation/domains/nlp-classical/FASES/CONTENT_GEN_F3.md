# Fase F3 — Guias Explicativos

**Status**: CONCLUIDO
**Dependencias**: F1
**Bloqueia**: F4, F5

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/nlp-classical/`

---

## Guias a Gerar

### 1. overview.md
- NLP classico e por que ainda e relevante
- Pipeline: preprocessing -> representacao -> modelo
- Tarefas: classificacao, NER, topic modeling, sentimento
- Quando NLP classico vs embeddings/LLMs
- Vantagens: interpretabilidade, baixo custo, poucos dados

### 2. models.md
- Bag of Words e TF-IDF: representacao vetorial
- Naive Bayes para classificacao de texto
- SVM com kernels para classificacao
- LDA e NMF para topic modeling
- CRF e HMM para NER e POS tagging
- Regex e regras para extracao de informacao
- Ensemble de modelos classicos

### 3. validation.md
- Checklist de validacao para NLP classico
- Validacao de preprocessing: impacto de stopwords, stemming, lematizacao
- Stratified CV para classes desbalanceadas
- Topic coherence (UMass, CV, NPMI)
- Metricas de NER: exact match vs partial match
- Robustez a variacoes linguisticas
- Analise de erros por categoria/classe

### 4. metrics.md
- Accuracy, Precision, Recall, F1
- Macro vs Micro vs Weighted averaging
- Cohen's Kappa
- Perplexity para modelos de linguagem
- Topic Coherence (CV, UMass, NPMI)
- Entity-level vs Token-level F1 para NER
- Confusion matrix e analise de erros

### 5. pitfalls.md
- Preprocessing inconsistente entre treino e producao
- Vocabulario fixo e OOV
- LDA com K arbitrario
- Ignorar desbalanceamento de classes
- Avaliar NER apenas com token-level metrics
- TF-IDF sensivel ao tamanho do corpus
- Nao considerar variacoes linguisticas

---

## Formato: frontmatter com `slug: nlp-classical-<nome>`, `domain: nlp-classical`, `type: guide`

Cada guia: minimo 1500 palavras, formulas LaTeX (TF-IDF, LDA generative process), tabelas, referencias da F1.

---

## Criterios de Aceite

- [x] 5 guias criados: overview.md, models.md, validation.md, metrics.md, pitfalls.md
- [x] Alem dos 5 guias, papers.md da F1 tambem presente
- [x] Todos com frontmatter YAML valido
- [x] Cada guia com minimo de 1500 palavras
- [x] Formulas LaTeX incluidas (TF-IDF formula, LDA plate notation, Bayes for NB)
- [x] Referencias cruzadas aos papers da F1
- [x] Conteudo baseado em pesquisa web
- [x] Tom tecnico para profissionais de model validation

---

## Ferramentas Necessarias

- **Read**, **WebSearch**, **WebFetch**, **Write**

---

**End of Specification**

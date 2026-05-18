# Fase F3 — Guias Explicativos

**Status**: COMPLETO
**Dependencias**: F1
**Bloqueia**: F4, F5

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/nlp-embeddings/`

---

## Guias a Gerar

### 1. overview.md
- Embeddings e por que revolucionaram NLP
- Evolucao: one-hot -> Word2Vec -> GloVe -> ELMo -> BERT
- Embeddings estaticos vs contextuais
- Transfer learning em NLP: pre-treino + fine-tuning
- Aplicacoes: classificacao, similaridade, busca semantica, clustering

### 2. models.md
- Word2Vec: CBOW e Skip-gram, negative sampling
- GloVe: co-ocorrencia global
- FastText: subword embeddings
- ELMo: contextuais com BiLSTM
- BERT: MLM e NSP, pre-treino bidirecional
- RoBERTa: otimizacoes
- Sentence-BERT: siamese networks
- BERTimbau: BERT para PT-BR
- Fine-tuning: feature extraction vs full

### 3. validation.md
- Checklist para modelos baseados em embeddings
- Avaliacao intrinseca: analogias, similaridade (Spearman)
- Avaliacao extrinseca: performance downstream
- Deteccao e mitigacao de bias
- Validacao de fine-tuning: overfitting, catastrophic forgetting
- Analise de embeddings: clustering, vizinhanca, probing tasks
- Comparacao com baselines (TF-IDF + SVM)
- Robustez a perturbacoes textuais

### 4. metrics.md
- Cosine similarity
- Spearman correlation para similaridade
- Metricas de classificacao: accuracy, F1, AUC-ROC
- WEAT/SEAT scores para bias
- Silhouette score para clusters de embeddings
- Probing task accuracy
- Retrieval metrics (MRR, Recall@k)

### 5. pitfalls.md
- Embeddings de dominio diferente sem fine-tuning
- Ignorar bias social
- Truncar textos longos sem estrategia
- Nao avaliar intrinsecamente antes de usar
- Fine-tuning com poucos dados = overfitting
- Catastrophic forgetting
- BERT nem sempre melhor que TF-IDF

---

## Formato: `slug: nlp-embeddings-<nome>`, `domain: nlp-embeddings`, `type: guide`

Cada guia: minimo 1500 palavras, formulas LaTeX (cosine sim, Word2Vec objective, BERT MLM), referencias da F1.

---

## Criterios de Aceite

- [x] 5 guias criados: overview.md, models.md, validation.md, metrics.md, pitfalls.md
- [x] papers.md da F1 tambem presente
- [x] Todos com frontmatter YAML valido
- [x] Cada guia com minimo de 1500 palavras
- [x] Formulas LaTeX incluidas
- [x] Referencias cruzadas aos papers da F1
- [x] Conteudo baseado em pesquisa web

---

**End of Specification**

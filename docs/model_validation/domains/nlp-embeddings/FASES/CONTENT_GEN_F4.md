# Fase F4 — Codigo de Exemplo

**Status**: CONCLUIDO
**Dependencias**: F3
**Bloqueia**: F5

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/nlp-embeddings/`

---

## Arquivos a Gerar

### Modeling (4 arquivos)

#### 1. modeling/word2vec_training.py
- Word2Vec com gensim em corpus customizado
- CBOW vs Skip-gram
- t-SNE de embeddings
- Analogias e similaridade
- Dataset: 20 Newsgroups (sklearn) ou sintetico

#### 2. modeling/bert_finetuning.py
- Fine-tuning de BERT para classificacao com HuggingFace
- Tokenizacao, lr scheduling (warmup + decay)
- Early stopping em validation set
- Comparacao com frozen BERT (feature extraction)
- Dataset: AG News ou IMDb subset

#### 3. modeling/sentence_embeddings.py
- Sentence embeddings com Sentence-BERT
- Busca semantica com FAISS
- Clustering de documentos por similaridade
- Comparacao de modelos de sentence embeddings
- Dataset: STS Benchmark ou sintetico

#### 4. modeling/bertimbau_portuguese.py
- BERTimbau para tarefas em portugues
- Fine-tuning para classificacao de sentimento PT-BR
- Comparacao com multilingual BERT
- Analise de performance por tipo de texto
- Dataset: TweetSentBR ou sintetico PT-BR

### Validation (2 arquivos)

#### 5. validation/bias_detection.py
- Deteccao de bias em Word2Vec e BERT
- WEAT test para bias de genero e raca
- Visualizacao de direcoes de bias
- Tecnicas de debiasing (hard e soft)
- Dataset: embeddings treinados na F4.1

#### 6. validation/embedding_quality.py
- Avaliacao intrinseca: analogias, similaridade
- Probing tasks para informacao linguistica
- Comparacao pre-treinados vs fine-tuned
- Estabilidade entre runs
- Dataset: Google Analogies, SimLex-999

### Visualization (1 arquivo)

#### 7. visualization/embedding_plots.py
- t-SNE e UMAP de word embeddings
- Heatmap de similaridade entre sentencas
- Bias direction visualization
- Attention heatmaps do BERT
- Curva de aprendizado do fine-tuning
- Clustering de documentos em 2D

---

## Formato: cada script com docstring, main(), RANDOM_STATE = 42

---

## Criterios de Aceite

- [x] 7 scripts Python criados nas subpastas corretas
- [x] modeling/word2vec_training.py — Word2Vec CBOW/Skip-gram com t-SNE
- [x] modeling/bert_finetuning.py — BERT fine-tuning com HuggingFace
- [x] modeling/sentence_embeddings.py — Sentence-BERT + FAISS busca semantica
- [x] modeling/bertimbau_portuguese.py — BERTimbau PT-BR sentiment
- [x] validation/bias_detection.py — WEAT test e debiasing
- [x] validation/embedding_quality.py — Intrinsic eval, probing, stability
- [x] visualization/embedding_plots.py — t-SNE, similarity heatmap, attention, bias
- [x] Todos passam verificacao de sintaxe Python
- [x] Todos tem docstring, funcoes organizadas e main()
- [x] Stack: transformers + sentence-transformers + gensim

---

## Bibliotecas Utilizadas

| Biblioteca | Versao Minima | Uso |
|------------|---------------|-----|
| transformers | >= 4.30 | BERT, RoBERTa, BERTimbau |
| sentence-transformers | >= 2.2 | Sentence-BERT |
| gensim | >= 4.3 | Word2Vec, GloVe |
| faiss-cpu | >= 1.7 | Busca semantica |
| umap-learn | >= 0.5 | Visualizacao |
| scikit-learn | >= 1.3 | t-SNE, metricas |
| matplotlib | >= 3.7 | Visualizacoes |
| seaborn | >= 0.12 | Visualizacoes |

---

**End of Specification**

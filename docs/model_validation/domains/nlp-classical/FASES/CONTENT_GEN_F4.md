# Fase F4 — Codigo de Exemplo

**Status**: CONCLUIDA
**Dependencias**: F3
**Bloqueia**: F5

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/nlp-classical/`

---

## Arquivos a Gerar

### Modeling (4 arquivos)

#### 1. modeling/tfidf_classification.py
- Pipeline: TF-IDF + SVM com sklearn
- Preprocessing: tokenizacao, stopwords, stemming
- Grid search (n-grams, max_features, C)
- Classification report e confusion matrix
- Dataset: 20 Newsgroups (sklearn)

#### 2. modeling/topic_modeling_lda.py
- LDA com gensim
- Preprocessing: tokenizacao, bigrams, lematizacao
- Selecao de K via coherence score
- Visualizacao com pyLDAvis
- Dataset: 20 Newsgroups (sklearn)

#### 3. modeling/ner_crf.py
- NER com CRF usando sklearn-crfsuite
- Feature engineering (POS tags, prefixos, sufixos)
- Treino e avaliacao com CoNLL format
- Analise de erros por tipo de entidade
- Dataset: CoNLL-2003 subset ou sintetico

#### 4. modeling/sentiment_analysis.py
- Sentimento com Naive Bayes e SVM
- Preprocessing especifico (negacoes, emoticons)
- Comparacao BoW vs TF-IDF vs n-grams
- Features mais discriminativas
- Dataset: IMDb Reviews subset ou sintetico

### Validation (2 arquivos)

#### 5. validation/text_classification_eval.py
- Cross-validation estratificada para texto
- Learning curve (performance vs tamanho do treino)
- Analise de erros: textos mal classificados
- Impacto de diferentes preprocessamentos
- Dataset: 20 Newsgroups (sklearn)

#### 6. validation/topic_coherence_eval.py
- Coherence para diferentes K
- Comparacao LDA vs NMF
- Estabilidade de topicos entre runs
- Validacao humana vs automatica
- Dataset: 20 Newsgroups (sklearn)

### Visualization (1 arquivo)

#### 7. visualization/nlp_classical_plots.py
- Word clouds por classe/topico
- Confusion matrix heatmap
- Topic coherence vs K
- Distribuicao de comprimento de documentos
- Feature importance (top TF-IDF terms por classe)
- Dataset: modelos anteriores

---

## Formato: cada script com docstring, main(), RANDOM_STATE = 42

---

## Criterios de Aceite

- [x] 7 scripts Python criados nas subpastas corretas
- [x] modeling/tfidf_classification.py — TF-IDF + SVM pipeline completo
- [x] modeling/topic_modeling_lda.py — LDA com gensim e coherence
- [x] modeling/ner_crf.py — CRF com feature engineering para NER
- [x] modeling/sentiment_analysis.py — NB + SVM com comparacao de representacoes
- [x] validation/text_classification_eval.py — CV, learning curve, error analysis
- [x] validation/topic_coherence_eval.py — Coherence, LDA vs NMF, stability
- [x] visualization/nlp_classical_plots.py — Word clouds, confusion, coherence plot
- [x] Todos os scripts passam verificacao de sintaxe Python
- [x] Todos os scripts tem docstring, funcoes organizadas e main()
- [x] Codigo usa sklearn + gensim + nltk como stack principal

---

## Bibliotecas Utilizadas

| Biblioteca | Versao Minima | Uso |
|------------|---------------|-----|
| scikit-learn | >= 1.3 | TF-IDF, NB, SVM, metricas, CV |
| gensim | >= 4.3 | LDA, NMF, coherence |
| nltk | >= 3.8 | Tokenizacao, stopwords, stemming |
| sklearn-crfsuite | >= 0.3 | CRF para NER |
| matplotlib | >= 3.7 | Visualizacoes |
| seaborn | >= 0.12 | Visualizacoes |
| wordcloud | >= 1.9 | Word clouds |

---

## Ferramentas Necessarias

- **Read**, **WebSearch**, **Write**

---

**End of Specification**

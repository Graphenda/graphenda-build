# Model Validation — Domains (Level 3)

## Visao Geral

Este documento mapeia todos os dominios de modelos que existem na ontologia
`model_validation`. Cada dominio e um **Level 3 (Domain)** na hierarquia
cognitiva, agrupando conceitos (L2) e entidades concretas (L1) relacionados
a um tipo especifico de modelagem.

```
L4 — Knowledge Systems (auto-gerado via clustering)
 |
L3 — Domains (ESTE DOCUMENTO)
 |    Os tipos de modelo que existem no mercado
 |
L2 — Concepts (conceitos de validacao compartilhados)
 |    Overfitting, Bias, Calibration, etc.
 |
L1 — Facts (metricas, testes, tecnicas especificas)
     R², AUC-ROC, Perplexity, Hausman Test, etc.
```

---

## Indice de Dominios

| # | Domain | Slug | Area | Regulacao Tipica |
|---|--------|------|------|------------------|
| 1 | Linear Regression Models | `linear_regression` | Estatistica classica | SR 11-7, Basel |
| 2 | Panel Data Models | `panel_data` | Econometria | SR 11-7, Basel |
| 3 | Time Series Models | `time_series` | Econometria / Forecasting | Basel, IFRS 9 |
| 4 | Generalized Linear Models | `glm` | Estatistica | SR 11-7 |
| 5 | Survival / Duration Models | `survival` | Atuaria / Credito | Solvency II, IFRS 17 |
| 6 | Classification Models | `classification` | Machine Learning | EU AI Act, SR 11-7 |
| 7 | Regression ML Models | `regression_ml` | Machine Learning | SR 11-7 |
| 8 | Ensemble Models | `ensemble` | Machine Learning | EU AI Act |
| 9 | Clustering Models | `clustering` | Unsupervised ML | Menor regulacao |
| 10 | Dimensionality Reduction | `dim_reduction` | Feature Engineering | Menor regulacao |
| 11 | Bayesian Models | `bayesian` | Estatistica / ML | Variavel |
| 12 | Reinforcement Learning | `reinforcement_learning` | RL / Decisao | EU AI Act |
| 13 | Deep Learning — Vision | `deep_learning_vision` | Computer Vision | EU AI Act (alto risco) |
| 14 | Deep Learning — Tabular | `deep_learning_tabular` | Neural Nets para dados estruturados | SR 11-7 |
| 15 | Deep Learning — Sequential | `deep_learning_sequential` | RNNs, LSTMs, Transformers | Variavel |
| 16 | NLP — Classical | `nlp_classical` | Text Mining / NLP tradicional | Variavel |
| 17 | NLP — Embeddings | `nlp_embeddings` | Representacao vetorial de texto | Variavel |
| 18 | Large Language Models | `llm` | Foundation Models / GenAI | EU AI Act, NIST AI RMF |
| 19 | Generative Models | `generative` | GANs, VAEs, Diffusion | EU AI Act |
| 20 | Recommender Systems | `recommender` | Sistemas de recomendacao | DSA (EU), FTC |
| 21 | Anomaly Detection | `anomaly_detection` | Fraude / Seguranca | PCI-DSS, AML |
| 22 | Causal Inference Models | `causal_inference` | Econometria / Epidemiologia | Variavel |
| 23 | Graph-based Models | `graph_models` | GNNs, Knowledge Graphs | Menor regulacao |
| 24 | Optimization Models | `optimization` | Pesquisa Operacional | Setor-especifico |
| 25 | Simulation Models | `simulation` | Monte Carlo / ABM | Basel (stress testing) |

---

## Detalhamento por Dominio

### 1. Linear Regression Models

**Descricao:** Modelos lineares classicos onde a variavel resposta e funcao
linear dos preditores. Base de toda a modelagem estatistica.

**Subtipos:**
- Ordinary Least Squares (OLS)
- Weighted Least Squares (WLS)
- Generalized Least Squares (GLS)
- Ridge Regression (L2 regularization)
- Lasso Regression (L1 regularization)
- Elastic Net
- Robust Regression (M-estimators, LTS)

**Conceitos de validacao relevantes (L2):**
- Overfitting, Underfitting
- Heteroscedasticity
- Multicollinearity
- Autocorrelation
- Normality of Residuals
- Linearity
- Feature Importance

**Metricas e testes tipicos (L1):**
- R², Adjusted R²
- RMSE, MAE, MAPE
- F-test
- t-test (coeficientes)
- Durbin-Watson test
- Breusch-Pagan test
- VIF (Variance Inflation Factor)
- Cook's Distance
- Residual plots

**Regulacao:** SR 11-7 (banking), Basel III/IV (capital models)

---

### 2. Panel Data Models

**Descricao:** Modelos para dados longitudinais (entidades observadas ao longo
do tempo). Combinam dimensao cross-sectional e temporal.

**Subtipos:**
- Fixed Effects (FE)
- Random Effects (RE)
- Pooled OLS
- Between Effects
- First Differences
- Arellano-Bond (dynamic GMM)
- Blundell-Bond (system GMM)
- Hausman-Taylor
- Correlated Random Effects

**Conceitos de validacao relevantes (L2):**
- Endogeneity
- Heteroscedasticity
- Autocorrelation
- Unobserved Heterogeneity
- Model Selection
- Instrument Validity
- Stationarity

**Metricas e testes tipicos (L1):**
- Hausman Test (FE vs RE)
- Breusch-Pagan LM Test
- Wooldridge Test (serial correlation)
- Pesaran CD Test (cross-sectional dependence)
- Hansen J Test (overidentification)
- Arellano-Bond AR(1)/AR(2) tests
- Sargan Test
- Im-Pesaran-Shin unit root test
- Within R²

**Regulacao:** SR 11-7, Basel (PD/LGD models), IFRS 9

---

### 3. Time Series Models

**Descricao:** Modelos para dados ordenados no tempo. Capturam tendencias,
sazonalidade, ciclos e dependencias temporais.

**Subtipos:**
- ARIMA / SARIMA
- Exponential Smoothing (ETS)
- VAR / VECM (multivariate)
- GARCH / EGARCH (volatility)
- State Space Models
- Prophet
- Theta Method
- Dynamic Factor Models
- Structural Break Models

**Conceitos de validacao relevantes (L2):**
- Stationarity
- Autocorrelation
- Seasonality
- Model Selection
- Forecast Accuracy
- Overfitting
- Structural Stability

**Metricas e testes tipicos (L1):**
- ADF Test (Augmented Dickey-Fuller)
- KPSS Test
- Phillips-Perron Test
- Ljung-Box Test
- AIC / BIC / HQIC
- RMSE, MAE, MAPE
- Diebold-Mariano Test
- CUSUM Test
- Johansen Cointegration Test
- Engle-Granger Test
- ARCH-LM Test

**Regulacao:** Basel (market risk, VaR), IFRS 9 (ECL), Solvency II

---

### 4. Generalized Linear Models (GLM)

**Descricao:** Extensao dos modelos lineares para distribuicoes nao-normais
da variavel resposta (Binomial, Poisson, Gamma, etc.) via funcao de ligacao.

**Subtipos:**
- Logistic Regression (Binomial)
- Probit Regression
- Poisson Regression
- Negative Binomial Regression
- Gamma Regression
- Tweedie Regression
- Quasi-likelihood Models
- Zero-inflated Models
- Ordinal Regression
- Multinomial Logistic Regression

**Conceitos de validacao relevantes (L2):**
- Calibration
- Discrimination
- Overfitting
- Goodness of Fit
- Dispersion
- Link Function Adequacy
- Bias

**Metricas e testes tipicos (L1):**
- Deviance / Residual Deviance
- AIC / BIC
- Hosmer-Lemeshow Test
- Pearson Chi-squared
- Log-likelihood
- Pseudo R² (McFadden, Cox-Snell, Nagelkerke)
- Calibration Plot
- Confusion Matrix (para classificacao)

**Regulacao:** SR 11-7 (PD models), Solvency II (claims models)

---

### 5. Survival / Duration Models

**Descricao:** Modelos para tempo ate um evento (morte, default, churn, falha).
Lidam com censura (observacoes incompletas).

**Subtipos:**
- Kaplan-Meier Estimator
- Cox Proportional Hazards
- Accelerated Failure Time (AFT)
- Competing Risks Models
- Frailty Models
- Cure Rate Models
- Discrete-time Hazard Models
- Multi-state Models

**Conceitos de validacao relevantes (L2):**
- Proportional Hazards Assumption
- Calibration
- Discrimination
- Censoring Bias
- Model Stability
- Time-varying Effects

**Metricas e testes tipicos (L1):**
- C-statistic (Harrell's C)
- Brier Score
- Log-rank Test
- Schoenfeld Residuals Test
- Groennesby-Borgan Test
- Calibration-in-the-large
- Nelson-Aalen Estimator
- Royston-Parmar D statistic
- Greenwood's Formula

**Regulacao:** Solvency II, IFRS 17 (insurance), IFRS 9 (lifetime PD)

---

### 6. Classification Models

**Descricao:** Modelos de machine learning supervisionado que predizem classes
discretas. Inclui desde logistica ate boosting.

**Subtipos:**
- Logistic Regression
- Decision Trees (CART)
- Random Forest (classification)
- Gradient Boosting (XGBoost, LightGBM, CatBoost)
- Support Vector Machines (SVC)
- k-Nearest Neighbors (kNN)
- Naive Bayes
- Neural Networks (classification)
- AdaBoost

**Conceitos de validacao relevantes (L2):**
- Overfitting
- Bias-Variance Tradeoff
- Class Imbalance
- Feature Importance
- Model Explainability
- Calibration
- Discrimination
- Data Drift
- Concept Drift
- Fairness

**Metricas e testes tipicos (L1):**
- AUC-ROC
- AUC-PR (Precision-Recall)
- Accuracy, Precision, Recall, F1
- Log Loss
- Brier Score
- Confusion Matrix
- Cohen's Kappa
- Matthews Correlation Coefficient (MCC)
- Gini Coefficient
- KS Statistic (Kolmogorov-Smirnov)
- Population Stability Index (PSI)
- SHAP Values
- Partial Dependence Plots

**Regulacao:** EU AI Act (alto risco), SR 11-7 (credit scoring), Equal Credit Opportunity Act

---

### 7. Regression ML Models

**Descricao:** Modelos de machine learning supervisionado para variavel resposta
continua. Arvores, boosting, SVR, etc.

**Subtipos:**
- Decision Trees (regression)
- Random Forest (regression)
- Gradient Boosting (XGBoost, LightGBM, CatBoost)
- Support Vector Regression (SVR)
- k-Nearest Neighbors (regression)
- ElasticNet / Lasso / Ridge (ja em Linear, mas cross-domain)
- Neural Networks (regression)

**Conceitos de validacao relevantes (L2):**
- Overfitting
- Bias-Variance Tradeoff
- Feature Importance
- Model Explainability
- Hyperparameter Sensitivity
- Data Drift
- Residual Analysis

**Metricas e testes tipicos (L1):**
- RMSE, MAE, MAPE, MdAE
- R², Adjusted R²
- Mean Bias
- Quantile Loss
- SHAP Values
- Permutation Feature Importance
- Residual Plots
- Learning Curves
- Cross-validation Scores

**Regulacao:** SR 11-7, EU AI Act (dependendo do uso)

---

### 8. Ensemble Models

**Descricao:** Modelos que combinam multiplos modelos base para melhorar
performance. Inclui stacking, blending e meta-learners.

**Subtipos:**
- Bagging (Bootstrap Aggregating)
- Boosting (AdaBoost, GBM, XGBoost, LightGBM, CatBoost)
- Stacking (meta-learner)
- Blending
- Voting Ensembles (hard/soft)
- Random Subspace Method
- Super Learner

**Conceitos de validacao relevantes (L2):**
- Overfitting
- Diversity of Base Learners
- Model Explainability
- Computational Cost
- Hyperparameter Sensitivity
- Model Stability

**Metricas e testes tipicos (L1):**
- Todas as metricas do task (classification ou regression)
- Diversity Metrics (Q-statistic, Correlation, Disagreement)
- Out-of-bag Error (OOB)
- Feature Importance (aggregated)
- Interaction Effects
- Ablation Studies

**Regulacao:** EU AI Act (explainability concerns), SR 11-7

---

### 9. Clustering Models

**Descricao:** Modelos nao-supervisionados que agrupam observacoes similares.
Validacao intrinseca (sem ground truth) e extrinseca.

**Subtipos:**
- K-Means / K-Medoids
- DBSCAN / HDBSCAN
- Gaussian Mixture Models (GMM)
- Agglomerative Hierarchical Clustering
- Spectral Clustering
- Mean Shift
- OPTICS
- Birch
- Fuzzy C-Means

**Conceitos de validacao relevantes (L2):**
- Cluster Stability
- Cluster Validity
- Number of Clusters Selection
- Scalability
- Sensitivity to Initialization
- Outlier Handling

**Metricas e testes tipicos (L1):**
- Silhouette Score
- Calinski-Harabasz Index
- Davies-Bouldin Index
- Adjusted Rand Index (ARI, extrinseca)
- Normalized Mutual Information (NMI, extrinseca)
- Elbow Method
- Gap Statistic
- Cluster Stability via Bootstrapping
- Inertia / Within-Cluster Sum of Squares

**Regulacao:** Menor pressao regulatoria direta; indireta quando usado em segmentacao de clientes

---

### 10. Dimensionality Reduction

**Descricao:** Tecnicas para reduzir o numero de features preservando
informacao relevante. Usadas em pre-processamento e visualizacao.

**Subtipos:**
- PCA (Principal Component Analysis)
- t-SNE
- UMAP
- LDA (Linear Discriminant Analysis)
- Autoencoders (para reducao)
- Factor Analysis
- Sparse PCA
- Kernel PCA
- ICA (Independent Component Analysis)
- NMF (Non-negative Matrix Factorization)

**Conceitos de validacao relevantes (L2):**
- Information Preservation
- Reconstruction Error
- Interpretability
- Scalability
- Stability of Embeddings

**Metricas e testes tipicos (L1):**
- Explained Variance Ratio (PCA)
- Reconstruction Error
- Trustworthiness Score (t-SNE, UMAP)
- Neighborhood Preservation
- Scree Plot
- Kaiser Criterion (eigenvalue > 1)
- Bartlett's Test of Sphericity
- KMO Test (Kaiser-Meyer-Olkin)

**Regulacao:** Menor pressao direta; relevante quando usado em pipelines regulados

---

### 11. Bayesian Models

**Descricao:** Modelos que usam inferencia bayesiana para estimar distribuicoes
posteriores de parametros. Incorporam prior knowledge formalmente.

**Subtipos:**
- Bayesian Linear Regression
- Bayesian Logistic Regression
- Gaussian Processes
- Bayesian Neural Networks
- Hierarchical / Multilevel Models
- Bayesian Structural Time Series (BSTS)
- Hidden Markov Models (HMM)
- Bayesian Additive Regression Trees (BART)
- Variational Inference Models

**Conceitos de validacao relevantes (L2):**
- Prior Sensitivity
- Convergence Diagnostics
- Model Comparison
- Posterior Predictive Checks
- Calibration
- Overfitting

**Metricas e testes tipicos (L1):**
- WAIC (Widely Applicable Information Criterion)
- LOO-CV (Leave-One-Out Cross-Validation)
- Bayes Factor
- R-hat (Gelman-Rubin convergence)
- Effective Sample Size (ESS)
- Trace Plots
- Posterior Predictive p-value
- DIC (Deviance Information Criterion)
- Credible Intervals vs Confidence Intervals

**Regulacao:** Variavel; crescente em pharma (clinical trials) e insurance

---

### 12. Reinforcement Learning

**Descricao:** Modelos que aprendem politicas de decisao via interacao com
ambiente. Maximizam recompensa acumulada ao longo do tempo.

**Subtipos:**
- Q-Learning / Deep Q-Networks (DQN)
- Policy Gradient (REINFORCE)
- Actor-Critic (A2C, A3C)
- Proximal Policy Optimization (PPO)
- Soft Actor-Critic (SAC)
- Multi-Armed Bandits (MAB)
- Contextual Bandits
- Model-based RL (World Models, Dreamer)
- Offline RL / Batch RL
- Multi-Agent RL (MARL)

**Conceitos de validacao relevantes (L2):**
- Reward Design
- Exploration-Exploitation Tradeoff
- Sample Efficiency
- Stability of Training
- Safety Constraints
- Sim-to-Real Transfer
- Off-policy Evaluation

**Metricas e testes tipicos (L1):**
- Cumulative Reward
- Regret (Bandit settings)
- Episode Length
- Policy Entropy
- Value Function Error
- Importance Sampling Estimators (OPE)
- Doubly Robust Estimator
- Safety Violation Rate
- Training Stability (reward curves)

**Regulacao:** EU AI Act (decisoes autonomas), safety-critical systems

---

### 13. Deep Learning — Vision

**Descricao:** Redes neurais profundas para processamento de imagens e video.
Convolucoes, atencao, deteccao de objetos.

**Subtipos:**
- Image Classification (CNNs: ResNet, EfficientNet, ViT)
- Object Detection (YOLO, Faster R-CNN, DETR)
- Semantic Segmentation (U-Net, DeepLab)
- Instance Segmentation (Mask R-CNN)
- Image Generation (part of Generative domain)
- Video Understanding
- OCR / Document AI
- Medical Imaging

**Conceitos de validacao relevantes (L2):**
- Overfitting
- Data Augmentation Adequacy
- Robustness to Adversarial Attacks
- Distribution Shift
- Model Explainability
- Fairness (demographic bias em facial recognition)
- Calibration

**Metricas e testes tipicos (L1):**
- Accuracy, Top-5 Accuracy
- mAP (mean Average Precision, detection)
- IoU (Intersection over Union)
- Dice Score (segmentation)
- FID Score (generation quality)
- Grad-CAM / Saliency Maps
- Adversarial Robustness Score
- Calibration Error (ECE)
- Confusion Matrix per class
- FPS (inference speed)

**Regulacao:** EU AI Act (biometric identification = alto risco), FDA (medical imaging)

---

### 14. Deep Learning — Tabular

**Descricao:** Redes neurais aplicadas a dados tabulares/estruturados.
Alternativa a tree-based models para dados corporativos.

**Subtipos:**
- Feed-forward Neural Networks (MLP)
- TabNet
- NODE (Neural Oblivious Decision Ensembles)
- FT-Transformer
- TabTransformer
- DeepFM (recomendacao)
- Wide & Deep
- AutoInt

**Conceitos de validacao relevantes (L2):**
- Overfitting (mais critico que em trees)
- Hyperparameter Sensitivity
- Model Explainability
- Comparison with Baselines (tree models)
- Feature Importance
- Calibration

**Metricas e testes tipicos (L1):**
- Todas as metricas de classification/regression
- Comparison Table vs XGBoost/LightGBM
- Training Curves (loss, validation)
- SHAP / Integrated Gradients
- Ablation Studies
- Inference Latency

**Regulacao:** SR 11-7, EU AI Act (dependendo do uso)

---

### 15. Deep Learning — Sequential

**Descricao:** Redes neurais para dados sequenciais (texto, audio, series temporais).
RNNs, LSTMs, Transformers.

**Subtipos:**
- RNN (Vanilla)
- LSTM / GRU
- Bidirectional LSTM
- Seq2Seq (Encoder-Decoder)
- Transformer (attention-based)
- Temporal Convolutional Networks (TCN)
- WaveNet
- Informer / Autoformer (long-range forecasting)

**Conceitos de validacao relevantes (L2):**
- Overfitting
- Vanishing/Exploding Gradients
- Sequence Length Sensitivity
- Attention Interpretability
- Forecast Accuracy
- Computational Cost

**Metricas e testes tipicos (L1):**
- Perplexity (language modeling)
- RMSE, MAE (forecasting)
- BLEU, ROUGE (translation/summarization)
- Attention Visualization
- Training Stability
- Gradient Norm Monitoring
- Inference Latency
- Memory Usage

**Regulacao:** Variavel; depende da aplicacao downstream

---

### 16. NLP — Classical

**Descricao:** Processamento de linguagem natural pre-deep learning.
Bag-of-words, TF-IDF, topic modeling, NER baseado em regras.

**Subtipos:**
- Bag-of-Words / TF-IDF
- Topic Modeling (LDA, NMF)
- Named Entity Recognition (rule-based, CRF)
- Sentiment Analysis (lexicon-based)
- Text Classification (SVM, Naive Bayes)
- Information Extraction (regex, patterns)
- Keyword Extraction (TextRank, RAKE)

**Conceitos de validacao relevantes (L2):**
- Feature Representation Quality
- Vocabulary Coverage
- Class Imbalance (text classification)
- Domain Adaptation
- Annotation Quality

**Metricas e testes tipicos (L1):**
- Accuracy, Precision, Recall, F1
- Coherence Score (topic modeling)
- Perplexity (topic modeling)
- Entity-level F1 (NER)
- Inter-annotator Agreement (Cohen's Kappa)
- Confusion Matrix
- TF-IDF Feature Analysis

**Regulacao:** Menor pressao direta; relevante em compliance text mining

---

### 17. NLP — Embeddings

**Descricao:** Modelos de representacao vetorial de texto. Transformam
palavras/frases/documentos em vetores densos.

**Subtipos:**
- Word2Vec (CBOW, Skip-gram)
- GloVe
- FastText
- ELMo
- BERT / RoBERTa / DeBERTa (contextual embeddings)
- Sentence-BERT (SBERT)
- Universal Sentence Encoder
- Doc2Vec
- Domain-specific Embeddings (BioBERT, FinBERT, LegalBERT)

**Conceitos de validacao relevantes (L2):**
- Embedding Quality
- Bias in Embeddings
- Domain Relevance
- Semantic Similarity Accuracy
- Stability of Representations
- Out-of-Vocabulary Handling

**Metricas e testes tipicos (L1):**
- Cosine Similarity (intrinsic)
- Spearman Correlation (STS benchmarks)
- Analogy Tests (king - man + woman = queen)
- WEAT (Word Embedding Association Test, bias)
- Downstream Task Performance
- Nearest Neighbor Quality
- Clustering of Embeddings
- Probing Tasks (syntactic/semantic)

**Regulacao:** EU AI Act (indireta, via downstream use), fairness regulations

---

### 18. Large Language Models

**Descricao:** Foundation models de linguagem com bilhoes de parametros.
GPT, Claude, Llama, Gemini. Modelos generativos de texto.

**Subtipos:**
- Autoregressive LMs (GPT-4, Claude, Llama, Mistral)
- Encoder-only (BERT, para fine-tuning)
- Encoder-Decoder (T5, BART)
- Instruction-tuned Models
- RLHF-trained Models
- Retrieval-Augmented Generation (RAG)
- Fine-tuned Domain Models
- Multimodal LLMs (GPT-4V, Gemini)
- Small Language Models (Phi, Gemma)

**Conceitos de validacao relevantes (L2):**
- Hallucination
- Factual Accuracy
- Calibration
- Bias
- Toxicity
- Robustness
- Prompt Sensitivity
- Data Contamination
- Alignment
- Safety
- Model Explainability
- Cost Efficiency

**Metricas e testes tipicos (L1):**
- Perplexity
- BLEU, ROUGE, METEOR (generation quality)
- BERTScore
- Factuality Score (FActScore)
- Hallucination Rate
- TruthfulQA Benchmark
- MMLU (Massive Multitask Language Understanding)
- HellaSwag
- HumanEval (code generation)
- Toxicity Score (Perspective API)
- Bias Benchmarks (BBQ, WinoBias)
- Cost per Token
- Latency (time to first token, tokens per second)
- Context Window Utilization
- Faithfulness Score (RAG)
- Answer Relevancy (RAG)

**Regulacao:** EU AI Act (general-purpose AI), NIST AI RMF, Executive Order on AI (US), China AI regulations

---

### 19. Generative Models

**Descricao:** Modelos que geram novos dados (imagens, audio, video, dados sinteticos).
GANs, VAEs, Diffusion Models.

**Subtipos:**
- GANs (GAN, DCGAN, StyleGAN, CycleGAN, Pix2Pix)
- VAEs (Variational Autoencoders)
- Diffusion Models (Stable Diffusion, DALL-E)
- Flow-based Models (RealNVP, Glow)
- Autoregressive Image Models (PixelCNN)
- Synthetic Data Generators (CTGAN, TVAE)
- Audio Generation (WaveGAN, Tacotron)
- Video Generation (Sora, Runway)

**Conceitos de validacao relevantes (L2):**
- Generation Quality
- Diversity of Outputs
- Mode Collapse (GANs)
- Training Stability
- Privacy Preservation
- Bias in Generation
- Fidelity vs Diversity Tradeoff

**Metricas e testes tipicos (L1):**
- FID (Frechet Inception Distance)
- IS (Inception Score)
- KID (Kernel Inception Distance)
- LPIPS (Learned Perceptual Image Patch Similarity)
- SSIM (Structural Similarity Index)
- Coverage / Density (manifold metrics)
- Machine Learning Efficacy (synthetic data)
- Statistical Similarity Tests
- Privacy Metrics (membership inference)
- Human Evaluation Scores
- CLIP Score (text-to-image alignment)

**Regulacao:** EU AI Act (deepfakes, synthetic media), copyright laws

---

### 20. Recommender Systems

**Descricao:** Modelos que predizem preferencias de usuarios para itens.
Filtragem colaborativa, content-based, hibridos.

**Subtipos:**
- Collaborative Filtering (user-based, item-based)
- Matrix Factorization (SVD, ALS, NMF)
- Content-based Filtering
- Hybrid Systems
- Deep Recommenders (NCF, DeepFM, Two-Tower)
- Sequential Recommendation (SASRec, BERT4Rec)
- Knowledge Graph-based Recommendation
- Contextual Bandits for Recommendation
- Session-based Recommendation

**Conceitos de validacao relevantes (L2):**
- Cold Start Problem
- Data Sparsity
- Popularity Bias
- Fairness
- Diversity
- Serendipity
- Scalability
- A/B Testing

**Metricas e testes tipicos (L1):**
- NDCG (Normalized Discounted Cumulative Gain)
- MAP (Mean Average Precision)
- Hit Rate / Recall@K
- Precision@K
- MRR (Mean Reciprocal Rank)
- Coverage (catalog coverage)
- Diversity Index
- Novelty Score
- AUC (implicit feedback)
- RMSE (explicit ratings)
- Online A/B Test Metrics (CTR, conversion)

**Regulacao:** Digital Services Act (EU), FTC (US), consumer protection laws

---

### 21. Anomaly Detection

**Descricao:** Modelos para detectar observacoes atipicas, fraude,
intrusions, defeitos. Supervisionados e nao-supervisionados.

**Subtipos:**
- Isolation Forest
- One-Class SVM
- Local Outlier Factor (LOF)
- Autoencoders (reconstruction error)
- Statistical Methods (Z-score, IQR, Grubbs)
- DBSCAN-based Detection
- Elliptic Envelope
- Rule-based Systems
- Graph-based Anomaly Detection
- Deep SVDD

**Conceitos de validacao relevantes (L2):**
- Class Imbalance (extreme)
- False Positive Rate Control
- Threshold Selection
- Concept Drift
- Explainability of Alerts
- Real-time Performance
- Seasonality Awareness

**Metricas e testes tipicos (L1):**
- Precision, Recall, F1 (anomaly class)
- AUC-ROC
- AUC-PR (mais relevante com class imbalance)
- False Positive Rate at fixed Recall
- Detection Latency
- Alert Volume
- SAR Filing Rate (AML)
- Reconstruction Error Distribution
- Threshold Sensitivity Analysis

**Regulacao:** PCI-DSS (fraude), AML/KYC (lavagem de dinheiro), BCBS 239

---

### 22. Causal Inference Models

**Descricao:** Modelos que estimam efeitos causais, nao apenas correlacoes.
Fundamentais para decisoes de politica e tratamento.

**Subtipos:**
- Randomized Controlled Trials (RCT)
- Difference-in-Differences (DiD)
- Regression Discontinuity Design (RDD)
- Instrumental Variables (IV / 2SLS)
- Propensity Score Matching (PSM)
- Inverse Probability Weighting (IPW)
- Synthetic Control Method
- Double/Debiased Machine Learning (DML)
- Causal Forests (Generalized Random Forests)
- Structural Equation Models (SEM)
- Directed Acyclic Graphs (DAGs)
- Do-Calculus (Pearl's framework)

**Conceitos de validacao relevantes (L2):**
- Confounding
- Selection Bias
- External Validity
- Internal Validity
- Parallel Trends Assumption (DiD)
- Overlap / Positivity
- Sensitivity to Unmeasured Confounding
- Stable Unit Treatment Value (SUTVA)

**Metricas e testes tipicos (L1):**
- Average Treatment Effect (ATE)
- Average Treatment Effect on Treated (ATT)
- Conditional Average Treatment Effect (CATE)
- Balance Tests (covariate balance)
- Placebo Tests
- Rosenbaum Sensitivity Analysis
- E-value (unmeasured confounding)
- Pre-trend Tests (DiD)
- McCrary Density Test (RDD)
- Weak Instrument Tests (F-statistic > 10)

**Regulacao:** FDA (clinical trials), EMA, public policy evaluation standards

---

### 23. Graph-based Models

**Descricao:** Modelos que operam sobre dados em formato de grafo.
Graph Neural Networks, knowledge graph embeddings, link prediction.

**Subtipos:**
- Graph Convolutional Networks (GCN)
- GraphSAGE
- Graph Attention Networks (GAT)
- Graph Isomorphism Network (GIN)
- Knowledge Graph Embeddings (TransE, RotatE, ComplEx)
- Link Prediction Models
- Node Classification Models
- Graph Classification Models
- Message Passing Neural Networks (MPNN)
- Temporal Graph Networks

**Conceitos de validacao relevantes (L2):**
- Over-smoothing
- Graph Structure Sensitivity
- Scalability
- Inductive vs Transductive Learning
- Embedding Quality
- Heterogeneous Graph Handling

**Metricas e testes tipicos (L1):**
- Node Classification Accuracy/F1
- Link Prediction (MRR, Hits@K)
- Graph Classification Accuracy
- Mean Rank / Mean Reciprocal Rank
- AUC (link prediction)
- Neighborhood Aggregation Analysis
- Over-smoothing Metrics (MADGap)
- Scalability Benchmarks

**Regulacao:** Menor pressao direta; relevante quando usado em fraud detection, AML

---

### 24. Optimization Models

**Descricao:** Modelos de otimizacao matematica para decisoes operacionais.
Programacao linear, inteira, estocastica.

**Subtipos:**
- Linear Programming (LP)
- Integer Programming (IP / MIP)
- Quadratic Programming (QP)
- Convex Optimization
- Stochastic Programming
- Robust Optimization
- Multi-objective Optimization
- Constraint Programming
- Metaheuristics (Genetic Algorithms, Simulated Annealing, PSO)
- Dynamic Programming

**Conceitos de validacao relevantes (L2):**
- Feasibility
- Optimality Gap
- Sensitivity Analysis
- Robustness to Input Uncertainty
- Computational Tractability
- Scalability
- Solution Quality vs Time Tradeoff

**Metricas e testes tipicos (L1):**
- Objective Function Value
- Optimality Gap (%)
- Constraint Violation
- Dual Gap
- Solution Time
- Sensitivity Report (shadow prices, reduced costs)
- Pareto Front (multi-objective)
- Convergence Curves (metaheuristics)
- Robustness under Perturbation

**Regulacao:** Setor-especifico (supply chain, energy, portfolio optimization)

---

### 25. Simulation Models

**Descricao:** Modelos que simulam sistemas complexos. Monte Carlo,
agent-based, discrete event, system dynamics.

**Subtipos:**
- Monte Carlo Simulation
- Agent-Based Models (ABM)
- Discrete Event Simulation (DES)
- System Dynamics
- Microsimulation
- Stochastic Simulation (Gillespie)
- Digital Twins
- Scenario Analysis / Stress Testing
- Bootstrap Simulation

**Conceitos de validacao relevantes (L2):**
- Convergence
- Calibration
- Sensitivity Analysis
- Scenario Coverage
- Model Fidelity
- Computational Efficiency
- Reproducibility

**Metricas e testes tipicos (L1):**
- Convergence Diagnostics (variance reduction)
- Number of Simulations (sufficiency test)
- Scenario Coverage Ratio
- Calibration to Historical Data
- Stress Test Results (tail percentiles)
- VaR / CVaR (risk)
- Confidence Intervals Width
- Run Time per Simulation
- Seed Sensitivity Analysis

**Regulacao:** Basel (stress testing, market risk), CCAR/DFAST (US), Solvency II

---

## Conceitos Compartilhados (Level 2) — Visao Geral

Estes conceitos aparecem em **multiplos dominios** e sao o motivo principal
para usar uma unica ontologia:

| Conceito (L2) | Dominios onde aparece |
|----------------|----------------------|
| Overfitting | Quase todos |
| Bias | Classification, LLM, Embeddings, Vision, Recommender |
| Calibration | GLM, Survival, Classification, LLM, Bayesian |
| Data Drift | Classification, Regression ML, Anomaly Detection |
| Feature Importance | Linear Regression, Classification, Regression ML, Ensemble |
| Model Explainability | Classification, Ensemble, Deep Learning, LLM |
| Model Stability | Time Series, Panel Data, Simulation |
| Fairness | Classification, LLM, Recommender, Embeddings |
| Stationarity | Time Series, Panel Data |
| Class Imbalance | Classification, Anomaly Detection |
| Convergence | Bayesian, Simulation, Optimization |
| Sensitivity Analysis | Causal Inference, Simulation, Optimization |
| Goodness of Fit | GLM, Linear Regression, Survival |
| Discrimination | GLM, Survival, Classification |
| Robustness | LLM, Deep Learning, Optimization |
| Scalability | Clustering, Graph Models, Recommender, Optimization |
| Hyperparameter Sensitivity | Regression ML, Deep Learning Tabular, Ensemble |
| Computational Cost | Deep Learning, LLM, Reinforcement Learning, Optimization |

---

## Resumo Quantitativo

| Metrica | Contagem |
|---------|----------|
| **Domains (L3)** | 25 |
| **Subtipos de modelo (dentro dos domains)** | ~200+ |
| **Conceitos compartilhados (L2)** | ~18 principais |
| **Metricas e testes (L1)** | ~250+ unicos |
| **Setores regulados cobertos** | Banking, Insurance, Healthcare, Government, Tech |
| **Regulacoes mapeadas** | SR 11-7, Basel, EU AI Act, NIST AI RMF, Solvency II, IFRS, FDA, FTC |

---

## Proximos Passos

1. Usar este documento como base para construir `ontology.yaml` do domain `model_validation`
2. Selecionar os ~18-22 entity types mais relevantes (sem ultrapassar 25)
3. Definir relationship types que cruzam dominios
4. Criar aliases para cada dominio/subtipo/metrica
5. Criar seed entities com os itens mais fundamentais

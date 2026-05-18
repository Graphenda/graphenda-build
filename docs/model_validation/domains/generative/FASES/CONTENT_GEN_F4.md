# Fase F4 — Codigo de Exemplo

**Status**: CONCLUIDO
**Dependencias**: F3
**Bloqueia**: F5

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/generative/`

---

## Arquivos a Gerar

### Modeling (4 arquivos)

#### 1. modeling/gan_tabular.py
- CTGAN com sdv para dados tabulares sinteticos
- Configuracao de hiperparametros
- Geracao e comparacao visual com reais
- Preservacao de restricoes (tipos, ranges)
- Dataset: Adult Income (UCI)

#### 2. modeling/vae_tabular.py
- VAE para dados tabulares com PyTorch
- Encoder-decoder linear
- Amostragem e interpolacao no espaco latente
- Comparacao com CTGAN
- Dataset: Adult Income (UCI)

#### 3. modeling/diffusion_basic.py
- DDPM simplificado com PyTorch
- Forward e reverse process
- Noise scheduler
- Geracao e avaliacao
- Dataset: MNIST (torchvision)

#### 4. modeling/synthetic_data_pipeline.py
- Pipeline completo: CTGAN vs TVAE vs Gaussian Copula (sdv)
- Comparacao de qualidade entre metodos
- Export de dataset sintetico final
- Dataset: Adult Income (UCI) ou Credit Card Fraud

### Validation (2 arquivos)

#### 5. validation/synthetic_quality_eval.py
- KS test e chi-squared por coluna
- Preservacao de correlacoes (diff de matrizes)
- ML utility: XGBoost em sinteticos, avaliar em reais
- Mode collapse detection
- Dataset: dados gerados na F4.1/F4.4

#### 6. validation/privacy_evaluation.py
- Distance to Closest Record (DCR)
- Membership inference attack basico
- Comparacao de re-identificacao entre metodos
- Report de risco de privacidade
- Dataset: dados gerados na F4.1/F4.4

### Visualization (1 arquivo)

#### 7. visualization/generative_plots.py
- Distribuicoes marginais: real vs sintetico (histogramas sobrepostos)
- Heatmap de correlacao: real vs sintetico side-by-side
- t-SNE/UMAP de reais vs sinteticos
- Training loss curves (generator vs discriminator)
- Privacy metrics (DCR distribution)
- Dataset: dados gerados nos scripts anteriores

---

## Formato: cada script com docstring, main(), RANDOM_STATE = 42

---

## Criterios de Aceite

- [x] 7 scripts Python criados nas subpastas corretas
- [x] modeling/gan_tabular.py — CTGAN com sdv para dados tabulares
- [x] modeling/vae_tabular.py — VAE tabular com PyTorch
- [x] modeling/diffusion_basic.py — DDPM simplificado
- [x] modeling/synthetic_data_pipeline.py — CTGAN vs TVAE vs Gaussian Copula
- [x] validation/synthetic_quality_eval.py — KS, chi2, correlacao, ML utility
- [x] validation/privacy_evaluation.py — DCR, membership inference
- [x] visualization/generative_plots.py — Distribuicoes, correlacao, t-SNE, DCR
- [x] Todos passam verificacao de sintaxe Python
- [x] Todos tem docstring, funcoes organizadas e main()
- [x] Stack: sdv + torch + sdmetrics

---

## Bibliotecas Utilizadas

| Biblioteca | Versao Minima | Uso |
|------------|---------------|-----|
| sdv | >= 1.0 | CTGAN, TVAE, Gaussian Copula |
| sdmetrics | >= 0.11 | Metricas de qualidade sintetica |
| torch | >= 2.0 | VAE, DDPM customizados |
| xgboost | >= 2.0 | ML utility test |
| scikit-learn | >= 1.3 | Metricas, preprocessing |
| matplotlib | >= 3.7 | Visualizacoes |
| seaborn | >= 0.12 | Visualizacoes |
| umap-learn | >= 0.5 | Visualizacao de embeddings |

---

**End of Specification**

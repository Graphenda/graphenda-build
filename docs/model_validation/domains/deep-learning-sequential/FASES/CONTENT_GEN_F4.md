# Fase F4 — Codigo de Exemplo

**Status**: COMPLETO
**Dependencias**: F3
**Bloqueia**: F5

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/deep-learning-sequential/`

---

## Arquivos a Gerar

### Modeling (5 arquivos)

#### 1. modeling/lstm_time_series.py
- LSTM para previsao de series temporais com PyTorch
- Preprocessamento: windowing, normalizacao
- Teacher forcing durante treino
- Multi-step forecasting
- Dataset: ETTh1 ou AirPassengers (statsmodels)

#### 2. modeling/gru_sequence.py
- GRU como alternativa ao LSTM
- Comparacao de parametros e tempo de treino
- Aplicacao a dados financeiros (sintetico ou Exchange Rates)
- Dataset: sintetico ou Exchange Rates

#### 3. modeling/transformer_time_series.py
- Transformer para series temporais com PyTorch
- Positional encoding para dados temporais
- Self-attention e visualizacao dos pesos
- Comparacao com LSTM no mesmo dataset
- Dataset: ETTh1 ou AirPassengers

#### 4. modeling/tft_multihorizon.py
- TFT com pytorch-forecasting
- Previsao multi-horizonte com intervalos de confianca
- Variable selection network e interpretabilidade
- Comparacao com baselines estatisticos
- Dataset: Electricity ou sintetico

#### 5. modeling/baseline_statistical.py
- ARIMA, ETS, Prophet como baselines
- Pipeline de comparacao padronizado
- Teste Diebold-Mariano entre modelos
- Dataset: mesmo dataset dos modelos DL

### Validation (2 arquivos)

#### 6. validation/walk_forward_validation.py
- Walk-forward com expanding e sliding window
- Avaliacao por horizonte de previsao
- Deteccao de degradacao temporal
- Comparacao entre estrategias de validacao
- Dataset: modelos treinados nas F4.1-F4.4

#### 7. validation/attention_analysis.py
- Extracao e visualizacao de attention weights
- Analise de quais timesteps recebem mais atencao
- Comparacao com feature importance por permutacao
- Dataset: Transformer ou TFT treinado

### Visualization (1 arquivo)

#### 8. visualization/sequential_plots.py
- Previsao vs realizado com intervalos de confianca
- Attention heatmaps por timestep
- Learning curves (train vs validation loss)
- Comparacao de metricas por horizonte (bar chart)
- Analise de erros ao longo do tempo
- Dataset: modelos anteriores

---

## Formato: cada script com docstring, main(), RANDOM_STATE = 42

---

## Criterios de Aceite

- [x] 8 scripts Python criados nas subpastas corretas
- [x] modeling/lstm_time_series.py — LSTM com windowing e multi-step
- [x] modeling/gru_sequence.py — GRU com comparacao vs LSTM
- [x] modeling/transformer_time_series.py — Transformer com positional encoding
- [x] modeling/tft_multihorizon.py — TFT com pytorch-forecasting
- [x] modeling/baseline_statistical.py — ARIMA, ETS, Prophet com Diebold-Mariano
- [x] validation/walk_forward_validation.py — Walk-forward expanding e sliding
- [x] validation/attention_analysis.py — Attention weights extraction e visualizacao
- [x] visualization/sequential_plots.py — Forecast, attention heatmaps, learning curves
- [x] Todos os scripts passam verificacao de sintaxe Python
- [x] Todos os scripts tem docstring, funcoes organizadas e main()
- [x] Codigo usa PyTorch como stack principal

---

## Bibliotecas Utilizadas

| Biblioteca | Versao Minima | Uso |
|------------|---------------|-----|
| torch | >= 2.0 | LSTM, GRU, Transformer |
| pytorch-forecasting | >= 1.0 | TFT, N-BEATS |
| statsmodels | >= 0.14 | ARIMA, ETS baselines |
| prophet | >= 1.1 | Baseline Prophet |
| matplotlib | >= 3.7 | Visualizacoes |
| seaborn | >= 0.12 | Visualizacoes |
| numpy | >= 1.24 | Arrays |
| pandas | >= 2.0 | DataFrames |

---

## Ferramentas Necessarias

- **Read**, **WebSearch**, **Write**

---

**End of Specification**

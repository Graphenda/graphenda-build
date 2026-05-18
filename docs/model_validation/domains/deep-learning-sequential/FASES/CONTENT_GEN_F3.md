# Fase F3 — Guias Explicativos

**Status**: COMPLETO
**Dependencias**: F1
**Bloqueia**: F4, F5

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/deep-learning-sequential/`

---

## Guias a Gerar

### 1. overview.md
- Modelos sequenciais e por que a ordem dos dados importa
- Evolucao: RNN -> LSTM -> GRU -> Transformer
- Aplicacoes: series temporais, NLP, sequencias de eventos
- Quando DL sequencial vs modelos estatisticos (ARIMA, ETS)
- Trade-off complexidade vs interpretabilidade

### 2. models.md
- RNN vanilla: vanishing gradient
- LSTM: gates (forget, input, output), celula de memoria
- GRU: arquitetura simplificada
- Transformer para TS: positional encoding, self-attention
- TFT: multi-horizon, interpretavel, variable selection
- N-BEATS: blocos de base expansion, interpretabilidade
- Informer: ProbSparse attention para sequencias longas
- Encoder-Decoder vs modelos diretos

### 3. validation.md
- Checklist de validacao para modelos sequenciais
- Walk-forward validation: expanding e sliding window
- Proibicao de data leakage temporal
- Convergencia e estabilidade do treino
- Teste em diferentes horizontes
- Comparacao obrigatoria com baselines (ARIMA, ETS, Prophet)
- Attention weights como diagnostico
- Robustez a mudancas de regime

### 4. metrics.md
- MAE, RMSE, MAPE para series temporais
- sMAPE: metrica simetrica
- MASE: comparacao com baseline naive
- Metricas por horizonte (1-step vs multi-step)
- Coverage e width de intervalos de previsao
- Diebold-Mariano test
- Calibracao para previsoes probabilisticas

### 5. pitfalls.md
- Data leakage temporal
- Nao usar walk-forward validation
- Ignorar baselines simples que vencem DL
- Overfitting em series curtas
- Confundir correlacao temporal com capacidade preditiva
- Attention weights nao sao explicacoes causais
- Nao reportar variancia entre runs

---

## Formato: frontmatter com `slug: deep-learning-sequential-<nome>`, `domain: deep-learning-sequential`, `type: guide`

Cada guia: minimo 1500 palavras, formulas LaTeX (LSTM gates, attention, positional encoding), tabelas, referencias da F1.

---

## Criterios de Aceite

- [x] 5 guias criados: overview.md, models.md, validation.md, metrics.md, pitfalls.md
- [x] Alem dos 5 guias, papers.md da F1 tambem presente
- [x] Todos com frontmatter YAML valido
- [x] Cada guia com minimo de 1500 palavras
- [x] Formulas LaTeX incluidas (LSTM gates, attention scores, positional encoding)
- [x] Referencias cruzadas aos papers da F1
- [x] Conteudo baseado em pesquisa web
- [x] Tom tecnico para profissionais de model validation

---

## Ferramentas Necessarias

- **Read**, **WebSearch**, **WebFetch**, **Write**

---

**End of Specification**

# Fase F4 — Codigo de Exemplo

**Status**: CONCLUIDO
**Dependencias**: F3
**Bloqueia**: F5

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/reinforcement-learning/`

---

## Arquivos a Gerar

### Modeling (4 arquivos)

#### 1. modeling/dqn_agent.py
- DQN com PyTorch e Gymnasium
- Experience replay buffer
- Target network com periodic update
- Treinamento em CartPole-v1
- Epsilon-greedy decay

#### 2. modeling/ppo_agent.py
- PPO com PyTorch e Gymnasium
- Clipped surrogate objective
- GAE (Generalized Advantage Estimation)
- Treinamento em CartPole-v1
- Comparacao on-policy vs DQN

#### 3. modeling/bandits.py
- Multi-Armed Bandits: epsilon-greedy, UCB1, Thompson Sampling
- Comparacao de estrategias de exploracao
- Regret acumulado por algoritmo
- Contextual bandits basico
- Ambiente sintetico de k-armed bandit

#### 4. modeling/sac_continuous.py
- SAC para controle continuo com PyTorch
- Entropy regularization automatica
- Treinamento em Pendulum-v1
- Comparacao com random policy baseline

### Validation (2 arquivos)

#### 5. validation/off_policy_evaluation.py
- Importance Sampling estimator
- Weighted Importance Sampling
- Doubly Robust estimator
- Confidence intervals para OPE
- Comparacao de estimadores com dados simulados

#### 6. validation/reproducibility_analysis.py
- Treinamento com multiplos seeds (10+ runs)
- Estatisticas agregadas: media, mediana, percentis
- Intervalo de confianca da performance
- Analise de sensibilidade a hiperparametros chave (lr, gamma, epsilon)

### Visualization (1 arquivo)

#### 7. visualization/rl_plots.py
- Learning curves com bandas de confianca (multiplos seeds)
- Reward por episodio com smoothing (moving average)
- Regret acumulado (bandits)
- Heatmap de Q-values (ambientes discretos simples)
- Comparacao de algoritmos side-by-side
- Distribuicao de returns por politica

---

## Formato: cada script com docstring, main(), RANDOM_STATE = 42

---

## Criterios de Aceite

- [x] 7 scripts Python criados nas subpastas corretas
- [x] modeling/dqn_agent.py — DQN com experience replay e target network
- [x] modeling/ppo_agent.py — PPO com clipped objective e GAE
- [x] modeling/bandits.py — Epsilon-greedy, UCB1, Thompson Sampling com regret
- [x] modeling/sac_continuous.py — SAC para controle continuo
- [x] validation/off_policy_evaluation.py — IS, WIS, DR com confidence intervals
- [x] validation/reproducibility_analysis.py — Multi-seed training com estatisticas
- [x] visualization/rl_plots.py — Learning curves, regret, Q-values, comparacao
- [x] Todos os scripts passam verificacao de sintaxe Python
- [x] Todos os scripts tem docstring, funcoes organizadas e main()
- [x] Codigo usa gymnasium e PyTorch (sem stable-baselines3 para ser didatico)

---

## Bibliotecas Utilizadas

| Biblioteca | Versao Minima | Uso |
|------------|---------------|-----|
| numpy | >= 1.24 | Arrays |
| torch | >= 2.0 | Redes neurais para DQN, PPO, SAC |
| gymnasium | >= 0.29 | Ambientes RL (CartPole, Pendulum, LunarLander) |
| matplotlib | >= 3.7 | Visualizacoes |
| seaborn | >= 0.12 | Visualizacoes estatisticas |
| scipy | >= 1.11 | Estatisticas para OPE |

---

## Ferramentas Necessarias

- **Read**, **WebSearch**, **Write**

---

**End of Specification**

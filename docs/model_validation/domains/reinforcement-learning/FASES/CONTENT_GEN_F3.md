# Fase F3 — Guias Explicativos

**Status**: COMPLETO
**Dependencias**: F1
**Bloqueia**: F4, F5

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/reinforcement-learning/`

---

## Guias a Gerar

### 1. overview.md
- O que e RL e como difere de supervised/unsupervised
- Elementos: agente, ambiente, estado, acao, recompensa, politica
- MDP (Markov Decision Process): formulacao matematica
- Categorias: model-free vs model-based, on-policy vs off-policy
- Aplicacoes: jogos, robotica, financas, recomendacao, controle
- Desafios unicos de validacao em RL

### 2. models.md
- Multi-Armed Bandits: epsilon-greedy, UCB, Thompson Sampling
- Q-Learning: value-based, tabular
- DQN: deep Q-network, experience replay, target network
- Double DQN, Dueling DQN
- REINFORCE: policy gradient basico
- A2C/A3C: Actor-Critic com advantage
- PPO: clipped surrogate objective
- DDPG e TD3: acoes continuas, off-policy
- SAC: soft actor-critic, maximum entropy

### 3. validation.md
- Learning curves: reward acumulado ao longo de episodios
- Off-Policy Evaluation (OPE): importance sampling, doubly robust
- Importance Sampling com clipping
- Fitted Q Evaluation (FQE)
- Safety constraints
- Reproducibilidade: sensibilidade a seeds e hiperparametros
- Ablation studies
- Comparacao com baselines (random policy, heuristica)

### 4. metrics.md
- Cumulative reward (return)
- Average reward per episode
- Success rate
- Regret (bandits)
- Off-Policy Evaluation metrics: MSE do value estimado
- Confidence intervals para OPE (bootstrap, HCOPE)
- Sample efficiency: reward vs interacoes
- Wall-clock time

### 5. pitfalls.md
- Reward hacking
- Nao avaliar off-policy antes de deploy
- Reproducibilidade: resultados variam entre seeds
- Overfitting ao ambiente de treino
- Sparse rewards sem reward shaping
- Safety: acoes perigosas durante exploracao
- Comparacao injusta: baselines nao tuned
- Nao reportar variancia entre runs

---

## Formato: frontmatter com `slug: reinforcement-learning-<nome>`, `domain: reinforcement-learning`, `type: guide`

Cada guia: minimo 1500 palavras, formulas LaTeX (Bellman equation, policy gradient, MDP), tabelas comparativas, referencias da F1.

---

## Criterios de Aceite

- [x] 5 guias criados: overview.md, models.md, validation.md, metrics.md, pitfalls.md
- [x] Alem dos 5 guias, papers.md da F1 tambem presente no diretorio
- [x] Todos com frontmatter YAML valido
- [x] Cada guia com minimo de 1500 palavras
- [x] Formulas LaTeX incluidas (Bellman, policy gradient, importance sampling)
- [x] Referencias cruzadas aos papers da F1
- [x] Conteudo baseado em pesquisa web
- [x] Tom tecnico e adequado para profissionais de model validation

---

## Ferramentas Necessarias

- **Read**, **WebSearch**, **WebFetch**, **Write**

---

**End of Specification**

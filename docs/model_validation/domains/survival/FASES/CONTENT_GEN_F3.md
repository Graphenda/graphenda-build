# Fase F3 — Guias Explicativos

**Status**: CONCLUIDO
**Dependencias**: F1 (para referencias dos papers)
**Bloqueia**: F4, F5

---

## Objetivo

Criar 5 guias explicativos completos sobre analise de sobrevivencia.

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/survival/`

---

## Guias a Gerar

### 1. overview.md — Visao Geral de Analise de Sobrevivencia

**Conteudo obrigatorio:**
- O que e analise de sobrevivencia e por que e especial (censura)
- Tipos de censura: a direita, a esquerda, por intervalo
- Funcoes fundamentais: S(t), h(t), H(t), f(t)
- Aplicacoes: medicina, churn, credit risk (time-to-default), confiabilidade
- Quando usar sobrevivencia vs logistica vs Poisson

**Pesquisa web:** buscar aplicacoes recentes em bancos (time-to-default), churn, oncologia

### 2. models.md — Tipos de Modelos de Sobrevivencia

**Conteudo obrigatorio:**
- Kaplan-Meier: estimador nao-parametrico, curvas de sobrevivencia
- Nelson-Aalen: estimador de hazard acumulada
- Cox Proportional Hazards: semi-parametrico, hazard ratios
- Cox com time-varying covariates
- Accelerated Failure Time (AFT): Weibull, Log-Normal, Log-Logistic
- Modelos parametricos: Exponencial, Weibull, Gompertz
- Competing Risks: Fine-Gray, cause-specific hazards

**Pesquisa web:** buscar comparacoes praticas, quando usar cada modelo

### 3. validation.md — Validacao de Modelos de Sobrevivencia

**Conteudo obrigatorio:**
- Teste da premissa de riscos proporcionais (Schoenfeld residuals)
- Log-log plot para verificacao visual de PH
- C-statistic (Harrell's concordance index)
- Calibracao de modelos de sobrevivencia
- Teste de log-rank para comparacao de curvas
- Brier Score temporal para sobrevivencia
- Validacao com bootstrap e cross-validation temporal

**Pesquisa web:** buscar melhores praticas de validacao, frameworks regulatorios

### 4. metrics.md — Metricas e Testes

**Conteudo obrigatorio:**
- C-statistic (concordance index): interpretacao e limitacoes
- Time-dependent AUC: AUC ao longo do tempo
- Brier Score integrado (IBS)
- Log-partial-likelihood para comparacao de modelos
- AIC para modelos parametricos
- Teste de log-rank e variantes (Wilcoxon, Tarone-Ware)
- Calibracao: predicted vs observed survival

**Pesquisa web:** buscar guias de interpretacao, debates sobre C-index vs td-AUC

### 5. pitfalls.md — Armadilhas e Erros Comuns

**Conteudo obrigatorio:**
- Ignorar censura e tratar como dado completo
- Violar premissa de PH no modelo Cox
- Censura informativa (nao aleatoria)
- Ignorar riscos competitivos quando relevante
- Nao testar proporcionalidade ao longo do tempo
- Usar C-statistic sem considerar horizonte temporal
- Confundir hazard ratio com risco relativo

**Pesquisa web:** buscar case studies de erros em analise de sobrevivencia

---

## Formato de Cada Guia

```markdown
---
slug: survival-<nome>
name: "<Titulo do Guia>"
domain: survival
type: guide
difficulty: intermediate
status: draft
tags: [survival, <tags-especificas>]
references:
  - title: "<titulo>"
    authors: "<autores>"
    year: <ano>
    type: paper
---
```

Cada guia: minimo 1500 palavras, formulas LaTeX, tabelas comparativas, referencias da F1.

---

## Etapas de Implementacao

### Etapa 1: Ler papers.md (F1) e spec do dominio
### Etapa 2: Pesquisa complementar na web
### Etapa 3: Redacao dos 5 guias
### Etapa 4: Verificacao

```bash
ls -la /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/survival/
wc -l /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/survival/*.md
```

---

## Criterios de Aceite

- [x] 5 guias criados: overview.md, models.md, validation.md, metrics.md, pitfalls.md
- [x] Alem dos 5 guias, papers.md da F1 tambem presente no diretorio
- [x] Todos com frontmatter YAML valido (slug, name, domain, type, difficulty, status, tags)
- [x] Cada guia com minimo de 1500 palavras
- [x] Formulas LaTeX incluidas onde necessario (S(t), h(t), hazard ratios)
- [x] Referencias cruzadas aos papers da F1
- [x] Conteudo baseado em pesquisa web
- [x] Tom tecnico e adequado para profissionais de model validation

---

## Ferramentas Necessarias

- **Read**, **WebSearch**, **WebFetch**, **Write**

---

**End of Specification**

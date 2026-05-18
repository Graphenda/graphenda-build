# Fase F3 — Guias Explicativos

**Status**: CONCLUIDO
**Dependencias**: F1 (para referencias dos papers)
**Bloqueia**: F4, F5

---

## Objetivo

Criar 5 guias explicativos completos sobre Generalized Linear Models, cobrindo
desde a visao geral ate armadilhas comuns. Cada guia deve ser autocontido, tecnico
e util para profissionais de model validation.

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/glm/`

---

## Guias a Gerar

### 1. overview.md — Visao Geral de GLMs

**Conteudo obrigatorio:**
- O que sao GLMs e a unificacao de modelos lineares
- Componentes: distribuicao da familia exponencial, link function, preditor linear
- Familias principais: Gaussian, Binomial, Poisson, Gamma, Inverse Gaussian
- Quando usar GLMs vs regressao linear vs ML
- Aplicacoes em credit scoring, seguros, saude e contagem de eventos

**Pesquisa web:** buscar aplicacoes recentes em bancos, seguradoras, fintech

### 2. models.md — Tipos de Modelos GLM

**Conteudo obrigatorio:**
- Regressao Logistica: binomial e multinomial, odds ratio
- Regressao Poisson: contagens, exposure/offset
- Negative Binomial: sobredispersao em contagens
- Zero-Inflated Poisson/NB: excesso de zeros
- Regressao Gamma: dados positivos continuos (custos, sinistros)
- Regressao Tweedie: distribuicao composta para seguros
- GAMs: extensao nao-parametrica com splines

**Pesquisa web:** buscar comparacoes praticas entre familias, exemplos de selecao de modelo

### 3. validation.md — Validacao de GLMs

**Conteudo obrigatorio:**
- Teste de Hosmer-Lemeshow para calibracao (logistica)
- Deviance residuals e Pearson residuals
- Teste de sobredispersao (Poisson vs NB)
- Analise de deviance (ANOVA para GLMs)
- Curva de calibracao (reliability diagram)
- Leverage e influencia em GLMs (hat matrix generalizada)
- Validacao out-of-sample com metricas proprias de cada familia

**Pesquisa web:** buscar melhores praticas de validacao SR 11-7 para logistica/credit scoring

### 4. metrics.md — Metricas e Testes

**Conteudo obrigatorio:**
- AUC-ROC e AUC-PR para classificacao binaria
- Log-loss (cross-entropy) para logistica
- Deviance e pseudo-R² (McFadden, Nagelkerke)
- AIC/BIC para selecao de modelo
- Brier Score para calibracao
- Chi-squared goodness of fit para contagens
- Gini coefficient para credit scoring

**Pesquisa web:** buscar guias de interpretacao, relacao entre Gini e AUC, melhores praticas

### 5. pitfalls.md — Armadilhas e Erros Comuns

**Conteudo obrigatorio:**
- Usar link function inadequada para o problema
- Ignorar sobredispersao em modelos Poisson
- Confundir odds ratio com risco relativo
- Separacao completa em logistica (convergencia falha)
- Nao verificar calibracao alem de discriminacao
- Extrapolar probabilidades fora do range dos dados
- Ignorar multicolinearidade em modelos com muitas variaveis

**Pesquisa web:** buscar case studies de falhas em credit scoring e seguros

---

## Formato de Cada Guia

```markdown
---
slug: glm-<nome>
name: "<Titulo do Guia>"
domain: glm
type: guide
difficulty: intermediate
status: draft
tags: [glm, <tags-especificas>]
references:
  - title: "<titulo>"
    authors: "<autores>"
    year: <ano>
    type: paper
---

# <Titulo>

## Introducao
[Contexto e motivacao — 2-3 paragrafos]

## [Secoes do conteudo]
[Conteudo tecnico com formulas LaTeX quando necessario]

### [Subsecoes]
[Detalhes, exemplos, tabelas comparativas]

## Summary
[Resumo em 3-5 bullet points]

## References
[Lista de referencias usadas]
```

---

## Etapas de Implementacao

### Etapa 1: Leitura de Referencias

- Ler o arquivo `papers.md` gerado na F1 (se disponivel)
- Ler a especificacao completa: `/home/guhaase/projetos/Graphenda/build/docs/model_validation/domains/04-glm.md`

### Etapa 2: Pesquisa Complementar

Para cada guia:
- Buscar na web conteudo complementar aos papers
- Buscar exemplos praticos de credit scoring, seguros, contagens
- Buscar melhores praticas de model validation para GLMs

### Etapa 3: Redacao dos Guias

Para cada guia:
- Redigir com minimo de 1500 palavras
- Incluir formulas LaTeX (link functions, likelihood, deviance)
- Incluir tabelas comparativas (familias, link functions, metricas)
- Referenciar papers da F1
- Tom tecnico mas didatico

### Etapa 4: Salvamento e Verificacao

```bash
ls -la /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/glm/

for f in /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/glm/*.md; do
    echo "=== $(basename $f) ==="
    head -15 "$f"
    echo ""
done

wc -l /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/glm/*.md
```

---

## Criterios de Aceite

- [x] 5 guias criados: overview.md, models.md, validation.md, metrics.md, pitfalls.md
- [x] Alem dos 5 guias, papers.md da F1 tambem presente no diretorio
- [x] Todos com frontmatter YAML valido (slug, name, domain, type, difficulty, status, tags)
- [x] Cada guia com minimo de 1500 palavras
- [x] Formulas LaTeX incluidas onde necessario
- [x] Referencias cruzadas aos papers da F1
- [x] Conteudo baseado em pesquisa web
- [x] Tom tecnico e adequado para profissionais de model validation

---

## Ferramentas Necessarias

- **Read**: para ler papers.md (F1) e a spec do dominio
- **WebSearch**: para pesquisa complementar
- **WebFetch**: para acessar fontes especificas
- **Write**: para criar cada guia

---

**End of Specification**

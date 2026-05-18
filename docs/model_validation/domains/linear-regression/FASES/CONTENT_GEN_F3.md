# Fase F3 — Guias Explicativos

**Status**: CONCLUIDO
**Dependencias**: F1 (para referencias dos papers)
**Bloqueia**: F4, F5

---

## Objetivo

Criar 5 guias explicativos completos sobre regressao linear, cobrindo desde
a visao geral ate armadilhas comuns. Cada guia deve ser autocontido, tecnico
e util para profissionais de model validation.

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/linear-regression/`

---

## Guias a Gerar

### 1. overview.md — Visao Geral de Regressao Linear

**Conteudo obrigatorio:**
- O que e regressao linear e por que ainda e relevante
- OLS como caso base, extensoes (WLS, GLS, Ridge, Lasso)
- Quando usar vs quando nao usar
- Interpretacao de coeficientes
- Relacao com GLM (logistica como extensao)

**Pesquisa web:** buscar aplicacoes recentes, estatisticas de uso em industria financeira

### 2. models.md — Tipos de Modelos de Regressao Linear

**Conteudo obrigatorio:**
- OLS: formulacao, propriedades BLUE, implementacao
- WLS: quando usar, estimacao de pesos
- GLS: correlacao serial, Feasible GLS
- Ridge: bias-variance tradeoff, escolha de lambda
- Lasso: sparsity, selecao de features
- Elastic Net: combinando L1+L2
- Robust Regression: M-estimators, LTS, RANSAC

**Pesquisa web:** buscar comparacoes praticas, benchmarks recentes

### 3. validation.md — Validacao de Modelos Lineares

**Conteudo obrigatorio:**
- Checklist completo de validacao para regressao linear
- Verificacao de premissas (passo a passo)
- Diagnostico de residuos
- Testes formais por premissa
- Validacao out-of-sample
- Analise de sensibilidade de coeficientes
- Cross-validation para selecao de modelo

**Pesquisa web:** buscar melhores praticas de validacao SR 11-7, frameworks de validacao

### 4. metrics.md — Metricas e Testes

**Conteudo obrigatorio:**
- R² e Adjusted R²: interpretacao correta e armadilhas
- RMSE, MAE, MAPE: quando usar cada uma
- F-test: significancia global
- t-test: significancia individual de coeficientes
- AIC/BIC: selecao de modelo
- Mallow's Cp
- VIF: deteccao de multicolinearidade

**Pesquisa web:** buscar guias de interpretacao, erros comuns em metricas

### 5. pitfalls.md — Armadilhas e Erros Comuns

**Conteudo obrigatorio:**
- Confundir correlacao com causalidade
- Ignorar premissas (heteroscedasticidade, nao-normalidade)
- Overfit por excesso de features
- Multicolinearidade nao detectada
- Extrapolacao alem do range dos dados
- R² alto nao significa modelo bom
- Variaveis omitidas e vies de especificacao

**Pesquisa web:** buscar case studies reais de falhas, exemplos da industria

---

## Formato de Cada Guia

```markdown
---
slug: linear-regression-<nome>
name: "<Titulo do Guia>"
domain: linear-regression
type: guide
difficulty: intermediate
status: draft
tags: [linear-regression, <tags-especificas>]
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
- Ler a especificacao completa: `/home/guhaase/projetos/Graphenda/build/docs/model_validation/domains/01-linear-regression.md`

### Etapa 2: Pesquisa Complementar

Para cada guia:
- Buscar na web conteudo complementar aos papers
- Buscar exemplos praticos da industria financeira
- Buscar melhores praticas de model validation

### Etapa 3: Redacao dos Guias

Para cada guia:
- Redigir com minimo de 1500 palavras
- Incluir formulas LaTeX para conceitos matematicos
- Incluir tabelas comparativas quando aplicavel
- Referenciar papers da F1
- Tom tecnico mas didatico

### Etapa 4: Salvamento e Verificacao

```bash
# Verificar que todos os 5 guias existem
ls -la /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/linear-regression/

# Verificar frontmatter de cada um
for f in /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/linear-regression/*.md; do
    echo "=== $(basename $f) ==="
    head -15 "$f"
    echo ""
done

# Verificar tamanho minimo (pelo menos 80 linhas cada)
wc -l /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/linear-regression/*.md
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

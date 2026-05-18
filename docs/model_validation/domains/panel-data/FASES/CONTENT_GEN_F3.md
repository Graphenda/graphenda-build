# Fase F3 — Guias Explicativos

**Status**: CONCLUIDO
**Dependencias**: F1 (para referencias dos papers)
**Bloqueia**: F4, F5

---

## Objetivo

Criar 5 guias explicativos completos sobre dados em painel, cobrindo desde
a visao geral ate armadilhas comuns. Cada guia deve ser autocontido, tecnico
e util para profissionais de model validation.

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/panel-data/`

---

## Guias a Gerar

### 1. overview.md — Visao Geral de Dados em Painel

**Conteudo obrigatorio:**
- O que sao dados em painel e por que sao importantes
- Paineis balanceados vs desbalanceados
- Vantagens sobre cross-section e series temporais puras
- Tipos de modelos: FE, RE, Pooled OLS, Between, First-Difference
- Aplicacoes em financas, economia e ciencias sociais

**Pesquisa web:** buscar aplicacoes recentes em bancos, regulacao financeira, credit risk

### 2. models.md — Tipos de Modelos para Dados em Painel

**Conteudo obrigatorio:**
- Pooled OLS: quando e valido, limitacoes
- Fixed Effects (FE): within estimator, entity e time dummies
- Random Effects (RE): GLS, premissa de exogeneidade
- First-Difference estimator: eliminacao de efeitos fixos
- Between estimator: variacao entre unidades
- Arellano-Bond GMM: paineis dinamicos, instrumentos
- Blundell-Bond System GMM: ganhos de eficiencia sobre Arellano-Bond

**Pesquisa web:** buscar comparacoes praticas, quando usar cada modelo

### 3. validation.md — Validacao de Modelos em Painel

**Conteudo obrigatorio:**
- Teste de Hausman: escolha entre FE e RE
- Teste de Breusch-Pagan Lagrangiano: RE vs Pooled OLS
- Teste F de efeitos fixos: FE vs Pooled OLS
- Testes de autocorrelacao serial (Wooldridge)
- Testes de heteroscedasticidade em painel
- Teste de Sargan/Hansen para validade dos instrumentos (GMM)
- Validacao out-of-sample com paineis

**Pesquisa web:** buscar melhores praticas de validacao em paineis, requisitos regulatorios

### 4. metrics.md — Metricas e Testes Estatisticos

**Conteudo obrigatorio:**
- R² within, between e overall
- Teste F para significancia conjunta
- Criterios de informacao (AIC, BIC) para selecao de modelo
- Teste de Wald para restricoes lineares
- Erros-padrao robustos (cluster, HAC)
- Estatisticas de diagnostico para GMM (AR(1), AR(2), Hansen J)

**Pesquisa web:** buscar guias de interpretacao, erros comuns em metricas de painel

### 5. pitfalls.md — Armadilhas e Erros Comuns

**Conteudo obrigatorio:**
- Ignorar heterogeneidade nao observada
- Usar RE quando efeitos fixos sao correlacionados com regressores
- Vies de Nickell em paineis dinamicos curtos
- Instrumentos fracos em GMM
- Excesso de instrumentos em System GMM
- Nao clusterizar erros-padrao adequadamente
- Attrition e selecao amostral em paineis desbalanceados

**Pesquisa web:** buscar case studies de falhas, exemplos da industria financeira

---

## Formato de Cada Guia

```markdown
---
slug: panel-data-<nome>
name: "<Titulo do Guia>"
domain: panel-data
type: guide
difficulty: intermediate
status: draft
tags: [panel-data, <tags-especificas>]
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
- Ler a especificacao completa: `/home/guhaase/projetos/Graphenda/build/docs/model_validation/domains/02-panel-data.md`

### Etapa 2: Pesquisa Complementar

Para cada guia:
- Buscar na web conteudo complementar aos papers
- Buscar exemplos praticos da industria financeira
- Buscar melhores praticas de model validation para paineis

### Etapa 3: Redacao dos Guias

Para cada guia:
- Redigir com minimo de 1500 palavras
- Incluir formulas LaTeX para conceitos matematicos (within estimator, GLS, GMM)
- Incluir tabelas comparativas quando aplicavel (FE vs RE vs Pooled)
- Referenciar papers da F1
- Tom tecnico mas didatico

### Etapa 4: Salvamento e Verificacao

```bash
# Verificar que todos os 5 guias existem
ls -la /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/panel-data/

# Verificar frontmatter de cada um
for f in /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/panel-data/*.md; do
    echo "=== $(basename $f) ==="
    head -15 "$f"
    echo ""
done

# Verificar tamanho minimo (pelo menos 80 linhas cada)
wc -l /home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/panel-data/*.md
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

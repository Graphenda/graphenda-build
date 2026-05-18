# Model Validation — Estrategia de Conteudo

## Objetivo

Cada dominio do grafo precisa de conteudo rico para que o Build extraia
entidades e relacoes de qualidade. Este documento define a estrutura de
conteudo que cada dominio deve ter.

## Estrutura de Conteudo por Dominio

Cada dominio deve ter um diretorio em `corpus/model_validation/<domain_slug>/`
com os seguintes tipos de conteudo:

```
corpus/model_validation/<domain_slug>/
├── papers/                     # Papers academicos (.pdf)
├── articles/                   # Artigos e noticias (.md, .pdf)
├── guides/                     # Documentos explicativos (.md)
│   ├── overview.md             # Visao geral do dominio
│   ├── models.md               # Modelos e algoritmos
│   ├── validation.md           # Como validar modelos deste dominio
│   ├── metrics.md              # Metricas relevantes
│   └── pitfalls.md             # Erros comuns e como evitar
├── code/                       # Codigo de exemplo (.py)
│   ├── modeling/               # Exemplos de modelagem
│   ├── validation/             # Exemplos de testes e validacao
│   └── visualization/          # Exemplos de graficos
├── reports/                    # Relatorios de validacao (.md, .pdf)
│   ├── template.md             # Template de relatorio de validacao
│   └── examples/               # Exemplos de relatorios completos
└── datasets/                   # Referencias a datasets (nao os dados em si)
    └── references.md           # Links e descricoes de datasets
```

## Tipos de Conteudo

### 1. Papers Academicos (`papers/`)
- Papers seminais que definem o modelo/metodo
- Papers de validacao e comparacao
- Surveys e reviews do dominio
- Formato: PDF
- Minimo: 5-10 papers por dominio

### 2. Artigos e Noticias (`articles/`)
- Artigos tecnicos de blogs (Towards Data Science, Medium, etc.)
- Posts de reguladores (Fed, ECB, NIST)
- Noticias sobre falhas de modelos no dominio
- Formato: Markdown (converter de web)
- Minimo: 5-10 artigos por dominio

### 3. Guias Explicativos (`guides/`)
- Escritos especificamente para o grafo
- Tom: tecnico mas acessivel
- Devem cobrir: o que e, quando usar, como validar, erros comuns
- Formato: Markdown
- Obrigatorio: 5 arquivos base por dominio

### 4. Codigo de Exemplo (`code/`)
- Exemplos reproduziveis em Python
- Devem demonstrar modelagem + validacao + visualizacao
- Usar bibliotecas reais (sklearn, statsmodels, xgboost, etc.)
- Comentarios explicativos detalhados
- Formato: Python (.py)
- Minimo: 3-5 scripts por dominio

### 5. Relatorios de Validacao (`reports/`)
- Templates de relatorio para o dominio
- Exemplos preenchidos com dados sinteticos
- Estrutura: sumario executivo, metodologia, resultados, conclusao
- Formato: Markdown
- Minimo: 1 template + 1 exemplo por dominio

### 6. Referencias de Datasets (`datasets/`)
- Nao armazenar dados — apenas referencias
- Links para datasets publicos relevantes
- Descricao de caracteristicas (tamanho, features, target)

## Prioridade de Criacao

| Prioridade | Dominios | Razao |
|------------|----------|-------|
| P0 | Classification, Anomaly Detection, Linear Regression | Maior demanda regulatoria |
| P1 | Panel Data, Time Series, GLM, Survival | Bancos e seguradoras |
| P2 | Ensemble, LLM, NLP Embeddings | Demanda crescente |
| P3 | Demais dominios | Completude |

## Metricas de Cobertura

Para cada dominio, rastrear:
- [ ] overview.md escrito
- [ ] models.md escrito
- [ ] validation.md escrito
- [ ] metrics.md escrito
- [ ] pitfalls.md escrito
- [ ] 5+ papers coletados
- [ ] 5+ artigos coletados
- [ ] 3+ scripts de modelagem
- [ ] 3+ scripts de validacao
- [ ] 2+ scripts de visualizacao
- [ ] Template de relatorio criado
- [ ] Exemplo de relatorio criado
- [ ] Referencias de datasets listadas

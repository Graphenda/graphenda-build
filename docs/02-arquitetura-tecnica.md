# Arquitetura Tecnica

> Baseada na implementacao real do sistema GraphRAG (panelbox/graphrag).

## Fluxo Principal

```
                  User
                    |
              Natural Query
                    |
                    v
        ┌─── Intent Parser ───┐
        │  (regex + aliases)   │
        │  zero LLM, 100%     │
        │  deterministico      │
        └──────────┬───────────┘
                   │
          ParsedIntent:
          - entities
          - intent_type
          - retrieval_weights
                   │
                   v
    ┌──────────────┼──────────────┐
    │              │              │
    v              v              v
 Graph        Vector        Community
Retriever    Retriever      Retriever
 (Cypher)   (embeddings)    (Leiden)
    │              │              │
    └──────────────┼──────────────┘
                   │
                   v
        ┌──────────────────┐
        │  Context Ranker  │
        │  - normalize     │
        │  - weight        │
        │  - dedup         │
        │  - truncate      │
        └────────┬─────────┘
                 │
                 v
        ┌──────────────────┐
        │ Curation Matcher │
        │ (golden answers) │
        │ bypassa LLM se   │
        │ match encontrado │
        └────────┬─────────┘
                 │
                 v
        ┌──────────────────┐
        │    Claude LLM    │
        │  (apenas escrita │
        │   linguistica)   │
        └────────┬─────────┘
                 │
                 v
           Final Answer
        (streaming WebSocket)
```

## Componentes

### 1. Intent Parser (Query Interpreter)

Classifica a query do usuario **sem usar LLM** - 100% deterministico via regex + dicionario de aliases.

**Output (ParsedIntent):**
- `entities`: entidades extraidas da query
- `intent_type`: VALIDATION | COMPARISON | RECOMMENDATION | EXPLANATION | CODE_EXAMPLE | GENERAL
- `retrieval_weights`: pesos dinamicos para cada estrategia de retrieval

**Pesos por tipo de intent:**

| Intent         | Graph | Vector | Community |
|----------------|-------|--------|-----------|
| VALIDATION     | 0.70  | 0.20   | 0.10      |
| COMPARISON     | 0.50  | 0.30   | 0.20      |
| CODE_EXAMPLE   | 0.30  | 0.60   | 0.10      |
| RECOMMENDATION | 0.30  | 0.40   | 0.30      |
| EXPLANATION    | 0.40  | 0.40   | 0.20      |
| GENERAL        | 0.33  | 0.33   | 0.34      |

**Implementacao:** `src/retrieval/intent_parser.py`

### 2. Ingestion Pipeline (Graph Builder)

Pipeline de 4 estagios que transforma documentos em knowledge graph.

```
Stage 1: Discovery & Chunking
    |  Parsers: Python, Markdown, Notebook
    |  Extrai: docstrings, signatures, type hints, sections
    v
Stage 2: Triple Extraction
    |  Claude API (Haiku) + ontologia
    |  Output: {subject, predicate, object, confidence}
    |  Batch processing (50 chunks por batch)
    v
Stage 3: Entity Resolution
    |  Normalizacao via aliases.yaml
    |  Fuzzy matching (difflib.SequenceMatcher)
    |  Validacao de tipos contra ontologia
    v
Stage 4: Graph Loading
    |  Upsert no Neo4j (MERGE para idempotencia)
    |  Metadata tracking (_PipelineMeta node)
    v
Knowledge Graph (~500 nodes, ~2000 relationships)
```

**Incremental ingestion:** SHA-256 hash por arquivo - pula arquivos nao modificados.

**Implementacao:** `src/ingestion/pipeline.py`, `chunker.py`, `triple_extractor.py`, `entity_resolver.py`

### 3. Ontologia Formal

Definida em YAML (`ontology/panelbox_ontology.yaml`), nao e ad-hoc.

**16 Entity Types:**

| Dominio Econometrico     | Dominio Regulatorio      |
|--------------------------|--------------------------|
| Estimator                | RegulatoryFramework      |
| DiagnosticTest           | CapitalRequirement       |
| Parameter                | RiskMetric               |
| StatisticalConcept       | RegulatoryBody           |
| Literature               | ComplianceProcess        |
| ModelFamily              | LegalArticle             |
| StandardError            |                          |
| Dataset                  |                          |
| CodePattern              |                          |
| ResultMetric             |                          |

**19 Relationship Types:**

| Relacao          | Semantica                         |
|------------------|-----------------------------------|
| BELONGS_TO       | Estimator -> ModelFamily          |
| INHERITS_FROM    | Estimator -> Estimator            |
| VALIDATES        | DiagnosticTest -> Estimator       |
| REQUIRES         | Estimator -> Parameter            |
| PRODUCES         | Estimator -> ResultMetric         |
| ADDRESSES        | Estimator -> StatisticalConcept   |
| TESTS_FOR        | DiagnosticTest -> StatisticalConcept |
| BASED_ON         | Estimator/Test -> Literature      |
| ALTERNATIVE_TO   | Estimator -> Estimator            |
| SUPPORTS_SE      | Estimator -> StandardError        |
| DEMONSTRATED_IN  | Estimator -> Dataset              |
| IMPLEMENTED_BY   | CodePattern -> Estimator          |
| SUCCEEDS         | DiagnosticTest -> DiagnosticTest  |

**Alias Resolution:** `ontology/aliases.yaml` - mapeia variacoes de nomes, abreviacoes e traducoes (PT<->EN).

### 4. Retrieval: 3 Estrategias Paralelas

#### A. Graph Retriever (Structural Traversal)

Busca estrutural via Cypher queries no Neo4j.

- Entry points: entidades do ParsedIntent
- Profundidade maxima: 2 hops (configuravel)
- Score: inversamente proporcional a distancia de hops
- Retorna: nodes, properties, relationships, hop_distance

**Melhor para:** VALIDATION (peso 0.70), COMPARISON (0.50)

**Implementacao:** `src/retrieval/graph_retriever.py`

#### B. Vector Retriever (Semantic Similarity)

Busca semantica via embeddings no Neo4j vector index.

- Modelo: `all-MiniLM-L6-v2` (384 dimensoes)
- Similaridade: cosine distance
- Threshold minimo: 0.5
- Retorna: chunks de texto com score de similaridade

**Melhor para:** CODE_EXAMPLE (peso 0.60), RECOMMENDATION (0.40)

**Implementacao:** `src/retrieval/vector_retriever.py`, `embedder.py`

#### C. Community Retriever (High-Level Context)

Busca por comunidades detectadas via Leiden algorithm.

**Pipeline de comunidades:**
1. **Leiden algorithm** (igraph + leidenalg) - deteccao automatica de clusters
2. **Summarization** - resumos de 3-5 frases por comunidade via Claude (cacheados)
3. **Storage** - community nodes no Neo4j com embeddings dos resumos

**Duas estrategias de busca:**
1. Entity membership: se a entidade tem community_id, retorna a comunidade (score=1.0)
2. Summary similarity: compara embedding da query vs embeddings dos resumos

**Melhor para:** GENERAL (peso 0.34), RECOMMENDATION (0.30)

**Implementacao:** `src/retrieval/community_retriever.py`, `community_detector.py`, `community_summarizer.py`

### 5. Context Ranker (Compressao e Fusao)

Combina os 3 retrievers em contexto comprimido para o LLM.

**Pipeline:**

```
3 listas de resultados
        |
        v
Score Normalization (min-max por estrategia)
        |
        v
Strategy Weighting (pesos do ParsedIntent)
        |
        v
Deduplication (merge por chunk_id, soma scores)
        |
        v
Token Budget Enforcement (max 2K-4K tokens)
        |
        v
Formatting (markdown estruturado)
```

**Metricas rastreadas:**
- `total_input_results` - antes do ranking
- `after_dedup` - apos merge
- `final_count` - apos truncamento
- `total_tokens` - tokens no contexto final
- `strategy_contributions` - contribuicao de cada retriever

**Implementacao:** `src/retrieval/context_ranker.py`

### 6. Curation Matcher (Golden Answers)

Sistema de respostas curadas por humanos que **bypassa o LLM completamente**.

- Tabela `curated_queries` no PostgreSQL com query_pattern, response_text, embedding
- Similaridade minima: 0.85 (configuravel)
- Se match encontrado: retorna resposta curada sem custo de LLM
- Fila `pending_curation` para queries novas aguardando revisao manual

**Implementacao:** `src/retrieval/curation_matcher.py`

### 7. LLM Layer (Interface Linguistica)

Claude recebe o contexto comprimido e gera resposta em linguagem natural.

**Modelo:** Claude Haiku (`claude-haiku-4-5-20251001`) - otimizado para custo

**Uso do LLM no sistema:**

| Etapa              | Usa LLM? | Modelo    | Proposito                    |
|--------------------|----------|-----------|------------------------------|
| Intent parsing     | Nao      | -         | Regex + aliases              |
| Triple extraction  | Sim      | Haiku     | Extrair entidades/relacoes   |
| Community summary  | Sim      | Haiku     | Resumir comunidades (cache)  |
| Response generation| Sim      | Haiku     | Gerar resposta final         |
| Curation match     | Nao      | -         | Golden answers humanas       |

**Streaming:** Token-by-token via WebSocket para UX em tempo real.

**Implementacao:** `src/generation/response_generator.py`, `prompts.py`

## Stack Tecnologico (Implementado)

| Componente         | Tecnologia                              |
|--------------------|-----------------------------------------|
| Graph DB           | Neo4j 5.x (Community/AuraDB)           |
| Relational DB      | PostgreSQL 16                           |
| Backend            | FastAPI (Python 3.10+) + Uvicorn        |
| Frontend           | Next.js 15 (React 19, TypeScript)       |
| LLM                | Claude Haiku (Anthropic API)            |
| Embeddings         | sentence-transformers (all-MiniLM-L6-v2, 384d) |
| Comunidades        | Leiden algorithm (igraph + leidenalg)   |
| ORM                | SQLAlchemy + Alembic (migrations)       |
| Autenticacao       | JWT                                     |
| Deploy             | Docker Compose (dev), Railway (prod)    |

## Estrutura de Codigo

```
src/
├── ingestion/           # Pipeline de dados
│   ├── pipeline.py         (orquestrador 4 estagios)
│   ├── chunker.py          (multi-parser)
│   ├── triple_extractor.py (extracao via Claude)
│   ├── entity_resolver.py  (dedup + normalizacao)
│   ├── parser_python.py
│   ├── parser_markdown.py
│   ├── parser_notebook.py
│   └── prompts.py
├── graph/               # Neo4j
│   ├── connection.py
│   ├── graph_loader.py
│   ├── queries.py          (templates Cypher)
│   ├── schema.py
│   ├── ontology_loader.py
│   └── models.py           (Entity, Relationship)
├── retrieval/           # Multi-strategy retrieval
│   ├── engine.py           (orquestrador unificado)
│   ├── intent_parser.py    (zero LLM)
│   ├── graph_retriever.py
│   ├── vector_retriever.py
│   ├── community_retriever.py
│   ├── community_detector.py
│   ├── community_summarizer.py
│   ├── context_ranker.py
│   ├── curation_matcher.py
│   ├── embedder.py
│   ├── vector_index.py
│   └── models.py
├── generation/          # Geracao de resposta
│   ├── response_generator.py
│   ├── chat.py
│   ├── prompts.py
│   ├── cost_calculator.py
│   └── notebook_builder.py
├── database/            # PostgreSQL + ORM
│   ├── connection.py
│   ├── models.py
│   ├── repositories.py
│   └── migrations/
└── api/                 # FastAPI
    ├── app.py
    ├── routes/
    ├── middleware/
    ├── schemas.py
    └── websocket.py
```

## Otimizacoes de Custo e Performance

| Tecnica                    | Impacto                              |
|----------------------------|--------------------------------------|
| Batch processing (50/batch)| Menos chamadas API na ingestao       |
| Incremental ingestion      | Pula arquivos nao modificados (SHA-256) |
| Community cache            | Resumos gerados uma vez e cacheados  |
| Haiku model                | Custo otimizado vs Sonnet/Opus       |
| Response cache (PostgreSQL)| Queries repetidas sem custo LLM      |
| Curation matcher           | Golden answers bypassa LLM 100%      |
| Token budget (2K-4K)       | Contexto comprimido, nao documentos  |

## Metricas Rastreadas (por mensagem)

- `input_tokens`, `output_tokens`
- `latency_ms` (end-to-end)
- `cost_usd` (calculado por token)
- Timings por estagio: intent_parsing_ms, retrieval_ms, ranking_ms, formatting_ms
- Strategy contributions por retriever

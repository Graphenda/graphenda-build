# Graphenda - Guia Tecnico

Documentacao tecnica para desenvolvedores sobre a arquitetura, extensibilidade
e deploy da Graphenda Cognitive Engine.

---

## 1. Arquitetura

### 1.1 Visao Geral

```
┌─────────────────────────────────────────────────────┐
│                    Frontend (React)                  │
│              Dashboard / Chat / Explorer             │
└──────────────────────┬──────────────────────────────┘
                       │ REST / WebSocket
┌──────────────────────▼──────────────────────────────┐
│                   API Layer (FastAPI)                │
│    Auth │ Chat │ Graph │ Curation │ Analytics        │
│    Middleware: Auth, RateLimit, CORS, Logging        │
└──────────────────────┬──────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────┐
│               Engine Core                            │
│  ┌──────────┐ ┌──────────┐ ┌──────────────────┐    │
│  │ Parsers  │ │Extractors│ │   Retrievers     │    │
│  │ PDF,DOCX │ │ Entity,  │ │ Graph, Vector,   │    │
│  │ TXT, MD  │ │ Relation │ │ Hybrid, Curated  │    │
│  └──────────┘ └──────────┘ └──────────────────┘    │
│  ┌──────────────────────────────────────────────┐   │
│  │         HCG (Hierarchical Cognitive Graph)    │   │
│  │  Community Detection → Levels → Cross-links   │   │
│  └──────────────────────────────────────────────┘   │
└──────────────────────┬──────────────────────────────┘
                       │
       ┌───────────────┼───────────────┐
       │               │               │
┌──────▼──────┐ ┌──────▼──────┐ ┌──────▼──────┐
│  Neo4j      │ │ PostgreSQL  │ │   Redis     │
│ Knowledge   │ │ Users,      │ │ Cache,      │
│ Graph       │ │ Sessions,   │ │ Rate Limit, │
│             │ │ Curations   │ │ Queue       │
└─────────────┘ └─────────────┘ └─────────────┘
```

### 1.2 Fluxo de Dados

**Ingestao:**
1. Documento entra via upload ou trigger
2. Parser extrai texto estruturado
3. Chunker segmenta em blocos semanticos
4. Entity Extractor identifica entidades da ontologia
5. Relationship Extractor identifica relacoes
6. Graph Population insere no Neo4j (merge)
7. Vector Indexing gera embeddings

**Query (Chat):**
1. Intent parsing classifica a pergunta
2. Multi-strategy retrieval busca no grafo e vetores
3. Ranker combina e pontua resultados
4. LLM gera resposta com contexto
5. Cache e curadoria sao verificados

### 1.3 Componentes Core

| Componente | Diretorio | Funcao |
|------------|-----------|--------|
| API | `api/` | Endpoints REST e WebSocket |
| Engine Core | `engine/core/` | Ontologia, config, pipeline |
| Parsers | `engine/parsers/` | Extracao de texto de documentos |
| Extractors | `engine/extractors/` | Extracao de entidades e relacoes |
| Retrievers | `engine/retrievers/` | Estrategias de busca |
| Graph | `engine/graph/` | Conexao e operacoes Neo4j |
| Database | `engine/database/` | Models, repos, migrations (PostgreSQL) |
| HCG | `engine/hierarchy/` | Hierarchical Cognitive Graph |
| Frontend | `frontend/` | React dashboard |

---

## 2. Extensibilidade

### 2.1 Adicionando um Novo Parser

Parsers convertem documentos brutos em texto estruturado.

**Passo 1**: Crie o arquivo em `engine/parsers/`:

```python
# engine/parsers/my_format_parser.py
from engine.parsers.base import BaseParser, ParsedDocument


class MyFormatParser(BaseParser):
    """Parser for .myformat files."""

    supported_extensions = [".myformat"]

    def parse(self, file_path: str) -> ParsedDocument:
        with open(file_path, "r") as f:
            content = f.read()

        return ParsedDocument(
            content=content,
            metadata={"source": file_path, "format": "myformat"},
            chunks=self._chunk(content),
        )

    def _chunk(self, text: str) -> list[str]:
        # Implementar logica de chunking
        return [text[i:i+1000] for i in range(0, len(text), 800)]
```

**Passo 2**: Registre no registry de parsers (se existir) ou garanta que o
pipeline detecte a extensao automaticamente.

### 2.2 Adicionando um Novo Retriever

Retrievers implementam estrategias de busca no grafo e/ou vetores.

```python
# engine/retrievers/my_retriever.py
from engine.retrievers.base import BaseRetriever, RetrievalResult


class MyRetriever(BaseRetriever):
    """Custom retrieval strategy."""

    name = "my_strategy"

    def retrieve(self, query: str, instance, top_k: int = 10) -> list[RetrievalResult]:
        # Implementar logica de busca
        results = []

        # Exemplo: busca customizada
        # ...

        return results
```

Registre no hybrid retriever ou configure via ontologia.

### 2.3 Adicionando um Novo Extractor

Extractors identificam entidades e relacoes em texto.

```python
# engine/extractors/my_extractor.py
from engine.extractors.base import BaseExtractor, ExtractionResult


class MyExtractor(BaseExtractor):
    """Custom entity/relationship extractor."""

    def extract(self, text: str, ontology) -> ExtractionResult:
        entities = []
        relationships = []

        # Implementar logica de extracao
        # ...

        return ExtractionResult(
            entities=entities,
            relationships=relationships,
        )
```

---

## 3. Configuracao do HCG

O Hierarchical Cognitive Graph (HCG) organiza o grafo em niveis hierarquicos
para permitir raciocinio multi-escala.

### 3.1 Niveis Hierarquicos

| Nivel | Nome | Descricao |
|-------|------|-----------|
| 1 | Facts | Entidades atomicas (estimadores, testes, parametros) |
| 2 | Concepts | Conceitos que agrupam fatos (conceitos estatisticos) |
| 3 | Domains | Dominios que agrupam conceitos (familias de modelos) |
| 4 | Systems | Macro-sistemas (opcional, definido pela ontologia) |

Os niveis sao definidos na ontologia via campo `level` em cada entity type.

### 3.2 Propagacao de Contexto

O HCG propaga informacao entre niveis de duas formas:

- **Bottom-up**: Fatos informam conceitos, que informam dominios
- **Top-down**: Contexto de dominio ajuda a desambiguar fatos
- **Bidirectional**: Combinacao de ambos (padrao)

A propagacao e configuravel por ontologia:

```yaml
hierarchy:
  levels:
    - name: "facts"
      description: "Atomic entities"
    - name: "concepts"
      description: "Grouping concepts"
    - name: "domains"
      description: "Domain areas"
  propagation: "bidirectional"
```

### 3.3 Hierarquia Automatica vs Manual

- **Automatica**: O HCG builder usa community detection (Leiden/Louvain) para
  agrupar entidades e criar niveis superiores automaticamente
- **Manual**: Entidades com `level` definido na ontologia respeitam o nivel manual.
  Relacionamentos `cross_level: true` criam links entre niveis

Para rebuild:

```bash
curl -X POST /api/instances/{id}/build-hierarchy \
  -H "Authorization: Bearer <token>"
```

---

## 4. Deploy

### 4.1 Ambiente de Desenvolvimento

```bash
# Clonar repositorio
git clone <repo-url>
cd Graphenda

# Criar ambiente virtual
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Subir dependencias
docker compose up -d neo4j postgres redis

# Rodar migrations
alembic upgrade head

# Iniciar API
uvicorn api.app:app --reload --host 0.0.0.0 --port 8000

# Iniciar frontend
cd frontend && npm install && npm run dev
```

### 4.2 Staging

```bash
# Build das imagens
docker compose -f docker-compose.staging.yml build

# Deploy
docker compose -f docker-compose.staging.yml up -d

# Verificar health
curl http://staging:8000/health
```

### 4.3 Producao

```bash
# Build com profile de producao
docker compose -f docker-compose.prod.yml build

# Deploy com replicas
docker compose -f docker-compose.prod.yml up -d --scale api=3

# Verificar health de todos os servicos
curl http://prod:8000/health
curl http://prod:8000/health/postgres
curl http://prod:8000/health/neo4j
curl http://prod:8000/health/redis
```

Consideracoes para producao:
- Use HTTPS (TLS termination via reverse proxy)
- Configure backups automaticos (ver guia de backup F5.4)
- Configure monitoramento (Prometheus + Grafana, ver F5.3)
- Use rate limiting adequado (`RATE_LIMIT_PER_MINUTE`)
- Habilite CORS apenas para origens confiadas

### 4.4 Variaveis de Ambiente

| Variavel | Descricao | Default |
|----------|-----------|---------|
| `APP_VERSION` | Versao da aplicacao | `1.0.0` |
| `DATABASE_URL` | URL de conexao PostgreSQL | `postgresql+asyncpg://...` |
| `NEO4J_URI` | URI do Neo4j | `bolt://localhost:7687` |
| `NEO4J_USER` | Usuario Neo4j | `neo4j` |
| `NEO4J_PASSWORD` | Senha Neo4j | - |
| `REDIS_URL` | URL do Redis | `redis://localhost:6379` |
| `JWT_SECRET` | Chave secreta para JWT | - |
| `JWT_EXPIRE_MINUTES` | Tempo de expiracao do token | `60` |
| `CORS_ORIGINS` | Origens CORS permitidas | `["http://localhost:3000"]` |
| `RATE_LIMIT_PER_MINUTE` | Limite de requests por minuto | `60` |
| `LOGIN_RATE_LIMIT_PER_MINUTE` | Limite de tentativas de login | `10` |
| `OPENAI_API_KEY` | Chave da API OpenAI (para LLM) | - |
| `EMBEDDING_MODEL` | Modelo de embeddings | `text-embedding-3-small` |

---

## 5. API Reference

A documentacao completa da API esta disponivel em:

- **Swagger UI**: `http://<host>:8000/docs`
- **ReDoc**: `http://<host>:8000/redoc`
- **OpenAPI JSON**: `http://<host>:8000/openapi.json`

A API suporta dois metodos de autenticacao:
- **JWT**: Token obtido via `POST /auth/login`
- **API Key**: Chave no formato `Bearer gph_...` no header Authorization

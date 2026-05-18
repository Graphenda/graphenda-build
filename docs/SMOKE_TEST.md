# Smoke test end-to-end — graphenda-build

Valida que `graphenda-build` funciona como repo independente: sobe Neo4j,
carrega a ontologia `panelbox` em um grafo real e publica o YAML correspondente
em `graphenda-registry/`.

Procedimento da subfase F4.2.

---

## Pre-requisitos

- Docker + Docker Compose v2 instalados
- Repo irmao `graphenda-registry/` presente em `../graphenda-registry`
  e `graphenda-shared/` em `../graphenda-shared` (instalavel via `pip install -e`)
- Venv com `graphenda-build` e `graphenda-shared` instalados editaveis:
  ```bash
  pip install -e ../graphenda-shared
  pip install -e ".[dev,test]"
  ```
- Arquivo `.env` em `graphenda-build/` (copiar de `.env.example`).
  Para o caminho seed-based (default), `ANTHROPIC_API_KEY` pode ficar vazia.
  Para o caminho LLM-based (full ingestion), preencher a chave.

---

## Caminho 1 — Seed-based (sem custo de LLM, recomendado para CI)

Usa `panelbox/seed_entities.yaml` (162 entidades + 212 relacionamentos ja extraidos).
Nao chama Anthropic. E o caminho default deste smoke test.

```bash
cd graphenda-build

# 1. Subir Neo4j
docker compose up -d neo4j
# aguardar healthcheck (~15s)
until [ "$(docker inspect -f '{{.State.Health.Status}}' graphenda-build-neo4j)" = "healthy" ]; do sleep 2; done

# 2. Criar instancia + carregar seed
set -a; source .env; set +a
python scripts/create_instance.py \
    --name panelbox \
    --ontology panelbox \
    --seed \
    --strategy prefix

# 3. Verificar Neo4j
docker exec graphenda-build-neo4j cypher-shell -u neo4j -p "${NEO4J_PASSWORD}" \
    "MATCH (n) RETURN count(n) AS nodes;"
# esperar: 162

# 4. Publicar no registry
python - <<'PY'
from graphenda_shared.registry.models import (
    GraphRegistryEntry, GraphStatus, GraphMetrics, GraphDomainConfig, GraphThresholds,
)
from graphenda_build.registry.publisher import RegistryPublisher

entry = GraphRegistryEntry(
    slug="panelbox",
    name="PanelBox",
    description="Biblioteca PanelBox para econometria de dados em painel",
    version="1.0",
    status=GraphStatus.BUILDING,
    neo4j_database="panelbox",
    ontology="panelbox",
    hierarchy_levels=4,
    metrics=GraphMetrics(nodes=162, edges=212, communities=0,
                         avg_confidence=1.0, coverage=1.0),
    retrievers=["graph", "curated"],
    domain=GraphDomainConfig(
        color="#1F77B4", icon="chart-line", category="econometrics",
        tags=["panel-data", "econometrics", "estimators", "diagnostics"],
    ),
    thresholds=GraphThresholds(min_confidence=0.7, min_nodes_for_active=100,
                               curation_review_days=30),
)
print(RegistryPublisher().publish(entry, force=True))
PY

# 5. Validar e commitar no registry
cd ../graphenda-registry
python validate.py .
git add panelbox.yaml
git commit -m "publish: panelbox via graphenda-build smoke test"

# 6. Teardown
cd ../graphenda-build
docker compose down -v
```

---

## Caminho 2 — LLM-based (full ingestion, requer ANTHROPIC_API_KEY)

Roda a extracao de triples via Claude sobre um corpus de codigo-fonte do PanelBox.
Custo monetario nao-zero — usar com criterio.

```bash
# Pre-requisito adicional: corpus de fontes em ./documentos/panelbox/
set -a; source .env; set +a
python scripts/create_instance.py --name panelbox --ontology panelbox --strategy prefix
python scripts/ingest.py \
    --instance panelbox \
    --ontology panelbox \
    --source ./documentos/panelbox/ \
    --file-types .py .md
# resto identico ao Caminho 1 (publish, validate, commit, teardown)
```

---

## Resultados esperados

| Etapa | Resultado |
|-------|-----------|
| Neo4j healthcheck | `healthy` em < 30s |
| `create_instance --seed` | exit 0, "Nodes: 162, Relationships: 212" |
| Cypher count(n) | `162` |
| `panelbox.yaml` em registry | criado, validado pelo `validate.py` |
| `git commit` no registry | exit 0, 1 file changed |

---

## Modos de falha conhecidos

**Neo4j Community + `--strategy database`**
Comandos `CREATE DATABASE` / `DROP DATABASE` exigem Enterprise.
Usar sempre `--strategy prefix` em ambientes Community (default deste repo).

**`ModuleNotFoundError: graphenda_build.scripts`**
Os console-scripts em `pyproject.toml` apontam para `graphenda_build.scripts.*`,
mas `scripts/` esta no nivel raiz, nao como submodulo. Workaround:
invocar `python scripts/create_instance.py` diretamente. Correcao definitiva
sera movida para uma subfase futura (mover scripts para o pacote OU corrigir
o mapping no pyproject).

**`ANTHROPIC_API_KEY` ausente**
Bloqueia apenas o Caminho 2. Caminho 1 (seed) funciona sem chave.

**Portas 7474/7687 ocupadas**
`docker compose logs neo4j` mostra bind failure. Encerrar processos
concorrentes ou editar `docker-compose.yml`.

---

## Evidencia

Log completo do ultimo run executado: `/tmp/graphenda-build-e2e.log`.

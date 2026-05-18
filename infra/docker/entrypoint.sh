#!/bin/bash
set -euo pipefail

: "${NEO4J_URI:?NEO4J_URI nao definida}"
: "${NEO4J_USER:?NEO4J_USER nao definida}"
: "${NEO4J_PASSWORD:?NEO4J_PASSWORD nao definida}"

for i in 1 2 3 4 5; do
    if python -c "from neo4j import GraphDatabase; GraphDatabase.driver('${NEO4J_URI}', auth=('${NEO4J_USER}', '${NEO4J_PASSWORD}')).verify_connectivity()" 2>/dev/null; then
        echo "[entrypoint] Neo4j OK"
        break
    fi
    echo "[entrypoint] aguardando Neo4j ($i/5)..."
    sleep 3
done

exec "$@"

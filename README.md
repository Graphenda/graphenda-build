# graphenda-build

<!-- TODO: substituir USER/graphenda-build pelo remoto Git real (decisao #2 do PLANO-DIVISAO-EM-PROJETOS.md) -->
[![CI](https://github.com/USER/graphenda-build/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/USER/graphenda-build/actions/workflows/ci.yml)

Motor offline de construção de grafos de conhecimento do Graphenda (Pilar 1).

`graphenda-build` lê ontologias e fontes textuais, executa extração via LLM
(provider configurável — Anthropic, OpenAI-compatible, Gemini, Ollama, ou endpoint
corporativo `/chatCompletion`), monta a hierarquia de comunidades e materializa o
resultado em Neo4j. É um processo **batch**: roda quando você precisa construir ou
reconstruir um grafo.

## Quando usar

- Geração inicial de um grafo a partir de uma ontologia registrada em `graphenda-registry`.
- Reconstrução de grafos após mudança de ontologia, modelo ou fontes.
- Backfill de hierarquia / comunidades / métricas de qualidade.

## Quando NÃO usar

- **Consultas runtime / API online** — esse papel é do `graphenda-saas` (Pilar 2).
- Acesso transacional ao grafo por usuário final.
- Streaming / eventos em tempo real.

## Pré-requisitos

- Python 3.11+
- Neo4j 5.x (local via Docker ou remoto)
- Docker (opcional, recomendado para Neo4j local)
- `graphenda-shared` instalável (vem como dependência do pyproject)

## Instalação

```bash
pip install -e ".[dev,test]"
```

## Rodar Neo4j local

```bash
docker compose up -d neo4j
```

## Ingerir uma ontologia

```bash
python -m graphenda_build.scripts.ingest --ontology panelbox
```

Outras ontologias suportadas: `ai_governance`, `model_intelligence`, `model_validation`,
`bias_intelligence`.

## LLM providers

O provider de LLM é selecionado por env var (`GRAPHENDA_LLM_PROVIDER`). Suportados:

| Provider | Env vars necessárias | Dependência extra |
|---|---|---|
| `anthropic` (default) | `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL` | (já no core) |
| `openai`, `deepseek`, `groq`, `openrouter`, `lmstudio`, `vllm` | `OPENAI_API_KEY`, opcionalmente `OPENAI_BASE_URL`, `OPENAI_MODEL` | `pip install -e ".[openai]"` |
| `gemini` | `GEMINI_API_KEY`, `GEMINI_MODEL` | `pip install -e ".[gemini]"` |
| `ollama` | `OLLAMA_BASE_URL` (default `http://localhost:11434`), `OLLAMA_MODEL` | (já no core via httpx) |
| `internal-llm` | `INTERNAL_LLM_ENDPOINT`, `INTERNAL_LLM_USER_UUID` | (já no core via httpx) |
| `internal-llm-agentic` | mesmas do `internal-llm` (acresce trimming de contexto 128k) | (já no core via httpx) |

Os presets de OpenAI-compatible já preenchem `base_url` automaticamente — para apontar
para outro endpoint, basta setar `OPENAI_BASE_URL`.

Exemplo: rodar a ingestão com o endpoint corporativo:

```bash
export GRAPHENDA_LLM_PROVIDER=internal-llm-agentic
export INTERNAL_LLM_ENDPOINT=http://localhost:5001/chatCompletion
export INTERNAL_LLM_USER_UUID=00000000-0000-0000-0000-000000000000
python scripts/ingest.py --instance minha_inst --ontology model_intelligence --source ./docs
```

Para instalar todos os SDKs opcionais de uma vez:

```bash
pip install -e ".[all-llm]"
```

Ver `.env.example` para o contrato completo das env vars.

## Imagem Docker

O `Dockerfile.build` (em `infra/docker/Dockerfile.build`) gera uma imagem
auto-suficiente baseada em `python:3.11-slim`. Ela instala `graphenda-shared` via
URL Git, instala o próprio pacote e expõe o entrypoint `python -m
graphenda_build.scripts`. As envs `GRAPHENDA_REGISTRY_PATH` e
`GRAPHENDA_ONTOLOGIES_PATH` já vêm definidas; `entrypoint.sh` valida `NEO4J_URI`,
`NEO4J_USER`, `NEO4J_PASSWORD` e aguarda o Neo4j responder antes de delegar
para o comando.

### Limitação no build local

O `pyproject.toml` declara `graphenda-shared` como
`git+file:///home/guhaase/projetos/Graphenda/graphenda-shared@v0.1.0`. Esse
caminho **não existe dentro do container** (o filesystem do build é isolado), então
um `docker build` local falha ao resolver a dependência.

Para construir localmente é preciso adaptar a dependência para um path montado
(por exemplo `graphenda-shared @ file:///shared` mais um volume `-v
/home/guhaase/projetos/Graphenda/graphenda-shared:/shared` via `docker-compose`,
configurado em F3.2). Em CI/prod a URL `git+file://` será substituída pela URL
remota do repositório (GitHub/GitLab) — TODO marcado em F4.3.

## Contrato com `graphenda-registry`

`graphenda_build.registry.publisher` escreve no caminho apontado pela env
`GRAPHENDA_REGISTRY_PATH` (default: `../graphenda-registry/`). Esse diretório deve ser um
clone do repo `graphenda-registry` — o publisher só grava YAMLs; commits e tags ficam a
cargo do operador do registry.

## Documento mestre

Decisões de arquitetura, contratos entre repos e mapeamento file-by-file da divisão estão
em [`../PLANO-DIVISAO-EM-PROJETOS.md`](../PLANO-DIVISAO-EM-PROJETOS.md).

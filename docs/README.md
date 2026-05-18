# Graphenda Build — Documentacao Tecnica

Documentacao tecnica do **motor de construcao** (Build). Cobre arquitetura do
engine, especificacao de ontologias, algoritmo Hierarchical Cognitive Graph
(HCG), desafios tecnicos e o dominio de Model Validation. Docs estrategicos
(visao, mercado, roadmap, produtos) vivem no repo `graphenda-saas`.

---

## Indice

### Guias do motor
- [guide.md](guide.md) — Guia de construcao de grafos com o Build (overview do pipeline, CLI, ontologia, ingestion, extracao, comunidades).
- [technical-guide.md](technical-guide.md) — Guia tecnico para desenvolvedores: arquitetura, extensibilidade e deploy.
- [ontology-format-spec.md](ontology-format-spec.md) — Especificacao formal do formato YAML das ontologias.

### Arquitetura e algoritmo
- [02-arquitetura-tecnica.md](02-arquitetura-tecnica.md) — Arquitetura tecnica do motor GraphRAG (parser, retrievers, fluxo).
- [03-hierarchical-cognitive-graph.md](03-hierarchical-cognitive-graph.md) — Especificacao do Hierarchical Cognitive Graph (HCG), evolucao futura do motor.
- [08-desafios-tecnicos.md](08-desafios-tecnicos.md) — Desafios tecnicos do motor (extracao, escalabilidade, qualidade).

### Dominio: Model Validation
- [model_validation/](model_validation/) — Estrategia de conteudo e ontologias por subdominio (anomaly-detection, bayesian, causal-inference, classification, clustering, deep-learning-*, GLM, graph-models, LLM, NLP, optimization, panel-data, recommender, regression-ml, reinforcement-learning, simulation, survival, time-series).

---

## Decisoes "vem ou nao vem"

Mapeamento de capitulos da pasta `docs/` do monorepo original; um por linha,
seguindo Decisao #4 do `PLANO-DIVISAO-EM-PROJETOS.md`.

| Capitulo origem                              | Destino  | Justificativa (1 linha)                                           |
|----------------------------------------------|----------|-------------------------------------------------------------------|
| `docs/01-visao-geral.md`                     | SaaS     | Visao geral do produto / posicionamento estrategico.              |
| `docs/02-arquitetura-tecnica.md`             | **Build**| Arquitetura tecnica do motor GraphRAG (parser, retrievers).       |
| `docs/03-hierarchical-cognitive-graph.md`    | **Build**| Especificacao do HCG, evolucao futura do motor.                   |
| `docs/04-produtos.md`                        | SaaS     | Catalogo de produtos e oferta comercial.                          |
| `docs/05-mercado-e-clientes.md`              | SaaS     | Mercado, ICP e clientes-alvo.                                     |
| `docs/06-estrategia-de-negocio.md`           | SaaS     | Estrategia de negocio, monetizacao, go-to-market.                 |
| `docs/07-vantagem-competitiva.md`            | SaaS     | Posicionamento competitivo e moats de negocio.                    |
| `docs/08-desafios-tecnicos.md`               | **Build**| Desafios tecnicos do pipeline de construcao do grafo.             |
| `docs/09-roadmap.md`                         | SaaS     | Roadmap de produto.                                               |
| `docs/VISIO/`                                | SaaS     | Diagramas Visio de visao executiva.                               |
| `docs/guides/ontology-format-spec.md`        | **Build**| Especificacao do formato YAML que o motor consome.                |
| `docs/guides/technical-guide.md`             | **Build**| Guia tecnico para desenvolvedores do motor.                       |
| `docs/guides/usage-guide.md`                 | SaaS     | Guia de uso para cliente final via API/UI do SaaS.                |
| `build/docs/guide.md`                        | **Build**| Guia proprio do motor (ja vivia em `build/`).                     |
| `build/docs/model_validation/`               | **Build**| Conteudo de dominio consumido pelo motor (ontologias).            |

Observacao: `docs/ENGINE/` nao existia no monorepo origem; entrada do spec
mantida apenas para referencia futura.

---

## Versao

Esta documentacao reflete o estado do motor no momento da divisao do monorepo
(`graphenda-build/` extraido de `graphenda/build/` + docs do motor).

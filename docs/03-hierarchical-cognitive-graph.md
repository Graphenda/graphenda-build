# Hierarchical Cognitive Graph (HCG)

> STATUS: **Nao implementado.** Este documento descreve uma evolucao futura
> da arquitetura GraphRAG atual (panelbox/graphrag).

## Conceito

Um grafo com **camadas cognitivas explicitas** que organiza conhecimento em multiplos niveis,
permitindo raciocinio **top-down** (do nivel mais abstrato ao mais especifico).

Diferente do sistema atual, onde os niveis sao **emergentes e implicitos**,
o HCG torna a hierarquia uma propriedade **explicita** do grafo.

## O que ja existe vs o que o HCG adicionaria

### Sistema Atual (panelbox/graphrag)

O sistema atual tem elementos que **se parecem** com niveis hierarquicos,
mas **nao sao tratados como hierarquia**:

| Elemento existente        | Funciona como        | Mas falta                           |
|---------------------------|----------------------|-------------------------------------|
| Entidades + relacoes      | ~Facts               | Nao tem propriedade `level`         |
| StatisticalConcept nodes  | ~Concepts            | Nao sao tratados como camada acima  |
| ModelFamily + Leiden       | ~Domains             | Nao ha navegacao hierarquica        |
| Community summaries       | ~Knowledge Systems   | Nao ha raciocinio top-down          |

**Problema:** Os 3 retrievers (Graph, Vector, Community) buscam em **paralelo e independente**.
Nao existe raciocinio que **desça** do nivel mais abstrato ao mais concreto.

### HCG: O que mudaria

Cada node teria um nivel explicito e o raciocinio seria **hierarquico e direcionado**.

```
Level 4: Knowledge Systems    (macro-dominios)
           |
           v  raciocinio top-down
Level 3: Domains              (familias, comunidades)
           |
           v
Level 2: Concepts             (conceitos abstratos)
           |
           v
Level 1: Facts                (entidades especificas, relacoes)
```

## Estrutura Proposta

### Level 1 - Facts

Entidades especificas com propriedades detalhadas. **Ja existem no sistema atual.**

```
Estimator: FixedEffects  [level=1]
  |-- REQUIRES --> Parameter: entity_effects
  |-- PRODUCES --> ResultMetric: R²
  |-- SUPPORTS_SE --> StandardError: ClusteredSE

DiagnosticTest: HausmanTest  [level=1]
  |-- VALIDATES --> Estimator: FixedEffects
  |-- TESTS_FOR --> StatisticalConcept: Endogeneity
```

### Level 2 - Concepts

Conceitos abstratos que agrupam facts. **Parcialmente existem** como `StatisticalConcept`.

```
StatisticalConcept: Endogeneity  [level=2]
  ← TESTS_FOR ── HausmanTest [level=1]
  ← ADDRESSES ── FixedEffects [level=1], IV [level=1]
```

**O que falta:** tratar esses nodes explicitamente como "nivel acima" e usar isso no retrieval.

### Level 3 - Domains

Agrupamentos tematicos. **Parcialmente existem** como ModelFamily e comunidades Leiden.

```
ModelFamily: StaticModels  [level=3]
  ← BELONGS_TO ── FixedEffects [level=1], RandomEffects [level=1]

Community: "GMM & Dynamic Models"  [level=3]
  Members: DifferenceGMM [level=1], SystemGMM [level=1]
  Summary: "Cluster focado em estimadores dinamicos..."
```

**O que falta:** unificar ModelFamily e comunidades Leiden como um unico nivel de dominio.

### Level 4 - Knowledge Systems

Nivel macro que agrupa dominios inteiros. **Nao existe no sistema atual.**

```
KnowledgeSystem: Panel Econometrics  [level=4]
  ← PART_OF ── StaticModels [level=3], GMM [level=3]

KnowledgeSystem: Regulatory Compliance  [level=4]
  ← PART_OF ── BaselFramework [level=3], RiskMetrics [level=3]
```

Poderia ser implementado como **meta-communities** (comunidades de comunidades).

## Raciocinio Top-Down (a grande mudanca)

### Sistema atual: busca paralela

```
Query
  |
  ├── Graph Retriever ──── busca Level 1 (facts)
  ├── Vector Retriever ─── busca Level 1 (chunks)
  └── Community Retriever ─ busca Level 3-4 (summaries)
  |
  v
Context Ranker (merge + weight)
```

Os retrievers **nao se comunicam entre si** e nao ha direcionamento hierarquico.

### HCG proposto: raciocinio direcionado

```
Query: "How to detect bias in credit models?"
  |
  v
Level 4: Qual Knowledge System?
  → "AI Governance" (alta similaridade)
  |
  v
Level 3: Qual Domain dentro de AI Governance?
  → Community "Model Fairness" (match)
  |
  v
Level 2: Quais Concepts nessa community?
  → StatisticalConcept: ProxyVariables, BiasRisk
  |
  v
Level 1: Quais Facts conectados?
  → Feature:ZipCode --proxy_for--> Race
  → DiagnosticTest:FairnessTest --validates--> CreditModel
  |
  v
Contexto ultra-comprimido → LLM
```

**Vantagem:** Cada nivel **filtra** o proximo, reduzindo drasticamente o espaco de busca.

## Compressao Hierarquica

| Nivel | O que envia ao LLM | Tokens (exemplo) |
|-------|---------------------|-------------------|
| RAG tradicional | Documentos completos | ~1200 tokens |
| Level 1 only (atual) | Nos + relacoes | ~200 tokens |
| HCG top-down | Caminho hierarquico filtrado | ~60-100 tokens |

## O que precisa ser implementado

### 1. Propriedade `level` nos nodes
```cypher
MATCH (n) SET n.level = CASE
  WHEN n:Estimator OR n:DiagnosticTest OR n:Parameter THEN 1
  WHEN n:StatisticalConcept OR n:RiskMetric THEN 2
  WHEN n:ModelFamily OR n:Community THEN 3
  WHEN n:KnowledgeSystem THEN 4
END
```

### 2. Relacoes inter-nivel
Novas relacoes explicitas:
- `ABSTRACTS`: Level 2 → Level 1 (conceito abstrai fatos)
- `GROUPS`: Level 3 → Level 2 (dominio agrupa conceitos)
- `PART_OF`: Level 4 → Level 3 (knowledge system contem dominios)

### 3. Hierarchical Retriever (novo retriever)
Substituiria ou complementaria os 3 retrievers atuais:
```python
class HierarchicalRetriever:
    def retrieve(self, query):
        # 1. Encontra Knowledge System relevante (Level 4)
        system = self.find_system(query)
        # 2. Filtra Domains dentro do system (Level 3)
        domains = self.get_domains(system)
        # 3. Filtra Concepts dentro dos domains (Level 2)
        concepts = self.get_concepts(domains)
        # 4. Extrai Facts conectados aos concepts (Level 1)
        facts = self.get_facts(concepts)
        # 5. Monta contexto comprimido
        return self.compress(system, domains, concepts, facts)
```

### 4. Meta-communities (Level 4)
Rodar Leiden com resolution mais baixa sobre os community summaries
para gerar agrupamentos de comunidades.

## Beneficios esperados

1. **Reducao de busca** - Cada nivel filtra o proximo, menos nodes visitados
2. **Mais determinismo** - Caminho hierarquico e mais previsivel que 3 buscas paralelas
3. **Explicabilidade nativa** - A resposta inclui o caminho: System → Domain → Concept → Fact
4. **Compressao extrema** - Contexto filtrado hierarquicamente usa menos tokens
5. **Escalabilidade** - Grafos grandes sao gerenciaveis quando organizados em niveis

## Produto: Graphenda Cognitive Engine

O HCG e o diferencial tecnico central do **Graphenda Cognitive Engine**.

Enquanto a maioria dos sistemas GraphRAG faz busca "flat" (todos os nodes iguais),
o Cognitive Engine faz **raciocinio hierarquico estruturado** - similar a como
especialistas humanos pensam: do geral para o especifico.

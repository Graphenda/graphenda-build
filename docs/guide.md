# Graphenda Build — Guia de Construcao de Grafos

## O que e o Graphenda Build

O Graphenda Build e a engine de construcao automatizada de grafos de conhecimento.
Dado um conjunto de documentos e uma **ontologia**, ele extrai entidades, relacoes
e hierarquias, carregando tudo em um grafo Neo4j pronto para consumo pelo SaaS.

```
Documentos (.py, .md, .pdf, .csv, .ipynb)
    |
    v
Ontologia (YAML) → define O QUE extrair
    |
    v
Pipeline: Chunking → Extracao (LLM) → Resolucao → Neo4j
    |
    v
Hierarquia: Levels → Communities → Knowledge Systems
    |
    v
Registry: Publicar grafo para o SaaS
```

---

## Pre-requisitos

```bash
# Python 3.11+
# Neo4j 5.0+ rodando (local ou Docker)

# Instalar pacotes
cd /home/guhaase/projetos/Graphenda
pip install -e shared/ -e build/

# Variavel de ambiente obrigatoria
export ANTHROPIC_API_KEY="sk-ant-..."

# Variaveis opcionais (defaults funcionam para dev local)
export NEO4J_URI="bolt://localhost:7687"
export NEO4J_USER="neo4j"
export NEO4J_PASSWORD="password"
```

---

## Fluxo Completo em 3 Passos

### Passo 1: Criar instancia

```bash
cd /home/guhaase/projetos/Graphenda/build

python scripts/create_instance.py \
    --name model_intelligence \
    --ontology model_intelligence \
    --seed
```

Isso faz:
- Cria database `model_intelligence` no Neo4j
- Aplica constraints e indexes baseados na ontologia
- Carrega seed entities (entidades iniciais definidas na ontologia)

Flags uteis:
- `--seed` — carrega entidades iniciais da ontologia
- `--drop` — remove instancia existente antes de criar (cuidado!)
- `--strategy prefix` — usa prefixing em vez de database separado (Neo4j Community)

### Passo 2: Ingerir documentos

```bash
python scripts/ingest.py \
    --instance model_intelligence \
    --ontology model_intelligence \
    --source ./meus_documentos/ \
    --file-types .md .pdf .py
```

Isso faz:
- Descobre e parseia todos os arquivos nos diretorios fonte
- Quebra em chunks semanticos (com cache incremental)
- Envia cada chunk para o Claude com a ontologia injetada no prompt
- O LLM extrai triples (sujeito, relacao, objeto) validados contra a ontologia
- Resolve nomes de entidades usando aliases (fuzzy matching 85%)
- Carrega entidades e relacoes no Neo4j

Flags uteis:
- `--dry-run` — extrai triples mas nao carrega no Neo4j (para testar)
- `--full` — ignora cache e reprocessa tudo
- `--batch-size 20` — ajustar batch de extracao (default: 50)
- `--model claude-sonnet-4-20250514` — modelo LLM

Exemplo com multiplos diretorios:
```bash
python scripts/ingest.py \
    --instance model_intelligence \
    --ontology model_intelligence \
    --source ./papers/ ./codigo/ ./docs/ \
    --file-types .pdf .py .md
```

### Passo 3: Construir hierarquia

```bash
python scripts/build_hierarchy.py \
    --ontology model_intelligence
```

Isso faz:
- Atribui levels (1-4) a todos os nodes baseado na ontologia
- Cria relacoes inter-nivel (ABSTRACTS, GROUPS)
- Detecta communities via algoritmo Leiden
- Constroi meta-communities (Knowledge Systems, Level 4)

Flags uteis:
- `--instance nome` — se o database tem nome diferente da ontologia
- `--skip-communities` — pular deteccao de communities
- `--skip-meta` — pular meta-communities (Level 4)
- `--resolution 0.5` — ajustar granularidade do Leiden

---

## Uso via Python (Programatico)

```python
from pathlib import Path
from graphenda_shared.graph.connection import Neo4jConnection
from graphenda_build.ontology.manager import OntologyRegistry
from graphenda_build.ingestion.pipeline import IngestPipeline
from graphenda_build.graph.loader import GraphLoader

# Carregar ontologia
registry = OntologyRegistry(Path("build/ontologies"))
ontology = registry.load("model_intelligence")

# Conectar ao Neo4j
neo4j = Neo4jConnection(database="model_intelligence")

# Pipeline completo (documentos → Neo4j)
pipeline = IngestPipeline(ontology=ontology, neo4j=neo4j)
stats = pipeline.run(
    source_dirs=[{"path": "./meus_docs/", "file_types": [".md", ".py"]}]
)
print(pipeline.get_report())

# Ou apenas extrair triples sem carregar
pipeline_dry = IngestPipeline(ontology=ontology)  # sem neo4j
pipeline_dry.run(
    source_dirs=[{"path": "./meus_docs/", "file_types": [".md"]}],
    dry_run=True,
)
for t in pipeline_dry.get_triples()[:5]:
    print(f"{t.subject} --[{t.predicate}]--> {t.object}")
```

---

## O que sao Ontologias

Uma ontologia e a **configuracao** que diz ao Build o que extrair dos documentos.
Ela define:

1. **Entity types** — quais tipos de entidade existem no dominio
2. **Relationships** — como essas entidades se relacionam
3. **Hierarchy levels** — qual nivel hierarquico cada tipo ocupa (1-4)
4. **Aliases** — nomes alternativos para entidades (para resolucao)
5. **Seed entities** — entidades iniciais pre-carregadas

A ontologia e o que torna o Build **domain-agnostic**: o mesmo codigo funciona
para qualquer area do conhecimento. Trocar a ontologia muda completamente
o que e extraido.

### Hierarquia de 4 Niveis (HCG)

```
Level 4 — Knowledge Systems    (mais abstrato)
Level 3 — Domains
Level 2 — Concepts
Level 1 — Facts                (mais concreto)
```

Cada entity type na ontologia tem um `level` que define onde ele aparece
na hierarquia cognitiva:

- **Level 1 (Facts):** Entidades concretas, atomicas. Ex: `FixedEffects`, `HausmanTest`
- **Level 2 (Concepts):** Conceitos abstratos que agrupam fatos. Ex: `Heteroscedasticity`, `Endogeneity`
- **Level 3 (Domains):** Dominios que agrupam conceitos. Ex: `PanelDataModels`, `CrossSectionModels`
- **Level 4 (Systems):** Gerados automaticamente via clustering de communities

### Relacoes Inter-nivel

O Build cria automaticamente relacoes derivadas entre niveis:

| Relacao | De → Para | Semantica | Exemplo |
|---------|-----------|-----------|---------|
| `ABSTRACTS` | L2 → L1 | Conceito abstrai fatos | `Endogeneity` abstrai `FixedEffects` |
| `GROUPS` | L3 → L2 | Dominio agrupa conceitos | `PanelDataModels` agrupa `Autocorrelation` |
| `PART_OF` | L4 → L3 | Sistema contem dominios | Gerado por meta-communities |

---

## Estrutura de uma Ontologia

Cada ontologia fica em `build/ontologies/<nome>/` com estes arquivos:

```
build/ontologies/model_intelligence/
├── ontology.yaml          # Definicao principal (obrigatorio)
├── aliases.yaml           # Nomes alternativos (opcional)
├── seed_entities.yaml     # Entidades iniciais (opcional)
└── hierarchy.yaml         # Config extra de hierarquia (opcional)
```

### ontology.yaml (obrigatorio)

Define entity types, seus levels, propriedades e relationship types.

```yaml
name: model_intelligence
version: "1.0"
description: "Modelos de risco, econometria de painel e validacao"

entity_types:
  # Level 1 — Facts (entidades concretas)
  Estimator:
    level: 1
    properties:
      name: { type: str, required: true }
      module_path: { type: str }
      description: { type: str }
      assumptions: { type: str }

  DiagnosticTest:
    level: 1
    properties:
      name: { type: str, required: true }
      null_hypothesis: { type: str }

  # Level 2 — Concepts (conceitos abstratos)
  StatisticalConcept:
    level: 2
    properties:
      name: { type: str, required: true }
      description: { type: str }
      formal_definition: { type: str }

  # Level 3 — Domains (agrupamentos)
  ModelFamily:
    level: 3
    properties:
      name: { type: str, required: true }
      description: { type: str }

relationship_types:
  # Intra-nivel (mesmo level)
  VALIDATES: { source: DiagnosticTest, target: Estimator }
  REQUIRES: { source: Estimator, target: Parameter }
  ALTERNATIVE_TO: { source: Estimator, target: Estimator }

  # Cross-level (entre niveis diferentes)
  ADDRESSES: { source: Estimator, target: StatisticalConcept, cross_level: true }
  TESTS_FOR: { source: DiagnosticTest, target: StatisticalConcept, cross_level: true }
  BELONGS_TO: { source: Estimator, target: ModelFamily, cross_level: true }
```

**Regras:**
- Cada entity type DEVE ter `level` entre 1 e 4
- `name` e propriedade obrigatoria em todo entity type
- Relationships referenciam entity types existentes em `source` e `target`
- `cross_level: true` marca relacoes que cruzam niveis hierarquicos

### aliases.yaml (opcional)

Mapeia nomes alternativos para formas canonicas. O entity resolver usa
esses aliases para normalizar entidades extraidas pelo LLM.

```yaml
# Formato flat: alias → canonical
"FE": "FixedEffects"
"RE": "RandomEffects"
"efeitos fixos": "FixedEffects"
"OLS": "OrdinaryLeastSquares"
"MQO": "OrdinaryLeastSquares"
"Hausman": "HausmanTest"
"teste de Hausman": "HausmanTest"
"heteroscedasticidade": "Heteroscedasticity"
"endogeneidade": "Endogeneity"
```

Tambem suporta formato nested:
```yaml
# Formato nested: EntityType → {canonical: [aliases]}
Estimator:
  FixedEffects: ["FE", "efeitos fixos", "fixed effects", "within estimator"]
  RandomEffects: ["RE", "efeitos aleatorios", "random effects"]
```

**Dicas:**
- Inclua abreviacoes comuns do dominio
- Inclua termos em portugues e ingles
- O matching e case-insensitive
- Fuzzy matching (85%) pega variacoes nao listadas

### seed_entities.yaml (opcional)

Entidades iniciais que sao carregadas no grafo antes da ingestao.
Util para garantir que entidades fundamentais existam.

```yaml
entities:
  # Domains (Level 3)
  - type: ModelFamily
    name: "PanelDataModels"
    properties:
      description: "Modelos para dados em painel"

  # Concepts (Level 2)
  - type: StatisticalConcept
    name: "Heteroscedasticity"
    properties:
      description: "Variancia dos erros nao e constante"
      formal_definition: "Var(u_i|X_i) != sigma^2"

  # Facts (Level 1)
  - type: Estimator
    name: "FixedEffects"
    properties:
      module_path: "linearmodels.panel.model.PanelOLS"
      description: "Estimador de efeitos fixos para dados em painel"

relationships:
  - source: "FixedEffects"
    relation: "BELONGS_TO"
    target: "PanelDataModels"
  - source: "FixedEffects"
    relation: "ADDRESSES"
    target: "Heteroscedasticity"
```

---

## Como Criar uma Ontologia para um Novo Dominio

### Exemplo: Psicologia Clinica

#### 1. Criar diretorio

```bash
mkdir -p build/ontologies/psychology
```

#### 2. Definir ontology.yaml

Pense em 3 perguntas:
- **Quais sao as entidades concretas?** → Level 1 (Facts)
- **Quais conceitos abstraem essas entidades?** → Level 2 (Concepts)
- **Quais dominios agrupam os conceitos?** → Level 3 (Domains)

```yaml
name: psychology
version: "1.0"
description: "Psicologia clinica: transtornos, terapias e tecnicas"

entity_types:
  # Level 1 — Facts
  Technique:
    level: 1
    properties:
      name: { type: str, required: true }
      description: { type: str }
      evidence_level: { type: str }

  Disorder:
    level: 1
    properties:
      name: { type: str, required: true }
      dsm_code: { type: str }
      description: { type: str }

  Assessment:
    level: 1
    properties:
      name: { type: str, required: true }
      type: { type: str }

  Medication:
    level: 1
    properties:
      name: { type: str, required: true }
      class: { type: str }

  # Level 2 — Concepts
  TherapyApproach:
    level: 2
    properties:
      name: { type: str, required: true }
      description: { type: str }
      theoretical_basis: { type: str }

  SymptomCluster:
    level: 2
    properties:
      name: { type: str, required: true }
      description: { type: str }

  # Level 3 — Domains
  PsychologyDomain:
    level: 3
    properties:
      name: { type: str, required: true }
      description: { type: str }

relationship_types:
  # Intra-nivel
  TREATS: { source: Technique, target: Disorder }
  ASSESSES: { source: Assessment, target: Disorder }
  PRESCRIBED_FOR: { source: Medication, target: Disorder }
  COMORBID_WITH: { source: Disorder, target: Disorder }
  COMPLEMENTS: { source: Technique, target: Technique }

  # Cross-level
  PART_OF_APPROACH: { source: Technique, target: TherapyApproach, cross_level: true }
  MANIFESTS_AS: { source: Disorder, target: SymptomCluster, cross_level: true }
  BELONGS_TO: { source: TherapyApproach, target: PsychologyDomain, cross_level: true }
```

#### 3. Definir aliases.yaml

```yaml
"TCC": "CognitiveBehavioralTherapy"
"CBT": "CognitiveBehavioralTherapy"
"terapia cognitivo-comportamental": "CognitiveBehavioralTherapy"
"EMDR": "EyeMovementDesensitization"
"depressao": "MajorDepressiveDisorder"
"MDD": "MajorDepressiveDisorder"
"ansiedade generalizada": "GeneralizedAnxietyDisorder"
"TAG": "GeneralizedAnxietyDisorder"
"GAD": "GeneralizedAnxietyDisorder"
"TDAH": "ADHD"
"transtorno de deficit de atencao": "ADHD"
"BDI": "BeckDepressionInventory"
"inventario de Beck": "BeckDepressionInventory"
```

#### 4. Definir seed_entities.yaml

```yaml
entities:
  - type: PsychologyDomain
    name: "ClinicalPsychology"
    properties:
      description: "Avaliacao e tratamento de transtornos mentais"

  - type: PsychologyDomain
    name: "Neuropsychology"
    properties:
      description: "Relacao entre cerebro e comportamento"

  - type: TherapyApproach
    name: "CognitiveBehavioralTherapy"
    properties:
      description: "Abordagem baseada na relacao entre pensamentos, emocoes e comportamentos"
      theoretical_basis: "Modelo cognitivo de Beck"

  - type: Disorder
    name: "MajorDepressiveDisorder"
    properties:
      dsm_code: "296.2x"
      description: "Episodios de humor deprimido persistente"

relationships:
  - source: "CognitiveBehavioralTherapy"
    relation: "BELONGS_TO"
    target: "ClinicalPsychology"
```

#### 5. Construir o grafo

```bash
# Criar instancia
python scripts/create_instance.py \
    --name psychology \
    --ontology psychology \
    --seed

# Ingerir documentos (ex: livros, artigos, manuais)
python scripts/ingest.py \
    --instance psychology \
    --ontology psychology \
    --source ./corpus_psicologia/ \
    --file-types .pdf .md

# Construir hierarquia
python scripts/build_hierarchy.py --ontology psychology
```

---

## Ontologias Existentes

| Nome | Descricao | Entity Types | Rel Types |
|------|-----------|-------------|-----------|
| `model_intelligence` | Validacao de modelos, econometria de painel | 10 (Estimator, DiagnosticTest, StatisticalConcept, ModelFamily, ...) | 13 |
| `ai_governance` | Compliance e regulacao de IA | Regulacao, Framework, Requisito, ... | ... |
| `bias_intelligence` | Deteccao de vies em modelos | FairnessMetric, ProtectedGroup, MitigationStrategy, ... | ... |
| `panelbox` | Analise de dados em painel | Similar a model_intelligence | ... |

Para listar ontologias disponiveis:
```python
from graphenda_build.ontology.manager import OntologyRegistry
from pathlib import Path

registry = OntologyRegistry(Path("build/ontologies"))
print(registry.list_available())
# ['model_intelligence', 'ai_governance', 'bias_intelligence', 'panelbox']
```

---

## Como o LLM Extrai Triples

O pipeline injeta a ontologia no **system prompt** do Claude. O LLM recebe:

1. Lista de entity types validos (com descricoes)
2. Lista de relationship types validos (com source/target)
3. O chunk de texto para analisar

O LLM retorna JSON com triples extraidos:
```json
[
  {
    "subject": {"name": "FixedEffects", "type": "Estimator"},
    "predicate": "ADDRESSES",
    "object": {"name": "Endogeneity", "type": "StatisticalConcept"},
    "confidence": 0.95
  }
]
```

Cada triple e validado contra a ontologia:
- Entity type deve existir na ontologia
- Relationship type deve existir na ontologia
- Source/target devem ser compativeis

Triples invalidos sao descartados com warning no log.

---

## Cache e Processamento Incremental

O pipeline usa cache em dois niveis:

1. **Chunks** (`cache/chunks/`) — cache por arquivo (hash SHA-256)
2. **Triples** (`cache/triples/`) — cache por chunk_id
3. **Manifest** (`cache/pipeline_manifest.json`) — hash de cada arquivo processado

No modo incremental (default), apenas arquivos modificados sao reprocessados.
Use `--full` para forcar reprocessamento completo.

Para limpar cache:
```bash
rm -rf cache/
```

---

## Publicar Grafo no Registry

Apos o grafo estar maduro, publique-o para o SaaS consumir:

```python
from graphenda_shared.registry.models import GraphRegistryEntry, GraphStatus, GraphMetrics
from graphenda_build.registry.publisher import RegistryPublisher

publisher = RegistryPublisher("build/registry")

entry = GraphRegistryEntry(
    slug="model-validation",
    name="Graphenda Model Validation",
    description="Knowledge graph for statistical model validation",
    version="1.0.0",
    status=GraphStatus.BUILDING,
    neo4j_database="model_intelligence",
    ontology="model_intelligence/ontology.yaml",
    metrics=GraphMetrics(nodes=1247, edges=3891, avg_confidence=0.91),
)

publisher.publish(entry)
# Quando estiver pronto:
publisher.set_status("model-validation", GraphStatus.ACTIVE)
```

---

## Resumo dos Scripts

| Script | Funcao | Quando usar |
|--------|--------|-------------|
| `create_instance.py` | Cria database + schema + seeds | Uma vez por grafo |
| `ingest.py` | Documentos → triples → Neo4j | Sempre que tiver novos docs |
| `build_hierarchy.py` | Levels + communities + meta | Apos ingestao |

Ordem: `create_instance` → `ingest` (N vezes) → `build_hierarchy`

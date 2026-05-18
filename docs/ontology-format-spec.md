# Graphenda - Ontology Format Specification

## Overview

Ontologias Graphenda sao definidas em YAML e determinam como a engine processa
dados de um dominio especifico. Cada ontologia configura os tipos de entidade,
relacionamentos, hierarquia e entidades iniciais (seed) para um grafo de
conhecimento.

---

## Estrutura de Diretorio

```
ontologies/
└── <ontology_name>/
    ├── ontology.yaml        # Definicao principal (obrigatorio)
    ├── aliases.yaml          # Mapeamento de sinonimos (opcional)
    └── seed_entities.yaml    # Entidades iniciais pre-definidas (opcional)
```

---

## Schema

### Top-level Fields

| Campo | Tipo | Obrigatorio | Descricao |
|-------|------|:-----------:|-----------|
| `name` | string | Sim | Identificador unico da ontologia (slug) |
| `version` | string | Sim | Versao semantica (ex: "1.0") |
| `description` | string | Sim | Descricao do dominio coberto |
| `entity_types` | map | Sim | Mapa de tipos de entidade |
| `relationship_types` | map | Sim | Mapa de tipos de relacionamento |
| `hierarchy` | object | Nao | Configuracao de niveis hierarquicos |
| `hierarchy_relationships` | map | Nao | Relacionamentos especificos de hierarquia |

### Entity Type

Cada entity type e definido como uma chave no mapa `entity_types`:

```yaml
entity_types:
  EntityName:
    level: 1                    # Nivel hierarquico (1-4, obrigatorio)
    properties:
      property_name:
        type: str               # str, int, float, bool, list
        required: true           # Se a propriedade e obrigatoria
        description: "O que esta propriedade representa"
        default: "valor"         # Valor default (opcional)
        valid_values:            # Lista de valores validos (opcional)
          - "valor1"
          - "valor2"
```

**Niveis hierarquicos:**

| Level | Nome | Descricao |
|-------|------|-----------|
| 1 | Facts | Entidades atomicas, dados concretos |
| 2 | Concepts | Conceitos que agrupam fatos |
| 3 | Domains | Dominios de conhecimento |
| 4 | Systems | Macro-sistemas (nivel mais alto) |

### Relationship Type

```yaml
relationship_types:
  RELATIONSHIP_NAME:
    source: SourceEntityType    # Tipo de entidade de origem
    target: TargetEntityType    # Tipo de entidade de destino
    description: "O que este relacionamento significa"
    cross_level: false          # Se conecta entidades de niveis diferentes
    properties:                 # Propriedades do relacionamento (opcional)
      weight:
        type: float
```

**Convencoes:**
- Nomes de relationship em `UPPER_SNAKE_CASE`
- `source` e `target` devem referenciar entity types existentes
- Use `cross_level: true` para relacoes entre niveis hierarquicos diferentes

### Hierarchy (Opcional)

```yaml
hierarchy:
  levels:
    - name: "facts"
      description: "Entidades atomicas"
    - name: "concepts"
      description: "Conceitos agrupadores"
    - name: "domains"
      description: "Dominios de conhecimento"
  propagation: "bottom_up"    # bottom_up, top_down, ou bidirectional
```

**Modos de propagacao:**

| Modo | Descricao |
|------|-----------|
| `bottom_up` | Fatos informam conceitos, conceitos informam dominios |
| `top_down` | Contexto de dominio ajuda a desambiguar fatos |
| `bidirectional` | Propagacao nos dois sentidos (padrao recomendado) |

---

## Exemplos

### Exemplo Completo: Model Intelligence

```yaml
name: model_intelligence
version: "1.0"
description: "Modelos de risco, econometria de painel e validacao"

entity_types:
  # Level 1 - Facts
  Estimator:
    level: 1
    properties:
      name: { type: str, required: true }
      module_path: { type: str }
      description: { type: str }
      assumptions: { type: str }
      supports_unbalanced: { type: bool }

  DiagnosticTest:
    level: 1
    properties:
      name: { type: str, required: true }
      null_hypothesis: { type: str }
      interpretation_guide: { type: str }

  Parameter:
    level: 1
    properties:
      name: { type: str, required: true }
      type: { type: str }
      default: { type: str }

  StandardError:
    level: 1
    properties:
      name: { type: str, required: true }
      description: { type: str }

  Dataset:
    level: 1
    properties:
      name: { type: str, required: true }

  CodePattern:
    level: 1
    properties:
      name: { type: str, required: true }
      code: { type: str }

  ResultMetric:
    level: 1
    properties:
      name: { type: str, required: true }

  Literature:
    level: 1
    properties:
      name: { type: str, required: true }
      authors: { type: str }
      year: { type: int }

  # Level 2 - Concepts
  StatisticalConcept:
    level: 2
    properties:
      name: { type: str, required: true }
      description: { type: str }
      formal_definition: { type: str }

  # Level 3 - Domains
  ModelFamily:
    level: 3
    properties:
      name: { type: str, required: true }
      description: { type: str }

relationship_types:
  VALIDATES:
    source: DiagnosticTest
    target: Estimator
    description: "Test validates a specific estimator"

  REQUIRES:
    source: Estimator
    target: Parameter
    description: "Estimator requires this parameter"

  PRODUCES:
    source: Estimator
    target: ResultMetric
    description: "Estimator produces this metric"

  ADDRESSES:
    source: Estimator
    target: StatisticalConcept
    cross_level: true
    description: "Estimator addresses this statistical concept"

  TESTS_FOR:
    source: DiagnosticTest
    target: StatisticalConcept
    cross_level: true
    description: "Test checks for this concept"

  BELONGS_TO:
    source: Estimator
    target: ModelFamily
    cross_level: true
    description: "Estimator belongs to this model family"

  INHERITS_FROM:
    source: Estimator
    target: Estimator
    description: "Estimator inherits from another"

  ALTERNATIVE_TO:
    source: Estimator
    target: Estimator
    description: "Estimator is an alternative to another"

  SUPPORTS_SE:
    source: Estimator
    target: StandardError
    description: "Estimator supports this standard error type"

  DEMONSTRATED_IN:
    source: Estimator
    target: Dataset
    description: "Estimator demonstrated using this dataset"

  IMPLEMENTED_BY:
    source: CodePattern
    target: Estimator
    description: "Code pattern implements this estimator"

  BASED_ON:
    source: Estimator
    target: Literature
    description: "Estimator based on this literature"

  SUCCEEDS:
    source: DiagnosticTest
    target: DiagnosticTest
    description: "Test should be run after another test"
```

### Exemplo Minimo

```yaml
name: minha_ontologia
version: "1.0"
description: "Descricao do dominio"

entity_types:
  Conceito:
    level: 1
    properties:
      name: { type: str, required: true }
      descricao: { type: str }

  Categoria:
    level: 2
    properties:
      name: { type: str, required: true }

relationship_types:
  PERTENCE_A:
    source: Conceito
    target: Categoria
    cross_level: true
```

### Exemplo com Hierarchy Explicito

```yaml
name: governance_ontology
version: "1.0"
description: "AI Governance and compliance"

entity_types:
  Regulation:
    level: 1
    properties:
      name: { type: str, required: true }
      jurisdiction: { type: str }

  ComplianceDomain:
    level: 2
    properties:
      name: { type: str, required: true }

  RegulatoryFramework:
    level: 3
    properties:
      name: { type: str, required: true }

relationship_types:
  GOVERNS:
    source: Regulation
    target: ComplianceDomain
    cross_level: true

  PART_OF:
    source: ComplianceDomain
    target: RegulatoryFramework
    cross_level: true

hierarchy:
  levels:
    - name: "regulations"
      description: "Individual regulations and rules"
    - name: "domains"
      description: "Compliance domains (privacy, fairness, etc.)"
    - name: "frameworks"
      description: "Regulatory frameworks (EU AI Act, NIST, etc.)"
  propagation: "bidirectional"
```

---

## Aliases (aliases.yaml)

O arquivo `aliases.yaml` mapeia sinonimos para nomes canonicos de entidades.
Suporta dois formatos:

### Formato Flat

```yaml
fe: "FixedEffects"
fixed effects: "FixedEffects"
efeitos fixos: "FixedEffects"
hausman: "HausmanTest"
```

### Formato Nested

```yaml
Estimator:
  FixedEffects:
    - "FE"
    - "Fixed Effects"
    - "Efeitos Fixos"
  RandomEffects:
    - "RE"
    - "Random Effects"

DiagnosticTest:
  HausmanTest:
    - "Hausman"
    - "Hausman Test"
```

---

## Seed Entities (seed_entities.yaml)

Define entidades iniciais que sao inseridas no grafo antes da ingestao:

```yaml
Estimator:
  - name: "FixedEffects"
    properties:
      module_path: "linearmodels.panel.model.PanelOLS"
      description: "Panel OLS with entity fixed effects"
  - name: "RandomEffects"
    properties:
      module_path: "linearmodels.panel.model.RandomEffects"

DiagnosticTest:
  - name: "HausmanTest"
    properties:
      null_hypothesis: "Random effects model is consistent"
```

---

## Validacao

A engine valida automaticamente ontologias ao carrega-las. Regras de validacao:

1. **Levels**: Cada entity type deve ter `level` entre 1 e 4
2. **References**: Cada relationship type deve referenciar entity types existentes
   em `source` e `target`
3. **Required fields**: `name`, `version`, `description`, `entity_types` e
   `relationship_types` sao obrigatorios

Erros de validacao impedem o carregamento da ontologia e sao reportados com
mensagens descritivas.

Para validar manualmente:

```bash
python scripts/validate_ontology.py ontologies/minha_ontologia
```

---

## Best Practices

1. **Entity types focados**: Mantenha tipos de entidade especificos e sem
   sobreposicao. Cada entidade deve ter um papel claro no dominio.

2. **Nomes de relationships em UPPER_SNAKE_CASE**: Use nomes descritivos que
   expressem claramente a semantica do relacionamento.
   - Bom: `VALIDATES`, `BELONGS_TO`, `IMPLEMENTED_BY`
   - Ruim: `rel1`, `connection`, `link`

3. **Seed entities para conceitos core**: Defina entidades iniciais para os
   conceitos mais importantes do dominio. Isso melhora a extracao automatica
   pois a engine ja conhece os termos.

4. **Limite a hierarquia a 3-5 niveis**: Hierarquias muito profundas dificultam
   a navegacao e o raciocinio. Na maioria dos dominios, 3 niveis sao
   suficientes (Facts, Concepts, Domains).

5. **Use cross_level com parcimonia**: Relacionamentos cross-level conectam
   entidades de niveis diferentes e sao essenciais para o HCG, mas em excesso
   podem diluir a estrutura hierarquica.

6. **Aliases abrangentes**: Inclua sinonimos em ingles e portugues, abreviacoes
   comuns, e variacoes de nomenclatura para maximizar a cobertura de extracao.

7. **Propriedades tipadas**: Use os tipos corretos (`str`, `int`, `float`,
   `bool`, `list`) e marque como `required: true` apenas campos essenciais.

8. **Versionamento**: Incremente a versao da ontologia ao fazer mudancas
   significativas nos tipos de entidade ou relacionamentos.

# Desafios Tecnicos

## 1. Construcao Automatica do Grafo

Construir o grafo automaticamente a partir de documentos e o maior desafio tecnico.

### Pipeline necessario
- Extracao de entidades (NER)
- Extracao de relacoes
- Resolucao de entidades (deduplicacao)
- Atualizacao incremental

### Ferramentas
- spaCy (NER)
- LangExtract
- LLMs para extracao assistida

### Risco
Qualidade do grafo depende diretamente da qualidade da extracao.
Grafo ruim -> respostas ruins.

## 2. Escalabilidade do Grafo

- Grafos muito grandes podem tornar queries lentas
- Necessidade de indexacao eficiente
- Particao e sharding do grafo

## 3. Manutencao e Atualizacao

- Conhecimento muda com o tempo
- Pipeline de atualizacao incremental e essencial
- Versioning do grafo

## 4. Qualidade da Compressao de Contexto

- Comprimir demais pode perder informacao critica
- Necessidade de balancear compressao vs completude
- Testes de qualidade de resposta sao fundamentais

## 5. Deteccao de Comunidades em Escala

- Algoritmos como Louvain podem ser custosos em grafos muito grandes
- Necessidade de recomputar comunidades quando o grafo muda
- Estrategias de cache e atualizacao incremental

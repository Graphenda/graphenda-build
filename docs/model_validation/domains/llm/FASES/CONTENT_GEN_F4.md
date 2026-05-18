# Fase F4 — Codigo de Exemplo

**Status**: COMPLETO
**Dependencias**: F3
**Bloqueia**: F5

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/llm/`

---

## Arquivos a Gerar

### Modeling (4 arquivos)

#### 1. modeling/rag_pipeline.py
- Pipeline RAG com LangChain
- Document loading, chunking, embedding
- Vector store com FAISS ou ChromaDB
- Query + retrieval + generation
- Avaliacao de qualidade das respostas

#### 2. modeling/lora_finetuning.py
- Fine-tuning com LoRA/QLoRA usando PEFT + transformers
- Preparacao de dataset instrucional
- Treino e avaliacao antes/depois
- Comparacao com modelo base

#### 3. modeling/prompt_engineering.py
- Templates de prompts para diferentes tarefas
- Chain-of-thought prompting
- Few-shot examples optimization
- Self-consistency com multiplas respostas

#### 4. modeling/llm_evaluation_suite.py
- Pipeline de avaliacao automatica de LLMs
- MMLU, TruthfulQA subsets
- Comparacao entre modelos
- Report automatico de resultados

### Validation (3 arquivos)

#### 5. validation/hallucination_detection.py
- Deteccao de alucinacoes via fact-checking
- Groundedness check para RAG
- NLI-based faithfulness evaluation
- Categorias de alucinacao

#### 6. validation/rag_evaluation.py
- Avaliacao end-to-end de RAG
- Retrieval metrics: Recall@k, MRR, NDCG
- Answer quality: relevance, faithfulness, completeness
- RAGAS framework

#### 7. validation/red_teaming.py
- Testes adversariais para LLMs
- Prompt injection detection
- Jailbreak resistance testing
- Safety evaluation suite

### Visualization (1 arquivo)

#### 8. visualization/llm_plots.py
- Dashboard de metricas de LLM
- Comparacao de modelos (radar chart)
- Hallucination rate por categoria
- Retrieval vs answer quality scatter
- Custo vs qualidade trade-off
- Latencia distribution

---

## Formato: cada script com docstring, main()

---

## Criterios de Aceite

- [x] 8 scripts Python criados nas subpastas corretas
- [x] modeling/rag_pipeline.py — RAG com LangChain + FAISS/ChromaDB
- [x] modeling/lora_finetuning.py — LoRA/QLoRA com PEFT
- [x] modeling/prompt_engineering.py — CoT, few-shot, self-consistency
- [x] modeling/llm_evaluation_suite.py — MMLU, TruthfulQA, comparacao
- [x] validation/hallucination_detection.py — Fact-checking, groundedness, NLI
- [x] validation/rag_evaluation.py — RAGAS, retrieval metrics, answer quality
- [x] validation/red_teaming.py — Prompt injection, jailbreak, safety
- [x] visualization/llm_plots.py — Dashboard, radar, hallucination, cost-quality
- [x] Todos passam verificacao de sintaxe Python
- [x] Todos tem docstring, funcoes organizadas e main()

---

## Bibliotecas Utilizadas

| Biblioteca | Versao Minima | Uso |
|------------|---------------|-----|
| transformers | >= 4.30 | Modelos, tokenizers |
| langchain | >= 0.1 | Pipelines RAG, agents |
| peft | >= 0.6 | LoRA, QLoRA |
| ragas | >= 0.1 | Avaliacao de RAG |
| chromadb | >= 0.4 | Vector store |
| faiss-cpu | >= 1.7 | Vector search |
| matplotlib | >= 3.7 | Visualizacoes |

---

**End of Specification**

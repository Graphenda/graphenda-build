# Fase F3 — Guias Explicativos

**Status**: COMPLETO
**Dependencias**: F1
**Bloqueia**: F4, F5

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/llm/`

---

## Guias a Gerar

### 1. overview.md
- LLMs e next-token prediction
- Panorama: GPT, Claude, Llama, Gemini, Mistral
- Paradigmas: zero-shot, few-shot, fine-tuning, RAG
- RLHF e alinhamento: InstructGPT, Constitutional AI
- Regulamentacao: EU AI Act para GPAI
- Riscos: alucinacao, bias, uso indevido, privacidade

### 2. models.md
- Transformer decoder-only (GPT family)
- Pre-treino: next-token prediction em larga escala
- RLHF: reward model, PPO, DPO
- Fine-tuning eficiente: LoRA, QLoRA, prefix tuning
- RAG: retriever + generator, chunking strategies
- Prompting: chain-of-thought, few-shot, self-consistency
- Modelos abertos vs fechados
- Quantizacao e otimizacao de inferencia

### 3. validation.md
- Checklist de validacao para sistemas LLM
- Factualidade: TruthfulQA, fact-checking automatico
- Deteccao de alucinacao: groundedness, faithfulness
- Benchmarks: MMLU, HellaSwag, HumanEval, TruthfulQA
- Avaliacao de RAG: retrieval quality, answer quality, groundedness
- Red teaming e testes adversariais
- Avaliacao humana: protocolos, concordancia inter-anotador
- Compliance EU AI Act
- Monitoramento: drift de qualidade, custo, latencia

### 4. metrics.md
- Perplexity: limitacoes
- MMLU accuracy
- BLEU, ROUGE, BERTScore
- Groundedness score para RAG
- Hallucination rate
- Human evaluation: Likert, pairwise, Elo
- RAG metrics: Recall@k, Answer Relevance, Faithfulness
- Latencia e custo por token

### 5. pitfalls.md
- Confiar em benchmarks como unica medida
- Nao testar alucinacoes em dominio especifico
- RAG sem avaliar retrieval quality
- Prompts frageis
- Fine-tuning sem dados de qualidade
- Ignorar custos operacionais
- Nao documentar riscos (EU AI Act)
- Metricas automaticas quando avaliacao humana e necessaria

---

## Formato: `slug: llm-<nome>`, `domain: llm`, `type: guide`

Cada guia: minimo 1500 palavras, referencias da F1.

---

## Criterios de Aceite

- [x] 5 guias criados: overview.md, models.md, validation.md, metrics.md, pitfalls.md
- [x] papers.md da F1 tambem presente
- [x] Todos com frontmatter YAML valido
- [x] Cada guia com minimo de 1500 palavras
- [x] Referencias cruzadas aos papers da F1
- [x] Conteudo baseado em pesquisa web

---

**End of Specification**

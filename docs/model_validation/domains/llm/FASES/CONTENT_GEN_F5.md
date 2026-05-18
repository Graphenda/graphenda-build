# Fase F5 — Templates e Exemplos de Relatorio de Validacao

**Status**: CONCLUIDO
**Dependencias**: F3, F4
**Bloqueia**: Nenhuma

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/report-templates/llm/`

---

### 1. template.md

```markdown
---
slug: llm-validation-report-template
name: "Validation Report Template — Large Language Models"
domain: llm
type: report-template
status: draft
tags: [llm, validation-report, template, rag, hallucination, eu-ai-act, red-teaming]
---

# Model Validation Report — Large Language Models

## 1. Executive Summary

## 2. System Description
### 2.1 Model (GPT-4, Claude, Llama, Mistral, fine-tuned)
### 2.2 Paradigm (RAG / Fine-Tuning / Prompting / Hybrid)
### 2.3 Use Case and Scope
### 2.4 Architecture (pipeline components)
### 2.5 Configuration (temperature, max_tokens, top_p)

## 3. Data and Knowledge
### 3.1 Training Data (if fine-tuned)
### 3.2 Knowledge Base (if RAG): sources, volume, freshness
### 3.3 Chunking and Embedding Strategy (if RAG)
### 3.4 Data Quality Assessment

## 4. Factuality Assessment
### 4.1 Hallucination Rate (by category)
### 4.2 Groundedness Score (RAG faithfulness)
### 4.3 TruthfulQA or Domain-Specific Factuality Test
### 4.4 Comparison with Baseline (no-RAG, different model)

## 5. Quality Assessment
### 5.1 Automatic Metrics (BLEU, ROUGE, BERTScore)
### 5.2 Human Evaluation Protocol and Results
### 5.3 Benchmark Performance (MMLU, task-specific)
### 5.4 Per-Category / Per-Task Breakdown

## 6. RAG Evaluation (if applicable)
### 6.1 Retrieval Quality (Recall@k, MRR, NDCG)
### 6.2 Answer Relevance
### 6.3 Answer Faithfulness (to retrieved context)
### 6.4 Answer Completeness
### 6.5 End-to-End RAGAS Score

## 7. Security and Robustness
### 7.1 Red Teaming Results
### 7.2 Prompt Injection Resistance
### 7.3 Jailbreak Resistance
### 7.4 PII Leakage Assessment
### 7.5 Adversarial Input Handling

## 8. Regulatory Compliance
### 8.1 EU AI Act: Risk Classification
### 8.2 Transparency and Disclosure
### 8.3 Documentation Requirements
### 8.4 Human Oversight Provisions
### 8.5 Bias and Fairness Assessment

## 9. Operational Metrics
### 9.1 Latency (p50, p95, p99)
### 9.2 Cost per Query / per Token
### 9.3 Availability and Error Rate
### 9.4 Scalability Assessment

## 10. Monitoring Plan
### 10.1 Quality Drift Detection
### 10.2 Cost Monitoring
### 10.3 User Feedback Loop
### 10.4 Revalidation Triggers

## 11. Limitations and Risks
### 11.1 Known Limitations
### 11.2 Model Risk Assessment (materiality)
### 11.3 Residual Risks

## 12. Conclusion and Recommendations
### 12.1 Overall Assessment
### 12.2 Conditions for Deployment
### 12.3 Recommended Review Frequency

## Appendices
### A. Full System Architecture Diagram
### B. Prompt Templates Used
### C. Human Evaluation Rubric
### D. Red Teaming Test Cases
### E. Benchmark Detailed Results
### F. Code and Reproducibility
```

### 2. example.md — Exemplo Completo

Preencher com:
- **Cenario**: Sistema RAG para atendimento ao cliente em banco
- **Modelo**: GPT-4 / Claude com RAG (LangChain + ChromaDB)
- **Knowledge base**: FAQs bancarias, regulamentacoes, termos de servico
- **Incluir**: hallucination rate, groundedness, retrieval metrics, red teaming, EU AI Act compliance, cost analysis, human evaluation
- **Tom**: relatorio real para comite de validacao de modelo em banco

---

## Criterios de Aceite

- [x] template.md criado com 12 secoes + appendices
- [x] template.md cobre factuality, RAG eval, security, compliance, operational
- [x] template.md inclui EU AI Act compliance e red teaming
- [x] template.md inclui monitoring plan com drift detection
- [x] example.md preenchido com RAG para atendimento bancario
- [x] example.md tem hallucination rate e groundedness
- [x] example.md tem retrieval metrics (Recall@k, RAGAS)
- [x] example.md tem red teaming results
- [x] example.md tem EU AI Act compliance assessment
- [x] example.md tem cost and latency analysis
- [x] example.md tem conclusao e recomendacoes realistas
- [x] Ambos tem frontmatter YAML valido
- [x] Conteudo baseado em pesquisa web

---

**End of Specification**

# Content Generation — Deep Learning Tabular Domain

## Objetivo

Gerar todo o conteudo do dominio "Deep Learning — Tabular" para o ModelRiskLab.

## Referencia

- Especificacao do dominio: `/home/guhaase/projetos/Graphenda/build/docs/model_validation/domains/14-deep-learning-tabular.md`
- Destino do conteudo: `/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/`
- Templates: `/home/guhaase/projetos/ModelRiskLab/mrl-content-files/templates/`

## Diagrama de Dependencias

```
F1 (Papers & Referencias) ─────┐
                                │
F2 (Noticias & Artigos) ───────┤  (F1 e F2 independentes)
                                │
F3 (Guias Explicativos) ───────┤  (depende de F1 para referencias)
                                │
F4 (Codigo de Exemplo) ────────┤  (depende de F3 para contexto)
                                │
F5 (Relatorios de Validacao) ──┘  (depende de F3 e F4)
```

## Subfases

| Status   | Arquivo               | Descricao                                                            | Dependencias |
|----------|-----------------------|----------------------------------------------------------------------|--------------|
| PENDENTE | CONTENT_GEN_F1.md     | Papers academicos: busca, resumo e referencias                       | Nenhuma      |
| PENDENTE | CONTENT_GEN_F2.md     | Noticias e artigos: busca e redacao                                  | Nenhuma      |
| PENDENTE | CONTENT_GEN_F3.md     | Guias explicativos: overview, models, validation, etc.               | F1           |
| PENDENTE | CONTENT_GEN_F4.md     | Codigo: MLP, TabNet, FT-Transformer, baseline, convergence, interp.  | F3           |
| PENDENTE | CONTENT_GEN_F5.md     | Templates e exemplos de relatorio de validacao                       | F3, F4       |

## Automacao

```bash
./prompt.sh          # Executa todas as subfases em ordem
./prompt.sh 3        # Executa apenas a subfase F3
./prompt.sh 2 3      # Executa subfases F2 a F3
```

## Destino dos Arquivos Gerados

```
ModelRiskLab/mrl-content-files/content/en/
├── guides/deep-learning-tabular/
│   ├── papers.md              ← F1
│   ├── overview.md            ← F3
│   ├── models.md              ← F3
│   ├── validation.md          ← F3
│   ├── metrics.md             ← F3
│   └── pitfalls.md            ← F3
├── news/
│   ├── dl-tabular-*.md        ← F2
├── code-examples/deep-learning-tabular/
│   ├── modeling/              ← F4
│   ├── validation/            ← F4
│   └── visualization/         ← F4
└── report-templates/deep-learning-tabular/
    ├── template.md            ← F5
    └── example.md             ← F5
```

## Criterios de Sucesso

- [ ] Todos os 7 papers cobertos
- [ ] Pelo menos 7 artigos de noticias
- [ ] 5 guias explicativos completos
- [ ] 7 arquivos de codigo funcional (MLP, TabNet, FT-Transformer, baseline comparison, convergence, interpretability, plots)
- [ ] Template de relatorio + exemplo com TabNet credit scoring
- [ ] Frontmatter YAML valido em todos os arquivos .md

---

**End of Overview**

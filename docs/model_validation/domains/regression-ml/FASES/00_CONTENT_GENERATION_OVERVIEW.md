# Content Generation — Regression ML Models Domain

## Objetivo

Gerar todo o conteudo do dominio "Regression ML Models" para o ModelRiskLab,
incluindo papers academicos, noticias, guias explicativos, codigo de exemplo
e templates de relatorio de validacao.

## Referencia

- Especificacao do dominio: `/home/guhaase/projetos/Graphenda/build/docs/model_validation/domains/07-regression-ml.md`
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
| PENDENTE | CONTENT_GEN_F4.md     | Codigo: trees, XGB/LGBM, SVR/KNN, quantile, residuals, comparison   | F3           |
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
├── guides/regression-ml/
│   ├── papers.md              ← F1
│   ├── overview.md            ← F3
│   ├── models.md              ← F3
│   ├── validation.md          ← F3
│   ├── metrics.md             ← F3
│   └── pitfalls.md            ← F3
├── news/
│   ├── regression-ml-*.md     ← F2 (multiplos artigos)
├── code-examples/regression-ml/
│   ├── modeling/              ← F4
│   ├── validation/            ← F4
│   └── visualization/         ← F4
└── report-templates/regression-ml/
    ├── template.md            ← F5
    └── example.md             ← F5
```

## Criterios de Sucesso

- [ ] Todos os 7 papers cobertos com resumos e referencias
- [ ] Pelo menos 7 artigos de noticias gerados
- [ ] 5 guias explicativos completos
- [ ] 7 arquivos de codigo funcional
- [ ] Template de relatorio de validacao completo
- [ ] Exemplo de relatorio com Ames Housing + XGBoost
- [ ] Todo conteudo segue os templates do mrl-content-files
- [ ] Frontmatter YAML valido em todos os arquivos .md

---

**End of Overview**

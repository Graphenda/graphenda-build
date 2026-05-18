# Content Generation — Time Series Models Domain

## Objetivo

Gerar todo o conteudo do dominio "Time Series Models" para o ModelRiskLab,
incluindo papers academicos, noticias, guias explicativos, codigo de exemplo
e templates de relatorio de validacao.

## Referencia

- Especificacao do dominio: `/home/guhaase/projetos/Graphenda/build/docs/model_validation/domains/03-time-series.md`
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

F1 e F2 podem ser paralelizados. F3 depende de F1. F4 depende de F3. F5 e a finalizacao.

## Subfases

| Status   | Arquivo               | Descricao                                                   | Dependencias |
|----------|-----------------------|-------------------------------------------------------------|--------------|
| PENDENTE | CONTENT_GEN_F1.md     | Papers academicos: busca, resumo e referencias              | Nenhuma      |
| PENDENTE | CONTENT_GEN_F2.md     | Noticias e artigos: busca e redacao                         | Nenhuma      |
| PENDENTE | CONTENT_GEN_F3.md     | Guias explicativos: overview, models, validation, etc.      | F1           |
| PENDENTE | CONTENT_GEN_F4.md     | Codigo de exemplo: ARIMA, GARCH, VAR, VECM, diagnosticos   | F3           |
| PENDENTE | CONTENT_GEN_F5.md     | Templates e exemplos de relatorio de validacao              | F3, F4       |

## Automacao

Todas as subfases podem ser executadas com o script `prompt.sh`.

```bash
./prompt.sh          # Executa todas as subfases em ordem
./prompt.sh 3        # Executa apenas a subfase F3
./prompt.sh 2 3      # Executa subfases F2 a F3
```

## Destino dos Arquivos Gerados

```
ModelRiskLab/mrl-content-files/content/en/
├── guides/time-series/
│   ├── papers.md              ← F1
│   ├── overview.md            ← F3
│   ├── models.md              ← F3
│   ├── validation.md          ← F3
│   ├── metrics.md             ← F3
│   └── pitfalls.md            ← F3
├── news/
│   ├── time-series-*.md       ← F2 (multiplos artigos)
├── code-examples/time-series/
│   ├── modeling/              ← F4
│   ├── validation/            ← F4
│   └── visualization/         ← F4
└── report-templates/time-series/
    ├── template.md            ← F5
    └── example.md             ← F5
```

## Criterios de Sucesso

- [ ] Todos os 7 papers listados na spec cobertos com resumos e referencias
- [ ] Pelo menos 7 artigos de noticias gerados
- [ ] 5 guias explicativos completos (overview, models, validation, metrics, pitfalls)
- [ ] 7 arquivos de codigo funcional (ARIMA, GARCH, VAR, VECM, stationarity, residuals, plots)
- [ ] Template de relatorio de validacao completo
- [ ] Exemplo de relatorio preenchido com AirPassengers
- [ ] Todo conteudo segue os templates do mrl-content-files
- [ ] Frontmatter YAML valido em todos os arquivos .md

---

**End of Overview**

# Fase F3 — Guias Explicativos

**Status**: COMPLETO
**Dependencias**: F1
**Bloqueia**: F4, F5

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/generative/`

---

## Guias a Gerar

### 1. overview.md
- Modelos generativos e por que sao importantes
- Panorama: GANs, VAEs, diffusion, normalizing flows
- Aplicacoes: geracao de imagens, dados sinteticos, data augmentation
- Dados sinteticos tabulares: privacidade, augmentation, balanceamento
- Riscos: deepfakes, privacidade, qualidade

### 2. models.md
- GAN: generator vs discriminator, treinamento adversarial
- Variantes: DCGAN, WGAN, StyleGAN, CTGAN
- VAE: encoder-decoder, espaco latente, ELBO
- Diffusion: forward process, reverse process, DDPM
- Latent Diffusion: eficiencia via espaco latente
- Normalizing Flows: transformacoes invertiveis
- CTGAN e TVAE para dados tabulares

### 3. validation.md
- Checklist para modelos generativos
- Qualidade: FID, IS, KID
- Diversidade: coverage, density
- Fidelidade tabular: distribuicoes marginais, correlacoes
- Utility test: modelo downstream em sinteticos vs reais
- Privacy test: DCR, membership inference
- Mode collapse detection
- Estabilidade do treino

### 4. metrics.md
- FID (Frechet Inception Distance)
- IS (Inception Score)
- KID (Kernel Inception Distance)
- Precision e Recall para geracao
- Para tabulares: KS test, chi-squared, correlation preservation, ML utility, DCR

### 5. pitfalls.md
- Mode collapse
- Treino instavel de GANs
- FID com poucas amostras
- Dados sinteticos vazando informacao real
- Assumir preservacao de todas as relacoes
- Nao validar utilidade downstream
- Usar sinteticos sem disclosure em contexto regulado

---

## Formato: `slug: generative-<nome>`, `domain: generative`, `type: guide`

Cada guia: minimo 1500 palavras, formulas LaTeX (GAN objective, VAE ELBO, FID), referencias da F1.

---

## Criterios de Aceite

- [x] 5 guias criados: overview.md, models.md, validation.md, metrics.md, pitfalls.md
- [x] papers.md da F1 tambem presente
- [x] Todos com frontmatter YAML valido
- [x] Cada guia com minimo de 1500 palavras
- [x] Formulas LaTeX incluidas (GAN minimax, ELBO, FID)
- [x] Referencias cruzadas aos papers da F1
- [x] Conteudo baseado em pesquisa web

---

**End of Specification**

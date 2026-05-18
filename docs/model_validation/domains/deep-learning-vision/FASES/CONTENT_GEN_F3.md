# Fase F3 — Guias Explicativos

**Status**: COMPLETO
**Dependencias**: F1
**Bloqueia**: F4, F5

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/guides/deep-learning-vision/`

---

## Guias a Gerar

### 1. overview.md
- O que e Deep Learning para visao computacional
- Evolucao: LeNet -> AlexNet -> VGG -> ResNet -> EfficientNet -> ViT
- Tarefas: classificacao, deteccao, segmentacao, geracao
- Transfer learning: por que funciona e quando usar
- CNNs vs Vision Transformers
- Desafios: dados, custo computacional, interpretabilidade

### 2. models.md
- CNNs: convolucoes, pooling, fully connected, batch normalization
- Arquiteturas classicas: VGG, ResNet, Inception, EfficientNet
- Vision Transformers (ViT): patches como tokens, attention
- Object Detection: YOLO (v5-v8), SSD, Faster R-CNN, DETR
- Segmentacao Semantica: U-Net, DeepLab, Mask R-CNN
- Transfer Learning: fine-tuning, feature extraction, frozen layers
- Data Augmentation: flips, rotations, color jitter, Mixup, CutMix

### 3. validation.md
- Split adequado para imagens: estratificado por classe
- Data leakage: imagens do mesmo paciente/cena em train e test
- Metricas por tarefa: accuracy, mAP, IoU, Dice
- Grad-CAM e SHAP para interpretabilidade
- Adversarial testing: FGSM, PGD, robustez a perturbacoes
- Calibracao de probabilidades em CNNs
- Cross-validation com imagens (cuidados com augmentation)
- Fairness em visao: bias por genero, etnia, idade

### 4. metrics.md
- Accuracy, Top-5 Accuracy: classificacao
- Precision, Recall, F1: por classe
- mAP (mean Average Precision): deteccao
- IoU (Intersection over Union): segmentacao
- Dice coefficient: segmentacao medica
- FPS: velocidade de inferencia
- FLOPs: custo computacional
- Robustez: accuracy sob ataques adversariais

### 5. pitfalls.md
- Data leakage com augmentation antes do split
- Overfitting em datasets pequenos sem transfer learning
- Nao usar data augmentation adequada
- Ignorar class imbalance em classificacao de imagens
- Confiar em accuracy sem Grad-CAM (modelo usa artefatos)
- Nao testar robustez adversarial
- Deploy sem considerar latencia e tamanho do modelo
- Avaliar em dataset enviesado

---

## Formato: frontmatter com `slug: deep-learning-vision-<nome>`, `domain: deep-learning-vision`, `type: guide`

Cada guia: minimo 1500 palavras, formulas LaTeX (convolution, cross-entropy, IoU), tabelas comparativas, referencias da F1.

---

## Criterios de Aceite

- [x] 5 guias criados: overview.md, models.md, validation.md, metrics.md, pitfalls.md
- [x] Alem dos 5 guias, papers.md da F1 tambem presente no diretorio
- [x] Todos com frontmatter YAML valido
- [x] Cada guia com minimo de 1500 palavras
- [x] Formulas LaTeX incluidas (convolution, cross-entropy, IoU, mAP)
- [x] Referencias cruzadas aos papers da F1
- [x] Conteudo baseado em pesquisa web
- [x] Tom tecnico e adequado para profissionais de model validation

---

## Ferramentas Necessarias

- **Read**, **WebSearch**, **WebFetch**, **Write**

---

**End of Specification**

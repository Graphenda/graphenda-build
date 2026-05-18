# Fase F4 — Codigo de Exemplo

**Status**: COMPLETO
**Dependencias**: F3
**Bloqueia**: F5

---

## Diretorio de Destino

`/home/guhaase/projetos/ModelRiskLab/mrl-content-files/content/en/code-examples/deep-learning-vision/`

---

## Arquivos a Gerar

### Modeling (5 arquivos)

#### 1. modeling/cnn_classification.py
- CNN customizada com PyTorch para classificacao
- Transfer learning com ResNet-50 pre-treinado
- Fine-tuning: frozen layers vs full training
- Data augmentation com torchvision.transforms
- Dataset: CIFAR-10 (torchvision)

#### 2. modeling/object_detection_yolo.py
- YOLOv8 com ultralytics para deteccao
- Treinamento em dataset formato COCO (subset sintetico ou PASCAL VOC)
- Inferencia e visualizacao de bounding boxes
- Metricas mAP e analise por classe
- Dataset: PASCAL VOC subset ou COCO subset

#### 3. modeling/segmentation_unet.py
- U-Net com PyTorch para segmentacao semantica
- Treinamento com Dice loss e cross-entropy
- Augmentation especifica (imagem + mascara)
- Visualizacao de predicoes
- Dataset: Oxford Pets (segmentacao) ou sintetico

#### 4. modeling/vision_transformer.py
- ViT com Hugging Face transformers
- Fine-tuning de ViT pre-treinado
- Comparacao com CNN (ResNet) em mesmo dataset
- Attention maps para interpretabilidade
- Dataset: CIFAR-10 (torchvision)

#### 5. modeling/efficientnet_transfer.py
- EfficientNet com timm (PyTorch Image Models)
- Comparacao de variantes (B0 vs B3)
- Progressive resizing
- Mixup e CutMix augmentation
- Dataset: CIFAR-10 ou Oxford Pets

### Validation (3 arquivos)

#### 6. validation/gradcam_interpretability.py
- Grad-CAM com pytorch-grad-cam
- Visualizacao de heatmaps sobre imagens
- Comparacao de Grad-CAM entre classes
- Grad-CAM++ e Score-CAM como alternativas
- Dataset: modelo treinado na F4.1

#### 7. validation/adversarial_robustness.py
- FGSM (Fast Gradient Sign Method) attack
- PGD (Projected Gradient Descent) attack
- Accuracy vs epsilon (intensidade do ataque)
- Adversarial training basico para robustez
- Dataset: CIFAR-10 + modelo treinado

#### 8. validation/model_calibration_vision.py
- Reliability diagram para CNNs
- Temperature scaling para calibracao
- ECE (Expected Calibration Error)
- Comparacao antes e depois de calibracao
- Dataset: modelo treinado na F4.1

### Visualization (1 arquivo)

#### 9. visualization/vision_plots.py
- Grid de imagens com predicoes e ground truth
- Confusion matrix para classificacao
- Grad-CAM heatmaps em grid
- Bounding boxes com scores (deteccao)
- Masks de segmentacao sobrepostas
- Training curves (loss e metricas por epoca)
- t-SNE dos features da penultima camada

---

## Formato: cada script com docstring, main(), RANDOM_STATE = 42

---

## Criterios de Aceite

- [x] 9 scripts Python criados nas subpastas corretas
- [x] modeling/cnn_classification.py — CNN + ResNet transfer learning
- [x] modeling/object_detection_yolo.py — YOLOv8 com ultralytics
- [x] modeling/segmentation_unet.py — U-Net com Dice loss
- [x] modeling/vision_transformer.py — ViT fine-tuning com Hugging Face
- [x] modeling/efficientnet_transfer.py — EfficientNet com timm e Mixup/CutMix
- [x] validation/gradcam_interpretability.py — Grad-CAM e variantes
- [x] validation/adversarial_robustness.py — FGSM e PGD com accuracy vs epsilon
- [x] validation/model_calibration_vision.py — Temperature scaling e ECE
- [x] visualization/vision_plots.py — Grid, confusion matrix, Grad-CAM, t-SNE features
- [x] Todos os scripts passam verificacao de sintaxe Python
- [x] Todos os scripts tem docstring, funcoes organizadas e main()
- [x] Codigo usa PyTorch + torchvision como stack principal

---

## Bibliotecas Utilizadas

| Biblioteca | Versao Minima | Uso |
|------------|---------------|-----|
| torch | >= 2.0 | CNNs, treinamento, modelos |
| torchvision | >= 0.15 | Datasets, transforms, modelos pre-treinados |
| timm | >= 0.9 | EfficientNet, ViT, modelos de imagem |
| ultralytics | >= 8.0 | YOLOv8 |
| transformers | >= 4.30 | Vision Transformers (Hugging Face) |
| pytorch-grad-cam | >= 1.4 | Grad-CAM e variantes |
| matplotlib | >= 3.7 | Visualizacoes |
| seaborn | >= 0.12 | Visualizacoes estatisticas |
| scikit-learn | >= 1.3 | t-SNE, metricas |

---

## Ferramentas Necessarias

- **Read**, **WebSearch**, **Write**

---

**End of Specification**

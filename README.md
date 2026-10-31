# Comparative Analysis of Deep Learning Architectures for Pneumonia Detection from Chest X-Ray Images

This project compares three deep learning models for classifying chest X-ray images as **NORMAL** or **PNEUMONIA**:

- Custom CNN
- ResNet50
- DenseNet121

## Dataset

The primary experiments use the Chest X-Ray Images (Pneumonia) dataset by Kermany et al. The models use the same train, validation, and test split. The test set contains 624 images.

A supplementary evaluation uses a small subset of NIH ChestX-ray14. Its labels differ from the primary dataset, so those results are reported separately and should be interpreted cautiously.

## Repository Structure

- `notebooks/` — dataset exploration, preprocessing, and model experiments
- `preprocessing/` — preprocessing code
- `results/` — saved evaluation tables and model files
- `models/` — saved DenseNet121 model
- `report/` — project report

## Main Test-Set Results

| Model | Accuracy | Precision | Recall | F1-score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Custom CNN | 88.94% | 87.59% | 95.90% | 91.55% | 95.44% |
| ResNet50 | 71.79% | 69.18% | 98.97% | 81.43% | 92.58% |
| DenseNet121 | 75.48% | 72.23% | 98.72% | 83.42% | 93.69% |

The Custom CNN achieved the best overall accuracy, F1-score, and ROC-AUC on the primary test set. ResNet50 achieved the highest pneumonia recall, with more false-positive predictions for NORMAL images.

## Notes and Limitations

- The validation split contains only 16 images, so validation-based model selection is limited.
- The NIH subset is a preliminary external check; its “No Finding” records are not equivalent to clinically confirmed normal cases.
- Results are experimental and are not intended for clinical diagnosis.

## Team

- Tanushree Ashok Hegde
- Sathwik
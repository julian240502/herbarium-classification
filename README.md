# README - Projet de Classification d'Images

## ⚠️ IMPORTANT ⚠️
Les dossiers `train`, `test` et `validation` sont vides car le dataset utilisé pour ce projet est **privé**. Je n'ai pas le droit de le partager publiquement. Toutefois, pour comprendre la jointure entre les fichiers CSV et les images, **les noms des images sont stockés dans la colonne `normalized_name` des fichiers CSV**.

---

## 📂 Structure du projet

### 1. `modeleMetrics/`
Ce dossier contient les métriques des différents modèles testés :

- `coatnet_0_rw_224.sw_in1k`
- `davit_small.msft_in1k`
- `mobilevitv2-1.0-imagenet1k-256`
- `swinv2-tiny-patch4-window8-256`

Chaque dossier contient un fichier **JSON** détaillant les métriques de l'entraînement et les graphiques correspondants.

**Note :** Les modèles finetunés n'ont pas été sauvegardés car ils ne sont pas exploitables en l'état.

---

### 2. `train/`, `test/`, `validation/`
Ces dossiers sont destinés à contenir les images utilisées pour l'entraînement, la validation et le test du modèle.

---

### 3. `annotations/`
Ce dossier contient les fichiers CSV avec les annotations des images (`train`, `test` et `validation`). Il inclut également :

- **`process_annotations.py`** : Script permettant de traiter le fichier brut d'annotations `Projet_DL.csv` pour générer un dataset filtré (`filtered_new_data.csv`).

---

## 🚀 Installation des dépendances
Avant d'exécuter les scripts, installe les dépendances requises en exécutant :
```bash
pip install -r requirements.txt
```

---

## 📜 Scripts principaux

### `structureWorkspace.py`
- **Entrée** : Dataset filtré (`filtered_new_data.csv`) et dossier d'images brut.
- **Sortie** : Dataset organisé avec images réparties en trois dossiers (`train`, `test`, `validation`) et fichiers CSV d'annotations correspondants.

### `training.ipynb`
- Notebook utilisé pour l'entraînement du modèle.

---

## 📝 Remarque
Ce projet repose sur la classification d'images à l'aide de modèles pré-entraînés et finetunés. Cependant, en raison des restrictions liées aux données, seules les structures de fichiers et les scripts de traitement sont fournis.

---

🔧 **Bon développement !**


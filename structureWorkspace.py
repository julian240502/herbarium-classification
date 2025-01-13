import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import shutil

# Configuration
base_dir = os.getcwd()
images_dir = os.path.join(base_dir, 'all_image_herbier')
csv_file = os.path.join(base_dir, 'annotations/filtered_new_data.csv')

# Création des dossiers
train_dir = os.path.join(base_dir, 'train')
test_dir = os.path.join(base_dir, 'test')
val_dir = os.path.join(base_dir, 'validation')

def create_directories():
    """Créer les répertoires nécessaires"""
    for directory in [train_dir, test_dir, val_dir]:
        if not os.path.exists(directory):
            os.makedirs(directory)

def split_dataset():
    """Diviser le dataset et créer les CSV correspondants"""
    # Lecture du CSV principal
    df = pd.read_csv(csv_file, sep=';')
    
    # Liste des images disponibles
    image_files = [f for f in os.listdir(images_dir) if f.endswith(('.jpg', '.png', '.jpeg'))]
    
    # Première division : séparer train+validation et test (80/20)
    train_val_files, test_files = train_test_split(
        image_files,
        test_size=0.2,
        random_state=42
    )
    
    # Deuxième division : séparer train et validation (75/25 du train+validation)
    train_files, val_files = train_test_split(
        train_val_files,
        test_size=0.25,
        random_state=42
    )
    
    # Fonction pour copier les fichiers
    def copy_files(files, target_dir):
        for file in files:
            src = os.path.join(images_dir, file)
            dst = os.path.join(target_dir, file)
            shutil.copy2(src, dst)
    
    # Copier les fichiers dans leurs dossiers respectifs
    copy_files(train_files, train_dir)
    copy_files(test_files, test_dir)
    copy_files(val_files, val_dir)
    
    # Créer les CSV correspondants
    def create_subset_csv(files, output_path):
        # Obtenir les noms de fichiers sans extension
        file_names = [os.path.splitext(f)[0] for f in files]
        # Filtrer le DataFrame pour ces fichiers
        subset_df = df[df['normalized_name'].isin(file_names)]
        # Sauvegarder le CSV
        subset_df.to_csv(output_path, index=False, sep=';')
        return len(subset_df)
    
    # Créer les trois CSV
    train_csv = os.path.join(base_dir, 'train.csv')
    test_csv = os.path.join(base_dir, 'test.csv')
    val_csv = os.path.join(base_dir, 'validation.csv')
    
    n_train = create_subset_csv(train_files, train_csv)
    n_test = create_subset_csv(test_files, test_csv)
    n_val = create_subset_csv(val_files, val_csv)
    
    return n_train, n_test, n_val

try:
    # Créer les dossiers
    create_directories()
    
    # Diviser le dataset et créer les CSV
    n_train, n_test, n_val = split_dataset()
    
    # Afficher les statistiques
    total = n_train + n_test + n_val
    print(f"\nDivision du dataset complétée ({total} images au total) :")
    print(f"Train      : {n_train} images ({n_train/total*100:.1f}%)")
    print(f"Test       : {n_test} images ({n_test/total*100:.1f}%)")
    print(f"Validation : {n_val} images ({n_val/total*100:.1f}%)")
    
    print(f"\nFichiers créés :")
    print(f"Images train      : {train_dir}")
    print(f"Images test       : {test_dir}")
    print(f"Images validation : {val_dir}")
    print(f"CSV train        : train.csv")
    print(f"CSV test         : test.csv")
    print(f"CSV validation   : validation.csv")

except Exception as e:
    print(f"Une erreur s'est produite : {e}")
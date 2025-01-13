Dans le dossier "modeleMetrics" vous trouverez les dossiers :

-coatnet_0_rw_224.sw_in1k
-davit_small.msft_in1k
-mobilevitv2-1.0-imagenet1k-256
-swinv2-tiny-patch4-window8-256

Un fichier json contenant les metrics de training de chaque modèle, et leur graphique. Je n'ai pas sauvegardé le modèle après finetuning car il n'est pas exploitable.


Les dossiers "train", "test" et "validation" contiennent les images qui seront utilisé pour l'entrainement du modèle.

Le dossier "annotations" contient les fichiers csv contenant les annotations de mes images de train/test/validation, mais aussi :

-"process_annotations.py" qui prend un le fichier d'annotations brut en entrée (Projet_DL.csv) et en sortie renvoi le dataset filtré (filtered_new_data.csv).

Lancer la commande "pip install -r requirements.txt" pour télécharger les frameworks nécessaire pour lancer l'entrainement.


Le fichier "structureWorkspace.py", prend en entrée le dataset fitlré, et le dossier d'image brut, afin d'avoir en sortie un dataset splitté 3 (dossier image + csv d'annotations).

Et pour finir le fichier "training.ipynb" est utilisé pour l'entrainement.




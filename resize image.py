# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 08:46:27 2024

@author: elisa
"""

from PIL import Image
import os

# Dossier contenant les images à redimensionner
input_folder = 'C:/Users/elisa/projectteststylef/static/images/'
# Dossier de sortie pour les images redimensionnées
output_folder = 'C:/Users/elisa/projectteststylef/static/resized_images/'


# Crée le dossier de sortie s'il n'existe pas
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Taille cible pour les images redimensionnées
target_size = (800, 600)  # Vous pouvez ajuster cette taille selon vos besoins

# Parcourt toutes les images dans le dossier d'entrée
for filename in os.listdir(input_folder):
    if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
        # Ouvre l'image
        img = Image.open(os.path.join(input_folder, filename))
        # Redimensionne l'image
        img_resized = img.resize(target_size, Image.Resampling.LANCZOS)
        # Sauvegarde l'image redimensionnée dans le dossier de sortie
        img_resized.save(os.path.join(output_folder, filename))

print("Redimensionnement terminé.")

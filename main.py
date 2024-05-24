# Librairies générales
import matplotlib.pyplot as plt
import numpy as np
import random

# Librairies pour l'affichage
import cv2

# Librairies internes
from images.image import afficher
from images.image import calculer_centroide
from images.image import calculer_vecteurs_propres
from images.image import estimer_angle_rotation
from images.image import appliquer_rotation


def main():

    # Définir les dimensions des caractères aléatoires
    hauteur = 150
    largeur = 150

    # Paramètres de la police d'écriture
    police = cv2.QT_FONT_NORMAL
    echelle = 3
    epaisseur = 3
    couleur = (128, 0, 0)

    while True:

        # Caractère aléatoire à replacer
        texte = chr(random.randint(ord('A'), ord('Z')))

        # Obtenir les dimensions
        taille_texte = cv2.getTextSize(texte, police, echelle, epaisseur)[0]

        # Calculer la position du centre du caractère
        x = (largeur - taille_texte[0]) // 2
        y = (hauteur + taille_texte[1]) // 2

        # Créer un canevas 150 x 150 pixels
        image = np.random.randint(0, 5, (hauteur, largeur))

        # Ajouter le caractère au canevas
        cv2.putText(image, texte, (x, y), police, echelle, couleur, epaisseur)

        # Afficher le caractère brut
        afficher(image, 'Caractère original')

        # Appliquer la rotation aléatoire de +/- [20, 45] degrés
        angle_rotation_degres = (-1) ** random.randint(0, 1) * random.randint(20, 45)
        caractere_tourne = appliquer_rotation(image, angle_rotation_degres)

        # Afficher l'angle réel
        print(f'Angle de rotation: {angle_rotation_degres} degrés')

        # Initialisation des points de départs et de fins des 2 vecteurs propres
        x0 = calculer_centroide(caractere_tourne)[0]
        y0 = calculer_centroide(caractere_tourne)[1]
        x1 = calculer_vecteurs_propres(caractere_tourne)[0, 0]
        y1 = calculer_vecteurs_propres(caractere_tourne)[0, 1]
        x2 = calculer_vecteurs_propres(caractere_tourne)[1, 0]
        y2 = calculer_vecteurs_propres(caractere_tourne)[1, 1]

        # Afficher des vecteurs propres
        plt.plot([x0, x0 + x0 * x1], [y0, y0 + y0 * y1], color='b')
        plt.plot([x0, x0 + x0 * x2], [y0, y0 + y0 * y2], color='r')

        # Afficher le caractère tourné
        afficher(caractere_tourne, 'Caractère tourné')

        # Estimer l'angle de rotation
        angle_rotation_approximatif = estimer_angle_rotation(caractere_tourne)

        # Afficher l'angle de rotation estimé
        print(f'Angle de rotation estimé: {angle_rotation_approximatif} degrés')

        # Corriger la rotation
        caractere_corrige = appliquer_rotation(caractere_tourne, -angle_rotation_approximatif)

        # Afficher le caractère repositionné
        afficher(caractere_corrige, 'Caractère repositionné')


if __name__ == '__main__':
    main()

# Librairies générales
import math
import numpy as np
import os

# Librairies images
import matplotlib.pyplot as plt

# Constantes internes
from constantes import RGB_MAX


def charger_jpeg(chemin: str) -> np.ndarray:
    """
    Charge une image donnée en format JPEG et la retourne sous la forme d'un tableau NumPy.

    Arguments : chemin (str) : Le chemin menant vers l'image à charger.

    Retourne : (np.ndarray) : L'image chargée.
    """

    # Valider que l'image existe
    if not os.path.exists(chemin):
        raise FileExistsError(f"Le fichier n'existe pas : {chemin}")

    # Valider qu'il s'agit d'une image en format JPEG
    if not chemin.endswith('.jpg'):
        raise TypeError(f'Seules les images en format JPEG sont supportées')

    # Charger l'image avec la librairie Matplotlib
    image = plt.imread(chemin) / RGB_MAX

    # Valider le chargement
    if image is None:
        raise IOError("Échec lors de l'ouverture de l'image")

    return image


def afficher(image: np.ndarray, titre: str = '') -> None:
    """
    Affiche une image donnée sous forme de tableau NumPy.

    Arguments : image (np.ndarray) : L'image à afficher.
                titre (str, optionnel) : Titre de la figure. Chaîne de caractères vide par défaut.

    Retourne : Rien.
    """

    # Créer l'image
    plt.imshow(image, cmap='gray')

    # Ajout d'une grille
    plt.grid(True, color='white', linestyle='--', alpha=0.5)

    # Nommer les axes
    plt.xlabel('Largeur')
    plt.ylabel('Hauteur')

    # Ajouter le titre
    plt.title(titre)

    # Afficher l'image
    plt.show()


def calculer_differences(image1: np.ndarray, image2: np.ndarray) -> float:
    """
    Description : Calcule la somme des distances absolues entre chacun des pixels
                  correspondants de deux images.

    Arguments : La première image.
                La deuxième image.

    Retourne : La distance entre les deux images.
    """

    # Calculer la somme des distances absolues entre chacun des points des images
    difference = np.abs(image1 - image2)
    distance = np.sum(difference)

    return distance


def calculer_moments_premier_ordre(image_reference: np.ndarray) -> tuple[int, int, int]:
    """
    Description : Calcule les moments du premier ordre d’une image.

    Arguments : L’image de référence.

    Retourne : Le moment en 𝑥 (c.-à-d. la coordonnée 𝑗 du tableau-image).
               Le moment en 𝑦 (c.-à-d. la coordonnée 𝑖 du tableau-image).
               La « masse » de l’image.

    Requis : • Le moment du premier ordre en 𝑥 correspond à ∑ ∑(𝑝𝑖𝑗 ⋅ 𝑗).
             • Le moment du premier ordre en 𝑦 correspond à ∑ ∑(𝑝𝑖𝑗 ⋅ 𝑖).
             • La masse de l’image correspond au dénominateur ∑ ∑ 𝑝𝑖𝑗.
    """

    # Trouver les dimensions du tableau NumPy pour le parcourir
    nb_lignes, nb_colonnes = image_reference.shape

    # Initialiser nos variables
    moment_premier_ordre_en_x = 0
    moment_premier_ordre_en_y = 0
    masse_image_premier_ordre = 0

    # Parcourir le tableau avec les dimensions
    for i in range(nb_lignes):
        for j in range(nb_colonnes):

            # Calculer les moments du premier ordre
            moment_premier_ordre_en_x += image_reference[i, j] * j
            moment_premier_ordre_en_y += image_reference[i, j] * i

            # Calculer la masse de l'image
            masse_image_premier_ordre += image_reference[i, j]

    return moment_premier_ordre_en_x, moment_premier_ordre_en_y, masse_image_premier_ordre


def calculer_centroide(image_reference: np.ndarray) -> tuple[float, float]:
    """
    Description : Calcule le centroïde d’une image.

    Arguments : L’image de référence.

    Retourne : Les coordonnées (𝑥𝑐, 𝑦𝑐) du centroïde.

    Requis : Utilisez la formule donnée dans l’introduction de cette section pour le calcul du
             centroïde. (𝑥𝑐, 𝑦𝑐) = (∑∑(𝑝𝑖𝑗 ⋅ 𝑖) / ∑∑ 𝑝𝑖𝑗, ∑∑(𝑝𝑖𝑗 ⋅ 𝑗) / ∑∑ 𝑝𝑖𝑗)
    """

    # Reprendre les viariable de la fonction calculer_moments_premier_ordre
    moment_premier_ordre_en_x, moment_premier_ordre_en_y, masse_image_premier_ordre = \
        (calculer_moments_premier_ordre(image_reference))

    # Contourner l'occurence où la variable masse_image_premier_ordre est égale à 0.
    if masse_image_premier_ordre > 0:

        # Calculer les coordonnées du centroïde
        xc = float(moment_premier_ordre_en_x / masse_image_premier_ordre)
        yc = float(moment_premier_ordre_en_y / masse_image_premier_ordre)
        coordonnees_centroides = (xc, yc)

    # Forcer les coordonnées du centroïde à (0,0) dans le cas où la variable masse_image_premier_ordre est égale à 0.
    else:
        coordonnees_centroides = (0.0, 0.0)

    return coordonnees_centroides


def calculer_moments_deuxieme_ordre(image_reference: np.ndarray) -> tuple[int, int, int]:
    """
    Description : Calcule les moments du deuxième ordre d’une image.

    Arguments : L’image de référence.

    Retourne : Le second moment de masse en 𝜇𝑥𝑦 (le moment de masse 𝜇𝑥𝑦 de deuxième ordre).
               Le second moment de masse en 𝜇𝑥𝑥 (le moment de masse 𝜇𝑥𝑥 de deuxième ordre).
               Le second moment de masse en 𝜇𝑦𝑦 (le moment de masse 𝜇𝑦𝑦 de deuxième ordre).
    """

    # Trouver les dimensions du tableau NumPy pour le parcourir
    nb_lignes, nb_colonnes = image_reference.shape

    # Initialiser nos variables
    moment_deuxieme_ordre_en_xy = 0
    moment_deuxieme_ordre_en_xx = 0
    moment_deuxieme_ordre_en_yy = 0

    # Définition des centroides pour alléger le code
    xc = calculer_centroide(image_reference)[0]
    yc = calculer_centroide(image_reference)[1]

    # Parcourir le tableau avec les dimensions
    for i in range(nb_lignes):
        for j in range(nb_colonnes):

            # Calculer les moments du deuxième ordre
            moment_deuxieme_ordre_en_xy = (image_reference[j, i] * (i - xc) * (j - yc)) + moment_deuxieme_ordre_en_xy
            moment_deuxieme_ordre_en_xx = (image_reference[j, i] * (i - xc) ** 2) + moment_deuxieme_ordre_en_xx
            moment_deuxieme_ordre_en_yy = (image_reference[j, i] * (j - yc) ** 2) + moment_deuxieme_ordre_en_yy

    return moment_deuxieme_ordre_en_xy, moment_deuxieme_ordre_en_xx, moment_deuxieme_ordre_en_yy


def calculer_matrice_covariance(image_reference: np.ndarray) -> np.ndarray[[int, int], [int, int]]:
    """
    Description : Calcule la matrice de covariance d’une image.

    Arguments : L’image de référence.

    Retourne : La matrice de covariance.
    """

    # Charger les moments de deuxième ordre
    second_moment_xy = calculer_moments_deuxieme_ordre(image_reference)[0]
    second_moment_xx = calculer_moments_deuxieme_ordre(image_reference)[1]
    second_moment_yy = calculer_moments_deuxieme_ordre(image_reference)[2]

    # Initialiser la matrice de covariance et y insérer les moments de deuxième ordre
    matrice_covariance = np.array([[second_moment_xx, second_moment_xy], [second_moment_xy, second_moment_yy]])

    return matrice_covariance


def calculer_vecteurs_propres(image_reference: np.ndarray) -> np.ndarray:
    """
      Description : Calcule les vecteurs propres d'une image.

      Arguments : L’image de référence.

      Retourne : Le premier vecteur propre.
                  Le deuxième vecteur propre.

      Requis : 1. Les valeurs propres doivent être calculées avec l’équation 9.
               2. Les vecteurs propres doivent calculer (équations 10 et 11).
               3. Les vecteurs propres doivent être normalisés.
               4. Vous devez retourner les vecteurs propres en ordre décroissant de
                valeurs propres.
      """

    # Initialisation des valeurs qui vont être utilisé dans l'équation quadratique [9]
    a = 1
    b = -(calculer_moments_deuxieme_ordre(image_reference)[1] + calculer_moments_deuxieme_ordre(image_reference)[2])
    c = ((calculer_moments_deuxieme_ordre(image_reference)[1] * calculer_moments_deuxieme_ordre(image_reference)[2]) -
         (calculer_moments_deuxieme_ordre(image_reference)[0]) ** 2)

    # Obtention des valeurs propres avec l'équation
    valeure_propre_1 = (- b + ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)
    valeure_propre_2 = (- b - ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)

    # Initialisation des vecteurs propres
    vecteur_1 = np.array([calculer_moments_deuxieme_ordre(image_reference)[0],
                          valeure_propre_1 - calculer_moments_deuxieme_ordre(image_reference)[1]])
    vecteur_2 = np.array([calculer_moments_deuxieme_ordre(image_reference)[0],
                          valeure_propre_2 - calculer_moments_deuxieme_ordre(image_reference)[1]])

    # Normalisation des vecteurs
    vecteur_1_norm = vecteur_1 / (vecteur_1[0] ** 2 + vecteur_1[1] ** 2) ** 0.5
    vecteur_2_norm = vecteur_2 / (vecteur_2[0] ** 2 + vecteur_2[1] ** 2) ** 0.5

    # Retour des vecteurs propres normalisés
    if valeure_propre_1 > valeure_propre_2:
        return np.array([vecteur_1_norm, vecteur_2_norm])
    else:
        return np.array([vecteur_2_norm, vecteur_1_norm])


def estimer_angle_rotation(image_reference: np.ndarray) -> float:
    """
    Description : Estime l’angle de rotation d’une image.

    Arguments : L’image de référence.

    Retourne : L'angle estimé en degrés
    """

    # Initialisation des valeurs qui seront utilisées dans l'équation pour trouver l'angle
    vecteur_1_x = calculer_vecteurs_propres(image_reference)[0, 0]
    vecteur_2_x = calculer_vecteurs_propres(image_reference)[1, 0]

    # Utiliser l'équation fournie
    theta_radiant = math.pi / 2 - abs(math.atan2(vecteur_2_x, vecteur_1_x))
    theta_degree = theta_radiant * 180 / math.pi

    return theta_degree


def appliquer_rotation(image: np.ndarray, angle_degres: float) -> np.ndarray:
    """
    Applique une rotation à une image.

    Note : Ceci est une implémentation manuelle.

    Arguments : image (np.ndarray) : L'image à tourner.
                angle_degres (float) : L'angle de rotation en degrés.

    Retourne : (np.ndarray) : L'image tournée.
    """

    # Trouver le centre de l'image
    xc, yc = image.shape[1] // 2, image.shape[0] // 2

    # Transformer l'angle en radians
    angle_radians = np.radians(angle_degres)

    # Les valeurs trigonométriques de l'angle
    cos_theta = np.cos(angle_radians)
    sin_theta = np.sin(angle_radians)

    # Extraire les dimensions de l'image
    hauteur, largeur = image.shape

    # Initialiser l'image tournée
    image_tournee = np.zeros((hauteur, largeur)) * RGB_MAX

    # Appliquer la rotation
    for y in range(hauteur):
        for x in range(largeur):

            # Calculer les nouvelles coordonnées du pixel courant
            x_ = (x - xc) * cos_theta - (y - yc) * sin_theta + xc
            y_ = (x - xc) * sin_theta + (y - yc) * cos_theta + yc

            # Trouver le pixel le plus près
            x_voisin = int(x_)
            y_voisin = int(y_)

            # Copier la couleur d'un voisin immédiat pour éviter les inclusions
            if 0 <= x_voisin < largeur and 0 <= y_voisin < hauteur:
                image_tournee[y, x] = image[y_voisin, x_voisin]

    return image_tournee

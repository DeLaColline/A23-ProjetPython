# Librairies générales
import numpy as np

# Librairies internes
from donnees.donnees import charger_references
from donnees.donnees import charger_centroides_references
from etiquettes.etiquette import decouper
from images.image import calculer_differences
from images.image import calculer_centroide

# Constantes internes
from constantes import DIMENSIONS_ATTENDUES_IMAGE
from constantes import ETIQUETTE_NB_CARACTERES
from constantes import NB_CARACTERES_REFERENCE
from constantes import REFERENCE_LETTRES
from constantes import REFERENCE_CHIFFRES


def identifier_caracteres_avec_distances(image_caractere: np.ndarray, base_donnees_caracteres_references: dict)\
                                                                                                    -> str | int:
    """
    Identifie un caractère alphanumérique par rapport à la distance avec un ensemble de caractères de références

    Arguments : Image du caractère à identifier
                Base de données qui contient les caractères de référence

    Retourne : Valeur du caractère identifié (int pour les chiffres et str pour les lettres)

    Requis : 1. Si la taille de l’image reçue ne correspond pas à la taille attendue de 40 pixels par 40 pixels,
               déclenchez une erreur.
             2. Si le caractère est alphabétique, retournez une chaîne de caractères.
             3. Si le caractère est numérique, retournes un entier.
             4. Le caractère identifié doit correspondre à celui dont la distance par rapport au caractère reçu
                est la plus petite de l’ensemble des caractères de référence.
    """

    # Vérifier si la taille de l'image est bien de 40 pixels par 40 pixels
    if np.shape(image_caractere) != DIMENSIONS_ATTENDUES_IMAGE:
        raise ValueError("La taille de l'image n'est pas de 40x40 pixels")

    # Charger la base de données des caractères de références et initialiser une liste où stocker les distances
    images_references = list(base_donnees_caracteres_references.values())
    caracteres_references = list(base_donnees_caracteres_references.keys())
    distances = []

    # Calculer la distance entre l'image du caractère et chacune des images de références et stocker dans une liste
    for i in range(NB_CARACTERES_REFERENCE):
        image_reference = images_references[i]
        distance = calculer_differences(image_caractere, image_reference)
        distances.append(distance)

    # Trouver la plus petite distance ainsi que le caractère qui lui correspond
    distance_min = min(distances)
    index_distance_min = distances.index(distance_min)
    caractere_identifie = caracteres_references[index_distance_min]

    # Vérifier si le caractère trouvé correspond à une lettre ou un chiffre
    if caractere_identifie in REFERENCE_LETTRES:
        caractere = str(caractere_identifie)
        return caractere
    elif caractere_identifie in REFERENCE_CHIFFRES:
        caractere = int(caractere_identifie)
        return caractere


def lire_etiquettes_distances(etiquette: np.ndarray) -> str:
    """
    Description : Identifie une étiquette à partir de l’identification de caractères basée sur la distance.

    Arguments : Une image qui correspond à une étiquette.

    Retourne : Une chaîne de caractères qui correspond à la lecture de l’étiquette.
    """

    # Charger la base de données des caractères de références
    base_donnees_caracteres_references = charger_references()

    # Découper l'étiquette pour pouvoir analyser chacune des images des caractères
    images_caracteres = decouper(etiquette)

    # Initialiser une chaîne de caractère qui va contenir les caractères de chacune des images
    valeur_etiquette = ''

    # Analyser chacune des images et déterminer de quel caractère il s'agit puis l'ajouter à la chaîne de caractère
    for i in range(ETIQUETTE_NB_CARACTERES):
        image_caractere = images_caracteres[i]
        caractere_identifie = identifier_caracteres_avec_distances(image_caractere, base_donnees_caracteres_references)
        valeur_etiquette += str(caractere_identifie)

    return valeur_etiquette


def identifier_caractere_avec_centroides(image_caractere: np.ndarray, base_donnees_centroides_references: dict)\
                                                                                                   -> str | int:
    """
    Identifie un caractère alphanumérique par rapport à son centroïde avec un ensemble de caractères de références

    Arguments : Image du caractère à identifier
                Base de données qui contient les centroïdes de référence

    Retourne : Valeur du caractère identifié (int pour les chiffres et str pour les lettres)

    Requis : 1. Si la taille de l’image reçue ne correspond pas à la taille attendue de 40 pixels par 40 pixels,
               déclenchez une erreur.
             2. Si le caractère est alphabétique, retournez une chaîne de caractères.
             3. Si le caractère est numérique, retournes un entier.
             4. Le caractère identifié doit correspondre à celui dont le centroïde est le plus proche
                par rapport au caractère reçu de l’ensemble des caractères de référence.
    """

    # Vérifier si la taille de l'image est bien de 40 pixels par 40 pixels
    if np.shape(image_caractere) != DIMENSIONS_ATTENDUES_IMAGE:
        raise ValueError("La taille de l'image n'est pas de 40x40 pixels")

    # Calculer le centroïde de l'image du caractère à analyser
    coordonnees_centroide = calculer_centroide(image_caractere)
    xc, yc = coordonnees_centroide

    # Trouver le caractère dans la base de données dont le centroïde a la plus petite distance comparée à notre image
    distance_min = min(base_donnees_centroides_references.items(),
                       key=lambda item: ((item[1][0] - xc) ** 2 + (item[1][1] - yc) ** 2) ** 0.5)
    caractere_identifie = distance_min[0]

    # Vérifier si le caractère trouvé correspond à une lettre ou un chiffre
    if caractere_identifie in REFERENCE_LETTRES:
        caractere = str(caractere_identifie)
        return caractere
    elif caractere_identifie in REFERENCE_CHIFFRES:
        caractere = int(caractere_identifie)
        return caractere


def lire_etiquette_centroides(etiquette: np.ndarray) -> str:
    """
    Description : Identifie une étiquette à partir de l’identification de caractères basée sur le centroïde.

    Arguments : Une image qui correspond à une étiquette.

    Retourne : Une chaîne de caractères qui correspond à la lecture de l’étiquette.
    """

    # Charger la base de données des centroïdes de références
    base_donnees_centroides_references = charger_centroides_references()

    # Découper l'étiquette pour pouvoir analyser chacune des images des caractères
    images_caracteres = decouper(etiquette)

    # Initialiser une chaîne de caractère qui va contenir les caractères de chacune des images
    valeur_etiquette = ''

    # Analyser chacune des images et déterminer de quel caractère il s'agit puis l'ajouter à la chaîne de caractère
    for i in range(ETIQUETTE_NB_CARACTERES):
        image_caractere = images_caracteres[i]
        caractere_identifie = identifier_caractere_avec_centroides(image_caractere, base_donnees_centroides_references)
        valeur_etiquette += str(caractere_identifie)

    return valeur_etiquette

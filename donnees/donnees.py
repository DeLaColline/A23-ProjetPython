# Librairies générales
import numpy as np
import pickle
import os

# Librairies internes
from images.image import charger_jpeg
from images.image import calculer_centroide

# Constantes internes
from constantes import CHEMIN_ETIQUETTES
from constantes import CHEMIN_REFERENCES
from constantes import CHEMIN_FICHIER_CENTROIDES
from constantes import NB_CARACTERES_REFERENCE
from constantes import REFERENCE_LETTRES_CHIFFRES


def charger_references() -> dict[str, np.ndarray]:
    """
    Charge la base de données de caractères de référence

    Arguments : Aucuns

    Retourne : Un dictionnaire dont les clés correspondent aux caractères et dont les valeurs correspondent aux
               images de références de ces derniers
    """

    # Initialiser le dictionnaire qui va contenir les images de références
    base_donnees_caracteres_references = {}

    # Insérer les images de références une à une dans le dictionnaire en utilisant la fonction charger_jpeg
    for i in range(NB_CARACTERES_REFERENCE):
        caractere = REFERENCE_LETTRES_CHIFFRES[i]
        image = charger_jpeg(f'{CHEMIN_REFERENCES}{caractere}.jpg')
        base_donnees_caracteres_references[caractere] = image

    return base_donnees_caracteres_references


def charger_etiquettes() -> list[np.ndarray]:
    """"
    Description : Charge la base de données d’étiquettes

    Arguments : Aucuns.

    Retourne : Une liste qui contient les images des étiquettes sous la forme de tableaux NumPy.
    """

    # Initialiser la liste qui va contenir les images de références
    base_donnees_images_etiquettes = []
    nb_etiquettes = 40

    # Insérer les images de références une à une dans la liste en utilisant la fonction charger_jpeg
    for i in range(1, nb_etiquettes+1):
        etiquette = i
        image = charger_jpeg(f'{CHEMIN_ETIQUETTES}{etiquette}.jpg')
        base_donnees_images_etiquettes.append(image)

    return base_donnees_images_etiquettes


def calculer_centroides_references() -> None:
    """
    Description : Calcule les centroïdes des références et les stocke dans un fichier binaire
                  dans le fichier de données du projet.

    Arguments : Aucuns.

    Retourne : Rien.
    """

    # Charger la base de données des caractères de références
    base_donnees_caracteres_references = charger_references()
    images_references = list(base_donnees_caracteres_references.values())
    caracteres_references = list(base_donnees_caracteres_references.keys())

    # Initialiser le dictionnaire qui va contenir les centroïdes de chaque caractère
    base_donnees_centroides_references = {}

    # Parcourir chacun des caractères et calculer son centroïde
    for i in range(NB_CARACTERES_REFERENCE):
        caractere = caracteres_references[i]
        image = images_references[i]
        centroide = calculer_centroide(image)

        # Stocker le centroïde dans la base de donnée
        base_donnees_centroides_references[caractere] = centroide

    # Écrire le dossier pickle
    with open(f'{CHEMIN_FICHIER_CENTROIDES}', 'wb') as centroides:
        pickle.dump(base_donnees_centroides_references, centroides)


def charger_centroides_references() -> dict[str, tuple[float, float]]:
    """
    Description : Charge les centroïdes de références sauvegardées au préalable.

    Arguments : Aucuns.

    Retourne : Chargez la base de données des centroïdes décrite à la procédure précédente avec la libraire pickle.
               N’oubliez pas que des exemples sont donnés dans main.py pour cette dernière.
    """

    # Valider que le chemin vers les centroïdes existe
    if not os.path.exists(f'{CHEMIN_FICHIER_CENTROIDES}'):
        FileExistsError('Exécutez calculer_centroides_references en premier!')

    # Charger en mode lecture binaire ('rb')
    with open(f'{CHEMIN_FICHIER_CENTROIDES}', 'rb') as centroides:
        base_donnees_centroides_references = pickle.load(centroides)

    return base_donnees_centroides_references

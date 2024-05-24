# Librairies générales
import numpy as np

# Constantes internes
from constantes import CARACTERE_NB_PIXELS_COTE
from constantes import ETIQUETTE_NB_CARACTERES


def decouper(etiquette: np.ndarray) -> list[np.ndarray]:
    """
    Description : Découpe chacun des caractères d’une étiquette.

    Arguments : Une image qui correspond à une étiquette.

    Retourne : Une liste qui contient les 13 caractères sous la forme d’images en tableaux NumPy.
    """

    # Initialiser une liste pour stocker les 13 caractères sous la forme de tableaux NumPy
    images_caracteres = []

    # Découper et insérer les tableaux NumPy de chacun des caractères dans la liste que nous avons initialisée
    for i in range(ETIQUETTE_NB_CARACTERES):
        debut = i * CARACTERE_NB_PIXELS_COTE
        fin = (i + 1) * CARACTERE_NB_PIXELS_COTE
        image_caractere = etiquette[:, debut: fin]
        images_caracteres.append(image_caractere)

    return images_caracteres

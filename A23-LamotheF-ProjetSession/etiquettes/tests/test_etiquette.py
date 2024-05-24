# Librairies internes
from images.image import afficher
from images.image import charger_jpeg

# Librairies testées
from etiquettes.etiquette import decouper

# Constantes internes
from constantes import CHEMIN_ETIQUETTES


def test_visuel_decouper():
    """
    Vous devez afficher les images de chacun des caractères découpés d’une étiquette de votre choix
    dans /donnees/etiquettes.
    """

    # Charger les images de références
    etiquette_test = charger_jpeg(f'{CHEMIN_ETIQUETTES}{1}.jpg')
    try:
        caracteres_obtenus = decouper(etiquette_test)
    except Exception as err:
        raise AssertionError(f'Le chargement des images de caractères retourne le message d\'erreur suivant: {err}')

    # Afficher les images venant du découpage d'une étiquette
    for image in caracteres_obtenus:
        afficher(image)

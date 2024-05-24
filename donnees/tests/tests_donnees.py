# Librairies générales
import pytest

# Librairies testées
from donnees.donnees import charger_references
from donnees.donnees import charger_etiquettes
from donnees.donnees import charger_centroides_references
from images.image import afficher


def test_visuel_charger_references():
    """
    Test pour l'affichage des images de références à partir du chargement de la base de données
    """

    # Charger les images de références
    base_donnees_caracteres_references = charger_references()

    # Afficher les images venant du chargement de la base de données
    for image in base_donnees_caracteres_references.values():
        afficher(image)


def test_visuel_charger_etiquettes():
    """
    Test pour l'affichage des images de chacune des étiquettes à partir du chargement de la base de données.
    """

    # Charger les étiquettes de références
    base_donnees_images_etiquettes = charger_etiquettes()

    # Afficher les étiquettes venant du chargement de la base de données
    for etiquette in base_donnees_images_etiquettes:
        afficher(etiquette)


def test_centroides_references():
    """
    Test pour le calcul, le stockage et le chargement des centroïdes des références.
    """

    # Charger les centroïdes des références
    try:
        centroides_obtenus = charger_centroides_references()
    except Exception as err:
        raise AssertionError(f'Le chargement des centroïdes retourne le message d\'erreur suivant: {err}')

    # Valider la structure de la base de données
    assert isinstance(centroides_obtenus, dict), \
        "Les centroïdes doivent être stockés dans un dictionnaire tel que décrit dans l'énoncé"

    # Les valeurs attendues
    centroides_attendus = \
        {'A': (19.238975501113547, 19.353808463251617), 'B': (18.47470422037786, 18.622903054917856),
         'C': (17.97689539068847, 18.34854290026701), 'D': (17.765927523322844, 18.605175566077506),
         'E': (18.100510204081626, 18.42425788497216), 'F': (18.14759080437228, 17.790157345228145),
         'G': (18.382754695503664, 18.557674065642157), 'H': (18.51326732673262, 18.50675467546751),
         'I': (18.44021024967147, 18.494778338750947), 'J': (19.286850969915157, 18.460971076780066),
         'K': (18.437494630122796, 18.30414984105158), 'L': (18.12375344790998, 19.366221090600423),
         'M': (18.70890422157542, 18.533272293253916), 'N': (18.327266710787526, 18.342525185675377),
         'O': (18.493576676937618, 18.44105238208103), 'P': (18.529361173491278, 18.000668928281282),
         'Q': (18.754755043227632, 20.206304034582075), 'R': (18.546199768332844, 18.624743829635527),
         'S': (18.636774827925247, 18.516666666666637), 'T': (18.427193726155107, 17.424544298431492),
         'U': (18.550302518643555, 18.156981379860195), 'V': (18.546407663650836, 17.268866418307553),
         'W': (18.512114575729093, 18.223276671185694), 'X': (18.521868113239446, 18.618240379725307),
         'Y': (18.414950333913197, 17.74117515012062), 'Z': (18.62463493364757, 18.731567351539663),
         '0': (18.473640306973618, 17.995273050828583), '1': (17.961065097917782, 19.034213174394285),
         '2': (18.356651246756172, 18.16044228816428), '3': (19.200935645823808, 18.261809675947045),
         '4': (18.90061129848228, 18.68080733558176), '5': (18.60183054660733, 18.052973359922262),
         '6': (18.75613630540608, 18.326005636689708), '7': (19.089706854749814, 16.322974065094403),
         '8': (18.530186030186016, 17.887636012635994), '9': (19.164724164724138, 17.75291375291372)}

    # Valider les clés (c'est-à-dire les caractères des lettres et chiffres)
    assert set(centroides_obtenus.keys()) == set(centroides_attendus.keys()), \
        'Les clés de votre base de données de centroïdes ne correspond pas à celles attendues'

    # Valider que les centroïdes concordent
    for caractere in centroides_attendus:

        # Extraire les valeurs attendues en x et en y
        cx_obtenu, cy_obtenu = centroides_obtenus[caractere]
        cx_attendu, cy_attendu = centroides_attendus[caractere]

        # Valider
        assert cx_obtenu == pytest.approx(cx_attendu) and cy_obtenu == pytest.approx(cy_attendu)

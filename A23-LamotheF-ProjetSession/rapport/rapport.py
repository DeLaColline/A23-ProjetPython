# Librairies générales
from datetime import datetime
import numpy as np

# Librairies internes
from algorithme.algorithme import lire_etiquettes_distances
from algorithme.algorithme import lire_etiquette_centroides
from donnees.donnees import charger_etiquettes


def trouver_date() -> datetime:

    # Trouver la date et l'heure exacte
    date = datetime.now()

    return date


def charger_usines() -> list[dict[str, int | str]]:

    # Initialiser un dictionnaire contenant les lieux de fabrication des pièces
    informations_usines = [{"01": "Laval", "ASSY": 0, "PART": 0, "TOTAL": 0},
                           {"02": "Longueuil", "ASSY": 0, "PART": 0, "TOTAL": 0},
                           {"03": "St-Hubert", "ASSY": 0, "PART": 0, "TOTAL": 0},
                           {"04": "Kitchener", "ASSY": 0, "PART": 0, "TOTAL": 0},
                           {"05": "Cambridge", "ASSY": 0, "PART": 0, "TOTAL": 0},
                           {"06": "Springfield", "ASSY": 0, "PART": 0, "TOTAL": 0},
                           {"07": "Wichita", "ASSY": 0, "PART": 0, "TOTAL": 0},
                           {"08": "Cleveland", "ASSY": 0, "PART": 0, "TOTAL": 0},
                           {"09": "Nottingham", "ASSY": 0, "PART": 0, "TOTAL": 0},
                           {"10": "Madrid", "ASSY": 0, "PART": 0, "TOTAL": 0},]

    return informations_usines


def charger_images_etiquettes() -> list[np.ndarray]:

    # Charger les images des étiquettes
    base_donnees_images_etiquettes = charger_etiquettes()

    return base_donnees_images_etiquettes


def analyser_etiquettes_avec_distances() -> list[str]:

    # Charger les images des étiquettes
    base_donnees_images_etiquettes = charger_images_etiquettes()

    # Initialiser une liste qui va contenir les valeurs d'étiquettes analysées avec la méthode distance
    valeurs_etiquettes_distances = []

    # Analyser chacune des étiquettes avec la méthode distance
    for image_etiquette in base_donnees_images_etiquettes:
        valeur_etiquette = lire_etiquettes_distances(image_etiquette)

        # Stocker les valeurs dans la liste
        valeurs_etiquettes_distances.append(valeur_etiquette)

    return valeurs_etiquettes_distances


def analyser_etiquettes_avec_centroides() -> list[str]:

    # Charger les images des étiquettes
    base_donnees_images_etiquettes = charger_images_etiquettes()

    # Initialiser une liste qui va contenir les valeurs d'étiquettes analysées avec la méthode centroïde
    valeurs_etiquettes_centroides = []

    # Analyser chacune des étiquettes avec la méthode centroïde
    for image_etiquette in base_donnees_images_etiquettes:
        valeur_etiquette = lire_etiquette_centroides(image_etiquette)

        # Stocker les valeurs dans la liste
        valeurs_etiquettes_centroides.append(valeur_etiquette)

    return valeurs_etiquettes_centroides


def comparer_valeurs_etiquettes() -> list[str]:

    # Charger les valeurs d'étiquettes obtenues
    valeurs_etiquettes_distances = analyser_etiquettes_avec_distances()
    valeurs_etiquettes_centroides = analyser_etiquettes_avec_centroides()

    # Initialiser une liste qui va contenir les valeurs d'étiquettes comparées
    valeurs_etiquettes_valides = []

    # Initialiser le nombre d'étiquettes à analyser
    nb_etiquettes = 40

    # Valider que les résultats obtenus avec les deux méthodes d'analyse concordent
    for i in range(0, nb_etiquettes):
        if valeurs_etiquettes_distances[i] == valeurs_etiquettes_centroides[i]:
            valeur_etiquette = valeurs_etiquettes_distances[i]

            # Stocker les valeurs validées dans une liste
            valeurs_etiquettes_valides.append(valeur_etiquette)
        else:
            raise ValueError("Les valeurs d'étiquettes retournées par les deux méthodes d'analyse ne concordent pas")

    return valeurs_etiquettes_valides


def analyser_valeurs_etiquettes() -> list[dict[str, int | str]]:

    # Charger un dictionnaire vide qui va contenir les lieux de fabrication des pièces et les quantités de chaque pièce
    informations_usines = charger_usines()

    # Charger la liste des valeurs d'étiquettes validées
    valeurs_etiquettes_valides = comparer_valeurs_etiquettes()

    # Modifier les informations pour chacun des lieux de fabrication
    for usine in informations_usines:

        # Analyser les valeurs de chacune des étiquettes
        for valeur_etiquette in valeurs_etiquettes_valides:

            # Verifier l'étiquette provient de quel lieu de fabrication
            if valeur_etiquette[-2:] in usine:

                # Vérifier si l'étiquette correspond à un assemblage
                if valeur_etiquette[0:4] == 'ASSY':
                    usine['ASSY'] += 1
                    usine['TOTAL'] += 1

                # Vérifier si l'étiquette correspond à un composant
                if valeur_etiquette[0:4] == 'PART':
                    usine['PART'] += 1
                    usine['TOTAL'] += 1

    return informations_usines


def generer():

    # Charger un dictionnaire contenant les lieux de fabrication des pièces et les quantités de chaque pièce
    informations_usines = analyser_valeurs_etiquettes()

    # Initialiser une liste contenant le nom de chacun des lieux de fabrications
    lieux_usines = [next(iter(usine.keys())) for usine in informations_usines]

    # Initialiser l'entête qui va contenir la date
    entete = "Date:   {}\n".format(trouver_date()) + '\n'

    # Initialiser chacune des colonnes de l'affichage avec le formatage désiré
    colonnes = "{:<12} {:<5} {:<5} {:<5}".format('Usine', 'ASSY', 'PART', 'TOTAL') + "\n"

    # Initialiser une chaîne de caractère qui va contenir le rapport complet
    rapport = ''

    # Afficher le nom et les informations de chacun des lieux de fabrication
    for usine, lieu_usine in zip(informations_usines, lieux_usines):

        # Utiliser le même formatage que les colonnes
        rapport += "{:<12} {:<5} {:<5} {:<5}".format(
            str(usine.get(lieu_usine, '')),
            str(usine.get('ASSY', '')),
            str(usine.get('PART', '')),
            str(usine.get('TOTAL', ''))
            ) + "\n"

    print(f"{entete}{colonnes}{rapport}")

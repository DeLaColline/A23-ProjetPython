# Librairies générales
import os

# Chemins d'accès du projet
CHEMIN_RACINE = os.path.abspath(os.path.dirname(__file__))
CHEMIN_ETIQUETTES = CHEMIN_RACINE + '\\donnees\\etiquettes\\'
CHEMIN_REFERENCES = CHEMIN_RACINE + '\\donnees\\references\\'
CHEMIN_FICHIER_CENTROIDES = \
    CHEMIN_RACINE + '\\donnees\\references\\centroides\\centroides.pkl'  # Chemin vers les centroïdes de référence

# Valeurs limites d'un composant RGB
RGB_MIN = 0
RGB_MAX = 255

# Nombre de caractères par étiquette
ETIQUETTE_NB_CARACTERES = 13

# Longueur et largeur d'un caractère en pixels
CARACTERE_NB_PIXELS_COTE = 40

# Dimensions attendues de l'image d'un caractère
DIMENSIONS_ATTENDUES_IMAGE = (CARACTERE_NB_PIXELS_COTE, CARACTERE_NB_PIXELS_COTE)

# Caractères de référence
REFERENCE_LETTRES = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'                        # Caractères alphabétiques de référence
REFERENCE_CHIFFRES = '0123456789'                                       # Caractères numériques de référence
REFERENCE_LETTRES_CHIFFRES = REFERENCE_LETTRES + REFERENCE_CHIFFRES     # Tous les caractères de référence
REFERENCE_NB_CARACTERES = len(REFERENCE_LETTRES_CHIFFRES)               # Nombre de caractères de référence

# Le nombre de caractères de référence
NB_CARACTERES_REFERENCE = 36

# Valeur d'un pixel allumé
PIXEL_ALLUME = 1

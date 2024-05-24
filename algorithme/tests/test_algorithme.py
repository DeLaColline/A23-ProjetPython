# Librairies internes
from donnees.donnees import charger_references
from donnees.donnees import charger_etiquettes
from donnees.donnees import charger_centroides_references
from images.image import afficher

# Librairies testées
from algorithme.algorithme import identifier_caracteres_avec_distances
from algorithme.algorithme import lire_etiquettes_distances
from algorithme.algorithme import identifier_caractere_avec_centroides
from algorithme.algorithme import lire_etiquette_centroides


def test_identifier_caractere_distances():
    """
    Description : Identifie chacun des caractères de la base de données. Autrement dit, lorsque le caractère
    ‘A’ est pigé de la base de données, la fonction identifier_caractere_distances l’identifie correctement
    et ainsi de suite pour les autres caractères.

    Requis : Il doit y avoir autant d’assertions (c.-à-d. de tests) qu’il y a de caractères de référence
    """

    # Charger les images de références
    base_donnees_caracteres_references = charger_references()

    # Effectuer une assertion pour chacun des caractères de références
    test_0 = identifier_caracteres_avec_distances(base_donnees_caracteres_references['0'],
                                                  base_donnees_caracteres_references)
    assert test_0 == 0, f"Le caractère devrait être 0, mais le test a renvoyé {test_0}"

    test_1 = identifier_caracteres_avec_distances(base_donnees_caracteres_references['1'],
                                                  base_donnees_caracteres_references)
    assert test_1 == 1, f"Le caractère devrait être 1, mais le test a renvoyé {test_1}"

    test_2 = identifier_caracteres_avec_distances(base_donnees_caracteres_references['2'],
                                                  base_donnees_caracteres_references)
    assert test_2 == 2, f"Le caractère devrait être 2, mais le test a renvoyé {test_2}"

    test_3 = identifier_caracteres_avec_distances(base_donnees_caracteres_references['3'],
                                                  base_donnees_caracteres_references)
    assert test_3 == 3, f"Le caractère devrait être 3, mais le test a renvoyé {test_3}"

    test_4 = identifier_caracteres_avec_distances(base_donnees_caracteres_references['4'],
                                                  base_donnees_caracteres_references)
    assert test_4 == 4, f"Le caractère devrait être 4, mais le test a renvoyé {test_4}"

    test_5 = identifier_caracteres_avec_distances(base_donnees_caracteres_references['5'],
                                                  base_donnees_caracteres_references)
    assert test_5 == 5, f"Le caractère devrait être 5, mais le test a renvoyé {test_5}"

    test_6 = identifier_caracteres_avec_distances(base_donnees_caracteres_references['6'],
                                                  base_donnees_caracteres_references)
    assert test_6 == 6, f"Le caractère devrait être 6, mais le test a renvoyé {test_6}"

    test_7 = identifier_caracteres_avec_distances(base_donnees_caracteres_references['7'],
                                                  base_donnees_caracteres_references)
    assert test_7 == 7, f"Le caractère devrait être 7, mais le test a renvoyé {test_7}"

    test_8 = identifier_caracteres_avec_distances(base_donnees_caracteres_references['8'],
                                                  base_donnees_caracteres_references)
    assert test_8 == 8, f"Le caractère devrait être 8, mais le test a renvoyé {test_8}"

    test_9 = identifier_caracteres_avec_distances(base_donnees_caracteres_references['9'],
                                                  base_donnees_caracteres_references)
    assert test_9 == 9, f"Le caractère devrait être 9, mais le test a renvoyé {test_9}"

    test_a = identifier_caracteres_avec_distances(base_donnees_caracteres_references['A'],
                                                  base_donnees_caracteres_references)
    assert test_a == 'A', f"Le caractère devrait être A, mais le test a renvoyé {test_a}"

    test_b = identifier_caracteres_avec_distances(base_donnees_caracteres_references['B'],
                                                  base_donnees_caracteres_references)
    assert test_b == 'B', f"Le caractère devrait être B, mais le test a renvoyé {test_b}"

    test_c = identifier_caracteres_avec_distances(base_donnees_caracteres_references['C'],
                                                  base_donnees_caracteres_references)
    assert test_c == 'C', f"Le caractère devrait être C, mais le test a renvoyé {test_c}"

    test_d = identifier_caracteres_avec_distances(base_donnees_caracteres_references['D'],
                                                  base_donnees_caracteres_references)
    assert test_d == 'D', f"Le caractère devrait être D, mais le test a renvoyé {test_d}"

    test_e = identifier_caracteres_avec_distances(base_donnees_caracteres_references['E'],
                                                  base_donnees_caracteres_references)
    assert test_e == 'E', f"Le caractère devrait être E, mais le test a renvoyé {test_e}"

    test_f = identifier_caracteres_avec_distances(base_donnees_caracteres_references['F'],
                                                  base_donnees_caracteres_references)
    assert test_f == 'F', f"Le caractère devrait être F, mais le test a renvoyé {test_f}"

    test_g = identifier_caracteres_avec_distances(base_donnees_caracteres_references['G'],
                                                  base_donnees_caracteres_references)
    assert test_g == 'G', f"Le caractère devrait être G, mais le test a renvoyé {test_g}"

    test_h = identifier_caracteres_avec_distances(base_donnees_caracteres_references['H'],
                                                  base_donnees_caracteres_references)
    assert test_h == 'H', f"Le caractère devrait être H, mais le test a renvoyé {test_h}"

    test_i = identifier_caracteres_avec_distances(base_donnees_caracteres_references['I'],
                                                  base_donnees_caracteres_references)
    assert test_i == 'I', f"Le caractère devrait être I, mais le test a renvoyé {test_i}"

    test_j = identifier_caracteres_avec_distances(base_donnees_caracteres_references['J'],
                                                  base_donnees_caracteres_references)
    assert test_j == 'J', f"Le caractère devrait être J, mais le test a renvoyé {test_j}"

    test_k = identifier_caracteres_avec_distances(base_donnees_caracteres_references['K'],
                                                  base_donnees_caracteres_references)
    assert test_k == 'K', f"Le caractère devrait être K, mais le test a renvoyé {test_k}"

    test_l = identifier_caracteres_avec_distances(base_donnees_caracteres_references['L'],
                                                  base_donnees_caracteres_references)
    assert test_l == 'L', f"Le caractère devrait être L, mais le test a renvoyé {test_l}"

    test_m = identifier_caracteres_avec_distances(base_donnees_caracteres_references['M'],
                                                  base_donnees_caracteres_references)
    assert test_m == 'M', f"Le caractère devrait être M, mais le test a renvoyé {test_m}"

    test_n = identifier_caracteres_avec_distances(base_donnees_caracteres_references['N'],
                                                  base_donnees_caracteres_references)
    assert test_n == 'N', f"Le caractère devrait être N, mais le test a renvoyé {test_n}"

    test_o = identifier_caracteres_avec_distances(base_donnees_caracteres_references['O'],
                                                  base_donnees_caracteres_references)
    assert test_o == 'O', f"Le caractère devrait être O, mais le test a renvoyé {test_o}"

    test_p = identifier_caracteres_avec_distances(base_donnees_caracteres_references['P'],
                                                  base_donnees_caracteres_references)
    assert test_p == 'P', f"Le caractère devrait être P, mais le test a renvoyé {test_p}"

    test_q = identifier_caracteres_avec_distances(base_donnees_caracteres_references['Q'],
                                                  base_donnees_caracteres_references)
    assert test_q == 'Q', f"Le caractère devrait être Q, mais le test a renvoyé {test_q}"

    test_r = identifier_caracteres_avec_distances(base_donnees_caracteres_references['R'],
                                                  base_donnees_caracteres_references)
    assert test_r == 'R', f"Le caractère devrait être R, mais le test a renvoyé {test_r}"

    test_s = identifier_caracteres_avec_distances(base_donnees_caracteres_references['S'],
                                                  base_donnees_caracteres_references)
    assert test_s == 'S', f"Le caractère devrait être S, mais le test a renvoyé {test_s}"

    test_t = identifier_caracteres_avec_distances(base_donnees_caracteres_references['T'],
                                                  base_donnees_caracteres_references)
    assert test_t == 'T', f"Le caractère devrait être T, mais le test a renvoyé {test_t}"

    test_u = identifier_caracteres_avec_distances(base_donnees_caracteres_references['U'],
                                                  base_donnees_caracteres_references)
    assert test_u == 'U', f"Le caractère devrait être U, mais le test a renvoyé {test_u}"

    test_v = identifier_caracteres_avec_distances(base_donnees_caracteres_references['V'],
                                                  base_donnees_caracteres_references)
    assert test_v == 'V', f"Le caractère devrait être V, mais le test a renvoyé {test_v}"

    test_w = identifier_caracteres_avec_distances(base_donnees_caracteres_references['W'],
                                                  base_donnees_caracteres_references)
    assert test_w == 'W', f"Le caractère devrait être W, mais le test a renvoyé {test_w}"

    test_x = identifier_caracteres_avec_distances(base_donnees_caracteres_references['X'],
                                                  base_donnees_caracteres_references)
    assert test_x == 'X', f"Le caractère devrait être X, mais le test a renvoyé {test_x}"

    test_y = identifier_caracteres_avec_distances(base_donnees_caracteres_references['Y'],
                                                  base_donnees_caracteres_references)
    assert test_y == 'Y', f"Le caractère devrait être Y, mais le test a renvoyé {test_y}"

    test_z = identifier_caracteres_avec_distances(base_donnees_caracteres_references['Z'],
                                                  base_donnees_caracteres_references)
    assert test_z == 'Z', f"Le caractère devrait être Z, mais le test a renvoyé {test_z}"


def test_lire_etiquettes_distances():
    """
    Test unitaire qui valide que la valeur de distance obtenue en lisant
    les images découpées d'une étiquette est la bonne.
    """

    # Charger les images des étiquettes
    base_donnees_images_etiquettes = charger_etiquettes()

    # Sélectionner notre étiquette de test
    etiquette_test = base_donnees_images_etiquettes[5]

    # Effectuer l'assertion que les valeurs obtenue et attendue de l'étiquette test concordent
    assert lire_etiquettes_distances(etiquette_test) == 'ASSYB19010101'


def test_integration_1():
    """
    Test d’intégration qui charge la base de données d’étiquettes, les analyse avec la distance et
    affiche chaque étiquette une par une en fournissant la valeur lue comme titre.
    """

    # Charger les images des étiquettes
    base_donnees_images_etiquettes = charger_etiquettes()

    # Afficher la valeur de chacune des étiquettes analysées
    for etiquette in base_donnees_images_etiquettes:
        valeur_etiquette = lire_etiquettes_distances(etiquette)
        afficher(etiquette, valeur_etiquette)


def test_identifier_caractere_centroides():
    """
    Description : Identifie chacun des caractères de la base de données. Autrement dit, lorsque le caractère
    ‘A’ est pigé de la base de données, la fonction identifier_caractere_avec_centroides l’identifie correctement
    et ainsi de suite pour les autres caractères.

    Requis : Il doit y avoir autant d’assertions (c.-à-d. de tests) qu’il y a de caractères de référence.
    """

    # Charger les images de références
    base_donnees_caracteres_references = charger_references()

    # Charger les centroïdes de références
    base_donnees_centroides_references = charger_centroides_references()

    # Effectuer une assertion pour chacun des caractères de références
    test_0 = identifier_caractere_avec_centroides(base_donnees_caracteres_references['0'],
                                                  base_donnees_centroides_references)
    assert test_0 == 0, f"Le caractère devrait être 0, mais le test a renvoyé {test_0}"

    test_1 = identifier_caractere_avec_centroides(base_donnees_caracteres_references['1'],
                                                  base_donnees_centroides_references)
    assert test_1 == 1, f"Le caractère devrait être 1, mais le test a renvoyé {test_1}"

    test_2 = identifier_caractere_avec_centroides(base_donnees_caracteres_references['2'],
                                                  base_donnees_centroides_references)
    assert test_2 == 2, f"Le caractère devrait être 2, mais le test a renvoyé {test_2}"

    test_3 = identifier_caractere_avec_centroides(base_donnees_caracteres_references['3'],
                                                  base_donnees_centroides_references)
    assert test_3 == 3, f"Le caractère devrait être 3, mais le test a renvoyé {test_3}"

    test_4 = identifier_caractere_avec_centroides(base_donnees_caracteres_references['4'],
                                                  base_donnees_centroides_references)
    assert test_4 == 4, f"Le caractère devrait être 4, mais le test a renvoyé {test_4}"

    test_5 = identifier_caractere_avec_centroides(base_donnees_caracteres_references['5'],
                                                  base_donnees_centroides_references)
    assert test_5 == 5, f"Le caractère devrait être 5, mais le test a renvoyé {test_5}"

    test_6 = identifier_caractere_avec_centroides(base_donnees_caracteres_references['6'],
                                                  base_donnees_centroides_references)
    assert test_6 == 6, f"Le caractère devrait être 6, mais le test a renvoyé {test_6}"

    test_7 = identifier_caractere_avec_centroides(base_donnees_caracteres_references['7'],
                                                  base_donnees_centroides_references)
    assert test_7 == 7, f"Le caractère devrait être 7, mais le test a renvoyé {test_7}"

    test_8 = identifier_caractere_avec_centroides(base_donnees_caracteres_references['8'],
                                                  base_donnees_centroides_references)
    assert test_8 == 8, f"Le caractère devrait être 8, mais le test a renvoyé {test_8}"

    test_9 = identifier_caractere_avec_centroides(base_donnees_caracteres_references['9'],
                                                  base_donnees_centroides_references)
    assert test_9 == 9, f"Le caractère devrait être 9, mais le test a renvoyé {test_9}"

    test_a = identifier_caractere_avec_centroides(base_donnees_caracteres_references['A'],
                                                  base_donnees_centroides_references)
    assert test_a == 'A', f"Le caractère devrait être A, mais le test a renvoyé {test_a}"

    test_b = identifier_caractere_avec_centroides(base_donnees_caracteres_references['B'],
                                                  base_donnees_centroides_references)
    assert test_b == 'B', f"Le caractère devrait être B, mais le test a renvoyé {test_b}"

    test_c = identifier_caractere_avec_centroides(base_donnees_caracteres_references['C'],
                                                  base_donnees_centroides_references)
    assert test_c == 'C', f"Le caractère devrait être C, mais le test a renvoyé {test_c}"

    test_d = identifier_caractere_avec_centroides(base_donnees_caracteres_references['D'],
                                                  base_donnees_centroides_references)
    assert test_d == 'D', f"Le caractère devrait être D, mais le test a renvoyé {test_d}"

    test_e = identifier_caractere_avec_centroides(base_donnees_caracteres_references['E'],
                                                  base_donnees_centroides_references)
    assert test_e == 'E', f"Le caractère devrait être E, mais le test a renvoyé {test_e}"

    test_f = identifier_caractere_avec_centroides(base_donnees_caracteres_references['F'],
                                                  base_donnees_centroides_references)
    assert test_f == 'F', f"Le caractère devrait être F, mais le test a renvoyé {test_f}"

    test_g = identifier_caractere_avec_centroides(base_donnees_caracteres_references['G'],
                                                  base_donnees_centroides_references)
    assert test_g == 'G', f"Le caractère devrait être G, mais le test a renvoyé {test_g}"

    test_h = identifier_caractere_avec_centroides(base_donnees_caracteres_references['H'],
                                                  base_donnees_centroides_references)
    assert test_h == 'H', f"Le caractère devrait être H, mais le test a renvoyé {test_h}"

    test_i = identifier_caractere_avec_centroides(base_donnees_caracteres_references['I'],
                                                  base_donnees_centroides_references)
    assert test_i == 'I', f"Le caractère devrait être I, mais le test a renvoyé {test_i}"

    test_j = identifier_caractere_avec_centroides(base_donnees_caracteres_references['J'],
                                                  base_donnees_centroides_references)
    assert test_j == 'J', f"Le caractère devrait être J, mais le test a renvoyé {test_j}"

    test_k = identifier_caractere_avec_centroides(base_donnees_caracteres_references['K'],
                                                  base_donnees_centroides_references)
    assert test_k == 'K', f"Le caractère devrait être K, mais le test a renvoyé {test_k}"

    test_l = identifier_caractere_avec_centroides(base_donnees_caracteres_references['L'],
                                                  base_donnees_centroides_references)
    assert test_l == 'L', f"Le caractère devrait être L, mais le test a renvoyé {test_l}"

    test_m = identifier_caractere_avec_centroides(base_donnees_caracteres_references['M'],
                                                  base_donnees_centroides_references)
    assert test_m == 'M', f"Le caractère devrait être M, mais le test a renvoyé {test_m}"

    test_n = identifier_caractere_avec_centroides(base_donnees_caracteres_references['N'],
                                                  base_donnees_centroides_references)
    assert test_n == 'N', f"Le caractère devrait être N, mais le test a renvoyé {test_n}"

    test_o = identifier_caractere_avec_centroides(base_donnees_caracteres_references['O'],
                                                  base_donnees_centroides_references)
    assert test_o == 'O', f"Le caractère devrait être O, mais le test a renvoyé {test_o}"

    test_p = identifier_caractere_avec_centroides(base_donnees_caracteres_references['P'],
                                                  base_donnees_centroides_references)
    assert test_p == 'P', f"Le caractère devrait être P, mais le test a renvoyé {test_p}"

    test_q = identifier_caractere_avec_centroides(base_donnees_caracteres_references['Q'],
                                                  base_donnees_centroides_references)
    assert test_q == 'Q', f"Le caractère devrait être Q, mais le test a renvoyé {test_q}"

    test_r = identifier_caractere_avec_centroides(base_donnees_caracteres_references['R'],
                                                  base_donnees_centroides_references)
    assert test_r == 'R', f"Le caractère devrait être R, mais le test a renvoyé {test_r}"

    test_s = identifier_caractere_avec_centroides(base_donnees_caracteres_references['S'],
                                                  base_donnees_centroides_references)
    assert test_s == 'S', f"Le caractère devrait être S, mais le test a renvoyé {test_s}"

    test_t = identifier_caractere_avec_centroides(base_donnees_caracteres_references['T'],
                                                  base_donnees_centroides_references)
    assert test_t == 'T', f"Le caractère devrait être T, mais le test a renvoyé {test_t}"

    test_u = identifier_caractere_avec_centroides(base_donnees_caracteres_references['U'],
                                                  base_donnees_centroides_references)
    assert test_u == 'U', f"Le caractère devrait être U, mais le test a renvoyé {test_u}"

    test_v = identifier_caractere_avec_centroides(base_donnees_caracteres_references['V'],
                                                  base_donnees_centroides_references)
    assert test_v == 'V', f"Le caractère devrait être V, mais le test a renvoyé {test_v}"

    test_w = identifier_caractere_avec_centroides(base_donnees_caracteres_references['W'],
                                                  base_donnees_centroides_references)
    assert test_w == 'W', f"Le caractère devrait être W, mais le test a renvoyé {test_w}"

    test_x = identifier_caractere_avec_centroides(base_donnees_caracteres_references['X'],
                                                  base_donnees_centroides_references)
    assert test_x == 'X', f"Le caractère devrait être X, mais le test a renvoyé {test_x}"

    test_y = identifier_caractere_avec_centroides(base_donnees_caracteres_references['Y'],
                                                  base_donnees_centroides_references)
    assert test_y == 'Y', f"Le caractère devrait être Y, mais le test a renvoyé {test_y}"

    test_z = identifier_caractere_avec_centroides(base_donnees_caracteres_references['Z'],
                                                  base_donnees_centroides_references)
    assert test_z == 'Z', f"Le caractère devrait être Z, mais le test a renvoyé {test_z}"


def test_lire_etiquette_centroides():
    """
    Test unitaire qui valide que la valeur de centroide obtenue en lisant une étiquette est la bonne
    """

    # Charger les images des étiquettes
    base_donnees_images_etiquettes = charger_etiquettes()

    # Sélectionner notre étiquette de test
    etiquette_test = base_donnees_images_etiquettes[13]

    # Effectuer l'assertion que les valeurs obtenue et attendue de l'étiquette test concordent
    assert lire_etiquette_centroides(etiquette_test) == 'ASSYC22040404'


def test_integration_2():
    """
    Test d’intégration qui charge la base de données d’étiquettes, les analyse avec le centroïde et
    affiche chaque étiquette une par une en fournissant la valeur lue comme titre.
    """

    # Charger les images des étiquettes
    base_donnees_images_etiquettes = charger_etiquettes()

    # Afficher la valeur de chacune des étiquettes analysées
    for etiquette in base_donnees_images_etiquettes:
        valeur_etiquette = lire_etiquette_centroides(etiquette)
        afficher(etiquette, valeur_etiquette)

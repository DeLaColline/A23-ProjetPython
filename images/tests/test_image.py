# Librairies générales
import numpy as np
from pytest import approx

# Librairies internes
from donnees.donnees import charger_references

# Librairies testées
from images.image import calculer_differences
from images.image import calculer_moments_premier_ordre
from images.image import calculer_centroide
from images.image import calculer_moments_deuxieme_ordre
from images.image import calculer_matrice_covariance
from images.image import calculer_vecteurs_propres
from images.image import estimer_angle_rotation


def test_calculer_difference_nulle():
    """
    Test pour vérifier que la distance entre une image et elle-même donne bel et bien zéro.
    """

    # Charger les images de références
    base_donnees_caracteres_references = charger_references()

    # Sélectionner l'image test
    image1 = base_donnees_caracteres_references['0']

    # Calculer la distance entre l'image test et elle-même
    distance = calculer_differences(image1, image1)

    # Valider que la distance obtenue est bien 0
    assert np.all(distance == 0)


def test_calculer_difference_non_nulle():
    """
    Test pour vérifier un cas d’usage dont la différence résultante est non-nulle.
    """

    # Charger les images de références
    base_donnees_caracteres_references = charger_references()

    # Sélectionner les images test
    image1 = base_donnees_caracteres_references['0']
    image2 = base_donnees_caracteres_references['3']

    # Calculer la distance entre les deux images test
    distance = calculer_differences(image1, image2)

    # Valider que la distance obtenue n'est pas 0
    assert np.all(distance != 0)


def test_calculer_difference_absolue():
    """
    Test pour vérifier que la distance calculée correspond à la valeur absolue des différences entre les pixels.
    """

    # Charger les images de références
    base_donnees_caracteres_references = charger_references()

    # Sélectionner les images test
    image1 = base_donnees_caracteres_references['0']
    image3 = base_donnees_caracteres_references['G']

    # Calculer la distance entre les deux images test
    distance = calculer_differences(image1, image3)

    # Valider que la distance obtenue est plus grande que 0
    assert np.all(distance > 0)


def test_calculer_moments_premier_ordre():
    """
    Test pour vérifier le sous-programme calculer_moments_premier_ordre
    """

    image_test = np.array([[1, 2], [3, 4]])

    # Assertion pour le moment du premier ordre en x
    assert calculer_moments_premier_ordre(image_test)[0] == 6

    # Assertion pour le moment du premier ordre en y
    assert calculer_moments_premier_ordre(image_test)[1] == 7

    # Assertion pour la masse de l'image
    assert calculer_moments_premier_ordre(image_test)[2] == 10


def test_calculer_centroide_image_vide():
    """
    Test pour vérifier un cas d’usage où l'image est vide.
    """

    # Sélectionner l'image test
    image_test = np.array([[0, 0], [0, 0]])

    # Calculer le centroïde de l'image test
    coordonnees_centroides = calculer_centroide(image_test)

    # Valider que les coordonées sont bonnes
    assert coordonnees_centroides == (0.0, 0.0)


def test_calculer_centroide_entiers():
    """
    Test pour vérifier un cas d’usage d'une image avec des entiers.
    """

    # Sélectionner l'image test
    image_test = np.array([[1, 2], [3, 4]])

    # Calculer le centroïde de l'image test
    coordonnees_centroides = calculer_centroide(image_test)

    # Valider que les coordonées sont bonnes
    assert coordonnees_centroides == (0.6, 0.7)


def test_calculer_centroide_rationnels():
    """
    Test pour vérifier un cas d’usage d'une image avec des rationnels.
    """

    # Sélectionner l'image test
    image_test = np.array([[0.5, 0], [0, 0.5]])

    # Calculer le centroïde de l'image test
    coordonnees_centroides = calculer_centroide(image_test)

    # Valider que les coordonées sont bonnes
    assert coordonnees_centroides == (0.5, 0.5)


def test_calculer_moments_deuxieme_ordre():
    """
    Test pour vérifier le sous-programme calculer_moments_deuxième_ordre
    """

    # Degré de tolérance 𝜺 = 𝟏/𝟏𝟎𝟎𝟎
    precision = 0.001

    image_test = np.array([[1.25, 20.5], [30.1, 40.5]])

    # Assertion pour le second moment 𝜇𝑥𝑦
    assert calculer_moments_deuxieme_ordre(image_test)[0] == approx(-6.13345966432052, precision)

    # Assertion pour le second moment 𝜇𝑥𝑥
    assert calculer_moments_deuxieme_ordre(image_test)[1] == approx(20.707634001082837, precision)

    # Assertion pour le second moment 𝜇𝑦𝑦
    assert calculer_moments_deuxieme_ordre(image_test)[2] == approx(16.627504060638874, precision)


def test_calculer_matrice_covariance():
    """
    Test pour vérifier le sous-programme calculer_matrice_covariance
    """

    # Degré de tolérance 𝜺 = 𝟏/𝟏𝟎𝟎𝟎
    precision = 0.001

    # Sélectionner l'image test
    image_test = np.array([[1.25, 20.5], [30.1, 40.5]])

    # Initialiser les moments de deuxième ordre
    second_moment_xy = -6.13345966432052
    second_moment_xx = 20.707634001082837
    second_moment_yy = 16.627504060368874

    # Calculer la matrice de covariance de l'image test
    x = calculer_matrice_covariance(image_test)

    # Initialiser la matrice test
    y = np.array([[approx(second_moment_xx, precision), approx(second_moment_xy, precision)],
                  [approx(second_moment_xy, precision), approx(second_moment_yy, precision)]])

    # Valider que les deux matrices concordent
    assert (x == y).all()


def test_calculer_vecteurs_propres():
    """
    Test pour vérifier le sous-programme calculer_vecteurs_propres
    """

    # Degré de tolérance 𝜺 = 𝟏/𝟏𝟎𝟎𝟎
    precision = 0.001

    # Sélectionner l'image test
    image_test = np.array([[0, 1, 0], [0, 1, 1], [0, 0, 0]])

    # Initialiser les vecteurs propres
    vecteur_1_x = 1 / 2 ** 0.5
    vecteur_1_y = 1 / 2 ** 0.5
    vecteur_2_x = 1 / 2 ** 0.5
    vecteur_2_y = - 1 / 2 ** 0.5

    # Calculer la liste de vecteurs propres de l'image test
    x = calculer_vecteurs_propres(image_test)

    # Initialiser la liste contenant les vecteurs propres
    y = np.array([[approx(vecteur_1_x, precision), approx(vecteur_1_y, precision), ],
                  [approx(vecteur_2_x, precision), approx(vecteur_2_y, precision), ]])

    # Valider que les deux listes de vecteurs propres concordent
    assert (x == y).all()


def test_estimer_angle_rotation():
    """
    Test pour vérifier le sous-programme estimer_angle_rotation
    """

    # Degré de tolérance 𝜺 = 𝟏/𝟏𝟎𝟎𝟎
    precision = 0.001

    # Sélectionner l'image test
    image_test = np.array([[0, 1, 0], [0, 1, 1], [1, 0, 0]])

    # Valider que les angles de rotation obtenus et attendus concordent
    assert estimer_angle_rotation(image_test) == approx(-45, precision)

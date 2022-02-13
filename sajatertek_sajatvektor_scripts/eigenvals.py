import numpy as np


def von_mises(A, iteracio_szam: int):
    """

    :param A: matrix
    :param iteracio_szam: mennyi szimulaciot szeretnenk futtatni
    :return: dominans sajat vektor kozelitese
    """
    # Feltesszuk, hogy nincs tudasunk, hogy milyen lehet a dominans sajatvektor
    # ezert veletlen vektorral dolgozunk, illetve ezzel kisebb az eselye annak,
    # hogy b es A szorzata 0 lesz, azaz, hogy ortoginalisak egymasra
    b_k = np.random.rand(A.shape[1])

    for iterval in range(iteracio_szam):
        # elvegezzuk a veletlen vektor es a matrix szorzasat
        b_k0 = np.dot(A, b_k)

        # letrehozzuk a normalt vektort
        norm = np.linalg.norm(b_k0)

        # normalizaljuk a vektort a normalt vektorral
        b_k = b_k0 / norm

        #  ezt a harom lepest folytatjuk
    return b_k


matrix = np.array([[1, 0], [0, 1]])
print(von_mises(matrix, 1000))

import numpy as np
from numba import jit
import statistics as st
import time
def von_mises(A, iteracio_szam: int):
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

@jit(nopython=True)
def numba_von_mises(A, iteracio_szam: int):

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


matrix = np.array([[1, 0], [0, 1]], dtype=np.float64)
numba_von_mises(matrix, 10)
numbalst = []
lst = []
for i in range(100):
    start = time.time()
    numba_von_mises(matrix, 10)
    end = time.time()
    numbalst.append(end - start)

    start = time.time()
    von_mises(matrix, 10)
    end = time.time()
    lst.append(end - start)

mean = st.mean(lst)
standraddev = st.stdev(lst)
med = st.median(lst)
print('Ordinary: ')
print('mean:', mean)
print('stdev:', standraddev)
print('med:', med)

print('-' * 20)
print('Numba:')
mean = st.mean(numbalst)
standraddev = st.stdev(numbalst)
med = st.median(numbalst)
print('mean:', mean)
print('stdev:', standraddev)
print('med:', med)
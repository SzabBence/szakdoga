import numpy as np
from numba import jit


def von_mises(A, iteracio_szam: int):

    b_k = np.random.rand(A.shape[1])
    for iterval in range(iteracio_szam):
        b_k0 = np.dot(A, b_k)
        norm = np.linalg.norm(b_k0)
        b_k = b_k0 / norm
    return b_k


@jit(nopython=True)
def numba_von_mises(A, iteracio_szam: int):

    b_k = np.random.rand(A.shape[1])
    for iterval in range(iteracio_szam):
        b_k0 = np.dot(A, b_k)
        norm = np.linalg.norm(b_k0)
        b_k = b_k0 / norm
    return b_k

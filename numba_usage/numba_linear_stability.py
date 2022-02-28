import numpy as np
from numba import jit
import statistics as st
import time


def linear_stabily_check(matrix: np.array):
    eigenvals,eigenvectors = np.linalg.eig(matrix)
    real_part = eigenvals.real
    lista = real_part < 0
    if np.all(lista):
        return "Aszimptotikusan stabil"
    else:
        return "Instabil"

@jit(nopython = True)
def numba_linear_stabily_check(matrix: np.array):
    eigenvals,eigenvectors = np.linalg.eig(matrix)
    real_part = eigenvals.real
    lista = real_part < 0
    if np.all(lista):
        return "Aszimptotikusan stabil"
    else:
        return "Instabil"

matrix = np.random.rand(2,2)
numba_linear_stabily_check(matrix)
original_values = []
numba_vales = []

for i in range(100):
    loop_matirx = np.random.rand(5,5)
    start = time.time()
    numba_linear_stabily_check(loop_matirx)
    end = time.time()
    numba_vales.append(end - start)

    start = time.time()
    linear_stabily_check(loop_matirx)
    end = time.time()
    original_values.append(end - start)

mean_ord = st.mean(original_values)
standraddev_ord = st.stdev(original_values)
# med = st.median(lst)
print('Ordinary: ')
print('mean:', mean_ord)
print('stdev:', standraddev_ord)
# print('med:', med)

print('-' * 20)
print('Numba:')
mean_nb = st.mean(numba_vales)
standraddev_nb = st.stdev(numba_vales)
# med = st.median(numbalst)
print('mean:', mean_nb)
print('stdev:', standraddev_nb)
# print('med:', med)
if mean_nb ==0:
    print('mean_nb = 0')
else:
    print('ratio mean:',mean_ord/ mean_nb)
if standraddev_nb == 0:
    print("stdev_nb = 0")
else:
    print('ratio standdev:',standraddev_ord/standraddev_nb )
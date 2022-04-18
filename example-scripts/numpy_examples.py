# vanilla python
import time
import statistics as st
import numpy as np

szam_lista = range(0, 1000, 1)
szam_lista_np = np.arange(0, 1000, 1)
time_lst = []
time_lst_np = []
if __name__ == "__main__":
    for vanilla_ismetles in range(1000):
        start = time.time()
        x = [i**2 - 1 for i in szam_lista]
        end = time.time()
        time_lst.append(end - start)

    print("Atlagos ido vanilla python mellett: " + str(st.mean(time_lst)))

    for numpy_ismetles in range(1000):
        start = time.time()
        x = np.power(szam_lista_np, 2) - 1
        end = time.time()
        time_lst_np.append(end - start)

    print("Atlagos ido numpy mellett: " + str(st.mean(time_lst_np)))
    print("Aranyuk: " + str(st.mean(time_lst) / st.mean(time_lst_np)))

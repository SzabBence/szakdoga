import numpy as np

def derivate_function():
    """

    :return:
    """
    return None

def lagrange_interpol_polinom(k: int, x_fix: float, x_array: np.array) -> float:
    x = np.delete(x_array,k)
    array_to_prod = (x_fix - x)/(x_array[k] - x)
    return np.prod(array_to_prod)
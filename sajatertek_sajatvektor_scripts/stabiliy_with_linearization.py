import numpy as np


def linear_stabily_check(matrix: np.array):
    eigenvals, eigenvectors = np.linalg.eig(matrix)
    real_part = eigenvals.real
    if all(eigenval_real_part < 0 for eigenval_real_part in real_part):
        return "Aszimptotikusan stabil"
    else:
        return "Instabil"

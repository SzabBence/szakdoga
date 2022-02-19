import numpy as np
matrix = np.array([[3, -2], [4, 1]])
matrix2 = np.array([[1, 0], [0, 1]])

def linear_stabily_check(matrix):
    eigenvals,eigenvectors = np.linalg.eig(matrix)
    real_part = eigenvals.real
    if all(eigenval_real_part < 0 for eigenval_real_part in real_part):
        return "Aszimptotikusan stabil"
    elif any(eigenval_real_part > 0 for eigenval_real_part in real_part):
        return "Instabil"
    else:
        return "Van 0 sajatertek"

print(linear_stabily_check(matrix))
print(linear_stabily_check(matrix2))
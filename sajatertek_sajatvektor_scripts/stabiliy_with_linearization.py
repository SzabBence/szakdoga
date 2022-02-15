import numpy as np
matrix = np.array([[3, -2], [4, 1]])
eigenvals, eigenvectors = np.linalg.eig(matrix)

# print(eigenvals)
# real_part = eigenvals.real
# if not any(x<0 for x in real_part):
#     # nincs negativ elem
#     print("Aszimptotikusan stabil")
# else:
#     print("Instabil")
# print(np.iscomplex(eigenvals))
m2 = np.array([[1, 0], [0, 1]])
def linear_stabily_check(matrix):
    eigenvals,eigenvectors = np.linalg.eig(matrix)
    real_part = eigenvals.real
    if all(eigenval_real_part < 0 for eigenval_real_part in real_part):
        return "Aszimptotikusan stabil"
    else:
        return "Instabil"

print(linear_stabily_check(matrix))
print(linear_stabily_check(m2))
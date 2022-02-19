import numpy as np

matrix = np.array([[3, -2], [4, 1]])
eigenvals, eigenvectors = np.linalg.eig(matrix)
print("Sajatertekek listaban:")
print(eigenvals)
print("Sajatvektorok listaban:")
print(eigenvectors)

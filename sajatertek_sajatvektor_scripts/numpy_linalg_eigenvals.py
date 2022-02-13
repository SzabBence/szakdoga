import numpy as np

matrix = np.array([[10, 20], [30, 40]])

eigenvals, eigenvectors = np.linalg.eig(matrix)
print("Sajatertekek listaban:")
print(eigenvals)
print("Sajatvektorok listaban:")
print(eigenvectors)

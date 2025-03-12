import numpy as np

matrix = np.random.randint(0, 10, size=(3,3))

determinant = np.linalg.det(matrix)

print("Матрица:")
print(matrix)
print("Определитель матрицы:", determinant)
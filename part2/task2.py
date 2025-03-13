import numpy as np


def matrix_determinant() -> None:
    """
    функция создают матрицу 3х3 с рандомными значениями
    и высчитывает определитель матрицы
    :return: None
    """
    matrix = np.random.randint(0, 10, size=(3,3))
    determinant = np.linalg.det(matrix)

    print("Матрица:")
    print(matrix)
    print("Определитель матрицы:", determinant)

if __name__ == "__main__":
    matrix_determinant()
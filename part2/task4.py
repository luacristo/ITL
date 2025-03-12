import matplotlib.pyplot as plt
import numpy as np 

def gystogram() -> None:
    """
    функция построения гистограммы из 1000 случайных чисел
    с распределением по нормальному закону
    :return: None
    """
    data = np.random.randn(1000)

    plt.hist(data, bins=30, color='skyblue', edgecolor='black')
    plt.title("Гистограмма нормального закона (1000 чисел)")
    plt.xlabel("Значение")
    plt.ylabel("Частота")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    gystogram()
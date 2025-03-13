import matplotlib.pyplot as plt
import numpy as np


def plot_graph(x_value: int, y_value: int) -> None:
    """
    функция построения графика функции
    :return: None
    """
    

    plt.plot(x_value, y_value, label="y = x^2", color="black")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    x = np.linspace(-10, 10, 100)
    y = x**2
    
    plot_graph(x, y)
import matplotlib.pyplot as plt
import numpy as np

def plot_graph() -> None:
    """
    функция построения графика функции
    :return: None
    """
    x = np.linspace(-10, 10, 100)
    y = x**2

    plt.plot(x, y, label="y = x^2", color="black")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    plot_graph()
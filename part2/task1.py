import numpy as np

def random_array() -> None:
    """
    функция создает массив с рандомными числами
    и высчитывает среднее значение и стандартное отклонение
    :return: None
    """
    array = np.random.random(10)
    avg_value = np.mean(array)
    std = np.std(array)

    print("Массив:", array)
    print("Среднее значение:", avg_value)
    print("Стандартное отклонение:", std)

if __name__ == "__main__":
    random_array()
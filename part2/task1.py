import numpy as np

array = np.random.randint(0, 100, 10)

avg_value = np.mean(array)
std = np.std(array)

print("Массив:", array)
print("Среднее значение:", avg_value)
print("Стандартное отклонение:", std)


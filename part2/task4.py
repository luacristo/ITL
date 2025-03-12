import matplotlib.pyplot as plt
import numpy as np 

data = np.random.randn(1000)

plt.hist(data, bins=30, color='skyblue', edgecolor='black')

plt.title("Гистограмма нормального закона (1000 чисел)")
plt.xlabel("Значение")
plt.ylabel("Частота")
plt.grid(True)

plt.show
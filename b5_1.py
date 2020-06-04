import matplotlib.pyplot as plt
import numpy as np

x_1 = np.linspace(start=-50, stop=50, num=100)


def f(x):
    return x**3 + 3*x + 1


y_1 = f(x_1)
plt.xlabel('X', fontsize=16)
plt.ylabel('f(x)', fontsize=16)
plt.plot(x_1, y_1)
plt.show()

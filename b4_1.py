import numpy as np
from numpy.linalg import *
a = np.array([1, 4, 3, 7, 2, 5, 3, 3])
b = a.reshape((2, -1))  # 2 hàng
# c=b.ravel()
c = b.flatten()
d = np.random.random((3, 5, 6))
d = np.arange(10, 20, 0.5).reshape(5, -1)

print(d)

import numpy as np
arr = np.array([[4, 4, 3], [5, 3, 7], [4, 9, 2]])
print(arr)
# ma tran chuyen vi
print("Ma tran chuyen vi:")
B = arr.transpose()
print(B)
# ma tran nghich dao
# ma tran tich
print("Ma tran tich:")
C = arr.dot(arr)
print(C)

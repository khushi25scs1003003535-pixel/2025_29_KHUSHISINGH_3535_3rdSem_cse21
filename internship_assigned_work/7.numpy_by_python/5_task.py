# slicing of array
print("1d array")
import numpy as np
array1 = np.array([19,72,36,65,90,27])
print(array1[1:3])
print(array1[1:6:2])
print(array1[-1:-3:-1])
print(array1[::2])

print("2d array")

import numpy as np
array1 = np.array([[14,15,25], [23,67,78],[45,78,45]])
print(array1[1,])
print(array1[:,1])
print(array1[1:3,1:3])
print(array1[1:3,:1])
print(array1[:,1:3])

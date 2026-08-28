# attribute of numpy array
# ndim, shape, size, dtype, itemsize


import numpy as np
list1 = [25, 67, 78, 26, 27]
list2 = [[25,8927,27],[67,89,56],[67,26,92]]
array1 = np.array(list1)
array2 = np.array(list2)
print(array1.ndim)
print(array2.ndim)
print(array1.shape)
print(array2.shape)
print(array1.size)
print(array1.size)
print(array1.dtype)
print(array2.dtype)
print(array1.itemsize)
print(array2.itemsize)
print("indexixing of arry")
print(array1[0])
print(array1[-1])
print(array2[1,2])
print(array2[0,:])






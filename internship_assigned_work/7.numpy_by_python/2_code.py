import numpy as np
arr1 = np.array([10, 30, 40, 20, 50])
arr2 = np.array(['red', 'white', 'blue'])
print(arr1.dtype)
print(arr2.dtype)





import numpy as np
arr1 = np.array([5.6, 4.7, 3.9])
arr2 = np.array([1, 5, 0])
new1 = arr1.astype('i')
new2 = arr1.astype(int)
new3 = arr2.astype(bool)
print(new1)
print(new1.dtype)
print(new2)
print(new2.dtype)
print(new3)
print(new3.dtype)






import numpy as np

arr1 =np.array([3,5,6,9])
arr2 = np.array([[15, 25, 55], [30, 55, 40]])
print(arr1.shape)
print(arr2.shape)




import numpy as np
arr1 = np.array([1, 2, 3])
# 1D array
for x in arr1:
    print(x)
# 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr2:
    print(x)
for x in arr2:
    for y in x:
         print(y)






import numpy as np
arr1 = np.array([7, 21, 17])
arr2 = np.array([3, 15, 16])
arr = np.concatenate((arr1, arr2))
print(arr)



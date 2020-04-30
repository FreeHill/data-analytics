import numpy as np

array = np.arange(0, 12)
print(array)
print(array[0])
print(array[0:5])
print(array[2:6])
array[0:5] = 20
print(array)
array[:] = 29
print(array)

array_copy = array.copy()
print(array_copy)
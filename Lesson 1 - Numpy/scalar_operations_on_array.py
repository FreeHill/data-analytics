# from __future__ import division  ''' for python 2.7'''
import numpy as np

array_1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(array_1)

# scalar multiplication
print(array_1 * array_1)

# Exponential multiplication
array_2 = array_1 ** 3
print(array_2)

# Subtraction
array_4 = array_1 - array_1
print(array_4)

# Reciprocal
print(1/array_1)
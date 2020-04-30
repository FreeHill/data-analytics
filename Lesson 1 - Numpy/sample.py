import numpy as np

my_list = [1, 2, 3, 4]
my_list_2 = [5, 6, 7, 8]

# adding two arrays into a multidimensional array
my_array = np.array([my_list, my_list_2])
print(my_array)

# find shape of array '2x2'
print(my_array.shape)

# finding datatype of array
print(my_array.dtype)

# zeros, ones, empty, eye, arrange

new_array_1 = np.zeros(5)  # creates a numpy array with (1 x 5) with all elements being zeros
print(new_array_1)

new_array_2 = np.ones([5, 5])  # creates a numpy array with (5 x 5) with all elements being zeros
print(new_array_2)

new_array_1 = np.empty(5)
print(new_array_1)

new_array_2 = np.eye(5)  # creates a 5 x 5 identity matrix
print(new_array_2)

new_array_1 = np.arange(5, 51, 3)
print(new_array_1)  # creates an array starting from 5 to 31 in steps of 3

import numpy as np

x = np.array([100, 400, 500, 600])  # Each member of 'a'
y = np.array([10, 15, 20, 25])  # Each member of 'b'
condition = np.array([True, True, False, False])  # Each member of cond

# Use loops indirectly to perform this
z = [a if cond else b for a, cond, b in zip(x, condition, y)]
print(z)

# np.where(#condition, #value for true, #value for false)
z_2 = np.where(condition, x, y)
print(z_2)

z_3 = np.where(x > 0, 0, 1)
print(z_3)

# Standard functions of numpy
# Sum
print(x.sum())

n = np.array([[1, 2], [3, 4]])

# column sum
print(n.sum(0))

print(x.mean())  # Arithmetic mean
print(x.std())  # Standard deviation

# Logical operations - and / or operations

condition_2 = np.array([True, False, True])

print(condition_2.any())  # or operator
print(condition_2.all())  # and operator

# Sorting in numpy arrays
unsorted_array = np.array([1, 2, 8, 10, 7, 3])
unsorted_array.sort()
print(unsorted_array)

# Fetch unique items in an array
array = np.array(["cow", "Mahama", "girl", "cow", "lindersfarne", "cow 2", "girl"])
print(np.unique(array))

# check if element is present in array
print(np.in1d(["cow", 'mahama'], array ))
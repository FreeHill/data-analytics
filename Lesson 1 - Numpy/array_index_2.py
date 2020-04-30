import numpy as np

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d)

# access first row
print(arr2d[1])

# access first element in first row
print(arr2d[0][0])

# access last element in last row
print(arr2d[2][2])

print('\n**********\n')

# slices of 2d array
print(arr2d[0:1, 0:2])  # access row 1 and elements from index 0 to 1
print(arr2d[0:2, 0:3])  # access row 1 and 2 and elements from index 0 to 2

slice_1 = arr2d[:2, :3]
print("\n", slice_1, "\n")

arr2d[:2, :3] = 15
print(arr2d)

print('\n**********\n')

# using loops to index
arr_len = arr2d.shape[0]  # number of rows passed to arr_len
print(arr_len)

for _ in range(arr_len):
    arr2d[_] = _

print(arr2d)

print('\n**********\n')

# another way of accessing rows
print(arr2d[[0, 1]])  # access row 0 and 1
print(arr2d[[1, 0]])  # access row 1 and 0

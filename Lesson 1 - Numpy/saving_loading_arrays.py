import numpy as np

arr = np.arange(10)
print(arr, "\n")

# Save array, arr with file name 'saved_array'
np.save('saved_array', arr)

new_array = np.load('saved_array.npy')
print(new_array, "\n")

# Save multiple arrays in a file
array_1 = np.arange(25)
array_2 = np.arange(30)
np.savez('saved_archive.npz', x=array_1, y=array_2)

load_archive = np.load('saved_archive.npz')
print(load_archive['x'])
print(load_archive['y'], "\n")

# Save to txt file
np.savetxt('file.txt', array_1, delimiter=',')

# Load txt file
load_txt_file = np.loadtxt('file.txt', delimiter=',')
print(load_txt_file, '\n')
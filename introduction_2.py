# How to create numpy matrix
# matrix is 2D array
# for make matrix use np.matrix

import numpy as np


c = np.matrix([[1,2,3],[3,4,5]])
d = np.array([[[3,4,5],[1,2,3]],[[1,2,3],[3,4,5]]])

# For chack matrix dimension use ndim

print(d.ndim)
# NumPy has a whole sub module dedicated towards matrix operations called numpy.mat

v = np.array([1,2,2,6,4], ndmin = 5)
print(v)

print("The dimension of this array is: ", v.ndim)


# Access array elements

print (c[0]) # access 1-D array

print(c[0,1]) # access 2-D array

print(d[0,1,2]) # access 3-D array

# There is query for how to look like 3d array 


# for this go on this link - https://www.askpython.com/wp-content/uploads/2023/02/3D-array-1.png

# Example:

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])

# The first number represents the first dimension, which contains two arrays:

# [[1, 2, 3], [4, 5, 6]]

# and:

# [[7, 8, 9], [10, 11, 12]]

# Since we selected 0, we are left with the first array:

# [[1, 2, 3], [4, 5, 6]]

# The second number represents the second dimension, which also contains two arrays:

# [1, 2, 3]

# and:

# [4, 5, 6]

# Since we selected 1, we are left with the second array:

# [4, 5, 6]

# The third number represents the third dimension, which contains three values:

# 4
# 5
# 6

# Since we selected 2, we end up with the third value:
# 6



# Negetive indexing

# It can access array elements from the end using negative indexing

print(c[-1,-1])
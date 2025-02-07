# Shape of an Array:

# The shape of an array is the number of elements in each dimension.

import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)

# What does the shape tuple represent?

# Integers at every index tells about the number of elements the corresponding dimension has.

# In the example above at index-4 we have value 4, so we can say that 5th ( 4 + 1 th) dimension has 4 elements.


# Array Re-Shape :

# Reshaping means changing the shape of an array.\

# By reshaping we can add or remove dimensions or change number of elements in each dimension.

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = x.reshape(4, 3)

print(newarr)
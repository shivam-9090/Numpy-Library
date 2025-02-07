# Joining NumPy Arrays ::

# Joining means putting contents of two or more arrays in a single array.

# In SQL we join tables based on a key, whereas in NumPy we join arrays by axes.

# We pass a sequence of arrays that we want to join to the concatenate() function, along with the axis. If axis is not explicitly passed, it is taken as 0.

# Example :
# Join two NumPy arrays along the first axis:

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = np.concatenate((a, b), axis=0)

print(c)    # Output: [1 2 3 4 5 6]

# Join two 2-D arrays along rows (axis=1):
arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)
# Output: [[1 2 5 6]
#         [3 4 7 8]]

# Note : axis=1 means joining along rows.

# Stacking Along Rows ::

# NumPy provides a helper function: hstack() to stack along rows.
from numpy import *

arr1 = array([1, 2, 3])

arr2 = array([4, 5, 6])

arr = hstack((arr1, arr2))

print(arr)  # Output: [1 2 3 4 5 6]

# Stacking Along Columns ::

# Stacking along columns is done using the vstack() function.

# NumPy provides a helper function: vstack()  to stack along columns.

# Example
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))

print(arr) 
# Output: [[1 2 3]
#         [4 5 6]]

# Stacking Along Height (depth) ::

# Stacking along height is done using the dstack() function.

# NumPy provides a helper function: dstack() to stack along height, which is the same as depth.

# Example
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.dstack((arr1, arr2))

print(arr)

# Output: [[[1 4]
#         [2 5]
#         [3 6]]]


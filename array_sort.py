# Array sort::
# 1. sort() - sort the array in ascending order
# 2. sort() - sort the array in descending order

# Sorting Arrays ::

# Sorting means putting elements in an ordered sequence.

# Ordered sequence is any sequence that has an order corresponding to elements, like numeric or alphabetical, ascending or descending.

# The NumPy ndarray object has a function called sort(), that will sort a specified array.

# Sort the array:

import numpy as np

arr = np.array([3, 2, 0, 1])

print(np.sort(arr))

# Output will be :: [0 1 2 3]

# Note: This method returns a copy of the array, leaving the original array unchanged.

arr = np.array(['banana', 'cherry', 'apple'])

print(np.sort(arr))

# Output will be :: ['apple' 'banana' 'cherry']

arr = np.array([True, False, True])

print(np.sort(arr))

# Output will be :: [False  True  True]

# Sorting a 2-D Array ::

# If you use the sort() method on a 2-D array, both arrays will be sorted:

# Example

# Sort a 2-D array:

import numpy as np

arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))

# Output will be :: [[0 1 2] [3 4 5]]
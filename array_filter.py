# Filtering Arrays::

# Getting some elements out of an existing array and creating a new array out of them is called filtering.

# In NumPy, you filter an array using a boolean index list.

# A boolean index list is a list of booleans corresponding to indexes in the array.

# If the value at an index is True that element is contained in the filtered array, if the value at that index is False that element is excluded from the filtered array.


# Create an array from the elements on index 0 and 2:

import numpy as np

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr)

# The example above will return [41, 43], why?

# The value at index 0 is True and the value at index 2 is True, so the elements on those indexes are included in the filtered array.

# The value at index 1 is False and the value at index 3 is False, so the elements on those indexes are excluded from the filtered array.

# Example
# Create a filter array that will return only values higher than 42:

import numpy as np

arr = np.array([41, 42, 43, 44])

x = arr > 42

newarr = arr[x]

print(newarr)

# Output will be :: [43, 44]

# The example above will return [43, 44], why?

# The value at index 0 is True and the value at index 2 is True, so the elements on those indexes are included in the filtered array.

# The value at index 1 is False and the value at index 3 is False, so the elements on those indexes are excluded from the filtered array.

# Creating Filter Directly From Array::
# Create a filter array that will return only even elements from the original array:

# Examaple::

import numpy as np

arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
# Output will be :: [False False True True]
print(newarr)
# Output will be :: [43 44]

# Creating Filter Directly From Array::

# Create a filter array that will return only even elements from the original array:

import numpy as np

arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = arr > 42

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

# Output will be :: [False False True True]
# Output will be :: [43 44]


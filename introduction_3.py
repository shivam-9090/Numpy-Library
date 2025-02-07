# Array slicling :
# We pass slice instead of index like this: [start:end].

# We can also define the step, like this: [start:end:step].

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])

# Note: The result includes the start index, but excludes the end index.

arr1 = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr1[1:5:2])


# Slicing 2-D Arrays

arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr2[1, 1:4])

print(arr2[0:4, 1:4])
# Note: Remember that second element has index 1.


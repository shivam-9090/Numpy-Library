# Array iterating :
from numpy import *

arr = array([1,2,3,4])

for x in arr:
    print(x,end=",")

# Output will be :
1,2,3,4

# Iterating in 2-D shape:

arr2 = array([[1,2,3],[4,5,6]])

for x in arr2 :
    print(arr2)

# Output will be :
# [1 2 3]
# [4 5 6]

# Note : If we iterate on a n-D array it will go through n-1th dimension one by one.

arr2 = array([[1,2,3],[4,5,6]])

for x in arr2 :
    for y in x :
        print(arr2)

# Output will be :
# 1,2,3,4,5,6

# Note : If we iterate on a n-D array it will go through n-1th dimension one by one.

# Iterating 3-D Arrays

# In 3d array is go through in 2d array

arr = array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  print(x)

# Output will be :
# [[1 2 3]
# [4 5 6]]
# [[7 8 9]
# [10 11 12]]

arr = array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  for y in x:
    for z in y:
      print(z)

# Output will be :
# 1,2,3,4,5,6,7,8,9,10,11,12

# Iterating Arrays Using nditer() ::

# The function nditer() is a helping function that can be used from very basic to very advanced iterations. It solves some basic issues which we face in iteration, lets go through it with examples.

# Iterating on Each Scalar Element

# In basic for loops, iterating through each scalar of an array we need to use n for loops which can be difficult to write for arrays with very high dimensionality.

arr = array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in nditer(arr):
  print(x)

# Output will be :  
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8

# Iterating Array With Different Data Types ::

# We can use op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating.

# NumPy does not change the data type of the element in-place (where the element is in array) so it needs some other space to perform this action, that extra space is called buffer, and in order to enable it in nditer() we pass flags=['buffered'].

arr = array([1,2,4,5])

for x in nditer(arr, op_dtypes=['S']):
  print(x)

# Output will be :
# b'1'
# b'2'
# b'4'
# b'5'

# Iterating With Different Step Size ::

# We can use filtering and followed by iteration.

# Example: 

# Iterate through every scalar element of the 2D array skipping 1 element:



arr = array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in nditer(arr[:, ::2]):
  print(x)

# Output will be :
# 1
# 3
# 5
# 7

# Enumerated Iteration Using ndenumerate() ::
 
# Enumeration means mentioning sequence number of somethings one by one.

# Sometimes we require corresponding index of the element while iterating, the ndenumerate() method can be used for those usecases.

# Enumerate on following 1D arrays elements:

arr = array([1, 2, 3])

for idx, x in ndenumerate(arr):
  print(idx, x)

# Output will be :
# (0, 1)
# (1, 2)
# (2, 3)

arr = array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in ndenumerate(arr):
  print(idx, x)

# Output will be :
# (0, 0)
# (0, 1)
# (0, 2)
# (0, 3)
# (1, 0)
# (1, 1)
# (1, 2)
# (1, 3)
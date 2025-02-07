# In numpy we have some data ypes
# 1. int
# 2. float
# 3. boolean
# 4. complex
# 5. string

# Below is a list of all data types in NumPy and the characters used to represent them.

# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )

import numpy as np

a = np.array([1,2,3])

print(a.dtype)

b = np.array([1.0,2.0,3.0])

print(b.dtype)

c = np.array(['a','b','c'])

print(c.dtype)

d = np.array([True, False, True])

print(d.dtype)

e = np.array([1+2j, 2+4j])

print(e.dtype)


# Creating Arrays With a Defined Data Type

f = np.array([1,2,3], dtype = 'i4')
print(f)
print(f.dtype)


# What if a Value Can Not Be Converted?

# ValueError: In Python ValueError is raised when the type of passed argument to a function is unexpected/incorrect.

# Example

g = np.array(['a','2','3'], dtype = 'i')

print(g)

# Output: ValueError: invalid literal for int() with base 10: '2'



# Converting Data Type on Existing Arrays

# The best way to change the data type of an existing array, is to make a copy of the array with the astype() method.

# The astype() function creates a copy of the array, and allows you to specify the data type as a parameter.

# The data type can be specified using a string, like 'f' for float, 'i' for integer etc. or you can use the data type directly like float for float and int for integer.

# Example

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)
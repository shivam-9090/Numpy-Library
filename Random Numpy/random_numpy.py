# What is a Random Number?
# Random number does NOT mean a different number every time. Random means something that can not be predicted logically.

# Pseudo Random and True Random ::

# Computers work on programs, and programs are definitive set of instructions. So it means there must be some algorithm to generate a random number as well.

# If there is a program to generate random number it can be predicted, thus it is not truly random.

# Random numbers generated through a generation algorithm are called pseudo random.

# Can we make truly random numbers?

# Yes. In order to generate a truly random number on our computers we need to get the random data from some outside source. This outside source is generally our keystrokes, mouse movements, data on network etc.

# We do not need truly random numbers, unless it is related to security (e.g. encryption keys) or the basis of application is the randomness (e.g. Digital roulette wheels).

# In this tutorial we will be using pseudo random numbers.

# Generate Random Number ::

# NumPy offers the random module to work with random numbers.

from numpy import random

x = random.randint(100)

print(x) # Output: A random number between 0 and 100

# Generate Random Float ::

y = random.rand()

print(y) # Output: A random number between 0 and 1

# Generate Random Array::
# In NumPy we work with arrays, and you can use the two methods from the above examples to make random arrays.

# Integers ::
# The randint() method takes a size parameter where you can specify the shape of an array.

x = random.randint(100, size=(5))

print(x) # Output: An array with 5 random integers between 0 and 100

x = random.randint(100, size=(3, 5))

print(x) # Output: A 2-D array with 3 rows, each row containing 5 random integers between 0 and 100

# Floats ::
# The rand() method takes a size parameter where you can specify the shape of an array.

x = random.rand(5)

print(x) # Output: An array with 5 random floats between 0 and 1

# Generate Random Number From Array ::

# The choice() method allows you to generate a random value based on an array of values.

# The choice() method takes an array as a parameter and randomly returns one of the values.

x = random.choice([3, 5, 7, 9])

print(x) # Output: A random value from the array

x = random.choice([3, 5, 7, 9], size=(3, 5))

print(x) # Output: A 2-D array with 3 rows, each row containing 5 random values from the array


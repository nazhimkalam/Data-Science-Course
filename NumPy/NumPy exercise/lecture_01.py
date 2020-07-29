import numpy as np

# arange(start, stop, step) using arange() we can create an array in a shorter method
print(np.arange(0,11,2))

# zeros((x,y)) 'x' is the row or "number of dimensions" & 'y' is the column or the number of elements in each dimension (row)
print(np.zeros((2,5)))

# ones((x,y)) 'x' is the row or "number of dimensions" & 'y' is the column or the number of elements in each dimension (row)
array03 = np.ones((3,6))
print(array03)

# linespace(start, stop, number of intervals) Return "evenly spaced numbers" over a specified interval between start and stop
print(np.linspace(2,10,50)) # NOTE: takes both 2 and 10 inclusive

# Creating Identity Matrices using eye(x), x represents the number of rows and columns
# This returns a square matrix therefore row = column = x
print(np.eye(1))
print(np.eye(2))
print(np.eye(3))
print(np.eye(4))
print(np.eye(5))

# We can display random number between 0 to 1 using random.rand()
print(np.random.rand(8))   # returns 8 random values between 0 and 1
print(np.random.rand(2,5)) # returns 2 dimensions (rows) with 5 elements for each dimension

# We also can use random.randn() which returns a matrix of random values from a univariate “normal” (Gaussian)
# distribution of mean 0 and variance 1.
print(np.random.randn(8))
print(np.random.randn(4,4))

# We also can use random.randint(x, y, z)
#   x = start number
#   y = end number
#   z = number of random values to be returned
# Depending on z it returns an array of random INTEGERS between x and y, x inclusive where as y exclusive
print(np.random.randint(1,101,50))

# reshaping arrays (EQUAL DISTRIBUTION)
arr = np.arange(0,50)     # this is a 1-D array
arr2 = arr.reshape(5,10)  # 2-D array with 10 elements each dimension
print(arr2)

# By checking the starting number of '[' you can decide the array dimension  [ HINT ]
# '[' this is 1-D array
# '[[' this is 2-D array
# '[[[' this is 3-D array
# '[[[[' this is 4-D array
# '[[[[[' this is 5-D array
myRandomArray = np.random.randint(1,51,50)
print('\nThis is the array',myRandomArray)

# GETTING MAXIMUM VALUE OF AN ARRAY using max()
print(myRandomArray.min(),'this is the minimum value')

# GETTING MINIMUM VALUE OF AN ARRAY using min()
print(myRandomArray.max(),'this is the maximum value')

# GETTING THE INDEX VALUE OF THE MINIMUM VALUE FROM THE ARRAY USING argmin()
print(myRandomArray.argmin(),'is the index for the minimum value')

# GETTING THE INDEX VALUE OF THE MAXIMUM VALUE FROM THE ARRAY USING argmax()
print(myRandomArray.argmax(),'is the index for the maximum value')

# Shape of the array
arr = arr.reshape(5,10)
print(arr.shape) # returns the shape of the array (5,10)

# data type of the array
print(arr.dtype)  # returns the data type of the array
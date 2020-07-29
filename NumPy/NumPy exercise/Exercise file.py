import numpy as np

# create an array of 10 zeros
print(np.zeros(10))

# create an array of 10 ones
print(np.ones(10))

# create an array of 10 fives
print(np.ones(10) * 5)

# create an array of integers from 10 to 50
print(np.arange(10, 51))

# create an array of all even integers from 10 to 50
arr = np.arange(10, 51)
print(arr[arr % 2 == 0])

# create 3x3 matrix ranging from 0 to 8
print(np.arange(0, 9).reshape(3, 3))

# create a 3x3 identity matrix
print(np.eye(3))

# Use NumPy to generate a random number between 0 and 1
print(np.random.rand())

# Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution
print(np.random.randn(25))

# Create an array of 100 linearly spaced points between 0 and 1
print(np.linspace(0.01, 1, 100).reshape(10, 10))

# Create an array of 20 linearly spaced points between 0 and 1
print(np.linspace(0, 1, 20))

# NUMPY INDEXING AND SELECTION
mat = np.arange(1, 26).reshape(5, 5)
print(mat)

# Selecting a sub matrix from a matrix (mat) [[12, 13, 14, 15],
#                                             [17, 18, 19, 20],
#                                             [22, 23, 24, 25]]
print(mat[2:, 1:])

# Displays 20 from the matrix
print(mat[3, 4])

# Produce this sub array [[ 2],
#                         [ 7],
#                         [12]]
print(mat[:3, 1:2])

# Displays  [21, 22, 23, 24, 25]
print(mat[4])

# Display [[16, 17, 18, 19, 20],
#         [21, 22, 23, 24, 25]]
print(mat[3:5])

# Get the sum of all the values in mat
print(mat.sum())

# Get the standard deviation of the values in mat
print(mat.std())

# Get the sum of all the columns in mat
# axis is an attribute of the sum() function
# axis = 0 represents the y axis of the table and axis = 1 represents the x axis of the table matrix
print(mat.sum(axis=0))  # returns the sum of the columns
print(mat.sum(axis=1))  # returns the sum of the rows
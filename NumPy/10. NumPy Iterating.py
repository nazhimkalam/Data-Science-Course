# Iterating Arrays

# Iterating means going through elements one by one.
# As we deal with multi-dimensional arrays in numpy, we can do this using basic for loop of python.
# If we iterate on a 1-D array it will go through each element one by one.

# 1-D Array
import numpy as np

arr = np.array([1, 2, 3])
for x in arr:
    print(x)

# Iterating 2-D Arrays
# In a 2-D array it will go through all the rows.

arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
    print(x)
for x in arr:
    for y in x:
        print(y)

# Iterating 3-D Arrays
# In a 3-D array it will go through all the 2-D arrays.

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
    print(x)
# To return the actual values, the scalars, we have to iterate the arrays in each dimension.

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
    for y in x:
        for z in y:
            print(z)

# Iterating Arrays Using nditer()

# The function nditer() is a helping function that can be used from very basic to very advanced iterations.
# It solves some basic issues which we face in iteration,

# Iterating on Each Scalar Element (rather than using n number of for loops for the dimension this is an easier method)

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
    print(x)

# Iterating Array With Different Data Types

# We can use op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating.

# NumPy does not change the data type of the element in-place (where the element is in array) so it needs some
# other space to perform this action, that extra space is called buffer, and in order to enable it in nditer() we pass flags=['buffered'].

arr = np.array([1, 2, 3])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):  # only for this loop we change the datatype
    print(x)
    print(x.dtype)

for x in arr:
    print(x)
    print(x.dtype)

# Iterating With Different Step Size

# We can use filtering and followed by iteration.

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
    print(x)

# Enumerated Iteration Using ndenumerate()

# Enumeration means mentioning sequence number of somethings one by one.

# Sometimes we require corresponding index of the element while iterating, the ndenumerate() method can be used for those usecases.

arr = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr):
    print(idx, x)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(arr):
    print(idx, x)


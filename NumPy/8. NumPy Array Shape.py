import numpy as np
# 1-D array shape
arr1 = np.array([1,2,3,4])
print(arr1.shape)  # (4,) meaning 4 elements present

# 2-D array shape
arr2 = np.array([[3, 4, 5], [5, 6, 7]])
print(arr2.shape) # (2, 3) meaning 2 dimensions with 2 elements equally

# 2-D array shape
arr3 = np.array([[3, 4], [5, 6, 7]])
print(arr3.shape) # (2,) meaning 2 dimensions with not equal number of elements

# 2-D array shape
arr4 = np.array([[3, 4, 5], [5, 7]])
print(arr4.shape) # (2,) meaning 2 dimensions with not equal number of elements

# 5-D array shape
# The number of elements in the tuple represent the array shape (number of elements - D)
ar = np.array([5, 2, 4, 3, 9, 7], ndmin=5)
print(ar)                                # [[[[[5 2 3 9]]]]]
print('shape of array :', ar.shape)      # (1, 1, 1, 1, 6)

# What does the shape tuple represent?
#-----> The last element represent the number of elements you used to create the array

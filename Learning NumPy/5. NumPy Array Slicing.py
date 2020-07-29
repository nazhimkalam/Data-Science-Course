# [start:end:step]
import numpy as np

#----SLICING---1-D----ARRAY---------
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
# Slicing elements from 2 to 4
print(arr[1:4])  # displays 2 3 4
print(arr[-5:-2])  # displays 2 3 4

# Slice elements from index 2 till the end of the array
print(arr[2:])

# Slice elements from the start of the array till index 8
print(arr[:9])

# Reverse all the elements in the array using "step"
print(arr[::-1])  # --> the start and the end is left empty because we are reversing all the elements

# Using "STEP"
# By using positive step integers it will step forwards and starts collecting elements from the end of the array
# This is the default stepping which returns an array with  each and every value from the array
print(arr[::1])

# Returns an array with the elements after stepping 2 times
print(arr[::2])

# Returns an array with the elements after stepping 3 times
print(arr[::3])

# By using negative step integers it will step backwards and starts collecting elements from the end of the array
# Returns an array with the elements after stepping 2 times
print(arr[::-2])

# Returns an array with the elements after stepping 3 times
print(arr[::-3])

#----SLICING---2-D----ARRAY---------
# --> We have to specify which array (Dimension) of the array we are about to slice then give the slicing range
arr2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr2[1][::-1])
print(arr2[1,1:3])

print(arr2[:,1])


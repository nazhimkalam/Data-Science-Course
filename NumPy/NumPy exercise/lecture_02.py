import numpy as np

arr = np.arange(0,11)
arr[1:4] = 20        # Broadcasting a values to slice
print(arr)

# broadcast slicing is a view form which affects the original array unless you specify copy() to get a copy.
arr = np.arange(0,11)
arr_copy = arr
arr_copy[1:10] = 49
print(arr)           # view form that's why the original data has also changed

# Overcome the above problem
arr = np.arange(0,11)
arr_copy = arr.copy()   # copy()
arr_copy[1:10] = 49
print(arr)

# 2-D aka 'Matrix'
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

# accessing elements using double bracket
print(arr[2][0])    # displays 7
# accessing elements using single bracket
print(arr[2,0])     # displays 7

# arr = [[1,2,3],
#        [4,5,6],
#        [7,8,9]]
# If i need to get 2 3 5 6 matrix i have to make use of split
# arrayName[dimension, element]
print(arr[:2, 1:])

# If i need to get 2 3 5 6 8 9 matrix i have to make use of split
print(arr[:,1:])

# CONDITIONAL FILTERING AN ARRAY
arr = np.arange(0,11)
print(arr[arr < 5])
print(arr[arr > 5])



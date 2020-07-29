# Sorting Arrays
# Sorting means putting elements in a ordered sequence.

# Ordered sequence is any sequence that has an order corresponding to elements, like numeric or alphabetical, ascending or descending.

# The NumPy ndarray object has a function called sort(), that will sort a specified array.

import numpy as np

arr = np.array([3, 2, 0, 1])

print(np.sort(arr))

# Note: This method returns a copy of the array, leaving the original array unchanged.

# You can also sort arrays of strings, or any other data type

# Sort the array alphabetically:
arr = np.array(['banana', 'cherry', 'apple'])

print(np.sort(arr))

#Sort a boolean array:
arr = np.array([True, False, True])

print(np.sort(arr))   # result is [False  True  True] because its similar to [0 1 1]

# Sorting a 2-D Array
# If you use the sort() method on a 2-D array, both arrays will be sorted:

arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))



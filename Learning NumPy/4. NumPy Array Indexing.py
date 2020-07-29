import numpy as np
# POSITIVE INDEXING
print("\nPositive-Indexing\n")
# Access Array Elements
# --> You can access an array element by referring to its index number.
# --> The indexes in NumPy arrays start with 0, meaning that the first element has index 0, and the second has index 1 etc.

# Accessing 1-D array elements
arr1 = np.array([5,4,8,7])
print('The first element in our array is',arr1[0])

print('These are the elements in the array')
for x in arr1: # we can loop through the array and output the values
    print(x)
print()

print('The result of adding the first element and the second element is',arr1[0] + arr1[1])

# Accessing 2-D array elements
arr2 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr2[0][1])       # 1st dimension 2nd element

# Accessing 3-D array elements
#--> 2 dimensions and element index
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])   # This is a 3-D array
print(arr3[0][1][2])  # displays 6

# NEGATIVE INDEXING
print("\nNegative-Indexing\n")
arr4 = np.array([12,34,56,79])
print(arr4[2])  # accessing elements using a positive index, displays 34
print(arr4[-3]) # accessing elements using a negative index, display 34



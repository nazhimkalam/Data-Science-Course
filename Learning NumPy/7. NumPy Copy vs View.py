# NumPy Array COPY vs VIEW

# The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view
# of the original array.

# The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the
# original array will not affect the copy.

# The view does not own the data and any changes made to the view will affect the original array, and any changes made
# to the original array will affect the view.
import numpy as np

# COPY --------- using copy() function
originalArray = np.array([1,2,3,4])       # This is the original array
copyArray = originalArray.copy();         # This is the copy array
originalArray[0] = 42                     # changing element of original array
print('This is the original array',originalArray)  # original array has 42
print('This is the copy array',copyArray)          # copy array has no 42

# VIEW --------- using view() function
originalArray2 = np.array([84,57,98,65,99])       # This is the original array 2
viewArray = originalArray2.view();                # This is the view array
originalArray2[0] = 2                             # changing element of original array 2
print('This is the original array 2',originalArray2)  # original array has 42
print('This is the view array',viewArray)             # view array has  42

# Check if Array Owns it's Data
# As mentioned above, copies owns the data, and views does not own the data, but how can we check this?
# Every NumPy array has the attribute "base" that returns "None" if the array owns the data.
# Otherwise, the base  attribute refers to the "original object".

myArray = np.array([1,2,3,4,5,6,7,8,9])
c = myArray.copy()
v = myArray.view()
print(c.base, 'copy')   # copy returns None
print(v.base, 'view')   # view returns the Original Array which is [1,2,3,4,5,6,7,8,9]


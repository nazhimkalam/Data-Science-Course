# Checking the Data Type of an Array
#--> The NumPy array object has a property called "dtype" that returns the data type of the array

import numpy as np
arr = np.array([1,2,3,4])
print(arr.dtype)    # displays int32

arr1 = np.array(['apple', 'banana', 'cherry'])
print(arr1.dtype)

# Creating Arrays With a Defined Data Type
# --> We use the array() function to create arrays, this function can take an optional argument:
# --> dtype that allows us to define the expected data type of the array elements

arr2 = np.array([1, 2, '3', 4], dtype='S') # "S" MEANS STRING DATA TYPE
print(arr2)
print(arr2[0] + arr2[2])
print(arr2.dtype)

# For i, u, f, S and U we can define size as well.
# Create an array with data type 4 bytes integer
myArray = np.array([1, 2, 3, 4], dtype='i4')
print(myArray)
print(myArray.dtype)

# WHAT IF A VALUE CANNOT BE CONVERTED?
# If a type is given in which elements can't be casted then NumPy will raise a ValueError.

# ValueError: In Python ValueError is raised when the type of passed argument to a function is unexpected/incorrect.

# Example
# A non integer string like 'a' can not be converted to integer (will raise an error):
# import numpy as np
# a = np.array(['a', '2', '3'], dtype='i')    # Displays an error indicating that invalid integer 'a'
# print(a)

# -------------------------------------------------------------------------------------------------------------------

# CONVERTING DATA TYPE ON EXISTING ARRAYS
# The best way to change the data type of an existing array, is to make a copy of the array with the astype() method.

# The astype() function creates a copy of the array, and allows you to specify the data type as a parameter.

# The data type can be specified using a string, like 'f' for float, 'i' for integer etc.
# or you can use the data type directly like float for float and int for integer.

oldArr = np.array([1.2,1.3,-1.5,2.5,0,8.9])   # float type
newArr = oldArr.astype('i')                   # integer type (we can use either 'i' or 'int')
newArrBool = oldArr.astype('bool')            # [ True  True  True  True False  True]
print(newArrBool)    # boolean form
print('This is the old array:',oldArr)         # [1.2 1.3 1.5 2.5 4.5 8.9]
print('Data type of old array:',oldArr.dtype)  # float64
print('This is the new array:',newArr)         # [1 1 1 2 4 8]
print('Data type of new array:',newArr.dtype)  # int32


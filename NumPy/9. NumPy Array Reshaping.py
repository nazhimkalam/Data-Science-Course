import numpy as np

# ------> RESHAPING ARRAYS

# - Reshaping means changing the shape of an array.
# - The shape of an array is the number of elements in each dimension.
# - By reshaping we can 'add or remove dimensions' or 'change number of elements in each dimension.'
# - By using the function reshape() we can achieve this

# ------> RESHAPE FROM 1-D TO 2-D

# - Convert the following 1-D array with 12 elements into a 2-D array.
# - The outermost dimension will have 4 arrays, each with 3 elements.

myArray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newArray = myArray.reshape(4, 3)  # 4 dimensions and 3 elements for each dimension
print(newArray)

print('-----------------------------------------------------------------------------------------')

# ------> RESHAPE FROM 1-D TO 3-D

# - Convert the following 1-D array with 12 elements into a 3-D array.
# - The outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements

nextArray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
myNewArray = nextArray.reshape(2, 3, 2)
print(myNewArray)

# ----->  CAN WE RESHAPE INTO ANY SHAPE ?????????

# - Yes, as long as the elements required for reshaping are "equal" in both shapes.
# - We can reshape an 8 elements 1D array into 4 elements in 2 rows 2D array but we cannot reshape
#   it into a 3 elements 3 rows 2D array as that would require 3x3 = 9 elements.

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])  # This will throw error because (3,3) you are able to make 3 dimensions but
# newArr = arr.reshape(3, 3)                # not able to distribute the 8 elements equally into each dimension
# print(newArr)

# WILL THIS RESHAPING RETURN A COPY ARRAY OR THE VIEW ARRAY ??????
# - LET'S CHECK IT USING THE .base ATTRIBUTE
# ( Let's refer to the code on line 20 to 22 )
print(myNewArray.base)  # It returns the array object therefore it a VIEW array type NOT COPY type

print('-----------------------------------------------------------------------------------------')

# UNKNOWN DIMENSION ARRAY ---------------------------

# * You are allowed to have one "unknown" dimension.
# * Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.
# * Pass -1 as the value, and NumPy will calculate this number for you.

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newArr = arr.reshape(2, 2, -1)  # Basically by putting -1 there the NumPy will calculate the number of elements for you.
print(newArr)

print('-----------------------------------------------------------------------------------------')

#   FLATTENING THE ARRAYS ----------------------

# - Flattening array means converting a multidimensional array into a 1D array.
# - We can use reshape(-1) to do this.

twoDArray = np.array([[1, 2, 3], [7, 8, 9], [6, 8, 0]])  # This is a 2-D Array
twoDArrayToOneDArray = twoDArray.reshape(-1)             # By using -1 it converts it into a 1-D array
print(twoDArrayToOneDArray)

threeDArray = np.array([[[1,2],[4,5]],[[3,7],[54,65]]])  # This is a 3-D Array
threeDArrayToOneDArray = threeDArray.reshape(-1)         # By using -1 it converts it into a 1-D array
print(threeDArrayToOneDArray)

# - Hence we can say that by using -1 we can convert any array into a 1-D array
import numpy as np
myArray = np.array([1,2,3,4,5]) # we are using the array() function or method from the numpy module or class
print(myArray)                  #display the array
print(type(myArray))            # displays the type of the array

# we can pass any array like looking object into the array() method and convert it into an array() method
myTuple = (11,22,33,44,55)       # this is my tuple
TupleToArray = np.array(myTuple)
print(TupleToArray) 

myList = ['a','b','c','d','e']
ListToArray = np.array(myList)
print(ListToArray)

# we can't use dictionary because it is not an array type because it uses key-value pair

#Dimensions in Arrays

# 0-D Arrays 
zero_D_Array = np.array(42)
print(zero_D_Array)        # displays 42 (this is basically not an ARRAY it's just an element of the array)

# 1-D Arrays
OneDArray = np.array([9,8,7,4,5,6])
print(OneDArray)                   # displays [9 8 7 4 5 6]  this contains a number of 0-D arrays 

# 2-D Arrays
twoDArray = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(twoDArray[2][0])  # displays 7

# 3-D Arrays
threeDArray = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(threeDArray[0][1][2]) # displays 6

# Checking the number of dimensions
# The ndim attribute that returns an integer that tells us how many dimensions the array have.

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print('\nDimensions of the arrays')
print(a.ndim)   # ndim stands for number of dimensions
print(b.ndim)   # ndim stands for number of dimensions
print(c.ndim)   # ndim stands for number of dimensions
print(d.ndim)   # ndim stands for number of dimensions

#--- Higher Dimensional Arrays ---
# --> An array can have any number of dimensions, when the array is created you can define the number of dimensions by
#     using the 'ndim' argument.

arr = np.array([1,2,3,4,5,6,7], ndmin = 6)  # 6 dimensional array
print(arr)
print('The above array is of', arr.ndim,'dimensions')

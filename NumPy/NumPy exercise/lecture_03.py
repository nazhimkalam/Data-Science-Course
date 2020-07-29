import numpy as np

# NumPy Operations
arr = np.arange(0,11)
# Basic operations
# array on array operations
print(arr + arr)   # Addition
print(arr - arr)   # Subtraction
print(arr * arr)   # Multiplication
print(arr / arr)   # Division

# array on scalar operations
print(arr + 10)    # adding 10 for all elements in the array
print(arr * 100)
print(arr - 100)
print(arr / 100)
print(arr ** 2) # power

# Universal Array Functions
# These are the mathematical functions mostly
print(np.exp(arr))
print(np.log(arr))
print(np.add(arr))
print(np.sin(arr))
print(np.cos(arr))
print(np.tan(arr))

# NOTE: You won't be getting errors but you will get a warning but output is given
# Eg: 1/0 give "inf" , 0/0 gives you "nan"
# It doesn't crash but it returns a value with warning

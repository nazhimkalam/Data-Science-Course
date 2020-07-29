# Series
# Series() is a function of pandas class or module

import numpy as np
import pandas as pd

label = ['a','b','c']         # list
my_data = [10, 20, 30]        # list
arr = np.array(my_data)       # NumPy array
d = {'a':10, 'b':20, 'c':30}  # Dictionary

# Series will return the data with index

# Syntax Series (data, index, dtype, name, copy, fastpath)
# Order of the parameter matters unless you define the argument such as data = label

# If you pass in a list without an index list it will default use a number list as such [0, 1, 2, 3, 4, 5, ....
print(pd.Series(my_data))
print(pd.Series(label))
print('------------------------------------------------------------------------------------------------------------')

# You can also index the data elements by a list of your own as a parameter in the Series() function
print(pd.Series(my_data,label))
print('------------------------------------------------------------------------------------------------------------')

# Order of the data you pass a parameter matters.
# Below you will be able to see data and index gets exchanged due to incorrect parameter order
print(pd.Series(label,my_data))
print('------------------------------------------------------------------------------------------------------------')

# Series can hold any data type object as well

print(pd.Series([1,1,2,3],['Nazhim','Nazhim','Abilash','Raveen']))  # we can use "strings" as keys
print('------------------------------------------------------------------------------------------------------------')

# Accessing Data values using the index value
ser = pd.Series([1,2,3,4],['Nazhim','Ravindu','Abilash','Raveen'])

# like this you can access the data elements using the string index
print(ser['Nazhim'])
print('------------------------------------------------------------------------------------------------------------')

print(ser['Abilash'])
print('------------------------------------------------------------------------------------------------------------')

# When adding TWO series it will convert the Integer data into to float number
# Only if both the series has the same key then only it will add else, it will return NaN for that key reference
ser1 = pd.Series([1,2,3,4],['a','b','c','d'])
ser2 = pd.Series([1,2,3,4],['a','b','f','d'])
print(ser1 + ser2)



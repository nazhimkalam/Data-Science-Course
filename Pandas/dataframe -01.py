import numpy as np
import pandas as pd

# seed()
# seed is a superb function if you wanted to store a set of random numbers or data and reuse them over and over again
# seed( parameter ) takes a parameter which is like a ID for each set of random number stored
# Example of how seed works

# np.random.seed(123)     # this seed id will store this set of random numbers which is unique
# for x in range(0,8):
#     print(np.random.randint(100))
# print('----------------------------------------------------------------------------------------------------------------')
#
# np.random.seed(10001)     # this seed id will store this set of random numbers which is unique
# for x in range(0,8):
#     print(np.random.randint(100))
# print('----------------------------------------------------------------------------------------------------------------')
#
# np.random.seed(123)    # you will be able to see the same result as the above code with seed(123)
# for x in range(0,8):
#     print(np.random.randint(100))
# print('----------------------------------------------------------------------------------------------------------------')
#
# np.random.seed(10001)     # you will be able to see the same result as the above code with seed(10001)
# for x in range(0,8):
#     print(np.random.randint(100))

#--------------------------------------------Data-Frames----------------------------------------------------------------

#  A Data frame is a two-dimensional data structure like a TABLE with ROWS and COLUMNS
# Each column in a data frame represents a Series
# Data frame function comes from pandas module

from numpy.random import randn
np.random.seed(101)

dataFrame = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(dataFrame)   # You will get a table with 5 rows and 4 columns
# randn(5,4) means create a table of random numbers under normal distribution with 5 rows and 4 columns (this is the data set)
# ['A','B','C','D','E'] this is column heading
# ['W','X','Y','Z'] this is the row heading
# Similar to Series

# Displaying a Series from a data frame (each column or row in a data frame is a series)
# More than one Series together becomes a data frame
print(dataFrame['W'])                   # we are using the index like series to get its data content
print(type(dataFrame['W']))             # displays <class 'pandas.core.series.Series'>

# if you need to view more than one column the output becomes a data frame
# A frame also can be considered as a series
# Numbers of series together forms a data frame
print(dataFrame[['W','Z']])
print(type(dataFrame[['W','Z']]))       # <class 'pandas.core.frame.DataFrame'>

# Creating a new column into the data frame
dataFrame['NEW'] = dataFrame['W'] + dataFrame['X']
print(dataFrame)

# Deleting / Dropping a column from a table
# If you need to delete permanently, you have to include inplace = True
dataFrame.drop('NEW',axis=1)  # to specify to delete from the x axis not from y
print(dataFrame)              # you will still see that 'NEW' column isn't deleted because we didn't include inplace = True

dataFrame.drop('NEW', axis=1, inplace=True)
print(dataFrame)              # Now you can see that it's removed

# There are 2 ways of selecting rows

print('---------------------------------------------------------------------------------------------------------------')
# By using the loc we can get the row in a form of series by loc['row index label'], this returns a row series
print(dataFrame.loc['A'])   # loc stands for 'location'

print('---------------------------------------------------------------------------------------------------------------')
# By using iloc[] we can get the row in a form of series, but inside iloc['NUMBERICAl index position of the row']
print(dataFrame.iloc[2])

print('---------------------------------------------------------------------------------------------------------------')
print(dataFrame)
# if you need to get a specific value when the required row and column intersects loc['row','column']
print(dataFrame.loc['C','Y'])  # returns 0.528813
# or using iloc[]
print(dataFrame.iloc[2,2])

print('---------------------------------------------------------------------------------------------------------------')
# returning a sub data frame
print(dataFrame.loc[['B','D'],['W','Z']])  # the intersecting data by the rows and columns are only displayed

# shape of the data frame
print(dataFrame.shape) 





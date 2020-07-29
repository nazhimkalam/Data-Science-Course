# Conditional selection with a data frame
from numpy.random import randn
import numpy as np
import pandas as pd

np.random.seed(12345)

df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['Nazhim', 'Hashim', 'Abilash', 'Divagar'])
print('---------------------------------------------longer-method-------------------------------------------------')
boolDF = df > 0
print(df)
print(boolDF)
print(df[boolDF])

# short method is like this
print('---------------------------------------------shorter-method-------------------------------------------------')
print(df[df > 0])

# You can see that we are getting NaN as the value for values less than 0
# We can overcome this by using Series to filter data
print('------------------------------------------------------------------------------------------------------------')
print(df)
print('------------------------------------------------------------------------------------------------------------')
print(df > 0)
print('------------------------------------------------------------------------------------------------------------')
print(df[df > 0])
print('------------------------------------------------------------------------------------------------------------')
print(df[df['Nazhim'] > 0])  # this remove the entire row which has NaN value in column 'Nazhim'
# NOTE: the above code can only be run on specific columns

print('------------------------------------------------------------------------------------------------------------')
# Selecting a particular column or row after filtering
print(df[df['Nazhim'] < 0]['Nazhim'])  # I am getting a series of the data of column 'Nazhim'

# NOTE: Series doesn't include NaN values

# IF we need to check two conditions at once DON"T use AND OR instead use & |
# Using AND OR returns an error because u are comparing several boolean values with several boolean values at once,
# which practically can't happen because we use 1 boolean value to compare with another boolean value
print('--------------------------------------IMPORTANT CODE-------------------------------------------')
print(df)  # original data form
print('------------------------------------------------------------------------------------------------------------')
print(df[(df['Nazhim'] > 0) & (df['Hashim'] < 1)])  # Filtering values where Nazhim > 0 and Hashim < 1
# Don't forget the parenthesis () & () or () | ()
print('------------------------------------------------------------------------------------------------------------')
print(df[(df['Nazhim'] > 0) | (df['Hashim'] > 1)])  # Filtering values where Nazhim > 0 or Hashim < 1

df_copy = df.copy()
# IF you need to reset the INDEX into a numerical for we can use the reset_index(inplace = True) function, and your previous index will
#  become a column with heading index
print(df)
print('------------------------------------------------------------------------------------------------------------')
df.reset_index(inplace=True)
print(df)
print('------------------------------------------------------------------------------------------------------------')
print(df['index'])   # Now you can access your previous index as a Series itself


# Let's say we want to add a new Column with data and make that into the new index
# We can use set_index(inplace = True) to achieve this
print()
print(df_copy)  # display the copy of the original df

newData = 'CA FG RE FN NS'.split() # easy way of creating a list
print()
print(newData)

df_copy['STATES'] = newData     # adding the new list into the data frame
print()
print(df_copy)

# converting the newly created column into an index
print()
df_copy.set_index('STATES',inplace=True)
print(df_copy)

# NOTE that the previous index are removed completely from the data frame



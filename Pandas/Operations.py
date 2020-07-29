# Operations
import numpy as np
import pandas as pd

df = pd.DataFrame({
    'col1':[1,2,3,4],
    'col2':[444,555,666,444],
    'col3':['abc','def','hij','xyz']
})

# Display unique values
print(df['col2'].unique())
print()

# Number of unique values
print(df['col2'].nunique())
print()

# Table of unique values and the number of times
print(df['col2'].value_counts())
print()

print(df[(df['col1'] > 1) & (df['col1'] < 4)])
print()

print(df[(df['col1'] > 2) & (df['col3'] == 'xyz')])
print()

# apply() method Syntax apply(function name)
print(df['col1'].apply(lambda x: x*2))   # this will multiply each element from the column and return it's result
print()

# Deleting a column or a row from a table using drop()
copyDF = df.copy()
print(copyDF)

print(copyDF.drop('col1', axis=1))
print()

print(copyDF)
print()

# getting columns names from a dataframe
print(df.columns)

# getting the indexes of a data frame
print(df.index)

# sorting data frame by column name
print('----------------sorting----------------')
print(df.sort_values(by='col2'))
print()

# checking the data inside the data frame contains any null value
print('--------------isnull()--------------')
print(df.isnull()) # returns a boolean table
print()

# Creating a Multi level index data frame to filter duplicated data from existing data frame
data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)
print('---------------current data frame which is to be converted into a multi dimensional data frame---------------')
print(df)

print('----------------------------this is the converted multi dimensional array--------------------')
multi = df.pivot_table(values='D',index=['A', 'B'],columns=['C'])
print(multi)



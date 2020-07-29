import numpy as np
import pandas as pd
# we can create a data frame using dictionary itself
d = {'A':[1, 2, np.nan],'B':[5, np.nan, np.nan],'C':[1, 2, 3]}      # this is a dictionary
df = pd.DataFrame(d)
print(df)
print()

# accessing a column in series from the data frame
print(df['A'])
print()

# accessing a row from a data frame
print(df.loc[2])
print()

# dropna() is a function of the data frame class, this removes the rows or columns which has NaN values
print(df.dropna())        # this displays data with the rows which only didn't have NaN
print()
print(df.dropna(axis=1))  # this displays data with the columns which only didn't have NaN
print()

# dropna() has a thresh parameter which filters data as to the value of thresh
# Let's say we need the rows which has at least 2 valid data
print(df.dropna(thresh=2))
print()

# Let's say we need the columns which has at least 2 valid data
print(df.dropna(axis=1, thresh=2))
print()

# We also can fill the NaN value with some other valid data using fillna() value parameter
print(df.fillna(value='NEW DATA'))
print()

# Let's do some logical data using fillna()
print(df.fillna(value = -1))
print()

# Let's filter one column and set its mean to the NaN value
print(df['A'].fillna(value = df['A'].mean()))
print()

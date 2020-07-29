import numpy as np
import pandas as pd

# What happens in group by is that we call the group by() and then call an aggregate method such as sum, max, min etc...

data = {
    'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
    'Person' : ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
    'Sales'  : [200, 120, 340, 124, 243, 350]
}

df = pd.DataFrame(data)
print(df)
print()

byComp = df.groupby('Company')
print(byComp.mean())                        # mean salary for each company in a data frame
print()
print(byComp.sum())                         # total sum for each company  in a data frame
print()
print(df.groupby('Company').sum().loc['FB'])  # total salary for FB in series
print()

print(df.groupby('Company').describe())       # displays all the data by the numerical methods






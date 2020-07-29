# Multi Index Data Frames
import numpy as np
import pandas as pd
from numpy.random import randn
np.random.seed(1)
# Index Levels
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
print(hier_index)
print()

df = pd.DataFrame(randn(6,2),hier_index,['A','B'])
print(df)

print()

# Accessing data from a multi level data frame index
print(df.loc['G1'].loc[3]['B'])   # if i need to get -2.301539

# Naming indexes
df.index.names = ['Groups','Num']
print(df)

# cross section xs() returns a cross section of data
print(df)
# Say i need to get all the numbers under index Num 1 but in all groups
print(df.xs(1, level='Num'))
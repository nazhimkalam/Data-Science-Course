import pandas as pd

# CONCATENATION

df1 = pd.DataFrame({
    'A':['A0', 'A1', 'A4', 'A3'],
    'B':['B0', 'B1', 'B2', 'B3'],
    'C':['C0', 'C1', 'C2', 'C3'],
    'D':['D0', 'D1', 'D2', 'D3',],
    }, index=[0,1,2,3]           # this is made by default in numerical form
)

df2 = pd.DataFrame({
    'A':['A4', 'A5', 'A6', 'A7'],
    'B':['B4', 'B5', 'B6', 'B7'],
    'C':['C4', 'C5', 'C6', 'C7'],
    'D':['D4', 'D5', 'D6', 'D7',],
    }, index=[4,5,6,7]           # this is made by default in numerical form
)

df3 = pd.DataFrame({
    'A':['A8', 'A9', 'A10', 'A11'],
    'B':['B8', 'B9', 'B10', 'B11'],
    'C':['C8', 'C9', 'C10', 'C11'],
    'D':['D8', 'D9', 'D10', 'D11',],
    }, index=[8,9,10,11]          # this is made by default in numerical form
)

print(df1)
print()

print(df2)
print()

print(df3)
print()

# Using Concatenation Method to Concat data
print(pd.concat([df1, df2]))    # we pass the list of data frames to concatenate and by default axis = 0
print()

print(pd.concat([df1, df2], axis=1))    # we pass the list of data frames to concatenate and by default axis = 1
print()                                 # NaN will be present because no data present when get combinations in x axis

# MERGING

right = pd.DataFrame({
    'keys' : ['k0','k1','k2'],
    'C'    : ['C0','C1','C2'],
    'D'    : ['D0','D1','D2']
})

left = pd.DataFrame({
    'keys' : ['k0','k1','k2'],
    'A'    : ['A0','A1','A2'],
    'B'    : ['B0','B1','B2']
})

print(left)
print()

print(right)
print()

# If I need to MERGE alone a particular column such as (keys)
# In general inner merging happens (just like inner joins in SQL) default how = 'inner'
print(pd.merge(left,right,on='keys'))
print()


x = pd.merge(left,right,on='keys')      # adding index name
x.index.name = 'index'
print(x)
print()

# we also can have multiple keys and merge with them, by doing like this we aren't duplicating keys when merging because both tables have the keys column
newRight = pd.DataFrame({
    'keys 01' : ['k0','k1','k2'],
    'keys 02' : ['k0','k1','k2'],
    'C'    : ['C0','C1','C2'],
    'D'    : ['D0','D1','D2']
})

newLeft = pd.DataFrame({
    'keys 01' : ['k0','k1','k2'],
    'keys 02' : ['k0','k1','k2'],
    'A'    : ['A0','A1','A2'],
    'B'    : ['B0','B1','B2']
})
print(pd.merge(newLeft, newRight, on=['keys 01','keys 02']))

print()
                                                                                    # adding index name
x = pd.merge(newLeft, newRight, on=['keys 01','keys 02'])
x.index.name = 'Index'
print(x)

# JOINING


right = pd.DataFrame({
    'C'    : ['C0','C1','C2'],
    'D'    : ['D0','D1','D2']
})

left = pd.DataFrame({
    'A'    : ['A0','A1','A2'],
    'B'    : ['B0','B1','B2']
},)

print()
print(left.join(right))
print()
print(right.join(left))

# Important Example where the default how = 'inner' is made of good use

left = pd.DataFrame({
    'A'    : ['A0','A1','A2'],
    'B'    : ['B0','B1','B2']
},
index = ['K0','K1','K2'])

right = pd.DataFrame({
    'C'    : ['C0','C1','C2'],
    'D'    : ['D0','D1','D2']
},
index = ['K0','K2','K3'])


print(left.join(right))  # since how = 'inner' it wont include K3 for join from left
print()

print(right.join(left))  # since how = 'inner' it wont include K1 for join from right
print()

# if you make it outer then you get all the data from both tables together
print(left.join(right, how='outer'))
print()

# similarly you have how = 'left' and how = 'right'
# how = 'left' means it will get all the data from the left table
print(left.join(right,how='left'))
print()

# how = 'right' means it will get all the data from the right table
print(left.join(right,how='right'))
print()
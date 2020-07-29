# ufuncs stands for "Universal Functions" and they are NumPy functions that operates on the ndarray object.
import numpy as np
# Add the Elements of Two Lists

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []

for i, j in zip(x, y):
  z.append(i + j)
print(z)

# NumPy has a ufunc for this, called add(x, y) that will produce the same result.

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)

print(z)

# There are several in-built functions like these which can be referred using w3schools.
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,100)
y = x*2
z = x**2

# Question 01
#  Create a figure object called fig using plt.figure() **
#  Use add_axes to add an axis to the figure canvas at [0,0,1,1]. Call this new axis ax. **
#  Plot (x,y) on that axes and set the labels and titles to match the plot below:**
# figure = plt.figure()
# axes = figure.add_axes([0.1,0.1,0.8,0.8])
# axes.plot(x,y)
# plt.show()

# Question 02
#   Create a figure object and put two axes on it, ax1 and ax2. Located at [0,0,1,1] and [0.2,0.5,.2,.2] respectively.
# figure1 = plt.figure()
# axes1 = figure1.add_axes([0.1,0.1,0.8,0.8])
# axes2 = figure1.add_axes([0.2,0.5,.2,.2])
# plt.show()

# Now plot (x,y) on both axes. And call your figure object to show it
# axes1.plot(x,y,color='red')
# axes2.plot(x,y,color='red')
# plt.show()

# Question 03
#    Create the plot below by adding two axes to a figure object at [0,0,1,1] and [0.2,0.5,.4,.4]
# figure = plt.figure(figsize=(8,6))
# ax1 = figure.add_axes([0.15,0.1,0.8,0.8])
# ax2 = figure.add_axes([0.25,0.5,.3,.3])
#
# ax1.plot(x,z)
# ax1.set_xlabel('x-axis')
# ax1.set_ylabel('z-axis')
#
# ax2.plot(x,y)
# ax2.set_xlabel('x-axis')
# ax2.set_ylabel('y-axis')
# ax2.set_xlim([20,22])
# ax2.set_ylim([30,50])
# plt.show()

# Question 04
#    Use plt.subplots(nrows=1, ncols=2) to create the plot below
# figure,axes = plt.subplots(nrows=1, ncols=2, figsize=(6,4))
# # plt.show()
#
# #   Now plot (x,y) and (x,z) on the axes. Play around with the linewidth and style
# axes[0].plot(x,y, linestyle='--', color='b', linewidth=3)
# axes[1].plot(x,z,color='r', linewidth=3)
# plt.show()

# See if you can resize the plot by adding the figsize() argument in plt.subplots() are copying and pasting your previous code
figure,axes = plt.subplots(nrows=1, ncols=2, figsize=(10,2))
axes[0].plot(x,y, color='b', linewidth=5)
axes[0].set_xlabel('x-axis')
axes[0].set_ylabel('y-axis')

axes[1].plot(x,z,color='r', linestyle='--', linewidth=2)
axes[1].set_xlabel('x-axis')
axes[1].set_ylabel('y-axis')
plt.show()

# saving the image in pdf format
figure.savefig('picture.pdf', dpi=200)
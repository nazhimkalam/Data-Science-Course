import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,5,11)
y = x**2
# CREATING SUB PLOTS USING OOP PYTHON ----------------------------------------------------------------------------------
fig,axes = plt.subplots(nrows=1, ncols=2)   # We are creating a figure with 2 graphs in one row with default axis 0 to 1 coordinates

# Note that these axis are in a list which can be accessed by it's index

axes[0].plot(x,y,'r')    # now we are updating the axes with the new coordinates
axes[0].set_title('FIRST GRAPH')
axes[0].set_xlabel('x-axis')
axes[0].set_ylabel('y-axis')


axes[1].plot(y,x,'g')    # now we are updating the axes with the new coordinates
axes[1].set_title('SECOND GRAPH')
axes[1].set_xlabel('x-axis')
axes[1].set_ylabel('y-axis')
# plt.show()

# IF YOUR PLOT OVER LAP USE plt.tight_layout()

# <<<<< FIGURE SIZE AND DPI ( Dots Per Inch ) using figsize = (width, height) >>>>>>

# ---Not sub plotting
figure = plt.figure(figsize=(6,3))
ax = figure.add_axes([0.1,0.1,0.8,0.8])
ax.plot(x,y,'r')


# ----sub plotting
fig,axes = plt.subplots(nrows=2, ncols=1, figsize=(6,3))
axes[0].plot(x,y)
axes[1].plot(y,x)
plt.tight_layout()
plt.show()

# SAVING A FIGURE
fig.savefig('myPicture.png',dpi=200)   # dots per inch or the quality of the image


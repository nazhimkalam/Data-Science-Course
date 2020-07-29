# plotting library
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,5,11)     # making a array of numbers
y = x**2                    # another array of numbers

# FUNCTIONAL METHOD ----------------------------------------------------------------------------------------------------
plt.plot(x,y,'g')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Title')

# subplots are sub graphs = number of graphs in a particular figure
plt.subplot(1,2,1)
plt.plot(x, y,'r')

plt.subplot(1,2,2)
plt.plot(y, x,'b')

# plt.show()

# OOP METHOD -----------------------------------------------------------------------------------------------------------
fig = plt.figure()                          # This is just used to create a blank figure (Empty space only)
axes = fig.add_axes([0.1,0.1,0.8,0.8])      # axes is basically like a graph with axis
axes.plot(x,y)                              # here we set the x and y values or coordinates of the graph
axes.set_xlabel('X label')                  # We are giving a label for the x axis
axes.set_ylabel('Y label')                  # We are giving a label for the y axis
axes.set_title('Title')                     # We are giving a title for this particular graph

fig1 = plt.figure()
axes1 = fig1.add_axes([0.1,0.1,0.8,0.8])  # [x axis, y axis, width, height] x axis and y axis of the point (0,0)
axes2 = fig1.add_axes([0.2,0.5,0.4,0.3])

axes1.plot(x,y,'r')
axes1.set_xlabel('Outer X')
axes1.set_ylabel('Outer Y')
axes1.set_title('Main Title')

axes2.plot(y,x,'g')
axes2.set_xlabel('Inner X')
axes2.set_ylabel('Inner Y')
axes2.set_title('Sub Title')

# Two lines in one graph
figure = plt.figure()
ax1 = figure.add_axes([0.1,0.1,0.8,0.8])
ax2 = figure.add_axes([0.1,0.1,0.8,0.8])
ax1.set_xlabel('time / min')
ax1.set_ylabel('number of death')
ax1.set_title('2020')

ax1.plot(x*2,y,'r', label = 'tiktok')
ax2.plot(x,y,'b', label = 'corona')

plt.legend(loc=0)
figure.savefig('virus.pdf', dpi = 500)
plt.show()
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,5,11)     # making a array of numbers
y = x**2                    # another array of numbers

figure = plt.figure();
ax = figure.add_axes([0.1,0.1,0.8,0.8])
ax.plot(x,y,color = 'red', linewidth=2, alpha=0.5, linestyle='--', marker='o', markersize=20,
        markerfacecolor='yellow', markeredgewidth=3, markeredgecolor='green')
figure.savefig('designGraph.pdf', dpi=500)
# plt.show()

# if you need to focus on a part of the graph in more detail
fig = plt.figure(figsize=(6,4))
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes.plot(x,y,color = 'red', marker = 'o', markersize = 15, markerfacecolor = 'blue', markeredgecolor = 'black', markeredgewidth = 2)
axes.set_xlim([0,2]) # setting the limit for x
axes.set_ylim([0,5]) # setting the limit for x
plt.show()

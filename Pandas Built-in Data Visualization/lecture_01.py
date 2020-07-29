import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.DataFrame(np.random.randn(1000, 3), columns=['A', 'B', 'C'])
# print(df.head())

# print(df['A'].hist(bins=30))        # histogram graph

# you can create a histogram in this way as well by using plot()
# print(df['A'].plot(kind='hist',bins=100))  # bins refers to number of bars, higher the number of bars higher the level of accuray

# print(df['A'].plot.area(alpha=0.8))
df1 = pd.DataFrame(np.random.rand(1000,5), columns=['A', 'B','C','D','E'])
# df1.head().plot.area(alpha=0.7)
# df1.head().plot.bar(stacked=True)


# df1.plot.scatter(x='A', y='B', c = "D", cmap="coolwarm")
# df1.plot.scatter(x='A', y='B', s=df1['C']*100, cmap="coolwarm")

# df1.plot.box()

# df.plot.hexbin(x='A', y='B', gridsize=25)

# df['A'].plot.kde()
# df['A'].plot.density()

plt.show()

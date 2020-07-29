# MATRIX PLOTS
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
# print(tips.head())

flight = sns.load_dataset('flights')
# print(flight.head())

# In order to create a Heat Map, your data set has to be in a Matrix Form
# We have to make the columns and rows have the same names, this can be done in 2 methods
# ----> By using a piviot table
# ----> By using corr()

# Using corr()
tc = tips.corr()
# print(tc)

# print(sns.heatmap(tc,annot=True))
# print(sns.heatmap(tc,annot=True, cmap='coolwarm'))

# Using pivot_table
fp = flight.pivot_table(index='month', columns='year', values='passengers')
# print(fp)
# print(sns.heatmap(fp))
# print(sns.heatmap(fp,cmap='magma'))
# print(sns.heatmap(fp,linecolor='white', linewidths=2))

# Cluster Map
# print(sns.clustermap(fp))
print(sns.clustermap(fp,cmap='coolwarm', standard_scale=1))
plt.show()

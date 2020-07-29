import seaborn as sns
import matplotlib.pyplot as plt

# GRIDS

iris = sns.load_dataset('iris')
# print(iris.head())

# print(sns.pairplot(iris)) # we get a number of graphs, which includes ( upper diagonal, lower diagonal, main diagonal )
# print(sns.PairGrid(iris))   # you basically get a number of EMPTY grids
g = sns.PairGrid(iris)
# print(g.map(plt.scatter))
# print(g.map_diag(sns.distplot))
# print(g.map_upper(plt.scatter))
# print(g.map_lower(sns.kdeplot))
# plt.show()

tips = sns.load_dataset('tips')
g = sns.FacetGrid(data=tips, col='time',row='smoker')
# print(g.map(sns.distplot, 'total_bill'))
# print(g.map(plt.scatter, 'total_bill', 'tip'))


plt.show()
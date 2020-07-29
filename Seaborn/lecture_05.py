# Regression Plots
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
print(tips.head())

# graph = sns.lmplot(x='total_bill', y='tip',data=tips,hue='sex',markers=['o','v'], scatter_kws={'s':30})
# print(graph)

# Instead of separating sex by color we can separate by column
# graph = sns.lmplot(x='total_bill', y='tip',data=tips,col='sex')
# print(graph)

# You can add rows as well
# print(sns.lmplot(x='total_bill', y='tip',data=tips,col='sex',row='time'))

# print(sns.lmplot(x='total_bill', y='tip',data=tips,hue='sex', col='day'))
plt.show()
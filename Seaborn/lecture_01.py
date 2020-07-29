# Statistical plotting library
# Using beautiful styles
# Works very well with panda data objects

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
print(tips.head())

sns.distplot(tips['total_bill'], kde=False,bins=60)

sns.jointplot(x='total_bill',y='tip',data=tips)
sns.jointplot(x='total_bill',y='tip',data=tips,kind='hex')
sns.jointplot(x='total_bill',y='tip',data=tips, kind='reg')
sns.jointplot(x='total_bill',y='tip',data=tips, kind='kde')
#
sns.pairplot(tips, hue='smoker')

sns.rugplot(tips['total_bill'])
sns.kdeplot(tips['total_bill'])
plt.show()

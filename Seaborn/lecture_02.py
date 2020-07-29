# CATEGORICAL PLOT
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

tips = sns.load_dataset('tips')
print(tips.head())

# sns.barplot(x='sex', y='total_bill', data=tips)              # by default the estimate is set to the aggregate function of calculating the mean
# sns.barplot(x='sex', y='tip', data=tips, estimator=np.std)   # we set the estimator function into standard deviation
#
# sns.countplot(x='sex', data=tips)# for countplot the y axis is by default set to count which represents the number of elements which is set for the x-axis
#
# sns.boxplot(x='day', y='total_bill', data=tips)
# sns.boxplot(x='day', y='total_bill', data=tips, hue='smoker')   # we can use hue and add another category to show some distribution
#
# sns.violinplot(x='day', y='total_bill', data=tips)
# sns.violinplot(x='day', y='total_bill', data=tips, hue='smoker', split=True)# in violinplot also we can use hue but there is something special we can combine half of both the graphs given when hue is used by split to make it easier to see and read

# sns.stripplot(x='day', y='total_bill', data=tips)
# sns.stripplot(x='day', y='total_bill', data=tips, hue='sex', split=True)

# sns.swarmplot(x='day', y='total_bill', data=tips)# swarmplot is where the striplot gets the shape of a violinplot

# we can merge a striplot and violinplot to analyse data
# sns.violinplot(x='day', y='total_bill', data=tips)
# sns.swarmplot(x='day', y='total_bill', data=tips, color='black')# swarmplot is where the striplot gets the shape of a violinplot

# factor plot a General plot method where you can use it to build any plot
# sns.factorplot(x='day', y='total_bill', data=tips, kind='violin')
# sns.factorplot(x='day', y='total_bill', data=tips, kind='bar')
# sns.factorplot(x='day', y='total_bill', data=tips, kind='strip')

plt.show()
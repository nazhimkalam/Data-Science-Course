# Style and Colour
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
# sns.set_style('whitegrid')
# # plt.figure(figsize=(12, 3))
# sns.countplot(x='sex', data=tips)
# sns.set_context('poster', font_scale=1.0)
# sns.despine()
graph = sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex',palette='seismic')
graph.savefig('png', dpi=300)
# plt.show()
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
data1=np.random.normal(0,1,100)
data2=np.random.normal(5,2,200)
data3=np.random.normal(13,3,300)

fig, ax = plt.subplots(figsize=(7,7))

xticks = np.arange(3)

violin = ax.violinplot([data1,data2,data3],showmeans=True, positions=xticks)

ax.set_xticks(xticks)
ax.set_xticklabels(['setosa','versicolor','virginica'])
ax.set_xlabel('Species',fontsize=15)
ax.set_ylabel('Values',fontsize=15)

violin['bodies'][0].set_facecolor('blue')
violin['bodies'][1].set_facecolor('red')
violin['bodies'][2].set_facecolor('red')

violin['cbars'].set_edgecolor('gray')
violin['cmaxes'].set_edgecolor('gray')
violin['cmins'].set_edgecolor('gray')
violin['cmeans'].set_edgecolor('gray')

plt.show()
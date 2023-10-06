import matplotlib.pyplot as plt
import numpy as np

plt.style.use("seaborn-v0_8")

n_student = 100
math_scores = np.random.normal(loc=50, scale=10,size=(100,1))
chem_scores = np.random.normal(loc=70, scale=10, size=(n_student, 1))
phy_scores = np.random.normal(loc=30, scale=12, size=(n_student, 1))
pro_scores = np.random.normal(loc=80, scale=5, size=(n_student, 1))

data = np.hstack((math_scores, chem_scores, phy_scores, pro_scores))

medianprops = {'linewidth':1.5, 'color':'tab:red'}
boxprops = {'linewidth':1.5,'color':'k','alpha':0.7}
whiskerprops = {'linestyle':'--','color':'tab:blue','alpha':0.8}
labels = ['Math','English','Physics','Programming']

fig, axes = plt.subplots(2,1,figsize=(15,10))
axes[0].boxplot(data)
axes[1].violinplot(data)

axes[0].set_ylim([0,100])
axes[1].set_ylim([0,100])
axes[0].tick_params(labelsize=20,
                    bottom=False, labelbottom=False)
axes[1].tick_params(labelsize=20)
fig.subplots_adjust(hspace=0.1)

plt.show()
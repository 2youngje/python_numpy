import matplotlib.pyplot as plt
figsize = (7,7)
fig,ax = plt.subplots(figsize=figsize)

ax.set_xlabel("X label", fontsize = 20)
ax.set_ylabel("Y label", fontsize = 20)

ax.set_title("Title of a Ax", fontsize=30, fontfamily = 'monospace')

fig.show()
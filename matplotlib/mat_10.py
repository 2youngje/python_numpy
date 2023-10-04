import numpy as np
import matplotlib.pyplot as plt

PI = np.pi
t = np.linspace(-4*PI, 4*PI, 300)
sin = np.sin(t)

fig, ax = plt.subplots(figsize=(10,10))

for ax_idx in range(12):
    label_template = 'added by {}'
    ax.plot(t,sin+ax_idx,
            label=label_template.format(ax_idx))
ax.legend(fontsize=15,
          ncol=4,
          bbox_to_anchor=(0.5,0.05),
          loc = 'upper center')
plt.show()
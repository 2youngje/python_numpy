import numpy as np
import matplotlib.pyplot as plt

fig,ax = plt.subplots(figsize=(5,5))

ax.set_xlim([-5,5])
ax.set_ylim([-5,5])

ax.axvline(x=1,
           color='black',
           linewidth=1)

ax.axvline(x=1,
           ymax=0.8, ymin=0.2,
           color = 'yellow',
           linewidth = 1)

plt.show()
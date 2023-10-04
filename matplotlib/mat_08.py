import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4*np.pi,4*np.pi,200)
sin = np.sin(x)

fig,ax = plt.subplots(figsize=(10,5))
ax.plot(x,sin)
ax.axhline(y=1, ls=':',lw=1, color = 'gray')
ax.axhline(y=-1, ls=':',lw=1, color = 'gray')

plt.show()
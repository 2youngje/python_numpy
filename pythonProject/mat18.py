import matplotlib.pyplot as plt
import numpy as np

n_data = 10
x_data = np.linspace(0,10,n_data)
y_data = np.linspace(0,10,n_data)

s_arr = np.linspace(10,400,n_data)

fig,ax =plt.subplots(figsize=(10,10))
ax.scatter(x_data,y_data,s=s_arr)

plt.show()
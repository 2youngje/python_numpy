import matplotlib.pyplot as plt
import numpy as np

n_data = 10
x_data = np.linspace(0,10,n_data)
y_data = np.linspace(0,10,n_data)

# 색이 점차 흐려지는 모노 톤으로 색을 주는 것.
c_arr = [(c/n_data,c/n_data,c/n_data)for c in range(n_data)]

fig,ax =plt.subplots(figsize=(10,10))
ax.scatter(x_data,y_data,
           s=500,
           c=c_arr)

plt.show()
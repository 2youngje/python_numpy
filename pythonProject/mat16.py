import matplotlib.pyplot as plt
import numpy as np

# seed를 박아줌 : 고정하고 싶을 때
np.random.seed(0)

n_data = 100
x_data = np.random.normal(0,1,(n_data))
y_data = np.random.normal(0,1,(n_data))

fig, ax = plt.subplots(figsize=(7,7))
ax.scatter(x_data,y_data,s=100,color='r')

plt.show()
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8")

fig, ax = plt.subplots(figsize=(10,5))

uniform = np.random.uniform(low=-10,high=10,size=(1000,))
ax.hist(uniform)
print(uniform.shape)

plt.show()
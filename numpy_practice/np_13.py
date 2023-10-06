import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10,5))

uniform = np.random.rand(1000)
ax.hist(uniform)
print(uniform.shape)

plt.show()
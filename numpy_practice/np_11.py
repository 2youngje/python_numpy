import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots(figsize=(10,5))

random_values = np.random.randn(300)
ax.hist(random_values,bins=20)
print(random_values.shape)
import matplotlib.pyplot as plt
import numpy as np

n_student = 100
math_scores = np.random.normal(loc=50,scale=10,size=(100,))

fig, ax = plt.subplots(figsize=(7,7))
ax.boxplot(math_scores,
           notch=True,
           showfliers=False,
           vert=False)
plt.show()
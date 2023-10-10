<<<<<<< HEAD
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

n_data = 500

data = np.random.normal(0,1,(n_data,))

fig, ax = plt.subplots(figsize=(14,10))

ax.tick_params(labelsize=30,
               length=10,
               width=3)

ax.hist(data, rwidth=0.9)

import matplotlib.pyplot as plt
import numpy as np

n_student = 100
math_scores = np.random.normal(loc=50,scale=10,size=(100,))
#loc = 평균 scale = 표준편차 size = 표 크

fig,ax = plt.subplots(figsize=(7,7))
ax.boxplot(math_scores)

plt.show()
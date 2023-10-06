import matplotlib.pyplot as plt
import numpy as np

n_student = 100
math_scores = np.random.normal(loc=50,scale=10,size=(100,))
#loc = 평균 scale = 표준편차 size = 표 크

fig,ax = plt.subplots(figsize=(7,7))
ax.boxplot(math_scores)

plt.show()
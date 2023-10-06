# ex7. hstack 사용해서 행렬 붙이기
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(7,7))

n_student = 100
math_scores = np.random.normal(loc=50, scale=10,size=(100,1))
chem_scores = np.random.normal(loc=70, scale=10, size=(n_student, 1))
phy_scores = np.random.normal(loc=30, scale=12, size=(n_student, 1))
pro_scores = np.random.normal(loc=80, scale=5, size=(n_student, 1))

data = np.hstack((math_scores, chem_scores, phy_scores, pro_scores))

fig, ax = plt.subplots(figsize=(10,7))
ax.set_ylim([0,100])

ax.boxplot(data,
           notch=True)

plt.show()
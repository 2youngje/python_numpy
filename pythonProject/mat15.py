import matplotlib.pyplot as plt
import numpy as np

# seed를 박아줌 : 고정하고 싶을 때
np.random.seed(0)

n_data = 100
x_data = np.random.normal(0,1,(n_data))
y_data = np.random.normal(0,1,(n_data))

fig, ax = plt.subplots(figsize=(7,7))
# ax.scatter(x_data,y_data)

#scatter 처럼 사용하고 싶을 때는 뒤에 'o'를 입력
ax.plot(x_data,y_data,'o')

plt.show()
import numpy as np

a = np.arange(24).reshape((-1,3,4))
u = np.arange(0,120,10).reshape((3,4))
b = a+u

print(b)
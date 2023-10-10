import numpy as np
#reshape -> 모양을 바꿔줌
a = np.arange(6)
b = np.reshape(a,(2,3))

print("original ndarray: \n",a)
print("reshaped ndarray: \n",b)
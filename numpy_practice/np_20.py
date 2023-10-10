#numpy_broardcasting
import numpy as np

A = np.arange(3).reshape((3,-1))
B = 10*np.arange(3).reshape((-1,3))
C = A + B

print(A,'\n')
print(B,'\n')
print(C)
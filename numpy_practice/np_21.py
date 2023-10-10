import numpy as np
#numpy broardcasting _ practice

A = np.arange(18).reshape((-1,3,3))
B = 10*np.arange(9).reshape((-1,3,3))
C = A + B

print(A,'\n')
print(B,'\n')
print(C)
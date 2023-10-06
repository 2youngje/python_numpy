import numpy as np
#flatten을 통해 다시 벡터로 만듦.
M = np.arange(9)
N = M.reshape((3,3))
O = N.flatten()

print(M,'\n')
print(N,'\n')
print(O,'\n')
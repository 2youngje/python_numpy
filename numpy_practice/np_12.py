import numpy as np

normal = np.random.normal(loc=[-2,0,3],
                          scale=[1,2,5], #표준편차
                          size=(200,3))
print(normal)
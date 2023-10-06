# 차원이 다른 것 끼리 broardcasting
import numpy as np

a = np.array(3)
u = np.arange(5)

print(f"shapes : {a.shape}/{u.shape}")
print("a: ",a)
print("u: ",u,'\n')

print("a*u: ", a*u)
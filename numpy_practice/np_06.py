#1차원, 2차원, 3차
import numpy as np

scalar_np = np.array(3.14)
vec_np = np.array([1,2,3])
mat_np = np.array([[1,2],[3,4]])
tensor_np = np.array([[[1,2,3],
                       [4,5,6]],
                      [[11,12,13],
                       [14,15,16]]])

print(scalar_np)
print(vec_np)
print(mat_np)
print(tensor_np)#1차원, 2차원, 3차
import numpy as np

scalar_np = np.array(3.14)
vec_np = np.array([1,2,3])
mat_np = np.array([[1,2],[3,4]])
tensor_np = np.array([[[1,2,3],
                       [4,5,6]],
                      [[11,12,13],
                       [14,15,16]]])

print(scalar_np.shape)# shape로 스칼라인지 어떤 모양의 벡터인지를 알 수 있음.
print(vec_np.shape)
print(mat_np.shape)
print(tensor_np.shape)
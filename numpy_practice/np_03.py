#배열의 속성을 dir 함수로 뽑아냄
import numpy as np

a = np.array([1,2,3])
for attr in dir(a):
    print(attr)
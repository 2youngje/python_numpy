# 벡터의 원소 값을 더해 봐라.
u = [1,2,3]
v = [4,5,6]

w = u+v
print(w)

u_1 = [1,2,3]
v_1 = [4,5,6]

w_1 = []

for i in range(len(u_1)):
    w_1.append(u_1[i]+v_1[i])

print(w_1)
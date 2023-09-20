v1 = [1,2,3]

# 제곱의 합 초기값
square_sum = 0

# dim_val을 주고 v1 리스트까지 하는 for문을 만듦
for dim_val in v1:
# 제곱의 합을 정의 하는 것
    square_sum += dim_val**2
# norm이라는 변수를 주고 제곱의 합에 루트를 씌어줌(루트는 1/2제곱을 말함)
norm = square_sum**0.5
#v1의 norm 값을 줌.
print("norm of v1: ", norm)

for dim_idx in range(len(v1)):
    v1[dim_idx] /= norm

# 제곱의 합 초기값
square_sum = 0

# dim_val을 주고 v1 리스트까지 하는 for문을 만듦
for dim_val in v1:
# 제곱의 합을 정의 하는 것
    square_sum += dim_val**2
# norm이라는 변수를 주고 제곱의 합에 루트를 씌어줌(루트는 1/2제곱을 말함)
norm = square_sum**0.5
#v1의 norm 값을 줌.

print("norm of v1: ",norm)
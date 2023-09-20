#리스트를 설정해줌
v1, v2 = [1,2,3],[3,4,5]

#dot_prod라는 초기 값을 설정해줌
dot_prod = 0
#dim_idx라는 변수를 만들고 v1의 길이 까지 범위를 준다.
for dim_idx in range(len(v1)):
#총 3번을 돈다 v1의 길이가 3이기 때문에 0,1,2를 돈다.
#dot_prod는 v1*v2의 각각의 원소 값이 더해진다.
#1*3 = 3, 2*4 = 8, 3*5 = 15로 나온 모든 값의 곱을 더해준다.
    dot_prod += v1[dim_idx]*v2[dim_idx]
print("dot product of v1 and v2: ",dot_prod)
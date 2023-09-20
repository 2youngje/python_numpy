#Euclidean Distance
# 두 점사이의 거리를 말하는 것, 피타고라스의 정리를 활용할 수 있는 것
#리스트를 설정해줌
v1, v2 = [1,2,3],[3,4,5]

#diff_square_sum의 값을 설정해줌
diff_square_sum = 0
for dim_idx in range(len(v1)):
# 두 점사이의 거리를 구하는 피타고라스의 정리를 사용한 것 x축, y축, z축의 거리를 가지고 하는 것.
    diff_square_sum += (v1[dim_idx]-v2[dim_idx])**2
#e_distance를 설정하고 합의 제곱을 선언
e_distance =  diff_square_sum**0.5

#ㅇㅇㅇ
print("Euclidean distance between v1 and v2: ",e_distance)
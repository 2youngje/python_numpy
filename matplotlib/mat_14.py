def euclidean_distance(A,B):
    distance = 0
    for i in range(len(A)):
        distance += (A[i]-B[i])**2
    return distance ** 0.5

#d12,d5의 유클리드 거리
print(f"d12와 d5의 유클리드 거리 : {euclidean_distance(A=[5,2.5],B=[2.75,7.5])}")

def manhattan_distance(a,b):
    distance = 0
    for i in range(len(a)):
        distance += abs(a[i]-b[i])
    return distance

#d12, d5의 멘하탄 거리
print()
print(f"d12와 d5의 멘하탄 거리 : {manhattan_distance(a=[5,2.5],b=[2.75,7.5])}")